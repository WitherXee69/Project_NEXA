class CMD_netinfo:
    # This is the network information command class
    # Command name
    name = "netinfo"
    aliases = ["ifconfig", "ipconfig"]

    data = {}

    # Command execution method
    def execute(self, context, flags=None, args=None):
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

                key = f"{interface} >>> {interface_type}"
                result = f" Address: {address}, Subnet Mask: {netmask}, Broadcast Address: {broadcast}, Point-to-Point: {ptp}"
                self.data[key] = result
        # print(self.data)
        return self.data
        # return context.netinfo