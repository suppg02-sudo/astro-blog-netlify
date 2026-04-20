---
pubDatetime: 2026-04-20T21:30:00Z
title: "Building a Unified Content Pipeline: From 11 Chaotic Pipelines to One Orchestrated System"
postSlug: "building-unified-content-pipeline"
description: "How we consolidated 11 independent content pipelines into one unified architecture with Kestra orchestration, Directus CMS, and Netlify CDN distribution."
tags:
  - content-pipeline
  - kestra
  - directus
  - netlify
  - astro
  - architecture
---

# Building a Unified Content Pipeline: From 11 Chaotic Pipelines to One Orchestrated System

What happens when your AI infrastructure accumulates 11 independent content pipelines — blog publishing, YouTube summaries, research digests, news aggregation, scraping, auto-improvement reports — each with its own entry point, its own publishing mechanism, and its own idea of what "done" looks like?

You get chaos. Posts duplicated across systems. Hugo references in an Astro codebase. Manual steps that should be automated. And zero visibility into what published, what failed, and what fell through the cracks.

This is the story of how we consolidated all of it into a single unified content pipeline architecture — with Kestra orchestration, Directus as the single content store, and Netlify CDN for global distribution.

<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHZpZXdCb3g9JzAgMCA5MDAgNTIwJz4KPGRlZnM+CiAgPGxpbmVhckdyYWRpZW50IGlkPSdiZycgeDE9JzAnIHkxPScwJyB4Mj0nMScgeTI9JzEnPjxzdG9wIG9mZnNldD0nMCUnIHN0b3AtY29sb3I9JyMwYTAwMjAnLz48c3RvcCBvZmZzZXQ9JzEwMCUnIHN0b3AtY29sb3I9JyMxYTBhM2EnLz48L2xpbmVhckdyYWRpZW50PgogIDxmaWx0ZXIgaWQ9J2dsb3cnPjxmZUdhdXNzaWFuQmx1ciBzdGREZXZpYXRpb249JzInIHJlc3VsdD0nYmx1cicvPjxmZU1lcmdlPjxmZU1lcmdlTm9kZSBpbj0nYmx1cicvPjxmZU1lcmdlTm9kZSBpbj0nU291cmNlR3JhcGhpYycvPjwvZmVNZXJnZT48L2ZpbHRlcj4KPC9kZWZzPgo8cmVjdCB3aWR0aD0nOTAwJyBoZWlnaHQ9JzUyMCcgZmlsbD0ndXJsKCNiZyknIHJ4PScxMicvPgo8dGV4dCB4PSc0NTAnIHk9JzMwJyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjMDBmZmZmJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzE0JyBmb250LXdlaWdodD0nYm9sZCcgZmlsdGVyPSd1cmwoI2dsb3cpJz5VTklGSUVEIENPTlRFTlQgUElQRUxJTkUgQVJDSElURUNUVVJFPC90ZXh0Pgo8cmVjdCB4PScyMCcgeT0nNTAnIHdpZHRoPScxMzAnIGhlaWdodD0nMTgwJyByeD0nOCcgZmlsbD0nbm9uZScgc3Ryb2tlPScjZmY0MDgxJyBzdHJva2Utd2lkdGg9JzEuNScgc3Ryb2tlLWRhc2hhcnJheT0nNCwyJy8+Cjx0ZXh0IHg9Jzg1JyB5PSc2OCcgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmNDA4MScgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPScxMCcgZm9udC13ZWlnaHQ9J2JvbGQnPlNPVVJDRVM8L3RleHQ+CjxyZWN0IHg9JzMwJyB5PSc3OCcgd2lkdGg9JzExMCcgaGVpZ2h0PScyNicgcng9JzQnIGZpbGw9JyNmZjQwODEnIGZpbGwtb3BhY2l0eT0nMC4xNScvPjx0ZXh0IHg9Jzg1JyB5PSc5NScgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmNDA4MScgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc5Jz5Zb3VUdWJlIFVSTHM8L3RleHQ+CjxyZWN0IHg9JzMwJyB5PScxMTAnIHdpZHRoPScxMTAnIGhlaWdodD0nMjYnIHJ4PSc0JyBmaWxsPScjZmY0MDgxJyBmaWxsLW9wYWNpdHk9JzAuMTUnLz48dGV4dCB4PSc4NScgeT0nMTI3JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmY0MDgxJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzknPmVSQUcgUmVzZWFyY2g8L3RleHQ+CjxyZWN0IHg9JzMwJyB5PScxNDInIHdpZHRoPScxMTAnIGhlaWdodD0nMjYnIHJ4PSc0JyBmaWxsPScjZmY0MDgxJyBmaWxsLW9wYWNpdHk9JzAuMTUnLz48dGV4dCB4PSc4NScgeT0nMTU5JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmY0MDgxJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzknPk5ld3MgLyBSU1M8L3RleHQ+CjxyZWN0IHg9JzMwJyB5PScxNzQnIHdpZHRoPScxMTAnIGhlaWdodD0nMjYnIHJ4PSc0JyBmaWxsPScjZmY0MDgxJyBmaWxsLW9wYWNpdHk9JzAuMTUnLz48dGV4dCB4PSc4NScgeT0nMTkxJyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmY0MDgxJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzknPlRlbGVncmFtIEJvdDwvdGV4dD4KPGxpbmUgeDE9JzE1NScgeTE9JzE0MCcgeDI9JzIxMCcgeTI9JzE0MCcgc3Ryb2tlPScjMDBmZmZmJyBzdHJva2Utd2lkdGg9JzInLz4KPHJlY3QgeD0nMjE1JyB5PSc1MCcgd2lkdGg9JzE2MCcgaGVpZ2h0PSc0MjAnIHJ4PSc4JyBmaWxsPSdub25lJyBzdHJva2U9JyMwMGZmZmYnIHN0cm9rZS13aWR0aD0nMicvPgo8dGV4dCB4PScyOTUnIHk9JzY4JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjMDBmZmZmJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzEwJyBmb250LXdlaWdodD0nYm9sZCcgZmlsdGVyPSd1cmwoI2dsb3cpJz5LRVNUUkEgRU5HSU5FPC90ZXh0Pgo8cmVjdCB4PScyMjUnIHk9Jzc4JyB3aWR0aD0nMTQwJyBoZWlnaHQ9JzM0JyByeD0nNCcgZmlsbD0nIzAwZmZmZicgZmlsbC1vcGFjaXR5PScwLjEnLz48dGV4dCB4PScyOTUnIHk9Jzk4JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjMDBmZmZmJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPkNsYXNzaWZ5IElucHV0PC90ZXh0Pgo8cmVjdCB4PScyMjUnIHk9JzEyMCcgd2lkdGg9JzE0MCcgaGVpZ2h0PSczNCcgcng9JzQnIGZpbGw9JyMwMGZmZmYnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nMjk1JyB5PScxNDAnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyMwMGZmZmYnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+UXVhbGl0eSBHYXRlPC90ZXh0Pgo8cmVjdCB4PScyMjUnIHk9JzE2Micgd2lkdGg9JzE0MCcgaGVpZ2h0PSczNCcgcng9JzQnIGZpbGw9JyMwMGZmZmYnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nMjk1JyB5PScxODInIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyMwMGZmZmYnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+RGVkdXAgQ2hlY2s8L3RleHQ+CjxyZWN0IHg9JzIyNScgeT0nMjA0JyB3aWR0aD0nMTQwJyBoZWlnaHQ9JzM0JyByeD0nNCcgZmlsbD0nIzAwZmZmZicgZmlsbC1vcGFjaXR5PScwLjEnLz48dGV4dCB4PScyOTUnIHk9JzIyNCcgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nIzAwZmZmZicgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc4Jz5TRU8gRW5yaWNoPC90ZXh0Pgo8cmVjdCB4PScyMjUnIHk9JzI0Nicgd2lkdGg9JzE0MCcgaGVpZ2h0PSczNCcgcng9JzQnIGZpbGw9JyNiMzg4ZmYnIGZpbGwtb3BhY2l0eT0nMC4xNScgc3Ryb2tlPScjYjM4OGZmJyBzdHJva2Utd2lkdGg9JzEnLz48dGV4dCB4PScyOTUnIHk9JzI2NicgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2IzODhmZicgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc4Jz5QdWJsaXNoPC90ZXh0Pgo8cmVjdCB4PScyMjUnIHk9JzI4OCcgd2lkdGg9JzE0MCcgaGVpZ2h0PSczNCcgcng9JzQnIGZpbGw9JyNiMzg4ZmYnIGZpbGwtb3BhY2l0eT0nMC4xNScgc3Ryb2tlPScjYjM4OGZmJyBzdHJva2Utd2lkdGg9JzEnLz48dGV4dCB4PScyOTUnIHk9JzMwOCcgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2IzODhmZicgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc4Jz5SZXB1cnBvc2U8L3RleHQ+CjxyZWN0IHg9JzIyNScgeT0nMzMwJyB3aWR0aD0nMTQwJyBoZWlnaHQ9JzM0JyByeD0nNCcgZmlsbD0nI2IzODhmZicgZmlsbC1vcGFjaXR5PScwLjE1JyBzdHJva2U9JyNiMzg4ZmYnIHN0cm9rZS13aWR0aD0nMScvPjx0ZXh0IHg9JzI5NScgeT0nMzUwJyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjYjM4OGZmJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPlJlYnVpbGQ8L3RleHQ+CjxyZWN0IHg9JzIyNScgeT0nMzcyJyB3aWR0aD0nMTQwJyBoZWlnaHQ9JzM0JyByeD0nNCcgZmlsbD0nIzAwZmY0MScgZmlsbC1vcGFjaXR5PScwLjEnIHN0cm9rZT0nIzAwZmY0MScgc3Ryb2tlLXdpZHRoPScxJy8+PHRleHQgeD0nMjk1JyB5PSczOTInIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyMwMGZmNDEnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+Tm90aWZ5PC90ZXh0Pgo8cmVjdCB4PScyMjUnIHk9JzQxNCcgd2lkdGg9JzE0MCcgaGVpZ2h0PSczNCcgcng9JzQnIGZpbGw9JyMwMGZmNDEnIGZpbGwtb3BhY2l0eT0nMC4xJyBzdHJva2U9JyMwMGZmNDEnIHN0cm9rZS13aWR0aD0nMScvPjx0ZXh0IHg9JzI5NScgeT0nNDM0JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjMDBmZjQxJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPkFuYWx5dGljczwvdGV4dD4KPGxpbmUgeDE9JzM4MCcgeTE9JzE4MCcgeDI9JzQ0MCcgeTI9JzE4MCcgc3Ryb2tlPScjZmYwMGZmJyBzdHJva2Utd2lkdGg9JzInLz4KPHJlY3QgeD0nNDQ1JyB5PSc1MCcgd2lkdGg9JzE1MCcgaGVpZ2h0PScyMDAnIHJ4PSc4JyBmaWxsPSdub25lJyBzdHJva2U9JyNmZjAwZmYnIHN0cm9rZS13aWR0aD0nMicvPgo8dGV4dCB4PSc1MjAnIHk9JzY4JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmYwMGZmJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzEwJyBmb250LXdlaWdodD0nYm9sZCcgZmlsdGVyPSd1cmwoI2dsb3cpJz5ESVJFQ1RVUyBDTVM8L3RleHQ+CjxyZWN0IHg9JzQ1NScgeT0nNzgnIHdpZHRoPScxMzAnIGhlaWdodD0nMjYnIHJ4PSc0JyBmaWxsPScjZmYwMGZmJyBmaWxsLW9wYWNpdHk9JzAuMScvPjx0ZXh0IHg9JzUyMCcgeT0nOTUnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyNmZjAwZmYnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+cG9zdHMgKDExNjQpPC90ZXh0Pgo8cmVjdCB4PSc0NTUnIHk9JzExMCcgd2lkdGg9JzEzMCcgaGVpZ2h0PScyNicgcng9JzQnIGZpbGw9JyNmZjAwZmYnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nNTIwJyB5PScxMjcnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyNmZjAwZmYnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+Y29udGVudF9xdWV1ZTwvdGV4dD4KPHJlY3QgeD0nNDU1JyB5PScxNDInIHdpZHRoPScxMzAnIGhlaWdodD0nMjYnIHJ4PSc0JyBmaWxsPScjZmYwMGZmJyBmaWxsLW9wYWNpdHk9JzAuMScvPjx0ZXh0IHg9JzUyMCcgeT0nMTU5JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmYwMGZmJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPnBpcGVsaW5lX2xvZ3M8L3RleHQ+CjxyZWN0IHg9JzQ1NScgeT0nMTc0JyB3aWR0aD0nMTMwJyBoZWlnaHQ9JzI2JyByeD0nNCcgZmlsbD0nI2ZmMDBmZicgZmlsbC1vcGFjaXR5PScwLjEnLz48dGV4dCB4PSc1MjAnIHk9JzE5MScgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmMDBmZicgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc4Jz5jb250ZW50X3ZhcmlhbnRzPC90ZXh0Pgo8cmVjdCB4PSc0NTUnIHk9JzIwNicgd2lkdGg9JzEzMCcgaGVpZ2h0PScyNicgcng9JzQnIGZpbGw9JyNmZjAwZmYnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nNTIwJyB5PScyMjMnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyNmZjAwZmYnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+dmlld19ldmVudHM8L3RleHQ+CjxsaW5lIHgxPSc2MDAnIHkxPScxNTAnIHgyPSc2NjAnIHkyPScxNTAnIHN0cm9rZT0nIzAwZmY0MScgc3Ryb2tlLXdpZHRoPScyJy8+CjxyZWN0IHg9JzY2NScgeT0nNTAnIHdpZHRoPScyMTUnIGhlaWdodD0nMjAwJyByeD0nOCcgZmlsbD0nbm9uZScgc3Ryb2tlPScjMDBmZjQxJyBzdHJva2Utd2lkdGg9JzInLz4KPHRleHQgeD0nNzcyJyB5PSc2OCcgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nIzAwZmY0MScgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPScxMCcgZm9udC13ZWlnaHQ9J2JvbGQnIGZpbHRlcj0ndXJsKCNnbG93KSc+RElTVFJJQlVUSU9OPC90ZXh0Pgo8cmVjdCB4PSc2NzUnIHk9Jzc4JyB3aWR0aD0nMTk1JyBoZWlnaHQ9JzM0JyByeD0nNCcgZmlsbD0nIzAwZmY0MScgZmlsbC1vcGFjaXR5PScwLjEnLz48dGV4dCB4PSc3NzInIHk9Jzk4JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjMDBmZjQxJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPkFzdHJvIEludGVybmFsICg6MzAwMikgU1NSPC90ZXh0Pgo8cmVjdCB4PSc2NzUnIHk9JzEyMCcgd2lkdGg9JzE5NScgaGVpZ2h0PSczNCcgcng9JzQnIGZpbGw9JyMwMGZmNDEnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nNzcyJyB5PScxNDAnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyMwMGZmNDEnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+TmV0bGlmeSBDRE4gKDExMzMgcG9zdHMpPC90ZXh0Pgo8cmVjdCB4PSc2NzUnIHk9JzE2Micgd2lkdGg9JzE5NScgaGVpZ2h0PSczNCcgcng9JzQnIGZpbGw9JyMwMGZmNDEnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nNzcyJyB5PScxODInIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyMwMGZmNDEnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+VGVsZWdyYW0gTm90aWZpY2F0aW9uczwvdGV4dD4KPHJlY3QgeD0nNjc1JyB5PScyMDQnIHdpZHRoPScxOTUnIGhlaWdodD0nMzQnIHJ4PSc0JyBmaWxsPScjMDBmZjQxJyBmaWxsLW9wYWNpdHk9JzAuMScvPjx0ZXh0IHg9Jzc3MicgeT0nMjI0JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjMDBmZjQxJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPlNvY2lhbCBWYXJpYW50cyAoVHdpdHRlci9MaW5rZWRJbik8L3RleHQ+CjxyZWN0IHg9JzQ0NScgeT0nMjcwJyB3aWR0aD0nNDMwJyBoZWlnaHQ9JzIwMCcgcng9JzgnIGZpbGw9J25vbmUnIHN0cm9rZT0nI2ZmYWIwMCcgc3Ryb2tlLXdpZHRoPScxLjUnIHN0cm9rZS1kYXNoYXJyYXk9JzYsMycvPgo8dGV4dCB4PSc2NjAnIHk9JzI5MCcgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmYWIwMCcgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPScxMCcgZm9udC13ZWlnaHQ9J2JvbGQnPjcgS0VTVFJBIFdPUktGTE9XUzwvdGV4dD4KPHJlY3QgeD0nNDYwJyB5PSczMDAnIHdpZHRoPScxOTAnIGhlaWdodD0nMjQnIHJ4PSc0JyBmaWxsPScjZmZhYjAwJyBmaWxsLW9wYWNpdHk9JzAuMScvPjx0ZXh0IHg9JzU1NScgeT0nMzE2JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmZhYjAwJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPnlvdXR1YmUtdG8tYmxvZyAobWFudWFsKTwvdGV4dD4KPHJlY3QgeD0nNDYwJyB5PSczMzAnIHdpZHRoPScxOTAnIGhlaWdodD0nMjQnIHJ4PSc0JyBmaWxsPScjZmZhYjAwJyBmaWxsLW9wYWNpdHk9JzAuMScvPjx0ZXh0IHg9JzU1NScgeT0nMzQ2JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmZhYjAwJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPmV2b2x2ZS10by1ibG9nIChkYWlseSAxOTowMCk8L3RleHQ+CjxyZWN0IHg9JzQ2MCcgeT0nMzYwJyB3aWR0aD0nMTkwJyBoZWlnaHQ9JzI0JyByeD0nNCcgZmlsbD0nI2ZmYWIwMCcgZmlsbC1vcGFjaXR5PScwLjEnLz48dGV4dCB4PSc1NTUnIHk9JzM3NicgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmYWIwMCcgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc4Jz5yZXNlYXJjaC10by1ibG9nIChtYW51YWwpPC90ZXh0Pgo8cmVjdCB4PSc0NjAnIHk9JzM5MCcgd2lkdGg9JzE5MCcgaGVpZ2h0PScyNCcgcng9JzQnIGZpbGw9JyNmZmFiMDAnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nNTU1JyB5PSc0MDYnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyNmZmFiMDAnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+bmV3cy10by1ibG9nIChkYWlseSAwODowMCk8L3RleHQ+CjxyZWN0IHg9JzY3MCcgeT0nMzAwJyB3aWR0aD0nMTkwJyBoZWlnaHQ9JzI0JyByeD0nNCcgZmlsbD0nI2ZmYWIwMCcgZmlsbC1vcGFjaXR5PScwLjEnLz48dGV4dCB4PSc3NjUnIHk9JzMxNicgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nI2ZmYWIwMCcgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc4Jz5zY3JhcGUtdG8tYmxvZyAobWFudWFsKTwvdGV4dD4KPHJlY3QgeD0nNjcwJyB5PSczMzAnIHdpZHRoPScxOTAnIGhlaWdodD0nMjQnIHJ4PSc0JyBmaWxsPScjZmZhYjAwJyBmaWxsLW9wYWNpdHk9JzAuMScvPjx0ZXh0IHg9Jzc2NScgeT0nMzQ2JyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjZmZhYjAwJyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzgnPmNvbnRlbnQtcmVwdXJwb3NlIChtYW51YWwpPC90ZXh0Pgo8cmVjdCB4PSc2NzAnIHk9JzM2MCcgd2lkdGg9JzE5MCcgaGVpZ2h0PScyNCcgcng9JzQnIGZpbGw9JyNmZmFiMDAnIGZpbGwtb3BhY2l0eT0nMC4xJy8+PHRleHQgeD0nNzY1JyB5PSczNzYnIHRleHQtYW5jaG9yPSdtaWRkbGUnIGZpbGw9JyNmZmFiMDAnIGZvbnQtZmFtaWx5PSdtb25vc3BhY2UnIGZvbnQtc2l6ZT0nOCc+bmV0bGlmeS1zeW5jIChkYWlseSAwMzowMCk8L3RleHQ+CjxyZWN0IHg9JzQ2MCcgeT0nNDMwJyB3aWR0aD0nNDAwJyBoZWlnaHQ9JzMwJyByeD0nNCcgZmlsbD0nIzAwYmZhNScgZmlsbC1vcGFjaXR5PScwLjEnIHN0cm9rZT0nIzAwYmZhNScgc3Ryb2tlLXdpZHRoPScxJy8+Cjx0ZXh0IHg9JzY2MCcgeT0nNDUwJyB0ZXh0LWFuY2hvcj0nbWlkZGxlJyBmaWxsPScjMDBiZmE1JyBmb250LWZhbWlseT0nbW9ub3NwYWNlJyBmb250LXNpemU9JzknIGZvbnQtd2VpZ2h0PSdib2xkJz5HcmFmYW5hIERhc2hib2FyZDogMTAgUGFuZWxzICsgQW5hbHl0aWNzPC90ZXh0Pgo8cmVjdCB4PScyMTUnIHk9JzQ0MCcgd2lkdGg9JzE2MCcgaGVpZ2h0PSczMCcgcng9JzQnIGZpbGw9JyMzYjgyZjYnIGZpbGwtb3BhY2l0eT0nMC4xJyBzdHJva2U9JyMzYjgyZjYnIHN0cm9rZS13aWR0aD0nMScvPgo8dGV4dCB4PScyOTUnIHk9JzQ2MCcgdGV4dC1hbmNob3I9J21pZGRsZScgZmlsbD0nIzNiODJmNicgZm9udC1mYW1pbHk9J21vbm9zcGFjZScgZm9udC1zaXplPSc5JyBmb250LXdlaWdodD0nYm9sZCc+U2hhcmVkIFRhc2sgTGlicmFyeSAoMTAgbW9kdWxlcyk8L3RleHQ+Cjwvc3ZnPg==" alt="Unified Content Pipeline Architecture" style="display:block;width:100%;max-width:700px;height:auto;margin:1.5rem auto;">

