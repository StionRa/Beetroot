import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8888))  # Server binding to a local address and port
data = 'Hello, server!'
sock.sendto(data.encode(), ('example.com', 12345))  # Send data to the server

received_data, server_address = sock.recvfrom(1024)  # Receive data and server address
print(received_data.decode())
sock.close()
