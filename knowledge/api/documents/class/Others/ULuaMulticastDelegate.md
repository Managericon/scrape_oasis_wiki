---
id: "api:class:ULuaMulticastDelegate"
title: "ULuaMulticastDelegate"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULuaMulticastDelegate.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULuaMulticastDelegate

UE 多播委托基类，用于绑定多个回调函数

## Functions

### `Add`

```text
Add(Callback: function, Obj: any) -> number
```

添加回调，Func 作为 Key 去重，同 Func 不同 Obj 会覆盖

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callback` | `function` | 回调函数，如果绑定了 Obj，则 Obj 作为回调第一个参数传入 |
| `Obj` | `any` | 可选的绑定对象，作为回调第一个参数传入 |

**Returns**

| Type | Description |
|---|---|
| `number` | 回调引用 |

### `AddInstance`

```text
AddInstance(Callback: function, Obj: any) -> number
```

添加回调，Func && Obj 共同作为 Key 去重，同 Func 不同 Obj 会共存

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callback` | `function` | 回调函数，Obj 作为回调第一个参数传入 |
| `Obj` | `any` | 绑定对象，作为回调第一个参数传入 |

**Returns**

| Type | Description |
|---|---|
| `number` | 回调引用 |

### `Remove`

```text
Remove(Callback: function, Obj: any)
```

移除指定回调

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callback` | `function` | 要移除的回调函数 |
| `Obj` | `any` | 可选的绑定对象 |

### `RemoveAll`

```text
RemoveAll()
```

移除所有 Lua 绑定

### `Clear`

```text
Clear(bDonotKeepThis: boolean)
```

移除所有绑定（C++/BP/Lua）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDonotKeepThis` | `boolean` | 是否不保留当前对象的回调 |

### `Broadcast`

```text
Broadcast(...: any)
```

触发 Lua 广播

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 委托参数 |

### `BroadcastAll`

```text
BroadcastAll(...: any)
```

触发所有广播（C++/BP/Lua）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 委托参数 |

## Language

`lua`
