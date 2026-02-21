class CMD_help:
    # This is the help command class
    # Command name
    name = "help"

    # Command execution method
    def execute(self, context, flags=None, args=None):
        return f"This is the help command. Available commands are:\n {'\n'.join(context.command_list.keys())}"