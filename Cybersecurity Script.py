#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install subprocess')


# In[2]:


get_ipython().system('pip install subprocess.run')


# In[3]:


get_ipython().system('pip install python-time')


# In[ ]:


import os
import re 
import subprocess 
import time

response = subprocess.Popen('speedtest-cli --simple', shell=True, stdout= subprocess.PIPE).stdout.read()

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Uploads:\s(.*?)/s', response, re.MULTILINE)

ping[0] = ping[0].replace(',', '.')
download[0] = download[0].replace(',', '.')
upload[0] = upload[0].replace(',', '.')

try:
    if os.stat('/home/stat_system/speedtest/speedtext.csv').st_size == 0:
        print("Date, Time, Pings(ms), Downloads (Mbit/s), Uploads (Mbit/s)")
    except:
        pass
    
print'{},{},{},{},{}'.format(time.strftime('%m%d%y'), time.strftime('%H:%M'), ping[0], download[0], upload[0])

