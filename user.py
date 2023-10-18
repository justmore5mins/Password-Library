import os

def CheckUser(data:dict) -> bool:
    getusers = {str:str}
    with open("user.login") as f:
        for line in f:
            # 跳過空白行
            if line == "\n":
                continue
            username, password = line.split()
            getusers.update(username,password)
            # 列印資料
            print(username, password)