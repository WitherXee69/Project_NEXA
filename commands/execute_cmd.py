class CMD_execute:
    # This is the execute command class
    # Command name
    name = "execute"
    aliases = ["exec", "run", "script"]

    # Command execution method
    def execute(self, context, flags, args):
        if not flags:
            if args:
                for script in args:
                    try:
                        with open(script, 'r') as file:
                            commands = file.readlines()
                        for command in commands:
                            # print(command)
                            if command.strip().startswith("@"):
                                context.engine.handle_directives()
                            else:
                                context.engine.run_line(command)
                        # return f"Executed script: {script}\n"
                    except FileNotFoundError:
                        return f"Script not found: {script}\n"