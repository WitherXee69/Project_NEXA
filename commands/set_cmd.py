from dotenv import set_key
from pathlib import Path

class CMD_set:
    # This is set command class
    # It allows users to set environment variables in either user or system scope, and also provides options for verbose output and showing all environment variables.

    name = "set"
    description = "Sets an environment variable. Usage: set VAR_NAME=VALUE"
    schema = {"-v": "bool", "--verbose": "bool"
              ,"-sys": "bool", "--system": "bool"
              ,"-sh": "bool", "--show": "bool"}
    need_paths = False

    def execute(self, context, flags, args):
        verbose_mode = False
        if not context.user_env_path.exists():
            # Create the file if it doesn't exist
            context.user_env_path.touch()

        if args:
            if len(args) > 1:
                return "Error: Too many arguments. Usage: set VAR_NAME=VALUE"

            var_name, value = args[0].split("=", 1)

            if flags:
                if "-show" in flags or "--show" in flags:
                    env_vars = []
                    if context.sys_env_path.exists():
                        with open(context.sys_env_path, "r") as sys_env_file:
                            env_vars.append("System Environment Variables:")
                            env_vars.extend(sys_env_file.read().splitlines())
                    if context.user_env_path.exists():
                        with open(context.user_env_path, "r") as user_env_file:
                            env_vars.append("User Environment Variables:")
                            env_vars.extend(user_env_file.read().splitlines())
                    return "\n".join(env_vars)

                if "-v" in flags or "--verbose" in flags:
                    verbose_mode = True

                if "-sys" in flags or "--system" in flags and "-show" not in flags and "--show" not in flags:
                    if verbose_mode:
                        set_key(str(context.sys_env_path), var_name, value)
                        return f"System environment variable '{var_name}' set to '{value}'.\nNote: Environment variables are currently session-based."
                    else:
                        set_key(str(context.sys_env_path), var_name, value)
                        return "Note: Environment variables are currently session-based."
                        #return "Done."
                else:
                    if verbose_mode:
                        set_key(str(context.user_env_path), var_name, value)
                        return f"User environment variable '{var_name}' set to '{value}'.\nNote: Environment variables are currently session-based."
                    else:
                        set_key(str(context.user_env_path), var_name, value)
                        return "Note: Environment variables are currently session-based."
                        #return "Done."

            else:
                set_key(str(context.user_env_path), var_name, value)
                return "Note: Environment variables are currently session-based."
                #return f"Done."
        else:
            return "Error: No variable provided. Usage: set VAR_NAME=VALUE"