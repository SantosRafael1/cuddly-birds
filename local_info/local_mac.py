from scapy.all import *

#get local mac
local_mac = get_if_hwaddr(conf.iface)
print(f"Local mac: {local_mac}")