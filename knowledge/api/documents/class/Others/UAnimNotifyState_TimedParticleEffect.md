---
id: "api:class:UAnimNotifyState_TimedParticleEffect"
title: "UAnimNotifyState_TimedParticleEffect"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimNotifyState_TimedParticleEffect.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimNotifyState_TimedParticleEffect

## Inheritance

`UAnimNotifyState`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PSTemplate` | `UParticleSystem *` | - |
| `bIsPlayInWorld` | `bool` | - |
| `bIsRelativeToMeshSocketInWorld` | `bool` | - |
| `SocketName` | `FName` | - |
| `LocationOffset` | `FVector` | - |
| `RotationOffset` | `FRotator` | - |
| `RotationOffsetDisable` | `uint32` | - |
| `ScaleDisable` | `uint32` | - |
| `ScaleMultiplier` | `FVector` | - |
| `bDestroyAtEnd` | `bool` | - |
| `bEnableAttachMeshChangeIgnoreSocketCheck` | `bool` | - |
| `bAdaptToNewFPP` | `bool` | - |
| `CacheAttachAdaptMeshComp` | `TWeakObjectPtr < USkeletalMeshComponent >` | - |
| `SimulatedActivationOfQualityLevel` | `int32` | - |
| `CurveParamList` | `TMap < FName , FCurveParams >` | - |
| `ParticleComp` | `UParticleSystemComponent *` | - |
| `bNotifyControlParticleVisible` | `bool` | - |
| `bEnableSpawnObjTrackFeature` | `bool` | - |
| `bAddAnotherBone_Z_Delta` | `bool` | - |
| `Z_Delta_BoneName` | `FName` | - |
| `ParticleTag` | `FName` | - |
| `SpawnedObjCacheMap` | `TMap < FName , TWeakObjectPtr < UObject > >` | - |
| `bSkipSocketNameCheck` | `bool` | - |
| `EnableDestoryByUniqueTagAtEnd` | `bool` | - |
| `PreviousPSTemplates` | `TArray < UParticleSystem * >` | - |
| `PreviousSocketNames` | `TArray < FName >` | - |
| `bInDebugMode` | `bool` | - |
| `CurrentLocationOffset` | `FVector` | - |
| `CurrentRotationOffset` | `FRotator` | - |
| `CurrentScaleMultiplier` | `FVector` | - |
| `CachedSpawnedParticleComponent` | `UParticleSystemComponent *` | - |

## Functions

### `IsEnableSpawnObjTrackFeature`

```text
IsEnableSpawnObjTrackFeature() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TryMarkSpawnObjTracker`

```text
TryMarkSpawnObjTracker(InTargetSkelMeshComp: USkeletalMeshComponent *, InSpawnedObj: UObject *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InSpawnedObj` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TryClearSpawnObjTracker`

```text
TryClearSpawnObjTracker(InTargetSkelMeshComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsTrackingObj`

```text
IsTrackingObj(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOverrideParticleTemplate`

```text
GetOverrideParticleTemplate(InTargetSkelMeshComp: USkeletalMeshComponent *, InPSTemplate: UParticleSystem *) -> UParticleSystem *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `InPSTemplate` | `UParticleSystem *` | - |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystem *` | - |

### `GetOverrideParticleWorldTransform`

```text
GetOverrideParticleWorldTransform(InTargetSkelMeshComp: USkeletalMeshComponent *, TargetTransform: FTransform) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |
| `TargetTransform` | `FTransform` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `InnerCheckParticleParentVisibility`

```text
InnerCheckParticleParentVisibility(skComp: USkeletalMeshComponent *, InPSC: UParticleSystemComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `skComp` | `USkeletalMeshComponent *` | - |
| `InPSC` | `UParticleSystemComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckParticleParentVisibility`

```text
CheckParticleParentVisibility(InComponent: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsEnableSearchAllDescendants`

```text
IsEnableSearchAllDescendants(InTargetSkelMeshComp: USkeletalMeshComponent *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SearchChildrenParticleAndDestroy`

```text
SearchChildrenParticleAndDestroy(Children: TArray < USceneComponent * >, MeshComp: USkeletalMeshComponent *, AttachAdaptMeshComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Children` | `TArray < USceneComponent * >` | - |
| `MeshComp` | `USkeletalMeshComponent *` | - |
| `AttachAdaptMeshComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
