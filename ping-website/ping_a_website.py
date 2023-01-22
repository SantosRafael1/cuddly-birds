from ping3 import ping

hostname = str(input("Host: "))

response_time = ping(hostname)
if response_time:
    print(f"\033[32m{hostname} IS up! Response time: {round(response_time, 2)} ms")
elif not response_time:
    print(f"{response_time}")
else:
    print(f"\033[31m{hostname} is DOWN. Response time: {round(response_time, 2)}")



#It is used to measure the time that a website takes to send packets of data from a source computer
#to a destination computer.