---
pubDatetime: 2026-03-17T06:00:02Z
title: "OpenCode Log Analysis Report - 2026-03-17"
postSlug: "opencode-log-analysis-2026-03-17"
description: "OpenCode Log Analysis Report - 2026-03-17"
tags:
  - opencode
  - logs
  - system-health
  - monitoring
---

## Summary

| Metric | Count |
|--------|-------|
| Total Errors | 4 |
| Total Warnings | 1 |
| Sources Analyzed | 3 |

## System Status

- **OpenCode Web**: 🔴 inactive
- **Disk**: /dev/sda1        96G   88G  8.0G  92% /
- **Memory**: Mem:           6.6Gi       5.3Gi       486Mi        23Mi       1.4Gi       1.3Gi

## Errors by Source

- **opencode-web.log**: 2 issues
- **async_recording.log**: 2 issues
- **opencode-server.log**: 1 issues

## Notable Issues

### Warning

- **WARNING**: OPENCODE_SERVER_PASSWORD is not set; server is unsecured.

### Failure

- **ERROR**: start server on port 4096
  - 💡 *Solution*: OpenCode web service is already running. Check systemd status: `systemctl status opencode-web`
- **ERROR**: start server on port 8765
  - 💡 *Solution*: Port 8765 is used by another service (likely Homepage). Consider changing port allocation.

### Log Error

- **ERROR**: Failed to record question: unhashable type: 'list'
  - 💡 *Solution*: Python type error in recording logic. Check for list being used as dict key.
- **ERROR**: Failed to record: unhashable type: 'list'
  - 💡 *Solution*: Python type error in recording logic. Check for list being used as dict key.

## Recommendations

### 🟡 Security

**Issue**: OpenCode server password not configured

**Action**: Set OPENCODE_SERVER_PASSWORD environment variable in systemd service file.

```bash
grep OPENCODE_SERVER_PASSWORD /etc/systemd/system/opencode-*.service
```

### 🟡 Data Recording

**Issue**: Recording errors detected (2 occurrences)

**Action**: Check context-registry async recording logic for type errors.

```bash
tail -100 ~/.config/opencode/context-registry/logs/async_recording.log
```


---

*Report generated automatically by OpenCode Log Analyzer.*

*Next report: Tomorrow at 6:00 AM UTC*