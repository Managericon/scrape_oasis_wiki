---
id: "api:cppenum:EUGCUIState"
title: "EUGCUIState"
source: "https://developer.gp.qq.com/api/cppenum/detail/EUGCUIState.json"
category: "API Wiki/cppenum"
kind: "cppenum"
api_root: "https://developer.gp.qq.com/api/"
---

# EUGCUIState

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Unloaded` | `Unloaded` | - |
| `Loading` | `Loading` | 尚未加载或实例已销毁；未注册的 Key 也返回此状态 |
| `Cached` | `Cached` | 尚未加载或实例已销毁；未注册的 Key 也返回此状态  正在等待 PlayerController、加载类或创建实例 |
| `Open` | `Open` | 尚未加载或实例已销毁；未注册的 Key 也返回此状态  正在等待 PlayerController、加载类或创建实例  实例已缓存但未打开，包括预加载完成或关闭后保留的实例 |
