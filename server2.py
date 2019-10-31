import socket
import random
s=socket.socket()
#port2=random.randrange(2000,2050)
#port=port2
port=3002
s.bind(('',port))
while True:
    s.listen(5)
    c,addr=s.accept()
    print("got connection from "+str(addr)) 
    c.send("connected - server2".encode())
c.close()
s.close()