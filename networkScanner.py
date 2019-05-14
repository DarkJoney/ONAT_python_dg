import subprocess
import socket
import win_unicode_console
import threading
from threading import Thread
import multiprocessing

def portscan(starttarget, endtarget):
    if portScan is True:
        for remoteServerIP in range(0, len(activeIP)):
            for port in range(starttarget, endtarget):
                print("Scanning port " + str(port) + "\n")
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(0.5)
                result = sock.connect_ex((activeIP[remoteServerIP], port))
                if result == 0:
                    print
                    "Port {}: 	 Open".format(port)
                    openedport.append(str(activeIP[remoteServerIP]) + ": " + str(port))
                sock.close()

def scanhome(start, end):
    for ping in range(start, end):
        address = "192.168.88." + str(ping)
        res = subprocess.call(['ping', '-n 1', '3', address])
        if res == 0:
            print("ping to", address, "OK")
            activeIP.append("192.168.88." + str(ping))
        elif res == 2:
            print("no response from", address)
        else:
            print("ping to", address, "failed!")


activeIP = []
openedport = []
print("Network scanner is starting...")
print("Scan 1 from 3: 192.168.88.x")
thread1 = Thread(target=scanhome, args=(1, 5))
thread2 = Thread(target=scanhome, args=(6, 10))
thread3 = Thread(target=scanhome, args=(11, 20))
thread4 = Thread(target=scanhome, args=(21, 30))

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()

print(activeIP)
print("Scanning complete. " + str(len(activeIP)) + " found online")
print("Port scanning start at alive IPs...")

if len(activeIP) is not 0:
    portScan = True
else:
    portScan = False

cpus = multiprocessing.cpu_count()
print(cpus)
if cpus <= 4:
    thread1 = Thread(target=portscan, args=(1, 250))
    thread2 = Thread(target=portscan, args=(251, 500))
    thread3 = Thread(target=portscan, args=(501, 800))
    thread4 = Thread(target=portscan, args=(801, 1024))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
elif cpus is 12:
    thread1 = Thread(target=portscan, args=(1, 100))
    thread2 = Thread(target=portscan, args=(101, 200))
    thread3 = Thread(target=portscan, args=(201, 300))
    thread4 = Thread(target=portscan, args=(301, 400))
    thread5 = Thread(target=portscan, args=(400, 499))
    thread6 = Thread(target=portscan, args=(500, 599))
    thread7 = Thread(target=portscan, args=(600, 699))
    thread8 = Thread(target=portscan, args=(700, 799))
    thread9 = Thread(target=portscan, args=(800, 899))
    thread10 = Thread(target=portscan, args=(900, 950))
    thread11 = Thread(target=portscan, args=(951, 999))
    thread12 = Thread(target=portscan, args=(1000, 1024))

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    thread12.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
    thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    thread12.join()



print(openedport)
print("enter email pass: ")
emailpass = input()
# import necessary packages

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# create message object instance
msg = MIMEMultipart()

message = str(openedport)

# setup the parameters of the message
password = emailpass
msg['From'] = "tinston@ukr.net"
msg['To'] = "darkjoney@outlook.com"
msg['Subject'] = "OPENED PORTS"

# add in the message body
msg.attach(MIMEText(message, 'plain'))

# create server
server = smtplib.SMTP('smtp.ukr.net: 465')

server.starttls()

# Login Credentials for sending the mail
server.login(msg['From'], password)

# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

server.quit()

print("successfully sent email to %s:" % (msg['To']))