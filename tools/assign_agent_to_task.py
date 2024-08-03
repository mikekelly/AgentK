import sys
import traceback
from langchain_core.tools import tool
import utils

@tool
def assign_agent_to_task(agent_name: str, task: str):
    """Assign an agent to a task. This function returns the response from the agent."""
    print(f"Assigning agent {agent_name} to task: {task}")
    # Handle the case where the call to the agent fails (might be a job for the toolmaker)
    try:
        agent_module = utils.load_module(f"agents/{agent_name}.py")
        agent_function = getattr(agent_module, agent_name)
        result = agent_function(task=task)
        del sys.modules[agent_module.__name__]
        response = result["messages"][-1].content
        print(f"{agent_name} responded:")
        print(response)
        return response
    except Exception as e:
        exception_trace = traceback.format_exc()
        error = f"An error occurred while assigning {agent_name} to task {task}:\n {e}\n{exception_trace}"
        print(error)
        return error