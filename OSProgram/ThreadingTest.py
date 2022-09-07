import threading
from struct import pack
import pyshark
from matplotlib import pyplot as plt
import numpy as np
ip = {}
os = {}
capture = pyshark.LiveCapture(interface='WiFi')

def Check_Packets(): 
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


       
print(ip, os)
threads = []

for i in range(50):
    t = threading.Thread(target=Check_Packets)
    t.daemon = True
    threads.append(t)

for i in range(50):
    threads[i].start()

for i in range(50):
    threads[i].join()
