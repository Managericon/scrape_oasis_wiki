---
id: "api:class:UGCTimerUtility"
title: "UGCTimerUtility"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCTimerUtility.json"
category: "API Wiki/class/和平全局接口/工具库"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCTimerUtility

计时器工具类

## Functions

### `CreateLuaTimer`

```text
CreateLuaTimer(TimeOffset: number, Callback: function, bLoop: boolean, TimerName: string, InitDelay: number, bLog: boolean, bCoroutine: boolean) -> UGCLuaTimerInstance
```

创建 Lua 计时器
 1. TimeOffset > 0，则 TimeOffset 单位是秒。
 2. TimeOffset == 0，遇到 tick 就会执行。
 3. TimeOffset < 0，是负数如 -N 的话，会在间隔 N 帧后执行第一次。如果传入了 InitDelay，则此条略过，按下面 InitDelay 参数说明来执行：
  a) 如果 InitDelay ~= nil(即传入 InitDelay 参数)，则计时器会在 InitDelay 秒后执行第一次；后面根据 TimeOffset 的设置，循环调用。
  b) 如果 InitDelay == 0，则 InsertTimer 时，会立即执行第一次；后面根据 TimeOffset 的设置，循环调用。
  c) 如果 InitDelay == nil(即未传入 InitDelay 参数)，则会在 TimeOffset 后，执行第一次；后面根据 TimeOffset 的设置，循环调用。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimeOffset` | `number` | 间隔时间 |
| `Callback` | `function` | 回调函数 |
| `bLoop` | `boolean` | 是否循环 |
| `TimerName` | `string` | 计时器名称 |
| `InitDelay` | `number` | 第一次执行延迟时间 |
| `bLog` | `boolean` | 是否记录日志 |
| `bCoroutine` | `boolean` | 是否是协程 |

**Returns**

| Type | Description |
|---|---|
| `UGCLuaTimerInstance` | 创建的计时器实例 |

### `RemoveLuaTimer`

```text
RemoveLuaTimer(TimerInstance: UGCLuaTimerInstance)
```

移除 Lua 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerInstance` | `UGCLuaTimerInstance` | 计时器实例 |

### `RemoveLuaTimerByName`

```text
RemoveLuaTimerByName(TimerName: string)
```

根据名称移除 Lua 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerName` | `string` | 计时器名称 |

### `IsLuaTimerExistByName`

```text
IsLuaTimerExistByName(TimerName: string) -> boolean
```

根据名称判断 Lua 计时器是否存在
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerName` | `string` | 计时器名称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否存在 |

### `CreateUETimer`

```text
CreateUETimer(CallbackFunction: LuaFunction, Time: number, IsLooping: boolean) -> ULuaSingleDelegate
```

设置 UE 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CallbackFunction` | `LuaFunction` | Lua 回调函数 |
| `Time` | `number` | 定时时长 |
| `IsLooping` | `boolean` | 是否循环 |

**Returns**

| Type | Description |
|---|---|
| `ULuaSingleDelegate` | 计时器句柄，计时器回调 |

### `RemoveUETimer`

```text
RemoveUETimer(TimerHandle: FTimerHandle)
```

移除 UE 计时器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimerHandle` | `FTimerHandle` | 计时器句柄 |

## Language

`lua`
