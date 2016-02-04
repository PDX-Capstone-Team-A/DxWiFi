#!/usr/bin/env python3
#possible issues: Might have issues because we only accept ipv4. Remove error checking or add extra checking
#if you need to use ipv6

# if you want to run default settings, then run python3 receive.py
# if you call with multiple args:
# first arg = distance of test
# second arg = receiving machine's IP
# third arg = port used

import socket
import sys
import select
import os
import datetime
import os.path
import csv

args = len(sys.argv)

if args < 2:
	distance = None
else:
	try:
		distance = int(sys.argv[1])
		if distance < 0:
			print("First argument (" + sys.argv[1] + ") (distance of test) must be a non negative integer. \n Exiting program")
			sys.exit()

	except ValueError:
		print("First argument (" + sys.argv[1] + ") (distance of test) must be a non negative integer. \n Exiting program")
		sys.exit()
if args < 3:
	UDP_IP = "10.0.0.8" #receivers ip address
else:
	UDP_IP = str(sys.argv[2])
	pieces = UDP_IP.split('.')
	if len(pieces) != 4:
		#if len(pieces) != 6:
		print("Second argument (" + sys.argv[2] + ") must be a valid ip4v address. \n Exiting program")
		sys.exit()
	try: 
		for p in pieces:
			if int(p) < 0:
				print("Second argument (" + sys.argv[2] + ") must be a valid ip4v address. \n Exiting program")
				sys.exit()
			elif int(p) >= 256:
				print("Second argument (" + sys.argv[2] + ")must be a valid ip4v address. \n Exiting program")
				sys.exit()
	except ValueError:
		print("Second argument (" + sys.argv[2] + ") must be a valid ip4v address. \n Exiting program")
		sys.exit()
if args < 4:
	UDP_PORT = 5005
else:
	try:
		UDP_PORT = int(sys.argv[3])
	except ValueError:
		print("Third argument (" + sys.argv[3] + ") (port to receive on) must be an integer. \n Exiting program")
		sys.exit()

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
try:
	sock.bind((UDP_IP, UDP_PORT))
except:
	print("Could not bind to the IP address provided. \nPlease provide the IP address of this computer as the second argument.")
	sys.exit()
filename = "wifi_test_data.csv"
test = os.path.isfile(filename)
#print filename
if test == False:
	csv = open(str(filename) , "a")
	csv.write("test_number,file_sent,total_sent,time_sent,delay,number_received,time_received,distance" + "\n")
	test_number = 1
else:
	reader = csv.reader(open(filename), delimiter=',')
	for row in reader:
		test_number = row[0]
	if test_number == "test_number":
		test_number = 0
	csv = open(str(filename) , "a")
	test_number = int(test_number) + 1
print ("test number:", test_number)
count = 0
print("Enter 'Ctrl+c' to stop receiving")
try:
	while True:
		data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
		count += 1
		csv.write(str(test_number) + "," + data.decode("utf-8") + "," + str(count) + "," + str(datetime.datetime.now()) + "," + str(distance) + "\n")
		print(data.decode("utf-8"))
except KeyboardInterrupt:
    pass
print ("\nTotal number of packets caught:", count)
if test == False:
	print ("File name created:", csv.name)
else:
	print ("Data appended to: " + csv.name + " under test number: " + str(test_number))
csv.close()
