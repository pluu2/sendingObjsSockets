import socket

class server(): 
    def __init__(self,ip,socket): 
        self.ip=ip
        self.socket=socket
        self.connection=0
    def createsocket(self): 
        self.connection =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connection.bind(('',self.socket) ) #listens to anything at given port
        self.connection.listen(5)
        print('listening')

        while True: 
            clientsocket,address = self.connection.accept() #the client address and socket. 
            print(f"Connection from {address} has been established")
            clientsocket.send(bytes("Welcome",'utf-8'))
