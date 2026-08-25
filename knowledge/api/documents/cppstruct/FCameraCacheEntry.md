---
id: "api:cppstruct:FCameraCacheEntry"
title: "FCameraCacheEntry"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCameraCacheEntry.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCameraCacheEntry

Cached camera POV info, stored as optimization so we only
  need to do a full camera update once per tick.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimeStamp` | `float` | World time this entry was created. |
| `POV` | `FMinimalViewInfo` | Camera POV to cache. |
