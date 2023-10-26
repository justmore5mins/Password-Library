from sys import path
path.append("D:\Password_Library")

from tkinter import Tk, Entry,Label,Button
from user import *
from os import system
login = Tk()

#function defining
def continues():
    result = User("front/user.login",username=username_entry.get(),password=password_entry.get()).CheckUser()
    if result == 0:
        username = username_entry.get()
        password = password_entry.get()
        data = username+" "+password
        print(data)
        with open("front/data.txt","w") as file:
            file.write(f"{username}")
        login.destroy()
        system("python3 dashboards/dashboard.py")
        
    elif result == 1:
        password_wrong_text = Label(text="Password Wrong",fg="#FF8800")
        password_wrong_text.place(x=43,y=200)
    elif result == 2:
        err = Label(text="User Not Exists",fg="#FF8800")
        err.place(x=43,y=200)
    

#window setting
login.title("Login")
WIDTH = 200
HEIGHT = 320
login.geometry(f"{WIDTH}x{HEIGHT}")
login.resizable(False,False)

username_Text = Label(text="username")
username_Text.place(x=65,y=75)
username_entry = Entry(login)
username_entry.place(x=43,y=100,width=120)
password_Text = Label(text="Password")
password_Text.place(x=65,y=125)
password_entry = Entry(login,show="*")
password_entry.place(x=43,y=150,width=120)
sumbit_btn = Button(text="Log in",command= lambda: login.after(1,continues()))
sumbit_btn.place(x=65,y=175)

login.mainloop()