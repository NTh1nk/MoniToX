import threading
from struct import pack
from time import sleep
from tracemalloc import start
import pyshark
from matplotlib import pyplot as plt
import numpy as np
ip = {}
os = {}
capture = pyshark.LiveCapture(interface='WiFi')

def Check_Packets():
    global os
    global ip
    for i in range(1):
        for packet in capture.sniff_continuously(packet_count=25):
            if "IP" in packet:
                if packet.ip.src not in ip:
                    ip[packet.ip.src] = 0      
            ip[packet.ip.src] += 1
            if "SSDP" in packet:
                if packet.ssdp.http_user_agent not in os:   
                    os[packet.ssdp.http_user_agent] = 0      
                os[packet.ssdp.http_user_agent] += 1


def CreateGraph ():
    global os
    global ip
    plt.pie(os.values(), labels = os.keys(), colors=["k", "b", "g", "r","c"]) 
    plt.pause(0.05)  
print(ip, os)
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


