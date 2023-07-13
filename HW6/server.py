# Yilin Yang
# Software Engineering Web Apps HW6

import socket
import sys

GETparse = 3
BOUNCEparse = 6
EXITparse = 4
space_syntax = 32

# Function to retrieve contents of specified file
def GET(data):

    length = len(data)
    
    # Not enough information given
    if length == GETparse or (length == GETparse+1 and data == "GET "):
        print("\tno further parameters given")       
        data = "Please provide parameters for GET"

    # Improper syntax
    elif ord(data[GETparse]) != space_syntax:
        print("\tbad syntax")
        data = "Error: Please include a space between command and parameter"

    # Get file    
    else:
        print("\tGetting " + data[GETparse+1:length])

        # Search for file and print contents
        try:
            file = open(data[GETparse+1:length], "r")
            print(file.read())
            data = "Successfully retrieved " + data[GETparse+1:length]

        # File not found
        except IOError: 
            data = data[GETparse+1:length] + " - File Not Found"
            print("\t" + data)

    return data

# Function to print specified text
def BOUNCE(data):

    length = len(data)

    # Not enough information given
    if length == BOUNCEparse or (length == BOUNCEparse+1 and data == "BOUNCE "):
        print("\tno further parameters given")
        data = "Please provide parameters for BOUNCE"

    # Improper syntax
    elif ord(data[6]) != space_syntax:
        print("\tbad syntax")
        data = "Error: Please include a space between command and parameter"
        
    # Print input
    else:
        print("\t" + data[BOUNCEparse+1:length])
        data = data[BOUNCEparse+1:length]

    return data

# Function to close connection with client
def EXIT(data, connection):

    length = len(data)
    failed = False
    
    data1 = "Exit Code - "
    # Standard exit procedure
    if length == EXITparse or (length == EXITparse+1 and data == "EXIT "):
        data2 = "Normal Exit"
        data = data1 + data2

    # Improper syntax
    elif ord(data[EXITparse]) != space_syntax:
        print("\tbad syntax")
        data = "Error: Please include a space between command and parameter"
        failed = True

    # Exit with input code
    else:
        data2 = data[EXITparse+1:length]
        data = data1 + data2

    if not failed:
        print("\tsending data back to the client")
        connection.sendall(data.encode())
        print("\tExiting...")    
        connection.close()
        print(">>connection with " + str(client_address) + " closed\n")
        
    return (data, failed)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on %s port %s' % server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print(">>waiting for a connection")
    connection, client_address = sock.accept()
    
    try:
        print('>>connection from', client_address)

        # Wait for data
        while True:
            print(">>waiting for input")
            data = connection.recv(4096)
            data = data.decode()

            # Received something
            if len(data)>0:
                print('\treceived "%s"' % data)

                # GET command recognized
                if data[:3] == "GET":
                    data = GET(data)

                # BOUNCE command recognized
                elif data[:6] == "BOUNCE":
                    data = BOUNCE(data)

                # EXIT command recognized
                elif data[:4] == "EXIT":
                    status = EXIT(data, connection)
                    data = status[0]
                    failed = status[1]
                    if not failed: break

                # Command not recognized                   
                else:
                    print("\tcommand not recognized")
                    data = "command not recognized"

                # Send response to client
                print("\tsending data back to the client")
                connection.sendall(data.encode())
                    
            # Received Nothing
            else:
                print(">>no more data from", client_address)
                break

    finally:
        # Close connection with client
        connection.close()
