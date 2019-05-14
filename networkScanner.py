import subprocess
import socket
import win_unicode_console
import threading
from threading import Thread


def portScan(starttarget, endtarget):
    if portScan is True:
        for remoteServerIP in range(0, len(activeIP)):
            for port in range(starttarget, endtarget):
                print("Scanning port " + str(port))
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((activeIP[remoteServerIP], port))
                if result == 0:
                    print
                    "Port {}: 	 Open".format(port)
                    openedport.append(str(activeIP[remoteServerIP] + ": " + port))
                sock.close()


activeIP = []
openedport = []
print("Network scanner is starting...")
print("Scan 1 from 3: 192.168.88.x")
for ping in range(1,2):
    address = "192.168.88." + str(ping)
    res = subprocess.call(['ping', '-n 1', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
        activeIP.append("192.168.88." + str(ping))
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
print("Scan 2 from 3: 192.168.0.x")
"""
for ping in range(1,99):
    address = "192.168.0." + str(ping)
    res = subprocess.call(['ping', '-n', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
        activeIP.append("192.168.0." + str(ping))
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
print("Scan 3 from 3: 10.0.0.x")
for ping in range(1,99):
    address = "10.0.0." + str(ping)
    res = subprocess.call(['ping', '-n', '3', address])
    if res == 0:
        print( "ping to", address, "OK")
        activeIP.append("10.0.0." + str(ping))
    elif res == 2:
        print("no response from", address)
    else:
        print("ping to", address, "failed!")
        """
print(activeIP)
print("Scanning complete. " + str(len(activeIP)) + " found online")
print("Port scanning start at alive IPs...")

if len(activeIP) is not 0:
    portScan = True
else:
    portScan = False

t1 =1
t2 = 250
t3 = t2 + 1
t4 = 500
t5 = 500+1
t6 = 800
t7 = t6 + 1
t8 = 1024


thread1 = Thread(target=portScan, args=(t1, t2))

thread1.start()
thread1.join()


print(openedport)