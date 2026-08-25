---
id: "api:class:UOverlapCheckAreaComponent"
title: "UOverlapCheckAreaComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UOverlapCheckAreaComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UOverlapCheckAreaComponent

区域重叠检测组件，能够检测到某个范围内开启重叠检测的Actor

## Inheritance

`UActorComponent` -> `IRegionObjectInterface` -> `IComponentHibernationNotifyInterface`

## Functions

### `CheckOverlapActor`

```text
CheckOverlapActor(DeltaTime: float) -> void
```

生效范围：S
	  触发一次区域重叠检测

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartCheck`

```text
StartCheck(InIgnoreActorList: TArray < AActor * >, bStopIfStarted: bool) -> void
```

生效范围：S
	  开始检测

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIgnoreActorList` | `TArray < AActor * >` | - |
| `bStopIfStarted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopCheck`

```text
StopCheck() -> void
```

生效范围：S
	  停止检测

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddIgnoreActors`

```text
AddIgnoreActors(Ignores: TArray < AActor * >) -> void
```

生效范围：S
	  添加要忽略的Actor列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Ignores` | `TArray < AActor * >` | 要添加的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveIgnoreActor`

```text
RemoveIgnoreActor(Ignore: AActor *) -> int32
```

生效范围：S
	  移除忽略的Actor列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Ignore` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`
