class CMD_help:
    # This is the help command class
    # Command name
    name = "help"
    aliases = ["h", "?"]
    description = "Provides help information for available commands."

    help_result_dict = {}
    # Command execution method
    def execute(self, context, flags=None, args=None):
        global help_result
        for key, value in context.lookup_command.items():
            if value.aliases:
                self.help_result_dict[key] = {
                    "Description": value.description,
                    "Aliases": value.aliases
                }
            else:
                self.help_result_dict[key] = {
                    "Description": value.description
                }
        return self.help_result_dict
