# UDP Packets

### These scripts are for sending and receiving UDP packets over a network.

#### For one Linux and one OS X machine:

On the Linux machine:

* Run the dual.sh script from the parent directory to set up a network called "rockets."  This computer's IP address is set to 10.0.0.8.

* Run receive.py and wait for sender.

On the OS X machine:

* Connect to the "rockets" network.

* In the TCP/IP tab under Advanced Wi-Fi Network Preferences, select "Manually" from the "Configure IPv4" dropdown. Then set the following fields:

```
IPv4 Address: 10.0.0.10
Subnet Mask: 255.255.255.0
```

* Run send.py with an integer command-line argument to specify how many packets to send.


#### Script arguments

##### send.py

send.py can take up to 4 arguments.

The first argument is the number of packets to send. It defaults to 20 packets. To change amount of packets, add the flag:
`-n <num of packets>`

The second argument is the delay in seconds between sendings of packets. It defaults to .001. To change the delay, add the flag:
`-d <delay>`

The third argument is the IP address to send to. It defualts to 10.0.0.8. To change the ip address, add the flag:
`-i <ip address to send to>`

The fourth argument is the Port to use. It defaults to 5005. To change the port, add the flag:
`-p <port>`

##### receive.py

receive.py can take up to 3 arguments.

The first argument is the distance between the sender and receiver. This only affects the output of the script. It defaults to 0. To change the distance, add the flag:
`-d <distance>`

The second argument is the IP address of the machine. YOU MUST SPECIFY THE IP OF THE MACHINE USED TO RECEIVE MESSAGES. This defaults to 10.0.0.8. To change the ip address, add the flag:
`-i <ip address of machine>`

The third argument is the port to use. It defaults to 5005. To change the port, add the flag:
`-p <port>`
