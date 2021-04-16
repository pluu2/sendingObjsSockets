import socket

class client(): 
    def __init__(self,ip,socket):
        self.ip=ip
        self.socket=socket
        self.connection=0

    def createsocket(self): 
        self.connection=socket.socket (socket.AF_INET,socket.SOCK_STREAM)
    def connect(self):
        self.connection.connect ((self.ip,self.socket))
        print('connected!')
        msg=self.connection.recv (1024)
        print(msg.decode("utf-8")) #decode bytes
        
