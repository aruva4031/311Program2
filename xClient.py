from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)

# Assigns IP address and port number to socket
# Connection will establish a  3-way-handshake
clientSocket.connect(('localhost', 12000))

# Client message for the server
sentence = 'Client X: Alice'

# Prints the message the server sent to the client.
print (clientSocket.recv(1024).decode())

# Prints the message to send to the server.
print(sentence)

# Sends message to the server
clientSocket.send(sentence.encode())

# Print the acknowledgement or the message the server sent back to the client.
print(clientSocket.recv(1024).decode())

#Close socket
clientSocket.close()