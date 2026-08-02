# DISABLE/STOP SERVICES

Services information:

```bash
service --status-all
ps -ef
ps -aux
```

Get a list of upstart jobs:

```bash
initctl list
```

Example of start, stop, restarting a service in<br>Ubuntu:

```bash
/etc/init,d/apache2 start
/etc/init.d/apache2 restart
/etc/init.d/apache2 stop (stops only until reboot)
service mysql start
service mysql restart
service mysql stop (stops only until reboot)
```

List all Upstart services:

```bash
ls /etc/init/*,conf
```

Show if a program is managed by upstart and the<br>process ID:

```bash
status ssh
```

If not managed by upstart:

```bash
update-rc.d apache2 disable
service apache2 stop
```