## The Problem: Pipeline Sprawl

Before this project, content flowed through at least 11 independent paths:

- **Telegram bot** published blog posts by writing Hugo markdown files and running `hugo --minify`
- **YouTube pipeline** transcribed videos and published via a dedicated script
- **Research pipeline** created posts from eRAG deep dives
- **News aggregator** ran RSS feeds through scoring and published daily digests
- **Scraping pipeline** processed URLs into blog content
- **Auto-improvement** (evolve) reports were generated but rarely published

Each pipeline had different quality standards, different publish targets, and no shared state. There was no content queue, no deduplication, and no way to track what happened to a piece of content after it entered the system.

The biggest problem: the Telegram bot was still writing to Hugo, but the blog had migrated to Astro + Directus months ago. Three publish points in the bot code were calling Hugo commands that no longer did anything useful.

## The Architecture: Four Layers

The solution breaks into four clean layers, each with a single responsibility:

**Layer 1: Sources** — YouTube URLs, research topics, RSS feeds, Telegram commands, scraped URLs. Each source produces a content input (title, body, metadata) but doesn't know anything about publishing.

**Layer 2: Orchestration** — Kestra is the brain. Seven workflows handle the full lifecycle: classify input, quality gate, dedup check, SEO enrichment, publish, repurpose, rebuild, notify, and track analytics. Every workflow follows the same pattern — only the input classification changes.

