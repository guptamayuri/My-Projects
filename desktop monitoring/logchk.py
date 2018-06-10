#login window
from tkinter import *
from tkinter import messagebox
import pymysql

bullet = "\u2022"


class Main_login:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master)
        self.f.pack(padx=20, pady=10)

        self.userlabel = Label(self.f, text="Username :", font=40).grid(row=3)
        self.userentry = Entry(self.f, font=1)
        self.userentry.grid(row=3, column=1, sticky=NW, pady=10)
        self.passlabel = Label(self.f, text="Password :", font=40).grid(row=4, column=0)
        self.passentry = Entry(self.f, font=1, show=bullet)
        self.passentry.grid(row=4, column=1, sticky=NW, pady=5)

        self.subbut = Button(self.f, text="Log In", font=40, fg="Red", command=self.login_action)
        self.subbut.grid(row=10, column=1, sticky=NW, pady=10)

    def login_action(self):
        # ----database connection----
        db = pymysql.connect("172.16.6.160", "root", "oracle123", "monitor")
        cursor = db.cursor()
        uname = self.userentry.get()
        pword = self.passentry.get()
        if uname == "" or pword == "":
            messagebox.showwarning("Warning!!", "Fill up the entries")
        else:
            var = [uname, pword]
            cursor.callproc('loginDetail', var) #call procedure "loginDetail" from mysql
            for record in cursor.fetchall():
                var1 = (record[0])
                if var1 == "null":
                    messagebox.showwarning("Warning!!", "Wrong Entries")
                else:
                    from uuid import getnode as get_mac #get mac address
                    mac = get_mac()
                    var2 = [var1, mac]
                    cursor.callproc('loginRecord', var2)#call procedure "loginRecord" from mysql
                    messagebox.showinfo("Logged In", "Successfully logged in")
                    db.commit()
                    self.master.destroy()
                    import upcall #call upcall program
                    upcall.main()




def login():

    root = Tk()
    root.wm_attributes('-fullscreen', 'true')
    root.wm_attributes('-topmost', 'true')
    root.resizable(width=False, height=False)
    Main_login(root)
    root.mainloop()


if __name__ == '__main__':
    login()
