---
pubDatetime: 2026-04-01T18:00:00Z
title: "SVG Rendering Test: Can Astro Handle Inline SVGs?"
postSlug: "svg-rendering-test"
description: "Testing whether inline SVG diagrams render correctly in the Astro blog theme, including flowcharts, structural diagrams, and dark mode support."
tags:
  - test
  - svg
  - diagrams
---

# SVG Rendering Test: Can Astro Handle Inline SVGs?

This post tests three approaches to embedding SVG in Astro blog posts to see what actually renders.

## Test 1: Inline SVG in a code block (XML)

This is what the SVG skill generates by default — raw SVG in a code block. It should display as **code**, not a rendered diagram.

```xml
<svg width="200" height="100" viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="180" height="80" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="1"/>
  <text x="100" y="55" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#3d3d3a">Code block SVG</text>
</svg>
```

## Test 2: Inline SVG as raw HTML

If the markdown renderer supports raw HTML, this should render as an **actual blue box with text**.

<svg width="200" height="100" viewBox="0 0 200 100" xmlns="http://www.w3.org/2000/svg">
  <rect x="10" y="10" width="180" height="80" rx="10" fill="#E6F1FB" stroke="#378ADD" stroke-width="1"/>
  <text x="100" y="55" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#3d3d3a">Raw HTML SVG</text>
</svg>

## Test 3: Flowchart via inline SVG

A simple deployment pipeline rendered as SVG.

