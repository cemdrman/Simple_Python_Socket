import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
ip_address = "0.0.0.0"
socket_port = 3008
server_address = (ip_address,socket_port)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:    
    while True:       
        data = sock.recv(1024)
        print >>sys.stderr, 'received %s' % data

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()