---
id: "api:class:UGCCommonDelegate"
title: "UGCCommonDelegate"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCCommonDelegate.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCCommonDelegate

UGC通用委托

## Functions

### `Add`

```text
Add(Callback: function, CallbackOwner: any)
```

添加回调

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callback` | `function` | 回调函数 |
| `CallbackOwner` | `any` | 回调函数所有者，可不传 |

### `Remove`

```text
Remove(Callback: function, CallbackOwner: any)
```

移除回调

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callback` | `function` | 回调函数 |
| `CallbackOwner` | `any` | 回调函数所有者，可不传 |

### `RemoveAll`

```text
RemoveAll()
```

移除所有回调

### `Broadcast`

```text
Broadcast(...: any)
```

广播事件，会根据委托类型进行不同的处理
可以直接用函数调用的方式触发广播，例如`CommonDelegate(1, 2, 3)`

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 事件参数 |

### `ToUEDelegate`

```text
ToUEDelegate(Outer: UObject) -> ULuaSingleDelegate
```

转换为UE的单播委托，可以传递给需要UE单播委托的接口

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject` | Outer 对象（GC 相关） |

**Returns**

| Type | Description |
|---|---|
| `ULuaSingleDelegate` | 单播委托 |

## Language

`lua`
