import subprocess
import os

path = "/etc/NetworkManager/system-connections/"
files = os.listdir(path)
output = ""

for file in files:
    output += subprocess.check_output(['sudo', 'cat', f'{path}/{file}']).decode()

#extract name and passwords
networks = {}
for i in output.splitlines():
    if "ssid=" in i:
        ssid = i.split('=')[1]
    if 'psk' in i:
        psk = i.split('=')[1]
        networks[ssid] = psk

for ssid, psk in networks.items():
    print(f"{ssid}: {psk}")