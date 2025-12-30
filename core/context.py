from pathlib import Path

class Context:
    def __init__(self):
        # Get the current working directory
        self.cwd = Path.cwd()
        # Get the user's home directory
        self.home = Path.home()

        # Available commands
        self.command_list = {}