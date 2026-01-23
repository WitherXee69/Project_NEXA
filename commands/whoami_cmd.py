class CMD_whoami:
    # This is the whoami command class
    # Command name
    name = "whoami"
    aliases = []

    # Command execution method
    def execute(self, context, flags=None, args=None):
        return context.current_user