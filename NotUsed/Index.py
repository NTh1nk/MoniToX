from struct import pack
import pyshark
from matplotlib import pyplot as plt
import numpy as np
capture = pyshark.LiveCapture(interface='WiFi')
ip = {}
os = {}
for packet in capture.sniff_continuously(packet_count=25):
    if "IP" in packet:
        if packet.ip.src not in ip:
            ip[packet.ip.src] = 0      
        ip[packet.ip.src] += 1
    if "SSDP" in packet:
       # print(packet.ssdp.field_names)
        if packet.ssdp.http_user_agent not in os:   
            os[packet.ssdp.http_user_agent] = 0      
        os[packet.ssdp.http_user_agent] += 1


       
print(ip, os)
