#!/usr/bin/env python3

# If you just call using python3 send.py, it will default to 20 packets, .001 second delay, 10.0.0.8 ip, 5005 as port.
# If you call with multiple args: 
# first arg = packets sent 
# second arg = time delay in seconds
# third arg = ip to send to
# fourth arg = port.

import socket
import sys
import datetime
import time

args = len(sys.argv) #get the number of args passed in. This is the list length, the first
					 #item in the list will always be the function name.

if args < 2: 
	tosend = 20 # defualt number of packets to send.
else:
	try:
		tosend = int(sys.argv[1]) #items to send passed in.
		if tosend < 1:
			print("First argument (" + sys.argv[1] + ") (number of packets to send), must be non negative integer \n Exiting program")
			sys.exit()
	except ValueError:
		print("First argument (" + sys.argv[1] + ") (number of packets to send), must be an integer \n Exiting program")
		sys.exit()
if args < 3:
	delay = .001
else:
	try:
		delay = float(sys.argv[2])
	except ValueError:
		print("Second argument (" + sys.argv[2] + ") (delay in seconds), must be a floating point. \n Exiting program")
		sys.exit()
	if delay < 0:
		print("Second argument (" + sys.argv[2] + ") (delay in seconds), must be a non negative floating point. \n Exiting program")
		sys.exit()
	if delay > .1:
		print("Because the delay is larger then .1, this test will take longer then general. \nThis test will take at least " + str((float(delay)*int(tosend))) + " seconds to run.")

if args < 4:
	UDP_IP = "10.0.0.8" # default ip address
else:
	UDP_IP = str(sys.argv[3])
	pieces = UDP_IP.split('.')
	if len(pieces) != 4:
		#if len(pieces) != 6:
		print("Third argument (" + sys.argv[3] + ") must be a valid ip4v address. \n Exiting program")
		sys.exit()
	try: 
		for p in pieces:
			if int(p) < 0:
				print("Third argument (" + sys.argv[3] + ") must be a valid ip4v address. \n Exiting program")
				sys.exit()
			elif int(p) >= 256:
				print("Third argument (" + sys.argv[3] + ") must be a valid ip4v address \n Exiting program")
				sys.exit()
	except ValueError:
		print("Third argument (" + sys.argv[3] + ") must be a valid ip4v address \n Exiting program")
		sys.exit()
if args < 5:
	UDP_PORT = 5005 # default port
else:
	try:
		UDP_PORT = int(sys.argv[4])
	except ValueError:
		print("Fourth argument (" + sys.argv[4] + ") (port to receive on) must be an integer. \n Exiting program")
		sys.exit()
MESSAGE = "Packet number "

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)

for num in range(1, tosend + 1):
    print ("message:", MESSAGE + str(num))

    sock = socket.socket(socket.AF_INET,  # Internet
           socket.SOCK_DGRAM)  # UDP
    sock.sendto(str(num).encode('ascii') + b"," + str(tosend).encode('ascii') + b"," + str(datetime.datetime.now()).encode('ascii') + b"," + str(delay).encode('ascii'), (UDP_IP, UDP_PORT))
    time.sleep(float(delay)) # Pause 1/1000th of a second before sending next packet
