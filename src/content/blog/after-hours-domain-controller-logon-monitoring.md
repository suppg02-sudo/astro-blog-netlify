---
pubDatetime: 2026-02-12T17:01:16Z
title: "PowerShell Script for After-Hours Domain Controller Logon Monitoring"
postSlug: "after-hours-domain-controller-logon-monitoring"
description: "PowerShell Script for After-Hours Domain Controller Logon Monitoring"
tags:
  - active-directory
  - security
  - powershell
  - windows
  - monitoring
---

## Overview

Monitoring after-hours logons to Domain Controllers is a critical security practice. This PowerShell script automatically queries all Domain Controllers in your Active Directory environment and identifies unusual logon activity during off-hours (1:00 AM to 6:00 AM), providing a CSV report of security events and any errors encountered.

## What the Script Does

### Core Functionality

The script performs the following operations:

1. **Date Range Calculation**: Automatically looks back 30 days from today (configurable via `$DaysBack` variable)
2. **Domain Controller Discovery**: Queries Active Directory to find all Domain Controllers
3. **Event Log Query**: For each DC, queries the Security event log for Event ID 4624 (account logon events)
4. **Time-Based Filtering**: Filters events to only those occurring between 1:00 AM and 6:00 AM
5. **Data Extraction**: Extracts key details from each logon event
6. **Error Handling**: Catches and records connection/query errors for each DC
7. **CSV Export**: Creates two CSV files with the results

### Event ID 4624: Account Logon

Event ID 4624 in the Windows Security log represents a successful account logon event. This includes:
- **Who logged in** (account name, domain)
- **Where they logged in from** (workstation name, source IP)
- **How they authenticated** (logon type)
- **When they logged in** (timestamp)

Monitoring these events during after-hours windows helps detect:
- Unauthorized administrator access attempts
- Compromised account usage outside normal business hours
- Stolen credential exploitation
- Insider threat activity patterns

## Script Breakdown

```powershell
# Configuration variables
$DaysBack = 30
$StartDate = (Get-Date).AddDays(-$DaysBack)

# Discover all Domain Controllers
$DCs = Get-ADDomainController -Filter * | Select-Object -ExpandProperty HostName

# Initialize collections
$events = New-Object System.Collections.Generic.List[object]
$errors = New-Object System.Collections.Generic.List[object]

# Process each Domain Controller
foreach ($dc in $DCs) {
    try {
        # Query Security event log for Event ID 4624
        Get-WinEvent -ComputerName $dc -FilterHashtable @{
            LogName   = 'Security'
            Id        = 4624
            StartTime = $StartDate
        } -ErrorAction Stop |
        # Filter for 1:00 AM to 6:00 AM
        Where-Object {
            $_.TimeCreated.TimeOfDay -ge [TimeSpan]::FromMinutes(1) -and
            $_.TimeCreated.TimeOfDay -lt [TimeSpan]::FromHours(6)
        } |
        # Extract relevant properties
        ForEach-Object {
            $events.Add([pscustomobject]@{
                TimeCreated = $_.TimeCreated
                Account     = $_.Properties[5].Value
                Domain      = $_.Properties[6].Value
                LogonType   = $_.Properties[8].Value
                Workstation = $_.Properties[11].Value
                SourceIP    = $_.Properties[18].Value
                DC          = $dc
            })
        }
    }
    catch {
        # Record any errors
        $errors.Add([pscustomobject]@{
            DC    = $dc
            Error = $_.Exception.Message
        })
    }
}

# Export results to CSV
$events | Sort-Object TimeCreated |
Export-Csv C:\Temp\AfterHours_Logons_Last_30_Days.csv -NoTypeInformation

$errors |
Export-Csv C:\Temp\AfterHours_Logons_DC_Errors.csv -NoTypeInformation
```

## Key Properties Extracted

| Property | Meaning | Use Case |
|----------|----------|-----------|
| **TimeCreated** | Timestamp of logon event | Time-based analysis, trend identification |
| **Account** | User account name that logged in | Identifying who accessed the system |
| **Domain** | Active Directory domain | Distinguishing between forest domains |
| **LogonType** | Type of logon (Type 2, 3, etc.) | Differentiating interactive vs. service logons |
| **Workstation** | Computer name from which logon originated | Tracking source workstation |
| **SourceIP** | IP address of logon source | Geographic analysis, anomaly detection |
| **DC** | Domain Controller processing the logon | Identifying which DC authenticated the request |

