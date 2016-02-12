#!/usr/bin/env python3

import sys, os, socket, argparse, ipaddress, datetime, select, csv

#
# Usage: 
#
# receive.py [-d distance] [-i ip] [-p port]
#
# arg       type        default     description
# ---------------------------------------------------------------------------------
# distance  int         0           distance in meters between sender and receiver
# ip        string      10.0.0.8    IPv4 address of receiver/this computer
# port      int         5005        port used
#

OUTPUT = "wifi_test_data.csv"

# Parse arguments
parser = argparse.ArgumentParser(
    prog="receive.py",
    description='Receive UDP packets across an ad-hoc network.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--distance", type=int, default=0, metavar='', help="distance in meters between sender and receiver (type: %(type)s)")
parser.add_argument("-i", "--ip", type=str, default="10.0.0.8", metavar='', help="IPv4 address of receiver/this computer (type: %(type)s)")
parser.add_argument("-p", "--port", type=int, default=5005, metavar='', help="port used (type: %(type)s)")

args = parser.parse_args()

# Setup socket
try:  # Validate IPv4 address
    UDP_IP = str(ipaddress.IPv4Address(args.ip))
except ipaddress.AddressValueError:
    print(args.ip + " is not a valid IPv4 address.")
    sys.exit()

UDP_PORT = args.port

sock = socket.socket(socket.AF_INET,  # Internet
                     socket.SOCK_DGRAM)  # UDP
try:
    sock.bind((UDP_IP, UDP_PORT))
except:
    print(str(UDP_IP) + " is not the IP address of this computer.\nThis computer's IP address may have been configured by the calling program.")
    sys.exit()

# Setup csv file for output
test = os.path.isfile(OUTPUT)
if test == False:
    csv = open(OUTPUT, "a")
    csv.write("test_number,file_sent,total_sent,time_sent,delay,number_received,time_received,distance" + "\n")
    test_number = 1
else:
    reader = csv.reader(open(OUTPUT), delimiter=',')
    for row in reader:
        test_number = row[0]
    if test_number == "test_number":
        test_number = 0
    csv = open(OUTPUT, "a")
    test_number = int(test_number) + 1

# Receive packets and write info for each to output file
print ("test number:", test_number)
print("Enter 'Ctrl+C' to stop receiving")

count = 0
try:
    while True:
        data, addr = sock.recvfrom(1024)  # Buffer size is 1024 bytes
        count += 1
        csv.write(str(test_number) + "," + data.decode("utf-8") + "," + str(count) + "," + str(datetime.datetime.now()) + "," + str(args.distance) + "\n")
        print(data.decode("utf-8"))
except KeyboardInterrupt:
    pass

# Display session statistics
print ("\nTotal number of packets received:", count)
if test == False:
    print ("File created:", csv.name)
else:
    print ("Data appended to: " + csv.name + " under test number: " + str(test_number))
csv.close()
