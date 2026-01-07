from core.parser import parser

class Engine:
    def __init__(self, registry, contexts):
        self.registry = registry
        self.context = contexts

        contexts.engine = self

    def handler(self, input_str):
        # Parse the input string to get command and arguments
        cmd, flags, args = parser(input_str)

        # Retrieve the command from the registry and execute it
        command = self.registry.get_cmd(cmd, self.context)
        if command:
            return command.execute(self.context, flags, args)
        else:
            return f"Unknown command: {cmd}"