---
pubDatetime: 2026-02-27T14:44:35Z
title: "System Health Report - February 27, 2026"
postSlug: "roundup-system-health-report"
description: "System Health Report - February 27, 2026"
tags:
  - roundup
  - server
  - system-health
  - monitoring
---

# Roundup System Health Report

**Generated:** 2026-02-27 14:44 UTC | **Server:** ubuntu4

---


---

[2026-02-27T14:44:31+00:00] Starting roundup report...
## System Performance

```
 14:44:31 up  5:37,  3 users,  load average: 2.47, 0.93, 0.64

               total        used        free      shared  buff/cache   available
Mem:           1.8Gi       1.3Gi       249Mi       3.3Mi       495Mi       523Mi
Swap:          5.0Gi       2.8Gi       2.2Gi

Filesystem      Size  Used Avail Use% Mounted on
/dev/sdc1        48G   33G   15G  69% /
```

## Memory Alerts

✅ No OOM events in last 24 hours

## Container Status

| Container | Status | Ports |
|-----------|--------|-------|
| jolly_antonelli | Up 2 seconds |  |
| olivetin | Up About an hour (healthy) | 0.0.0.0:1337->1337/tcp, [::]:1337->1337/tcp |
| relay | Up 3 hours |  |
| freshrss | Up 6 hours | 0.0.0.0:8282->80/tcp, [::]:8282->80/tcp |
| hugo | Up 6 hours | 0.0.0.0:1313->1313/tcp, [::]:1313->1313/tcp |
| astro-fresh | Up 3 hours | 0.0.0.0:8086->4321/tcp, [::]:8086->4321/tcp |
| prometheus | Up 6 hours | 0.0.0.0:9090->9090/tcp, [::]:9090->9090/tcp |
| node-exporter | Up 6 hours | 0.0.0.0:9100->9100/tcp, [::]:9100->9100/tcp |
| cronmaster | Up 6 hours | 0.0.0.0:40123->3000/tcp, [::]:40123->3000/tcp |
| nextexplorer | Up 6 hours (healthy) | 0.0.0.0:8080->3000/tcp, [::]:8080->3000/tcp |
| fossflow | Up 6 hours | 3001/tcp, 0.0.0.0:3080->80/tcp, [::]:3080->80/tcp |
| filebrowser | Up 6 hours (healthy) | 0.0.0.0:2280->80/tcp, [::]:2280->80/tcp |
| dashdot | Up 6 hours | 0.0.0.0:3001->3001/tcp, [::]:3001->3001/tcp |
| memos | Up 50 seconds | 0.0.0.0:5230->5230/tcp, [::]:5230->5230/tcp |
| n8n | Up Less than a second | 0.0.0.0:5678->5678/tcp, [::]:5678->5678/tcp |
| homepage | Up About an hour (healthy) | 0.0.0.0:8765->3000/tcp, [::]:8765->3000/tcp |
| grafana-otel | Up 6 hours | 0.0.0.0:3003->3000/tcp, [::]:3003->3000/tcp |
| otel-collector | Up 6 hours | 0.0.0.0:4317-4318->4317-4318/tcp, [::]:4317-4318->4317-4318/tcp, 0.0.0.0:8889->8889/tcp, [::]:8889->8889/tcp, 0.0.0.0:13133->13133/tcp, [::]:13133->13133/tcp, 55679/tcp |
| nginxproxy | Up 6 hours | 0.0.0.0:80-81->80-81/tcp, [::]:80-81->80-81/tcp, 0.0.0.0:443->443/tcp, [::]:443->443/tcp |
| portainer | Up 6 hours | 0.0.0.0:9000->9000/tcp, [::]:9000->9000/tcp, 8000/tcp, 0.0.0.0:9443->9443/tcp, [::]:9443->9443/tcp |

**Running:** 21 containers

## Cron Jobs

