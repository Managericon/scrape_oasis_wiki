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

### `AddBindingByStateAndName`

```text
AddBindingByStateAndName(StateName: FName, BindingName: FName, Object: UObject *) -> void
```

按 State 名 + Binding 名一步绑定：将指定 State 的 SkillSequence 中
	  名为 BindingName 的 Actor 轨道操控实例，绑定到 Object 指向的运行时目标。
	  与编辑器 "Get 绑定" + "Add Binding" 节点等价，供  Lua 使用。
	  生效范围: 服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | 技能状态名（需 SequenceType == GenerateSkillSequence 且配置了 SkillSequence） |
| `BindingName` | `FName` | 该 SkillSequence 中目标轨道的名称（对应编辑器绑定下拉中的显示名） |
| `Object` | `UObject *` | 要绑定的运行时目标 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
