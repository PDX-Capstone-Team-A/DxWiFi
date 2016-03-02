#Different Tests
We did many tests using different distances to fine tune the 
scripts and see if there was any unexpected outcomes during these
tests.

The final test was a planned 12 mile stretch from Little Beacon Rock
to Vista House.

##Goals
The goal of the tests were to see if there were any unusual happenings
that we would need to change, such as acknowledgments, etc. While we did extensive research into the 802.11 specs requirement, the specs 
were comprehensive to the point that a complete research would be impractical.


##1 & ~2 mile tests
The first distance test we attempted was a 1 mile test, then a 1.7 
mile test.  

###Hardware
* 2 Laptops
* 2 Wireless Cards
* 1 Sieve
* 1 & ~2 mile Clear Line of Sight (LOS)

###Test goals
To see if there was any unusual timeouts in wireless going this 
short distance. We expected there shouldn't be but we also used
out of the box USB WiFI cards at their original power settings. 

###Results
Both successful, the sieve wrapped around one of the wireless
cards was extremely useful as we were unsuccessful in making a 
connection without it. We did notice some unusual packet loss
which resulted in needing a sleep before sending out more packets. 
After this adjustment of adding a minor sleep on the thread before
sending out more packets, we found a considerable packet increase. 
We assume this was to do with the buffer of the wireless cards used.

###Gallery


##Radio room test
###Hardware
* 2 Laptops
* 2 Wireless Cards

###Test goals
In this test, we wanted to see if there was any unusual packet loss
using some packet resistors in the intermediary to incur man in 
the middle timeouts. We could also get a cleaner packet sniffing 
using wireshark without extensive filters. 

###Results
We did find that there was a handshake occurring
because as soon as we unplugged the wireless card, the other computer
would disconnect immediately even though there were still packets in 
the air. We suspected either a handshake or some buffer. There are
further suspicions, however, take a look at the 12 mile test results
to understand what our suspicion was. 

###Gallery

##12 mile test 
###Hardware

###Test goals
While we had done some testing of 1 & 2 mile tests, we had found 
some documentation that suggested timeouts might occur using 102.11b
after 9 miles. Even though we had done timeout tests in the radio 
room, it was a nice Saturday and we wanted to see if there was 
other interference in the real world. We beamed wireless data from
Little Beacon Rock to Vista House.

###Results
The tests were successful. We were pleased that there were no big 
issues and we were up and sending data in short order. We ran 
multiple tests using python UDP scripts, ping tests and also
sent an image. The image we sent we used fountain codes (see 
research) to send it which was a success and a pleasant surprise. 
Finally we also noted a large amount of ACK's or Acknowledgments. 
We believe this was why the tests in the radio room had some
interesting results. The solution to this was to use multicasting. 
This doesn't require an acknowledgment and it just beams the data
out there without a required connection.

###Gallery


TL-WN722N
