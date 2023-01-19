from scapy.all import *
from scapy.layers.dhcp import DHCP
import pprint

def listener(packet):
    if DHCP in packet:
        pprint.pprint(packet[DHCP].fields)
        

sniff(prn=listener, filter="udp and (port 67 or 68)")
