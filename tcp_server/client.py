import socket 
import time
host = socket.gethostname() 
port = 8000
BUFFER_SIZE = 1024
MESSAGE = 0

tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

while True:
    tcpClientA.send(str(MESSAGE)+"ENDOFPACKET\n")     
    #data = tcpClientA.recv(BUFFER_SIZE)
    #print " Client2 received data:", data
    time.sleep(1)
    MESSAGE += 1

tcpClientA.close() 
