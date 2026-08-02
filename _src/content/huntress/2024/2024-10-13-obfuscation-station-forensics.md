# 2024-10-13 Obfuscation Station (Forensics)

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

```python
(nEW-objECt  SYstem.iO.COMPreSsIon.deFlaTEStREAm( [IO.mEmORYstreAM][coNVERt]::FROMBAse64sTRING( 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA') ,[io.COmPREssioN.coMpreSSioNmODE]::DeCoMpReSS)| %{ nEW-objECt  sYStEm.Io.StREAMrEADeR($,[TeXT.encodiNG]::AsCii)} |%{ $.READTOENd()})| & ( $eNV:cOmSPEc[4,15,25]-JOin'')
```

```powershell
$base64String = 'UzF19/UJV7BVUErLSUyvNk5NMTM3TU0zMDYxNjSxNDcyNjexTDY2SUu0NDRITDWpVQIA'

$bytes = [System.Convert]::FromBase64String($base64String)

$memoryStream = New-Object System.IO.MemoryStream
$memoryStream.Write($bytes, 0, $bytes.Length)
$memoryStream.Seek(0, [System.IO.SeekOrigin]::Begin) | Out-Null

$deflateStream = New-Object System.IO.Compression.DeflateStream($memoryStream, [System.IO.Compression.CompressionMode]::Decompress)
$streamReader = New-Object System.IO.StreamReader($deflateStream, [System.Text.Encoding]::ASCII)
$decompressedString = $streamReader.ReadToEnd()

$decompressedString
```

*[image unavailable]*

```python
flag{3ed675ef0343149723749c34fa910ae4}
```
