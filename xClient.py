from socket import *
from select import *
bye = False
clientSocket = socket(AF_INET, SOCK_STREAM)

# Assigns IP address and port number to socket
# Connection will establish a  3-way-handshake
clientSocket.connect(('localhost', 12000))

# Client message for the server
sentence = 'Client X: Alice'
message =''

# Prints the message the server sent to the client.
print (clientSocket.recv(1024).decode())

# Prints the message to send to the server.
print(sentence)

# Sends message to the server
clientSocket.send(sentence.encode())

# Print the acknowledgement or the message the server sent back to the client.
print(clientSocket.recv(1024).decode())

sentence = None
clientSocket.settimeout(1)
while bye == False:
    try:
        message = str(clientSocket.recv(1024).decode())
        print("Bob: ", message)
        if message == "Ending Session":
            bye = True
            print(clientSocket.recv(1024).decode())
            print(clientSocket.recv(1024).decode())
            break
    except timeout:
        sentence = input("You: ")
        clientSocket.send(sentence.encode())
    
#Close socket
clientSocket.close()
