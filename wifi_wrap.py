#!/usr/bin/python

"""
History:
    rev 1 - Jon-Erik - script skeleton
    rev 2 - Jon-Erik - add support for auto tests

"""
import argparse, os

#
# The purpose of this script is to wrap dual.sh and check that necessary arguments are supplied
# by the user. The script also provides user help and allows user to put args in any order.
#
# Command Line Options:
#   -h : help
#   -i : desired ip address
#   -d : physical device / wifi driver (e.g. phy0)
#   -c : wifi card name (e.g. wlan0)
#   -pwr : set txpower in dBm (e.g. 30)
#
#       e.g. python wifi_wrap.py -i 10.0.0.9 -d phy0 -c wlan0
#
#   -restart : reset machine to original settings
#
#       e.g. python --restart 
#
def parse_args():

    #arg parsing

    arg = len(sys.argv)
    if arg == 1 and sys.argv[2] == '-restart':
	os.execv('./wifi_back_on.sh', ["sudo", "wifi_back_on.sh"])
 
    parser = argparse.ArgumentParser(description = 'Python wrapper + argument parser for dual.sh wifi script')
    parser.add_argument('-i', '-ip', required=True, help='e.g. 10.0.0.9')
    parser.add_argument('-d', '-driver', required=True, help='e.g. phy0')
    parser.add_argument('-c', '-card', required=True, help='e.g. wlan0')
    parser.add_argument('-pwr', '-power', help='set txpower in dBm (e.g. 30)', default=20 )
    parser.add_argument('-t', '-test', help='run testing scripts send.py, receive.py')

    #standard args parse
    args = parser.parse_args()

    os.execv('./dual.sh', ["sudo", "sh", "dual.sh", "-c", str(args.c),  "-d", str(args.d), "-i", str(args.i)])
    # "-pwr", str(args.pwr)

def run_tests(argT):
    if argsT is not None:
        script = input("Type 'S' for sender, 'R' for receiver: ").upper()
        if script == 'S':
            sender()
        if script == 'R':
            receiver()
        else:
            print 'Unrecognized Input...\n\n'
            run_tests(argT)                         # change to while loop if preferred
            return
    else:
        return

def sender():
    packets = input("# of Packets to Send [20]: ")
    delay   = input("Time Delay in Seconds [.001]: ")
    ipAddr  = input("IP Address to Send To [10.0.0.8]: ")
    port    = input("Port [5005]: ")

    if not packets:
        packets = '20'
    if not delay:
        delay = '.001'
    if not ipAddr:
        ipAddr = '10.0.0.8'
    if not port:
        port = '5005'

    os.execv('./testing/send.py', ["python3", "send.py", packets, delay, ipAddr, port])

def receiver():
    dist    = input("Distance of Test [None]: ")
    ipAddr  = input("IP Address of Receiver [10.0.0.8]: ")
    port    = input("Port [5005]: ")

    if not dist:
        dist = None
    if not ipAddr:
        ipAddr = '10.0.0.8'
    if not port:
        port = '5005'

    os.execv('./testing/receive.py', ["python3", "receive.py", dist, ipAddr, port])


parse_args()
run_tests(args.t)
