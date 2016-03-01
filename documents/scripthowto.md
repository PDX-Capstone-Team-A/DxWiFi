##dual.sh
Plug in the wireless device and type 

```bash
dmesg | tail
```
which will return the kernel logs and note the new device that was
plugged in. You will be looking for something like phy# and wlan#. 

Take note of these as they will be necessary for the dual.sh 
