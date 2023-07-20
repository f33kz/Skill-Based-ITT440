import socket
import threading
import random

quotes = [
    "Jangan sekali-kali kita meremehkan sesuatu perbuatan baik walaupun hanya sekadar senyuman.",
    "Dunia ini umpama lautan yg luas. Kita adalah kapal yg belayar di lautan telah ramai kapal karam didalamnya.. andai muatan kita adalah iman, dan layarnya takwa, nescaya kita akan selamat dari tersesat di lautan hidup ini.",
    "Hidup tak selalunya indah tapi yang indah itu tetap hidup dalam kenangan.",
    "Setiap yang kita lakukan biarlah jujur kerana kejujuran itu telalu penting dalam sebuah kehidupan. Tanpa kejujuran hidup sentiasa menjadi mainan orang.",
    "Hati yg terluka umpama besi bengkok walau diketuk sukar kembali kepada bentuk asalnya."
]

def get_random_quote():
    return random.choice(quotes)

def handle_client(client_socket):
    print("Connected from client:", client_socket.getpeername())
    quote = get_random_quote()
    client_socket.send(quote.encode())
    client_socket.close()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.138.128', 8888))
server_socket.listen(5)
print("Quote of the Day server is running on port 8888...")

while True:
    client_socket, addr = server_socket.accept()
    client_socket.send(b'Successfully connected to QOTD server!')
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()

