# Snort Rules to detect PSEXEC traffic:

Ref. [https://github.com/John-Lin/docker-snort/blob/master/snortrules-snapshot2972/rules/policy-other.rules](https://github.com/John-Lin/docker-snort/blob/master/snortrules-snapshot2972/rules/policy-other.rules)

```text
alert tcp $HOME_NET any -> $HOME_NET [139,445]
(msg:"POLICY-OTHER use of psexec remote
administration tool"; flow:to_server,established;
content:"|FF|SMB|A2|"; depth:5; offset:4;
content:"|5C
00|p|00|s|00|e|00|x|00|e|00|c|00|s|00|v|00|c";
nocase; metadata:service netbios-ssn;
reference:url,technet.microsoft.com/en-
us/sysinternals/bb897553.aspx; classtype:policy-
violation; sid:24008; rev:1;)
alert tcp $HOME_NET any -> $HOME_NET [139,445]
(msg:"POLICY-OTHER use of psexec remote
administration tool SMBv2";
flow:to_server,established; content:"IFEISMB";
depth:8; nocase; content:"|05 00|"; within:2;
distance:8;
content:"P|00|S|00|E|00|X|00|E|00|S|00|V|00|C|00|";
fast_pattern:only; metadata:service netbios-ssn;
reference:url,technet.microsoft,com/en-
us/sysinternals/bb897553.aspx[1]; classtype:policy-
violation; sid:30281; rev:1;)
```
