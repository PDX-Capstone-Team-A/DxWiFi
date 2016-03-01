#Meeting History
Documentation: 

This is a first pass at documenting some of the steps that we took in our process and what we were able to find. Feel free to change the format and add everything that you can. I decided to organize the documentation into a series of sprints and breakdown some of the challenges / results throughout the process. I used this as a brain dump to include all of the notes that I’ve taken. Sprints 1, 2, 3 might be good for a presentation but maybe not necessary for psas. 

My memory is average at best so also feel free to add corrections to my notes!


Sprint 1 - Project Selection

Requirements: Listen to presentations from the group of candidates. Discuss, vote, and prepare to present our top choices. 

Challenges: Fairly selecting a project that we all had interest in. To account for this, we completed a survey for each of the presentations, and re-voted on our top 6. At the end of the voting process the PSAS Wifi project was our top selection. 

Results: We presented PSAS as our top choice and were selected. 


Sprint 2 - Initial Meetings and Project Overview

Requirements: Learn about PSAS and their previous launches. Develop an understanding of the goals for our capstone project. 

Challenges: Somewhat of a steeper learning curve. Wifi / Networking is something that some of us had a bit of experience in, but as a group we were required to get up to speed quickly. The project involved a good amount of research and documentation of what we learned along the way. 

Results: Understood the guidelines for our project. Gave us the information needed to devise a plan to deliver. 


Sprint 3 - Creating a Plan of Attack 

Requirements: Generate minimum viable product, stretch goals. 

Challenges: Setting a reachable goal without knowing a lot of background on the subject.

Results: Minimum viable product includes driver and kernel modifications to create a connection between two machines, transmit data across the machines, and document all research, findings. Stretch goals include optimizing for long distance transmissions, and performing a successful long-distance test. 


Sprint 4 - Background Research

Requirements: Make sure that the driver (ath9k_htc) is optimal for long-distance wifi. Learn about some of the useful techniques for packet sending. Research linux distributions, wifi protocols, etc. Understand the basics of networking and general wifi. 

Challenges: Steep learning curve. Large amount of information to weed through. 

Results: ifconfig, iwconfig, and netcat are early options for modifications. Ath9k driver is probably the right choice. Modification of the ath9k driver code will probably not be necessary. Distribution is mostly up to us, and we found that Ubuntu will work fine for our project. 

Sprint 5 - Meeting with Professor Singh 

Requirements: Interview Professor Singh to get his thoughts on directions we should take.

Challenges:

Results: A lot of what he told us was about the hardware that should be used, which isn’t applicable to what we are working on specifically, but he did recommend that we send in ad-hoc mode and provided some information that we maybe could use for a stretch goal including fountain codes and software-defined radio.

Sprint 6 - Automated Pairing and Packet Sending


// Someone who can comment on Monitor, Ad-Hoc mode, etc. add notes here!! 

Requirements: Come up with a way to automatically connect two machines (Ground, Satellite), and successfully send data across the table. 

Challenges: This sprint included lots of trial and error. The research on packet sending over long distances isn’t well documented because wifi isn’t generally made for long distance. Because of this, the main challenge was creating a solution without a lot of direction. 

Results: Wireshark was an important tool to monitor packets from the sending computer. The first step was to make sure that the sending machine was transmitting data. After confirming this with wireshark, the goal was to pair to the receiving machine, and pipe the results into a file. Here’s a breakdown of some of the findings we made during this sprint: 

Satellite netcat command: 	nc -u -v <ip of receiver> <port> 
				e.g. nc -l -u -v 10.0.0.4 4444

Ground netcat command:	nc -l -u -v <port>
				e.g. nc -l -u -v 4444

* -l command switches on listen mode
* -u for udp protocol
* -v for verbose 

To connect the two machines, we wrote two shell scripts. One, called init_wifi_ad-hoc.sh, places the machine it’s run on into ad-hoc mode and also begins broadcasting an IBSS (Independent Basic Service Set) or ad-hoc network. An ad-hoc network allows two machines to communicate directly to each other without any network infrastructure. The second script, associate.sh, simply causes the machine it’s run on to enter ad-hoc mode and connect to the established ad-hoc network. 

Sprint 7 - Disabling RTS / CTS and other Unimportant Processes

Requirements: Data should be sent without unnecessary signals from satellite to ground.

Challenges: There are several different places that these signals could be set (linux kernel, driver, etc.) and finding the right place is important. Finding a tool to monitor these transmissions is also a challenge (wireshark ignores them by default). 

Results: In wireshark, we were able to locate a deeply nested preference that showed RTS / CTS packets. We were able to set the rate of these packets to high, see the packets being transmitted, switch them off in the kernel (command shown below) and confirm that they were no longer being sent. 

Wireshark option path: 	 preferences → protocols → display hidden protocol items. 

Kernel command to disable RTS / CTS packets : 	iw phy phy(1|0) set rts -1

The command was put in both the init_wifi_ad-hoc.sh and associate.sh scripts to automatically disable RTS/CTS when the machines are placed into ad-hoc mode using either script. 

Sprint 8 - Optimizing Workflow

Requirements: Create a workflow that could be mirrored by a satellite and ground software package. When the satellite is in range to send data, the satellite needs to be ready to send packets and the ground software should be ready to receive. 

Challenges: 

Results: 

Sprint 9 - Testing Methods

Requirements: Sender and receiver scripts to automate the transfer of packets, and a way to imitate/induce high latency.

Challenges: Since the goal of the project is to allow a Wi-Fi connection to operate at long distances and high latency, we needed a way to imitate that in testing to see if what we were doing had any impact in high-latency situations.

Results: We wrote two Python scripts that use sockets to send UDP packets (containing text strings listing a given packet’s number) from one machine (running the send.py script) to another (running the receive.py script). The receiver script prints the number of packets that were received, and lists every packet it got with a timestamp. 

For imitating high latency, we looked at Linux Netem to add delays to all packets sent from or received by a machine.

For example, the following Netem command induces a latency of 100ms to all packets sent or received:
tc qdisc add dev <device name> root netem delay 100ms

Running the command on both the machine sending packets and the machine receiving packets will induce a net delay of 200ms.

Sprint 10 - Documentation and Delivery

Requirements: GitHub wiki and brain dump of all that we have learned over the course of this project.

Challenges: Consistent formatting and centralization of all information

Results: 



Sections: 

Project Selection
Initial Requirements
Generate Plan of Attack (MVP, stretch)
Initial Research
Suresh Brain Dump
Automated Pairing and Sending Data
Disabling RTS / CTS and Other Unimportant Processes
Optimizing Workflow
Testing Methods
Documentation and Delivery
