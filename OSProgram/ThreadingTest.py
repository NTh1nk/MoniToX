import http
import threading
from struct import pack
from time import sleep
from tkinter.tix import COLUMN
from tracemalloc import start
import pyshark
from matplotlib import pyplot as plt
import numpy as np
ip = {}
os = {}
http = {}
dns = {}
users = {}
capture = pyshark.LiveCapture(interface='WiFi')

def Check_Packets():
    global os
    global ip
    global dns
    global users
    while True:
        for packet in capture.sniff_continuously(packet_count=25):
           
            if "IP" in packet:
                if packet.ip.src not in ip:
                    ip[packet.ip.src] = 0      
                ip[packet.ip.src] += 1
            if "SSDP" in packet:
                if packet.ssdp.http_user_agent not in os:   
                    os[packet.ssdp.http_user_agent] = 0      
                os[packet.ssdp.http_user_agent] += 1
                users[packet.ip.src] = packet.ssdp.http_user_agent
            if "DNS" in packet:
                if packet.dns.qry_name not in dns:   
                    dns[packet.dns.qry_name] = 0      
                dns[packet.dns.qry_name] += 1  

                

        print(dns, users)

def CreateGraph ():
    global os
    global ip
    global users
    plt.pie(os.values(), labels = os.keys(), colors=["b", "k", "g", "r","c","m","y"]) 
    #plt.table(cellText=[list(users.values())], colLabels=list(users.keys()))
    plt.pause(0.05)
    

threads = []
fig = plt.figure(figsize =(10, 7))
plt.ion()
plt.show()
t = threading.Thread(target=Check_Packets)
t2 = threading.Thread(target=CreateGraph)
t.daemon = True
t2.daemon = True    
threads.append(t)
threads.append(t2)

threads[0].start()
while True:
    CreateGraph()

threads[0].join()


