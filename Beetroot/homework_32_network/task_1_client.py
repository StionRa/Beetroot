import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 8000)

# Send a message to the server
message = "Hello, server!"
client_socket.sendto(message.encode(), server_address)

# Receive the response from the server
response, _ = client_socket.recvfrom(1024)
print('Received from server:', response.decode())

# Close the socket
client_socket.close()
