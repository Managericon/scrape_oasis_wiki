---
id: "api:class:PlayerProfileManagerPlayerComponent"
title: "PlayerProfileManagerPlayerComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/PlayerProfileManagerPlayerComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# PlayerProfileManagerPlayerComponent

玩家档案玩家组件

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerProfileManagerPlayerComponent.OnPlayerProfileOpen` | `-` | 玩家档案打开委托<br>生效范围：客户端<br>@param UID number @玩家 UID<br>@param IconURL string @玩家头像 URL<br>@param NickName string @玩家昵称<br>@param PlatformGender number @玩家性别（0=未知，1=男，2=女）<br>@param bIsOnline boolean @玩家是否在线 |

## Functions

### `RequestPlayerProfile`

```text
RequestPlayerProfile(TargetUID: number)
```

请求打开指定 UID 的玩家档案
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetUID` | `number` | 目标玩家 UID |

## Language

`lua`
