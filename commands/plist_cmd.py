import psutil
import tabulate

class CMD_plist:
    # This is the plist command class
    # Command name
    name = "plist"
    aliases = ["ps", "tasklist"]
    description = "Shows a list of all processes running on the system."
    schema = None # No flags for this command, just arguments
    need_paths = False

    # Command execution method
    def execute(self, context, flags, args):
        header = "Currently running processes:"
        theaders = {"pid": "PID", "name": "Name", "username": "Username"}

        processes = []

        for proc in psutil.process_iter(['pid', 'name', 'username']):
            try:
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "username": proc.info['username'] if proc.info['username'] else "Unknown"
                })

            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        if processes:
            table = tabulate.tabulate(processes, headers=theaders, tablefmt="fancy_outline")
            return header + "\n" + table
        