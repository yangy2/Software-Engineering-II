# Yilin Yang
# Software Engineering Web Apps HW6

# INSTRUCTIONS
This assignment was developed in Python3. Two files are provided:
	server.py
	client.py
You may run a program using the example notation: 

python3 ./filename.py


Alternatively, you may directly execute the file by double-clicking it.

Please execute server.py first; client.py searches for a host to connect to,
which will not exist unless first established by server.py. 

Three commands are recognized: GET, BOUNCE, and EXIT. Input is case-
sensitive, i.e. it will not recognize "get" as "GET". The program should
acknowledge syntax errors. server.py will continuously run in the 
background. client.py will run until a successful EXIT command input.

Example on Client side:
>>Enter Command: GET test1.txt
        Sent: "GET test1.txt"
        Response: "Successfully retrieved test1.txt"
>>Enter Command: BOUNCE hello world
        Sent: "BOUNCE hello world"
        Response: "hello world"