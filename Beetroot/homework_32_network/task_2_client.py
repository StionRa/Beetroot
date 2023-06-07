import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Server address and port
server_address = ('localhost', 8000)

# Send the encryption key to the server
key = 3
key_message = str(key)
client_socket.sendto(key_message.encode(), server_address)

# Send the data message to the server
message = "Hello, server!"
client_socket.sendto(message.encode(), server_address)

# Receive the encrypted response from the server
response, _ = client_socket.recvfrom(1024)
print('Received from server:', response.decode())

# Close the socket
client_socket.close()
