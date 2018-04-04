import socket
import sys
import utilFuncs as utilFuncs

# Create a TCP/IP socket

# The type of communications between the two endpoints, 
# typically SOCK_STREAM for connection-oriented protocols and SOCK_DGRAM for connectionless protocols.
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "0.0.0.0"
socket_port = 3008
# Bind the socket to the port
server_address = (ip_address,socket_port)
print ("#######################################################")
print >> sys.stdout, '\tstarting up on %s port %s' % server_address
sock.bind(server_address)
print ("#######################################################")
# Listen for incoming connections
sock.listen(0)

while True:
    utilFuncs.menu()
    print >> sys.stdout, 'Waiting for a connection'
    
    try:
        #accept() returns an open connection between the server and client, along with the address of the client. 
        #The connection is actually a different socket on another port (assigned by the kernel). 
        #Data is read from the connection with recv() and transmitted with sendall().
        connection, client_address = sock.accept()
        print >> sys.stdout, 'connection from', client_address
        while True:            
            while True:
                komut = utilFuncs.getCommand()
                if komut != "null":                    
                    break
            
            if komut == "W":
                utilFuncs.forward(connection)
            elif komut == "A":
                utilFuncs.left(connection)
            elif komut == "S":
                utilFuncs.backward(connection)
            elif komut == "D":
                utilFuncs.right(connection)
            else:                
                break
                       
    finally:
        # Clean up the connection        
        connection.close()
        sock.close()