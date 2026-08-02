# HASHING

Hash all executable files in these specified<br>locations:

```bash
find /<PATHNAME TO ENUMERATE> -type f -exec mdSsum {} >> mdSsums.txt \; 
```

```bash
md5deep -rs /> mdSsums.txt
```
