# PASSIVE DNS MONITORING

Use dnstop to monitor DNS requests at any sniffer location:

```bash
apt-get update
apt-get install dnstop
dnstop -l 3 <INTERFACE NAME>
```

Step 1: Hit 2 key to show query names<br>Use dnstop to monitor DNS requests from a pcap file:

```bash
dnstop -l 3 <PCAP FILE NAME> | <OUTPUT FILENAME>,txt
```
