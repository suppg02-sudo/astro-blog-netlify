---
pubDatetime: 2026-04-18T20:30:00Z
title: "What If Your AI Infrastructure Could Improve Itself?"
postSlug: "what-if-your-ai-infrastructure"
description: "What If Your AI Infrastructure Could Improve Itself?"
tags:
  - others
---

Skills drift. Cron jobs silently degrade. Your instruction file bloats with CRITICAL markers until nothing means anything. What if, instead of periodic manual audits, you built a system that **continuously monitors itself, scores every artefact, and auto-applies improvements it's confident about** — while surfacing the uncertain ones for human review?

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA4MDAgNTIwIj4KPHJlY3Qgd2lkdGg9IjgwMCIgaGVpZ2h0PSI1MjAiIGZpbGw9IiMwYTAwMjAiIHJ4PSI4Ii8+Cjx0ZXh0IHg9IjQwMCIgeT0iMzIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGZmZmYiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMTYiIGZvbnQtd2VpZ2h0PSJib2xkIj5BdXRvLUltcHJvdmVtZW50IFBpcGVsaW5lIOKAlCBUaGUgRXZvbHZlIERhc2hib2FyZDwvdGV4dD4KCjwhLS0gU2lnbmFsIFNvdXJjZXMgLS0+CjxyZWN0IHg9IjIwIiB5PSI2MCIgd2lkdGg9IjE0MCIgaGVpZ2h0PSI0NCIgcng9IjYiIGZpbGw9Im5vbmUiIHN0cm9rZT0iI2ZmMDBmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPHRleHQgeD0iOTAiIHk9Ijc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmYwMGZmIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCI+U2lnbmFsIFNvdXJjZXM8L3RleHQ+Cjx0ZXh0IHg9IjkwIiB5PSI5MyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI4Ij5Dcm9uIMK3IEJsb2cgwrcgQUdFTlRTLm1kPC90ZXh0PgoKPCEtLSBDYXB0dXJlIExheWVyIC0tPgo8cmVjdCB4PSIyMDAiIHk9IjYwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjQ0IiByeD0iNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDBmZmZmIiBzdHJva2Utd2lkdGg9IjEuNSIvPgo8dGV4dCB4PSIyNzAiIHk9Ijc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBmZmZmIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCI+Q2FwdHVyZSBMYXllcjwvdGV4dD4KPHRleHQgeD0iMjcwIiB5PSI5MyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI4Ij5zY2FuX2Nyb24gwrcgcmV2aWV3X3Bvc3RzPC90ZXh0PgoKPCEtLSBQb3N0Z3JlU1FMIC0tPgo8cmVjdCB4PSIzODAiIHk9IjYwIiB3aWR0aD0iMTQwIiBoZWlnaHQ9IjQ0IiByeD0iNiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjMDBmZjQxIiBzdHJva2Utd2lkdGg9IjEuNSIvPgo8dGV4dCB4PSI0NTAiIHk9Ijc4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBmZjQxIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjEwIiBmb250LXdlaWdodD0iYm9sZCI+UG9zdGdyZVNRTDwvdGV4dD4KPHRleHQgeD0iNDUwIiB5PSI5MyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI4Ij5ldm9sdXRpb24gdGFibGU8L3RleHQ+Cgo8IS0tIEV2b2x2ZSBEYXNoYm9hcmQgLS0+CjxyZWN0IHg9IjU2MCIgeT0iNTAiIHdpZHRoPSIyMjAiIGhlaWdodD0iNjQiIHJ4PSI4IiBmaWxsPSJyZ2JhKDAsMjU1LDI1NSwwLjA4KSIgc3Ryb2tlPSIjMDBmZmZmIiBzdHJva2Utd2lkdGg9IjIiLz4KPHRleHQgeD0iNjcwIiB5PSI3MiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzAwZmZmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSIxMiIgZm9udC13ZWlnaHQ9ImJvbGQiPkVWT0xWRSBEQVNIQk9BUkQ8L3RleHQ+Cjx0ZXh0IHg9IjY3MCIgeT0iODgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGZmZmYiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOSI+RmFzdEFQSSArIFN0YXRpYyBIVE1MPC90ZXh0Pgo8dGV4dCB4PSI2NzAiIHk9IjEwMiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI4Ij4zIFRhYnM6IE92ZXJ2aWV3IC8gQXBwcm92YWxzIC8gQ3JvbjwvdGV4dD4KCjwhLS0gQXJyb3dzOiBTb3VyY2VzIOKGkiBDYXB0dXJlIC0tPgo8bGluZSB4MT0iMTYwIiB5MT0iODIiIHgyPSIyMDAiIHkyPSI4MiIgc3Ryb2tlPSIjZmYwMGZmIiBzdHJva2Utd2lkdGg9IjEuMiIgbWFya2VyLWVuZD0idXJsKCNhcnItcGluaykiLz4KPCEtLSBDYXB0dXJlIOKGkiBQRyAtLT4KPGxpbmUgeDE9IjM0MCIgeTE9IjgyIiB4Mj0iMzgwIiB5Mj0iODIiIHN0cm9rZT0iIzAwZmZmZiIgc3Ryb2tlLXdpZHRoPSIxLjIiIG1hcmtlci1lbmQ9InVybCgjYXJyLWN5YW4pIi8+CjwhLS0gUEcg4oaSIERhc2hib2FyZCAtLT4KPGxpbmUgeDE9IjUyMCIgeTE9IjgyIiB4Mj0iNTYwIiB5Mj0iODIiIHN0cm9rZT0iIzAwZmY0MSIgc3Ryb2tlLXdpZHRoPSIxLjIiIG1hcmtlci1lbmQ9InVybCgjYXJyLWdyZWVuKSIvPgoKPCEtLSBEb21haW4gYm94ZXMgLS0+CjxnPgo8cmVjdCB4PSIzMCIgeT0iMTQwIiB3aWR0aD0iMTA1IiBoZWlnaHQ9IjM2IiByeD0iNSIgZmlsbD0icmdiYSgwLDI1NSwyNTUsMC4wNikiIHN0cm9rZT0iIzAwZmZmZiIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjgyIiB5PSIxNTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGZmZmYiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOSI+U2tpbGxzICgyMzIpPC90ZXh0PgoKPHJlY3QgeD0iMTQ1IiB5PSIxNDAiIHdpZHRoPSIxMDUiIGhlaWdodD0iMzYiIHJ4PSI1IiBmaWxsPSJyZ2JhKDI1NSwwLDI1NSwwLjA2KSIgc3Ryb2tlPSIjZmYwMGZmIiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iMTk3IiB5PSIxNTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZjAwZmYiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOSI+TWVudXMgKDM3OSk8L3RleHQ+Cgo8cmVjdCB4PSIyNjAiIHk9IjE0MCIgd2lkdGg9IjEwNSIgaGVpZ2h0PSIzNiIgcng9IjUiIGZpbGw9InJnYmEoMCwyNTUsNjUsMC4wNikiIHN0cm9rZT0iIzAwZmY0MSIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjMxMiIgeT0iMTU4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBmZjQxIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjkiPlByb21wdHMgKDg1KTwvdGV4dD4KCjxyZWN0IHg9IjM3NSIgeT0iMTQwIiB3aWR0aD0iMTA1IiBoZWlnaHQ9IjM2IiByeD0iNSIgZmlsbD0icmdiYSgyNTUsMTcxLDAsMC4wNikiIHN0cm9rZT0iI2ZmYWIwMCIgc3Ryb2tlLXdpZHRoPSIxIi8+Cjx0ZXh0IHg9IjQyNyIgeT0iMTU4IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZhYjAwIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjkiPlNjaGVtYXMgKDIwMik8L3RleHQ+Cgo8cmVjdCB4PSI0OTAiIHk9IjE0MCIgd2lkdGg9IjEwNSIgaGVpZ2h0PSIzNiIgcng9IjUiIGZpbGw9InJnYmEoMCwxOTEsMTY1LDAuMDYpIiBzdHJva2U9IiMwMGJmYTUiIHN0cm9rZS13aWR0aD0iMSIvPgo8dGV4dCB4PSI1NDIiIHk9IjE1OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzAwYmZhNSIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij5BZ2VudHMgKDI4KTwvdGV4dD4KCjxyZWN0IHg9IjYwNSIgeT0iMTQwIiB3aWR0aD0iMTA1IiBoZWlnaHQ9IjM2IiByeD0iNSIgZmlsbD0icmdiYSgxNzksMTM2LDI1NSwwLjA2KSIgc3Ryb2tlPSIjYjM4OGZmIiBzdHJva2Utd2lkdGg9IjEiLz4KPHRleHQgeD0iNjU3IiB5PSIxNTgiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOSI+Q3JvbiAoNzEpPC90ZXh0Pgo8L2c+Cgo8IS0tIERvbWFpbiBhcnJvdyB1cCB0byBkYXNoYm9hcmQgLS0+CjxsaW5lIHgxPSI2NzAiIHkxPSIxNDAiIHgyPSI2NzAiIHkyPSIxMTgiIHN0cm9rZT0iIzAwZmZmZiIgc3Ryb2tlLXdpZHRoPSIxIiBzdHJva2UtZGFzaGFycmF5PSIzLDMiLz4KCjwhLS0gQXV0by1BcHByb3ZlIFNlY3Rpb24gLS0+CjxyZWN0IHg9IjQwIiB5PSIyMTAiIHdpZHRoPSIzNDAiIGhlaWdodD0iMTAwIiByeD0iOCIgZmlsbD0icmdiYSgyNTUsMCwyNTUsMC4wNCkiIHN0cm9rZT0iI2ZmMDBmZiIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPHRleHQgeD0iMjEwIiB5PSIyMzIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZjAwZmYiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSJib2xkIj5BdXRvLUFwcHJvdmUgRW5naW5lPC90ZXh0Pgo8dGV4dCB4PSIyMTAiIHk9IjI1MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij5UaHJlc2hvbGQ6IDgwJSBjb25maWRlbmNlIOKGkiBhdXRvLWFwcGx5PC90ZXh0Pgo8dGV4dCB4PSIyMTAiIHk9IjI2OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij4xMjUgc2NoZW1hcyBhdXRvLWFwcGxpZWQ8L3RleHQ+Cjx0ZXh0IHg9IjIxMCIgeT0iMjg2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYjM4OGZmIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjkiPjQzIHNraWxsIGltcHJvdmVtZW50cyBhdXRvLWFwcGxpZWQ8L3RleHQ+Cjx0ZXh0IHg9IjIxMCIgeT0iMzAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBmZjQxIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjgiPjE2OCB0b3RhbCBoYW5kcy1mcmVlIGltcHJvdmVtZW50czwvdGV4dD4KCjwhLS0gQmxvZyBRdWFsaXR5IFNlY3Rpb24gLS0+CjxyZWN0IHg9IjQyMCIgeT0iMjEwIiB3aWR0aD0iMzQwIiBoZWlnaHQ9IjEwMCIgcng9IjgiIGZpbGw9InJnYmEoMCwyNTUsNjUsMC4wNCkiIHN0cm9rZT0iIzAwZmY0MSIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPHRleHQgeD0iNTkwIiB5PSIyMzIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGZmNDEiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSJib2xkIj5CbG9nIFF1YWxpdHkgUmV2aWV3ZXI8L3RleHQ+Cjx0ZXh0IHg9IjU5MCIgeT0iMjUwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYjM4OGZmIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjkiPkxMTSBzY29yZXM6IHN0cnVjdHVyZSwgZGVwdGgsIHJlYWRhYmlsaXR5PC90ZXh0Pgo8dGV4dCB4PSI1OTAiIHk9IjI2OCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij5zb3VyY2VfZGl2ZXJzaXR5LCByZWxldmFuY2UgKDEtMTApPC90ZXh0Pgo8dGV4dCB4PSI1OTAiIHk9IjI4NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2ZmYWIwMCIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij5hdmcgc2NvcmU6IDUuNS8xMCAoYWktbmV3cyk8L3RleHQ+Cjx0ZXh0IHg9IjU5MCIgeT0iMzAwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBmZjQxIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjgiPkdlbmVyYXRlcyBzY3JpcHQgaW1wcm92ZW1lbnQgc3VnZ2VzdGlvbnM8L3RleHQ+Cgo8IS0tIEFHRU5UUy5tZCBIZWFsdGggLS0+CjxyZWN0IHg9IjQwIiB5PSIzNDAiIHdpZHRoPSIzNDAiIGhlaWdodD0iMTAwIiByeD0iOCIgZmlsbD0icmdiYSgyNTUsMTcxLDAsMC4wNCkiIHN0cm9rZT0iI2ZmYWIwMCIgc3Ryb2tlLXdpZHRoPSIxLjUiLz4KPHRleHQgeD0iMjEwIiB5PSIzNjIiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNmZmFiMDAiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iMTEiIGZvbnQtd2VpZ2h0PSJib2xkIj5BR0VOVFMubWQgSGVhbHRoIEFuYWx5emVyPC90ZXh0Pgo8dGV4dCB4PSIyMTAiIHk9IjM4MCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij41IHNpZ25hbCBzb3VyY2VzOiB0cmlnZ2VycywgbWVudXMsPC90ZXh0Pgo8dGV4dCB4PSIyMTAiIHk9IjM5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij5kZWZlcnJlZCwgc3ViYWdlbnRzLCBzZXNzaW9uIHF1YWxpdHk8L3RleHQ+Cjx0ZXh0IHg9IjIxMCIgeT0iNDE0IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjZmZhYjAwIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjkiPlNjb3JlOiAwLjIzLzEuMCDigJQgNzQgc2VjdGlvbnMgcGFyc2VkPC90ZXh0Pgo8dGV4dCB4PSIyMTAiIHk9IjQzMCIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzAwZmY0MSIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI4Ij40IGltcHJvdmVtZW50IHByb3Bvc2FscyBwZW5kaW5nPC90ZXh0PgoKPCEtLSBDcm9uIFRyYWNrZXIgLS0+CjxyZWN0IHg9IjQyMCIgeT0iMzQwIiB3aWR0aD0iMzQwIiBoZWlnaHQ9IjEwMCIgcng9IjgiIGZpbGw9InJnYmEoMCwxOTEsMTY1LDAuMDQpIiBzdHJva2U9IiMwMGJmYTUiIHN0cm9rZS13aWR0aD0iMS41Ii8+Cjx0ZXh0IHg9IjU5MCIgeT0iMzYyIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBiZmE1IiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjExIiBmb250LXdlaWdodD0iYm9sZCI+Q3JvbiBIZWFsdGggVHJhY2tlcjwvdGV4dD4KPHRleHQgeD0iNTkwIiB5PSIzODAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiNiMzg4ZmYiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOSI+OCBjcm9uIGpvYnMgaW5zdHJ1bWVudGVkPC90ZXh0Pgo8dGV4dCB4PSI1OTAiIHk9IjM5NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2IzODhmZiIgZm9udC1mYW1pbHk9Im1vbm9zcGFjZSIgZm9udC1zaXplPSI5Ij42NyBoaXN0b3JpY2FsIHJ1bnMgcmV0cm8tc2Nhbm5lZDwvdGV4dD4KPHRleHQgeD0iNTkwIiB5PSI0MTQiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGJmYTUiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOSI+UmVhbC10aW1lIGhvb2tzICsgZGFpbHkgc2Nhbm5lcjwvdGV4dD4KPHRleHQgeD0iNTkwIiB5PSI0MzAiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwMGZmNDEiIGZvbnQtZmFtaWx5PSJtb25vc3BhY2UiIGZvbnQtc2l6ZT0iOCI+MiBkb21haW5zOiBjcm9uX25ld3MgKyBjcm9uX3Jlc2VhcmNoPC90ZXh0PgoKPCEtLSBGb290ZXIgLS0+Cjx0ZXh0IHg9IjQwMCIgeT0iNDgwIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMDBmZmZmIiBmb250LWZhbWlseT0ibW9ub3NwYWNlIiBmb250LXNpemU9IjkiIG9wYWNpdHk9IjAuNiI+MSwxNTcgYXJ0ZWZhY3RzIGFjcm9zcyAxMiBkb21haW5zIMK3IDMsMDE2IGxpbmVzIG9mIGNvZGUgwrcgMTAwJSBzZWxmLWltcHJvdmluZzwvdGV4dD4KCjwhLS0gQXJyb3cgbWFya2VycyAtLT4KPGRlZnM+CjxtYXJrZXIgaWQ9ImFyci1jeWFuIiBtYXJrZXJXaWR0aD0iNiIgbWFya2VySGVpZ2h0PSI2IiByZWZYPSI1IiByZWZZPSIzIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0wLDAgTDYsMyBMMCw2IiBmaWxsPSIjMDBmZmZmIi8+PC9tYXJrZXI+CjxtYXJrZXIgaWQ9ImFyci1waW5rIiBtYXJrZXJXaWR0aD0iNiIgbWFya2VySGVpZ2h0PSI2IiByZWZYPSI1IiByZWZZPSIzIiBvcmllbnQ9ImF1dG8iPjxwYXRoIGQ9Ik0wLDAgTDYsMyBMMCw2IiBmaWxsPSIjZmYwMGZmIi8+PC9tYXJrZXI+CjxtYXJrZXIgaWQ9ImFyci1ncmVlbiIgbWFya2VyV2lkdGg9IjYiIG1hcmtlckhlaWdodD0iNiIgcmVmWD0iNSIgcmVmWT0iMyIgb3JpZW50PSJhdXRvIj48cGF0aCBkPSJNMCwwIEw2LDMgTDAsNiIgZmlsbD0iIzAwZmY0MSIvPjwvbWFya2VyPgo8L2RlZnM+Cjwvc3ZnPgo=" alt="Auto-Improvement Pipeline Architecture" style="display:block;width:100%;max-width:680px;height:auto;margin:1.5rem auto;">

