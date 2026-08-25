---
id: "api:class:UGameplayTask_TimeLimitedExecution"
title: "UGameplayTask_TimeLimitedExecution"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_TimeLimitedExecution.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayTask_TimeLimitedExecution

Adds time limit for running a child task
  - child task needs to be created with UGameplayTask_TimeLimitedExecution passed as TaskOwner 
  - activations are tied together and when either UGameplayTask_TimeLimitedExecution or child task is activated, other one starts as well
  - OnFinished and OnTimeExpired are mutually exclusive

## Inheritance

`UGameplayTask`

## Delegates

### `OnFinished`

```text
OnFinished() -> void
```

called when child task finishes execution before time runs out

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTimeExpired`

```text
OnTimeExpired() -> void
```

called when time runs out

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
