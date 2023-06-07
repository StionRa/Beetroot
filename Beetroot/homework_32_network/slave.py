import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_address = ('localhost', 8000)
server_socket.bind(server_address)

# Listen for incoming connections
server_socket.listen(1)

print('Server listening on {}:{}'.format(*server_address))

while True:
    # Wait for a client to connect
    print('Waiting for a connection...')
    client_socket, client_address = server_socket.accept()
    print('Accepted connection from {}:{}'.format(*client_address))
    print("Client her!!")

    # Receive and send back data
    while True:
        data = client_socket.recv(1024)
        if not data:
            # No more data, connection closed
            print('Connection closed by {}:{}'.format(*client_address))
            break

        # Echo the received data back to the client
        client_socket.sendall(data)

    # Close the client socket
    client_socket.close()
