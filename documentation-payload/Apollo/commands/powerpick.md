+++
title = "powerpick"
chapter = false
weight = 103
hidden = false
+++

## Summary
Execute PowerShell commands as post-exploitation job.

### Arguments (positional)
#### command
PowerShell command to be executed.

## Usage
```
powerpick [command]
```

## Detailed Summary
The `powerpick` command uses process injection and the CLR loader to create a PowerShell runspace and execute commands in a sacrificial process. This method allows stability for long running PowerShell commands and scripts. Any PowerShell scripts loaded with the `psimport` command will be loaded into the runspace prior to command execution, allowing cmdlets from these scripts to be available to operators. PowerShellv4 is used by default.