## Quick Summary

- **1,157 artefacts** tracked across 12 domains — skills, prompts, schemas, menus, agents, cron jobs, and more
- **168 auto-applied improvements** at 80% confidence threshold with zero false positives
- **Closed feedback loops**: blog quality scores feed back into the scripts that generate them
- **Instruction file as code**: your AGENTS.md gets its own health checks, parsed into 74 sections and scored against real usage data
- **~3,000 lines of code** — one FastAPI router, one HTML file, six scripts

<details>
<summary><strong>The Core Idea: Schema &rarr; Signal &rarr; Self-Improvement</strong></summary>

The system rests on a simple triad:

1. **Schema** — Define what matters. Every artefact gets a type (skill, prompt, schema, cron run, blog post, instruction section), a phase (captured, analysed, improved, applied, dismissed), and a confidence score (0-100%).

2. **Signal** — Instrument everything. Cron jobs log their runs. Blog posts get scored by an LLM on 5 dimensions. Menu selections get tracked. Trigger usage gets recorded. Your AGENTS.md gets parsed into sections and each section scored against actual usage data.

3. **Self-Improvement** — Close the loop. High-confidence changes get auto-applied. Blog quality scores feed back into script improvements. Instruction file analysis generates concrete edit proposals. The system doesn't just report — it acts.

