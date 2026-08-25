---
id: "api:class:UGCSkillManagerSystem"
title: "UGCSkillManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCSkillManagerSystem.json"
category: "API Wiki/class/和平全局接口/技能系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCSkillManagerSystem

【废弃】技能管理系统接口库

## Functions

### `GetSkillManagerComponent`

```text
GetSkillManagerComponent(Actor: Actor) -> SkillManagerComponent
```

【废弃】请使用 UGCPersistEffectSystem
获取技能组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |

**Returns**

| Type | Description |
|---|---|
| `SkillManagerComponent` | 技能组件 |

### `UseSkill`

```text
UseSkill(Actor: Actor, SkillName: string)
```

【废弃】请使用 UGCPersistEffectSystem
使用技能（技能列表中，技能需配置 SET_KEY_DOWN 事件触发）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillName` | `string` | 技能短名 |

### `StopSkill`

```text
StopSkill(Actor: Actor, SkillName: string)
```

【废弃】请使用 UGCPersistEffectSystem
停止技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillName` | `string` | 技能短名 |

### `TriggerSkillEvent`

```text
TriggerSkillEvent(Actor: Actor, SkillName: string, EventType: UTSkillEventType)
```

【废弃】请使用 UGCPersistEffectSystem
使用技能（自定义触发事件类型）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillName` | `string` | 技能短名 |
| `EventType` | `UTSkillEventType` | 事件类型 |

### `UseSkillByPath`

```text
UseSkillByPath(Actor: Actor, SkillPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
根据技能路径使用技能（技能列表中，技能需配置 SET_KEY_DOWN 事件触发）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |

### `StopSkillByPath`

```text
StopSkillByPath(Actor: Actor, SkillPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
根据技能路径停止技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |

### `TriggerSkillEventByPath`

```text
TriggerSkillEventByPath(Actor: Actor, SkillPath: string, EventType: UTSkillEventType)
```

【废弃】请使用 UGCPersistEffectSystem
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `EventType` | `UTSkillEventType` | 事件类型 |

### `StopAllSkill`

```text
StopAllSkill(Actor: Actor)
```

【废弃】请使用 UGCPersistEffectSystem
停止所有技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |

### `AddSkill`

```text
AddSkill(Actor: Actor, SkillClassPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
添加技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillClassPath` | `string` | 技能完整路径 |

### `RemoveSkill`

```text
RemoveSkill(Actor: Actor, SkillClassPath: string)
```

【废弃】请使用 UGCPersistEffectSystem
移除技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillClassPath` | `string` | 技能完整路径 |

### `IsSkillRunning`

```text
IsSkillRunning(Actor: Actor) -> boolean
```

【废弃】请使用 UGCPersistEffectSystem
当前是否有技能在执行
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否有技能在执行 |

### `GetSkillCD`

```text
GetSkillCD(Actor: Actor, SkillPath: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取技能冷却
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |

**Returns**

| Type | Description |
|---|---|
| `number` | 技能冷却时间 |

### `SetSkillActive`

```text
SetSkillActive(Actor: Actor, SkillPath: string, NewActive: boolean)
```

【废弃】请使用 UGCPersistEffectSystem
激活技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `NewActive` | `boolean` | 技能状态 |

### `TriggerStringEvent`

```text
TriggerStringEvent(Actor: Actor, SkillPath: string, EventString: string)
```

【废弃】请使用 UGCPersistEffectSystem
向技能抛出一个字符串类型的事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `EventString` | `string` | 字符串事件 |

### `TriggerUAEEvent`

```text
TriggerUAEEvent(Actor: Actor, SkillPath: string, EventType: UAESkillEvent)
```

【废弃】请使用 UGCPersistEffectSystem
向技能抛出一个预定义的事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | Actor 对象 |
| `SkillPath` | `string` | 技能完整路径 |
| `EventType` | `UAESkillEvent` | 预定义事件 |

## Language

`lua`
