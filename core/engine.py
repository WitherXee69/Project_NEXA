from core.parser import parser
from frontend.renderer import Renderer

renderer = Renderer()

class Engine:
    def __init__(self, registry, contexts):
        self.registry = registry
        self.context = contexts

        # Engine directives
        self.verbose = False

        # Link engine to contexts
        contexts.engine = self

    def handle_directives(self, directive):
        if directive[0] == "@VERBOSE" or directive[0] == "@ECHO":
            self.verbose = True

    def run_line(self, input_str):
        response = self.handler(input_str)
        renderer.render(result=response)

    def handler(self, input_str):
        # Parse the input string to get command and arguments
        cmd, flags, args = parser(input_str)

        # Retrieve the command from the registry and execute it
        command = self.registry.get_cmd(cmd, self.context)
        header = f"\nExecuting command:{input_str}"
        if command:
            if self.verbose:
                return header + command.execute(self.context, flags, args)
            else:
                return command.execute(self.context, flags, args)
        else:
            return f"Unknown command: {cmd}"