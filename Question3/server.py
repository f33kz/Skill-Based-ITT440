import socket

def convert_to_standard_atm(pressure_bar):
    # Conversion formula: 1 bar = 0.9869233 atm
    return pressure_bar * 0.9869233

s = socket.socket()
port = 8888
s.bind(('', port))
s.listen(5)
print("Waiting for client..")

while True:
    c, addr = s.accept()
    print("Connected to client: " + str(addr))
    c.send(b'Successfully connected to the server!')
    buffer = c.recv(1024)

    try:
        pressure_bar = float(buffer)
        atm = convert_to_standard_atm(pressure_bar)
        response = f"Pressure in standard atmospheres: {atm:.4f} atm"
    except ValueError:
        response = "Invalid input. Please send a valid pressure value in bar."

    c.send(response.encode())

    c.close()
