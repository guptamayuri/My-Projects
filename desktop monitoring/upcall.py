#update password or not messagebox
from tkinter import *
from tkinter import messagebox


def main():
    root = Tk()

    root.wm_attributes('-fullscreen', 'true')
    root.wm_attributes('-topmost', 'true')
    root.resizable(width=False, height=False)
    root.withdraw()
    result = messagebox.askyesno("Ask for Update", "Want to update your password ?")
    if result == False :
        import logout # call logout.py program
        logout.logout_action()
        root.destroy()

    else:
        import upchk # call upchk.py program
        upchk.update()

    root.mainloop()


if __name__ == '__main__':
    main()