When the improver can improve itself, you've built something genuinely new: an AI infrastructure that gets better at getting better.

</details>

## The Dashboard

A dark-themed control plane with three views. **Overview** shows all domains at a glance — artefact counts, average confidence, phase distribution. **Approvals** queues items needing human review, filterable by domain and phase. **Cron Health** tracks every instrumented job, run history, success rates, and output quality scores.

Each artefact opens into a detail modal: what it is, why it was flagged, what the proposed change is, and a confidence breakdown. Approve, reject, or defer with one click — or let the auto-approve engine handle anything above your threshold.

<details>
<summary><strong>Technical Details: Architecture and Stack</strong></summary>

The dashboard is deliberately simple: a **1,078-line FastAPI router** backed by PostgreSQL, serving a **550-line single-file HTML frontend** with a neon cyberpunk palette (dark backgrounds, cyan and pink highlights, green success states).

It runs as an additional route (`/evolve/`) on an existing chat-api container — no new services needed. The router registers with `prefix="/evolve"` in `main.py`, so all API paths are `/evolve/api/*`.

**Key endpoints:**

| Endpoint | Purpose |
|----------|---------|
| `/api/stats` | Domain aggregates, confidence distribution |
| `/api/artefacts` | Filtered artefact list with pagination |
| `/api/detail/{id}` | Full artefact content and confidence breakdown |
| `/api/confidence/{id}` | Confidence score computation |
| `/api/auto-approve` | Batch auto-approve above threshold |
| `/api/approve/{id}` | Manual single-artefact approve |
| `DELETE /api/skill/{name}` | Skill deletion with safety checks |

