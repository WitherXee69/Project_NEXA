from enum import Enum, auto

class KeyType(Enum):
    CHAR = auto()
    ENTER = auto()
    BACKSPACE = auto()
    TAB = auto()
    LEFT = auto()
    RIGHT = auto()
    UP = auto()
    DOWN = auto()
    CTRL_C = auto()
    UNKNOWN = auto()

class KeyEvent:
    def __init__(self, key_type: KeyType, value: str | None = None):
        self.key_type = key_type
        self.value = value

class InputDriver:
    def enable_raw_mode(self):
        raise NotImplementedError
    def disable_raw_mode(self):
        raise NotImplementedError
    def read_key(self) -> KeyEvent:
        raise NotImplementedError

def __enter__(self):
    self.enable_raw_mode()
    return self

def __exit__(self, exc_type, exc_val, exc_tb):
    self.disable_raw_mode()

with InputDriver() as input_driver:
    while True:
        key_event = input_driver.read_key()
        if key_event.key_type == KeyType.CTRL_C:
            break
        # Handle other key events here