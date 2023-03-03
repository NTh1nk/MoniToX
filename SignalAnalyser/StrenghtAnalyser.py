from matplotlib import pyplot as plt
import os
import socket
from tkinter import *
import pyshark
import numpy as np


capture = pyshark.LiveCapture(interface='WiFi')

def MeasurePackets():
    for packet in capture.sniff_continuously(packet_count=25):
        print(packet)
MeasurePackets()