**Layer 3: Content Store** — Directus is the single source of truth. Five collections hold everything: `posts` (1164 published), `content_queue` (pipeline state tracking), `pipeline_logs` (execution history), `content_variants` (social media repurposing), and `view_events` (analytics).

**Layer 4: Distribution** — Content fans out to Astro Internal (port 3002, SSR, all posts), Netlify CDN (public-only, static, 1133 posts synced), Telegram notifications, and social media variants (Twitter threads, LinkedIn posts, newsletter excerpts).

## Phase 1: Foundation (Fixing the Plumbing)

The first phase was unglamorous but critical — stopping the bleeding.

### Telegram Bot Detox

The bot had three Hugo publish points (research, news, YouTube) and two Hugo-dependent functions (blog list, blog delete). All five were rewritten to use the Directus API. A new `_publish_to_directus()` helper function replaced the Hugo workflow, and the bot now publishes via our shared script with pipeline provenance tracking.

### Enhanced Publish Script

The existing `publish_to_directus.py` only accepted file paths. We added a `direct` mode that takes title, content, tags, and pipeline metadata as CLI arguments — no file needed. This is what the Kestra workflows call.

### Directus Collections

Two new collections were created: `content_queue` (13 fields tracking pipeline state from `received` through `published` or `failed`) and `pipeline_logs` (8 fields for execution history). These give us full observability over every piece of content that enters the system.

