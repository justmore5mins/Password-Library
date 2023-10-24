import sys
sys.path.append("D:\Password_Library")

from tkinter import Tk, Entry,Label,Button
from command import *
from time import sleep as delay

login = Tk()
user = User()

#window setting
login.title("Passowrd Library Login")
WIDTH = 200
HEIGHT = 320
login.geometry(f"{WIDTH}x{HEIGHT}")

username_Text = Label(text="username")
username_Text.place(x=65,y=75)
username_entry = Entry(login)
username_entry.place(x=43,y=100,width=120)
password_Text = Label(text="Password")
password_Text.place(x=65,y=125)
password_entry = Entry(login,show="*")
password_entry.place(x=43,y=150,width=120)
sumbit_btn = Button(text="Log in",command=user.ReadUserData(username=username_entry,password=password_entry))
sumbit_btn.place(x=65,y=175)


login.mainloop()
