from scapy.all import *

#get local IP
local_ip = get_if_addr(conf.iface)
print(f"Local IP: {local_ip}")