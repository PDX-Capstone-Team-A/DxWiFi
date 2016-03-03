This gives an in depth look at the script and extensive explanation as to what we did and why. 

##IP Suite
There are 7 layers to the OSI Model. Some relevant layers are:
* Data Link Layer
	* This consists of communication that doesn't always show up in Wireshark using default settings. 
	But there are settings to enable this to make Wireshark show this information.
* Network Layer
	* Contains information about IP Addresses
	* As far as we know, everything on the Internet layer and above is currently working for support for 
	long distance communications
* Transport Layer
	* UPD Layer: Great for long distance WiFi (the catch is that it is lossy)
	* TCP Layer: This has additional verification requirements and will not work for long distance WiFi
	as the handshakes between each packet time out before making the distance
* Application layer
	* This is your programming layer (e.g. Python...)

##Setup
We tested this using many different network cards and all code is hardware agnostic expect for 
 the broadcast rate settings (certain cards support different broadcast rates and are not continuous
 across spectrums, e.g. Card a support broadcasting at 1mbps 6mbps 11mbps while card b support 
 broadcasting at 2mbps 8mbps 12mbps. This has no effect on their ability to communication between 
 Card A and Card B, although we have been asked to leave this user configurable due to possible physical
 limitations)

##Software
All computers used for testing were running Linux kernel 3.4 or later. Kernels as far back as 2.6 *should* work but 
we have not tested it. 

###Network utilities
There are two kinds of network utilities.

<code>ifconfig</code> and <code>iwconfig</code> are still functional on all Linux builds but are deprecated and
are not suggested for use. 

<code>ip</code> and <code>iw</code> are their replacements for the above commands. Our scripts use this for forward
looking reasons. 

###Line by line detailed explanation of the script
This explanation explains line by line why we wrote it the way we did. 

####Lines 18-26
i) Linux runs daemons (background processes) that typically handle networking. 
	These are distribution specific and might need to be changed per distro. 
	There are two primary daemon managers that all linux distributions use: 
	systemd (more popular), and upstart (currently being phased out)
	1) upstart
		a) Ubuntu <= v.14
	2) Systemd
		a) Most other linux based systems use this daemon manager.
ii) These must be disabled in order to allow for manual control of the networking hardware as the daemons might change configurations. There are many different daemons which control networking hardware but the most common is called NetworkManager. This script is written currently using a NetworkManager solution but if your distro uses a different network daemon the process to disable it will be similar. 
iii) Upstart solution (line 25)
iv) Systemd solution (line 20)
 
####Line 29
i. Sets the device down (sort of "off") to allow for configuration changes which cannot be made when the device is up (on)
ii. Linux names the device drivers & device hardware (logical devices and physical devices). 
	1) In order to view device names, you can type "ip addr"
		a) Typical device names are similar to wlan0, wlan1…, wlp4s0, wlp4s1…, etc. (device lo does not control Wi-Fi, and any device starting with e.g. en1, … controls only Ethernet ports)
	2) In order to list physical devices use iw list. 
		a) Typical physical device names are phy0, phy1…,

####Line 30
Sets the device into ad-hoc mode (referred to as ibss)

####Line 31
i. Remove any previous ip address settings 

####Line 32
i. Set ip address and netmask for the device 
ii. Each device needs a distinct ip address and the same netmask to communicate with each other 
iii. The ip address is then used in the application layer to communicate between the two nodes
iv. Only the last field of the ip address needs to be set
v. The netmask should remain as 255.255.255.0 or in the notation used in the script as /24 (the 24 represents 24 out of 30 bits)

####Line 34
Set the device back up (on) to prepare for data transmission

####Line 36
Associate to the essid (this can be any string, but must be equal between devices)

####Line 37
i. Turn off RTS/CTS on the network device
ii. RTS/CTS (Request to Send/Clear to Send) is an optional protocol that will send a flag out if the byte size of a packet is greater than a given threshold. Setting this threshold to -1 disables this threshold. The purpose of this RTS/CTS packet is to solve a networking issue that arises when dealing with a "many-to-one" or "one-to-many" network topology. 

####Line 33
i. Set the channel to be fixed on transmission. 
ii. This addresses a physical limitation that a prior group noted: clouds could possibly interfere with the radio signal when the radio signal varies (we have yet to test this issue but are trusting the physics group).
