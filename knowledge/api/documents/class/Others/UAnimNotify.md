---
id: "api:class:UAnimNotify"
title: "UAnimNotify"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimNotify.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimNotify

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCheckAnimIsolation` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP_IgnoreOldAnimMode` | `bool` | - |

## Functions

### `GetNotifyName`

```text
GetNotifyName() -> FString
```

Implementable event to get a custom name for the notify

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Received_Notify`

```text
Received_Notify(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, InvokeAnimInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |
| `InvokeAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
