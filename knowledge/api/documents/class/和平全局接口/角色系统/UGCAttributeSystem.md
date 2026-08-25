---
id: "api:class:UGCAttributeSystem"
title: "UGCAttributeSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCAttributeSystem.json"
category: "API Wiki/class/和平全局接口/角色系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCAttributeSystem

属性系统接口库

## Functions

### `GetGameAttributeValue`

```text
GetGameAttributeValue(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举) -> number
```

获取指定属性数值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Returns**

| Type | Description |
|---|---|
| `number` | 目标数值 |

### `SetGameAttributeValue`

```text
SetGameAttributeValue(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, Value: number)
```

设置指定属性数值（自动同步到客户端）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `Value` | `number` | 操作数值 |

### `GetGameAttributeValueMax`

```text
GetGameAttributeValueMax(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举) -> number
```

获取指定属性数值的最大值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Returns**

| Type | Description |
|---|---|
| `number` | 目标数值 |

### `GetGameAttributeValueMin`

```text
GetGameAttributeValueMin(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举) -> number
```

获取指定属性数值的最小值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Returns**

| Type | Description |
|---|---|
| `number` | 目标数值 |

### `AddGameAttributeValue`

```text
AddGameAttributeValue(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, Value: number)
```

服务端添加指定属性数值（自动同步到客户端）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `Value` | `number` | 操作数值 |

### `AddGameAttributeOperation`

```text
AddGameAttributeOperation(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, OperateType: EAttrOperator, Value: number) -> string
```

对指定属性添加数值修改操作
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `OperateType` | `EAttrOperator` | 操作类型 |
| `Value` | `number` | 操作数值 |

**Returns**

| Type | Description |
|---|---|
| `string` | 操作完成的唯一ID |

### `RemoveGameAttributeOperation`

```text
RemoveGameAttributeOperation(AttributeOwner: AActor, OperateUniqueID: string)
```

对指定属性移除特定的数值修改操作
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `OperateUniqueID` | `string` | 操作属性时返回的唯一ID |

### `AddGameAttributeChangedDelegate`

```text
AddGameAttributeChangedDelegate(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, CallbackFunction: function) -> Delegate
```

注册指定属性变化时的回调函数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `CallbackFunction` | `function` | 此属性变化时的回调函数 函数形式: function(AttributeOwner, AttrName, CurValue) end |

**Returns**

| Type | Description |
|---|---|
| `Delegate` | 属性变化的代理 |

### `RemoveGameAttributeChangedDelegate`

```text
RemoveGameAttributeChangedDelegate(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, ChangedDelegate: Delegate)
```

清除指定属性变化时的回调函数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `ChangedDelegate` | `Delegate` | 注册回调函数时返回的代理 |

### `GetSourceObjectFromContext`

```text
GetSourceObjectFromContext(Context: FGameMagnitudeContext) -> UObject
```

获取伤害事件上下文中的原对象
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 原对象 |

### `GetVictimFromContext`

```text
GetVictimFromContext(Context: FGameMagnitudeContext) -> AActor
```

获取伤害事件上下文中的受害者
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 受害者 |

### `GetCauserFromContext`

```text
GetCauserFromContext(Context: FGameMagnitudeContext) -> AActor
```

获取伤害事件上下文中的攻击者
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 攻击者(如玩家，怪物, 枪械等) |

### `GetInstigatorFromContext`

```text
GetInstigatorFromContext(Context: FGameMagnitudeContext) -> AController
```

获取伤害事件上下文中的攻击者Controller
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AController` | 攻击者Controller(如玩家PlayerController，怪物AIController, 枪械所属角色的Controller等) |

### `GetSourceMagnitudeFromContext`

```text
GetSourceMagnitudeFromContext(Context: FGameMagnitudeContext) -> number
```

获取伤害事件上下文中的原伤害数值
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `number` | 伤害数值 |

### `GetDamageTypeFromContext`

```text
GetDamageTypeFromContext(Context: FGameMagnitudeContext) -> ERestrictedDamageType
```

获取伤害事件上下文中的伤害类型
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `ERestrictedDamageType` | 伤害类型 |

### `GetDamageTagsFromContext`

```text
GetDamageTagsFromContext(Context: FGameMagnitudeContext) -> FName[]
```

获取伤害事件上下文中的伤害Tags
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `FName[]` | 伤害Tags |

### `GetRecoverTagsFromContext`

```text
GetRecoverTagsFromContext(Context: FGameMagnitudeContext) -> FName[]
```

获取治疗事件上下文中的治疗Tags
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 治疗事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `FName[]` | 伤害Tags |

### `GetRecoveredActorFromContext`

```text
GetRecoveredActorFromContext(Context: FGameMagnitudeContext) -> AActor
```

获取治疗上下文中的被治疗者
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 治疗事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 被治疗者 |

### `GetDamagePositionTypeFromContext`

```text
GetDamagePositionTypeFromContext(Context: FGameMagnitudeContext) -> EAvatarDamagePosition
```

获取伤害事件上下文中的伤害部位类型
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `EAvatarDamagePosition` | 伤害部位类型 |

## Language

`lua`
