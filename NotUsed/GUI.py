import tkinter as tk
from tkinter import filedialog, Text
import os



root = tk.Tk()

def Cleanser():
    print("Works")

def graph():
    print("works")


canvas = tk.Canvas(root, height=700, width=1000, bg="#2c2d7d")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

RunCleanser = tk.Button(root, text="Run", padx=10, pady=5, fg="white", bg="#2c2d7d", command=Cleanser)
StartGraph = tk.Button(root, text="Graph", padx=10, pady=5, fg="white", bg="#2c2d7d", command=graph)
Users = tk.Button(root, text="Users", padx=10, pady=5, fg="white", bg="#2c2d7d", command=Cleanser)
Searches = tk.Button(root, text="DNS", padx=10, pady=5, fg="white", bg="#2c2d7d", command=Cleanser)

RunCleanser.pack(side='left', anchor='e', expand=True)
StartGraph.pack(side='right', anchor='w', expand=True)
Users.pack(side='right', anchor='w', expand=True)
Searches.pack(side='left', anchor='e', expand=True)
root.mainloop()