##Main Research Areas
The main research area, while we understood hardware was a critical
component to the success (or failure) of this project, focused
primarily on the software, 802.11 specifications and suggestions 
to make on technology choices with regard to software. 

###UDP
UDP was picked on the onset of the project. We knew that TCP/IP has inbuilt
overheads and timeouts that would require an acknowledgment which would
definitely time out too soon. UDP only sends out the packets with no expectation
that it will be received properly or at all. It also doesn't attempt to re-send
out the packets if it doesn't receive an acknowledgment. The trouble with this, 
however is that it is lossy. Files/data might not be received, it might
be received out of order, or much later. There are many solutions to 
resolve this and is investigated later on. 

###Multicasting
Instead of sending to a specific IP address, it will send to a group address. 
This has a slightly different netmask. In this case, anyone can assign their
networking address to the group address and it will receive the the data being
sent from the multicasting server. This removes the need for ACK's which was 
a bandwidth hog.  

###Driver && Firmware modification
Our research found that it was unnecessary to modify the drivers to make this successful. 

###Fountain Code
Fountain code is a data reconstruction technique discussed
[here](http://www.mit.edu/~gauri/FountainCodes.pdf). 
Essentially, on one end, the data is continually be distributed and on the other, it will 
wait until it has enough information to construct the data. 

##Suggestions for future research

##Other Alternatives Researched But Not Pursued
We investigate different routes and determine they were
not pertinent to the scope of our project but might interest
others.

1. OCB / P2P / V2X / wifi direct / other names

OCB stands for outside the context of a BSS

This was originally introduced to let vehicles and other items 
talk openly and freely directly with each other. Each item in 
a V2X system acts as both an AP (access point), and station. 
This lets items communicate without the handshake and authentication
generally associated with joining a network. It still does, however,
have security that can be used. Also, because each item in the 
network works as a station and an AP, there is no scanning for networks. 
The network must be hard coded in including channel and band used.

The major issue with OCB is that the 2012 version of 802.11 states that it must be used on the 5.9 Ghz band. This is prohibitive on the antennas we have available. There is a loophole currently that the 3.x current version of linux does have OCB available, but does not limit it to the 5.9 Ghz band, so could be used in current computers. We are just unsure if future Linux kernels will have the restriction, or not. So if the restriction was put in place, it could break the satellite communication if the ground computer was upgraded. Also, when OCB is turned on, it stops all power saving features of the antenna. This could be an issue for the satellite.

Sections about OCB in 802.11 2012 spec:
4.3.11 STA transmission of data frames outside the context of a BSS

Interesting links:  
http://riya80211.blogspot.com/2013/07/p2p-configuration-of-wpasupplicant-in.html  
http://events.linuxfoundation.org/sites/events/files/slides/How_to_Begin_V2X_Development_on_Linux_ZENOME_ALS_2015.pdf  
https://gist.github.com/yangmenghui/d01c12561aeb133adc35  

2. 3.65 / 3.6 / 3.7 Ghz band

The 3.7 Ghz band was designed to be used for long range wifi communication. Part of the use would be for Mesh networks, and WLAN set ups. The base distance for 3.7 is currently around 5 km.

The major issue with 3.7 Ghz band is that it was just recently announced, so there is not a lot of hardware specifically made for it yet. Meaning that the cost of hardware is currently much higher than what can be found in the 2.4 / 5 Ghz bands. Also, the 3.7 band will be licensed, and the PSAS project does not fall into different categories for licensing. Also, there would be additional fees for obtaining the licenses.

links:
https://apps.fcc.gov/edocs_public/attachmatch/FCC-13-144A1.pdf  
http://www.engadget.com/2012/05/07/ieee-802-11-2012-wifi-standard-published/  
http://www.acma.gov.au/webwr/_assets/main/lib310829/spp2009-02_release_of_3.6ghz_band_for_was-disc_paper.doc  
http://www.fiercewireless.com/tech/story/fcc-35-ghz-will-become-small-cell-band/2012-12-12  



##If you have budget...
This product was found and released during the time we were working on this project. 
Its a bit more expensive but if you are interested. [AirFiber](https://www.ubnt.com/products/)