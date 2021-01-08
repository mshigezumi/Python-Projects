from tkinter import *
from tkinter.filedialog import askdirectory
import shutil
import os
import time

class ParentWindow:
    def __init__(self, win):
        self.var1 = StringVar()
        self.var1.set("/Users/mshigezumi/Documents/GitHub/Python-Projects/folderA/") #default source directory
        self.lbl1 = Label(win, textvariable=self.var1) #label displaying selected file path
        self.lbl1.pack()
        self.but1 = Button(win, text="Browse...", command=self.browseDir1) #creating a button element
        self.but1.pack()

        self.var2 = StringVar()
        self.var2.set("/Users/mshigezumi/Documents/GitHub/Python-Projects/folderB/") #default destination directory
        self.lbl2 = Label(win, textvariable=self.var2) #label displaying selected file path
        self.lbl2.pack()
        self.but2 = Button(win, text="Browse...", command=self.browseDir2) #creating a button element
        self.but2.pack()

        self.but3 = Button(win, text="Check files", command=self.fileCheck) #creating a button element
        self.but3.pack()
        
    def browseDir1(self):
        dir1 = askdirectory(title='Select Directory') #dialog to select the directory for the source
        self.var1.set(dir1 + "/")

    def browseDir2(self):
        dir2 = askdirectory(title='Select Directory') #dialog to select the directory for the destination
        self.var2.set(dir2 + "/")

    def fileCheck(self):
        source = self.var1.get() #setting source directory variable
        destination = self.var2.get() #setting destination directory variable
        files = os.listdir(source) #tuple of files found in source directory

        for file in files:
            timeM = os.path.getmtime(source+file) #getting the modification time of the file
            timeM = time.time() - timeM #subtracting modification time from the start of the epoch to get how much time since last modification in seconds
            #print(source+file) #these prints were for testing to see file paths and time since last modification
            #print(timeM)
            if timeM <= 86400: #if it's been 24 hours or less copy the file from the source to the destination
                shutil.copy(source+file, destination)

if __name__ == "__main__":
    win = Tk()
    app = ParentWindow(win)
    win.mainLoop() #this is throwing an exception?
