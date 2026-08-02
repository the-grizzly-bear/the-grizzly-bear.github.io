# STAND ALONE SYSTEM - WITHOUT ACTIVE DIRECTORY (AD)

Disallow running a .exe file:

```bash
C:\> reg add
"HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer" /v DisallowRun /t REG_DWORD /d "00000001" /f
C:\> reg add "HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer\DisallowRun" /v badfile.exe /t REG_SZ /d <BAD FILE NAME>.exe /f
```

Disable Remote Desktop:

```bash
C:\> reg add "HKLM\SYSTEM\CurrentControlSet\Control\TerminalServer" /f /v fDenyTSConnections /t REG_DWORD /d 1
```

Send NTLMv2 response only/refuse LM and NTLM: (Windows 7 default)

```bash
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa\ /v lmcompatibilitylevel /t REG_DWORD /d 5 /f
```

Restrict Anonymous Access:

```bash
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /v restrictanonymous /t REG_DWORD /d 1 /f
```

Do not allow anonymous enumeration of SAM accounts<br>and shares:

```bash
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /vrestrictanonymoussam /t REG_DWORD /d 1 /f
```

Disable IPV6:

```bash
C:\> reg add HKLM\SYSTEM\CurrentControlSet\services\TCPIP6\Parameters /v DisabledComponents /t REG_DWORD /d 255 /f
```

Disable sticky keys:

```bash
C:\> reg add "HKCU\ControlPanel\Accessibility\StickyKeys" /v Flags /t REG_SZ /d 506 /f Disable Toggle Keys:
C:\> reg add "HKCU\ControlPanel\Accessibility\ ToggleKeys" /v Flags /t REG_SZ Id 58 /f
```

Disable Filter Keys:

```bash
C:\> reg add "HKCU\ControlPanel\Accessibility\Keyboard Response" /v Flags /t REG_SZ /d 122 /f
```

Disable On-screen Keyboard:

```bash
C:\> reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Authentication\LogonUI /f /v ShowTabletKeyboard /t REG_DWORD /d 0
```

Disable Administrative Shares - Workstations:

```bash
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters /f /v AutoShareWks /t REG_DWORD /d 0
```

Disable Administrative Shares - Severs

```bash
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Services\LanmanServer\Parameters /f /v AutoShareServer /t REG_DWORD /d 0
```

Remove Creation of Hashes Used to Pass the Hash Attack (Requires password reset and reboot to purge old hashes):

```bash
C:\> reg add HKLM\SYSTEM\CurrentControlSet\Control\Lsa /f /v NoLMHash /t REG_DWORD /d 1
```

To Disable Registry Editor: (High Risk)

```bash
C:\> reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\System /v DisableRegistryTools /t REG_DWORD /d 1 /f
```

Disable IE Password Cache:

```bash
C:\> reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings /v DisablePasswordCaching /t REG_DWORD/d 1 /f
```

Disable CMD prompt:

```bash
C:\> reg add HKCU\Software\Policies\Microsoft\Windows\System /v DisableCMD /t REG_DWORD /d 1 /f
```

Disable Admin credentials cache on host when using RDP:

```bash
C:\> reg add HKLM\System\CurrentControlSet\Control\Lsa /v DisableRestrictedAdmin /t REG_DWORD /d 0 /f
```

Do not process the run once list:

```bash
C:\> reg add HKLM\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v DisableLocalMachineRunOnce /t REG_DWORD /d 1
C:\> reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Policies\Explorer /v DisableLocalMachineRunOnce /t REG_DWORD /d 1
```

Require User Access Control (UAC) Permission:

```bash
C:\> reg add HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v EnableLUA /t REG_DWORD /d 1 /f
```

Change password at next logon:

```bash
PS C:\> Set-ADAccountPassword <USER> -NewPassword $newpwd -Reset -PassThru | Set-ADuser ChangePasswordAtLogon $True
```

Change password at next logon for OU Group:

```bash
PS C:\> Get-ADuser -filter "department -eq '<OU GROUP>' -AND enabled -eq 'True | Set-ADuser -ChangePasswordAtLogon $True
```

Enabled Firewall logging:

```bash
C:\> netsh firewall set logging droppedpackets connections = enable
```
