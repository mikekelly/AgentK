import sys
from typing import Literal
from langchain_openai import ChatOpenAI

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, END
from langgraph.prebuilt import ToolNode

import utils
from tools.list_available_agents import list_available_agents
from tools.assign_agent_to_task import assign_agent_to_task

system_prompt = f"""You are Hermes, an agent that achieves goals for the user.

Your responses must be either an inner monologue or a message to the user.
If you are intending to call tools, then your response must be a succinct summary of your inner thoughts.
Else, your response is a message the user.

You interact with a user in this specific order:
1. Reach a shared understanding on a goal.
2. Think of a detailed plan for how to achieve the goal by creating and orchestrating LangChain agents.
3. Orchestrate agents and coordinate achievement of the goal.
4. Respond to the user once the goal is achieved or if you need their input.

Further guidance:
You have a tool to list available agents.
You have a tool to assign an agent to a task.
Try to use tools as much as possible, rather than asking for the user's input.

There is a special agent, called agent_smith, that is able to create new agents deisgned for a specific kind of task.
If you need an agent that doesn't appear on the list, assign agent_smith the task of creating it.
Once that new agent has been created, you can immediately assign it a task.
Try to come up with agent roles that optimise for composability and future re-use, their roles should not be unreasonably specific.

Here's a list of currently available agents:
{list_available_agents.invoke({})}
"""

tools = [list_available_agents, assign_agent_to_task]

def feedback_and_wait_on_human_input(state: MessagesState):
    # if messages only has one element we need to start the conversation
    if len(state['messages']) == 1:
        message_to_human = "What can I help you with?"
    else:
        message_to_human = state["messages"][-1].content
    
    print(message_to_human)

    human_input = ""
    while not human_input.strip():
        human_input = input("> ")
    
    return {"messages": [HumanMessage(human_input)]}

def check_for_exit(state: MessagesState) -> Literal["reasoning", END]:
    last_message = state['messages'][-1]
    if last_message.content.lower() == "exit":
        return END
    else:
        return "reasoning"

def reasoning(state: MessagesState):
    print()
    print("Hermes is thinking...")
    messages = state['messages']
    tooled_up_model = ChatOpenAI(model="gpt-4o", temperature=0).bind_tools(tools)
    response = tooled_up_model.invoke(messages)
    return {"messages": [response]}

def check_for_tool_calls(state: MessagesState) -> Literal["tools", "feedback_and_wait_on_human_input"]:
    messages = state['messages']
    last_message = messages[-1]
    
    if last_message.tool_calls:
        print("Hermes thought this:")
        print(last_message.content)
        print()
        print("Hermes is acting by invoking these tools:")
        print([tool_call["name"] for tool_call in last_message.tool_calls])
        return "tools"
    else:
        return "feedback_and_wait_on_human_input"

acting = ToolNode(tools)

workflow = StateGraph(MessagesState)
workflow.add_node("feedback_and_wait_on_human_input", feedback_and_wait_on_human_input)
workflow.add_node("reasoning", reasoning)
workflow.add_node("tools", acting)
workflow.set_entry_point("feedback_and_wait_on_human_input")
workflow.add_conditional_edges(
    "feedback_and_wait_on_human_input",
    check_for_exit,
)
workflow.add_conditional_edges(
    "reasoning",
    check_for_tool_calls,
)
workflow.add_edge("tools", 'reasoning')

graph = workflow.compile(checkpointer=utils.checkpointer)

def hermes(uuid: str):
    """Hermes."""
    print("Hermes: starting session with id ", uuid)
    print("Type 'exit' to end the session.")

    return graph.invoke(
        {"messages": [SystemMessage(system_prompt)]},
        config={"configurable": {"thread_id": uuid}}
    )