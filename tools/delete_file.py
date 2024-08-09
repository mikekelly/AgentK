import os
from langchain_core.tools import tool

@tool
def delete_file(file_path: str) -> str:
    """Deletes the file at the given path and returns a string confirming success."""
    try:
        os.remove(file_path)
        return f"File at {file_path} has been deleted successfully."
    except Exception as e:
        return str(e)
