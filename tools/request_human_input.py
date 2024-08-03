from langchain_core.tools import tool

@tool
def request_human_input(prompt: str) -> str:
    """Request human input via Python's input method."""
    print(prompt)
    return input("> ")
