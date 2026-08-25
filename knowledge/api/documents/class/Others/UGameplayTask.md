---
id: "api:class:UGameplayTask"
title: "UGameplayTask"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayTask

## Inheritance

`UObject` -> `IGameplayTaskOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceName` | `FName` | This name allows us to find the task later so that we can end it. |
| `ResourceOverlapPolicy` | `ETaskResourceOverlapPolicy` | - |
| `ChildTask` | `UGameplayTask *` | child task instance |

## Functions

### `ReadyForActivation`

```text
ReadyForActivation() -> void
```

Called to trigger the actual task once the delegates have been set up

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EndTask`

```text
EndTask() -> void
```

Called explicitly to end the task (usually by the task itself). Calls OnDestroy.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
