class CMD_say:
    # This is the say command class
    # Command name
    name = "say"
    aliases = ["echo"]
    description = "Echoes the input text back to the user."
    schema = None # No flags for this command, just arguments

    # Command execution method
    def execute(self, context, flags, args):
        full_line = ""
        if args:
            # return args
            for arg in args:
                # return type(arg)
                if isinstance(arg, str):
                    full_line = f"{full_line} " + "".join(arg)
            return full_line.lstrip()
        elif args == ".":
            return "\n"
        return None