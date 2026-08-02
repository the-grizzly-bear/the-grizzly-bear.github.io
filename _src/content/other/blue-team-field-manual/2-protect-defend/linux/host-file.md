# HOST FILE

Add new malicious domain to hosts file, and route to localhost:

```bash
echo 127.0.0.1 <MALICIOUS DOMAIN> >> /etc/hosts
```

Check if hosts file is working, by sending ping to 127.0.0.1:

```bash
ping -c 1 <MALICIOUS DOMAIN>
```

Ubuntu/Debian DNS cache flush:

```bash
/etc/init.d/dns-clean start
```

Flush nscd DNS cache four ways:

```bash
/etc/init.d/nscd restart
service nscd restart
service nscd reload
nscd -i hosts
```

Flush dnsmasq DNS cache:

```bash
/etc/init.d/dnsmasq restart
```
