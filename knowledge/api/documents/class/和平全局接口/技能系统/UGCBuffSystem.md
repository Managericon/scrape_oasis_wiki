---
id: "api:class:UGCBuffSystem"
title: "UGCBuffSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCBuffSystem.json"
category: "API Wiki/class/和平全局接口/技能系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCBuffSystem

【废弃】Buff 系统接口库

## Functions

### `GetBuffSystemComponent`

```text
GetBuffSystemComponent(PlayerPawn: PlayerPawn) -> BuffSystemComponent
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色。所有的接口里的 PlayerPawn 都可以扩展成任意的 Actor，只要这个 Actor 有一个名字叫 BuffSystemComponent 的 Buff 组件即可。 |

**Returns**

| Type | Description |
|---|---|
| `BuffSystemComponent` | USTBaseBuffSystemComponent |

### `AddBuff`

```text
AddBuff(PlayerPawn: PlayerPawn, BuffName: string, LayerCount: number, BuffCauser: Controller, CauserActor: Actor) -> number
```

【废弃】请使用 UGCPersistEffectSystem
为玩家添加 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色。所有的接口里的 PlayerPawn 都可以扩展成任意的 Actor，只要这个 Actor 有一个名字叫 BuffSystemComponent 的 Buff 组件即可。 |
| `BuffName` | `string` | Buff 名 |
| `LayerCount` | `number` | 层数 |
| `BuffCauser` | `Controller` | 施加 Buff 的玩家或 AI 的控制器 |
| `CauserActor` | `Actor` | 施加 Buff 的 Actor，比如说 PlayerPawn、燃烧瓶 Actor 等等 |

**Returns**

| Type | Description |
|---|---|
| `number` | Buff 唯一 ID |

### `RemoveBuff`

```text
RemoveBuff(PlayerPawn: PlayerPawn, BuffName: string, LayerCount: number)
```

【废弃】请使用 UGCPersistEffectSystem
为玩家移除 Buff,本帧内不即时移除
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |
| `LayerCount` | `number` | 层数 |

### `RemoveBuffByInstanceID`

```text
RemoveBuffByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number, LayerCount: number)
```

【废弃】请使用 UGCPersistEffectSystem
使用唯一 ID 移除 Buff，本帧内不即时移除
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | Buff 唯一 ID |
| `LayerCount` | `number` | 层数 |

### `HasBuff`

```text
HasBuff(PlayerPawn: PlayerPawn, BuffName: string) -> boolean
```

【废弃】请使用 UGCPersistEffectSystem
是否存在该 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否存在 Buff |

### `GetCurLayer`

```text
GetCurLayer(PlayerPawn: PlayerPawn, BuffName: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 当前层数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `number` | 层数 |

### `GetMaxLayer`

```text
GetMaxLayer(PlayerPawn: PlayerPawn, BuffName: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 最大层数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大层数 |

### `GetLeftTime`

```text
GetLeftTime(PlayerPawn: PlayerPawn, BuffName: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 剩余持续时间
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `number` | 剩余持续时间 |

### `GetBuffCauserActor`

```text
GetBuffCauserActor(PlayerPawn: PlayerPawn, InstanceID: number) -> Actor
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 的施加者
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | Buff |
| `InstanceID` | `number` | Buff 唯一 ID |

**Returns**

| Type | Description |
|---|---|
| `Actor` | Buff 施加者（弱引用，需使用 Actor:Get() 获取实际对象） |

## Language

`lua`
