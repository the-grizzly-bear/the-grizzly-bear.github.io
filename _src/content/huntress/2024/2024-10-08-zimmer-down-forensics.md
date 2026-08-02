# 2024-10-08-Zimmer Down (Forensics)

Really danced around this one, sometimes the flg stuff is jsut too obvious and annoying.

Run regripper -r NTUSER.DAT -f ntuser

*[image unavailable]*

*[image unavailable]*

Some stuff from recmd.exe wasn't working

*[image unavailable]*

Registry Explorer also showed the same

*[image unavailable]*

*[image unavailable]*

All it was as the base62 encoded file name

*[image unavailable]*

```python
flag{4b676ccc1070be66b1a15d8601c8d500}
```

Trying the plugins for extraction

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*

*[image unavailable]*
