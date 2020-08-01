from tkinter import *
from tkinter import filedialog
import os
from Imagehiding import imageHide, imageRetrieve
from Datahiding import *

class stego:
    def __init__(self, master):
        self.master = master
        master.title("Stego 1.0")
        master.geometry("200x100+200+200")
        
        #creating menu
        menu = Menu(root)
        root.config(menu=menu)
        
        embedMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Embed", menu=embedMenu)
        embedMenu.add_command(label="Text", command=textHide)
        embedMenu.add_command(label="Image", command=imageHide)
        
        extractMenu = Menu(menu, tearoff=0)
        menu.add_cascade(label="Extract", menu=extractMenu)
        extractMenu.add_command(label="Text", command=textRetrieve)
        extractMenu.add_command(label="Image", command=imageRetrieve)  
        
    
        
        
root = Tk()
s = stego(root)
root.mainloop()
