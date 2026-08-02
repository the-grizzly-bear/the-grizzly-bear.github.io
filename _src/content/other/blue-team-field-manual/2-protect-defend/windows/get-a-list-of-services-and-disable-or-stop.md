# Get a list of services and disable or stop:

```bash
C:\> sc query
C:\> sc config "<SERVICE NAME>" start= disabled
C:\> sc stop "<SERVICE NAME>"
C:\> wmic service where name='<SERVICE NAME>' call ChangeStartmode Disabled
```
