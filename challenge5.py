from tkinter import *

class ParentWindow:
    def __init__(self, win):
        #Frame.__init__ (self)

        self.b1 = Button(win, text="Browse...")
        self.b1.grid(row=0, column=1, pady=(30,0), padx=(10,0), command=self.askDirectory)
        self.b2 = Button(win, text="Browse...")
        self.b2.grid(row=1, column=1, pady=(10,0), padx=(10,0), command=self.askDirectory)
        self.b3 = Button(win, text="Check for files...")
        self.b3.grid(row=2, column=1, pady=(10,10), padx=(10,0))
        self.b4 = Button(win, text="Close Program", command=self.cancel)
        self.b4.grid(row=2, column=2, sticky=E, pady=(10,10), padx=(0,10))
        var1 = StringVar()
        var2 = StringVar()
        self.e1 = Entry(win, textvariable=var1)
        self.e1.grid(row=0, column=2, pady=(30,0), padx=(0,10))
        self.e2 = Entry(win, textvariable=var2)
        self.e2.grid(row=1, column=2, pady=(10,0), padx=(0,10))

        #cd = filedialog.askdirectory()

    def askDirectory(self):
        cd = filedialog.askdirectory()

    def cancel(self):
        self.master.destroy()

if __name__ == "__main__":
    win = Tk()
    app = ParentWindow(win)
    win.mainLoop()

"""
if __name__ == "__main__":
    root = tkinter.Tk()
    App = ParentWindow(root)
    root.mainloop()
"""

#page 263 challenge, I don't really know what's going wrong
