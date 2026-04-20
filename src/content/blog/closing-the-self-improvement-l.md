---
pubDatetime: 2026-04-13T01:00:00Z
title: "Closing the Self-Improvement Loop: How We Made AI Agent Prompts Evolvable"
postSlug: "closing-the-self-improvement-l"
description: "Closing the Self-Improvement Loop: How We Made AI Agent Prompts Evolvable"
tags:
  - 4
---

The evolution engine was supposed to capture, analyse, improve, and apply changes across our AI infrastructure autonomously. It did the first three. The last one — actually applying improvements to production files — was completely broken. This is the story of diagnosing that gap and building a pipeline that respects a critical constraint: **humans must stay in the loop**.

## The Promise and the Problem


<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA3MjAgNDIwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLC1hcHBsZS1zeXN0ZW0sc2Fucy1zZXJpZiI+CiAgPHJlY3Qgd2lkdGg9IjcyMCIgaGVpZ2h0PSI0MjAiIGZpbGw9IiMwYTAwMjAiIHJ4PSIxMiIvPgogIDx0ZXh0IHg9IjM2MCIgeT0iMzIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGZmZmYiIGZvbnQtc2l6ZT0iMTYiIGZvbnQtd2VpZ2h0PSI3MDAiPkV2b2x1dGlvbiBFbmdpbmUgUGlwZWxpbmUg4oCUIENhcHR1cmUg4oaSIEFwcGx5PC90ZXh0PgogIDx0ZXh0IHg9IjM2MCIgeT0iNTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iMTAiPkJlZm9yZTogSElHSC1yaXNrIGl0ZW1zIGludmlzaWJsZSBhZnRlciBpbXByb3ZlIHBoYXNlPC90ZXh0PgoKICA8IS0tIFBoYXNlIGJveGVzIC0tPgogIDxyZWN0IHg9IjIwIiB5PSI3NSIgd2lkdGg9IjEwMCIgaGVpZ2h0PSI1NSIgcng9IjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZmNDA4MSIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iNzAiIHk9Ijk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmY0MDgxIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNjAwIj5DYXB0dXJlPC90ZXh0PgogIDx0ZXh0IHg9IjcwIiB5PSIxMTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iOCI+ZXZlcnkgNmg8L3RleHQ+CgogIDxyZWN0IHg9IjE2MCIgeT0iNzUiIHdpZHRoPSIxMDAiIGhlaWdodD0iNTUiIHJ4PSI4IiBmaWxsPSJub25lIiBzdHJva2U9IiNmZmFiMDAiIHN0cm9rZS13aWR0aD0iMiIvPgogIDx0ZXh0IHg9IjIxMCIgeT0iOTciIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmFiMDAiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI2MDAiPkFuYWx5c2U8L3RleHQ+CiAgPHRleHQgeD0iMjEwIiB5PSIxMTMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iOCI+c2NvcmUgMS0xMDwvdGV4dD4KCiAgPHJlY3QgeD0iMzAwIiB5PSI3NSIgd2lkdGg9IjEwMCIgaGVpZ2h0PSI1NSIgcng9IjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZmYWIwMCIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iMzUwIiB5PSI5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmYWIwMCIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjYwMCI+SW1wcm92ZTwvdGV4dD4KICA8dGV4dCB4PSIzNTAiIHk9IjExMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSI4Ij5MTE0tcG93ZXJlZDwvdGV4dD4KCiAgPHJlY3QgeD0iNDQwIiB5PSI3NSIgd2lkdGg9IjExMCIgaGVpZ2h0PSI1NSIgcng9IjgiIGZpbGw9Im5vbmUiIHN0cm9rZT0iIzAwZmZmZiIgc3Ryb2tlLXdpZHRoPSIyIi8+CiAgPHRleHQgeD0iNDk1IiB5PSI5NyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjYwMCI+QXV0by1BcHByb3ZlPC90ZXh0PgogIDx0ZXh0IHg9IjQ5NSIgeT0iMTEzIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYjM4OGZmIiBmb250LXNpemU9IjgiPnRpZXJlZCByaXNrPC90ZXh0PgoKICA8cmVjdCB4PSI1OTAiIHk9Ijc1IiB3aWR0aD0iMTEwIiBoZWlnaHQ9IjU1IiByeD0iOCIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDBmZjQxIiBzdHJva2Utd2lkdGg9IjIiLz4KICA8dGV4dCB4PSI2NDUiIHk9Ijk3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBmZjQxIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNjAwIj5BcHBseTwvdGV4dD4KICA8dGV4dCB4PSI2NDUiIHk9IjExMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSI4Ij5ISVRMICsgVGVsZWdyYW08L3RleHQ+CgogIDwhLS0gQXJyb3dzIC0tPgogIDxsaW5lIHgxPSIxMjAiIHkxPSIxMDIiIHgyPSIxNTUiIHkyPSIxMDIiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIG1hcmtlci1lbmQ9InVybCgjYXJyKSIvPgogIDxsaW5lIHgxPSIyNjAiIHkxPSIxMDIiIHgyPSIyOTUiIHkyPSIxMDIiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIG1hcmtlci1lbmQ9InVybCgjYXJyKSIvPgogIDxsaW5lIHgxPSI0MDAiIHkxPSIxMDIiIHgyPSI0MzUiIHkyPSIxMDIiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIG1hcmtlci1lbmQ9InVybCgjYXJyKSIvPgogIDxsaW5lIHgxPSI1NTAiIHkxPSIxMDIiIHgyPSI1ODUiIHkyPSIxMDIiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiIG1hcmtlci1lbmQ9InVybCgjYXJyKSIvPgogIDxkZWZzPjxtYXJrZXIgaWQ9ImFyciIgbWFya2VyV2lkdGg9IjgiIG1hcmtlckhlaWdodD0iNiIgcmVmWD0iOCIgcmVmWT0iMyIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNMCwwIEw4LDMgTDAsNiIgZmlsbD0iI2IzODhmZiIvPjwvbWFya2VyPjwvZGVmcz4KCiAgPCEtLSBSaXNrIHRpZXIgc2VjdGlvbiAtLT4KICA8cmVjdCB4PSIyMCIgeT0iMTYwIiB3aWR0aD0iNjgwIiBoZWlnaHQ9IjI0MCIgcng9IjgiIGZpbGw9InJnYmEoMCwyNTUsMjU1LDAuMDQpIiBzdHJva2U9IiMwMGZmZmYiIHN0cm9rZS13aWR0aD0iMSIgc3Ryb2tlLWRhc2hhcnJheT0iNCw0Ii8+CiAgPHRleHQgeD0iMzYwIiB5PSIxODIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGZmZmYiIGZvbnQtc2l6ZT0iMTMiIGZvbnQtd2VpZ2h0PSI2MDAiPlJpc2sgVGllciBSb3V0aW5nPC90ZXh0PgoKICA8IS0tIExPVyB0aWVyIC0tPgogIDxyZWN0IHg9IjQwIiB5PSIyMDAiIHdpZHRoPSIyMDAiIGhlaWdodD0iOTAiIHJ4PSI2IiBmaWxsPSJyZ2JhKDM0LDE5Nyw5NCwwLjA4KSIgc3Ryb2tlPSIjMjJjNTVlIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDx0ZXh0IHg9IjE0MCIgeT0iMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMjJjNTVlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNzAwIj5MT1cgUklTSzwvdGV4dD4KICA8dGV4dCB4PSIxNDAiIHk9IjIzOCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzg2ZWZhYyIgZm9udC1zaXplPSI5Ij5wcm9tcHRzLCBkZWNpc2lvbnMsIGF0dGVudGlvbjwvdGV4dD4KICA8bGluZSB4MT0iNzAiIHkxPSIyNTAiIHgyPSIyMTAiIHkyPSIyNTAiIHN0cm9rZT0icmdiYSgzNCwxOTcsOTQsMC4zKSIgc3Ryb2tlLXdpZHRoPSIwLjUiLz4KICA8dGV4dCB4PSIxNDAiIHk9IjI2OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzIyYzU1ZSIgZm9udC1zaXplPSIxMCI+4oaSIGF1dG8tYXBwcm92ZWQ8L3RleHQ+CiAgPHRleHQgeD0iMTQwIiB5PSIyODIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iOCI+ZGFpbHkgbGltaXQ6IDEwPC90ZXh0PgoKICA8IS0tIE1FRElVTSB0aWVyIC0tPgogIDxyZWN0IHg9IjI2MCIgeT0iMjAwIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjkwIiByeD0iNiIgZmlsbD0icmdiYSgyNDUsMTU4LDExLDAuMDgpIiBzdHJva2U9IiNmNTllMGIiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPHRleHQgeD0iMzYwIiB5PSIyMjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmNTllMGIiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI3MDAiPk1FRElVTSBSSVNLPC90ZXh0PgogIDx0ZXh0IHg9IjM2MCIgeT0iMjM4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmNkMzRkIiBmb250LXNpemU9IjkiPm1lbnVzLCB0cmlnZ2Vycywgcm9hZG1hcDwvdGV4dD4KICA8bGluZSB4MT0iMjkwIiB5MT0iMjUwIiB4Mj0iNDMwIiB5Mj0iMjUwIiBzdHJva2U9InJnYmEoMjQ1LDE1OCwxMSwwLjMpIiBzdHJva2Utd2lkdGg9IjAuNSIvPgogIDx0ZXh0IHg9IjM2MCIgeT0iMjY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZjU5ZTBiIiBmb250LXNpemU9IjEwIj7ihpIgcGVuZGluZ19yZXZpZXc8L3RleHQ+CiAgPHRleHQgeD0iMzYwIiB5PSIyODIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iOCI+cXVldWVkIGZvciBodW1hbjwvdGV4dD4KCiAgPCEtLSBISUdIIHRpZXIgLS0+CiAgPHJlY3QgeD0iNDgwIiB5PSIyMDAiIHdpZHRoPSIyMDAiIGhlaWdodD0iOTAiIHJ4PSI2IiBmaWxsPSJyZ2JhKDIzOSw2OCw2OCwwLjA4KSIgc3Ryb2tlPSIjZWY0NDQ0IiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDx0ZXh0IHg9IjU4MCIgeT0iMjIyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZWY0NDQ0IiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNzAwIj5ISUdIIFJJU0s8L3RleHQ+CiAgPHRleHQgeD0iNTgwIiB5PSIyMzgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmY2E1YTUiIGZvbnQtc2l6ZT0iOSI+c2tpbGxzLCBzY2hlbWFzLCBhZ2VudHM8L3RleHQ+CiAgPGxpbmUgeDE9IjUxMCIgeTE9IjI1MCIgeDI9IjY1MCIgeTI9IjI1MCIgc3Ryb2tlPSJyZ2JhKDIzOSw2OCw2OCwwLjMpIiBzdHJva2Utd2lkdGg9IjAuNSIvPgogIDx0ZXh0IHg9IjU4MCIgeT0iMjY4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZWY0NDQ0IiBmb250LXNpemU9IjEwIj7ihpIgcGVuZGluZ19yZXZpZXcgKyDimqDvuI88L3RleHQ+CiAgPHRleHQgeD0iNTgwIiB5PSIyODIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmY2E1YTUiIGZvbnQtc2l6ZT0iOCI+aHVtYW4gZ2F0ZSBSRVFVSVJFRDwvdGV4dD4KCiAgPCEtLSBBcnJvdyBmcm9tIGltcHJvdmUgdG8gdGllcnMgLS0+CiAgPGxpbmUgeDE9IjQ5NSIgeTE9IjEzMCIgeDI9IjQ5NSIgeTI9IjE1MCIgc3Ryb2tlPSIjYjM4OGZmIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjMsMyIvPgogIDxsaW5lIHgxPSIxNDAiIHkxPSIxNTAiIHgyPSI1ODAiIHkyPSIxNTAiIHN0cm9rZT0iI2IzODhmZiIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSIzLDMiLz4KICA8bGluZSB4MT0iMTQwIiB5MT0iMTUwIiB4Mj0iMTQwIiB5Mj0iMTk1IiBzdHJva2U9IiMyMmM1NWUiIHN0cm9rZS13aWR0aD0iMSIgbWFya2VyLWVuZD0idXJsKCNhcnIyKSIvPgogIDxsaW5lIHgxPSIzNjAiIHkxPSIxNTAiIHgyPSIzNjAiIHkyPSIxOTUiIHN0cm9rZT0iI2Y1OWUwYiIgc3Ryb2tlLXdpZHRoPSIxIiBtYXJrZXItZW5kPSJ1cmwoI2FycjIpIi8+CiAgPGxpbmUgeDE9IjU4MCIgeTE9IjE1MCIgeDI9IjU4MCIgeTI9IjE5NSIgc3Ryb2tlPSIjZWY0NDQ0IiBzdHJva2Utd2lkdGg9IjEiIG1hcmtlci1lbmQ9InVybCgjYXJyMykiLz4KICA8ZGVmcz4KICAgIDxtYXJrZXIgaWQ9ImFycjIiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjYiIHJlZlg9IjgiIHJlZlk9IjMiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTTAsMCBMOCwzIEwwLDYiIGZpbGw9IiNiMzg4ZmYiLz48L21hcmtlcj4KICAgIDxtYXJrZXIgaWQ9ImFycjMiIG1hcmtlcldpZHRoPSI4IiBtYXJrZXJIZWlnaHQ9IjYiIHJlZlg9IjgiIHJlZlk9IjMiIG9yaWVudD0iYXV0byI+PHBhdGggZD0iTTAsMCBMOCwzIEwwLDYiIGZpbGw9IiNlZjQ0NDQiLz48L21hcmtlcj4KICA8L2RlZnM+CgogIDwhLS0gQm90dG9tOiBub3RpZmljYXRpb24gLS0+CiAgPHJlY3QgeD0iMTIwIiB5PSIzMTAiIHdpZHRoPSI0ODAiIGhlaWdodD0iMzYiIHJ4PSI2IiBmaWxsPSJyZ2JhKDAsMTkxLDE2NSwwLjEpIiBzdHJva2U9IiMwMGJmYTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPHRleHQgeD0iMzYwIiB5PSIzMzMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGJmYTUiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI2MDAiPvCflJQgVGVsZWdyYW0gTm90aWZpY2F0aW9uIOKGkiBIdW1hbiBSZXZpZXdzIOKGkiBBcHBseSAvIFJlamVjdCAvIFNraXA8L3RleHQ+CgogIDxsaW5lIHgxPSIxNDAiIHkxPSIyOTAiIHgyPSIxNDAiIHkyPSIzMTAiIHN0cm9rZT0icmdiYSgzNCwxOTcsOTQsMC40KSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSIyLDIiLz4KICA8bGluZSB4MT0iMzYwIiB5MT0iMjkwIiB4Mj0iMzYwIiB5Mj0iMzEwIiBzdHJva2U9InJnYmEoMjQ1LDE1OCwxMSwwLjQpIiBzdHJva2Utd2lkdGg9IjEiIHN0cm9rZS1kYXNoYXJyYXk9IjIsMiIvPgogIDxsaW5lIHgxPSI1ODAiIHkxPSIyOTAiIHgyPSI1ODAiIHkyPSIzMTAiIHN0cm9rZT0icmdiYSgyMzksNjgsNjgsMC40KSIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSIyLDIiLz4KCiAgPCEtLSBGYWlsdXJlIGNhbGxvdXQgLS0+CiAgPHJlY3QgeD0iMzAiIHk9IjM2MCIgd2lkdGg9IjY2MCIgaGVpZ2h0PSIzMCIgcng9IjQiIGZpbGw9InJnYmEoMjM5LDY4LDY4LDAuMDgpIiBzdHJva2U9InJnYmEoMjM5LDY4LDY4LDAuMykiIHN0cm9rZS13aWR0aD0iMSIvPgogIDx0ZXh0IHg9IjM2MCIgeT0iMzgwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmNhNWE1IiBmb250LXNpemU9IjEwIj7inYwgQkVGT1JFIEZJWDogSElHSC1yaXNrIGl0ZW1zIHN0YXllZCBhdCAiaW1wcm92ZWQiIOKAlCBpbnZpc2libGUgdG8gYXBwbHkgcGhhc2UgKyBub3RpZmljYXRpb25zPC90ZXh0Pgo8L3N2Zz4=" alt="Evolution Engine Pipeline Flow" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

