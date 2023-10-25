from socket import socket,AF_INET,SOCK_STREAM
recive = socket(AF_INET, SOCK_STREAM)
recive.connect(("localhost",8787))
recive.listen(2)

data = recive.recv(1024).decode()
print(data)