---
id: "api:class:PlayerListManager"
title: "PlayerListManager"
source: "https://developer.gp.qq.com/api/class/detail/Others/PlayerListManager.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# PlayerListManager

玩家列表全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerListManager.PlayerListUpdateDelegate` | `-` | 玩家列表数据更新委托<br>生效范围：客户端<br>@param PlayerListData FPlayerListEntry[] @排序后的玩家列表 |

## Functions

### `UpdatePlayerSortValue`

```text
UpdatePlayerSortValue(PlayerController: BP_UGCPlayerController_C, UID: number, SortValue: number) -> boolean
```

更新排序属性值
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `UID` | `number` | 玩家UID |
| `SortValue` | `number` | 排序数值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否更新成功 |

### `UpdatePlayerDisplayValue`

```text
UpdatePlayerDisplayValue(PlayerController: BP_UGCPlayerController_C, UID: number, DisplayValue: number) -> boolean
```

更新展示属性值
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `UID` | `number` | 玩家UID |
| `DisplayValue` | `number` | 展示数值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否更新成功 |

### `GetPlayerListData`

```text
GetPlayerListData() -> FPlayerListEntry[]
```

获取排序后的玩家列表
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FPlayerListEntry[]` | 排序后的玩家列表 |

### `GetPlayerListConfig`

```text
GetPlayerListConfig() -> FPlayerListConfig
```

获取玩家列表配置
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FPlayerListConfig` | - |

## Language

`lua`
