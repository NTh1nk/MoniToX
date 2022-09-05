import pyshark
capture = pyshark.LiveCapture(interface='WiFi')
ip = {}
os = {}
for packet in capture.sniff_continuously(packet_count=5):
    if packet.ip.src not in ip:
        ip[packet.ip.src] = 0
    ip[packet.ip.src] += 1
print(ip)
