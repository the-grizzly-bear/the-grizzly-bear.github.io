# OPENVAS

Step 1: Install the server, client and plugin<br>packages:

```bash
apt-get install openvas-server openvas-client openvas-plugins-base openvas-plugins-dfsg
```

Step 2: Update the vulnerability database

```bash
openvas-nvt-sync
```

Step 3: Add a user to run the client:

```bash
openvas-adduser
```

Step 4: Login: sysadm<br>Step 5: Authentication (pass/cert) \[pass\]: \[HIT ENTER\]<br>Step 6: Login password: \<PASSWORD\><br>You will then be asked to add "User rules".<br>Step 7: Allow this user to scan authorized network by typing:

```bash
accept <YOUR IP ADDRESS OR RANGE>
default deny
```

Step 8: type ctrl-D to exit, and then accept.<br>Step 9: Start the server:

```bash
service openvas-server start
```

Step 10: Set targets to scan:<br>Create a text file with a list of hosts/networks to scan.

```bash
vi scanme.txt
```

Step 11: Add one host, network per line:

```bash
<IP ADDRESS OR RANGE>
```

Step 12: Run scan:

```bash
openvas-client -q 127.0.0.1 9390 sysadm nsrc+ws
scanme.txt openvas-output-.html -T txt -V -x
```

Step 13: (Optional)run scan with HTML format:

```bash
openvas-client -q 127.0.0.1 9390 sysadm nsrc+ws scanme.txt openvas-output.txt -T html -V -x
```
