# Intergalactic Recovery (Forensic Challenge)

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

```bash
python2 vol.py -f ../../../Downloads/inter/forensics_intergalactic_recovery/0c584923.img imageinfo

┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/hack/tools/volatility]
└──╼ [★]$ python2 vol.py -f ../../../Downloads/inter/forensics_intergalactic_recovery/0c584923.img imageinfo
```

*[image unavailable]*

raid 5 1 drive failure

xor recovery

*[image unavailable]*

```bash
from pwn import *
disk1 = read('disk1.img')
disk2 = read('disk2.img')
disk3 = xor(disk1, disk2)
write('disk3.img', disk3)

pip install pwntools
pip install -U simplejson
```

strings on disk3

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

```bash
No tldr entry for mdadm
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ mdadm --create --level=5 --raid-devices=3 /dev/md0 dev/loop1 dev/loop2 dev/loop3
mdadm: must be super-user to perform this action
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ sudo mdadm --create --level=5 --raid-devices=3 /dev/md0 dev/loop1 dev/loop2 dev/loop3
mdadm: cannot open dev/loop1: No such file or directory
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ sudo mdadm --create --level=5 --raid-devices=3 /dev/md0 /dev/loop1 /dev/loop2 /dev/loop3
mdadm: Defaulting to version 1.2 metadata
mdadm: array /dev/md0 started.
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ sudo mount /dev/md0 /mnt/raid
mount: /mnt/raid: mount point does not exist.
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ sudo mkdir /mnt/raid
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ sudo mount /dev/md0 /mnt/raid
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ ls /mnt/
raid  shared
┌─[us-dedicated-100-dhcp]─[10.10.14.3]─[user@parrot]─[~/Downloads/inter/forensics_intergalactic_recovery]
└──╼ [★]$ ls /mnt/raid/
imw_1337.pdf
```

*[image unavailable]*

```bash
sudo losetup /dev/loop1 disk1.img
sudo losetup /dev/loop2 disk2.img
sudo losetup /dev/loop3 disk3.img

sudo mdadm --create --level=5 --raid-devices=3 /dev/md0 /dev/loop1 /dev/loop2 /dev/loop3
```

*[image unavailable]*

```bash
HTB{f33ls_g00d_t0_b3_1nterg4l4ct1c_m0st_w4nt3d}
```
