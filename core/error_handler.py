class NEXA_Error(Exception):
    """Base class for NEXA exceptions."""
    pass

class CommandNotFoundError(NEXA_Error):
    """Raised when a command is not found in the registry."""
    def __init__(self, command):
        self.command = command
        self.message = f"Command '{command}' not found."
        super().__init__(self.message)

class InvalidFlagError(NEXA_Error):
    """Raised when an invalid flag is provided."""
    def __init__(self, flag):
        self.flag = flag
        self.message = f"Invalid flag: '{flag}'."
        super().__init__(self.message)

class MissingValueError(NEXA_Error):
    """Raised when a value is missing for a flag that requires one."""
    def __init__(self, flag):
        self.flag = flag
        self.message = f"Missing value for flag: '{flag}'."
        super().__init__(self.message)

class DuplicateFlagError(NEXA_Error):
    """Raised when a flag is provided more than once."""
    def __init__(self, flag):
        self.flag = flag
        self.message = f"Duplicate flag: '{flag}'."
        super().__init__(self.message)

class CommandExecutionError(NEXA_Error):
    """Raised when an error occurs during command execution."""
    def __init__(self, command, original_exception):
        self.command = command
        self.original_exception = original_exception
        self.message = f"Error executing command '{command}': {str(original_exception)}"
        super().__init__(self.message)

class NoSchemaError(NEXA_Error):
    """Raised when a command does not have a schema defined."""
    def __init__(self, command):
        self.command = command
        self.message = f"No schema found for command '{command}'."
        super().__init__(self.message)

class NoCommandError(NEXA_Error):
    """Raised when no command is provided."""
    def __init__(self):
        self.message = "No command provided."
        super().__init__(self.message)