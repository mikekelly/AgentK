import sys
import os

sys.path.append(os.path.join(os.getcwd(), 'agents/langgraph-engineer/src'))

from langchain_core.messages import HumanMessage

from langgraph_engineer import agent

def langgraph_engineer(task: str) -> str:
    """Expert in designing and writing langgraph code."""
    return agent.graph.invoke(
        {"messages": [HumanMessage(task)]}
    )