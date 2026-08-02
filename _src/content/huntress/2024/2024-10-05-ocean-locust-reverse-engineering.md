# 2024-10-05 Ocean-Locust (Reverse Engineering)

*[image unavailable]*

```python
flag{fec87c690b8ec8d65b8b10ee7bb65d0}
```

Basically removing alot ofother testing, messed around with the png and saw the biTx values changed, and using the program, created a 1x1.png to see the changes, took the encoding program, ran through png-challenge.exe 1x1.png flag{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa} changing each value, when you had a match moved on to the next biT value pair.

*[image unavailable]*

Analyzing the file with 7 or 14 a's

*[image unavailable]*

My scripts were working, though poorly. I would get the values for A, B, etc and move to the next chunk

```shell
 flag{fec87c690b8ec8d65b8bb10eeaaaaaaa}

# Define the correct known biTx values as arrays of byte pairs (now all uppercase)
$knownValues = @{
    'bita' = @('04', '05', '35', '06', '19')
    'bitb' = @('04', '0C', '37', '5A', '55')
    'bitc' = @('01', '5F', '6D', '53', '00')
    'bitd' = @('5A', '0C', '37', '5C', '06')
    'bite' = @('54', '5C', '36', '5D', '00')
    'bitf' = @('00', '58', '64', '03', '07') 
    'bitg' = @('55', '0B', '36', '51', '57')
    'bith' = @('06', '59', '29', 'C2', 'C8')
}

# Define the initial flag starting from the matched part for bitc
$flag = "flag{fec87c690b8ec8d65b8baaaaaaaaaaaa}"

function Extract-PngChunks {
    param (
        [string]$filePath
    )
    
    $data = [System.IO.File]::ReadAllBytes($filePath)
    $pointer = 8  # Skip the PNG signature
    $chunks = @()

    while ($pointer -lt $data.Length) {
        $chunkLengthBytes = $data[$pointer..($pointer + 3)]
        [Array]::Reverse($chunkLengthBytes)
        $chunkLength = [BitConverter]::ToUInt32($chunkLengthBytes, 0)
        $chunkType = [System.Text.Encoding]::ASCII.GetString($data[($pointer + 4)..($pointer + 7)])
        $chunkData = $data[($pointer + 8)..($pointer + 7 + $chunkLength)]
        $chunkCRC = $data[($pointer + 8 + $chunkLength)..($pointer + 11 + $chunkLength)]
        $chunks += [PSCustomObject]@{
            Type = $chunkType
            Length = $chunkLength
            Data = $chunkData
            CRC = $chunkCRC
        }
        $pointer += $chunkLength + 12
    }

    return $chunks
}

function Check-BiTChunk {
    param (
        [array]$chunks,
        [string]$targetType,
        [array]$expectedPairs,  # Known values as an array of byte pairs
        [int]$charPosition  # Position to match in byte pair sequence
    )
    
    foreach ($chunk in $chunks) {
        if ($chunk.Type -eq $targetType) {
            # Extract bytes from the chunk data
            $extractedBytes = @()
            for ($i = 0; $i -lt $chunk.Data.Length; $i++) {
                $byte = "{0:X2}" -f $chunk.Data[$i]
                $extractedBytes += $byte
            }

            # Print extracted and expected values for debugging
            Write-Host "Chunk Type: $($chunk.Type)"
            Write-Host "Found $targetType values: $($extractedBytes -join ' ')"
            Write-Host "Expected $targetType values: $($expectedPairs -join ' ')" 

            # Calculate the correct index based on the current character's position in the flag
            $index = ($charPosition - 25)  # Adjust index for the bitf chunk starting position
            
            if ($index -ge 0 -and $index -lt $expectedPairs.Length) {
                $extractedByte = $extractedBytes[$index].ToLower()
                $expectedByte = $expectedPairs[$index].ToLower()

                # Print details of the current byte comparison
                Write-Host ("Comparing extracted byte '{0}' with expected byte '{1}' at position {2}" -f $extractedByte, $expectedByte, $charPosition)

                if ($extractedByte -eq $expectedByte) {
                    Write-Host "Match found for position $charPosition!"
                    return $true
                } else {
                    Write-Host "No match at position $charPosition."
                }
            } else {
                Write-Host "Position $charPosition is out of bounds for the extracted bytes or expected pairs."
                return $false
            }
        }
    }
    return $false
}

# Main loop to test flags by updating byte pairs
$characters = @('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')  # Possible characters for the flag

$position = 25  # Start at position 30 for the bitf chunk

while ($position -lt $flag.Length - 1) {
    $matchFound = $false
    foreach ($nextChar in $characters) {
        # Create the current flag by substituting the character at the current position
        $currentFlag = $flag.Substring(0, $position) + $nextChar + $flag.Substring($position + 1)

        Write-Host "`nTesting flag with $nextChar`: $currentFlag"
        & .\png-challenge.exe 1x1.png $currentFlag | Out-Null
        $chunks = Extract-PngChunks -filePath "encoded 1x1.png"

        # Check the current position for bitf
        $result = Check-BiTChunk -chunks $chunks -targetType "bitf" -expectedPairs $knownValues['bitf'] -charPosition $position

        if ($result) {
            Write-Host "Match found: $currentFlag"
            $flag = $currentFlag
            $matchFound = $true
            break
        }
    }

    if ($matchFound) {
        $position += 1  # Increment by 1 to move to the next character position in the flag
    } else {
        Write-Host "No match found for position $position in chunk type bitf."
        break
    }
}

Write-Host "`nFinal flag: $flag"
```

```shell
run to get flag{fec87c690baaaaagaaaaaaaaaaaaaaaa}