Our evolution engine runs on a four-phase pipeline adapted from Karpathy's autoresearch pattern: **capture** raw artefacts from source systems, **analyse** them for quality, **improve** low-scoring items with LLM assistance, then **approve and apply** the results.

The engine already had adapters for prompts, menus, skills, schemas, triggers, decisions, attention, intent, and roadmap items. It ran daily via cron:

```
🔴 Capture (every 6h)
    → 🟠 Analyse (07:00 UTC)
    → 🟡 Improve (07:30 UTC, LLM-powered)
    → 🟢 Auto-Approve (tiered by risk)
    → 🔵 Apply (human-in-the-loop)
    → 🟣 Telegram Notification (08:15 UTC)
```

In practice, the pipeline was accumulating artefacts in the database but never delivering them to the files that mattered. Five hundred and sixty-six analysed artefacts sat in PostgreSQL. Seventy-three improved skills and eighty-one improved schemas existed only as database rows. The apply phase had never successfully written a change to disk.

**Diagnosis revealed three distinct failures:**

## Failure 1: HIGH-Risk Items Were Invisible

The auto-approve phase classified domains into three risk tiers:

| Tier | Domains | Behaviour |
|------|---------|-----------|
| LOW | Prompts, decisions, attention, intent | Auto-approved |
| MEDIUM | Menus, triggers, roadmap | Queued for review |
| HIGH | Skills, schemas | **Reported but never moved** |

