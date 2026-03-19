class CMD_here:
    # This is the cwd(current working directory) command class
    # Command name
    name = "here"
    aliases = ["pwd", "cd"]
    description = "Displays the current working directory."
    schema = None
    need_paths = False

    # Command execution method
    def execute(self, context, flags=None, args=None):
        return f"{str(context.cwd)}"