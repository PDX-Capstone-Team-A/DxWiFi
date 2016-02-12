#!/usr/bin/env python3

import sys, socket, argparse, ipaddress, datetime, time

#
# Usage: 
#
# send.py [-n numpackets] [-d delay] [-i ip] [-p port]
#
# arg           type        default     description
# ----------------------------------------------------------------------------
# numpackets    int         20          number of packets to send
# delay         float       .001        time delay in seconds between packets
# ip            string      10.0.0.8    IPv4 address of receiver
# port          int         5005        port used
#

# Parse arguments
parser = argparse.ArgumentParser(
    prog="send.py",
    description='Send UDP packets across an ad-hoc network.',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-n", "--numpackets", type=int, default=20, metavar='', help="number of packets to send (type: %(type)s)")
parser.add_argument("-d", "--delay", type=float, default=.001, metavar='', help="time delay in seconds between packets (type: %(type)s)")
parser.add_argument("-i", "--ip", type=str, default="10.0.0.8", metavar='', help="IPv4 address of receiver (type: %(type)s)")
parser.add_argument("-p", "--port", type=int, default=5005, metavar='', help="port used (type: %(type)s)")

args = parser.parse_args()

# Setup socket
try:  # Validate IPv4 address
    UDP_IP = str(ipaddress.IPv4Address(args.ip))
except ipaddress.AddressValueError:
    print(args.ip + " is not a valid IPv4 address.")
    sys.exit()

UDP_PORT = args.port

# Send packets
print ("\nSending...")
for num in range(1, args.numpackets + 1):
    print ("\tPacket number:", str(num))
    sock = socket.socket(socket.AF_INET,  # Internet
           socket.SOCK_DGRAM)  # UDP
    sock.sendto(
        str(num).encode('ascii') + b"," 
        + str(args.numpackets).encode('ascii') + b"," 
        + str(datetime.datetime.now()).encode('ascii') + b"," 
        + str(args.delay).encode('ascii'), (UDP_IP, UDP_PORT))
    time.sleep(float(args.delay))  # Pause specified number of seconds before sending next packet
