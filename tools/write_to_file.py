import os
from langchain_core.tools import tool

@tool
def write_to_file(file: str, file_contents: str) -> str:
    """Write the contents to a new file, will not overwrite an existing file."""
    if os.path.exists(file):
        raise FileExistsError(f"File {file} already exists and will not be overwritten.")

    print(f"Writing to file: {file}")
    with open(file, 'w') as f:
        f.write(file_contents)

    return f"File {file} written successfully."