## Output Files

### Primary Output: AfterHours_Logons_Last_30_Days.csv

Contains all after-hours logon events sorted chronologically. Each row represents a logon event meeting the time criteria.

**Analysis Use Cases**:
- Identify accounts with frequent after-hours access
- Spot IP addresses appearing from unusual locations
- Detect service accounts used for interactive logons
- Create time-based heatmaps of suspicious activity
- Correlate with security incident tickets

### Error Log: AfterHours_Logons_DC_Errors.csv

Contains any errors encountered during the script execution. Each row includes:
- **DC**: Domain Controller hostname
- **Error**: Exception or error message

**Common Error Types**:
- **RPC Server Unavailable**: DC is offline or unreachable
- **Access Denied**: Insufficient permissions to query event logs
- **Event Log Not Found**: Security log was cleared or corrupted
- **Network Timeout**: Connection issues during query

## Customization Options

### Adjusting the Date Range

```powershell
# Look back 7 days instead of 30
$DaysBack = 7
$StartDate = (Get-Date).AddDays(-$DaysBack)
```

### Changing the Time Window

```powershell
# Monitor 6:00 PM to 12:00 AM (night shift)
Where-Object {
    $_.TimeCreated.TimeOfDay -ge [TimeSpan]::FromHours(18) -and
    $_.TimeCreated.TimeOfDay -lt [TimeSpan]::FromHours(24)
}
```

### Filtering Specific Accounts

```powershell
# Add account filter after extracting events
ForEach-Object {
    if ($_.Properties[5].Value -notmatch '^(svc_|mssql_|_svc_)') {
        $events.Add(...)
    }
}
```

### Targeting Specific Domain Controllers

```powershell
# Only query specific DCs instead of all
$DCs = @("DC01", "DC02", "DC03")
```

## Security Use Cases

### 1. Detecting Compromised Admin Accounts

**Scenario**: An attacker obtains Domain Admin credentials and accesses systems during off-hours to avoid detection.

**Detection**:
```powershell
# Run script daily via scheduled task
# Analyze output for repeated admin account logons
Import-Csv C:\Temp\AfterHours_Logons_Last_30_Days.csv |
Where-Object { $_.Account -match 'Admin|Administrator' } |
Group-Object Account, Workstation |
Select-Object Name, Count, @{Name='LastLogon';Expression={$_.Group[-1].TimeCreated}} |
Sort-Object Count -Descending
```

### 2. Identifying Lateral Movement

**Scenario**: Attacker uses compromised account to access multiple workstations after hours.

**Detection**:
- **Pattern**: Same account, same source IP, multiple different workstations
- **Indicator**: One workstation accessed every 5-15 minutes during off-hours
- **Action**: Block source IP, rotate credentials, investigate workstation compromise

### 3. Spotting Service Account Abuse

**Scenario**: Service account used for interactive logon (credential theft).

**Detection**:
```powershell
# Filter for interactive logon types (Type 2, 3)
Import-Csv C:\Temp\AfterHours_Logons_Last_30_Days.csv |
Where-Object { $_.LogonType -eq '2' -or $_.LogonType -eq '3' } |
Where-Object { $_.Account -match '^svc_|^mssql_|^iis_|^sql_' } |
Select-Object TimeCreated, Account, Workstation, SourceIP
```

### 4. Correlating with Geographic Data

**Scenario**: Source IP addresses are from unexpected geographic locations.

**Detection**:
- Extract `SourceIP` column
- Run through IP geolocation service
- Flag logons from countries where your organization has no presence
- Create alerts for cross-border access during off-hours

## Deployment Considerations

### Scheduled Task Configuration

```powershell
# Create daily scheduled task at 6:30 AM (after monitoring window)
$action = New-ScheduledTaskAction -Execute 'PowerShell.exe' `
    -Argument '-File "C:\Scripts\AfterHoursLogonMonitor.ps1"'

$trigger = New-ScheduledTaskTrigger -Daily -At 6:30am

Register-ScheduledTask -TaskName "After-Hours Logon Monitor" `
    -Action $action `
    -Trigger $trigger `
    -User "DOMAIN\security.account" `
    -RunLevel Highest
