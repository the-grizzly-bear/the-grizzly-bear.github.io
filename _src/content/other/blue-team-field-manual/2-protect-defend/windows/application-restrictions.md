# APPLICATION RESTRICTIONS

Applocker - Server 2008 R2 or Windows 7 or higher:<br>Using GUI Wizard configure:

-Executable Rules (.exe, .com)<br>-DLL Rules (.dll, .ocx)<br>-Script Rules (.psl, .bat, .cmd, .vbs, .js)<br>-Windows Install Rules (.msi, .msp, .mst)<br>Steps to employ Applocker (GUI is needed for digital<br>signed app restrictions):

Step 1: Create a new GPO.
Step 2: Right-click on it to edit, and then navigate through Computer Configuration, Policies, Windows Settings, Security Settings, Application Control Policies and Applocker. Click Configure Rule Enforcement.
Step 3: Under Executable Rules, check the Configured box and then make sure Enforce Rules is selected from the drop-down box. Click OK.
Step 4: In the left pane, click Executable Rules.
Step 5: Right-click in the right pane and select Create New Rule.
Step 6: On the Before You Begin screen, click Next.
Step 7: On the Permissions screen, click Next.
Step 8: On the Conditions screen, select the Publisher condition and click Next.
Step 9: Click the Browse button and browse to any executable file on your system. It doesn't matter which.
Step 10: Drag the slider up to Any Publisher and then click Next.
Step 11: Click Next on the Exceptions screen.
Step 12: Name policy, Example uonly run executables that are signed" and click Create.
Step 13: If this is your first time creating an Applocker policy, Windows will prompt you to create default rule, click Yes.
Step 14: Ensure Application Identity Service is Running.

```bash
C:\> net start AppIDSvc
C:\> REG add "HKLM\SYSTEM\CurrentControlSet\services\AppIDSvc" /v Start /t REG_DWORD /d 2 /f
```

Step 15: Changes require reboot.

```bash
C:\ shutdown.exe /r
C:\ shutdown.exe /r /m \\<IP ADDRESS OR COMPUTER NAME> /f
```

Add the Applocker cmdlets into PowerShell:

```bash
PS C:\> import-module Applocker
```

Gets the file information for all of the executable<br>files and scripts in the directory C:\Windows\System32:

```bash
PS C:\> Get-ApplockerFileinformation -Directory C:\Windows\System32\ -Recurse -FileType Exe, Script
```

Create a Applocker Policy that allow rules for all of the executable files in C:\Windows\System32:

```bash
PS C:\> Get-Childitem C:\Windows\System32\*,exe | Get-ApplockerFileinformation | New-ApplockerPolicy RuleType Publisher, Hash -User Everyone - RuleNamePrefix System32
```

Sets the local Applocker policy to the policy specified in C:\Policy.xml:

```bash
PS C:\> Set-AppLockerPolicy -XMLPolicy C:\Policy.xml
```

Uses the Applocker policy in C:\Policy.xml to test whether calc.exe and notepad.exe are allowed to run for users who are members of the Everyone group. If you do not specify a group, the Everyone group is used by default:

```bash
PS C:\> Test-AppLockerPolicy -XMLPolicy
C:\Policy.xml -Path C:\Windows\System32\calc.exe,
C:\Windows\System32\notepad.exe -User Everyone
```

Review how many times a file would have been blocked from running if rules were enforced:

```bash
PS C:\> Get-ApplockerFileinformation -Eventlog -Logname "Microsoft-Windows-Applocker\EXE and DLL" EventType Audited -Statistics
```

Creates a new Applocker policy from the audited events in the local Microsoft-Windows-Applocker/EXE and DLL event log, applied to \<GROUP\> and current Applocker policy will be overwritten:

```bash
PS C:\> Get-ApplockerFileinformation -Eventlog -LogPath "Microsoft-Windows-AppLocker/EXE and DLL" EventType Audited | New-ApplockerPolicy -RuleType
Publisher,Hash -User domain\<GROUP> -IgnoreMissingFileinformation | Set-ApplockerPolicy -LDAP "LDAP://<DC>,<DOMAIN>.com/CN={31B2F340-016D11D2-945F00C04FB984F9},CN=Policies,CN=System,DC=<DOMAIN>,DC=com"
```

Export the local Applocker policy, comparing User's explicitly denied access to run, and output text file:

```bash
PS C:\> Get-AppLockerPolicy -Local | Test­AppLockerPolicy -Path C:\Windows\System32\*,exe User domain\<USER NAME> -Filter Denied | Format-List
-Property Path > C:\DeniedFiles.txt
```

Export the results of the test to a file for analysis:

```bash
PS C:\> Get-Childitem <DirectoryPathtoReview> Filter <FileExtensionFilter> -Recurse I Convert-Path | Test-ApplockerPolicy -XMLPolicy <PathToExportedPolicyFile> -User <domain\username> Filter <TypeofRuletoFilterFor> | Export-CSV <PathToExportResultsTo.CSV>
```

GridView list of any local rules applicable:

```bash
PS C:\> Get-AppLockerPolicy -Local -Xml I Out­GridView
```
