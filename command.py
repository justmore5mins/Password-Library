from tkinter import Entry

class User:
    def __init__(self) -> None:
        self.username:str
        self.password:str
    
    def ReadUserData(self,username:Entry,password:Entry):
        self.username = username.get()
        self.password = password.get()
        self.userdata = (self.username,self.password)