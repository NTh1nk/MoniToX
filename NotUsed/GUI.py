import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()

def Cleanser():
    print("Works")




canvas = tk.Canvas(root, height=700, width=700, bg="#2c2d7d")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

RunCleanser = tk.Button(root, text="Run", padx=10, pady=5, fg="white", bg="#2c2d7d", command=Cleanser)
RunCleanser.pack()
root.mainloop()