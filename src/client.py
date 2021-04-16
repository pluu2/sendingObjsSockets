import socket
HEADERSIZE=10
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
        full_msg=""
        new_msg=True
        while True:
            msg=self.connection.recv(16)
            if new_msg: 
                #read message to headersize
                #print(f"new message length: {msg[:HEADERSIZE]}")
                msglen = int(msg[:HEADERSIZE]) #python will be okay.
                new_msg=False
            full_msg+=msg.decode("utf-8")

            if len(full_msg)-HEADERSIZE == msglen: 
                #3print("full message recv")
                print(full_msg[HEADERSIZE:])
                new_msg=True
                full_msg=''

                
        
