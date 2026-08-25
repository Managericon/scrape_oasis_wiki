---
id: "api:class:UGCDelegateUtility"
title: "UGCDelegateUtility"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCDelegateUtility.json"
category: "API Wiki/class/和平全局接口/基础功能"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCDelegateUtility

UGC 委托工具库

Lua 委托工具
- 使用 New() 创建委托
- 使用 Add(callable, obj) 绑定可调用对象
- 使用 Remove(callable, obj) 解绑可调用对象
- 使用 Broadcast(...) 触发委托

## Functions

### `CreateLuaDelegate`

```text
CreateLuaDelegate() -> @Lua
```

创建 Lua 委托（纯 Lua 实现）

**Returns**

| Type | Description |
|---|---|
| `@Lua` | 委托 |

### `CopyLuaDelegate`

```text
CopyLuaDelegate(Delegate: UGCLuaDelegate) -> UGCLuaDelegate
```

复制 Lua 委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `UGCLuaDelegate` | 被复制的 Lua 委托 |

**Returns**

| Type | Description |
|---|---|
| `UGCLuaDelegate` | 复制出来的新 Lua 委托 |

### `CreateUEDelegate`

```text
CreateUEDelegate(Outer: UObject) -> ULuaSingleDelegate
```

创建虚幻兼容单播委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject` | Outer 对象（GC 相关） |

**Returns**

| Type | Description |
|---|---|
| `ULuaSingleDelegate` | 虚幻兼容单播委托 |

### `DestroyUEDelegate`

```text
DestroyUEDelegate(UEDelegate: ULuaSingleDelegate)
```

销毁虚幻兼容单播委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UEDelegate` | `ULuaSingleDelegate` | 虚幻兼容单播委托 |

## Language

`lua`
