import socket

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('0.0.0.0', 8000))
server_socket.listen(1)

print('listening...')

while True:    
    # wait for connection
    client_connection, client_address = server_socket.accept()

    # get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # send
    response = "HTTP/1.1 418 I'm a teapot\n\nI'm a teapot"
    client_connection.sendall(response.encode())
    client_connection.close()

# close socket
server_socket.close()