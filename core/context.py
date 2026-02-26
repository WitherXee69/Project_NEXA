from pathlib import Path
import psutil

class Context:
    def __init__(self):
        # Engine instance
        self.engine = None

        # Exit state
        self.exit_state = False

        # Get the current working directory
        self.cwd = Path.cwd()
        # Get the user's home directory
        self.home = Path.home()

        self.netinfo = psutil.net_if_addrs()

        # Available commands and their aliases
        self.command_list = {}
        # Available commands for lookup (name)
        self.lookup_command = {}
        
        # Metadata storage
        self.metadata = {}
        self.default_metadata = {
            "name":"NEXA Shell",
            "version":"Unknown",
            "codename":"Unknown",
            "channel":"Unknown",
            "min_python_ver":"3.10"
        }

        # Directive states
        # Verbose/Echo mode
        self.verbose_mode = True