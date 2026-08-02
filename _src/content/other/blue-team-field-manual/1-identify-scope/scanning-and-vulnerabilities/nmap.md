# NMAP

Ping sweep for network:

```bash
nmap -sn -PE <IP ADDRESS OR RANGE>
```

Scan and show open ports:

```bash
nmap --open <IP ADDRESS OR RANGE>
```

Determine open services:

```bash
nmap -sV <IP ADDRESS>
```

Scan two common TCP ports, HTTP and HTTPS:

```bash
nmap -p 80,443 <IP ADDRESS OR RANGE>
```

Scan common UDP port, DNS:

```bash
nmap -sU -p 53 <IP ADDRESS OR RANGE>
```

Scan UDP and TCP together, be verbose on a single<br>host and include optional skip ping:

```bash
nmap -v -Pn -SU -ST -p U:53,111,137,T:2125,80,139,8080 <IP ADDRESS>
```
