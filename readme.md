#Overview
The goal of this project is to attempt to push the bounds of current WiFi 
technolgies with the goal that we can send 
WiFi to space. PSAS [(Portland State Aerospace Society)](http://psas.pdx.edu/) 
has asked us [(PSU CS Capstone Team)]() to find the limitaitons of 
the current WiFi specifications and attempt to remove those limitations 
if they are software related. 

##Wrapper
The simple python wrapper [(wifi_wrap.py)](wifi_wrap.py) will get you started quickly. It has most of the 
commands from the other scripts built into it, but you might still 
need to use some the python scripts on its own once you are connected. 

###Usage
```bash
sudo python3 wifi_wrap.py -i 10.0.0.9 -d phy0 -c wlan0

```
> Command Line Options:
>   -h : help
>   -i : desired ip address
>   -d : physical device / wifi driver (e.g. phy0)
>   -c : wifi card name (e.g. wlan0)
>   -pwr : set txpower in dBm (e.g. 30)
>
>       e.g. sudo python3 wifi_wrap.py -i 10.0.0.9 -d phy0 -c wlan0
>
>   -restart : reset machine to original settings
>
>       e.g. sudo python3 -restart wlan1
>

##Script
The [dual.sh](dual.sh) script will set up an Ad-Hoc between two computers and change the
WiFi settings to what
we think will make the best possible connection between two computers.

###Using the scripts
More extensive options can be found [here](documents/scriptingdocs.md). 

On both computers, run the following script with the following parameters. 
The [extensive readme](documents/scriptingdocs.md) can explain how to get each individual parameter. 

```bash
sudo ./dual.sh $devicename $physicalname $ipaddress
```

Once connected, you can test your connection by pinging the computers ip address. 
```bash
ping $ipaddress
```

The [wifi_back_on.sh](wifi_back_on.sh) script is used to reset the computer's WiFi settings back 
to the original state before the dual.sh script was run. To use this, simply type
```bash
./wifi_back_on.sh $devicename
```

##Testing
The testing module includes two python scripts which use a UDP connection to have one device
ping the other device by sending integer variables. The other device then writes
them to a csv file for later analysis. 

Another attempt we found much more valuable was to use the multicasting technique
to remove the need for ACKS which took up much of the bandwith on some of our testing. 
This phase was begun but only experimental. Please read [research](documents/research.md)
for more information. 

###Usage
See the [testing script's readme](testing/README.md) for more information and usage. 

##Research
###TLDR;
When the team began researching this project, we investigated many avenues. You can 
read more details of the reserach investigated [here](documents/research.md). 
In the end, we went with the following technologies. 
* UDP Communication Protcol
* UNIX (Tested on Ubuntu)
* Python (Packet send testing)
* Ad-Hoc network


##Hardware
While the hardware can vary (we have not extensivly tested various devices), we tested it 
primarily on the Atheros Wireless card and TP link cards. Please see 
[Long Range Test Documents](documents/tests.md) for more extensive details. 
