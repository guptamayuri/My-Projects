# update password window
from tkinter import *
from tkinter import messagebox
import pymysql

bullet = "\u2022"


class Update_pass:
    def __init__(self, master):
        self.master = master
        self.f = Frame(self.master)
        self.f.pack(padx=20, pady=10)

        self.unameLable = Label(self.f, text='Username :', font=40).grid(row=0, sticky=W)
        self.in_uname = Entry(self.f, font=1)
        self.in_uname.grid(row=0, column=1, pady=10)
        self.oldpLabel = Label(self.f, text='Old Password :', font=40).grid(row=1, sticky=W)
        self.oldEntry = Entry(self.f, font=1, show=bullet)
        self.oldEntry.grid(row=1, column=1, pady=10)
        self.newpLabel = Label(self.f, text='New Password :', font=40).grid(row=2, sticky=W)
        self.newEntry = Entry(self.f, font=1, show=bullet)
        self.newEntry.grid(row=2, column=1, pady=10)

        self.update_btn = Button(self.f, text="Update", font=40, fg="Red", command=self.update_action)
        self.update_btn.grid(row=8, column=1, pady=10)

    def update_action(self):
        db = pymysql.connect("172.16.6.160", "root", "oracle123", "monitor") # database connection
        cursor = db.cursor()
        user_get = self.in_uname.get()
        old_get = self.oldEntry.get()
        new_get = self.newEntry.get()
        up_list = [user_get, old_get, new_get]
        cursor.callproc('up_pass', up_list) # call procedure "up_pass" from mysql
        db.commit()
        if user_get == "" or old_get == "" or new_get == "":
            messagebox.showwarning("Warning!!", "Fill up the entries")

        else:
            for update in cursor.fetchall():
                up = (update[0])
                if up == "null":
                    messagebox.showwarning("Warning!!", "Wrong Entries")
                    continue
                else:
                    messagebox.showinfo("Update Info", "Successfully Updated")
                    self.master.destroy()
        import logout #call logout.py program
        logout.logout_action()


def update():

    root = Tk()
    root.wm_attributes('-fullscreen', 'true')
    root.wm_attributes('-topmost', 'true')
    root.resizable(width=False, height=False)
    Update_pass(root)
    root.mainloop()


if __name__ == '__main__':
    update()
