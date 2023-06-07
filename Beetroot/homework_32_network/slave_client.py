import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
server_address = ('localhost', 8000)
client_socket.connect(server_address)

# Send data to the server
message = "Hello, server!"
client_socket.sendall(message.encode())

# Receive the response from the server
response = client_socket.recv(1024)
print('Received from server:', response.decode())

# Close the socket
client_socket.close()
