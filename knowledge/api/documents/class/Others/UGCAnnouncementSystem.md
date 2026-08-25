---
id: "api:class:UGCAnnouncementSystem"
title: "UGCAnnouncementSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCAnnouncementSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCAnnouncementSystem

UGC公告系统

## Functions

### `GetLatestAnnouncements`

```text
GetLatestAnnouncements() -> PromiseFuture
```

发起异步请求获取最新的公告列表（最新的5个公告）
参考用法：
```lua
local PF = UGCAnnouncementSystem.GetLatestAnnouncements()
PF:Then(function (PromiseFuture) local Announcements = PromiseFuture:Get() end)
PF:Else(function (PromiseFuture) print("[UGCAnnouncementSystem.GetLatestAnnouncements] Failed, timeout") end)
```
Announcements结构为Lua数组
```
Announcements = {{Title:string, Content:string, EffectiveTime:number, bTop:boolean}, ...}
```
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 如果上一次请求未完成，则返回上一次请求的 PromiseFuture，否则返回新的 PromiseFuture |

## Language

`lua`
