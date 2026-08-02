# 2024-10-07 System Code (Miscellaneous)

*[image unavailable]*

*[image unavailable]*

git clone the credited matrix
use 'find' to create a wordlist

*[image unavailable]*

Then scanned with the wordlist

*[image unavailable]*

Download all the files from the ctf url using the wordlist for the original fork

*[image unavailable]*

Directory downloaded

*[image unavailable]*

Tried another download cause I was wondering in circles

*[image unavailable]*

I figured out just check the hash against all, vs line for line which obv was different.

*[image unavailable]*

Tried a match against all matrix hashes, as soon as I didn't that I saw the different file excluding the 404s I didn't exclude in downloading

*[image unavailable]*

*[image unavailable]*

Analyzing the differences, we circle back to this field…

*[image unavailable]*

Used itertools.permutations to create a list of those values.

*[image unavailable]*

```shell
import itertools

# Define the matrix of characters
matrix = ['a', 'b', 'c', 'd', 'e', 'f']

# Generate all possible permutations of the matrix
permutations = itertools.permutations(matrix)

# Convert each permutation tuple to a string
wordlist = [''.join(permutation) for permutation in permutations]

# Save the wordlist to a file
with open('wordlist.txt', 'w') as file:
    for word in wordlist:
        file.write(word + '\n')

print("Wordlist saved to 'wordlist.txt'")
```

*[image unavailable]*

Used ffuf with the wordlist and find a status 200 okay page, different from the size and code from the otehrs

*[image unavailable]*

There's the flag

*[image unavailable]*

```python
Correct! Here is your flag: flag{dc9edf4624504202eec5d3fab10bbccd}
```

#####################################
#####################################
#####################################
#####################################
#####################################

Other notes, not really relevant, just the other rabbit holes I was digging into

[https://www.aperisolve.com/a0a7ef2c2767c7e04befb5f12592321a](https://www.aperisolve.com/a0a7ef2c2767c7e04befb5f12592321a)
[https://www.aperisolve.com/0201dfbecbf8d096fc6c156aad9b5438](https://www.aperisolve.com/0201dfbecbf8d096fc6c156aad9b5438)

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
