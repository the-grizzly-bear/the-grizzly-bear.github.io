# IPSEC

Allow firewall to pass IPSEC traffic:

```bash
iptables -A INPUT -p esp -j ACCEPT
iptables -A INPUT -p ah -j ACCEPT
iptables -A INPUT -p udp --dport 500 -j ACCEPT
iptables -A INPUT -p udp --dport 4500 -j ACCEPT
```

Pass IPSEC traffic:<br>Step 1: Install Racoon utility on \<HOSTl IP ADDRESS\><br>and \<HOST2 IP ADDRESS\> to enable IPSEC tunnel in<br>Ubuntu.

```bash
apt-get install racoon
```

Step 2: Choose direct then edit letclipsec­tools.conf on \<HOSTl IP ADDRESS\> and \<HOST2 IPADDRESS\>.

```bash
flush;
spdflush;
spdadd <HOSTl IP ADDRESS> <HOST2 IP ADDRESS> any -P
out ipsec
esp/transport//require;
spdadd <HOST2 IP ADDRESS> <HOSTl IP ADDRESS> any -P 
in ipsec
esp/transport//require;
```

Step 3: Edit /etc/racoon/racoon.conf on \<HOSTl IPADDRESS\> and \<HOST2 IP ADDRESS\>,

```bash
log notify;
path pre_shared_key "/etc/racoon/psk.txt";
path certificate "/etc/racoon/certs";
remote anonymous {
exchange_mode main,aggressive;
proposal {
encryption_algorithm aes_256;
hash_algorithm sha256;
authentication_method
pre_shared_key;
dh_group modp1024;
}
generate_policy off;
}
sainfo anonymous{
pfs_group 2;
encryption_algorithm aes_256;
authentication_algorithm hmac_sha256;
compression_algorithm deflate;
}
```

Step 4: Add preshared key to both hosts.
On HOST l:
echo \<HOST2 IP ADDRESS\> \<PRESHARED PASSWORD\>

```bash
/etc/racoon/psk.txt
```

On HOST2:
echo \<HOSTl IP ADDRESS\> \<PRESHARED PASSWORD\>

```bash
/etc/racoon/psk.txt
```

Step 5: Restart service on both systems.

```bash
service setkey restart
```

Check security associations, configuration and<br>polices:

```bash
setkey -D
setkey -DP
```
