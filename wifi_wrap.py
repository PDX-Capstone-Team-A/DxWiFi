#!/usr/bin/python3

"""
History:
    rev 1 - Jon-Erik - script skeleton
    rev 2 - Jon-Erik - add support for auto tests
    rev 3 - Jon and Jon-Erik - adding subprocess and more logic
"""
import argparse, os, sys, subprocess

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
#       e.g. sudo python3 wifi_wrap.py -i 10.0.0.9 -d phy0 -c wlan0
#
#   -restart : reset machine to original settings
#
#       e.g. sudo python3 -restart wlan1
#
def parse_args():

    #arg parsing

    arg = len(sys.argv)
    if arg <= 2:
        help()
        sys.exit(1)

    if arg == 3  and (sys.argv[1] == '-restart' or sys.argv[1] == '-r'):  # make sure this is argv[2] instead of argv[1]
        subprocess.call(["./wifi_back_on.sh", sys.argv[2]])
        sys.exit(1) 
    
    parser = argparse.ArgumentParser(description = 'Python wrapper + argument parser for dual.sh wifi script')
    parser.add_argument('-i', '-ip', required=True, help='e.g. 10.0.0.9')
    parser.add_argument('-d', '-driver', required=True, help='e.g. phy0')
    parser.add_argument('-c', '-card', required=True, help='e.g. wlan0')
    parser.add_argument('-pwr', '-power', help='set txpower in dBm (e.g. 30)', default=20 )
    parser.add_argument('-t', '-test', action='store_true',  help='run testing scripts send.py, receive.py')

    #standard args parse
    args = parser.parse_args()
    subprocess.call(["./dual.sh", str(args.c), str(args.d), str(args.i)])
    # "-pwr", str(args.pwr)
    return args.t

def run_tests(argT):
    if argsT:
        script = input("Type 'S' for sender, 'R' for receiver: ").upper()
        if script == 'S':
            sender()
        if script == 'R':
            receiver()
        else:
            print("Unrecognized Input...\n\n")
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

    os.execv('./testing/send.py', ["python3", "send.py", int(packets), delay, ipAddr, port])  # fix this line after receive.py get's updated

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

    os.execv('./testing/receive.py', ["python3", "receive.py", int(dist), ipAddr, port])  # fix this line after receive.py get's updated

def help():
    print("\n <>--Help Menu--<>")
    print("\n Example usage:\n")
    print(" To restart WiFi -> sudo python3 wifi_wrap.py -restart wlan1\n")
    print(" Setup non-default adhoc Wifi -> sudo python3 wrap.py -i 10.0.0.10 -d phy1 -c wlan1\n")
    print(" Setup defualt adhoc Wifi & Test -> sudo python3 wrap.py -i 10.0.0.10 -d phy1 -c wlan1 -t")
    print("\n\n Optional Options:")
    print(" -i <IP>\t\tUse to pick IP Address. Default: 10.0.0.8")
    print(" -d <driver>\t\tUse to pick phy#. Default: phy0")
    print(" -c <card>\t\tUse to pick device. Default: wlan0")
    print(" -pwr <integer>\t\tUse to pick txpower in dBm . Default: 20")
    print(" -t\t\t\tUse -t to turn on testing, follow the instructions on screen\n\n")

argsT = parse_args()
run_tests(argsT)
