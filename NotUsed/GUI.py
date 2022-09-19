from functools import cache
import tkinter as tk
from tkinter import *
from tkinter import filedialog, Text
import os




def openFile():
   with open("Cache/UserData.txt") as tf:
        
        data = tf.read()
        txtarea.insert(END, data)
        

ws = Tk()
ws.title("Cleanser")
ws.geometry("400x450")
ws['bg']='#fb0'

txtarea = Text(ws, width=40, height=20)
txtarea.pack(pady=20)

pathh = Entry(ws)
pathh.pack(side=LEFT, expand=True, fill=X, padx=20)



Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=RIGHT, expand=True, fill=X, padx=20)

ws.mainloop()
