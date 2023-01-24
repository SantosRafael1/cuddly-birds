import subprocess, string, random, re

#generate and return a mac addr
def random_mac_address():
    #get hexdigits uppercase
    upper_hex = "".join(set(string.hexdigits.upper()))

    #second char must be 0,2,6,4,8,E,C,A
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac = mac + random.choice("02468ACE")
            else:
                mac = mac + random.choice(upper_hex)
        
        mac = mac + ":"
    
    return mac.strip(":")


#use ifconfig command to get interface details
def get_current_mac(iface):
    output = subprocess.check_output(f"ifconfig {iface}", shell=True).decode()
    return re.search("ether (.+)", output).group().split()[1].strip()


#actually change it
def change_mac_addr(iface, new_mac_addr):
    # disable the network interface
    subprocess.check_output(f"ifconfig {iface} down", shell=True)
    #change the mac
    subprocess.check_output(f"ifconfig {iface} hw ether {new_mac_addr}", shell=True)
    #enable it again
    subprocess.check_output(f"ifconfig {iface} up", shell=True)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="MAC changer")
    parser.add_argument("interface", help="Network interface name")
    parser.add_argument("-r", "--random", action="store_true", help="Whether to generate a random MAC addr")
    parser.add_argument("-m", "--mac", help="The new MAC you want to change to")

    args = parser.parse_args()
    iface = args.interface
    if args.random:
        new_mac_addr = random_mac_address()
    elif args.mac:
        new_mac_addr = args.mac
    
    old_mac_addr = get_current_mac(iface)
    print("[*] Old MAC addr: ", old_mac_addr)

    change_mac_addr(iface, new_mac_addr)
    new_mac_addr = get_current_mac(iface)
    print("[+] New MAC addr:", new_mac_addr)