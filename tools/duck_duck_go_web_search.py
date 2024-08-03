from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def duck_duck_go_web_search(query: str):
    """Search the web using DuckDuckGo."""
    return DuckDuckGoSearchResults().invoke(query)