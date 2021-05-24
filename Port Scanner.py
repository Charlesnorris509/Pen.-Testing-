#This is the implementation of a Port Scanner in Python
# Cybersecurity tool

import socket

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

Host = input("Enter The IP address you want to scan :  ")
Port = 21

def PortScanner(Port):
    if soc.connect_ex((Host, Port)):
        print("Port closed")
    else:
        print("Port Open")

PortScanner(Port)

