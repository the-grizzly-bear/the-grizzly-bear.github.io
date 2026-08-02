# DNS

Start DNS logging:

```bash
rndc querylog
```

View DNS logs:

```bash
tail -f /var/log/messages | grep named
```
