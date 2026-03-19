import json
import os
from pathlib import Path
from prompt_toolkit import PromptSession
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.shortcuts import CompleteStyle

from core.engine import Engine
from core.registry import CommandRegistry
from core.context import Context
from core.dynamic_importer import DynamicImporter

from core.prompt.completer import NEXACompleter
from core.prompt.provider import PromptProvider

from ui.cli import frontend_cli
from ui.renderer import Renderer


def nexa(registry, context, renderer, prompt):
    # Register commands (this would typically be more dynamic)
    importer = DynamicImporter()
    imported_modules = importer.dynamic_import('commands', {})
    classes = importer.get_classes_from_module(imported_modules)

    for class_name, cls in classes.items():
        if hasattr(cls, 'execute'):
            registry.register(cls(), context)

    # print(registry.command_registry)

    completer = NEXACompleter(context)
    session = PromptSession(history=InMemoryHistory(), 
                            complete_while_typing=False, 
                            complete_style=CompleteStyle.READLINE_LIKE)

    # Start the frontend CLI
    engine = Engine(registry, context)
    while not context.exit_state:
        frontend_cli(engine, renderer, prompt, context, completer, session)

def main():
    # Initialize core components
    registry = CommandRegistry()
    context = Context()
    renderer = Renderer()

    prompt = PromptProvider()

    sys_env_path = Path(context.env_dir / "sys_define.env")
    if not sys_env_path.exists():
        with open(sys_env_path, "w") as sys_env_file:
            for key, value in os.environ.items():
                sys_env_file.write(f"{key}={value}\n")

    try:
        with open(fr"data\\meta.json", "r") as metafile:
            metadata = json.load(metafile)
            context.metadata = metadata
    except FileNotFoundError:
        context.metadata = context.default_metadata
    try:
        print("\033c", end="")
        print(f"""NEXA Shell [Version {context.metadata["version"]}]
by WitherXee. All rights reserved.\n""")

        nexa(registry, context, renderer, prompt)
    except (KeyboardInterrupt, EOFError):        
        if sys_env_path.exists():
            sys_env_path.unlink()  # Remove the file on exit
        print("\nShutting down NEXA...")

if __name__ == '__main__':
    main()