HIGH-risk items reached the `improved` phase and stopped. The auto-approve script logged them as `requires_human` but left them in `improved` state. The apply phase only queried items in `approved` state. The notification script only queried `approved` items.

**Result**: Skills, schemas, and any HIGH-risk domain were invisible to the entire review and notification pipeline. They existed in the database but nobody knew about them.

The fix was to introduce a `pending_review` phase — already partially implemented for MEDIUM-risk items. HIGH-risk items now transition to `pending_review`, which makes them visible to both the apply phase and Telegram notifications. Each item gets a `⚠️ HIGH RISK` badge in the review interface.

```python
# Before: HIGH items stayed invisible
for item in buckets["HIGH"]:
    results.append({"action": "requires_human"})  # no phase change

# After: HIGH items become reviewable
for item in buckets["HIGH"]:
    cur.execute(
        "UPDATE evolution_artefacts SET phase = 'pending_review' "
        "WHERE artefact_id = %s", (item["artefact_id"],)
    )
```

## Failure 2: Agent Prompts Were Outside the System


<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2ODAgMzgwIiBmb250LWZhbWlseT0ic3lzdGVtLXVpLC1hcHBsZS1zeXN0ZW0sc2Fucy1zZXJpZiI+CiAgPHJlY3Qgd2lkdGg9IjY4MCIgaGVpZ2h0PSIzODAiIGZpbGw9IiMwYTAwMjAiIHJ4PSIxMiIvPgogIDx0ZXh0IHg9IjM0MCIgeT0iMzAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZjAwZmYiIGZvbnQtc2l6ZT0iMTYiIGZvbnQtd2VpZ2h0PSI3MDAiPkFnZW50IFF1YWxpdHkgU2NvcmluZyBNYXRyaXg8L3RleHQ+CiAgPHRleHQgeD0iMzQwIiB5PSI0OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSIxMCI+NyBjcml0ZXJpYSDCtyBzY29yZSAx4oCTMTAgwrcg4omlNiBza2lwcyBpbXByb3ZlbWVudDwvdGV4dD4KCiAgPCEtLSBDcml0ZXJpYSByb3dzIC0tPgogIDxyZWN0IHg9IjIwIiB5PSI2NSIgd2lkdGg9IjY0MCIgaGVpZ2h0PSIzMCIgcng9IjQiIGZpbGw9InJnYmEoMCwyNTUsMjU1LDAuMDYpIiBzdHJva2U9InJnYmEoMCwyNTUsMjU1LDAuMikiIHN0cm9rZS13aWR0aD0iMC41Ii8+CiAgPHRleHQgeD0iMzUiIHk9Ijg1IiBmaWxsPSIjMDBmZmZmIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iNjAwIj5Dcml0ZXJpb248L3RleHQ+CiAgPHRleHQgeD0iMjYwIiB5PSI4NSIgZmlsbD0iIzAwZmZmZiIgZm9udC1zaXplPSIxMSIgZm9udC13ZWlnaHQ9IjYwMCI+V2VpZ2h0PC90ZXh0PgogIDx0ZXh0IHg9IjM2MCIgeT0iODUiIGZpbGw9IiMwMGZmZmYiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSI2MDAiPkNoZWNrczwvdGV4dD4KCiAgPHRleHQgeD0iMzUiIHk9IjExNSIgZmlsbD0iI2UwZTBlMCIgZm9udC1zaXplPSIxMCI+RnJvbnRtYXR0ZXIgY29tcGxldGVuZXNzPC90ZXh0PgogIDx0ZXh0IHg9IjI2MCIgeT0iMTE1IiBmaWxsPSIjMDBmZjQxIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iNjAwIj4rMjwvdGV4dD4KICA8dGV4dCB4PSIzNjAiIHk9IjExNSIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSIxMCI+SGFzIFlBTUwgZnJvbnRtYXR0ZXIgYmxvY2s8L3RleHQ+CgogIDx0ZXh0IHg9IjM1IiB5PSIxMzciIGZpbGw9IiNlMGUwZTAiIGZvbnQtc2l6ZT0iMTAiPkRlc2NyaXB0aW9uPC90ZXh0PgogIDx0ZXh0IHg9IjI2MCIgeT0iMTM3IiBmaWxsPSIjMDBmZjQxIiBmb250LXNpemU9IjEwIj4rMTwvdGV4dD4KICA8dGV4dCB4PSIzNjAiIHk9IjEzNyIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSIxMCI+Q2xlYXIgcHVycG9zZSBzdGF0ZW1lbnQgaW4gZnJvbnRtYXR0ZXI8L3RleHQ+CgogIDx0ZXh0IHg9IjM1IiB5PSIxNTkiIGZpbGw9IiNlMGUwZTAiIGZvbnQtc2l6ZT0iMTAiPk1vZGVsIHNwZWNpZmljYXRpb248L3RleHQ+CiAgPHRleHQgeD0iMjYwIiB5PSIxNTkiIGZpbGw9IiMwMGZmNDEiIGZvbnQtc2l6ZT0iMTAiPisxPC90ZXh0PgogIDx0ZXh0IHg9IjM2MCIgeT0iMTU5IiBmaWxsPSIjYjM4OGZmIiBmb250LXNpemU9IjEwIj5EZWNsYXJlcyB3aGljaCBMTE0gdG8gdXNlPC90ZXh0PgoKICA8dGV4dCB4PSIzNSIgeT0iMTgxIiBmaWxsPSIjZTBlMGUwIiBmb250LXNpemU9IjEwIj5QZXJtaXNzaW9uIGJsb2NrPC90ZXh0PgogIDx0ZXh0IHg9IjI2MCIgeT0iMTgxIiBmaWxsPSIjMDBmZjQxIiBmb250LXNpemU9IjEwIj4rMTwvdGV4dD4KICA8dGV4dCB4PSIzNjAiIHk9IjE4MSIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSIxMCI+RGVmaW5lcyB0b29sIGFjY2VzcyBydWxlczwvdGV4dD4KCiAgPHRleHQgeD0iMzUiIHk9IjIwMyIgZmlsbD0iI2UwZTBlMCIgZm9udC1zaXplPSIxMCI+U2VjdGlvbiBzdHJ1Y3R1cmU8L3RleHQ+CiAgPHRleHQgeD0iMjYwIiB5PSIyMDMiIGZpbGw9IiNmZmFiMDAiIGZvbnQtc2l6ZT0iMTAiPsKxMTwvdGV4dD4KICA8dGV4dCB4PSIzNjAiIHk9IjIwMyIgZmlsbD0iI2IzODhmZiIgZm9udC1zaXplPSIxMCI+KzEgaWYg4omlNSBzZWN0aW9ucywg4oiSMSBpZiAmbHQ7MzwvdGV4dD4KCiAgPHRleHQgeD0iMzUiIHk9IjIyNSIgZmlsbD0iI2UwZTBlMCIgZm9udC1zaXplPSIxMCI+Q29uc3RyYWludCBsYW5ndWFnZTwvdGV4dD4KICA8dGV4dCB4PSIyNjAiIHk9IjIyNSIgZmlsbD0iI2ZmYWIwMCIgZm9udC1zaXplPSIxMCI+wrExPC90ZXh0PgogIDx0ZXh0IHg9IjM2MCIgeT0iMjI1IiBmaWxsPSIjYjM4OGZmIiBmb250LXNpemU9IjEwIj4rMSBpZiBNVVNUL05FVkVSL0FMV0FZUywg4oiSMSBpZiB3ZWFrPC90ZXh0PgoKICA8dGV4dCB4PSIzNSIgeT0iMjQ3IiBmaWxsPSIjZTBlMGUwIiBmb250LXNpemU9IjEwIj5Xb3JkIGNvdW50PC90ZXh0PgogIDx0ZXh0IHg9IjI2MCIgeT0iMjQ3IiBmaWxsPSIjZmZhYjAwIiBmb250LXNpemU9IjEwIj7CsTE8L3RleHQ+CiAgPHRleHQgeD0iMzYwIiB5PSIyNDciIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iMTAiPuKIkjEgaWYgJmx0OzIwMCwgKzEgaWYgJmd0OzMwMDA8L3RleHQ+CgogIDwhLS0gRGl2aWRlciAtLT4KICA8bGluZSB4MT0iMzAiIHkxPSIyNjIiIHgyPSI2NTAiIHkyPSIyNjIiIHN0cm9rZT0icmdiYSgwLDI1NSwyNTUsMC4yKSIgc3Ryb2tlLXdpZHRoPSIwLjUiLz4KCiAgPCEtLSBSZXN1bHRzIC0tPgogIDx0ZXh0IHg9IjM0MCIgeT0iMjgyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmYwMGZmIiBmb250LXNpemU9IjEzIiBmb250LXdlaWdodD0iNzAwIj5Jbml0aWFsIENhcHR1cmUgUmVzdWx0czwvdGV4dD4KCiAgPCEtLSBBZ2VudCBjYXJkcyAtLT4KICA8cmVjdCB4PSIzMCIgeT0iMjk1IiB3aWR0aD0iMTQ1IiBoZWlnaHQ9IjY1IiByeD0iNiIgZmlsbD0icmdiYSgzNCwxOTcsOTQsMC4xKSIgc3Ryb2tlPSIjMjJjNTVlIiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDx0ZXh0IHg9IjEwMiIgeT0iMzE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMjJjNTVlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iNzAwIj5icmFpbnN0b3JtPC90ZXh0PgogIDx0ZXh0IHg9IjEwMiIgeT0iMzMyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjODZlZmFjIiBmb250LXNpemU9IjE4IiBmb250LXdlaWdodD0iNzAwIj43PC90ZXh0PgogIDx0ZXh0IHg9IjEwMiIgeT0iMzUwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYjM4OGZmIiBmb250LXNpemU9IjgiPuKGkiBhY3RpdmUgKHNraXApPC90ZXh0PgoKICA8cmVjdCB4PSIxOTAiIHk9IjI5NSIgd2lkdGg9IjE0NSIgaGVpZ2h0PSI2NSIgcng9IjYiIGZpbGw9InJnYmEoMzQsMTk3LDk0LDAuMSkiIHN0cm9rZT0iIzIyYzU1ZSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KICA8dGV4dCB4PSIyNjIiIHk9IjMxNSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzIyYzU1ZSIgZm9udC1zaXplPSIxMCIgZm9udC13ZWlnaHQ9IjcwMCI+Z2xtLXJlc2VhcmNoPC90ZXh0PgogIDx0ZXh0IHg9IjI2MiIgeT0iMzMyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjODZlZmFjIiBmb250LXNpemU9IjE4IiBmb250LXdlaWdodD0iNzAwIj43PC90ZXh0PgogIDx0ZXh0IHg9IjI2MiIgeT0iMzUwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYjM4OGZmIiBmb250LXNpemU9IjgiPuKGkiBhY3RpdmUgKHNraXApPC90ZXh0PgoKICA8cmVjdCB4PSIzNTAiIHk9IjI5NSIgd2lkdGg9IjE0NSIgaGVpZ2h0PSI2NSIgcng9IjYiIGZpbGw9InJnYmEoMjQ1LDE1OCwxMSwwLjEpIiBzdHJva2U9IiNmNTllMGIiIHN0cm9rZS13aWR0aD0iMS41Ii8+CiAgPHRleHQgeD0iNDIyIiB5PSIzMTUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmNTllMGIiIGZvbnQtc2l6ZT0iMTAiIGZvbnQtd2VpZ2h0PSI3MDAiPmJyb3dzZXItYWdlbnQ8L3RleHQ+CiAgPHRleHQgeD0iNDIyIiB5PSIzMzIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmY2QzNGQiIGZvbnQtc2l6ZT0iMTgiIGZvbnQtd2VpZ2h0PSI3MDAiPjY8L3RleHQ+CiAgPHRleHQgeD0iNDIyIiB5PSIzNTAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtc2l6ZT0iOCI+4oaSIGFjdGl2ZSAoc2tpcCk8L3RleHQ+CgogIDxyZWN0IHg9IjUxMCIgeT0iMjk1IiB3aWR0aD0iMTQ1IiBoZWlnaHQ9IjY1IiByeD0iNiIgZmlsbD0icmdiYSgyMzksNjgsNjgsMC4xKSIgc3Ryb2tlPSIjZWY0NDQ0IiBzdHJva2Utd2lkdGg9IjEuNSIvPgogIDx0ZXh0IHg9IjU4MiIgeT0iMzE1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZWY0NDQ0IiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iNzAwIj5wbGFuLWFnZW50PC90ZXh0PgogIDx0ZXh0IHg9IjU4MiIgeT0iMzMyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmNhNWE1IiBmb250LXNpemU9IjE4IiBmb250LXdlaWdodD0iNzAwIj4yPC90ZXh0PgogIDx0ZXh0IHg9IjU4MiIgeT0iMzUwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYjM4OGZmIiBmb250LXNpemU9IjgiPuKGkiBMTE0gaW1wcm92ZTwvdGV4dD4KPC9zdmc+" alt="Agent Quality Scoring Matrix" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

