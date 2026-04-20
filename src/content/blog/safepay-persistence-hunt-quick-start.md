---
pubDatetime: 2026-02-07T00:00:00Z
title: "SafePay Persistence Hunt - Centralized Deployment Quick Start Guide"
postSlug: "safepay-persistence-hunt-quick-start"
description: "SafePay Persistence Hunt - Centralized Deployment Quick Start Guide"
tags:
  - security
  - incident-response
  - powershell
  - safepay
  - persistence-hunting
---

# QUICK START GUIDE
## SafePay Persistence Hunt - Centralized Deployment

---

## 🚀 Get Started in 5 Minutes

### Step 1: Prepare Your Server List

Create a file called `servers.txt` with your server names (one per line):

```
SERVER01
SERVER02
DC01
SQL-SERVER
FILESERVER
```

Or export from Active Directory:
```powershell
Get-ADComputer -Filter 'OperatingSystem -like "*Server*"' | 
    Select-Object -ExpandProperty Name | 
    Out-File "servers.txt"
```

---

### Step 2: Choose Your Deployment Method

**Option A: PowerShell Remoting (Fastest - Recommended for Immediate Use)**
```powershell
# Run this command
.\Deploy-PersistenceHunt.ps1 `
    -ComputerList "servers.txt" `
    -CentralResultsPath "\\YOURFILESERVER\IT\SafePay_Hunt"
```

**Option B: SCCM (Best for Organization-Wide)**
- See full instructions in `Deployment_Guide.md`

**Option C: Group Policy (Best for Scheduled)**
- See full instructions in `Deployment_Guide.md`

---

### Step 3: Review Results

After deployment completes, open the HTML report:
```
\\YOURFILESERVER\IT\SafePay_Hunt\Collection_[TIMESTAMP]\Consolidated\Consolidated_Report.html
```

---

## 📁 File Reference

### Core Scripts (Run Individually on Single Server)
- `Master-PersistenceHunt.ps1` - Runs all checks on current server
- `Hunt-ScheduledTasks.ps1` - Scheduled tasks only
- `Hunt-Services.ps1` - Windows services only
- `Hunt-RegistryPersistence.ps1` - Registry persistence only
- `Hunt-RemoteAccessTools.ps1` - Remote access tools only

### Deployment Scripts (Run from Management Server)
- `Deploy-PersistenceHunt.ps1` - Deploy to multiple servers
- `Consolidate-Results.ps1` - Combine results (auto-runs)

### Documentation
- `SafePay_Persistence_Hunting_Guide.md` - Complete hunting guide
- `Deployment_Guide.md` - Detailed deployment instructions
- `README_QUICK_START.md` - This file

---

## ⚡ Common Usage Scenarios

### Scenario 1: Test on One Server First
```powershell
# Single server test
.\Deploy-PersistenceHunt.ps1 `
    -ComputerList "TESTSERVER01" `
    -CentralResultsPath "\\FILESERVER\IT\SafePay_Hunt"
```

### Scenario 2: Hunt on All Domain Controllers
```powershell
# Get all DCs
$dcs = Get-ADDomainController -Filter * | Select-Object -ExpandProperty HostName
$dcs | Out-File "dcs.txt"

# Deploy
.\Deploy-PersistenceHunt.ps1 `
    -ComputerList "dcs.txt" `
    -CentralResultsPath "\\FILESERVER\IT\SafePay_Hunt"
```

### Scenario 3: Hunt on Specific OU
```powershell
# Get servers from OU
Get-ADComputer -Filter * -SearchBase "OU=Servers,OU=Production,DC=domain,DC=com" |
    Select-Object -ExpandProperty Name |
    Out-File "prod_servers.txt"

# Deploy
.\Deploy-PersistenceHunt.ps1 `
    -ComputerList "prod_servers.txt" `
    -CentralResultsPath "\\FILESERVER\IT\SafePay_Hunt"
```

### Scenario 4: Already Ran Scripts Manually, Just Collect Results
```powershell
# If scripts were already run on servers manually
.\Deploy-PersistenceHunt.ps1 `
    -ComputerList "servers.txt" `
    -CentralResultsPath "\\FILESERVER\IT\SafePay_Hunt" `
    -CollectOnly
```

---

## 🎯 What to Look for in Results

### CRITICAL Priority (Investigate Immediately)
✅ **ScreenConnect/ConnectWise** - SafePay's preferred remote access tool
✅ **Encoded PowerShell** in scheduled tasks (-enc, -encodedcommand)
✅ **Services running from %TEMP% or %APPDATA%**

### HIGH Priority (Investigate Soon)
⚠️ **Other remote access tools** (TeamViewer, AnyDesk, etc.)
⚠️ **Scheduled tasks running from user directories**
⚠️ **Registry Run keys with scripting executables**

### Your Incident Timeline
📅 **Initial Breach:** October 21, 2024
📅 **Detection:** January 13, 2025
📅 **Dwell Time:** ~84 days

**Focus on items created or modified during this period!**

---

## 🔧 Prerequisites Check

Before running deployment, verify:

### For PowerShell Remoting:
```powershell
# Test WinRM on target servers
Test-WSMan SERVER01