### Grafana Dashboard

A 10-panel Grafana dashboard at http://ubuntu4:3003/d/content-pipeline/ shows content items by status, pipeline throughput, failure rates, average time to publish, total posts, breakdowns by source pipeline, top posts by views, page views over time, content variants by type, and referrer analytics.

## Phase 2: Orchestration (The Brain)

With the plumbing fixed, we built the shared task library and Kestra workflows.

### Shared Task Library

Ten Python modules live in `/root/scripts/pipeline-tasks/`: config, content_queue, classify, enrich, quality_gate, publish, notify, rebuild, dedup, and repurpose. Each module does one thing and is independently testable. Six unit tests all pass.

### Seven Kestra Workflows

Every workflow follows the same pattern: create queue entry → quality gate → dedup → enrich → publish → rebuild → notify. What changes is the input classification and whether content auto-publishes or goes to draft for human review.

| Workflow | Trigger | Auto-Publish? |
|----------|---------|---------------|
| youtube-to-blog | Manual (URL input) | Yes |
| evolve-to-blog | Daily 19:00 UTC | Yes |
| research-to-blog | Manual (topic input) | No — draft for review |
| news-to-blog | Daily 08:00 UTC | No — draft for review |
| scrape-to-blog | Manual (URL input) | Yes |
| content-repurpose | Manual (post ID/slug) | N/A — generates variants |
| netlify-sync | Daily 03:00 UTC | N/A — syncs to CDN |

