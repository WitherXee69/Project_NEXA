from core.engine import Engine
from core.registry import CommandRegistry
from core.context import Context

from core.prompt.provider import PromptProvider

from frontend.cli import frontend_cli
from frontend.renderer import Renderer

from commands.help_cmd import CMD_help
from commands.here_cmd import CMD_here
from commands.scan_cmd import CMD_scan
from commands.warp_cmd import CMD_warp
from commands.say_cmd import CMD_say
from commands.execute_cmd import CMD_execute
from commands.netinfo_cmd import CMD_netinfo

def nexa():
    # Initialize core components
    registry = CommandRegistry()
    context = Context()
    renderer = Renderer()

    prompt = PromptProvider()

    # Register commands (this would typically be more dynamic)
    registry.register(CMD_help(), context)
    registry.register(CMD_here(), context)
    registry.register(CMD_scan(), context)
    registry.register(CMD_warp(), context)
    registry.register(CMD_say(), context)
    registry.register(CMD_execute(), context)
    registry.register(CMD_netinfo(), context)

    # print(registry.command_registry)

    # Start the frontend CLI
    engine = Engine(registry, context)
    while not context.exit_state:
        frontend_cli(engine, renderer, prompt, context)

if __name__ == '__main__':
    try:
        print("\033c", end="")
        print("""NEXA Shell [Version 0.1a]
by WitherXee. All rights reserved.\n""")
        
        nexa()
    except KeyboardInterrupt:
        print("\nShutting down NEXA...")