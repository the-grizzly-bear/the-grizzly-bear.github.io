# DHCP

Enable DHCP server logging:

```bash
C:\> reg add
HKLM\System\CurrentControlSet\Services\DhcpServer\Parameters /v ActivityLogFlag /t REG_DWORD /d 1
```

Default Location Windows 2003/2008/2012:

```bash
C:\> %windir%\System32\Dhcp
```