The editorial decision is deliberate: YouTube, evolve, and scrape content auto-publishes because it's machine-generated from known sources. Research and news go to draft because they benefit from human review before going public.

## Phase 3: Distribution (Reaching the World)

### Netlify CDN Sync

This was the trickiest part. Directus stores tags as JSON arrays, and the `_contains` filter operator doesn't work on JSON fields — it silently returns zero results. The solution was a Python sync script that fetches all published posts, filters for the `public` tag client-side, and writes markdown files to the Netlify GitHub repo.

The script handles pagination (1164 posts in batches of 100), generates proper Astro frontmatter, and auto-pushes to GitHub where Netlify picks it up. 1133 public posts are now live on the CDN.

### Content Repurposing

The `repurpose.py` module takes any published post and generates three variants: a Twitter thread (extracting key points into numbered tweets), a LinkedIn post (professional tone with bullet takeaways), and a newsletter excerpt (with CTA). Variants are stored in the `content_variants` Directus collection for reuse.

### SEO Metadata Enrichment

Every post gets automatic keyword extraction (frequency-based bigram analysis), JSON-LD Article structured data, Open Graph meta tags, and canonical URLs. The `enrich.py` module runs before publish in all workflows.

### Analytics and Consulting Funnel

A simple PostgreSQL-based view counter records slug, referrer, and user agent. The Grafana dashboard includes four analytics panels (top posts, views over time, variants by type, referrer breakdown). A consulting CTA generator produces styled HTML snippets for embedding in relevant posts.