The confidence scoring considers phase momentum (artefacts progressing through phases gain confidence), domain-specific baselines (schemas score higher than subjective domains like prompts), age decay (stale artefacts lose confidence), and content quality signals.

**Hot-deploy pattern:** `docker cp evolve.py chat-api:/app/routers/evolve.py && docker restart chat-api` for router changes. The HTML frontend is volume-mounted and auto-updates on host edit.

</details>

## Cron Job Tracking

Every cron job gets a hook — a single function call at the end of each run that logs the job name, status, duration, items processed, and any errors. For existing jobs, a retroactive scanner backfills historical runs from log files so you get immediate visibility without waiting for new data.

The payoff: see at a glance which jobs are healthy, which are degrading, and which have quietly stopped working.

<details>
<summary><strong>Technical Details: Instrumentation Patterns</strong></summary>

Eight cron jobs are instrumented across two patterns:

**Shared tracker** (4 jobs): `tracker_base.py` provides a `log_to_evolution()` function used by ai-news, oss-releases, karpathy-tracker, and evolution-research. Each job calls it at the end of its run.

**Shell scripts** (4 jobs): iran-research and market-news use inline Python hooks that write directly to PostgreSQL — minimal additions that don't require refactoring existing scripts.

**Retroactive scanner** (`scan_cron_logs.py`, 177 lines): Parses historical log files to backfill past runs. Found 67 historical runs on first scan. Runs daily at 09:30 UTC to catch any runs the real-time hooks miss.

