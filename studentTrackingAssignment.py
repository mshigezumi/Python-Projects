import os
import tkinter
from tkinter import *
import sqlite3

class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        self.master = master
        self.master.minsize(500,300)
        self.master.maxsize(500,300)

        self.master.title("Student Tracking")
        self.master.configure(bg="darkgray")

        self.master.protocol("WM_DELETE_WINDOW", lambda: ask_quit(self))
        #no clue if I did this lamba function correctly
        arg = self.master

        self.lbl_fname = tk.Label(self.master,text='First Name:')
        self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_lname = tk.Label(self.master,text='Last Name:')
        self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_phone = tk.Label(self.master,text='Phone Number:')
        self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_email = tk.Label(self.master,text='Email Address:')
        self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
        self.lbl_course = tk.Label(self.master,text='Current Course:')
        self.lbl_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

        self.txt_fname = tk.Entry(self.master,text='')
        self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_lname = tk.Entry(self.master,text='')
        self.txt_lname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_phone = tk.Entry(self.master,text='')
        self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_email = tk.Entry(self.master,text='')
        self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        self.txt_course = tk.Entry(self.master,text='')
        self.txt_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)
        
        elf.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
        self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
        self.lstList1.bind('<<ListboxSelect>>',lambda event: onSelect(self,event))
        #again I don't know if I'm doing this lambda correctly
        self.scrollbar1.config(command=self.lstList1.yview)
        self.scrollbar1.grid(row=1,column=5,rowspan=9,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
        self.lstList1.grid(row=1,column=2,rowspan=9,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)
    
        self.btn_add = tk.Button(self.master,width=12,height=2,text='Add',command=lambda: addToList(self))
        self.btn_add.grid(row=10,column=0,padx=(25,0),pady=(45,10),sticky=W)
        self.btn_update = tk.Button(self.master,width=12,height=2,text='Update',command=lambda: onUpdate(self))
        self.btn_update.grid(row=10,column=1,padx=(15,0),pady=(45,10),sticky=W)
        self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: onDelete(self))
        self.btn_delete.grid(row=10,column=2,padx=(15,0),pady=(45,10),sticky=W)
        self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: ask_quit(self))
        self.btn_close.grid(row=10,column=4,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)
        #lambdas might be wrong? just replace "self." with the correct prefix to call from this script
        
        create_db(self)
        onRefresh(self)

    ######################

    def ask_quit(self):
        if messagebox.askokcancel("Exit program", "Okay to exit application?"):
            self.master.destroy()
            os._exit(0)

    def create_db(self):
        conn = sqlite3.connect('db_studentTracking.db')
        with conn:
            cur = conn.cursor()
            cur.execute("CREATE TABLE if not exists tbl_students( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_fullname TEXT, \
            col_phone TEXT, \
            col_email TEXT \
            col_course TEXT \
            );")
            conn.commit()
        conn.close()
        first_run(self)

    def first_run(self):
        conn = sqlite3.connect('db_studentTracking.db')
        with conn:
            cur = conn.cursor()
            cur,count = count_records(cur)
            if count < 1:
                cur.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""", ('John','Doe','John Doe','111-111-1111','jdoe@email.com','Basic Course'))
                conn.commit()
        conn.close()

    def count_records(cur):
        count = ""
        cur.execute("""SELECT COUNT(*) FROM tbl_students""")
        count = cur.fetchone()[0]
        return cur,count
    
    def onSelect(self,event):
        varList = event.widget
        select = varList.curselection()[0]
        value = varList.get(select)
        conn = sqlite3.connect('db_studentTracking.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_course FROM tbl_students WHERE col_fullname = (?)""", [value])
            varBody = cursor.fetchall()
            for data in varBody:
                self.txt_fname.delete(0,END)
                self.txt_fname.insert(0,data[0])
                self.txt_lname.delete(0,END)
                self.txt_lname.insert(0,data[1])
                self.txt_phone.delete(0,END)
                self.txt_phone.insert(0,data[2])
                self.txt_email.delete(0,END)
                self.txt_email.insert(0,data[3])
                self.txt_course.delete(0,END)
                self.txt_course.insert(0,data[4])

    def addToList(self):
        var_fname = self.txt_fname.get()
        var_lname = self.txt_lname.get()
        var_fname = var_fname.strip()
        var_lname = var_lname.strip()
        var_fname = var_fname.title()
        var_lname = var_lname.title()
        var_fullname = ("{} {}".format(var_fname,var_lname))
        print("var_fullname: {}".format(var_fullname))
        var_phone = self.txt_phone.get().strip()
        var_email = self.txt_email.get().strip()
        var_course = self.txt_course.get().strip()
        if not "@" or not "." in var_email:
            print("Invalid email, please check the format.")
        if (len(var_fname) > 0) and (len(var_lname) > 0) and (len(var_phone) > 0) and (len(var_email) > 0) and (len(var_course) > 0):
            conn = sqlite3.connect('db_studentTracking.db')
            with conn:
                cursor = conn.cursor()
                cursor.execute("""SELECT COUNT(col_fullname) FROM tbl_students WHERE col_fullname = '{}'""".format(var_fullname))
                count = cursor.fetchone()[0]
                chkName = count
                if chkName == 0:
                    print("chkName: {}".format(chkName))
                    cursor.execute("""INSERT INTO tbl_students (col_fname,col_lname,col_fullname,col_phone,col_email,col_course) VALUES (?,?,?,?,?,?)""",(var_fname,var_lname,var_fullname,var_phone,var_email,var_course))
                    self.lstList1.insert(END, var_fullname)
                    onClear(self)
                else:
                    messagebox.showerror("Name Error","'{}' already exists in the database! Please choose a different name.".format(var_fullname))
                    onClear(self)
            conn.commit()
            conn.close()
        else:
            messagebox.showerror("Missing Text Error","Please ensure that there is data in all four fields.")
        
    def onDelete(self):
        var_select = self.lstList1.get(self.lstList1.curselection())
        conn = sqlite3.connect('db_studentTracking.db')
        with conn:
            cur = conn.cursor()
            cur.execute("""SELECT COUNT(*) FROM tbl_students""")
            count = cur.fetchone()[0]
            if count > 1:
                confirm = messagebox.askokcancel("Delete Confirmation", "All information associated with, ({}) \nwill be permenantly deleted from the database. \n\nProceed with the deletion request?".format(var_select))
                if confirm:
                    conn = sqlite3.connect('db_studentTracking.db')
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""DELETE FROM tbl_students WHERE col_fullname = '{}'""".format(var_select))
                    onDeleted(self)
                    onRefresh(self) #check if working?
                    conn.commit()
            else:
                confirm = messagebox.showerror("Last Record Error", "({}) is the last record in the database and cannot be deleted at this time. \n\nPlease add another record first before you can delete ({}).".format(var_select,var_select))
        conn.close()

    def onDeleted(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_email.delete(0,END)
        onRefresh(self) #check if working?
        try:
            index = self.lstList1.curselection()[0]
            self.lstList1.delete(index)
        except IndexError:
            pass

    def onClear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_phone.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_cursor.delete(0,END)

    def onRefresh(self):
        self.lstList1.delete(0,END)
        conn = sqlite3.connect('db_studentTracking.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute("""SELECT COUNT(*) FROM tbl_students""")
            count = cursor.fetchone()[0]
            i = 0
            while i < count:
                    cursor.execute("""SELECT col_fullname FROM tbl_students""")
                    varList = cursor.fetchall()[i]
                    for item in varList:
                        self.lstList1.insert(0,str(item))
                        i = i + 1
        conn.close()
    
    def onUpdate(self):
        try:
            var_select = self.lstList1.curselection()[0]
            var_value = self.lstList1.get(var_select)
        except:
            messagebox.showinfo("Missing selection","No name was selected from the list box. \nCancelling the Update request.")
            return
        var_phone = self.txt_phone.get().strip()
        var_email = self.txt_email.get().strip()
        var_course = self.txt_course.get().strip()
        if (len(var_phone) > 0) and (len(var_email) > 0 and (len(var_course) > 0):
            conn = sqlite3.connect('db_studentTracking.db')
            with conn:
                cur = conn.cursor()
                cur.execute("""SELECT COUNT(col_phone) FROM tbl_students WHERE col_phone = '{}'""".format(var_phone))
                count = cur.fetchone()[0]
                print(count)
                cur.execute("""SELECT COUNT(col_email) FROM tbl_students WHERE col_email = '{}'""".format(var_email))
                count2 = cur.fetchone()[0]
                print(count2)
                cur.execute("""SELECT COUNT(col_course) FROM tbl_students WHERE col_course = '{}'""".format(var_course))
                count3 = cur.fetchone()[0]
                print(count3)
                if count == 0 or count2 == 0 or count3 == 0:
                    response = messagebox.askokcancel("Update Request","The following changes ({}), ({}), and ({}) will be implemented for ({}). \n\nProceed with the update request?".format(var_phone,var_email,var_course,var_value))
                    print(response)
                    if response:
                        #conn = sqlite3.connect('db_studentTracking.db')
                        with conn:
                           cursor = conn.cursor()
                            cursor.execute("""UPDATE tbl_students SET col_phone = '{0}',col_email = '{1}',col_course = '{2}' WHERE col_fullname = '{3}'""".format(var_phone,var_email,var_course,var_value))
                            onClear(self)
                            conn.commit()
                    else:
                        messagebox.showinfo("Cancel request","No changes have been made to ({}).".format(var_value))
                else:
                    messagebox.showinfo("No changes detected","({}), ({}), and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone, var_email, var_course))
                onClear(self)
            conn.close()
        else:
            messagebox.showerror("Missing information","Please select a name from the list. \nThen edit the phone or email information.")
        onClear(self)
        
if __name__ == "__main__":
    root = tkinter.Tk()
    App = ParentWindow(root)
    root.mainloop()
