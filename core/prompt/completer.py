from prompt_toolkit.completion import Completion, Completer, PathCompleter


class NEXACompleter(Completer):
    def __init__(self, context):
        self.context = context

    def get_completions(self, document, complete_event):
        text_before_cursor = document.text_before_cursor
        words = text_before_cursor.split()

        # Get the list of available commands from the context
        available_commands = self.context.lookup_command.keys()

        if not words:
            for cmd in available_commands:
                yield Completion(cmd, start_position=0)
            return
        
        # Get the current command being typed
        current_input = words[0]

        if len(words) == 1 and not text_before_cursor.endswith(" "):
            # Suggest command names
            for cmd in available_commands:
                if cmd.lower().startswith(current_input.lower()):
                    yield Completion(cmd, start_position=-len(current_input), display=cmd)
        elif len(words) > 1 and not text_before_cursor.startswith("-"):
            # Suggest file paths for arguments
            path = words[-1]

            path_completer = PathCompleter(get_paths=lambda: [path])
            for completion in path_completer.get_completions(document, complete_event):
                yield completion