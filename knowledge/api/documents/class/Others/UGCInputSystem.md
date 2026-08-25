---
id: "api:class:UGCInputSystem"
title: "UGCInputSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCInputSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCInputSystem

输入系统接口库

## Functions

### `BindInputMapping`

```text
BindInputMapping(BindingOwner: UObject, InputTag: UGCGameplayTag|string|FGameplayTag, TriggerEvent: ETriggerEvent, CallbackFunction: fun(InputValue:float, ElapsedTime:float, TriggeredTime:float, InputTag:FGameplayTag) @事件触发回调函数) -> int32
```

绑定指定InputTag事件的回调函数
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindingOwner` | `UObject` | 绑定输入事件的对象 |
| `InputTag` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |
| `TriggerEvent` | `ETriggerEvent` | 输入事件类型 |
| `CallbackFunction` | `fun(InputValue:float, ElapsedTime:float, TriggeredTime:float, InputTag:FGameplayTag) @事件触发回调函数` | 事件触发回调函数 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 输入事件绑定的索引，-1时为绑定失败 |

### `RemoveBindingToObject`

```text
RemoveBindingToObject(BindingOwner: UObject)
```

解除与目标Object所有相关的输入事件绑定
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindingOwner` | `UObject` | 绑定输入事件的对象 |

### `RemoveBinding`

```text
RemoveBinding(WorldContext: UObject, InputBindingHandle: int32)
```

解除指定索引的输入事件绑定
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputBindingHandle` | `int32` | 输入事件绑定的索引 |

### `InjectInputMapping`

```text
InjectInputMapping(WorldContext: UObject, InputTag: UGCGameplayTag|string|FGameplayTag, Value: float)
```

通过脚本手动触发某个InputTag
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputTag` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |
| `Value` | `float` | 输入事件的值 |

### `SetBindingConsumeInput`

```text
SetBindingConsumeInput(WorldContext: UObject, InputBindingHandle: int32, bConsumeInput: bool)
```

设置某个输入事件绑定是否消耗输入，消耗输入后，后续的其他输入事件绑定将不被触发
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputBindingHandle` | `int32` | 输入事件绑定的索引 |
| `bConsumeInput` | `bool` | 是否消耗Input |

### `GetInputValue`

```text
GetInputValue(WorldContext: UObject, InputTag: UGCGameplayTag|string|FGameplayTag) -> float
```

获取指定InputTag对应Input的当前值
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `InputTag` | `UGCGameplayTag\|string\|FGameplayTag` | 由Tag标识的输入事件 |

**Returns**

| Type | Description |
|---|---|
| `float` | Input当前值，未找到时返回0 |

## Language

`lua`
