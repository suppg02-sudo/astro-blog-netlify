---
pubDatetime: 2026-04-08T04:39:13Z
title: "Ecosystem Analysis Report — 2026-04-08 04:39"
postSlug: "ecosystem-analysis-report-2026"
description: "Ecosystem Analysis Report — 2026-04-08 04:39"
tags:
  - "064e3b"
  - "065f46"
  - "1e293b"
  - "0f172a"
  - "16a34a"
---

Automated ecosystem analysis. 4 scanners ran, 244 objects analyzed, 363 issues found.

**Tags**: ecosystem-analysis, automated-report, infrastructure
**Categories**: Infrastructure, Reports

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

> **TL;DR**: Automated ecosystem analysis across all object types. 4 scanners ran, 244 objects analyzed, 363 issues found.


<style>
.eco-action-bar {
  display: flex; flex-wrap: wrap; gap: 8px; align-items: flex-start;
  padding: 12px 16px; margin: 16px 0; border-radius: 8px;
  background: #f8f9fa; border: 1px solid #e2e8f0;
}
[data-theme="dark"] .eco-action-bar { background: #1e293b; border-color: #334155; }
.eco-action-group { flex: 1 1 200px; min-width: 200px; }
.eco-group-label {
  color: #475569; font-size: 12px; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.5px; margin-bottom: 6px; padding: 0 2px;
}
[data-theme="dark"] .eco-group-label { color: #94a3b8; }
.eco-action-btn {
  display: flex; align-items: center; gap: 6px; width: 100%; padding: 6px 10px;
  border-radius: 6px; border: 1px solid #cbd5e1; background: #fff;
  color: #1e293b; font-size: 12px; font-weight: 500; cursor: pointer;
  text-decoration: none; white-space: nowrap; transition: all 0.15s;
}
[data-theme="dark"] .eco-action-btn { background: #0f172a; border-color: #475569; color: #e2e8f0; }
.eco-action-btn:hover { border-color: #94a3b8; background: #f1f5f9; }
[data-theme="dark"] .eco-action-btn:hover { border-color: #64748b; background: #1e293b; }
.eco-action-btn-running { opacity: 0.6; cursor: not-allowed; pointer-events: none; }
.eco-action-btn-running .eco-spinner { display: inline !important; }
.eco-spinner { display: none; margin-left: 4px; }
.eco-action-detail {
  margin: 2px 0 0 0; padding: 6px 8px; border-radius: 4px;
  background: #eef2ff; border: 1px solid #c7d2fe; font-size: 11px; color: #4b5563;
  display: none;
}
[data-theme="dark"] .eco-action-detail { background: rgb(30, 27, 59); border-color: #334155; color: #cbd5e1; }
.eco-action-detail summary { cursor: pointer; font-weight: 500; padding: 2px 0; }
.eco-action-detail summary::marker { color: #6366f1; }
.eco-action-meta { margin: 4px 0 0 4px; font-size: 10px; color: #6b7280; }
[data-theme="dark"] .eco-action-meta { color: #94a3b8; }
.eco-action-meta::before { content: "→ "; color: #9ca3af; }
.eco-status {
  width: 100%; margin-top: 8px; padding: 8px 12px; border-radius: 6px;
  font-size: 11px; display: none; text-align: left;
}
.eco-status-success { background: #ecfdf5; border: 1px solid #bbf7d0; color: #065f46; }
.eco-status-error { background: #fef2f2; border: 1px solid #fecaca; color: #991b1b; }
[data-theme="dark"] .eco-status-success { background: #064e3b; border-color: #065f46; color: #86efac; }
[data-theme="dark"] .eco-status-error { background: #450a0a; border-color: #991b1b; color: #fca5a5; }
</style>


<script>
window._runAction = function(btn) {
  if (btn.classList.contains('eco-action-btn-running')) return;
  var container = btn.closest('.eco-action-bar');
  var status = container.querySelector('.eco-status');
  if (!container || !status) return;
  var actions = JSON.parse(container.getAttribute('data-actions').replace(/&quot;/g, '"'));
  var id = btn.getAttribute('data-action');
  var action = actions[id];
  if (!action) return;
  btn.classList.add('eco-action-btn-running');
  status.style.display = 'none';
  fetch('http://ubuntu4:8057/actions/' + id + '/execute', {
    method: 'POST', headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({action_id: id})
  })
  .then(function(r) { return r.json(); })
  .then(function(data) {
    btn.classList.remove('eco-action-btn-running');
    status.style.display = 'block';
    if (data.status === 'completed') {
      status.className = 'eco-status eco-status-success';
      var out = data.output ? data.output.substring(0, 300) : '';
      status.innerHTML = '✅ <b>' + action.icon + ' ' + action.label + '</b> completed in ' + (data.duration_ms||0) + 'ms' +
        (out ? '<pre style="margin:4px 0 0;max-height:60px;overflow:auto;font-size:10px;white-space:pre-wrap;line-height:1.4">' + out.replace(/</g,'&lt;') + '</pre>' : '');
    } else {
      status.className = 'eco-status eco-status-error';
      status.innerHTML = '❌ <b>' + action.icon + ' ' + action.label + '</b> failed: ' + (data.error || 'Unknown');
    }
  })
  .catch(function(e) {
    btn.classList.remove('eco-action-btn-running');
    status.style.display = 'block';
    status.className = 'eco-status eco-status-error';
    status.innerHTML = '❌ Network error: ' + e.message;
  });
};
</script>

<div class="eco-action-bar" data-actions="{&quot;ecosystem-full-scan&quot;: {&quot;action_id&quot;: &quot;ecosystem-full-scan&quot;, &quot;icon&quot;: &quot;\ud83d\udd2c&quot;, &quot;label&quot;: &quot;Full Scan&quot;, &quot;description&quot;: &quot;Runs all four analyzers (schemas, skills, menus, agents), saves the unified registry to /data/registry/, appends to the scan history log, publishes a new blog report with action buttons, and captures deferred options for each issue found.&quot;, &quot;files_affected&quot;: &quot;Entire ecosystem \u2014 all analyzers run&quot;, &quot;safe&quot;: true}, &quot;menu-compliance-fix&quot;: {&quot;action_id&quot;: &quot;menu-compliance-fix&quot;, &quot;icon&quot;: &quot;\ud83d\udccb&quot;, &quot;label&quot;: &quot;Fix Menus&quot;, &quot;description&quot;: &quot;Runs the menus analyzer to check option counts, progressive disclosure, defer/toggle presence, and signal tracking. Returns a compliance report with specific issues.&quot;, &quot;files_affected&quot;: &quot;Reads all SKILL.md files with menu configurations&quot;, &quot;safe&quot;: true}, &quot;schema-add-changelogs&quot;: {&quot;action_id&quot;: &quot;schema-add-changelogs&quot;, &quot;icon&quot;: &quot;\ud83d\udcdd&quot;, &quot;label&quot;: &quot;Add Changelogs&quot;, &quot;description&quot;: &quot;Scans all schema YAML files for missing $changelog headers and adds a standard creation entry to each. This raises the freshness score and ensures every schema has a version history.&quot;, &quot;files_affected&quot;: &quot;All .yaml files in /schemas/&quot;, &quot;safe&quot;: true}, &quot;schema-fix-overlaps&quot;: {&quot;action_id&quot;: &quot;schema-fix-overlaps&quot;, &quot;icon&quot;: &quot;\ud83d\udd17&quot;, &quot;label&quot;: &quot;Fix Overlaps&quot;, &quot;description&quot;: &quot;Adds $extends: base-entity to schemas that share significant fields with base-entity but don't yet declare the inheritance. This enables composition and reduces the overlap score.&quot;, &quot;files_affected&quot;: &quot;mixin-*.yaml, experiment-schema.yaml, research-task-schema.yaml, task-schema.yaml&quot;, &quot;safe&quot;: false}, &quot;schema-scan-and-report&quot;: {&quot;action_id&quot;: &quot;schema-scan-and-report&quot;, &quot;icon&quot;: &quot;\ud83d\udd0d&quot;, &quot;label&quot;: &quot;Re-scan&quot;, &quot;description&quot;: &quot;Runs the full schema scanner: parses all schemas, calculates health scores, detects overlap and issues, updates $analysis blocks in each file, and regenerates the registry.&quot;, &quot;files_affected&quot;: &quot;Reads all schemas, writes $analysis blocks and schema-registry.yaml&quot;, &quot;safe&quot;: true}, &quot;skills-add-context&quot;: {&quot;action_id&quot;: &quot;skills-add-context&quot;, &quot;icon&quot;: &quot;\ud83d\udcc2&quot;, &quot;label&quot;: &quot;Add Context&quot;, &quot;description&quot;: &quot;Creates context/ directories for any skill that lacks one, with an empty metadata.json file. This makes those skills participate in the analysis framework.&quot;, &quot;files_affected&quot;: &quot;All skills in /skills/ without a context/ directory&quot;, &quot;safe&quot;: true}}">
<div class="eco-action-group">
<button class="eco-action-btn" data-action="ecosystem-full-scan" onclick="window._runAction(this)">
<span>🔬</span> <span>Full Scan</span> <span class="eco-spinner">⏳</span>
</button>
<details class="eco-action-detail">
<summary>What does this do?</summary>
<p style="margin:4px 0 0 8px">Runs all four analyzers (schemas, skills, menus, agents), saves the unified registry to /data/registry/, appends to the scan history log, publishes a new blog report with action buttons, and captures deferred options for each issue found.</p>
<div class="eco-action-meta">Affects: Entire ecosystem — all analyzers run</div>
<div class="eco-action-meta">Safety: ✅ Safe</div>
</details>
</div>
<div class="eco-action-group">
<button class="eco-action-btn" data-action="menu-compliance-fix" onclick="window._runAction(this)">
<span>📋</span> <span>Fix Menus</span> <span class="eco-spinner">⏳</span>
</button>
<details class="eco-action-detail">
<summary>What does this do?</summary>
<p style="margin:4px 0 0 8px">Runs the menus analyzer to check option counts, progressive disclosure, defer/toggle presence, and signal tracking. Returns a compliance report with specific issues.</p>
<div class="eco-action-meta">Affects: Reads all SKILL.md files with menu configurations</div>
<div class="eco-action-meta">Safety: ✅ Safe</div>
</details>
</div>
<div class="eco-action-group">
<button class="eco-action-btn" data-action="schema-add-changelogs" onclick="window._runAction(this)">
<span>📝</span> <span>Add Changelogs</span> <span class="eco-spinner">⏳</span>
</button>
<details class="eco-action-detail">
<summary>What does this do?</summary>
<p style="margin:4px 0 0 8px">Scans all schema YAML files for missing $changelog headers and adds a standard creation entry to each. This raises the freshness score and ensures every schema has a version history.</p>
<div class="eco-action-meta">Affects: All .yaml files in /schemas/</div>
<div class="eco-action-meta">Safety: ✅ Safe</div>
</details>
</div>
<div class="eco-action-group">
<button class="eco-action-btn" data-action="schema-fix-overlaps" onclick="window._runAction(this)">
<span>🔗</span> <span>Fix Overlaps</span> <span class="eco-spinner">⏳</span>
</button>
<details class="eco-action-detail">
<summary>What does this do?</summary>
<p style="margin:4px 0 0 8px">Adds $extends: base-entity to schemas that share significant fields with base-entity but don't yet declare the inheritance. This enables composition and reduces the overlap score.</p>
<div class="eco-action-meta">Affects: mixin-*.yaml, experiment-schema.yaml, research-task-schema.yaml, task-schema.yaml</div>
<div class="eco-action-meta">Safety: ⚠️ Modifies files</div>
</details>
</div>
<div class="eco-action-group">
<button class="eco-action-btn" data-action="schema-scan-and-report" onclick="window._runAction(this)">
<span>🔍</span> <span>Re-scan</span> <span class="eco-spinner">⏳</span>
</button>
<details class="eco-action-detail">
<summary>What does this do?</summary>
<p style="margin:4px 0 0 8px">Runs the full schema scanner: parses all schemas, calculates health scores, detects overlap and issues, updates $analysis blocks in each file, and regenerates the registry.</p>
<div class="eco-action-meta">Affects: Reads all schemas, writes $analysis blocks and schema-registry.yaml</div>
<div class="eco-action-meta">Safety: ✅ Safe</div>
</details>
</div>
<div class="eco-action-group">
<button class="eco-action-btn" data-action="skills-add-context" onclick="window._runAction(this)">
<span>📂</span> <span>Add Context</span> <span class="eco-spinner">⏳</span>
</button>
<details class="eco-action-detail">
<summary>What does this do?</summary>
<p style="margin:4px 0 0 8px">Creates context/ directories for any skill that lacks one, with an empty metadata.json file. This makes those skills participate in the analysis framework.</p>
<div class="eco-action-meta">Affects: All skills in /skills/ without a context/ directory</div>
<div class="eco-action-meta">Safety: ✅ Safe</div>
</details>
</div>
<div class="eco-status"></div>
</div>
## Summary

<div class="summary-grid">
<div class="summary-card sc-blue"><div class="sc-val">🔍 4</div><div class="sc-label">Scanners</div></div>
<div class="summary-card sc-green"><div class="sc-val">📦 244</div><div class="sc-label">Objects</div></div>
<div class="summary-card sc-amber"><div class="sc-val">⚠️ 363</div><div class="sc-label">Issues</div></div>
<div class="summary-card sc-blue"><div class="sc-val">📊 73.0</div><div class="sc-label">Health</div></div>
</div>

## Analysis Results by Type

| Type | Objects | Issues | Health | Status |
|------|---------|--------|--------|--------|
| menus | 90 | 187 | 82.5 | ✅ |
| schemas | 14 | 13 | 87.2 | ✅ |
| skills | 122 | 134 | 65.1 | ⚠️ |
| agents | 18 | 29 | 57.2 | 🔴 |

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
<summary>📋 schemas — 87/100</summary>
<div class="sev-body">

**Issues (13):**

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


<details class="sev-section sev-warning" open>
<summary>📋 skills — 65/100</summary>
<div class="sev-body">

**Issues (134):**

- WARNING: No context directory
- WARNING: Very short skill description (<200 words)
- WARNING: Very short skill description (<200 words)
- WARNING: No context directory
- WARNING: Very short skill description (<200 words)

</div>
</details>


<details class="sev-section sev-critical" open>
<summary>📋 agents — 57/100</summary>
<div class="sev-body">

**Issues (29):**

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
| 2026-04-08 | schemas | 14 | 13 | 87.2 | h |
| 2026-04-08 | skills | 122 | 134 | 65.08196721311475 | d |
| 2026-04-08 | agents | 18 | 29 | 57.22222222222222 | c |

---

*This report was automatically generated by the ecosystem scanner.*