# (iteration focusing on biTc chunk — near-identical brute-force script,
#  $flag = "flag{fec87aaaaaaaaaaaaaaaaaaaaaaaaaaa}", $position = 10,
#  targetType "bitc", index = $charPosition - 10)
```

```shell
Final flag: flag{fec87c690b8ec8daaaaaaaaaaaaaaaaa}

# (iteration focusing on bitd chunk — near-identical brute-force script,
#  $flag = "flag{fec87c690baaaaaaaaaaaaaaaaaaaaaa}", $position = 15,
#  targetType "bitd", index = $charPosition - 15)
```

```shell
Final flag: flag{fec87c690b8ec8d65b8baaaaaaaaaaaa}

# (iteration focusing on bite chunk — near-identical brute-force script,
#  $flag = "flag{fec87c690b8ec8daaaaaaaaaaaaaaaaa}", $position = 20,
#  targetType "bite", index = $charPosition - 20)
```

*[image unavailable]*

```shell
# Consolidated version iterating every chunk type in one pass
$knownValues = @{
    'bitb' = @('04', '0C', '37', '5A', '55')  # Start with bitb chunk
    'bitc' = @('01', '5F', '6D', '53', '00')  # Move to bitc chunk next
    'bitd' = @('5A', '0C', '37', '5C', '06')  # Next chunk after bitc
    'bite' = @('54', '5C', '36', '5D', '00')  # bite chunk
    'bitf' = @('00', '58', '64', '03', '07')  # bitf chunk
    'bitg' = @('55', '0B', '36', '51', '57')  # bitg chunk
    'bith' = @('06', '59', '29', 'C2', 'C8')  # bith chunk
}

$flag = "flag{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}"

# Extract-PngChunks and Check-BiTChunk as above, with an added $chunkStartPos param;
# index = $charPosition - $chunkStartPos

$chunkTypeMap = @{
    'bitb' = 5
    'bitc' = 10
    'bitd' = 15
    'bite' = 20
    'bitf' = 25
    'bitg' = 30
    'bith' = 35
}

foreach ($chunkType in $chunkTypeMap.Keys) {
    $chunkStartPos = $chunkTypeMap[$chunkType]
    $expectedPairs = $knownValues[$chunkType]
    $position = $chunkStartPos
    while ($position -lt $chunkStartPos + 5) {
        # brute-force each character with png-challenge.exe as above
    }
}

