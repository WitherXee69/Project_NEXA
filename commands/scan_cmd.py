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

        def only_files(dirlist):
            return [info for info in dirlist if not info["is_dir"]]
            print(dirlist)

        def only_dirs(dirlist):
            return [info for info in dirlist if info["is_dir"]]

        if not args:
            if flags:
                time_flag = "-time" in flags or "-t" in flags
                time_subflags = {"-a", "-c"}
                used_subflags = time_subflags.intersection(flags)

                if used_subflags and not time_flag:
                    return (
                        Fore.RED
                        + " [ERROR] "
                        + Style.RESET_ALL
                        + "Flags -a / -c can only be used with -time"
                    )
                
                for flag in flags:
                    if flag in ("-file", "-fl"):
                        dirlist = only_files(dirlist)
                    elif flag in ("-dir", "-d"):
                        dirlist = only_dirs(dirlist)
                    elif flag in ("-time", "-t"):
                        columns.remove("size")
                        columns.append("created")
                        columns.append("accessed")
                    elif flag in ("-a"):
                        columns.remove("created")
                        # columns[-1] = "accessed"
                    elif flag in ("-c"):
                        columns.remove("accessed")
                        # columns[-1] = "created"
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

