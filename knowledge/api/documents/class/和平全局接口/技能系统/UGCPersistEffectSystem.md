---
id: "api:class:UGCPersistEffectSystem"
title: "UGCPersistEffectSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCPersistEffectSystem.json"
category: "API Wiki/class/和平全局接口/技能系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCPersistEffectSystem

新技能和Buff系统接口库

## Functions

### `AddSkillByClass`

```text
AddSkillByClass(TargetActor: AActor, SkillClass: UClass|string, OverrideApplyTime: number, Slot: UGCGameplayTag|string|FGameplayTag) -> UPersistEffectSkill
```

给指定拥有新技能组件的目标 Actor 添加技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `SkillClass` | `UClass\|string` | 技能蓝图类或蓝图路径 |
| `OverrideApplyTime` | `number` | 技能生效时长(可选，默认为技能类中配置的时长) |
| `Slot` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的技能槽位 |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill` | 技能对象 |

### `RemoveSkillInstance`

```text
RemoveSkillInstance(TargetActor: AActor, SkillInstance: UPersistEffectSkill) -> boolean
```

给指定拥有新技能组件的目标 Actor 移除技能
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `SkillInstance` | `UPersistEffectSkill` | 技能对象 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否移除成功 |

### `GetSkillsByClass`

```text
GetSkillsByClass(TargetActor: AActor, SkillClass: UClass|string) -> UPersistEffectSkill[]
```

从指定拥有新技能组件的目标 Actor 获取指定类型的技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `SkillClass` | `UClass\|string` | 技能蓝图类或蓝图路径,为空时获取所有技能 |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill[]` | 技能列表 |

### `GetSkillsByTag`

```text
GetSkillsByTag(TargetActor: AActor, Tag: UGCGameplayTag|string|FGameplayTag) -> UPersistEffectSkill[]
```

从指定拥有新技能组件的目标 Actor 获取拥有指定 Tag 的技能
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要获取的技能所包含的 Tag,为空时获取所有技能 |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectSkill[]` | 技能列表 |

### `AddBuffByClass`

```text
AddBuffByClass(TargetActor: AActor, BuffClass: UClass|string, Causer: AActor, OverrideDuration: number, StackNum: number) -> UPersistEffectBuff
```

给指定拥有新技能组件的目标 Actor 添加 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `BuffClass` | `UClass\|string` | Buff 蓝图类或蓝图路径 |
| `Causer` | `AActor` | Buff释放者（可选，默认为空） |
| `OverrideDuration` | `number` | 技能生效时长（可选，默认为-1代表Buff类中配置的时长） |
| `StackNum` | `number` | Buff的堆叠层数（可选，默认为 1 层） |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectBuff` | Buff对象 |

### `RemoveBuffByClass`

```text
RemoveBuffByClass(TargetActor: AActor, BuffClass: UClass|string, RemoveNum: number, Causer: AActor) -> boolean
```

给指定拥有新技能组件的目标 Actor 移除 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `BuffClass` | `UClass\|string` | Buff 蓝图类或蓝图路径 |
| `RemoveNum` | `number` | Buff减少堆叠数量（可选，默认-1移除全部层） |
| `Causer` | `AActor` | 筛选特定的释放者（可选，默认不筛选） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否移除成功 |

### `RemoveBuffByTag`

```text
RemoveBuffByTag(TargetActor: AActor, Tag: UGCGameplayTag|string|FGameplayTag, RemoveNum: number, Causer: AActor) -> boolean
```

给指定拥有新技能组件的目标 Actor 移除包含某个 Tag 的 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要移除的 Buff 所包含的 Tag |
| `RemoveNum` | `number` | Buff 减少堆叠数量（可选，默认移除全部层） |
| `Causer` | `AActor` | 筛选特定的释放者(可选，默认不筛选) |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否移除成功 |

### `GetBuffsByClass`

```text
GetBuffsByClass(TargetActor: AActor, BuffClass: UClass|string) -> UPersistEffectBuff[]
```

从指定拥有新技能组件的目标 Actor 获取指定类型的Buff
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `BuffClass` | `UClass\|string` | Buff蓝图类或蓝图路径,为空时获取所有Buff |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectBuff[]` | Buff列表 |

### `GetBuffsByTag`

```text
GetBuffsByTag(TargetActor: AActor, Tag: UGCGameplayTag|string|FGameplayTag) -> UPersistEffectBuff[]
```

从指定拥有新技能组件的目标 Actor 获取拥有指定Tag的Buff
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标Actor |
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要获取的 Buff 所包含的 Tag,为空时获取所有Buff |

**Returns**

| Type | Description |
|---|---|
| `UPersistEffectBuff[]` | Buff列表 |

### `HasDynamicState`

```text
HasDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查指定拥有新技能组件的目标 Actor 是否包含某个 Tag 标识的状态
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要检查的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否拥有 Tag 标识的状态 |

