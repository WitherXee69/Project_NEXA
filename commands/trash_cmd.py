from pathlib import Path

class CMD_trash:
    # This is the trash command class
    # Command name
    name = "trash"
    aliases = ["rm", "del"]
    description = "Deletes specified files or directories."
    schema = None  # No specific flags or arguments schema for this command(for now)
    need_paths = True

    # Command execution method
    def execute(self, context, flags, args):
        if args:
            for arg in args:
                file_path = Path(arg)
                if file_path.exists():
                    if file_path.is_dir():
                        file_path.rmdir()
                    else:
                        file_path.unlink()
            return "Deleted: " + ", ".join(args)
        return "No files specified for deletion."