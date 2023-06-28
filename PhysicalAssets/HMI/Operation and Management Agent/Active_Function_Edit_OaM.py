from tkinter import *
from tkinter import filedialog
import os

#current_working_directory
parent_dir = os.getcwd()

# functions 
def openFile():
    tf = filedialog.askopenfilename(
        initialdir= parent_dir + r"\Operation and Management Agent", 
        title="Open Text file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    pathh.insert(END, tf)
    tf = open(tf, 'r+')
    file_cont = tf.read()
    txtarea.insert(END, file_cont)
   
    tf.close()

def saveFile():
    tf = filedialog.askopenfilename(
        initialdir=parent_dir + r"\Operation and Management Agent", 
        title="Save file", 
        filetypes=(("Text Files", "*.txt"),)
        )
    tf = open(tf,'w')
    pathh.insert(END, tf)
    data = str(txtarea.get(1.0, END))
    tf.write(data)
   
    tf.close()

ws = Tk()
ws.title("PythonGuides")
ws.geometry("600x700")
ws['bg']='#2a636e'

# adding frame
frame = Frame(ws)
frame.pack(pady=20)

# adding scrollbars 
ver_sb = Scrollbar(frame, orient=VERTICAL )
ver_sb.pack(side=RIGHT, fill=BOTH)

hor_sb = Scrollbar(frame, orient=HORIZONTAL)
hor_sb.pack(side=BOTTOM, fill=BOTH)

# adding writing space
txtarea = Text(frame, width=40, height=20)
txtarea.pack(side=LEFT)

# binding scrollbar with text area
txtarea.config(yscrollcommand=ver_sb.set)
ver_sb.config(command=txtarea.yview)

txtarea.config(xscrollcommand=hor_sb.set)
hor_sb.config(command=txtarea.xview)

# adding path showing box
pathh = Entry(ws)
pathh.pack(expand=True, fill=X, padx=10)

# adding buttons 
Button(
    ws, 
    text="Open File", 
    command=openFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Save File", 
    command=saveFile
    ).pack(side=LEFT, expand=True, fill=X, padx=20)

Button(
    ws, 
    text="Exit", 
    command=lambda:ws.destroy()
    ).pack(side=LEFT, expand=True, fill=X, padx=20, pady=20)

ws.mainloop()
