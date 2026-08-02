# IPSEC

Create a IPSEC Local Security Policy, applied to any connection, any protocol, and using a preshared key:

```bash
C:\> netsh ipsec static add filter
filterlist=MyIPsecFilter srcaddr=Any dstaddr=Any
protocol=ANY
C:\> netsh ipsec static add filteraction
name=MyIPsecAction action=negotiate
C:\> netsh ipsec static add policy
name=MyIPsecPolicy assign=yes
C:\> netsh ipsec static add rule name=MyIPsecRule
policy=MyIPsecPolicy filterlist=MyIPsecFilter
filteraction=MyIPsecAction conntype=all activate=yes
psk=<PASSWORD>
```

Add rule to allow web browsing port 80(HTTP) and<br>443(HTTPS) over IPSEC:

```bash
C:\> netsh ipsec static add filteraction name=Allow action=permit
C:\> netsh ipsec static add filter
filterlist=WebFilter srcaddr=Any dstaddr=Any protocol=TCP dstport=80
C:\> netsh ipsec static add filter
filterlist=WebFilter srcaddr=Any dstaddr=Any protocol=TCP dstport=443
C:\> netsh ipsec static add rule name=WebAllow policy=MyIPsecPolicy filterlist=WebFilter filteraction=Allow conntype=all activate=yes psk=<PASSWORD>
```

Shows the IPSEC Local Security Policy with name "MyIPsecPolicy":

```bash
C:\> netsh ipsec static show policy
name=MyIPsecPolicy
```

Stop or Unassign a IPSEC Policy:

```bash
C:\> netsh ipsec static set policy
name=MyIPsecPolicy
```

Create a IPSEC Advance Firewall Rule and Policy and preshared key from and to any connections:

```bash
C:\> netsh advfirewall consec add rule name= u IPSEC" endpointl=any endpoint2=any action=requireinrequireout qmsecmethods=default
```

Require IPSEC preshared key on all outgoing requests:

```bash
C:\> netsh advfirewall firewall add rule
name= u IPSEC_Out" dir=out action=allow enable=yes profile=any localip=any remoteip=any protocol=any interfacetype=any security=authenticate
```

Create a rule for web browsing:

```bash
C:\> netsh advfirewall firewall add rule name="Allow Outbound Port 80 11 dir=out localport=80 protocol=TCP action=allow
```

Create a rule for DNS:

```bash
C:\> netsh advfirewall firewall add rule name="Allow Outbound Port 53 11 dir=out localport=53 protocol=UDP action=allow
```

Delete ISPEC Rule:

```bash
C:\> netsh advfirewall firewall delete rule name="IPSEC_RULE"
```
