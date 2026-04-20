---
pubDatetime: 2026-04-08T03:58:36Z
title: "Ecosystem Analysis Report — 2026-04-08"
postSlug: "ecosystem-report-2026-04-08T0358"
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


<script>
window._runAction = function(btn) {
  var bar = btn.closest('.eco-action-bar');
  var status = document.getElementById('eco-status');
  if (!bar || !status || btn.classList.contains('running')) return;
  var actions = JSON.parse(bar.getAttribute('data-actions').replace(/&quot;/g, '"'));
  var action = actions[btn.getAttribute('data-action')];
  if (!action) return;
  btn.classList.add('running');
  status.style.display = 'none';
  fetch('http://ubuntu4:8057/actions/' + action.action_id + '/execute', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({action_id: action.action_id})
  })
  .then(function(r) { return r.json(); })
  .then(function(data) {
    btn.classList.remove('running');
    status.style.display = 'block';
    if (data.status === 'completed') {
      status.className = 'eco-status success';
      var out = data.output ? data.output.substring(0, 200) : '';
      status.innerHTML = '✅ ' + action.icon + ' ' + action.label + ' in ' + (data.duration_ms||0) + 'ms' +
        (out ? '<br><code style="font-size:10px">' + out.replace(/</g,'&lt;') + '</code>' : '');
    } else {
      status.className = 'eco-status error';
      status.innerHTML = '❌ ' + action.icon + ' ' + action.label + ' failed: ' + (data.error || 'Unknown');
    }
  })
  .catch(function(e) {
    btn.classList.remove('running');
    status.style.display = 'block';
    status.className = 'eco-status error';
    status.innerHTML = '❌ Network: ' + e.message;
  });
};
</script>

<style>
.eco-action-bar { display: flex; flex-wrap: wrap; gap: 10px; align-items: center; justify-content: center; padding: 16px 20px; margin: 20px 0; border-radius: 12px; background: #0a0020; border: 1px solid #1a1a3a; }
.eco-action-label { color: #888; font-size: 12px; font-weight: 700; text-transform: uppercase; letter-spacing: 1.5px; margin-right: 8px; }
.eco-action-btn { display: inline-flex; align-items: center; gap: 6px; padding: 8px 16px; border-radius: 8px; border: 1px solid var(--c); background: rgba(255,255,255,0.05); color: var(--c); font-size: 13px; font-weight: 600; cursor: pointer; text-decoration: none; white-space: nowrap; }
.eco-action-btn:hover { background: var(--c); color: #0a0020; transform: translateY(-1px); box-shadow: 0 4px 16px rgba(255,255,255,0.1); }
.eco-action-btn.running { opacity: 0.6; cursor: not-allowed; }
.eco-action-btn .spinner { display: none; margin-left: 4px; }
.eco-action-btn.running .spinner { display: inline; }
.eco-status { width: 100%; margin-top: 10px; padding: 10px 14px; border-radius: 8px; font-size: 12px; text-align: center; }
.eco-status.success { background: rgba(34,197,94,0.15); border: 1px solid #22c55e; color: #22c55e; }
.eco-status.error { background: rgba(239,68,68,0.15); border: 1px solid #ef4444; color: #ef4444; }
</style>
<div class="eco-action-bar" data-actions="{&quot;ecosystem-full-scan&quot;: {&quot;action_id&quot;: &quot;ecosystem-full-scan&quot;, &quot;icon&quot;: &quot;\ud83d\udd2c&quot;, &quot;label&quot;: &quot;Full Scan&quot;, &quot;color&quot;: &quot;#ff00ff&quot;}, &quot;skills-add-context&quot;: {&quot;action_id&quot;: &quot;skills-add-context&quot;, &quot;icon&quot;: &quot;\ud83d\udcc2&quot;, &quot;label&quot;: &quot;Add Context&quot;, &quot;color&quot;: &quot;#00ff41&quot;}, &quot;menu-compliance-fix&quot;: {&quot;action_id&quot;: &quot;menu-compliance-fix&quot;, &quot;icon&quot;: &quot;\ud83d\udccb&quot;, &quot;label&quot;: &quot;Fix Menus&quot;, &quot;color&quot;: &quot;#ff4081&quot;}, &quot;schema-add-changelogs&quot;: {&quot;action_id&quot;: &quot;schema-add-changelogs&quot;, &quot;icon&quot;: &quot;\ud83d\udcdd&quot;, &quot;label&quot;: &quot;Add Changelogs&quot;, &quot;color&quot;: &quot;#ffab00&quot;}, &quot;schema-fix-overlaps&quot;: {&quot;action_id&quot;: &quot;schema-fix-overlaps&quot;, &quot;icon&quot;: &quot;\ud83d\udd17&quot;, &quot;label&quot;: &quot;Fix Overlaps&quot;, &quot;color&quot;: &quot;#7c3aed&quot;}, &quot;schema-scan-and-report&quot;: {&quot;action_id&quot;: &quot;schema-scan-and-report&quot;, &quot;icon&quot;: &quot;\ud83d\udd0d&quot;, &quot;label&quot;: &quot;Re-scan&quot;, &quot;color&quot;: &quot;#00ffff&quot;}}">
<span class="eco-action-label">⚡ Quick Actions</span>
<a class="eco-action-btn" data-action="ecosystem-full-scan" style="--c: #ff00ff; color: #ff00ff; border-color: #ff00ff;" onclick="window._runAction(this)">
<span>🔬</span> <span>Full Scan</span> <span class="spinner">⏳</span>
</a>
<a class="eco-action-btn" data-action="skills-add-context" style="--c: #00ff41; color: #00ff41; border-color: #00ff41;" onclick="window._runAction(this)">
<span>📂</span> <span>Add Context</span> <span class="spinner">⏳</span>
</a>
<a class="eco-action-btn" data-action="menu-compliance-fix" style="--c: #ff4081; color: #ff4081; border-color: #ff4081;" onclick="window._runAction(this)">
<span>📋</span> <span>Fix Menus</span> <span class="spinner">⏳</span>
</a>
<a class="eco-action-btn" data-action="schema-add-changelogs" style="--c: #ffab00; color: #ffab00; border-color: #ffab00;" onclick="window._runAction(this)">
<span>📝</span> <span>Add Changelogs</span> <span class="spinner">⏳</span>
</a>
<a class="eco-action-btn" data-action="schema-fix-overlaps" style="--c: #7c3aed; color: #7c3aed; border-color: #7c3aed;" onclick="window._runAction(this)">
<span>🔗</span> <span>Fix Overlaps</span> <span class="spinner">⏳</span>
</a>
<a class="eco-action-btn" data-action="schema-scan-and-report" style="--c: #00ffff; color: #00ffff; border-color: #00ffff;" onclick="window._runAction(this)">
<span>🔍</span> <span>Re-scan</span> <span class="spinner">⏳</span>
</a>
<div class="eco-status" id="eco-status" style="display:none;"></div>
</div>
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
