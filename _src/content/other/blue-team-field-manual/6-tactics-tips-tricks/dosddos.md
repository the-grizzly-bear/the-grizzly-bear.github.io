# DOS/DDOS

### FINGERPRINT DOS/DDOS

Fingerprinting the type of DoS/DDoS:
Ref. [https://www.trustwave.com/Resources/SpiderLabs-Blog/PCAP-Files-Are-Great-Arn-t-They--/](https://www.trustwave.com/Resources/SpiderLabs-Blog/PCAP-Files-Are-Great-Arn-t-They--/)

Volumetric: Bandwidth consumption
Example, sustaining sending 1Gb of traffic to 10Mb connection
Ref. [http://freecode.com/projects/iftop](http://freecode.com/projects/iftop)

```bash
iftop -n
```

and Protocol: Use of specific protocol
Example, SYN Flood, ICMP Flood, UDP flood

```bash
tshark -r <FILE NAME>,pcap -q -z io,phs
tshark -c 1000 -q -z io,phs
tcpdump -tnr $FILE |awk -F '. ' '{print
$1","$2"."$3"."$4}' | sort | uniq -c | sort -n |tail
tcpdump -qnn "tcp[tcpflags] & (tcp-syn) != 0"
netstat -s
```

Example, isolate one protocol and or remove other protocols

```bash
tcpdump -nn not arp and not icmp and not udp
tcpdump -nn tcp
```

Resource: State and connection exhaustion
Example, Firewall can handle 10,000 simultaneous connections, and attacker sends 20,000

```bash
netstat -n | awk '{print $6}' | sort | uniq -c
sort -nr | head
```

Application: Layer 7 attacks
Example, HTTP GET flood, for a large image file.

```bash
tshark -c 10000 -T fields -e http.host |sort | uniq -c | sort -r | head -n 10

tshark -r capture6 -T fields -e
http.request.full_uri | sort | uniq -c | sort -r | head -n 10c

tcpdump -n 'tcp[32:4] = 0x47455420'| cut -f 7- -d ":"
```

Example, look for excessive file requests, GIF, ZIP, JPEG, PDF, PNG.

```bash
tshark -Y "http contains "ff:d8"" || "http
contains "GIF89a"" || "http contains
"\x50\x4B\x03\x04"" || "http contains\xff\xd8" " ||
"http contains "%PDF1"" || "http contains
"\x89\x50\x4E\x47""
```

Example, Look for web application 'user-agent' pattern of abuse.

```bash
tcpdump -c 1000 -Ann I grep -Ei 'user-agent' | sort | uniq -c | sort -nr | head -10
```

Example, show HTTP Header of requested resources.

```bash
tcpdump -i en0 -A -s 500 | grep -i refer
```

Sniff HTTP Headers for signs of repeat abuse:

```bash
tcpdump -s 1024 -l -A dst <EXAMPLE.COM>
```

Poison: Layer 2 attacks
Example, ARP poison, race condition DNS, DHCP

```bash
tcpdump 'arp or icmp'
tcpdump -tnr <SAMPLE TRAFFIC FILE>.pcap ARP |awk F ',' '{print $1"."$2"."$3"."$4}' | sort | uniq -c | sort -n | tail
tshark -r <SAMPLE TRAFFIC FILE>.pcap -q -z io,phs| grep arp.duplicate-address-detected
```
