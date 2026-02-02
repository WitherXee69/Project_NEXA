from pathlib import Path

class CMD_forge:
    # This is the forge command class
    # Command name
    name = "forge"
    aliases = ["touch"]

    # Command execution method
    def execute(self, context, flags, args):
        modes = None
        if args:
            if flags:
                for flag in flags:
                    if flag in ["-t", "--time"]:
                        modes = "time"
                    elif 
                for arg in args:
                    file_path = Path(context.cwd) / arg