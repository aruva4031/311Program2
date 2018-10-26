from socket import *
bye = False
clientSocket = socket(AF_INET, SOCK_STREAM)

# Assigns IP address and port number to socket
# Connection will establish a  3-way-handshake
clientSocket.connect(('localhost', 12000))

# Client message for the server
sentence = 'Client Y: Bob'

# Prints the message the server sent to the client.
print (clientSocket.recv(1024).decode())

# Prints the message to send to the server.
print(sentence)

# Sends message to the server
clientSocket.send(sentence.encode())

# Print the acknowledgement or the message the server sent back to the client.
print(clientSocket.recv(1024).decode())

sentence = None
while bye == False:
    sentence = input("Enter Message: ")
    print(sentence)
    clientSocket.send(sentence.encode())
    print(clientSocket.recv(1024).decode())
    if clientSocket.recv(1024).decode() is not None:
         print("Alice: " , clientSocket.recv(1024).decode())
    if clientSocket.recv(1024).decode() == "Ending Session":
        bye = True
        print(clientSocket.recv(1024).decode())
        print(clientSocket.recv(1024).decode())
        break
    
    
    
#Close socket
clientSocket.close()
