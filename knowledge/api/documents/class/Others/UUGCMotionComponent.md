---
id: "api:class:UUGCMotionComponent"
title: "UUGCMotionComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUGCMotionComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUGCMotionComponent

运动器组件

## Inheritance

`UActorComponent`

## Functions

### `StartMotion`

```text
StartMotion(ConfigID: int) -> void
```

开始运行特定运动器
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `int` | 运动器索引，默认参数-1(所有运动器) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseMotion`

```text
PauseMotion(ConfigID: int) -> void
```

停止特定运动器
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `int` | 运动器索引，默认参数-1(所有运动器) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetMotion`

```text
ResetMotion(ConfigID: int) -> void
```

重置特定运动器
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `int` | 运动器索引，默认参数-1(所有运动器) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
