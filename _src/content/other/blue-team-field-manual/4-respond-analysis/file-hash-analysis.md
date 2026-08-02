# FILE HASH ANALYSIS

## HASH QUERY

VirusTotal online API query:
Ref. [https://www.virustotal.com/en/documentation/public-api/](https://www.virustotal.com/en/documentation/public-api/) (Prerequisite: Need a VT API Key)
Send a suspicious hash to VirtusTotal using cURL:

```shell
curl -v --request POST --url
'https://www.virustotal.com/vtapi/v2/file/report' -d
apikey=<VT API KEY> -d 'resource=<SUSPICIOUS FILE
HASH>'
```

Send a suspicious file to VirusTotal using cURL:

```shell
curl -v -F 'file=/<PATH TO FILE>/<SUSPICIOUS FILE
NAME>' -F apikey=<VT API KEY>
https://www.virustotal.com/vtapi/v2/file/scan
```

Team Cymru API:
Ref. [https://hash.cymru.com](https://hash.cymru.com/), [http://totalhash.com](http://totalhash.com/)
Team Cymru malware hash lookup using whois: (Note: Output is timestamp of last seen and detection rate)

```shell
whois -h hash,cymru.com <SUSPICIOUS FILE HASH>
```
