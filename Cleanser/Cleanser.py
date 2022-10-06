from dataclasses import dataclass
import http
import threading
from struct import pack
import sys
from time import sleep
import pyshark
from matplotlib import pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import END, filedialog, Text
import os
import socket
from tkinter import *
GraphState = True
ip = {}
os = {}
http = {}
dns = {}
users = {}
capture = pyshark.LiveCapture(interface='Ethernet')


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
            #if "SSDP" in packet:
             #   if packet.ssdp.http_user_agent not in os:   
              #      os[packet.ssdp.http_user_agent] = 0      #Here is the raise atribute error
               # os[packet.ssdp.http_user_agent] += 1
               # users[packet.ip.src] = packet.ssdp.http_user_agent
            if "DNS" in packet:
                if packet.dns.qry_name not in dns:   
                    dns[packet.dns.qry_name] = 0      
                dns[packet.dns.qry_name] += 1 

        print(dns, users)
    
def StopGr():
    global GraphState
    GraphState = False
    
def CreateGraph ():
    global os
    global ip
    global users
    plt.pie(os.values(), labels = os.keys(), colors=["b", "k", "g", "r","c","m","y"]) 
    #plt.table(cellText=[list(users.values())], colLabels=list(users.keys()))
    plt.pause(0.05)

def Network():
    with open("Cache/NetList.txt", 'w') as net:
        net.write(socket.gethostbyname(socket.gethostname()))

def SaveData(txtarea):   
    global users
    global dns
    
    with open("Cache/UserData.txt", 'w') as f:

        f.write(f"These are the searches {dns}. These are the users {users}")

    txtarea.delete("1.0","end")
    txtarea.insert(tk.END, dns)


threads = []
fig = plt.figure(figsize =(10, 7))

t = threading.Thread(target=Check_Packets)
t.daemon = False
threads.append(t)
threads[0].start()
def graph():
    global GraphState
    GraphState = True
    plt.ion()
    plt.show()
    while GraphState:
     CreateGraph()
    

def Gui():
    global dns
    root = tk.Tk()
    root.title("MoniToX")
    canvas = tk.Canvas(root, height=700, width=1000, bg="#2c2d7d")
    canvas.pack()
    frame = tk.Frame(root, bg="white")
    frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)
    txtarea = Text(frame, width=40, height=20)
    txtarea.pack(side="top")
    txtarea.insert(tk.END, dns)
    StartGraph = tk.Button(root, text="Graph", padx=10, pady=5, fg="white", bg="#2c2d7d", command=graph)
    Save= tk.Button(root, text="Save", padx=10, pady=5, fg="white", bg="#2c2d7d", command=lambda: SaveData(txtarea=txtarea))
    StopGraph= tk.Button(root, text="StopGraph", padx=10, pady=5, fg="white", bg="#2c2d7d", command=StopGr)
    AddNet= tk.Button(root, text="Net", padx=10, pady=5, fg="white", bg="#2c2d7d", command=Network)


    Save.pack(side='left', anchor='e', expand=True)
    StartGraph.pack(side='right', anchor='w', expand=True)
    StopGraph.pack(side='left', anchor='e', expand=True)
    AddNet.pack(side='left', anchor='e', expand=True)    
    root.mainloop()
Gui()


threads[0].join()


