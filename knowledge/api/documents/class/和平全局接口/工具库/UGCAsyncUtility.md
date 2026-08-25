---
id: "api:class:UGCAsyncUtility"
title: "UGCAsyncUtility"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCAsyncUtility.json"
category: "API Wiki/class/和平全局接口/工具库"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCAsyncUtility

异步工具类

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCAsyncUtility.CoroutineManager` | `-` | - |
| `UGCAsyncUtility.AsyncErrorType` | `-` | - |

## Functions

### `CreatePromiseFuture`

```text
CreatePromiseFuture(Prerequisite: UGCPromiseFuture, ...: any) -> UGCPromiseFuture
```

创建一个新的 PromiseFuture 实例
 - 创建实例: 使用 PromiseFuture.New() 创建新的 PromiseFuture 实例。
 - 设置回调: 使用 Then 和 Else 方法设置成功和失败的回调函数。
 - 执行逻辑: 使用 Set 方法定义 PromiseFuture 的执行逻辑，可以在其中使用 Yield 暂停执行。
 - 前置条件: 可以将其他 PromiseFuture 实例作为前置条件，确保在执行当前 PromiseFuture 之前，所有前置条件都已完成。
 - 自动恢复: 可以设置自动恢复功能，监控对象的状态并在需要时自动恢复执行。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Prerequisite` | `UGCPromiseFuture` | 可选的前置条件 PromiseFuture 实例 |
| `...` | `any` | 其他可选的前置条件 |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 新创建的 PromiseFuture 实例 |

### `NewSequenceList`

```text
NewSequenceList() -> UGCAsyncSequenceHandle
```

新建一个保序列表，并返回ListHandle用于操作

**Returns**

| Type | Description |
|---|---|
| `UGCAsyncSequenceHandle` | 返回的ListHandle |

### `InsertItemIntoSequenceList`

```text
InsertItemIntoSequenceList(ListHandle: UGCAsyncSequenceHandle, ParamIndex: number, InConditionFunction: any, InConditionTable: table, InFunction: function@, InFunctionTable: table, ...: any)
```

往List里添加变量和函数。激活后时序逻辑为：轮询变量是否为空或者函数是否返回true，当变量不为空的时候，执行对应的函数，所以每次Insert一组变量和函数，就相当于添加一个时序逻辑。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListHandle` | `UGCAsyncSequenceHandle` | 保序列表的索引 |
| `ParamIndex` | `number` | 参数插入保序列表的位置，如果是0，则是插入到列表的尾部 |
| `InConditionFunction` | `any` | 可执行的Function或变量 |
| `InConditionTable` | `table` | 轮询变量或函数所在的Table |
| `InFunction` | `function@` | 当条件为true时执行的函数 |
| `InFunctionTable` | `table` | 当条件为true时执行函数的Table |
| `...` | `any` | 可变参数，当条件为true时执行的函数参数 |

### `ActivateSequenceList`

```text
ActivateSequenceList(ListHandle: UGCAsyncSequenceHandle, Interval: number, Timeout: number)
```

激活保序列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListHandle` | `UGCAsyncSequenceHandle` | 保序列表的索引 |
| `Interval` | `number` | 自动恢复的间隔，单位为秒 |
| `Timeout` | `number` | 自动恢复的超时时间，单位为秒 |

### `AsyncLoadSomething`

```text
AsyncLoadSomething(AsyncFun: function, ParamTables: UGCAsyncSequenceParamTable[], OnCompleteCallback: function) -> table
```

支持并行初始化的通用有序异步加载器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AsyncFun` | `function` | 需要调用的异步函数（格式：func(LoadPath, CallBack, CallBack_Self)） |
| `ParamTables` | `UGCAsyncSequenceParamTable[]` | 参数表数组 |
| `OnCompleteCallback` | `function` | 最终回调(loadedObjects) |

**Returns**

| Type | Description |
|---|---|
| `table` | loadedObjects |

### `AsyncCall`

```text
AsyncCall(CallFunction: function, Callback: function, CheckFunction: function, Opts: table) -> PromiseFuture
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CallFunction` | `function` | 调用函数 |
| `Callback` | `function` | 回调函数 |
| `CheckFunction` | `function` | 检查函数 |
| `Opts` | `table` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | - |

### `AsyncIfThen`

```text
AsyncIfThen(IfFunction: function, ThenFunction: function, Opts: table)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IfFunction` | `function` | 条件函数，返回 true 时执行 ThenFunction |
| `ThenFunction` | `function` | 条件满足时执行的函数 |
| `Opts` | `table` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

### `AsyncIfThenElse`

```text
AsyncIfThenElse(IfFunction: function, ThenFunction: function, ElseFunction: function, Opts: table)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IfFunction` | `function` | 条件函数，返回 true 时执行 ThenFunction，超时/取消时执行 ElseFunction |
| `ThenFunction` | `function` | 条件满足时执行的函数 |
| `ElseFunction` | `function` | 超时或取消时执行的函数 |
| `Opts` | `table` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

## Language

`lua`
