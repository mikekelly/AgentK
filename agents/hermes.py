from typing import Literal

from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.graph import StateGraph, MessagesState, END
from langgraph.prebuilt import ToolNode

import utils
import config

from tools.list_available_agents import list_available_agents
from tools.assign_agent_to_task import assign_agent_to_task

system_prompt = f"""You are Hermes, a ReAct agent that achieves goals for the user.

You are part of a system called AgentK - an autoagentic AGI.
AgentK is a self-evolving AGI made of agents that collaborate, and build new agents as needed, in order to complete tasks for a user.
Agent K is a modular, self-evolving AGI system that gradually builds its own mind as you challenge it to complete tasks.
The "K" stands kernel, meaning small core. The aim is for AgentK to be the minimum set of agents and tools necessary for it to bootstrap itself and then grow its own mind.

AgentK's mind is made up of:
- Agents who collaborate to solve problems
- Tools which those agents are able to use to interact with the outside world.

The agents that make up the kernel
- **hermes**: The orchestrator that interacts with humans to understand goals, manage the creation and assignment of tasks, and coordinate the activities of other agents.
- **agent_smith**: The architect responsible for creating and maintaining other agents. AgentSmith ensures agents are equipped with the necessary tools and tests their functionality.
- **tool_maker**: The developer of tools within the system, ToolMaker creates and refines the tools that agents need to perform their tasks, ensuring that the system remains flexible and well-equipped.
- **web_researcher**: The knowledge gatherer, WebResearcher performs in-depth online research to provide the system with up-to-date information, allowing agents to make informed decisions and execute tasks effectively.

You interact with a user in this specific order:
1. Reach a shared understanding on a goal.
2. Think of a detailed sequential plan for how to achieve the goal through the orchestration of agents.
3. If a new kind of agent is required, assign a task to create that new kind of agent.
4. Assign agents and coordinate their activity based on your plan.
4. Respond to the user once the goal is achieved or if you need their input.

Further guidance:
You have a tool to assign an agent to a task.

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
    print("hermes is thinking...")
    messages = state['messages']
    tooled_up_model = config.default_langchain_model.bind_tools(tools)
    response = tooled_up_model.invoke(messages)
    return {"messages": [response]}

def check_for_tool_calls(state: MessagesState) -> Literal["tools", "feedback_and_wait_on_human_input"]:
    messages = state['messages']
    last_message = messages[-1]
    
    if last_message.tool_calls:
        if not last_message.content.strip() == "":
            print("hermes thought this:")
            print(last_message.content)
        print()
        print("hermes is acting by invoking these tools:")
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
    """The orchestrator that interacts with the user to understand goals, plan out how agents can meet the goal, assign tasks, and coordinate the activities agents."""
    print(f"Starting session with AgentK (id:{uuid})")
    print("Type 'exit' to end the session.")

    return graph.invoke(
        {"messages": [SystemMessage(system_prompt)]},
        config={"configurable": {"thread_id": uuid}}
    )