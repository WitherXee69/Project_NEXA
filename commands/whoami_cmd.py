import platform

class CMD_whoami:
    # This is the whoami command class
    # Command name
    name = "whoami"
    aliases = []
    description = "Displays information about the current NEXA Shell session and environment."
    schema = {
        "-f": "bool",
        "--full": "bool"}

    # Command execution method
    def execute(self, context, flags, args=None):
        data_normal = f"""
███╗   ██╗███████╗██╗  ██╗ █████╗           
████╗  ██║██╔════╝╚██╗██╔╝██╔══██╗          NEXA Shell by WitherXee
██╔██╗ ██║█████╗   ╚███╔╝ ███████║          Version >> {context.metadata["version"]} : {context.metadata["channel"]}
██║╚██╗██║██╔══╝   ██╔██╗ ██╔══██║          Codename >> {context.metadata["codename"]}
██║ ╚████║███████╗██╔╝ ██╗██║  ██║          
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝          
                                    """
        data_full = f"""            
                                            NEXA Shell by WitherXee
███╗   ██╗███████╗██╗  ██╗ █████╗           Version >> {context.metadata["version"]} : {context.metadata["channel"]}
████╗  ██║██╔════╝╚██╗██╔╝██╔══██╗          Codename >> {context.metadata["codename"]}
██╔██╗ ██║█████╗   ╚███╔╝ ███████║          
██║╚██╗██║██╔══╝   ██╔██╗ ██╔══██║          OS >> {platform.system()} {platform.release()}
██║ ╚████║███████╗██╔╝ ██╗██║  ██║          Version >> {platform.version()}
╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝          CPU >> {platform.processor()}
                                            Machine >> {platform.machine()}
                                            
                                    """

        for key, value in flags.items():
            if key in ("-f", "--full") and value:
                return data_full
        return data_normal