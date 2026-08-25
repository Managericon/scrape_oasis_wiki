---
id: "api:class:UGameplayTask_WaitDelay"
title: "UGameplayTask_WaitDelay"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_WaitDelay.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayTask_WaitDelay

## Inheritance

`UGameplayTask`

## Functions

### `TaskWaitDelay`

```text
TaskWaitDelay(TaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, Time: float, Priority: uint8) -> UGameplayTask_WaitDelay *
```

Wait specified time. This is functionally the same as a standard Delay node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `Time` | `float` | - |
| `Priority` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_WaitDelay *` | - |

## Delegates

### `OnFinish`

```text
OnFinish() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
