#import tkinter
from tkinter import *

win = Tk()
#f = Frame(win)
b1 = Button(win, text="Browse...")
b1.grid(row=0, column=1, pady=(30,0), padx=(10,0))
b2 = Button(win, text="Browse...")
b2.grid(row=1, column=1, pady=(10,0), padx=(10,0))
b3 = Button(win, text="Check for files...")
b3.grid(row=2, column=1, pady=(10,10), padx=(10,0))
b4 = Button(win, text="Close Program")
b4.grid(row=2, column=2, sticky=E, pady=(10,10), padx=(0,10))
var1 = StringVar()
var2 = StringVar()
e1 = Entry(win, textvariable=var1)
e1.grid(row=0, column=2, pady=(30,0), padx=(0,10))
e2 = Entry(win, textvariable=var2)
e2.grid(row=1, column=2, pady=(10,0), padx=(0,10))

"""
if __name__ == "__main__":
    root = tkinter.Tk()
    App = ParentWindow(root)
    root.mainloop()
"""
