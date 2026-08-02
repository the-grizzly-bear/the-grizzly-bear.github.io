# DHCP

View DHCP lease logs:<br>Red Hat 3:

```bash
cat /var/lib/dhcpd/dhcpd.leases
```

Ubuntu:

```bash
grep -Ei 'dhcp' /var/log/syslog.1
```

Ubuntu DHCP logs:

```bash
tail -f dhcpd.log
```