<svg width="100%" viewBox="0 0 640 120" xmlns="http://www.w3.org/2000/svg">
<style>.th{font:500 13px/1.3 sans-serif;fill:#3d3d3a}.ts{font:400 11px/1.3 sans-serif;fill:#888780}.box{stroke-width:.5;rx:8}.arr{fill:none;stroke:#888780;stroke-width:1.5;marker-end:url(#a)}</style>
<defs><marker id="a" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#888780"/></marker></defs>
<rect class="box" x="20" y="30" width="100" height="55" fill="#E6F1FB" stroke="#378ADD"/>
<text class="th" x="70" y="55" text-anchor="middle">Commit</text>
<text class="ts" x="70" y="72" text-anchor="middle">git push</text>
<line class="arr" x1="120" y1="57" x2="145" y2="57"/>
<rect class="box" x="145" y="30" width="100" height="55" fill="#EEEDFE" stroke="#7F77DD"/>
<text class="th" x="195" y="55" text-anchor="middle">Test</text>
<text class="ts" x="195" y="72" text-anchor="middle">jest + lint</text>
<line class="arr" x1="245" y1="57" x2="270" y2="57"/>
<rect class="box" x="270" y="30" width="100" height="55" fill="#FAEEDA" stroke="#BA7517"/>
<text class="th" x="320" y="55" text-anchor="middle">Build</text>
<text class="ts" x="320" y="72" text-anchor="middle">docker image</text>
<line class="arr" x1="370" y1="57" x2="395" y2="57"/>
<rect class="box" x="395" y="30" width="100" height="55" fill="#E1F5EE" stroke="#1D9E75"/>
<text class="th" x="445" y="55" text-anchor="middle">Deploy</text>
<text class="ts" x="445" y="72" text-anchor="middle">kestra flow</text>
<line class="arr" x1="495" y1="57" x2="520" y2="57"/>
<rect class="box" x="520" y="30" width="100" height="55" fill="#EAF3DE" stroke="#639922"/>
<text class="th" x="570" y="55" text-anchor="middle">Live</text>
<text class="ts" x="570" y="72" text-anchor="middle">monitoring</text>
</svg>

## Test 4: Structural diagram

A container-with-regions diagram showing a VPC layout.

<svg width="100%" viewBox="0 0 640 220" xmlns="http://www.w3.org/2000/svg">
<style>.th{font:500 13px/1.3 sans-serif;fill:#3d3d3a}.ts{font:400 11px/1.3 sans-serif;fill:#888780}.box{stroke-width:.5;rx:8}.arr{fill:none;stroke:#888780;stroke-width:1.5;marker-end:url(#b)}</style>
<defs><marker id="b" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto"><polygon points="0 0,8 3,0 6" fill="#888780"/></marker></defs>
<rect class="box" x="20" y="20" width="600" height="180" rx="12" fill="#F1EFE8" stroke="#888780" stroke-dasharray="6 3"/>
<text class="th" x="40" y="45">VPC: Production</text>
<rect class="box" x="40" y="60" width="170" height="120" fill="#E6F1FB" stroke="#378ADD"/>
<text class="th" x="125" y="85" text-anchor="middle">Public subnet</text>
<text class="ts" x="125" y="105" text-anchor="middle">ALB + NAT</text>
<text class="ts" x="125" y="120" text-anchor="middle">10.0.1.0/24</text>
<rect class="box" x="235" y="60" width="170" height="120" fill="#EEEDFE" stroke="#7F77DD"/>
<text class="th" x="320" y="85" text-anchor="middle">App subnet</text>
<text class="ts" x="320" y="105" text-anchor="middle">API servers</text>
<text class="ts" x="320" y="120" text-anchor="middle">10.0.2.0/24</text>
<rect class="box" x="430" y="60" width="170" height="120" fill="#FAECE7" stroke="#D85A30"/>
<text class="th" x="515" y="85" text-anchor="middle">Data subnet</text>
<text class="ts" x="515" y="105" text-anchor="middle">PostgreSQL + Redis</text>
<text class="ts" x="515" y="120" text-anchor="middle">10.0.3.0/24</text>
<line class="arr" x1="210" y1="120" x2="235" y2="120"/>
<line class="arr" x1="405" y1="120" x2="430" y2="120"/>
</svg>

## Test 5: Dark mode SVG

This SVG uses CSS variables and a `prefers-color-scheme: dark` media query. It should change colours when your browser is in dark mode.

<svg width="200" height="80" viewBox="0 0 200 80" xmlns="http://www.w3.org/2000/svg">
<style>.dm-box{fill:var(--test-fill,#E6F1FB);stroke:var(--test-stroke,#378ADD);stroke-width:.5;rx:10}.dm-text{font:500 14px/1.3 sans-serif;fill:var(--test-text,#3d3d3a)}@media(prefers-color-scheme:dark){.dm-box{fill:#0a2540;stroke:#5DCAA5}.dm-text{fill:#c2c0b6}}</style>
<rect class="dm-box" x="10" y="10" width="180" height="60"/>
<text class="dm-text" x="100" y="45" text-anchor="middle">Dark mode test</text>
</svg>

## Test 6: img tag pointing to external SVG file

Using an `<img>` tag to load an SVG. This tests whether the theme allows img tags with data URIs.

<img src="data:image/svg+xml,%3Csvg width='200' height='80' viewBox='0 0 200 80' xmlns='http://www.w3.org/2000/svg'%3E%3Crect x='10' y='10' width='180' height='60' rx='10' fill='%23EAF3DE' stroke='%23639922' stroke-width='0.5'/%3E%3Ctext x='100' y='45' text-anchor='middle' font-family='sans-serif' font-size='14' fill='%233d3d3a'%3Eimg data URI%3C/text%3E%3C/svg%3E" alt="Test diagram" />

## Results

| Test | Method | Expected | Verdict |
|------|--------|----------|--------|
| 1 | Code block (xml) | Shows code | Check above |
| 2 | Raw HTML inline SVG | Renders diagram | Check above |
| 3 | Flowchart inline SVG | Renders pipeline | Check above |
| 4 | Structural inline SVG | Renders VPC diagram | Check above |
| 5 | Dark mode SVG | Changes with theme | Toggle dark mode |
| 6 | img data URI | Renders via img tag | Check above |

The key question: **does the Astro theme's markdown renderer pass through raw SVG HTML tags, or does it sanitize them?** If tests 2-5 render as diagrams, inline SVG works. If they show nothing or raw code, the theme strips HTML.