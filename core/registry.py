class CommandRegistry:
    def get_cmd(self, command, context):
        return context.command_list.get(command)

    def register(self, command, context):
        # Register both command name and aliases
        context.command_list[command.name] = command
        context.lookup_command[command.name] = command
        if hasattr(command, 'aliases'):
            for alias in getattr(command, "aliases", []):
                context.command_list[alias] = command

        # To test the help cmd
        # context.command_list.append(command.name)