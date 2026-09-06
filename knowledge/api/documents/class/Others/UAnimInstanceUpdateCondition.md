---
id: "api:class:UAnimInstanceUpdateCondition"
title: "UAnimInstanceUpdateCondition"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimInstanceUpdateCondition.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimInstanceUpdateCondition

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Enable` | `bool` | - |
| `StopDelay` | `float` | - |

## Functions

### `SetEnable`

```text
SetEnable(InEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckCondition`

```text
CheckCondition(AnimInstance: UAnimInstance *, DeltaTime: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnInit`

```text
OnInit(OwnerInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUninit`

```text
OnUninit(OwnerInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OwnerInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `NeedUpdate`

```text
NeedUpdate(AnimInstance: UAnimInstance *, DeltaTime: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimInstance` | `UAnimInstance *` | - |
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
