---
id: "api:class:ULuaSingleDelegate"
title: "ULuaSingleDelegate"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULuaSingleDelegate.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULuaSingleDelegate

UE 单播委托基类，用于绑定单个回调函数，后绑定会覆盖先绑定

## Functions

### `Bind`

```text
Bind(Callback: function, Obj?: any) -> number
```

绑定回调函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callback` | `function` | 回调函数，如果绑定了 Obj，则 Obj 作为回调第一个参数传入 |
| `Obj?` | `any` | 可选的绑定对象，作为回调第一个参数传入 |

**Returns**

| Type | Description |
|---|---|
| `number` | 回调引用 |

### `UnBind`

```text
UnBind()
```

解绑回调函数

### `Execute`

```text
Execute(...: any)
```

执行委托，触发已绑定的回调

**Parameters**

| Name | Type | Description |
|---|---|---|
| `...` | `any` | 委托参数 |

## Language

`lua`
