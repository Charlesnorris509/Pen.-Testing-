#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install paramiko')


# In[ ]:


# ------ --------------------------- SSHRCMT.PY-------------------------------

import threading
import paramiko
import subprocess

def ssh_command(ip, user, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, username=user, password=password)
    
    ssh_session = client.get_transport().open_session()
    
    if ssh_session.active:
        ssh_session.exec_command(command)
        print ssh_session.exec_command(command)
    return ssh_command('192.168.1.8', 'chuck', 'foremostgecko', 'id')

