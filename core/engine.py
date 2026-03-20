from core.parser.parser import parser
from ui.renderer import Renderer
from core.parser.schema_helper import Schema_Helper
from core.error_handler import *

from pathlib import Path

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
                if args[0].startswith("$"):
                    var_name = args[0][1:]
                    value = None
                    if self.context.user_env_path.exists():
                        with open(self.context.user_env_path, "r") as user_env_file:
                            for line in user_env_file:
                                if line.startswith(f"{var_name}="):
                                    value = line.strip().split("=", 1)[1]
                                    break
                    if value is None and self.context.sys_env_path.exists():
                        with open(self.context.sys_env_path, "r") as sys_env_file:
                            for line in sys_env_file:
                                if line.startswith(f"{var_name}="):
                                    value = line.strip().split("=", 1)[1]
                                    break
                    if value is not None:
                        args[0] = value

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
                if self.context.sys_env_path.exists() or self.context.user_env_path.exists():
                    self.context.sys_env_path.unlink()  # Remove the file on exit
                    self.context.user_env_path.unlink()  # Remove the file on exit
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