class User():
    def __init__(self,path: str, username:str, password:str) -> None:
        self.path = path
        self.username = username
        self.password = password

    def CheckUser(self) -> int:
        """
        0:scusses
        1:password wrong
        2:no account
        """
        users = {}
        with open(self.path) as f:
            for line in f:
                # 跳過空白行
                if line == "\n":
                    continue
                username, password = line.split()
                users[username] = password
        if self.username in users and users[username] == self.password:
            return 0
        if self.username in users and users[username] != self.password:
            return 1
        else: 
            return 2

    def AddUser(self):
        data = f"{self.username} {self.password}"
        write = open(self.path,"a")
        write.write(data)
        write.close()