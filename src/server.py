import socket
HEADERSIZE=10
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
            
            msg="Welcome to the Server"
            msg=f'{len(msg):<{HEADERSIZE}}' + msg #this is the header. 

            clientsocket.send(bytes(msg,'utf-8'))
            #you need a header at the start in order to stream the data. 
            #you need the fixed header. This will keep the length of the header 
            #always at 10 characters. 
          
