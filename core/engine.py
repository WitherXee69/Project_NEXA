from core.parser.parser import parser
from frontend.renderer import Renderer
from core.parser.schema_helper import Schema_Helper
from core.error_handler import *

renderer = Renderer()
schema_helper = Schema_Helper()

class Engine:
    def __init__(self, registry, contexts):
        self.registry = registry
        self.context = contexts

        # Link engine to contexts
        contexts.engine = self

    def handle_directives(self, directive, args):
        if directive.upper() == "@VERBOSE" or directive.upper() == "@ECHO":
            if args and args[0].upper() == "OFF":
                self.context.verbose_mode = False
                renderer.render(result="Verbose mode disabled.\n")
                # print("off")
            elif args and args[0].upper() == "ON":
                if self.context.verbose_mode:
                    renderer.render(result="Verbose mode is already enabled.\n")
                    return
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
        cmd, tail_flags = parser(input_str)

        try:
            if not cmd:
                raise NoCommandError

            # Retrieve the command from the registry and execute it
            command = self.registry.get_cmd(cmd, self.context)
            if command:
                flags, args, error = schema_helper.helper(command, tail_flags)
                if error:
                    return error
                return command.execute(self.context, flags, args)

            # Built-in clear command
            elif cmd == "clear" or cmd == "cls":
                renderer.clear()
                return None

            # Built-in exit command
            elif cmd == "exit":
                renderer.render(result="Shutting down NEXA...")
                self.context.exit_state = True
                return None

            elif cmd.startswith("@"):
                self.handle_directives(cmd, tail_flags)
                return ""  # Ignore directives

            else:
                raise CommandNotFoundError(cmd)

        except NoCommandError as e:
            return e.message
        except CommandNotFoundError as e:
            return e.message