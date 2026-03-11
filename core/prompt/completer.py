from prompt_toolkit.completion import Completion, Completer

class NEXACompleter(Completer):
    def __init__(self, context):
        self.context = context

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor
        words = text_before_cursor.split()

        # Get the list of available commands from the context
        available_commands = self.context.lookup_command.keys()
        available_aliases = [alias for cmd in self.context.lookup_command.values() for alias in cmd.aliases]

        if not words:
            for cmd in available_commands:
                yield Completion(cmd, start_position=0)
            return
        
        # Get the current command being typed
        current_command = words[0]

        if len(words) == 1 and not text_before_cursor.endswith(" "):
            # Suggest command names
            for cmd in available_commands:
                if cmd.lower().startswith(current_command.lower()):
                    yield Completion(cmd, start_position=-len(current_command), display=f"{cmd}, {available_aliases}")