## What This Enables

This isn't just a technical cleanup — it's a content machine:

- **One input, multiple outputs**: Drop a YouTube URL into Kestra and get a blog post, Twitter thread, LinkedIn post, and newsletter excerpt — all tracked, all deduplicated.
- **Full observability**: Every piece of content has a lifecycle in `content_queue`. You can see what's pending, what published, and what failed — with error messages.
- **Automated distribution**: Netlify CDN sync runs daily at 03:00 UTC. The internal Astro blog rebuilds on publish. Nothing falls through the cracks.
- **Monetisation ready**: The consulting CTA generator and analytics tracking support the income-generation goal. We can see which posts get traffic and which topics drive engagement.

## The Numbers

| Metric | Value |
|--------|-------|
| Total published posts | 1,164 |
| Public posts on Netlify CDN | 1,133 |
| Kestra workflows | 7 (3 scheduled, 4 manual) |
| Pipeline task modules | 10 |
| Directus collections | 5 |
| Grafana dashboard panels | 10 |
| Unit tests passing | 6/6 |

## Lessons Learned

1. **API filter operators lie**: Directus `_contains` doesn't work on JSON fields. Client-side filtering is the reliable approach.
2. **Disk space is a pipeline dependency**: Kestra's Docker image is 2.6GB. We had to clean up 9GB of unused images before we could pull it.
3. **Git credentials don't survive container restarts**: The sync script needed `gh auth token` injection at runtime.
4. **Permissions are invisible until they block you**: New Directus collections need explicit permissions added via PostgreSQL — the API token can't self-authorise.
5. **Naming matters**: A file called `queue.py` in Python path shadows the stdlib `queue` module. Renamed to `content_queue.py`.

## What's Next

The pipeline is live and operational. Next steps:

- Wire the YouTube transcription skill into the `youtube-to-blog` Kestra workflow
- Add Umami analytics for privacy-first visitor tracking
- Create a Directus webhook that triggers the Netlify sync workflow on post publish (instead of waiting for the daily cron)
- Build a "best of" digest that auto-generates weekly roundup posts from top-viewed content

**Tags**: content-pipeline, kestra, directus, netlify, astro, architecture, orchestration
