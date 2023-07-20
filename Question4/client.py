import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('192.168.138.128', 8888))

welcome = client_socket.recv(1024)
print(welcome.decode())

received_quote = client_socket.recv(1024)
print("Received Quote of the Day from server:", received_quote.decode())

client_socket.close()
