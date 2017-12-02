from tkinter import *
import os
from PIL import ImageTk,Image
import tkinter as Tk

class App:
    def __init__(self, master):
        master.minsize(width=110, height=110)
        self.frame = Frame(master)
        self.b = Button(self.frame, text = 'Motion Module',bg="blue",width=10,height=5, command = self.openFile)
        self.b.grid(row = 2)
        self.b.pack(side=LEFT)
        self.button = Button(self.frame, 
                         text="Exit Module", fg="red",
                         command=self.close_window)
        self.button.pack(side=RIGHT)
        self.frame.grid()
    def openFile(self):
        os.startfile("run.bat")
    def close_window (self): 
     root.destroy()    



root = Tk.Tk()
background_image=Tk.PhotoImage(file="motion.gif")
background_label = Tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
root.wm_geometry("300x200+40+60")
root.title('Motion Detector')

app = App(root)
root.mainloop()
    