# If failed, enable on target:
Enable-PSRemoting -Force
```

### For File Share Access:
```powershell
# Create central results directory
New-Item -ItemType Directory -Path "\\FILESERVER\IT\SafePay_Hunt" -Force

# Test write access
New-Item -Path "\\FILESERVER\IT\SafePay_Hunt\test.txt" -ItemType File
```

### For Credentials:
```powershell
# Prepare credentials if needed
$cred = Get-Credential -Message "Enter Domain Admin credentials"

# Use in deployment
.\Deploy-PersistenceHunt.ps1 `
    -ComputerList "servers.txt" `
    -CentralResultsPath "\\FILESERVER\IT\SafePay_Hunt" `
    -Credential $cred
```

---

## 📊 Understanding the Output

### Individual Server Results
Each server will have a folder with these files:
- `SuspiciousScheduledTasks_*.csv` - Scheduled tasks findings
- `SuspiciousServices_*.csv` - Service findings
- `RegistryPersistence_*.csv` - Registry persistence
- `RemoteAccessTools_*.csv` - Remote access tools
- `Report_Summary.html` - Individual server report

### Consolidated Results
After running on multiple servers:
- `Consolidated/All_ScheduledTasks.csv` - All servers combined
- `Consolidated/All_Services.csv` - All services across fleet
- `Consolidated/Priority_Findings.csv` - **START HERE**
- `Consolidated/Server_Summary.csv` - Risk levels per server
- `Consolidated/Consolidated_Report.html` - **MAIN REPORT**

---

## 🆘 Troubleshooting

### Error: "Access Denied"
```powershell
# Solution: Run with explicit credentials
$cred = Get-Credential
.\Deploy-PersistenceHunt.ps1 -ComputerList "servers.txt" -CentralResultsPath "\\FILESERVER\IT\SafePay_Hunt" -Credential $cred
```

### Error: "WinRM cannot complete the operation"
```powershell
# Solution: Enable WinRM on target server
Invoke-Command -ComputerName SERVER01 -ScriptBlock { Enable-PSRemoting -Force }

# Or via PsExec if PSRemoting not available
psexec \\SERVER01 -s powershell Enable-PSRemoting -Force
```

### Error: "Cannot find path"
```powershell
# Solution: Verify network share is accessible
Test-Path "\\FILESERVER\IT\SafePay_Hunt"

# Create if doesn't exist
New-Item -ItemType Directory -Path "\\FILESERVER\IT\SafePay_Hunt" -Force
```

---

## 📞 Next Steps After Review

1. **Share with Aspire SOC** - Send them the consolidated CSV files
2. **Coordinate with Acumen** - Provide Priority_Findings.csv for analysis
3. **Document findings** for your incident response timeline
4. **Plan remediation** for confirmed threats
5. **Implement monitoring** using EDR queries from the guide

---

## 📚 Additional Resources

- **Complete Hunting Guide**: `SafePay_Persistence_Hunting_Guide.md`
  - CrowdStrike Falcon queries
  - Microsoft Defender queries
  - Sysinternals tool usage
  - SafePay-specific IOCs

- **Deployment Methods**: `Deployment_Guide.md`
  - GPO deployment
  - SCCM deployment
  - Intune deployment
  - Advanced scenarios

---

## 🎯 Recommended Immediate Action Plan

### Today (Within 2 Hours)
```powershell
# 1. Test on one critical server
.\Deploy-PersistenceHunt.ps1 -ComputerList "CRITICAL-SERVER" -CentralResultsPath "\\FILESERVER\IT\SafePay_Hunt"

# 2. Review results
Start-Process "\\FILESERVER\IT\SafePay_Hunt\Collection_*\Consolidated\Consolidated_Report.html"

# 3. If successful, deploy to all critical servers (breach entry points, DCs)
```

### This Week
```powershell
# Deploy organization-wide via SCCM or GPO
# See Deployment_Guide.md for instructions
```

### Ongoing
- Implement EDR detection rules from hunting guide
- Schedule monthly persistence hunts
- Monitor for ScreenConnect installations
- Review new remote access tool deployments

---

## 💡 Pro Tips

1. **Run on your known breach entry point first** - this server is most likely to have persistence
2. **Cross-reference all findings with Oct 21 - Jan 13 timeline** - focus on this window
3. **Don't panic at volume of results** - the consolidated report prioritizes findings
4. **Save your deployment for future use** - you can re-run monthly for ongoing monitoring
5. **Share ScreenConnect findings immediately** - this is SafePay's favorite tool

---

## Support

For questions or issues:
1. Review `Deployment_Guide.md` for detailed troubleshooting
2. Check `SafePay_Persistence_Hunting_Guide.md` for hunting techniques
3. Coordinate with your SOC (Aspire) and security partner (Acumen)

---

**Good hunting! 🔍**