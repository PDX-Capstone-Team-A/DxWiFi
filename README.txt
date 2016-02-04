to set up adhoc networking between computer A and B

1) find out the device names on both computers, this can be done with ifconfig
	example:

wlp4s0    Link encap:Ethernet  HWaddr 30:3A:64:53:57:69  
          inet addr:10.0.0.5  Bcast:10.0.0.255  Mask:255.255.255.0
          inet6 addr: 2601:1c0:4f01:a849:9d8b:87c8:dec5:f2c4/64 Scope:Global
          inet6 addr: 2601:1c0:............. etc..

 ^^ this is your device name (wlp4s0)



2) on computer A (the host) run the following:
	sudo ./dual.sh $devicename $physicalname $ipaddress

	this will enable an ad-hoc wireless network on computer A.
	some operation systems have different daemon names and the script may not properly kill all networking daemons. if you suspect this to be the case (for instance if your gui shows you connected to a network) you will have to manually kill these daemons through systemctl or service

3) on computer B (the client) run the following:
	sudo ./associate $devicename $physicalname $ipaddress
	(as of the time I am writing this this script is untested so it may need some tweaking)

if all goes well the computers should associate to each other. you can test this by typing
ping 10.0.0.10
from the host computer, or
ping 10.0.0.8
from the client


note: the monitor mode script is not currently used


after this you should be able to send udp data beteen the computers using either netcat or the python scripts
nc example:

host:
nc -luv 4444 > out.txt

client:
echo "hello world" | nc -u 10.0.0.8 4444

python:
idk


