---
id: "api:class:UGCPlayerStateSystem"
title: "UGCPlayerStateSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCPlayerStateSystem.json"
category: "API Wiki/class/和平全局接口/角色系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCPlayerStateSystem

玩家数据/状态系统接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCPlayerStateSystem._CrossPlayerChunkDataCallbacks` | `-` | - |
| `UGCPlayerStateSystem._CrossPlayerChunkDataRequestID` | `-` | - |

## Functions

### `IsAlive`

```text
IsAlive(PlayerKey: number) -> boolean
```

是否存活
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `IsExit`

```text
IsExit(PlayerKey: number) -> boolean
```

是否离开游戏（主动退出，非断线）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetUGCVIPLevel`

```text
GetUGCVIPLevel(PlayerKey: number) -> number
```

获取 VIP Level
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPlayerAccountInfo`

```text
GetPlayerAccountInfo(PlayerKey: number) -> FPlayerAccountInfo
```

获取玩家的账号数据
生效范围：服务器 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `FPlayerAccountInfo` | - |

### `GetPlayerBattleInfo`

```text
GetPlayerBattleInfo(PlayerKey: number) -> FPlayerBattleInfo
```

获取玩家的战斗数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `FPlayerBattleInfo` | - |

### `SavePlayerArchiveData`

```text
SavePlayerArchiveData(UID: number, ArchiveData: table) -> boolean
```

保存玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）!!!!注意，不能在对局结算之后保存存档数据，在对局结算后调用此接口无法成功保存存档数据
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |
| `ArchiveData` | `table` | 存档数据 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `SavePlayerArchiveDataByKey`

```text
SavePlayerArchiveDataByKey(UID: number, Key: string, Value: any) -> boolean
```

按key保存玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |
| `Key` | `string` | 要保存的键名 |
| `Value` | `any` | 要保存的值 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetPlayerArchiveData`

```text
GetPlayerArchiveData(UID: number) -> table
```

获取玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `table` | 存档数据 |

### `GetPlayerArchiveDataByKey`

```text
GetPlayerArchiveDataByKey(UID: number, Key: string) -> any
```

按key获取玩家存档数据（存档数据在 PIE 下无法跨对局保存和读取）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |
| `Key` | `string` | 要获取的键名 |

**Returns**

| Type | Description |
|---|---|
| `any` | 对应key的值，key不存在时返回nil |

### `GetTableDataSize`

```text
GetTableDataSize(Data: table) -> number
```

计算Lua table序列化后的字节大小
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `table` | 要计算大小的table |

**Returns**

| Type | Description |
|---|---|
| `number` | 序列化后的字节大小，计算失败返回-1 |

### `GetPlayerDataSize`

```text
GetPlayerDataSize(UID: number) -> number
```

获取玩家存档数据的总字节大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number` | 存档数据的总字节大小，无数据时返回0 |

### `ClearPlayerArchiveData`

```text
ClearPlayerArchiveData()
```

清理玩家存档数据（GM 指令，仅开发环境生效）
生效范围：客户端

### `GetPlayerPlatformGender`

```text
GetPlayerPlatformGender(PlatformGender: number, UID: number) -> number
```

获取玩家账号性别
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlatformGender` | `number` | 从DS获取的玩家性别 |
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家账号性别，0 - 隐藏，1 - 男，2 - 女 |

### `GetTeamID`

```text
GetTeamID(PlayerKey: number) -> number
```

获取 TeamID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPlayerKeyInt64`

```text
GetPlayerKeyInt64(PlayerState: PlayerState) -> number
```

获取 64 位玩家 PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `PlayerState` | - |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetPlayerKey`

```text
GetPlayerKey(PlayerState: PlayerState) -> string
```

获取字符串玩家 PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `PlayerState` | - |

**Returns**

| Type | Description |
|---|---|
| `string` | - |

## Language

`lua`
