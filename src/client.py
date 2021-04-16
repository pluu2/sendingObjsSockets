import socket

class client(): 
    def __init__(self,ip,socket): 
        self.ip=ip
        self.socket=socket
        self.connection=0
    def createsocket(self): 
        self.connection =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.bind(self.ip,self.socket) 
    
