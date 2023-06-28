import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os
import shutil


#current_working_directory
parent_dir = os.getcwd()
  
# Top level window
# create the root window
root = tk.Tk()
root.title('Delete Function')
root.resizable(False, False)
root.geometry('300x150')
  
def delete_function():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        initialdir=parent_dir+r"\Machine_Twin 1\DownloadableFunctions",
        title='Open a file',
        filetypes=filetypes)
    lst = filename.split('/')
    x = lst[-1]
    inp = x[:-3]
    print(inp)
    os.chdir(parent_dir+r"\Machine_Twin 1")
    #print("Current Working Directory " , os.getcwd())
    path_to_save='DownloadableFunctions\\'
    os.remove(path_to_save+inp+".py")
    db_dir = "DataBase/"
    shutil.rmtree(db_dir+inp)
    os.chdir(parent_dir)
    showinfo(
        title='Delete Function',
        message=inp + " deleted"
    )
  
# open button
open_button = ttk.Button(
    root,
    text='Delete Function',
    command=delete_function
)

open_button.pack(expand=True)


# run the application
root.mainloop()
