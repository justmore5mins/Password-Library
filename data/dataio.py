from encryption import *

class PasswordOperate():
    def __init__(self,username:str,userdata: tuple[str,str,str]) -> None:
        self.username = username
        self.usrname,self.password,self.source = userdata
        
    
    def add(self):
        pass