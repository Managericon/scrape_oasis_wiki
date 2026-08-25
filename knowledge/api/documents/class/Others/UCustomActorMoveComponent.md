---
id: "api:class:UCustomActorMoveComponent"
title: "UCustomActorMoveComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCustomActorMoveComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCustomActorMoveComponent

一个给ActivityBaseActor移动功能的组件，用于移动所挂载的ActivityBaseActor

## Inheritance

`UActorComponent`

## Functions

### `StartMove`

```text
StartMove() -> void
```

生效范围：S
	  开始移动

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopMove`

```text
StopMove() -> void
```

生效范围：S
	  结束移动

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMoveSpeed`

```text
SetMoveSpeed(InSpeed: float) -> void
```

生效范围：S
	  设置移动速度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSpeed` | `float` | 速度 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGlideTime`

```text
SetGlideTime(GlideTime: float) -> void
```

生效范围：S
	  设置固定的滑行时间, 而不是使用起始点到终点位置除以速度得到这个数值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GlideTime` | `float` | 滑行时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPosition`

```text
SetPosition(InStart: FVector, InEnd: FVector) -> void
```

生效范围：S
	  设置移动的起始点和终点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStart` | `FVector` | 起点 |
| `InEnd` | `FVector` | 终点 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsMoving`

```text
IsMoving() -> bool
```

生效范围：SC
	  获取Actor是否在移动
	  return 是否在移动

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `ActorMoveEvent`

```text
ActorMoveEvent(bIsMove: bool) -> void
```

移动状态改变事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsMove` | `bool` | 是否正在移动 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
