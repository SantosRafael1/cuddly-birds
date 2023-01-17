from scapy.all import *

#list interfaces
interfaces = get_if_list()
print("Interfaces:")
for interface in interfaces:
    print("- " + interface)
    