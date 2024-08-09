from langchain_core.tools import tool

@tool
def overwrite_file(file_path: str, content: str) -> str:
    """Replaces the file at the given path with the given content, returning a string message confirming success."""
    with open(file_path, 'w') as file:
        file.write(content)
    return f"File at {file_path} has been successfully overwritten."