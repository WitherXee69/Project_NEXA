import psutil


class CMD_kill:
    name = "kill"
    aliases = ["kill", "taskkill"]
    description = "Terminates a process by PID or name."
    schema = None
    need_paths = False

    def execute(self, context, flags, args):
        target = args.get("target")
        if not target:
            return "Error: No target specified."

        # Try to interpret target as PID
        try:
            pid = int(target)
            proc = psutil.Process(pid)
            proc.terminate()
            return f"Process with PID {pid} has been terminated."
        except ValueError:
            # Not a PID, treat as process name
            killed = []
            for proc in psutil.process_iter(['name']):
                if proc.info['name'] == target:
                    proc.terminate()
                    killed.append(proc.pid)
            if killed:
                return f"Processes named '{target}' with PIDs {killed} have been terminated."
            else:
                return f"No processes named '{target}' found."