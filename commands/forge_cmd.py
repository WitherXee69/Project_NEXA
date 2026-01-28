from pathlib import Path

class CMD_forge:
    # This is the forge command class
    # Command name
    name = "forge"
    aliases = ["touch"]

    # Command execution method
    def execute(self, context, flags, args):
        if args:
            for arg in args:
                file_path = Path(context.cwd) / arg
                try:
                    file_path.touch(exist_ok=True)
                except Exception as e:
                    return f"Error creating file {arg}: {str(e)}"
            return f"File(s) created successfully."