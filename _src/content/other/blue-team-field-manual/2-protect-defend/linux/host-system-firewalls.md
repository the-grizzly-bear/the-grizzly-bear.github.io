# HOST SYSTEM FIREWALLS

Export existing iptables firewall rules:

```bash
iptables-save > firewall.out
```

Edit firewall rules and chains in firewall.out and<br>save the file:

```bash
vi firewall.out
```

Apply iptables:

```bash
iptables-restore < firewall.out
```

Example iptables commands (IP, IP Range, Port Blocks):

```bash
iptables -A INPUT -s 10.10.10.10 -j DROP
iptables -A INPUT -s 10,10.10.0/24 -j DROP
iptables -A INPUT -p tcp --dport ssh -s
10.10.10.10 -j DROP
iptables -A INPUT -p tcp --dport ssh -j DROP
```

Block all connections:

```bash
iptables-policy INPUT DROP
iptables-policy OUTPUT DROP
iptables-policy FORWARD DROP
```

Log all denied iptables rules:

```bash
iptables -I INPUT 5 -m limit --limit 5/min -j LOG
--log-prefix "iptables denied: " --log-level 7
```

Save all current iptables rules:<br>Ubuntu:

```bash
/etc/init.d/iptables save
/sbin/service iptables save
```

RedHat / CentOS:

```bash
/etc/init.d/iptables save
/sbin/iptables-save
```

List all current iptables rules:

```bash
iptables -L
```

Flush all current iptables rules:

```bash
iptables -F
```

Start/Stop iptables service:

```bash
service iptables start
service iptables stop
```

Start/Stop ufw service:

```bash
ufw enable
ufw disable
```

Start/Stop ufw logging:

```bash
ufw logging on
ufw logging off
```

Backup all current ufw rules:

```bash
cp /lib/ufw/{user.rules,user6.rules} /<BACKUP
LOCATION>
cp /lib/ufw/{user.rules,user6.rules} ./
```

Example uncomplicated firewall (ufw) Commands (IP, IP range, Port blocks):

```bash
ufw status verbose
ufw delete <RULE#>
ufw allow for <IP ADDRESS>
ufw allow all 80/tcp
ufw allow all ssh
ufw deny from <BAD IP ADDRESS> proto udp to any
port 443
```
