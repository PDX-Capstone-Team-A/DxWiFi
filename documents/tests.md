#Different Tests
We did many tests at different distances to fine-tune our 
scripts and see if there were any unexpected outcomes during these
tests.

The final test was a planned 12 mile stretch from Little Beacon Rock, located on the Washington side of the Columbia Gorge,
to Vista House, located on the Oregon side.

##Goals
The goal of the tests was to see if there were any unusual happenings
that we would need to address. Specifically we wanted to avoid any unnecessary data exchanges, such as the sending of acknowledgment packets, etc. While we did extensive research into the WiFi 802.11 specification requirements, the specs 
were comprehensive to the point that a complete analysis would be impractical.


##1 & ~2 mile tests
The first distance test we attempted was a 1 mile test, then a 1.7 
mile test.  

###Hardware
* 2 Laptops
* 2 Wireless Cards
* 1 Sieve
* 1 & ~2 mile Clear Line of Sight (LOS)

###Test goals
To see if there were any unusual timeouts in wireless going this 
short distance. We expected there shouldn't be, but we also used
out-of-the-box USB WiFI cards at their default power settings. 

###Results
Both tests were successful. The sieve wrapped around one of the wireless
cards was extremely useful as we were unsuccessful in making a 
connection without it. We did notice some unusual packet loss
which was rectified by adding a short delay before sending each packet. 
After this adjustment, we saw considerably lower packet loss. 
We assume this was to do with sending too many packets too quickly overflowing a buffer somewhere along the way.

###Gallery


##Radio room test
###Hardware
* 2 Laptops
* 2 Wireless Cards

###Test goals
In this test, we wanted to see if there was any unusual packet loss
using some packet resistors along the connection to incur "man in 
the middle" timeouts. We also wanted to get cleaner packet sniffing 
using Wireshark without the need for extensive filters. 

###Results
We found that there was some kidn of a wireless handshake occurring
because as soon as we unplugged the wireless card, the other computer
would disconnect immediately even though there were still packets in 
the air. We suspected either a handshake or some buffer. There are
further suspicions, however. Take a look at the 12 mile test results
to understand what our suspicion was. 

###Gallery

##12 mile test 
###Hardware

###Test goals
While we had done some testing at 1 & 2 miles, we had found 
some documentation that suggested timeouts might occur using 802.11b
after 9 miles. Even though we had done timeout tests in the radio 
room, it was a nice Saturday and we wanted to see if there was 
other interference in the real world. We beamed wireless data from
Little Beacon Rock to Vista House.

###Results
The tests were successful. We were pleased that there were no big 
issues and we were up and sending data in short order. We ran 
multiple tests using our Python UDP scripts, standard pings, and fountain codes.
We used fountain codes to send an image (see 
research), which was a success and a pleasant surprise. 
We also noted a large amount of unwanted ACK's or acknowledgment packets being sent. 
We believe this was why the tests in the radio room had some
interesting results. The solution to this was to use multicasting. 
This doesn't require an acknowledgment and it simply sends data without a required connection.

###Gallery


TL-WN722N
