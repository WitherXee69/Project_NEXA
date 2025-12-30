from pathlib import Path
from colorama import Fore, Style
from tabulate import tabulate
from datetime import datetime

class CMD_scan:
    # This is the scan command class
    # Command name
    name = "scan"
    aliases = ["ls", "list"]

    # Command execution method
    def execute(self, context, flags, args):
        header = f"\nThe file directory of {context.cwd}\n"
        columns = ["name", "type", "size", "modified"]
        dirlist = []
        for p in Path(context.cwd).iterdir():
            stats = p.stat()
            dirlist.append({
                "name" : p.name,
                "is_dir" : p.is_dir(),
                "size" : stats.st_size if not p.is_dir() else "",
                "modified" : datetime.fromtimestamp(stats.st_mtime),
                "created" : datetime.fromtimestamp(stats.st_birthtime),
                "accessed" : datetime.fromtimestamp(stats.st_atime),
            })

        if not args:
            if flags:
                if "-dir" in flags or "-d" in flags:
                    dirlist = [info for info in dirlist if info["is_dir"]]

                elif "-file" in flags or "-fl" in flags:
                    dirlist = [info for info in dirlist if not info["is_dir"]]

                elif "-time" in flags or "-t" in flags:
                    columns.remove("size")
                    if "-a" in flags:
                        columns[-1] = "accessed"
                    elif "-c" in flags:
                        columns[-1] = "created"
                    else:
                        columns.append("created")
                        columns.append("accessed")

                else:
                    return Fore.RED + " [ERROR] " + Style.RESET_ALL + f'Unknow flag "{', '.join(flags)}"'

            dirlist.sort(key=lambda info: (not info["is_dir"], info["name"].lower()))
            rows = []
            for info in dirlist:
                row = []
                for col in columns:
                    if col == "type":
                        row.append("<dir>" if info["is_dir"] else "")
                    else:
                        value = info.get(col)
                        if isinstance(value, datetime):
                            value = value.strftime("%Y-%m-%d %H:%M:%S")
                        row.append(value)
                rows.append(row)

            return header + tabulate(rows, headers=[col.capitalize() for col in columns], tablefmt="fancy_outline")
        return None

