# Yilin Yang
# Software Engineering Web Apps HW6

import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
address = ('localhost', 10000)
print('>>connecting to %s port %s' % address)
sock.connect(address)

while True:
    
    # Get user input
    while True:
        message = input('>>Enter Command: ')
        if len(message) > 0: break

    # Send data            
    print('\tSent: "%s"' % message)
    sock.sendall(message.encode())

    # Look for the response
    data = sock.recv(4096)
    data = data.decode()
    print('\tResponse: "%s"' % data)

    # Shut down for EXIT command
    if message[:4] == "EXIT" and data[:5] != "Error":
        print('>>closing socket')
        sock.close()
        break

print(">>program terminated")
