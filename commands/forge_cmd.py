from pathlib import Path

class CMD_forge:
    # This is the forge command class
    # Command name
    name = "forge"
    aliases = ["touch"]
    description = "Creates a new file or updates the timestamp of an existing file. Usage: forge [options] <file_path>\nOptions:\n  -t, --time    Update the timestamp of the file without modifying its content."

    # Command execution method
    def execute(self, context, flags, args):
        modes = None
        if args:
            if flags:
                for flag in flags:
                    if flag in ["-t", "--time"]:
                        modes = "time"
                for arg in args:
                    file_path = Path(arg)
                    if modes == "time":
                        if file_path.exists():
                            file_path.touch()
                    else:
                        file_path.touch()