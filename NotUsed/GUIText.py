from tkinter import *
from tkinter import filedialog

def openFile():
 
      
    data = open("Cache/UserData.txt")
    txtarea.insert(END, data)
    data.close()

ws = Tk()
ws.title("PythonGuides")
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