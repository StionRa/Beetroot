import socket


def caesar_encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + key) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + key) % 26 + 97)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text


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

    # Get the encryption key from the client
    key = int(data.decode())

    # Wait for the data message from the client
    data, client_address = server_socket.recvfrom(1024)
    print("Data:", data.decode())

    # Encrypt the data using the Caesar cipher with the key
    encrypted_data = caesar_encrypt(data.decode(), key)
    print("Encrypted data:", encrypted_data)

    # Send the encrypted data back to the client
    server_socket.sendto(encrypted_data.encode(), client_address)
