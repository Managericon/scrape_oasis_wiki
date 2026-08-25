---
id: "api:class:UPersistEffectWithState"
title: "UPersistEffectWithState"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectWithState.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPersistEffectWithState

实现了状态机的PersistEffect，是PersistEffectSkill的基类

## Inheritance

`UPersistEffectBase` -> `IActivityStateInterface` -> `IClientConditionInerterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bTickStateMachineBeforeSequence` | `bool` | 控制Tick中状态机和Sequence的执行顺序<br>	  true: 先TickStateMachine再SequenceWrapper.Tick（默认，与原有逻辑一致）<br>	  false: 先SequenceWrapper.Tick再TickStateMachine |

## Functions

### `GetCurrentStateName`

```text
GetCurrentStateName() -> FName
```

获取当前状态的名字
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetCurrentStateTime`

```text
GetCurrentStateTime() -> float
```

获取状态的运行时间
	  生效范围: 服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `JumpToState`

```text
JumpToState(StateName: FName, EnterTime: float, bPause: bool) -> void
```

获取跳转到指定状态
	  生效范围: 服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | 跳转的目标状态名 |
| `EnterTime` | `float` | 跳转到目标状态的时间 |
| `bPause` | `bool` | 是否暂停sequence播放 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
