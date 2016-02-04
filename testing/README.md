# UDP Packets

### These scripts are for sending and receiving UDP packets over a network.

##### For one Linux and one OS X machine:

On the Linux machine: 

* Run the init_wifi_ad_hoc.sh script from the wifi_scripts repo to set up a network called "rockets."  This computer's IP address is set to 10.0.0.8.

* Run receive.py and wait for sender.

On the OS X machine:

* Connect to the "rockets" network.

* In the TCP/IP tab under Advanced Wi-Fi Network Preferences, select "Manually" from the "Configure IPv4" dropdown. Then set the following fields:

```
IPv4 Address: 10.0.0.10
Subnet Mask: 255.255.255.0
```

* Run send.py with an integer command-line argument to specify how many packets to send.


##### Updates to scripts:

send.py now can take up to 3 arguments. 

The first argument is the number of packets to send. it defaults to 20 packets at this time. To change amount of packets:
	python send.py <num of packets>

The second argument is the IP address to send to. It defualts to 10.0.0.8. If you want to change ip address:
	python send.py <num of packets> <ip address to send to>

The third argument is the Port to use. It defaults to 5005. If you want to change port:
	python send.py <num of packets> <ip address to send to> <port>

Recieve has two different scripts. One is just a receive, which puts all information on the screen. This is meant to be used to test connection. The receiveandprint.py will take the information and store it in a .txt file that is @ seperated. Both can take up to 2 arguments.

The first argument is the IP address of the machine. YOU MUST SPECIFY THE IP OF THE MACHINE USED TO RECEIVE MESSAGES. This defaults to 10.0.0.8. if you want to change the ip address:
	python receive.py <ip address of machine>

The second argument is the port to use. It defaults to 5005. If you want to change port:
	pythong receive.py <ip address of machine> <port>