Write-Host "`nFinal flag: $flag"
```

*[image unavailable]*

```shell
# Same consolidated loop, resetting $position = $chunkStartPos at the top of each chunk
```

The flag

```python
flag{fec87c690b8ec8d65b8b10ee7bb65d0}
```

After I was chatting with some others on their solutions, I saved their scripts here for my reference.

```shell
def extract_custom_chunks_from_png(png_file_path):
    with open(png_file_path, 'rb') as file:
        byte_data = file.read()

    custom_chunks = []
    i = 8  # Start after PNG header (8 bytes)

    while i < len(byte_data):
        if i + 4 > len(byte_data):
            break
        
        # Read chunk length
        length = int.from_bytes(byte_data[i:i + 4], 'big')
        i += 4

        if i + 4 > len(byte_data):
            break
        
        # Read chunk type
        chunk_type = byte_data[i:i + 4]
        i += 4

        # Read the chunk data if it's a custom chunk
        if chunk_type.startswith(b'biT'):
            chunk_data = byte_data[i:i + length]
            custom_chunks.append((chunk_type.decode('utf-8'), chunk_data))
        
        # Move past this chunk's data and CRC
        i += length + 4  # Skip chunk data and 4-byte CRC

    return custom_chunks


# Main execution
if __name__ == "__main__":
    png_file_path = "encoded 1x1.png"
    #png_file_path = "inconspicuous.png"
    custom_chunks = extract_custom_chunks_from_png(png_file_path)

    if not custom_chunks:
        print("No custom chunks found.")
    else:
        custom_chunks.sort(key=lambda x : x[0])
        z = ''.join([i[1].hex() for i in custom_chunks])
        print(z)
        #for chunk_type, chunk_data in custom_chunks:
        #    print(f"Custom Chunk Type: {chunk_type}, Data (hex): {chunk_data.hex()}")
```

```shell
from pwn import *
import subprocess
import string

# Known part of the flag
KNOWN_FLAG = 'flag{'
# Expected byte sequence in hexadecimal
e = "0405350619040c375a55015f6d53005a0c375c06545c365d000058640307550b365157065929c2c8"
# Convert expected hex string into a list of two-character segments
EXPECTED = [e[i:i+2] for i in range(0, len(e), 2)]

while True:
    for c in string.digits + string.ascii_lowercase + '}':
        # Create the current attempt by appending characters
        attempt = KNOWN_FLAG + c
        while len(attempt) < 38:
            attempt += 'a'
        
        # Run the command using subprocess
        subprocess.run(["png-challenge-debug.exe", "1x1.png", attempt], check=True)

        # Start the Python script to process the PNG file
        p = subprocess.Popen(['python', 'data.py'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = p.communicate()
        
        # Decode and strip the output
        s = stdout.decode('utf-8').strip()
        num = len(KNOWN_FLAG)
        # Create a list of bytes from the output string
        byte_list = [s[i:i+2] for i in range(0, len(s), 2)]
        
        # Check if the current character matches the expected one
        if byte_list[num] == EXPECTED[num]:
            KNOWN_FLAG += c
            print(KNOWN_FLAG)
            break
```

*[image unavailable]*

```shell
$values="a","b","c","d","e","f","0","1","2","3","4","5","6","7","8","9","}","l","{","g"
$final = "04","05" ,"35" ,"06", "19","04", "0c", "37", "5a", "55", "01", "5f", "6d", "53", "00", "5a", "0c", "37", "5c", "06", "54", "5c", "36", "5d", "00", "00", "58", "64", "03", "07", "55", "0b", "36", "51", "57", "06", "59", "29", "c2", "c8"

for ($r = 0; $r -lt 8 ; $r++) {
foreach($value in $values){
$position = $r+61
$pattern = "62-69-54-$position(?<MatchedCodes>(?:-[0-9A-Za-z]{2}){5})"
$before = "a"*(5*$r)
$after = "a"*(5*(7-$r))
$flag = "small.png $before$value$value$value$value$value$after"
Start-Process -FilePath .\png-challenge-debug.exe -ArgumentList $flag
start-sleep -Milliseconds 200
(Get-Content '.\encoded small.png' -Raw -Encoding Byte| % { [System.BitConverter]::ToString($_) } )-match $pattern |out-null
$currentvar= $matches['MatchedCodes'].trimstart('-').split('-')

for ($i = ($r*5); $i -le (($r*5)+5); $i++) {
    # Use modulus to get the correct index in comparison array
    $modIndex = $i % 5
    
    # Check the element in cyclic comparison slots
    if ($currentvar[$modIndex] -ieq $final[$i]) {
        # If they match, replace with the specified value
        $final[$i] = $value
    }
}
}

}
$final -join ''
```
