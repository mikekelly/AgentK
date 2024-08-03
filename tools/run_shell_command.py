import subprocess
from langchain_core.tools import tool

@tool
def run_shell_command(command: str):
    """Run a shell command and return the output."""
    print(f"Running shell command: {command}")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return { "stdout": result.stdout, "stderr": result.stderr, "returncode": result.returncode }