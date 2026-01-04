from core.engine import Engine
from core.registry import CommandRegistry
from core.context import Context
from frontend.cli import frontend_cli

from commands.help_cmd import CMD_help
from commands.here_cmd import CMD_here
from commands.scan_cmd import CMD_scan
from commands.warp_cmd import CMD_warp
from commands.say_cmd import CMD_say
from commands.execute_cmd import CMD_execute

def nexa():
    # Initialize core components
    registry = CommandRegistry()
    context = Context()

    # Register commands (this would typically be more dynamic)
    registry.register(CMD_help(), context)
    registry.register(CMD_here(), context)
    registry.register(CMD_scan(), context)
    registry.register(CMD_warp(), context)
    registry.register(CMD_say(), context)
    registry.register(CMD_execute(), context)

    # print(registry.command_registry)

    # Start the frontend CLI
    engine = Engine(registry, context)
    frontend_cli(engine,context)

if __name__ == '__main__':
    try:
        nexa()
    except KeyboardInterrupt:
        print("\nShutting down NEXA...")