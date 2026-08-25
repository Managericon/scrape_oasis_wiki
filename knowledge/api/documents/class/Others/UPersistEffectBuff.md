---
id: "api:class:UPersistEffectBuff"
title: "UPersistEffectBuff"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectBuff.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPersistEffectBuff

Buff系统归属与和平精英的技能系统，用于帮助开发者更方便快捷地实现Buff效果
  通过与Tag、Attribute等系统的配合能够通过配置就实现大部分所需的效果
  对于更细致的Buff效果也可以通过重写BP结尾的函数来实现定制化效果。

## Inheritance

`UPersistEffectBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BuffInfo` | `FPEBuffInfo` | 生效范围：服务器&客户端<br>      Buff蓝图的配置信息 |

## Functions

### `AddStackNum`

```text
AddStackNum(Num: int32) -> void
```

生效范围：服务器
	  修改堆叠层数，修改后的层数大于等于0且小于等于最大堆叠层数(MaxStackNum)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Num` | `int32` | 新增的层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStackNum`

```text
GetStackNum() -> int32
```

生效范围：服务器&客户端
	 获取当前层数

**Returns**

| Type | Description |
|---|---|
| `int32` | 当前层数 |

### `GetCauser`

```text
GetCauser() -> AActor *
```

生效范围：服务器&客户端
      获取Buff的施加者

**Returns**

| Type | Description |
|---|---|
| `AActor *` | 施加者 |

### `SetCauser`

```text
SetCauser(Causer: AActor *) -> void
```

生效范围：服务器
	 设置Buff的施加者

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Causer` | `AActor *` | 施加者 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TriggerAllLayer`

```text
TriggerAllLayer() -> void
```

生效范围：服务器
      触发当前所有层的Buff的效果

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TriggerSingleLayer`

```text
TriggerSingleLayer() -> void
```

生效范围：服务器
	  触发单层的Buff的效果

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshBuff`

```text
RefreshBuff() -> void
```

生效范围：服务器
	  重置Buff持续时间

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBuffEnable`

```text
SetBuffEnable(IsEnable: bool) -> void
```

生效范围：服务器
	  设置Buff是否生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `bool` | 是否生效 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBuffEnable`

```text
IsBuffEnable() -> bool
```

生效范围：服务器&客户端
	  获取Buff当前是否生效

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否生效 |

### `Pause`

```text
Pause() -> void
```

生效范围：服务器
	  暂停Buff持续减少剩余时间

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Resume`

```text
Resume() -> void
```

生效范围：服务器
	  恢复Buff持续减少剩余时间

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OverwriteBuffUIInfo`

```text
OverwriteBuffUIInfo(BuffName: FName &, BuffDetail: FString &, BuffIconPath: FString &) -> void
```

生效范围：服务器&客户端
	  更改UI信息，但双端不同步

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuffName` | `FName &` | Buff名字 |
| `BuffDetail` | `FString &` | Buff描述 |
| `BuffIconPath` | `FString &` | Buff图标路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBuffName`

```text
GetBuffName() -> SHADOWTRACKEREXTRA_API FName
```

生效范围：服务器&客户端
	  获取Buff名字

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API FName` | Buff名字 |

### `GetBuffDetail`

```text
GetBuffDetail() -> SHADOWTRACKEREXTRA_API FString
```

生效范围：服务器&客户端
	  获取Buff描述

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API FString` | Buff描述 |

### `GetBuffIconPath`

```text
GetBuffIconPath() -> FString
```

生效范围：服务器&客户端
	  获取Buff图标路径

**Returns**

| Type | Description |
|---|---|
| `FString` | Buff图标路径 |

## Events

### `OnTotalDurationChange_BP`

```text
OnTotalDurationChange_BP(Pre: float, Current: float) -> void
```

生效范围：服务器
	  当Buff持续时间改变时调用，如修改ApplyTime、修改StackNum

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pre` | `float` | 上一次的持续时间 |
| `Current` | `float` | 当前的持续时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStackChange_BP`

```text
OnStackChange_BP(PreNum: int32, CurrentNum: int32) -> void
```

生效范围：服务器&客户端
	  当Buff堆叠层数变化时调用，如调用AddStackNum、消耗一层Buff

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PreNum` | `int32` | 上一次的堆叠层数 |
| `CurrentNum` | `int32` | 当前的堆叠层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRefresh_BP`

```text
OnRefresh_BP() -> void
```

生效范围：服务器&客户端
	  Buff刷新时调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanTrigger_BP`

```text
CanTrigger_BP() -> bool
```

生效范围：服务器
	  当Buff效果触发前调用，用于改写Buff触发条件，默认实现为直接返回True

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否可以触发 |

### `OnTrigger_BP`

```text
OnTrigger_BP(Reason: EPEBuffTriggerType) -> void
```

生效范围：服务器&客户端
	  当Buff效果触发时调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EPEBuffTriggerType` | 触发原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnStackNumChange`

```text
OnStackNumChange(ChangeNum: int32) -> void
```

Event
	  生效范围：服务器&客户端
	  Buff层数改变事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangeNum` | `int32` | 改变的层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUIInfoChange`

```text
OnUIInfoChange() -> void
```

Event
	  生效范围：客户端
	  Buff的UI信息改变事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
