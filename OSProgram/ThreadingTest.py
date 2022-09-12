import threading
from struct import pack
from time import sleep
from tracemalloc import start
import pyshark
from matplotlib import pyplot as plt
import numpy as np
ip = {}
os = {}
dns = {}
capture = pyshark.LiveCapture(interface='WiFi')

def Check_Packets():
    global os
    global ip
    global dns
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
            if "DNS" in packet:
                if packet.dns.qry_name not in dns:   
                    dns[packet.dns.qry_name] = 0      
                dns[packet.dns.qry_name] += 1  
                

        print(ip, os, dns)

def CreateGraph ():
    global os
    global ip
    plt.pie(os.values(), labels = os.keys(), colors=["b", "k", "g", "r","c","m","y"]) 
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


