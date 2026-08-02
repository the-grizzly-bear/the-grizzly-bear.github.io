# WHITELIST

Use a Proxy Auto Config(PAC) file to create Bad URL<br>or IP List (IE, Firefox, Chrome):

```bash
function FindProxyForURL(url, host) {
II Send bad DNS name to the proxy
if (dnsDomainis(host, ".badsite.com"))
return "PROXY http:11127.0.0.1:8080";
II Send bad IPs to the proxy
if (isinNet(myipAddress(), "222.222.222.222",
"255.255.255.0"))
return "PROXY http:11127.0.0.1:8080";
II All other traffic bypass proxy
return "DIRECT";
}
```
