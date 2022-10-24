
from this import d
import threading
import sys
from time import sleep
from turtle import clear
import pyshark
import os
import socket
ip = {}
os = {}
UserINP = ""
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
            #if "SSDP" in packet:
             #   if packet.ssdp.http_user_agent not in os:   
              #      os[packet.ssdp.http_user_agent] = 0      #Here is the raise atribute error
               # os[packet.ssdp.http_user_agent] += 1
               # users[packet.ip.src] = packet.ssdp.http_user_agent
            if "DNS" in packet:
                if packet.dns.qry_name not in dns:   
                    dns[packet.dns.qry_name] = 0      
                dns[packet.dns.qry_name] += 1 
    

def UserInput():
    UserINP = input("")
    if UserINP == "Help":
        print("DNS, USER, IP")
    else: 
        if UserINP == "DNS":
               print("\033[1;32;40m\n")
               print(dns)
        else: 
            if UserINP == "USER":
                print("\033[1;32;40m\n")
                print(users)
            else:
                if UserINP == "IP":
                    print("\033[1;32;40m\n")
                    print(ip)
                else:
                    print("\033[1;32;40m\n")
                    print("Error")
    UserInput()

def Network():
    with open("Cache/NetList.txt", 'w') as net:
        net.write(socket.gethostbyname(socket.gethostname()))

def SaveData():   
    global users
    global dns
    
    with open("Cache/UserData.txt", 'w') as f:

        f.write(f"These are the searches {dns}. These are the users {users}")




threads = []

t = threading.Thread(target=Check_Packets)
t.daemon = False
threads.append(t)
threads[0].start()

    

def Gui():
    global dns
    global UserINP
    print("\033[1;32;40m\n")
    print("   _____                ._____________   ____  ___")
    print(" /     \   ____   ____ |__\__    ___/___\   \/   \.")
    print("/    Y    (  <_> )   |  \  | |    |(  <_> )       \.")
    print("\____|__  /\____/|___|  /__| |____| \____/___\/   /")
    print("        \/            \/                       \_/")
   
    UserINP = input("Welcome to MoniToX, type help for more info: ")
    if UserINP == "Help":
        print("DNS, USER, IP")
    else: 
        if UserINP == "DNS":
               print("\033[1;32;40m\n")
               print(dns)
        else: print("Error")
    UserInput()

Gui()


threads[0].join()


