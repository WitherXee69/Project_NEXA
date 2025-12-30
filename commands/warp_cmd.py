from pathlib import Path
from colorama import Fore, Style


class CMD_warp:
    # This is the warp command class
    # Command name
    name = "warp"
    aliases = ["cd","chdir"]

    # Command execution method
    def execute(self, context, flags, args):
        if not flags:
            if args:
                new_location = Path(args[0])

                if str(new_location).startswith("~"):
                    new_location = context.home / str(new_location)[2:]

                new_location = (context.cwd / new_location).resolve() if not new_location.is_absolute() else new_location

                if not new_location.exists():
                    return Fore.RED + " [ERROR] " + Style.RESET_ALL + f"We couldn't find the location: {new_location}"
                if not new_location.is_dir():
                    return Fore.RED + " [ERROR] " + Style.RESET_ALL + "The given location is not a directory!"

                context.cwd = new_location
            else:
                 context.cwd = context.home

        return None


