import socket
from subprocess import PIPE, Popen

def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]

s=socket.socket()
#id="client1"
while 1:
    port=3000
    s.settimeout(1)
    s.connect(('127.0.0.1',port))
    p=int(s.recv(1024).decode())
    s.close()
    s=socket.socket()
    s.settimeout(1)
    if p==3001:
        if int(cmdline('netstat -aon | find /i "listening" | findstr "3001" |  find /c /v ""').decode())==1:
            s.connect(('127.0.0.1',p))
            print(s.recv(1024).decode())
            break

        else:
            print('no port is available : service not available '+str(p))       
            break
    
    elif p==3002:
        if int(cmdline('netstat -aon | find /i "listening" | findstr "3002" |  find /c /v ""').decode())==1:
            s.connect(('127.0.0.1',p))
            print(s.recv(1024).decode())
            break

        else:
            print('no port is available : service not available '+str(p))       
            break

s.close()
