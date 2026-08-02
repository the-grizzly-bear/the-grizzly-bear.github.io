# NETWORK CAPTURE (PCAP) TOOLS

**EDITCAP**

Use to edit a pcap file (split into 1000 packets):

```bash
> editcap -F pcap -c 1000 orignal.pcap
out_split,pcap
```

Use to edit a pcap file (split into 1 hour each packets):

```bash
> editcap -F pcap -t+3600 orignal.pcap
out_split.pcap
```

**MERGECAP**

Use to merge multiple pcap files:

```bash
> mergecap -w merged_cap.pcap capl.pcap cap2.pcap cap3.pcap
```
