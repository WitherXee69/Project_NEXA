class CMD_netinfo:
    # This is the network information command class
    # Command name
    name = "netinfo"
    aliases = ["ifconfig", "ipconfig"]

    # Command execution method
    def execute(self, context, flags, args=None):
        data = {}
        mode = None
        for flag in flags:
            if flag in ("-all", "-a"):
                mode = "all"
            elif flag in ("-ip4", "-4"):
                mode = "ip4"
            elif flag in ("-ip6", "-6"):
                mode = "ip6"
            else:
                mode = None
        for item in context.netinfo.items():
            interface = item[0]
            for addr in item[1]:
                if addr.family.name == "AF_LINK":
                    interface_type = "MAC"
                elif addr.family.name == "AF_INET":
                    interface_type = "IPv4"
                elif addr.family.name == "AF_INET6":
                    interface_type = "IPv6"
                address = addr.address
                netmask = addr.netmask
                broadcast = addr.broadcast
                ptp = addr.ptp

                result = f" Address: {address}"

                if mode == "ip4" and interface_type != "IPv4":
                    continue
                elif mode == "ip6" and interface_type != "IPv6":
                    continue
                elif mode == "all":
                    all_result = f"Subnet Mask: {netmask}, Broadcast Address: {broadcast}, Point-to-Point: {ptp}"
                    result += f", {all_result}"

                key = f"{interface} >>> {interface_type}"
                data[key] = result
        
        # print(data)
        return data