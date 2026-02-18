from pathlib import Path

class CMD_construct:
    # This is the construct command class
    # Command name
    name = "construct"
    aliases = ["mkdir"]

    # Command execution method
    def execute(self, context, flags, args):
        if args:
            for arg in args:
                dir_path = Path(arg)
                dir_path.mkdir(parents=True, exist_ok=True)
                return "Directory created: " + str(dir_path)