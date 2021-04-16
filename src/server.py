import socket
import pickle
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
            
            msg=self.create_message('123')


            clientsocket.send(msg)
            #you need a header at the start in order to stream the data. 
            #you need the fixed header. This will keep the length of the header 
            #always at 10 characters. 
          
    def create_message(self,object): 
        d={1:"Hey",2:"There"} #for now it's a hardcoded
        msg=pickle.dumps(d) 
        msg=bytes(f'{len(msg):<{HEADERSIZE}}',"utf -8") +msg
        return msg
        