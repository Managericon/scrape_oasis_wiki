---
id: "api:class:UPersistEffectBase"
title: "UPersistEffectBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPersistEffectBase

PersistEffectBase, PersistEffectSkill和PersistEffectBuff的基类

## Inheritance

`UBasicPersistEffect` -> `IGameplayTaskOwnerInterface` -> `ILimitationInterface` -> `IOwnershipChainInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bPersistOnUnapply` | `bool` | Unapply 时是否缓存到 PlayerState 上的 PersistEffectCacheComponent，<br>	  下次同类型 Apply 会取回并触发 OnRecover |

## Functions

### `HasAuthority`

```text
HasAuthority() -> bool
```

检查当前对象是否运行在服务器端
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `bool` | 否运行在服务器端 |

### `IsAutonomous`

```text
IsAutonomous(bConsiderObReplay: bool) -> const bool
```

检查当前对象是否运行在主控客户端
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bConsiderObReplay` | `bool` | 是否包含观战和回放时的主控端 |

**Returns**

| Type | Description |
|---|---|
| `const bool` | 否运行在主控客户端 |

### `RefreshValidTime`

```text
RefreshValidTime() -> void
```

刷新PersistEffect的生效时间
	  生效范围: 服务器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTickEnable`

```text
SetTickEnable(bEnable: bool) -> void
```

设置PersistEffect是否每帧执行Tick函数，在服务器调用只会开启服务器的Tick，在客户端调用只会开启客户端的Tick
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetApplyTime`

```text
SetApplyTime(Time: float) -> void
```

设置PersistEffect的生效时间
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetApplyTime`

```text
GetApplyTime() -> float
```

获取PersistEffect的生效时间
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTimeStamp`

```text
GetTimeStamp() -> float
```

获取当前服务器时间戳
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `HasTag`

```text
HasTag(Tag: FGameplayTag) -> bool
```

检查当前技能或Buff是否有某个类型的Tag
	  生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `FGameplayTag` | 要检查的Tag |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否有对应的Tag |

### `GetRemainingTime`

```text
GetRemainingTime() -> float
```

获取剩余时间

**Returns**

| Type | Description |
|---|---|
| `float` | 剩余时间 |

### `SetPersistOnUnapply`

```text
SetPersistOnUnapply(bInPersistOnUnapply: bool) -> void
```

运行时动态修改 bPersistOnUnapply。仅服务端生效，不 Replicated。
	  可在 OnApply  Tick  OnUnApply_BP 等任意服务端时机调用。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInPersistOnUnapply` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShouldPersistOnUnapply`

```text
ShouldPersistOnUnapply() -> bool
```

读取当前 bPersistOnUnapply (含运行时修改值)。

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOwnerActor`

```text
GetOwnerActor() -> AActor *
```

获取PersistEffect所属的Actor
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetOwnerComponent`

```text
GetOwnerComponent() -> UPersistBaseComponent *
```

获取PersistEffect所属的组件
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UPersistBaseComponent *` | - |

## Events

### `OnApply_BP`

```text
OnApply_BP(Character: AActor *) -> void
```

当PersistEffect挂载到角色身上时调用
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnApply_BP`

```text
OnUnApply_BP(Character: AActor *, Reason: EPersistEffectUnApplyReason) -> void
```

当PersistEffect从角色身上移除时调用
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |
| `Reason` | `EPersistEffectUnApplyReason` | 移除的原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanApply_BP`

```text
CanApply_BP(Character: AActor *) -> bool
```

当PersistEffect挂载到角色身上前检查是否可挂载时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 尝试挂载的角色 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否可以挂载 |

### `OnMerge_BP`

```text
OnMerge_BP(Target: UPersistEffectBase *, ApplyTime: float) -> void
```

当PersistEffect合并时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `UPersistEffectBase *` | 被合并的PersistEffect |
| `ApplyTime` | `float` | 被合并的PersistEffect的生效时长 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanMerge_BP`

```text
CanMerge_BP(Target: UPersistEffectBase *) -> bool
```

当PersistEffect合并前检查是否可合并时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `UPersistEffectBase *` | 被合并的PersistEffect |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否可以合并 |

### `OnRecover_BP`

```text
OnRecover_BP(Character: AActor *) -> void
```

当PersistEffect从缓存中恢复使用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 恢复后的新挂载角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Tick_BP`

```text
Tick_BP(Character: AActor *, DeltaTime: float) -> void
```

PersistEffect每帧调用，开启Tick需要SetTickEnable(true)
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |
| `DeltaTime` | `float` | 距离上次触发后经过的时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInterrupted_BP`

```text
OnInterrupted_BP(Character: AActor *) -> void
```

当PersistEffect被打断时调用
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `AActor *` | 挂载的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
