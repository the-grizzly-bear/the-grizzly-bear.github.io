# SNORT

Run test on snort config file:

```bash
snort -T -c /<PATH TO SNORT>/snort/snort.conf
```

Use snort(v=verbose,d=dump packet payload):

```bash
snort -dv -r <LOG FILE NAME>, log
```

Replay a log file and match icmp traffic:

```bash
snort -dvr packet.log icmp
```

Logs in ASCII:

```bash
snort -K ascii -l <LOG DIRECTORY>
```

Logs in binary:

```bash
snort -l <LOG DIRECTORY>
```

Sent events to console:

```bash
snort -q -A console -i eth0 -c
/etc/snort/snort.conf
snort -c snort.conf -l /tmp/so/console -A console
```

Create a single snort rule and save:

```bash
echo alert any any <SNORT RULE> > one.rule
```

Test single rule:

```bash
snort -T -c one.rule
```

Run single rule and output to console and logs dir:

```bash
mkdir ,/logs
snort -vd -c one.rule -r <PCAP FILE NAME>,pcap -A
console -l logs
```
