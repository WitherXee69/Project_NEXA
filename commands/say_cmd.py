class CMD_say:
    # This is the say command class
    # Command name
    name = "say"
    aliases = ["echo"]

    # Command execution method
    def execute(self, context, flags, args):
        global full_line
        if flags is None: # Temporary till I add sub-system flags
            if args:
                # return args
                for arg in args:
                    # return type(arg)
                    if type(arg) == str:
                        full_line = "".join(arg)
                return full_line
            elif args == ".":
                return "\n"
        return None