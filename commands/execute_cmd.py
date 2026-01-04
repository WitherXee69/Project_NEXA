from core.engine import Engine
from core.registry import CommandRegistry


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
                    with open(arg) as nexa_batch:
                        commands = nexa_batch.readlines()
                        for command in commands:
                            return engine.handler(command)
        return None