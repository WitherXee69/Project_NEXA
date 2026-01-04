class CMD_here:
    # This is the cwd(current working directory) command class
    # Command name
    name = "here"
    aliases = ["pwd", "cd"]

    # Command execution method
    def execute(self, context, flags=None, args=None):
        if flags is None and args is None:
            return f"{str(context.cwd)}"
        return None