```cron
0 * * * * /usr/local/bin/resource-trend-logger.sh >> /var/log/resource-trends.log 2>&1
0 3 * * * ROUNDUP_CRON_MODE=true /root/.config/opencode/skills/roundup/scripts/cron-executor.sh --quiet >> /root/cron-logs/roundup-cron.log 2>&1
```

## Backup Status

No backup directory found

Latest backup log: backup-freshstart-20260224.log

## Skills Updated (Last 48h)

- **olivetin** - 2026-02-27 01:33:54
- **skill-blueprint** - 2026-02-27 02:50:32
- **containers** - 2026-02-27 02:42:56
- **astro** - 2026-02-27 02:48:05
- **menu-system** - 2026-02-27 03:10:22
- **research** - 2026-02-27 02:48:33
- **homepage** - 2026-02-27 00:06:14
- **cron** - 2026-02-27 04:59:04
- **opentelemetry** - 2026-02-26 22:23:13
- **flow** - 2026-02-27 02:52:06
- **context-registry** - 2026-02-27 02:44:00
- **roundup** - 2026-02-27 02:11:55
- **performance** - 2026-02-27 02:44:42
- **skill-discovery** - 2026-02-27 03:06:10

## Triggers Updated (Last 48h)

- **roundup** - 2026-02-27 02:16:37
- **skill-discovery** - 2026-02-27 03:37:34
- **olivetin** - 2026-02-27 01:36:17
- **menu** - 2026-02-27 03:11:38
- **README** - 2026-02-27 01:55:37

## Freshstart Repository Sync

Repository status:
```
 D .config/opencode/skills/homarr/SKILL.md
 D skills/homarr/SKILL.md
?? .config/opencode/docs/instructions/triggers/roundup.md
?? .config/opencode/skills/roundup/
```

⚠️ **4 uncommitted changes**

## Error Summary

### System Errors: 129

```
Feb 27 09:06:57 ubuntu4 kernel: I/O error, dev fd0, sector 0 op 0x0:(READ) flags 0x0 phys_seg 1 prio class 2
Feb 27 09:06:57 ubuntu4 kernel: I/O error, dev fd0, sector 0 op 0x0:(READ) flags 0x0 phys_seg 1 prio class 2
Feb 27 09:06:58 ubuntu4 kernel: piix4_smbus 0000:00:07.3: SMBus base address uninitialized - upgrade BIOS or use force_addr=0xaddr
Feb 27 09:06:59 ubuntu4 kernel: I/O error, dev fd0, sector 0 op 0x0:(READ) flags 0x0 phys_seg 1 prio class 2
Feb 27 09:06:59 ubuntu4 kernel: I/O error, dev fd0, sector 0 op 0x0:(READ) flags 0x0 phys_seg 1 prio class 2
Feb 27 09:06:59 ubuntu4 kernel: I/O error, dev fd0, sector 0 op 0x0:(READ) flags 0x0 phys_seg 1 prio class 2
Feb 27 09:07:00 ubuntu4 kernel: I/O error, dev fd0, sector 0 op 0x0:(READ) flags 0x0 phys_seg 1 prio class 2
Feb 27 09:07:00 ubuntu4 kernel: I/O error, dev fd0, sector 0 op 0x0:(READ) flags 0x0 phys_seg 1 prio class 2
Feb 27 09:07:05 ubuntu4 systemd[1]: Failed to mount mnt-backup.mount - /mnt/backup.
Feb 27 09:07:05 ubuntu4 systemd[1]: Failed to mount mnt-smb\x2doutput.mount - /mnt/smb-output.
```

### Container Errors

- **olivetin**: 2 errors
- **freshrss**: 13 errors
- **hugo**: 1 errors
- **node-exporter**: 4 errors

## Recommendations

4. ⚠️ **Backup is 999 days old** - Verify backup system

---

*Generated by [Roundup Skill](/skills/roundup) at 2026-02-27T14:44:31+00:00*
[2026-02-27T14:44:31+00:00] Report generated: /root/cron-logs/roundup-2026-02-27.log
[2026-02-27T14:44:31+00:00] History recorded
[2026-02-27T14:44:31+00:00] Publishing to blog...