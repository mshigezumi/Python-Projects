from tkinter import *
import webbrowser
import os

class ParentWindow:
    def __init__(self, win):
        self.var = StringVar()
        self.var.set("Stay tuned for our amazing summer sale!") #starting text for entry
        self.ent = Entry(win, textvariable=self.var) #creating an entry element, links var to the text
        self.ent.pack()
        self.but = Button(win, text="Create Webpage", command=self.writeFile) #creating a button element
        self.but.pack()

    def writeFile(self):
        text = self.var.get() #gets the string from the var variable and sets it to text
        file = open("index.html", "w") #opens/creates index.html and write to the file
        file.write( """\
                       <html>
                           <body>
                               <h1>
                                   {}
                               </h1>
                           </body>
                       </html>\
                    """.format(text)) #layout of html file plus the body text given by the user
        
        path = "file://" + os.path.realpath("index.html") #get the absolute path to the edited/created file
        webbrowser.open_new_tab(path) #opens the path in the default web browser in a new tab

if __name__ == "__main__":
    win = Tk()
    app = ParentWindow(win)
    win.mainLoop() #this is throwing an exception?
