---
id: "api:class:PromiseFuture"
title: "PromiseFuture"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/PromiseFuture.json"
category: "API Wiki/class/和平全局接口/工具库"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# PromiseFuture

提供处理异步操作的类，支持链式调用和状态管理

说明：
- 创建实例: 使用 PromiseFuture.New() 创建新的 PromiseFuture 实例。
- 设置回调: 使用 Then 和 Else 方法设置成功和失败的回调函数。
- 执行逻辑: 使用 Set 方法定义 PromiseFuture 的执行逻辑，可以在其中使用 Yield 暂停执行。
- 前置条件: 可以将其他 PromiseFuture 实例作为前置条件，确保在执行当前 PromiseFuture 之前，所有前置条件都已完成。
- 自动恢复: 可以设置自动恢复功能，监控对象的状态并在需要时自动恢复执行。

## Functions

### `Resume`

```text
Resume(...: any) -> boolean
```

手动恢复 PromiseFuture 的执行

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 可选的参数，将传递给恢复的协程 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当 IsPrerequisitesEstablished() && IsEstablished() 时返回 true，否则返回 false |

### `IsPrerequisitesEstablished`

```text
IsPrerequisitesEstablished() -> boolean
```

检查所有先决条件是否已建立

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果所有先决条件都已建立则返回 true，否则返回 false |

### `IsAnyPrerequisiteCancellationRequested`

```text
IsAnyPrerequisiteCancellationRequested() -> boolean
```

检查任意先决条件是否已被取消

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果任意先决条件已被取消则返回 true，否则返回 false |

### `IsEstablished`

```text
IsEstablished() -> boolean
```

检查当前 PromiseFuture 是否已建立

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果已建立则返回 true，否则返回 false |

### `WaitForPrerequisites`

```text
WaitForPrerequisites() -> PromiseFuture
```

等待所有前置条件变为已建立状态
如果前置条件未完成，则会自动 Yield
只能在 Set 回调函数中使用

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `AddPrerequisites`

```text
AddPrerequisites(Prerequisite: PromiseFuture) -> PromiseFuture
```

添加前置条件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Prerequisite` | `PromiseFuture` | 前置条件 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `IsCancellationRequested`

```text
IsCancellationRequested() -> boolean
```

检查当前 PromiseFuture 是否已被取消

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果已被取消则返回 true，否则返回 false |

### `GetError`

```text
GetError() -> any
```

获取协程异常时保存的原始错误对象
主动 Cancel 时返回 nil；协程内业务异常时返回 error 值
可与 IsCancellationRequested 配合区分失败原因：
  IsCancellationRequested()==true 且 GetError()==nil  → 主动 Cancel
  IsCancellationRequested()==true 且 GetError()~=nil  → 协程内抛出的业务异常

**Returns**

| Type | Description |
|---|---|
| `any` | 错误对象，或 nil |

### `Cancel`

```text
Cancel() -> PromiseFuture
```

取消当前 PromiseFuture 的执行

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `CancelAll`

```text
CancelAll() -> PromiseFuture
```

取消当前 PromiseFuture 及其所有前置条件的执行

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Get`

```text
Get() -> any
```

获取 Set 回调函数的返回值
只能在 Set、Then 回调函数中使用

**Returns**

| Type | Description |
|---|---|
| `any` | 返回 Set 回调函数的所有返回值 |

### `Then`

```text
Then(Callable: function, ...: any) -> PromiseFuture
```

设置成功回调函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callable` | `function` | 回调函数 |
| `...` | `any` | 可选的参数，将传递给回调函数 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Else`

```text
Else(Callable: function, ...: any) -> PromiseFuture
```

设置失败回调函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callable` | `function` | 回调函数 |
| `...` | `any` | 可选的参数，将传递给回调函数 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Set`

```text
Set(Setter: function, SetterValue: any, ...: any) -> PromiseFuture
```

设置执行逻辑

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Setter` | `function` | 回调函数 |
| `SetterValue` | `any` | - |
| `...` | `any` | 其他可选参数 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `Yield`

```text
Yield(...: any) -> PromiseFuture
```

暂停当前 PromiseFuture 的执行
只能在 Set 回调函数中使用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 可选的参数，将传递给 yield(...) 方法 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

### `AutoResume`

```text
AutoResume(WatchedObject: UObject, Interval: number, Timeout: number) -> PromiseFuture
```

设置自动恢复功能

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WatchedObject` | `UObject` | 监控的对象，如果对象被销毁则停止自动恢复 |
| `Interval` | `number` | 自动恢复的间隔，单位为秒 |
| `Timeout` | `number` | 自动恢复的超时时间，单位为秒 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 当前 PromiseFuture 实例，以支持链式调用 |

## Language

`lua`
