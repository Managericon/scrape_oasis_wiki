---
id: "api:class:UPersistBaseComponent"
title: "UPersistBaseComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPersistBaseComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPersistBaseComponent

技能Buff组件

## Inheritance

`UGameplayTasksComponent` -> `IObjectPoolInterface`

## Functions

### `RegisterPersistEffectWithSlot`

```text
RegisterPersistEffectWithSlot(Slot: FGameplayTag, InPE: UPersistEffectBase *, bShouldUnapply: bool) -> bool
```

生效范围：服务器
	  将PersistEffect注册到目标槽位中

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `FGameplayTag` | 槽位 |
| `InPE` | `UPersistEffectBase *` | 注册到槽位的PersistEffect |
| `bShouldUnapply` | `bool` | 是否将原来槽位上的PersistEffect进行Unapply |

**Returns**

| Type | Description |
|---|---|
| `bool` | 注册是否成功 |

### `UnRegisterPersistEffectWithSlot`

```text
UnRegisterPersistEffectWithSlot(Slot: FGameplayTag, bShouldUnapply: bool) -> bool
```

生效范围：服务器
	  将目标槽位中的PersistEffect解除注册

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `FGameplayTag` | 槽位 |
| `bShouldUnapply` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | 解除注册是否成功 |

### `GetPersistEffectBySlot`

```text
GetPersistEffectBySlot(Slot: FGameplayTag) -> SHADOWTRACKEREXTRA_API UPersistEffectBase *
```

生效范围：服务器&客户端
	  获取目标槽位中的PersistEffect

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `FGameplayTag` | 槽位 |

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API UPersistEffectBase *` | 槽位上的PersistEffect |

## Delegates

### `DynamicStateEnterHandle`

```text
DynamicStateEnterHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
	  生效范围：服务器&客户端
	  进入状态事件, 注意：服务端DynamicState是有计数的, 服务端多次EnterDynamicState都会触发这个代理

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 进入的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateLeaveHandle`

```text
DynamicStateLeaveHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
      生效范围：服务器&客户端
      离开状态事件, 注意：服务端DynamicState是有计数的, 服务端多次LeaveDynamicState都会触发这个代理, 只有当前计数为0时再Leave就不会触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 离开的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateInterruptedHandle`

```text
DynamicStateInterruptedHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
	  生效范围：服务器&客户端
	  打断状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 打断的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateInterruptedWithSourceHandle`

```text
DynamicStateInterruptedWithSourceHandle(SelfRef: UPersistBaseComponent*, InterruptedState: FGameplayTag, SourceState: FGameplayTag) -> void
```

Event
	  生效范围：服务器
	  打断状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `InterruptedState` | `FGameplayTag` | - |
| `SourceState` | `FGameplayTag` | 打断的状态的来源 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateDisabledChangedHandle`

```text
DynamicStateDisabledChangedHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag, bNewDisabled: bool) -> void
```

Event
	  生效范围：服务器&客户端
	  禁用状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 禁用的状态 |
| `bNewDisabled` | `bool` | 禁用解除禁用 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicStateDisabledResetHandle`

```text
DynamicStateDisabledResetHandle(SelfRef: UPersistBaseComponent*, state: FGameplayTag) -> void
```

Event
	  生效范围：服务器&客户端
	  重置禁用状态事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelfRef` | `UPersistBaseComponent*` | 监听的组件 |
| `state` | `FGameplayTag` | 重置禁用的状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