The result is two auto-populated dashboard domains:
- `cron_news` — 39 tracked runs
- `cron_research` — 32 tracked runs

Each log entry includes: job name, status, duration, items count, error messages, output references (blog post URLs, file paths), and timestamps.

</details>

## Blog Quality as a Feedback Loop

If your cron jobs produce blog posts, score them automatically — structure, depth, readability, source diversity, relevance — each on a 1-10 scale. But the real value isn't the score itself. It's what happens next: **aggregating scores by cron job and generating specific script improvements**.

If ai-news posts consistently score 3/10 on depth, the system proposes concrete changes — add a technical context paragraph, include a comparison table, write a "what this means" summary. Not generic advice. Code-level suggestions with What/Where/Change structure.

<details>
<summary><strong>Technical Details: Reviewer Implementation</strong></summary>

The reviewer (`review_cron_posts.py`, 361 lines) works in two modes:

**Review mode** (`--scan`): Fetches recent blog posts from Directus, sends each to an LLM with a structured scoring prompt. The LLM returns JSON with scores on 5 dimensions plus reasoning. Results stored as child artefacts in the evolution table.

**Improve mode** (`--improve <job_name>`): Aggregates all reviews for a specific cron job, identifies the weakest dimension, and generates specific script improvement suggestions. For ai-news, depth scored 3/10 — 5 suggestions generated:

