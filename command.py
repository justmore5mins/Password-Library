from tkinter import Entry

class User:
    def __init__(self) -> None:
        self.username:str
        self.password:str
    
    def ReadUserData(self,username:Entry,password:Entry):
        with open("front\data.cache","w", encoding="utf-8") as file:
            file.write(f"{username.get()} {password.get()}")