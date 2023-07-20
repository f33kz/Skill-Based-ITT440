import socket

def get_pressure_from_user():
    while True:
        try:
            pressure_bar = float(input("Enter pressure value in bar: "))
            return pressure_bar
        except ValueError:
            print("Invalid input. Please enter a valid number.")

s = socket.socket()
port = 8888
s.connect(('192.168.138.128', port))

data = s.recv(1024)
print(data.decode())

pressure_bar = get_pressure_from_user()
s.send(str(pressure_bar).encode())

response = s.recv(1024)
print(response.decode())

s.close()