| Suggestion | What | Where |
|------------|------|-------|
| Technical context | Add a paragraph explaining implications | After each news item |
| Comparison table | Include a table comparing approaches | In the analysis section |
| Trend analysis | Add a "trends this week" summary | At the end of the digest |
| Source attribution | Cite original sources with links | In each item header |
| "What this means" | Add forward-looking implications | After each major item |

Scoring dimensions and typical ranges:

| Dimension | What It Measures | Range |
|-----------|-----------------|-------|
| Structure | Heading hierarchy, paragraph flow | 6-8/10 |
| Depth | Technical detail, evidence quality | 2-5/10 (weakest) |
| Readability | Sentence complexity, jargon balance | 5-7/10 |
| Source Diversity | Multiple perspectives, links | 3-6/10 |
| Relevance | Topic alignment with target audience | 7-9/10 |

Cron schedule: review at 10:30 UTC daily, improve at 11:00-11:30 UTC per job.

</details>

## Your Instruction File Needs Its Own Doctor

Your AGENTS.md is a **configuration file**. Like any config file, it accumulates cruft. What if you treated it like code that needs CI/CD — parsed into sections, each scored against real usage data?

The findings are usually uncomfortable: zombie triggers that haven't fired in months, CRITICAL markers inflated to the point of meaninglessness, sections costing thousands of tokens per session that rarely get used.

<details>
<summary><strong>Technical Details: Health Analyzer Implementation</strong></summary>

The analyzer (`agents_md_health.py`, 850 lines) uses five signal sources:

1. **Trigger usage** — which triggers fire frequently vs. which are zombies (defined but never used)
2. **Menu signals** — present/select patterns revealing which options users actually choose
3. **Deferred options** — items deferred more than 30 days (stale interest)
4. **Subagent outcomes** — success/failure ratios per agent type
5. **Session quality** — ratio of experiences, lessons, patterns captured per session

