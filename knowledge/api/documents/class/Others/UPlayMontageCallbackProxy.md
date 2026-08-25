---
id: "api:class:UPlayMontageCallbackProxy"
title: "UPlayMontageCallbackProxy"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPlayMontageCallbackProxy.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPlayMontageCallbackProxy

## Inheritance

`UObject`

## Functions

### `CreateProxyObjectForPlayMontage`

```text
CreateProxyObjectForPlayMontage(InSkeletalMeshComponent: USkeletalMeshComponent *, MontageToPlay: UAnimMontage *, PlayRate: float, StartingPosition: float, StartingSection: FName) -> UPlayMontageCallbackProxy *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSkeletalMeshComponent` | `USkeletalMeshComponent *` | - |
| `MontageToPlay` | `UAnimMontage *` | - |
| `PlayRate` | `float` | - |
| `StartingPosition` | `float` | - |
| `StartingSection` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UPlayMontageCallbackProxy *` | - |

### `OnMontageBlendingOut`

```text
OnMontageBlendingOut(Montage: UAnimMontage *, bInterrupted: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageEnded`

```text
OnMontageEnded(Montage: UAnimMontage *, bInterrupted: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyBeginReceived`

```text
OnNotifyBeginReceived(NotifyName: FName, BranchingPointNotifyPayload: FBranchingPointNotifyPayload &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |
| `BranchingPointNotifyPayload` | `FBranchingPointNotifyPayload &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyEndReceived`

```text
OnNotifyEndReceived(NotifyName: FName, BranchingPointNotifyPayload: FBranchingPointNotifyPayload &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |
| `BranchingPointNotifyPayload` | `FBranchingPointNotifyPayload &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCompleted`

```text
OnCompleted(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBlendOut`

```text
OnBlendOut(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInterrupted`

```text
OnInterrupted(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyBegin`

```text
OnNotifyBegin(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyEnd`

```text
OnNotifyEnd(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
