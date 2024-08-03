from langchain_core.tools import tool
import utils

@tool
def list_available_agents():
    """List the name of available agents along with the type of task it's designed to be assigned."""
    return utils.all_agents()