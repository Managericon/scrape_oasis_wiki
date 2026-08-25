---
id: "api:cppenum:GuideConfig.State"
title: "GuideConfig.State"
source: "https://developer.gp.qq.com/api/cppenum/detail/GuideConfig.State.json"
category: "API Wiki/cppenum"
kind: "cppenum"
api_root: "https://developer.gp.qq.com/api/"
---

# GuideConfig.State

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Idle` | `1` | - |
| `Active` | `2` | -- 空闲：等待触发 |
| `Completed` | `3` | -- 空闲：等待触发 -- 激活：正在显示 |
| `Disabled` | `4` | -- 空闲：等待触发 -- 激活：正在显示 -- 已完成（本次） |
| `Queued` | `5` | -- 空闲：等待触发 -- 激活：正在显示 -- 已完成（本次） -- 已禁用（达到完成上限） |
