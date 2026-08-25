---
id: "api:class:Delegate"
title: "Delegate"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/Delegate.json"
category: "API Wiki/class/和平全局接口/基础功能"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# Delegate

Lua代理

Lua代理
- 使用 Add(callable, obj) 绑定可调用对象
- 使用 Remove(callable, obj) 解绑可调用对象
- 使用 Broadcast(...) 触发委托

## Functions

### `Add`

```text
Add()
```

绑定可调用对象
第一个参数为可调用对象（函数），第二个参数为定义了对应函数的表实例
例：Delegate:Add(self.foo, self)
生效范围：服务器&客户端

### `Remove`

```text
Remove() -> nil
```

移除可调用对象
第一个参数为可调用对象（函数），第二个参数为定义了对应函数的表实例
例：Delegate:Remove(self.foo, self)
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `nil` | - |

### `RemoveAll`

```text
RemoveAll(Callable: function)
```

移除可调用对象（函数）上绑定的所有监听函数
例：Delegate:RemoveAll()
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Callable` | `function` | 【可选】可调用对象（函数） |

### `Broadcast`

```text
Broadcast()
```

广播调用监听此委托的所有函数
例：Delegate:Broadcast(param1, param2 ...)
生效范围：服务器&客户端

## Language

`lua`
