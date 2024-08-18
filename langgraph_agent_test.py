from agents.langgraph_engineer import langgraph_engineer as agent

state = agent(task="write a react agent with langgraph")
# response = state["messages"][-1].content
# print(response)
print(state)