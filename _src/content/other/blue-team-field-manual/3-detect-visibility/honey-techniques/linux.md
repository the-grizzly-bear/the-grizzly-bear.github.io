# LINUX

Honey Ports Linux:
Ref. [http://securityweekly.com/wp­content/uploads/2013/06/howtogetabetterpentest.pdf](http://securityweekly.com/wp%C2%ADcontent/uploads/2013/06/howtogetabetterpentest.pdf)
Step 1: Run a while loop to create TCP Firewall<br>rules to block any hosts connecting on port 2222

```bash
while [ 1 ] ; echo "started" ; do IP='nc -v -l -p
2222 2>&1 l> /dev/null I grep from I cut -d[ -f 3 I
cut -d] -f 1'; iptables -A INPUT -p tcp -s ${IP} -j
DROP ; done
```

Linux Honey Ports Python Script:
Ref.[https://github.com/gchetrick/honeyports/blob/master/honeyports-0.5.py](https://github.com/gchetrick/honeyports/blob/master/honeyports-0.5.py)
Step 1: Download Python Script

```bash
wget https://github.com/gchetrick/honeyports/blob/master/honeyports-0.5.py
```

Step 2: Run Python Script

```bash
python honeyports-0.5.py -p <CHOOSE AN OPEN PORT>
-h <HOST IP ADDRESS>
```

Detect rogue scanning with Labrea Tarpit:

```bash
apt-get install labrea
labrea -z -s -o -b -v -i eth0 2>&11 tee -a log.txt
```
