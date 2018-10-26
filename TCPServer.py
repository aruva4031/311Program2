from socket import *
bye = False
bob_count = 0
alice_count = 0
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
comp = "X: Alice received before Y: Bob" if X < Y else "Y: Bob received before X: Alice"

print (comp)#Print the comparison of the comparison

#send the aknowledgements back to the TCP clients (Alice and Bob)
Alice.send(comp.encode())
Bob.send(comp.encode())

print("Sent acknowledgment to both X and Y")
X = None
Y = None

while bye == False:
    X = Alice.recv(1024)
    Y = Bob.recv(1024)
    if X is not None:
        Bob.send(X)
        bob_count = bob_count + 1
    if Y is not None:
        Alice.send(Y)
        alice_count = alice_count + 1
    if X.decode() == "Bye" or Y.decode() == "Bye":
        bye = True
        Bob.send("Ending Session")
        Alice.send("Ending Session")
        Bob.send("Bob Message Count: " , bob_count , " Alice Message Count: ", alice_count)
        Alice.send("Bob Message Count: " , bob_count , " Alice Message Count: ", alice_count)
    Y = None
    X = None
#close connections
Bob.close()
Alice.close()
