from core.parser import parser
from frontend.renderer import Renderer

renderer = Renderer()

class Engine:
    def __init__(self, registry, contexts):
        self.registry = registry
        self.context = contexts

        # Link engine to contexts
        contexts.engine = self

    def handle_directives(self, directive, args):
        if directive[0].upper() == "@VERBOSE" or directive[0].upper() == "@ECHO":
            if args and args[0].upper() == "OFF":
                self.context.verbose_mode = False
                renderer.render(result="Verbose mode disabled.\n")
                # print("off")
            elif args and args[0].upper() == "ON":
                self.context.verbose_mode = True
                renderer.render(result="Verbose mode enabled.\n")
                # print("on")

    def run_line(self, input_str):
        response = self.handler(input_str)
        if self.context.verbose_mode:
            header = f"\n Executing command:{response}\n"
            renderer.render(result=header + response)

    def handler(self, input_str):
        # Parse the input string to get command and arguments
        cmd, flags, args = parser(input_str)

        # print(args)

        if not cmd:
            return "Please enter a command."

        # Retrieve the command from the registry and execute it
        command = self.registry.get_cmd(cmd, self.context)
        if command:
            return command.execute(self.context, flags, args)
        
        # Built-in clear command
        elif cmd == "clear" or cmd == "cls":
            renderer.clear()

        # Built-in exit command
        elif cmd == "exit":
            renderer.render(result="Shutting down NEXA...")
            self.context.exit_state = True

        elif cmd.startswith("@"):
            self.handle_directives(cmd.strip().split(), args)
            return "" # Ignore directives

        else:
            return f"Unknown command: {cmd}"