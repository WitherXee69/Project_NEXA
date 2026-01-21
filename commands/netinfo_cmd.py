class CMD_netinfo:
    # This is the network information command class
    # Command name
    name = "netinfo"
    aliases = ["ifconfig", "ipconfig"]

    data = []

    # Command execution method
    def execute(self, context, flags=None, args=None):
        for item in context.netinfo.items():
            interface = item[0]
            for addr in item[1]:
                interface_type = addr.family.name
                address = addr.address
                netmask = addr.netmask
                broadcast = addr.broadcast
                ptp = addr.ptp

                result = f"Interface: {interface}, Type: {interface_type}, Address: {address}, Subnet Mask: {netmask}, Broadcast Address: {broadcast}, Point-to-Point: {ptp}"
                self.data.append(result)
        # print(self.data)
        return self.data
        # return context.netinfo