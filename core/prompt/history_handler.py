from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory

def history_handler():
    session = PromptSession(history=InMemoryHistory())
    return session