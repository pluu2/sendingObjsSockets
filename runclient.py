from src.client import * 
from serverconfig import ip,socket

cl= client(ip,socket) 

cl.createsocket()
cl.connect()