from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchResults

@tool
def duck_duck_go_news_search(query: str):
    """Search for news using DuckDuckGo."""
    return DuckDuckGoSearchResults(backend="news").invoke(query)