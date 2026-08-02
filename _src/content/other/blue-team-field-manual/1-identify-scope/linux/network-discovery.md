# NETWORK DISCOVERY

Net view scan:

```bash
smbtree -b
```

```bash
smbtree -D
```

```bash
smbtree -5
```

View open 5MB shares:

```bash
smbclient -L <HOST NAME>
```

```bash
smbstatus
```

Basic ping scan:

```bash
for ip in $(seq 1 254); do ping -c 1 192.168.1.$ip>/dev/null; [ $? -eq 0 ] && echo "192.168.1.$ip UP" || : ; done
```
