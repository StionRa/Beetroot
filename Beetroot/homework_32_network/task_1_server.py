import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

print('Server listening on {}:{}'.format(*server_address))

while True:
    # Wait for a message from the client
    print('Waiting for a message...')
    data, client_address = server_socket.recvfrom(1024)
    print('Received message from {}:{}'.format(*client_address))
    print("Message:", data.decode())

    # Send a response back to the client
    response = "Hello, client!"
    server_socket.sendto(response.encode(), client_address)
