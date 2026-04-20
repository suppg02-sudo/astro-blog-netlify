---
pubDatetime: 2026-04-08T03:49:09Z
title: "Ecosystem Analysis Report — 2026-04-08"
postSlug: "ecosystem-report-2026-04-08T0349"
description: "Ecosystem Analysis Report — 2026-04-08"
tags:
  - automated-report
  - ecosystem-analysis
---

<style>
.sev-section { border-radius: 6px; margin: 1.2rem 0; overflow: hidden; border: 1px solid; }
.sev-critical { border-color: #ef4444; background: rgba(239,68,68,0.04); }
.sev-critical > summary { background: rgba(239,68,68,0.12); color: #dc2626; }
.sev-warning { border-color: #f59e0b; background: rgba(245,158,11,0.04); }
.sev-warning > summary { background: rgba(245,158,11,0.12); color: #b45309; }
.sev-positive { border-color: #22c55e; background: rgba(34,197,94,0.04); }
.sev-positive > summary { background: rgba(34,197,94,0.12); color: #16a34a; }
.sev-neutral { border-color: #6b7280; background: rgba(107,114,128,0.04); }
.sev-neutral > summary { background: rgba(107,114,128,0.08); color: #4b5563; }
.sev-section > summary { padding: 0.6rem 1rem; font-weight: 600; cursor: pointer; display: flex; align-items: center; gap: 0.5rem; list-style: none; }
.sev-section > summary::-webkit-details-marker { display: none; }
.sev-section > summary::before { content: '▶'; font-size: 0.75rem; transition: transform 0.15s; }
.sev-section[open] > summary::before { transform: rotate(90deg); }
.sev-body { padding: 0.8rem 1rem; }
.summary-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px,1fr)); gap: 0.6rem; margin: 0.5rem 0; }
.summary-card { border-radius: 6px; padding: 0.6rem 0.8rem; text-align: center; }
.summary-card .sc-val { font-size: 1.4em; font-weight: 700; }
.summary-card .sc-label { font-size: 0.75em; opacity: 0.7; margin-top: 0.15rem; }
.sc-red { background: rgba(239,68,68,0.1); color: #dc2626; }
.sc-amber { background: rgba(245,158,11,0.1); color: #b45309; }
.sc-green { background: rgba(34,197,94,0.1); color: #16a34a; }
.sc-blue { background: rgba(59,130,246,0.1); color: #2563eb; }
</style>

> **TL;DR**: Automated ecosystem analysis across all object types. 4 scanners ran, 251 objects analyzed, 411 issues found.


<!-- Action Buttons -->
<script>
  window.ECOSYSTEM_ACTIONS = {"schema-add-changelogs": {"action_id": "schema-add-changelogs", "icon": "\ud83d\udcdd", "label": "Add Changelogs", "color": "#ffab00"}, "schema-fix-overlaps": {"action_id": "schema-fix-overlaps", "icon": "\ud83d\udd17", "label": "Fix Overlaps", "color": "#7c3aed"}, "schema-scan-and-report": {"action_id": "schema-scan-and-report", "icon": "\ud83d\udd0d", "label": "Re-scan Schemas", "color": "#00ffff"}, "skills-add-context": {"action_id": "skills-add-context", "icon": "\ud83d\udcc2", "label": "Add Context Dirs", "color": "#00ff41"}, "menu-compliance-fix": {"action_id": "menu-compliance-fix", "icon": "\ud83d\udccb", "label": "Fix Menu Compliance", "color": "#ff4081"}, "ecosystem-full-scan": {"action_id": "ecosystem-full-scan", "icon": "\ud83d\udd2c", "label": "Full Ecosystem Scan", "color": "#ff00ff"}};
  window.ECOSYSTEM_API = 'http://ubuntu4:8057/actions';
</script>
<style>
.action-bar {
  display: flex; flex-wrap: wrap; gap: 10px; align-items: center;
  padding: 16px 20px; margin: 20px 0; border-radius: 10px;
  background: #0a0030; border: 1px solid #1a1a3a;
}
.action-label {
  color: #666; font-size: 12px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 1px; margin-right: 8px;
}
.action-btn {
  display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px;
  border-radius: 8px; border: 1px solid var(--btn-color); background: rgba(var(--btn-rgb), 0.1);
  color: var(--btn-color); font-size: 13px; font-weight: 600; cursor: pointer;
  transition: all 0.2s; user-select: none; text-decoration: none;
}
.action-btn:hover { background: rgba(var(--btn-rgb), 0.2); transform: translateY(-1px); box-shadow: 0 4px 12px rgba(var(--btn-rgb), 0.2); }
.action-btn:active { transform: translateY(0); }
.action-btn.running { opacity: 0.7; cursor: not-allowed; }
.action-btn.running .btn-spinner { display: inline-block; }
.btn-icon { font-size: 14px; }
.btn-label { white-space: nowrap; }
.btn-eta { font-size: 10px; opacity: 0.6; margin-left: 4px; }
.btn-spinner { display: none; animation: spin 1s linear infinite; }
@keyframes spin { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
.action-status { width: 100%; margin-top: 12px; padding: 10px 14px; border-radius: 8px; font-size: 12px; display: none; }
.action-status.success { background: rgba(34,197,94,0.1); border: 1px solid #22c55e; color: #22c55e; }
.action-status.error { background: rgba(239,68,68,0.1); border: 1px solid #ef4444; color: #ef4444; }
</style>
<div class="action-bar">
  <span class="action-label">⚡ Quick Actions:</span>
  <button class="action-btn" id="btn-schema-add-changelogs" onclick="executeAction('schema-add-changelogs')" style="--btn-color: #ffab00; --btn-rgb: 255,171,0;">
    <span class="btn-icon">📝</span>
    <span class="btn-label">Add Changelogs</span>
    <span class="btn-spinner">⏳</span>
  </button>
  <button class="action-btn" id="btn-schema-fix-overlaps" onclick="executeAction('schema-fix-overlaps')" style="--btn-color: #7c3aed; --btn-rgb: 124,58,237;">
    <span class="btn-icon">🔗</span>
    <span class="btn-label">Fix Overlaps</span>
    <span class="btn-spinner">⏳</span>
  </button>
  <button class="action-btn" id="btn-schema-scan-and-report" onclick="executeAction('schema-scan-and-report')" style="--btn-color: #00ffff; --btn-rgb: 0,255,255;">
    <span class="btn-icon">🔍</span>
    <span class="btn-label">Re-scan Schemas</span>
    <span class="btn-spinner">⏳</span>
  </button>
  <button class="action-btn" id="btn-skills-add-context" onclick="executeAction('skills-add-context')" style="--btn-color: #00ff41; --btn-rgb: 0,255,65;">
    <span class="btn-icon">📂</span>
    <span class="btn-label">Add Context Dirs</span>
    <span class="btn-spinner">⏳</span>
  </button>
  <button class="action-btn" id="btn-menu-compliance-fix" onclick="executeAction('menu-compliance-fix')" style="--btn-color: #ff4081; --btn-rgb: 255,64,129;">
    <span class="btn-icon">📋</span>
    <span class="btn-label">Fix Menu Compliance</span>
    <span class="btn-spinner">⏳</span>
  </button>
  <button class="action-btn" id="btn-ecosystem-full-scan" onclick="executeAction('ecosystem-full-scan')" style="--btn-color: #ff00ff; --btn-rgb: 255,0,255;">
    <span class="btn-icon">🔬</span>
    <span class="btn-label">Full Ecosystem Scan</span>
    <span class="btn-spinner">⏳</span>
  </button>
  <div class="action-status" id="action-status"></div>
</div>

<script>
async function executeAction(actionId) {
  const btn = document.getElementById('btn-' + actionId);
  const status = document.getElementById('action-status');
  const action = window.ECOSYSTEM_ACTIONS[actionId];
  if (!action || btn.classList.contains('running')) return;

  btn.classList.add('running');
  btn.querySelector('.btn-spinner').style.display = 'inline-block';
  status.style.display = 'none';

  try {
    const resp = await fetch(window.ECOSYSTEM_API + '/' + actionId + '/execute', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({action_id: actionId})
    });
    const data = await resp.json();

    if (data.status === 'completed') {
      status.className = 'action-status success';
      status.innerHTML = '✅ ' + action.icon + ' ' + action.label + ' completed in ' + data.duration_ms + 'ms' + (data.output ? '<pre style="margin:8px 0;max-height:20px;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:11px">' + data.output.substring(0,200) + '</pre>' : '');
    } else {
      status.className = 'action-status error';
      status.innerHTML = '❌ ' + action.icon + ' ' + action.label + ' failed: ' + (data.error || 'Unknown error');
    }
    status.style.display = 'block';
  } catch (e) {
    status.className = 'action-status error';
    status.innerHTML = '❌ Network error: ' + e.message;
    status.style.display = 'block';
  } finally {
    btn.classList.remove('running');
    btn.querySelector('.btn-spinner').style.display = 'none';
  }
}
</script>

## Summary

<div class="summary-grid">
<div class="summary-card sc-blue"><div class="sc-val">🔍 4</div><div class="sc-label">Scanners</div></div>
<div class="summary-card sc-green"><div class="sc-val">📦 251</div><div class="sc-label">Objects</div></div>
<div class="summary-card sc-amber"><div class="sc-val">⚠️ 411</div><div class="sc-label">Issues</div></div>
<div class="summary-card sc-blue"><div class="sc-val">📊 69.4</div><div class="sc-label">Health</div></div>
</div>

## Analysis Results by Type

| Type | Objects | Issues | Health | Status |
|------|---------|--------|--------|--------|
| menus | 90 | 187 | 82.5 | ✅ |
| schemas | 19 | 18 | 83.5 | ✅ |
| skills | 122 | 174 | 55.2 | 🔴 |
| agents | 20 | 32 | 56.5 | 🔴 |

<details class="sev-section sev-positive" >
<summary>📋 menus — 82/100</summary>
<div class="sev-body">

**Issues (187):**

- WARNING: No options detected despite menu presence
- INFO: No defer option — consider adding
- INFO: No mobile/desktop toggle detected
- WARNING: No options detected despite menu presence
- INFO: No defer option — consider adding

</div>
</details>


<details class="sev-section sev-positive" >
<summary>📋 schemas — 84/100</summary>
<div class="sev-body">

**Issues (18):**

- INFO: No changelog entries. Version history unknown.
- INFO: No changelog entries. Version history unknown.
- INFO: No changelog entries. Version history unknown.
- INFO: No changelog entries. Version history unknown.
- INFO: No changelog entries. Version history unknown.

**Recommendations:**

- HIGH: Adopt base-entity inheritance for entity schemas
- MEDIUM: Add changelog entries to all schemas

</div>
</details>


<details class="sev-section sev-critical" open>
<summary>📋 skills — 55/100</summary>
<div class="sev-body">

**Issues (174):**

- WARNING: No context directory
- WARNING: Very short skill description (<200 words)
- WARNING: Very short skill description (<200 words)
- WARNING: No context directory
- WARNING: Very short skill description (<200 words)

</div>
</details>


<details class="sev-section sev-critical" open>
<summary>📋 agents — 56/100</summary>
<div class="sev-body">

**Issues (32):**

- WARNING: No tools defined
- INFO: No workflow definitions
- WARNING: No tools defined
- INFO: No model configuration
- WARNING: No tools defined

</div>
</details>

## Scan History

| Date | Scanner | Objects | Issues | Health |
|------|---------|---------|--------|--------|
| 2026-04-08 | menus | 90 | 187 | 82.5 | h |
| 2026-04-08 | schemas | 19 | 18 | 83.5 | h |
| 2026-04-08 | skills | 122 | 174 | 55.24590163934426 | c |
| 2026-04-08 | agents | 20 | 32 | 56.5 | c |
| 2026-04-08 | menus | 90 | 187 | 82.5 | h |
| 2026-04-08 | schemas | 19 | 18 | 83.5 | h |
| 2026-04-08 | skills | 122 | 174 | 55.24590163934426 | c |
| 2026-04-08 | agents | 20 | 32 | 56.5 | c |

---

*This report was automatically generated by the ecosystem scanner.*
