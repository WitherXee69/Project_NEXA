from prompt_toolkit.completion import Completion, Completer
from pathlib import Path

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

        cmd = current_input.lower()
        command = self.context.lookup_command.get(cmd)

        if len(words) == 1 and not text_before_cursor.endswith(" "):
            # Suggest command names
            for cmd in available_commands:
                if cmd.lower().startswith(current_input.lower()):
                    yield Completion(cmd, start_position=-len(current_input), display=cmd)

        elif command and command.need_paths:
            prefix = "" if text_before_cursor.endswith(" ") else words[-1]
            start_pos = 0 if prefix == "" else -len(prefix)
            # Ensure cwd is a Path
            cwd = Path(self.context.cwd)

            # Resolve directory to search
            p = Path(prefix)

            # Special case: path ends with '/'
            if prefix.endswith("/"):
                dirname = (Path(self.context.cwd) / p).resolve()
                name_prefix = ""
                base = p
            else:
                dirname = (Path(self.context.cwd) / p.parent).resolve() if prefix else Path(self.context.cwd)
                name_prefix = p.name if prefix else ""
                base = p.parent

            try:
                for entry in dirname.iterdir():
                    if entry.name.startswith(name_prefix):
                        name = entry.name

                        # Build correct completion text
                        if base != Path("."):
                            complete_path = (base / name).as_posix()
                        else:
                            complete_path = name

                        if Path(complete_path).is_dir():
                            completion = complete_path + "/"
                        else:
                            completion = complete_path

                        yield Completion(
                            completion,
                            start_position=start_pos,
                            display=name
                        )
            except Exception:
                pass