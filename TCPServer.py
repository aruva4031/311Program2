from socket import *

# Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assigns IP address and port number to socket
serverSocket.bind(('localhost', 12000))

#server waits for 2 TCP connetions
serverSocket.listen(2)

#Message for both clients to receive
message = "The server is ready to receive"

#Creates sockets to connect to the server
Alice, addr = serverSocket.accept()
Bob, addr = serverSocket.accept()

#Sends the messgae to "Alice" and "Bob"; X and Y respectively
Alice.send(message.encode())
Bob.send(message.encode())

#Receives messages from clients
X = Alice.recv(1024)
Y = Bob.recv(1024)

#Prints messages received from the clients
print(X.decode())
print(Y.decode())

#checks to see which message was 1st
comp = "Y: Bob received before X: Alice" if Y > X  else "X: Alice received before Y: Bob"

print (comp)#Print the comparison of the comparison

#send the aknowledgements back to the TCP clients (Alice and Bob)
Alice.send(comp.encode())
Bob.send(comp.encode())

print("Sent acknowledgment to both X and Y")

#close connections
Bob.close()
Alice.close()