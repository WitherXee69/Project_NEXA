from pathlib import Path
from datetime import datetime

from frontend.renderer import Renderer

renderer = Renderer()

class CMD_reveal:
    # This is the reveal command class
    # Command name
    name = "reveal"
    aliases = ["cat"]

    metadata = {}

    # Command execution method
    def execute(self, context, flags, args):
        reveal_mode = "normal"
        if args:
            if flags:
                for flag in flags:
                    if flag in ["-m", "--meta"]:
                        reveal_mode = "meta"
                    elif flag in ["-ln", "--lines"]:
                        reveal_mode = "lines"
            try:
                if Path(args[0]).is_dir():
                    return f"{args[0]} is a directory! Please enter a file...\n"
                else:
                    with open(args[0], "r") as file:
                        content = file.read()
            except FileNotFoundError:
                return f"File not found: {args[0]}\n"
            
            if reveal_mode == "normal":
                return f"\nFull reveal of {args[0]}:\n\n{content}\n"
            elif reveal_mode == "meta":
                file_path = Path(args[0])
                metadata = f"File Name: {file_path.name}, File Size (bytes): {file_path.stat().st_size}, Absolute Path: {str(file_path.resolve())}, Parent Directory: {str(file_path.parent)}, Created Time: {datetime.fromtimestamp(file_path.stat().st_birthtime).strftime("%Y-%m-%d %H:%M:%S")}, Modified Time: {datetime.fromtimestamp(file_path.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")}"
                key = f"{file_path.name} >>> Metadata"
                self.metadata[key] = metadata
                return self.metadata
            elif reveal_mode == "lines":
                lines = content.splitlines()
                for i in range(len(lines)):
                    renderer.render(f"{i+1}| {lines[i]}")
                    continue
        elif not args:
            return "Usage: reveal <file_path>\n"