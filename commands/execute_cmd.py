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
        registry = CommandRegistry()
        engine = Engine(registry, context)

        if flags is None:
            if args:
                for arg in args:
                    if Path.exists(arg):
                        with open(arg) as nexa_batch:
                            commands = nexa_batch.readlines()
                            for command in commands:
                                if command in ("@ECHO OFF", "@VERBOSE OFF"):
                                    return engine.handler(command)
                                else:
                                    return f"command line: {command}\n" + engine.handler(command)
                    else:
                        return f"Unknown file: {arg}!"
        return None