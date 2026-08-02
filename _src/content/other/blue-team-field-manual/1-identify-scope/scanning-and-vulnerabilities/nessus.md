# NESSUS

Basic Nessus scan:

```bash
nessus -q -x -T html <NESSUS SERVER IP ADDRESS><NESSUS SERVER PORT 1241 > <ADMIN ACCOUNT> <ADMIN PASSWORD> <FILE WITH TARGETS>,txt <RESULTS FILE NAME>.html 

nessus [-vnh] [-c .refile] [-VJ [-T <format>]
```

Batch-mode scan:

```bash
nessus -q [-pPS] <HOST> <PORT> <USER NAME><PASSWORD> <targets-file> <result-file>
```

Report conversion:

```bash
nessus -i in. [nsr|nbe] -oout. [xml|nsr|nbe|html|txt]
```
