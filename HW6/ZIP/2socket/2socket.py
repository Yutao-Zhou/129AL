import socket
import sys  

host = 'http://web.physics.ucsb.edu/~phys129/lipman/'
port = 80

# create socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print('Failed to create socket')
    sys.exit()

#geting ip address
ip_address='128.111.17.41'

# Connect to remote server
s.connect((ip_address , port))

# Send data to remote server
request= b'GET /~phys129/lipman/\r\n\r\n'
try:
    s.sendall(request)
except socket.error:
    print('Send failed')
    sys.exit()

# Receive data
reply = s.recv(2048)
#decode html to string
r=reply.decode()
#Find update time we want and deal with unrelated information
rts=r.split('\n')
for line in rts:
    if line.find("Latest")!=-1:
        line=line.replace('<span class="greenss">','')
        line=line.replace('</span></p>','')
        line=line.replace('&nbsp;',' ')
        print(line)