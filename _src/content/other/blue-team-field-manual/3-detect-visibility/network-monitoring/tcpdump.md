# TCPDUMP

View ASCII (-A) or HEX (-X) traffic:

```bash
tcpdump -A
tcpdump -X
```

View traffic with timestamps and don't convert<br>addresses and be verbose:

```bash
tcpdump -tttt -n -vv
```

Find top talkers after 1000 packets (Potential<br>DDoS):

```bash
tcpdump -nn -c 1000 |awk '{print $3}' | cut -d. -f1-4 | sort -n | uniq -c | sort -nr
```

Capture traffic on any interface from a target host<br>and specific port and output to a file:

```bash
tcpdump -w <FILENAME>,pcap -i any dst <TARGET IP
ADDRESS> and port 80
```

View traffic only between two hosts:

```bash
tcpdump host 10.0.0.1 && host 10.0.0.2
```

View all traffic except from a net or a host:

```bash
tcpdump not net 10.10 && not host 192.168.1,2
```

View host and either of two other hosts:

```bash
tcpdump host 10,10,10.10 && \(10,10.10.20 or 10,10,10,30\)
```

Save pcap file on rotating size:

```bash
tcpdump -n -s65535 -C 1000 -w '%host_%Y-%m­%d_%H:%M:%S.pcap'
```

Save pcap file to a remote host:

```bash
tcpdump -w - | ssh <REMOTE HOST ADDRESS> -p 50005
"cat - > /tmp/remotecapture.pcap"
```

Grab traffic that contains the word pass:

```bash
tcpdump -n -A -s0 | grep pass
```

Grab many clear text protocol passwords:

```bash
tcpdump -n -A -s0 port http or port ftp or port
smtp or port imap or port pop3 | egrep -i
'pass=|pwd=|log=|login=|user=|username=|pw=|passw=|P
asswd=|password=|pass:|user:|username:| password:| log
in:| pass |user ' --color=auto --line-buffered -B20
```

Get throughput:

```bash
tcpdump -w - |pv -bert >/dev/null
```

Filter out ipv6 traffic:

```bash
tcpdump not ip6
```

Filer out ipv4 traffic:

```bash
tcpdump ip6
```

Script to capture multiple interface tcpdumps to files rotating every hour:

```bash
#!/bin/bash
tcpdump -pni any -s65535 -G 3600 -w any%Y-%m­
%d_%H:%M:%S.pcap
Script to move multiple tcpdump files to alternate
location:
#!/bin/bash
while true; do
sleep 1;
rsync -azvr -progress <USER NAME>@<IP
ADDRESS>:<TRAFFIC DIRECTORY>/, <DESTINATION DIRECTORY/.
done
```

Look for suspicious and self-signed SSL certificates:

```bash
tcpdump -s 1500 -A '(tcp[((tcp[12:1] & 0xf0) >>
2)+5:1] = 0x01) and (tcp[((tcp[12:1] & 0xf0) >>
2) :1] : 0x16)
```

Get SSL Certificate:

```bash
openssl s_client -connect <URL>:443
openssl s_client -connect <SITE>:443 </dev/null
2>/dev/null | sed -ne '/-BEGIN CERTIFICATE-/,/-END
CERTIFICATE-Ip' > <CERT>.pem
```

Examine and verify the certificate and check for Self-Signed:

```bash
openssl x509 -text -in <CERT>.pem
openssl x509 -in <CERT>,pem -noout -issuer -subject -startdate -enddate -fingerprint
openssl verify <CERT>.pem
```

Extract Certificate Server Name:

```bash
tshark -nr <PCAP FILE NAME> -Y
"ssl. handshake. ciphersuites" -Vx | grep "Server
Name:" | sort | uniq -c | sort -r
```

Extract Certificate info for analysis:

```bash
ssldump -Nr <FILE NAME>.pcap | awk 'BEGIN {c=0;}
{ if ($0 ~/^[ ]+Certificate$/) {c=l; print
"========================================";} if
($0 !~ /^ +/) {c=0;} if (c==l) print $0; }'
```
