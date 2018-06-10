#logout window
from tkinter import *
import pymysql



def logout_action():
    db = pymysql.connect("172.16.6.160", "root", "oracle123", "monitor") #database connection
    cursor = db.cursor()
    from uuid import getnode as get_mac #get amc address
    mac = get_mac()
    cursor.callproc('log_out', [mac])#call procedure "log_out" from mysql
    db.commit()
    import mac_Add #call mac_Add program
    mac_Add.chrome_history_fetch()




logout = Tk()
logout.resizable(width=False, height=False)
logout.overrideredirect(1)
w = 90  # width for the logout
h = 40  # height for the logout
ws = logout.winfo_screenwidth()  # width of the screen
hs = logout.winfo_screenheight()  # height of the screen
x = ws/2
y = (hs+2)-hs
logout.geometry('%dx%d+%d+%d' % (w, h, x, y))
logbtn = Button(logout, text="Log Out", font=40,fg="Red", command=logout_action)
logbtn.grid(sticky=NW)
logout.mainloop()

