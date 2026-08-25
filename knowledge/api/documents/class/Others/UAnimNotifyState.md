---
id: "api:class:UAnimNotifyState"
title: "UAnimNotifyState"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimNotifyState

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InOldFPPAnimMode_ChangeToNewFPPMesh` | `bool` | - |
| `bEnableBoneRetargetAdaptFeature` | `bool` | - |
| `bCheckAnimIsolation` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP` | `bool` | - |
| `bCheckAnimIsolation_OnlyNewFPP_IgnoreOldAnimMode` | `bool` | - |
| `bCheckAnimIsolation_OnlyTPP` | `bool` | 仅在TPP（第三人称）下生效，开启后此NotifyState只会在TPP AnimInstance中触发 |

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

### `Received_NotifyBegin`

```text
Received_NotifyBegin(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, TotalDuration: float, InvokeAnimInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |
| `TotalDuration` | `float` | - |
| `InvokeAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Received_NotifyTick`

```text
Received_NotifyTick(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, FrameDeltaTime: float, InvokeAnimInstance: UAnimInstance *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `Animation` | `UAnimSequenceBase *` | - |
| `FrameDeltaTime` | `float` | - |
| `InvokeAnimInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Received_NotifyEnd`

```text
Received_NotifyEnd(MeshComp: USkeletalMeshComponent *, Animation: UAnimSequenceBase *, InvokeAnimInstance: UAnimInstance *) -> bool
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

### `TryGetNewFPPAdaptSkelMeshComp`

```text
TryGetNewFPPAdaptSkelMeshComp(InTargetSkelMeshComp: USkeletalMeshComponent *, InIsInitCall: bool, HasRetarget: bool, ForceGetFPPMesh: bool) -> USkeletalMeshComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InIsInitCall` | `bool` | - |
| `HasRetarget` | `bool` | - |
| `ForceGetFPPMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshComponent *` | - |

### `TryGetBoneRetargetAdaptSkelMeshComp`

```text
TryGetBoneRetargetAdaptSkelMeshComp(InTargetSkelMeshComp: USkeletalMeshComponent *, InIsInitCall: bool) -> USkeletalMeshComponent *
```

For Bone Retarget Feature Start

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InIsInitCall` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshComponent *` | - |

### `ClearBoneRetargetAdaptState`

```text
ClearBoneRetargetAdaptState(InTargetSkelMeshComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBoneRetargetAdaptInitDone`

```text
IsBoneRetargetAdaptInitDone(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsEnableBoneRetargetAdaptFeature`

```text
IsEnableBoneRetargetAdaptFeature(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
