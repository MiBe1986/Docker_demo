import socket
import time 

HOST = '192.168.100.2'  # The server's hostname or IP address
PORT = 8080     # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        s.sendall(b"Hello world !")
        data = s.recv(1024)
        time.sleep(1)
        print('Received', repr(data))