The parser breaks AGENTS.md into 74 sections and scores each on six axes: usage, recency, dependency, conflict, complexity, and token cost.

**First scan results:**
- Overall health: **0.23/1.0**
- 15 CRITICAL markers in a single block — classic inflation
- 3 deferral categories with zero completions
- ~9,588 tokens/session just for AGENTS.md context

**Five proposal types generated:**

| Type | Meaning | Action |
|------|---------|--------|
| `TRIGGER_ZOMBIE` | Trigger defined but never used | Remove or consolidate |
| `DUPLICATE_RULE` | Same rule stated multiple times | Merge into one |
| `CRITICAL_INFLATION` | Too many CRITICALs in one section | Demote to WARNING |
| `TOKEN_BLOAT` | High token cost, low usage | Move behind progressive disclosure |
| `DEFERRAL_SIGNAL` | Deferred items accumulating | Clean up or commit |

CLI modes: `--scan-only` (daily cron), `--dry-run` (preview), `--review` (queue proposals), `--apply` (execute), `--reject` (dismiss), `--rollback` (undo). All changes logged to `agents_md_changes.jsonl`.

</details>

## Auto-Approve Engine

Set a confidence threshold (80% by default) and let the system apply improvements automatically. Schemas get auto-applied at higher rates because they're mechanical — either the structure validates or it doesn't. Skills get fewer auto-applies because quality is more subjective. Stale artefacts decay over time, preventing zombie approvals.

After each run, a blog post report documents what was applied — a permanent audit trail.

<details>
<summary><strong>Technical Details: Scoring and Results</strong></summary>

Confidence scoring considers four factors:

- **Phase momentum** — artefacts progressing through phases gain confidence naturally
- **Domain baselines** — schemas start higher (mechanical) than prompts or menus (subjective)
- **Age decay** — confidence decreases over time, preventing stale auto-applies
- **Content quality** — well-structured content with clear purpose descriptions scores higher

**Results so far:**

| Domain | Total | Auto-Applied | Manually Applied | Dismissed |
|--------|-------|-------------|-----------------|-----------|
| Schemas | 202 | 125 | 0 | 0 |
| Skills | 232 | 43 | 23 | 60 |
| Prompts | 85 | 3 | 3 | 17 |
| Menus | 379 | 0 | 0 | 80 |
| Agents | 28 | 2 | 1 | 21 |

Overall: **168 auto-applied, 27 manually applied, 80 dismissed** across 1,157 artefacts. A **17% action rate** — 1 in 6 artefacts results in a real change. Zero false positives at 80% threshold.

</details>

## What It Takes to Build One

You don't need a new service. One PostgreSQL table, one FastAPI router, one HTML file, and instrumentation hooks for your existing cron jobs. The prototype was ~3,000 lines built in one session.

<details>
<summary><strong>Technical Details: Code Breakdown</strong></summary>

| Component | Lines | Purpose |
|-----------|-------|---------|
| `evolve.py` | 1,078 | FastAPI router — all endpoints, scoring, domain handlers |
| `index.html` | 550 | Single-file dashboard — 3 tabs, detail modal, filters |
| `agents_md_health.py` | 850 | AGENTS.md health analyzer — 5 signal sources, 5 proposal types |
| `review_cron_posts.py` | 361 | Blog quality reviewer + script improvement generator |
| `scan_cron_logs.py` | 177 | Retroactive cron log scanner |
| `tracker_base.py` | ~50 | Shared `log_to_evolution()` function |
| **Total** | **~3,016** | |

Dependencies: PostgreSQL (existing), FastAPI (existing container), one LLM endpoint (for blog scoring). No new infrastructure required.

</details>

## Why This Matters

The pattern generalises beyond any specific stack. Any system where AI agents generate configuration, content, or code has the same entropy problem. The solution is always the same triad: **schema** (define what you track), **signal** (instrument everything), **auto-improve** (close the loop).

The goal isn't just monitoring. It's **recursive self-improvement**: the tool that improves the system should also be able to improve itself. Track dashboard usage. Auto-tune confidence thresholds based on false-positive rates. Propose UI improvements based on which filters and tabs users actually interact with.

When the improver can improve itself, you've built something that gets better at getting better.

**Tags**: ai-infrastructure, self-improving-systems, auto-improvement, python, fastapi, postgresql, devops
**Categories**: AI Automation, Engineering