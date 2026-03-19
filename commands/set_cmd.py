from dotenv import set_key
from pathlib import Path

class CMD_set:
    # This is set command class

    name = "set"
    description = "Sets an environment variable. Usage: set VAR_NAME=VALUE"
    schema = {"-v": "bool", "--verbose": "bool"
              ,"-sys": "bool", "--system": "bool"
              ,"-sh": "bool", "--show": "bool"}
    need_paths = False

    def execute(self, context, flags, args):
        verbose_mode = False
        user_define_env_path = Path(context.env_dir / "user_define.env")
        sys_define_env_path = Path(context.env_dir / "sys_define.env")
        if not user_define_env_path.exists():
            # Create the file if it doesn't exist
            user_define_env_path.touch()

        if args:
            if len(args) > 1:
                return "Error: Too many arguments. Usage: set VAR_NAME=VALUE"
            
            var_name, value = args[0].split("=", 1)

            if flags:
                if "-show" in flags or "--show" in flags:
                    env_vars = []
                    if sys_define_env_path.exists():
                        with open(sys_define_env_path, "r") as sys_env_file:
                            env_vars.append("System Environment Variables:")
                            env_vars.extend(sys_env_file.read().splitlines())
                    if user_define_env_path.exists():
                        with open(user_define_env_path, "r") as user_env_file:
                            env_vars.append("User Environment Variables:")
                            env_vars.extend(user_env_file.read().splitlines())
                    return "\n".join(env_vars)

                if "-v" in flags or "--verbose" in flags:
                    verbose_mode = True

                if "-sys" in flags or "--system" in flags and "-show" not in flags and "--show" not in flags:
                    if verbose_mode:
                        set_key(str(sys_define_env_path), var_name, value)
                        return f"System environment variable '{var_name}' set to '{value}'."
                    else:
                        set_key(str(sys_define_env_path), var_name, value)
                        return "Done."
                else:
                    if verbose_mode:
                        set_key(str(user_define_env_path), var_name, value)
                        return f"User environment variable '{var_name}' set to '{value}'."
                    else:
                        set_key(str(user_define_env_path), var_name, value)
                        return "Done."

            else:
                set_key(str(user_define_env_path), var_name, value)
                return f"Done."