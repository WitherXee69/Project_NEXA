import shutil
from pathlib import Path

from ui.renderer import Renderer

renderer = Renderer()


def normalize(parsed_flags):
    FORCE_FLAGS = {"-f", "--force", "/F"}
    RECURSIVE_FLAGS = {"-r", "-R", "--recursive", "/S"}
    INTERACTIVE_FLAGS = {"-i", "--interactive", "/P"}
    INTERACTIVE_OFF_FLAGS = {"/Q"}
    DIR_ONLY_FLAGS = {"-d", "--directory"}
    VERBOSE_FLAGS = {"-v", "--verbose"}

    norm_map = {"force": False,
                "recursive": False,
                "interactive": "auto",
                "dir_only": False,
                "verbose": False}

    for flag in parsed_flags:
        if flag in FORCE_FLAGS:
            norm_map["force"] = True
        elif flag in RECURSIVE_FLAGS:
            norm_map["recursive"] = True
        elif flag in INTERACTIVE_FLAGS:
            norm_map["interactive"] = "always"
        elif flag in INTERACTIVE_OFF_FLAGS:
            norm_map["interactive"] = "never"
        elif flag in DIR_ONLY_FLAGS:
            norm_map["dir_only"] = True
        elif flag in VERBOSE_FLAGS:
            norm_map["verbose"] = True

    return norm_map


class CMD_trash:
    # This is the trash command class
    # Command name
    name = "trash"
    aliases = ["rm", "del"]
    description = "Deletes specified files or directories."
    schema = {"-f": "bool", "--force": "bool", "/F": "bool",    # Force deletion without confirmation and ignore errors
              "-r": "bool", "-R": "bool", "--recursive": "bool", "/S": "bool",  # Recursively delete directories and their contents
              "-i": "bool", "--interactive": "bool", "/P": "bool",  # Prompt before each deletion
              "/Q": "bool",  # Quiet mode (no prompts)
              "-d": "bool", "--directory": "bool",  # Only delete directories, skip files
              "-v": "bool", "--verbose": "bool",
              "-help": "bool", "/?": "bool",}
    need_paths = True

    # Command execution method
    def execute(self, context, flags, args):
        norm_map = normalize(flags)

        def recursive_rm(target, map):
            items = list(target.rglob("*"))
            if map["verbose"]:
                renderer.render(f"Preparing to delete {target}...")
                for item in items:
                    if item.is_file():
                        renderer.render(f"Deleting file: {item}")
                    elif item.is_dir():
                        renderer.render(f"Deleting directory: {item}")
            try:
                shutil.rmtree(target)
            except Exception as e:
                if not map["force"]:
                    renderer.render(f"\nError during deletion of {target}: {e}")

        def confirmation_deletion(map, target):
            if map["interactive"] == "always":
                response = input(f"Delete {target}? (y/n): ")
                return response.lower() == "y"
            elif map["interactive"] == "never":
                return True
            else:
                return True

        def delete_target(target, map):
            try:
                if target.is_dir():
                    if map["recursive"]:
                        recursive_rm(target, map)
                    else:
                        renderer.render(f"\nThe {target} is not empty. Try using (-r, -R, /S) flags for recursive delete.")
                else:
                    target.unlink()
                if map["verbose"]:
                    renderer.render(f"Deleted '{target}'")
            except Exception as e:
                if not map["force"]:
                    renderer.render(f"Error deleting '{target}': {e}")


        if args:
            for arg in args:
                target_path = Path(context.cwd) / arg
                if not target_path.exists() and not norm_map["force"]:
                    renderer.render(f"File or directory '{target_path}' does not exist.")
                    continue

                if norm_map["dir_only"] and not target_path.is_dir():
                    renderer.render(f"'{target_path}' is not a directory. Skipping.")
                    continue

                if confirmation_deletion(norm_map, target_path):
                    delete_target(target_path, norm_map)