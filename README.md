### Setting up an adhoc network between computers A and B

1) Find out the device names on both computers, this can be done with ifconfig.

Example:

    wlp4s0    Link encap:Ethernet  HWaddr 30:3A:64:53:57:69
              inet addr:10.0.0.5  Bcast:10.0.0.255  Mask:255.255.255.0
              inet6 addr: 2601:1c0:4f01:a849:9d8b:87c8:dec5:f2c4/64 Scope:Global
              inet6 addr: 2601:1c0:............. etc..

 ^^ This is your device name (wlp4s0).

2) On computer A (the host) run the following:
    sudo ./dual.sh $devicename $physicalname $ipaddress

This will enable an ad-hoc wireless network on computer A.
Some operation systems have different daemon names and the script may not properly kill all networking daemons. If you suspect this to be the case (for instance if your gui shows you connected to a network) you will have to manually kill these daemons through systemctl or service.

3) On computer B (the client) run the following:
    sudo ./dual $devicename $physicalname $ipaddress

If all goes well the computers should associate to each other. You can test this by typing:
    ping 10.0.0.10
from the host computer, or:
    ping 10.0.0.8
from the client.

### Using the connection

After this you should be able to send udp data beteen the computers using either netcat or the python scripts found in the testing directory.

#### nc example

host:
    nc -luv 4444 > out.txt

client:
    echo "hello world" | nc -u 10.0.0.8 4444

#### Python

Check out the README.md file in the testing directory.