```

### Permissions Required

The account running the script needs:
- **Read access** to Active Directory: `Get-ADDomainController`
- **Read access** to Security event logs on all DCs: `Get-WinEvent`
- **Write access** to output directory: `C:\Temp\`

Recommended: Use a dedicated service account with minimum required permissions, not a Domain Admin.

### Performance Optimization

For large environments (50+ DCs, high log volume):

```powershell
# Query only specific DCs to reduce overhead
$DCs = Get-ADDomainController | Where-Object { $_.HostName -match '^DC[0-9]{2}$' }

# Limit time range to reduce dataset size
$DaysBack = 7  # Weekly review instead of monthly

# Use `-MaxEvents` to prevent memory issues
Get-WinEvent -MaxEvents 10000 -FilterHashtable @{
    LogName   = 'Security'
    Id        = 4624
    StartTime = $StartDate
}
```

## Limitations and Mitigations

### Limitation: Log Retention

**Issue**: Security event logs may be overwritten if retention policy is insufficient.

**Mitigation**:
- Set minimum retention to 30+ days
- Forward events to SIEM/log aggregation system
- Archive logs regularly to long-term storage

### Limitation: Distributed Environments

**Issue**: Script queries each DC individually; may miss logons if load balancing occurs.

**Mitigation**:
- Include authentication DC in output (already done via `$dc` property)
- Correlate events across multiple DCs in post-processing
- Consider querying Active Directory domain controllers vs. authentication servers

### Limitation: False Positives

**Issue**: Legitimate after-hours activity (maintenance, deployments, on-call).

**Mitigation**:
- Maintain whitelist of expected after-hours access patterns
- Correlate with change management tickets
- Review findings manually before alerting

## Enhancing the Script

### Email Alerting

```powershell
# Add email notification for suspicious activity
$suspiciousEvents = Import-Csv C:\Temp\AfterHours_Logons_Last_30_Days.csv |
    Where-Object { $_.Account -match 'Admin' -and $_.SourceIP -notmatch '10\.|192\.168\.|172\.' }

if ($suspiciousEvents) {
    Send-MailMessage -From 'security@domain.com' `
        -To 'soc@domain.com' `
        -Subject "After-Hours Admin Logon Alert" `
        -Body "Suspicious after-hours logons detected. Review attached CSV." `
        -Attachments $suspiciousEvents |
        -SmtpServer 'smtp.domain.com'
}
```

### Integration with SIEM

```powershell
# Convert to syslog format for SIEM ingestion
$events | ForEach-Object {
    $syslogMessage = "<134>$(Get-Date -Format 'MMM dd HH:mm:ss') hostname powershell[$($_.Account)]: After-hours logon from $($_.SourceIP) on $($_.Workstation)"
    $syslogMessage | Out-File -FilePath "C:\Temp\afterhours_logons.log" -Append
}
```

## Best Practices

1. **Run Daily**: Schedule execution every morning after the monitoring window closes
2. **Review Weekly**: Analyze trends in the CSV data manually
3. **Investigate Immediately**: Flag any admin account or privileged service logons during off-hours
4. **Maintain Baseline**: Document expected after-hours access patterns for legitimate maintenance
5. **Automate Escalation**: Integrate with ticketing system for automatic incident creation
6. **Secure Output**: Delete old CSV files after archiving; restrict file system permissions
7. **Audit Script**: Regularly review the script itself for unauthorized modifications

## Conclusion

This PowerShell script provides a foundational tool for detecting suspicious after-hours access to Domain Controllers in Active Directory environments. By automatically querying all DCs, filtering for off-hours activity, and exporting structured CSV data, it enables security teams to identify potential credential theft, compromised accounts, or insider threats.

The script's modular design allows customization for specific organizational requirements, time windows, and alerting mechanisms. Coupled with regular review processes and integration with existing security infrastructure (SIEM, ticketing systems), it becomes an effective layer in a defense-in-depth strategy.

Remember: **Detection is only the first step**. Investigating flagged events and understanding the context of legitimate after-hours access is equally important to avoid alert fatigue and false positives.

---

## References

- [Windows Security Event ID 4624 Documentation](https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/event-4624)
- [Get-WinEvent PowerShell Documentation](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-winevent)
- [Active Directory Best Practices for Auditing](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/ad-ds-auditing)