The evolution engine could improve skills, menus, prompts, and schemas — but not the **agent definition files** that control how AI subagents behave. These `.md` files in `~/.config/opencode/agents/` define each agent's personality, constraints, tool permissions, and workflow. They are, in effect, the most critical prompts in the system — yet they were invisible to the evolution engine.

We built `adapter_agents.py` to close this gap. The adapter follows the same `DomainAdapter` interface as all other adapters:

**Capture** scans 4 agent definitions and 15 context files from the agents directory. Each file is fingerprinted with a content hash to prevent duplicates.

**Analyse** scores each agent on seven criteria:

| Criterion | Weight | Checks |
|-----------|--------|--------|
| Frontmatter completeness | +2 | Has YAML frontmatter block |
| Description | +1 | Clear purpose statement |
| Model specification | +1 | Declares which LLM to use |
| Permission block | +1 | Defines tool access rules |
| Section structure | +1 | ≥5 markdown sections |
| Constraint language | +1 | Uses MUST/NEVER/ALWAYS |
| Word count | +1 | ≥200 words (comprehensive if >3000) |

Scores range from 1–10. Items scoring ≥6 skip improvement and go directly to `active`.

Results from our initial capture:

| Agent | Score | Issues |
|-------|-------|--------|
| brainstorm | 7 | None — well-structured |
| glm-research | 7 | None — comprehensive |
| browser-agent | 6 | None — solid despite fewer sections |
| plan-agent | 2 | Missing frontmatter entirely |
| 15 context files | 1–2 | No frontmatter (expected — they're plain markdown) |

**Improve** sends low-scoring agents to GLM-5.1 with a domain-specific system prompt that instructs the LLM to add missing frontmatter, strengthen constraint language, and improve structural clarity.

A key design decision: improved versions **inherit parent metadata** (`filename`, `agent_name`, `mode`, `model`) so the apply phase knows exactly which file to write to.

```python
inherited = {}
for key in ("agent_name", "filename", "mode", "model"):
    if key in parent_meta:
        inherited[key] = parent_meta[key]
```

The adapter was registered across three entry points (`bridges.py`, `cli.py`, `run_phase.py`) and added to the risk tier map as HIGH — because overwriting agent definition files without human review would be reckless.

## Failure 3: The Apply Phase Had No Target Resolution

Even when items reached the review queue, the apply phase couldn't determine where to write them. The `_resolve_target` function only knew about skills, menus, schemas, prompts, and triggers. Agents returned `(None, None)` — meaning the apply phase would silently skip them.

```python
# Before: agents were unhandled
if domain == "triggers":
    return str(TRIGGERS_FILE), "triggers.yaml"
return None, None  # agents fell through to here

# After: agents resolve to actual file paths
if domain == "agents":
    filename = meta.get("filename", "")
    if filename:
        target = AGENTS_DIR / filename
        return str(target), f"agents/{filename} ({agent_name})"
```

This same pattern applies to any new domain adapter — the apply phase needs a resolver for each domain. Without it, artefacts accumulate but never reach production.

## The Notification Gap (And Fix)

The Telegram notification script had a path mismatch — it referenced `send.py` when the actual script was `send-telegram.sh`. We fixed both the path and the invocation:

```python
# Before: wrong script, wrong arguments
subprocess.run([sys.executable, str(NOTIFY_SCRIPT), "--message", message])

# After: correct shell script, positional argument
subprocess.run([str(NOTIFY_SCRIPT), message])
```

The notification now correctly reports HIGH-risk items separately with a warning, giving the operator clear visibility into what needs attention:

```
🔔 Evolution Engine: 50 items pending review

⚠️  50 HIGH-risk items require human review

  • agents: 5
  • schemas: 11
  • skills: 34

Run `evolve review` to inspect, or `evolve apply-all` for interactive session.
```

## Evaluation Criteria for Self-Improving Systems

Based on this work, we propose five evaluation criteria for any self-improving AI pipeline:

**1. Signal Coverage**: What percentage of events generate trackable signals? Our signal reconciler backfills missing signals from trigger event logs, taking coverage from 7% to 100%.

**2. Noise Ratio**: How many proposed improvements are genuinely useful? The original menu adapter generated 40 noise proposals for skills with zero signal data. Reading from aggregate statistics instead of flat events, and skipping skills with fewer than 3 presentations, eliminated this entirely.

**3. Loop Closure**: Does every improved artefact eventually reach a human for review? Before this work, HIGH-risk domains had a 0% closure rate. They now flow through `pending_review` → Telegram notification → interactive apply.

**4. Blast Radius Awareness**: When an improvement is applied, does the system understand what it affects? Agent definitions control subagent behaviour across the entire system — hence the HIGH risk tier and human gate.

**5. Metadata Continuity**: When an artefact is improved by LLM, does it retain enough metadata to be actionable? Our initial implementation lost `filename` and `agent_name` in the improvement phase, making improved artefacts unresolvable. Inheriting parent metadata solved this.

<details>
<summary>Technical Details: The Complete Pipeline Architecture</summary>

### File Layout

```
~/.config/opencode/skills/evolve/scripts/
├── adapter_base.py        # DomainAdapter ABC + registry
├── adapter_agents.py      # NEW: agents domain adapter
├── adapter_skills.py      # skills quality reviews
├── adapter_prompts.py     # prompt capture from sessions
├── adapter_menus.py       # menu signal analysis
├── adapter_schemas.py     # schema DNA scoring
├── adapter_*.py           # triggers, decisions, attention, intent, roadmap
├── orchestrator.py        # coordinates all adapters through 4 phases
├── auto_approve.py        # tiered approval (LOW/MEDIUM/HIGH)
├── apply_phase.py         # HITL apply with diff preview + Telegram
├── db.py                  # PostgreSQL layer with pgvector
├── llm.py                 # GLM-5.1 integration for improve phase
├── bridges.py             # cross-domain feedback loops
├── cli.py                 # CLI entry point
└── run_phase.py           # cron entry point
```

### Cron Schedule

```
0 */6 * * *   capture (every 6 hours)
0 7 * * *     analyse
30 7 * * *    improve (LLM-powered)
0 8 * * *     monitor
15 8 * * *    notify (Telegram)
```

### Database Schema

The `evolution_artefacts` table uses PostgreSQL with pgvector for semantic search. Artefacts progress through phases: `captured → analysed → improved → pending_review/approved → applied/dismissed`. The CHECK constraint on `risk_tier` enforces `LOW/MEDIUM/HIGH` only.

### Risk Tier Classification

| Domain | Risk | Rationale |
|--------|------|-----------|
| Prompts, decisions, attention, intent | LOW | Non-destructive, easily reversible |
| Menus, triggers | MEDIUM | Affects UX, moderate blast radius |
| Skills, schemas, agents | HIGH | Controls system behaviour, high blast radius |

</details>

## What This Means

The pattern here generalises beyond our specific stack. Any system that uses LLMs to improve its own configuration needs:

1. **A capture phase** that knows where to look for improvable artefacts
2. **A quality gate** that can distinguish signal from noise
3. **A risk classification** that matches blast radius to approval requirements
4. **A notification system** that doesn't silently drop HIGH-risk items
5. **An apply phase** that resolves abstract artefacts back to concrete file paths

The most subtle failure mode is #4 — systems that appear to work but silently skip their most critical outputs. Our HIGH-risk items weren't failing; they were being processed and reported correctly. They just never appeared in the queue that humans actually looked at.

Self-improving AI systems need the same thing that all autonomous systems need: **observability at every stage, and a human gate at every point where the blast radius exceeds the confidence threshold.**

**Tags**: ai-agents, self-improvement, evolution-engine, hitl, observability, karpathy
**Categories**: AI Infrastructure, Engineering