### `AllowDynamicState`

```text
AllowDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查指定拥有新技能组件的目标 Actor 是否允许进入某个 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要检查的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否允许进入 Tag 标识的状态 |

### `EnterDynamicState`

```text
EnterDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

尝试让拥有新技能组件的目标 Actor 获取指定 Tag 标识的状态，多次获取同一个 Tag 会叠加计数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要添加的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否成功 |

### `LeaveDynamicState`

```text
LeaveDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

尝试从拥有新技能组件的目标 Actor 移除指定 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要移除的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否有剩余的 Tag。若移除 Tag 的一次计数后还有剩余则返回 False，若全部没有剩余则返回 True |

### `InterruptDynamicState`

```text
InterruptDynamicState(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

将拥有新技能组件的目标 Actor 的 Tag 标识的状态移除并触发打断事件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要打断的 Tag 标识的状态 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否成功打断 |

### `SetDynamicStateDisabled`

```text
SetDynamicStateDisabled(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag, bNewDisabled: boolean, bInterrupt: boolean)
```

设置由 Tag 标识的状态的是否禁用，Actor 中 Tag 的禁用计数大于 0 时禁用生效
 - bNewDisabled == True：将拥有新技能组件的目标 Actor 的一组 Tag 标识的状态进行打断，并为这一组 Tag 的禁用计数 +1
 - bNewDisabled == false：将拥有新技能组件的目标 Actor 的一组 Tag 标识的状态禁用计数 -1
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要增加或减少禁用的 Tag 标识的状态 |
| `bNewDisabled` | `boolean` | 是否禁用 |
| `bInterrupt` | `boolean` | 是否打断，默认为 true |

### `ResetDynamicStateDisabled`

```text
ResetDynamicStateDisabled(TargetActor: AActor, DynamicStateTag: UGCGameplayTag|string|FGameplayTag)
```

重置被禁用的由 Tag 标识的状态，重置后目标 Actor 将允许进入这个 Tag 标识的状态
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |
| `DynamicStateTag` | `UGCGameplayTag\|string\|FGameplayTag` | 需要增加或减少禁用的 Tag 标识的状态 |

### `GetPersistBaseComponentByContent`

```text
GetPersistBaseComponentByContent(TargetActor: AActor) -> @UPersistBaseComponent
```

从拥有新技能组件的目标 Actor 上获取 PersistBaseComponent 组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `AActor` | 拥有新技能组件的目标 Actor |

**Returns**

| Type | Description |
|---|---|
| `@UPersistBaseComponent` | 组件 |

### `AddOcclusionHighlight`

```text
AddOcclusionHighlight(TargetCharacter: ACharacter, Causer: AActor, Type: EPEBuffOcclusionHighlightType, Color: FLinearColor) -> number
```

添加透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetCharacter` | `ACharacter` | 被透视的角色或怪 |
| `Causer` | `AActor` | 透视的发起方 |
| `Type` | `EPEBuffOcclusionHighlightType` | 透视类型(仅Causer透视/Causer及其队友透视/所有人) |
| `Color` | `FLinearColor` | 透视颜色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 透视ID，用于移除透视效果,<=0为无效值 |

### `RemoveOcclusionHighlight`

```text
RemoveOcclusionHighlight(WorldContextObject: UObject, OcclusionID: number)
```

移除透视效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `OcclusionID` | `number` | 透视ID，AddOcclusionHighlight函数的返回值, <=0为无效值 |

### `AddFresnelEffect`

```text
AddFresnelEffect(TargetCharacter: ACharacter, Color: FLinearColor, Duration: number)
```

添加菲涅尔效果
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetCharacter` | `ACharacter` | 被透视的角色或怪 |
| `Color` | `FLinearColor` | 颜色 |
| `Duration` | `number` | 时长 |

### `PickTargets`

```text
PickTargets(OwnerActor: AActor, StartTransform: FTransform, TargetPickerParams: FTargetPickerParams, IgnoreActors: AActor[]) -> AActor[]
```

选取参数指定范围内的目标
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerActor` | `AActor` | 发起选目标的角色 |
| `StartTransform` | `FTransform` | Picker开始位置 |
| `TargetPickerParams` | `FTargetPickerParams` | Picker参数 |
| `IgnoreActors` | `AActor[]` | 忽略的Actors |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 选中的目标 |

## Language

`lua`
