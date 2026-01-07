from core.engine import Engine
from core.registry import CommandRegistry
from pathlib import Path


class CMD_execute:
    # This is the execute command class
    # Command name
    name = "execute"
    aliases = ["exec", "run", "script"]

    # Command execution method
    def execute(self, context, flags, args):
