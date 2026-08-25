---
id: "api:class:UKismetAnimationLibrary"
title: "UKismetAnimationLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetAnimationLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetAnimationLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `K2_TwoBoneIK`

```text
K2_TwoBoneIK(RootPos: FVector &, JointPos: FVector &, EndPos: FVector &, JointTarget: FVector &, Effector: FVector &, OutJointPos: FVector &, OutEndPos: FVector &, bAllowStretching: bool, StartStretchRatio: float, MaxStretchScale: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RootPos` | `FVector &` | - |
| `JointPos` | `FVector &` | - |
| `EndPos` | `FVector &` | - |
| `JointTarget` | `FVector &` | - |
| `Effector` | `FVector &` | - |
| `OutJointPos` | `FVector &` | - |
| `OutEndPos` | `FVector &` | - |
| `bAllowStretching` | `bool` | - |
| `StartStretchRatio` | `float` | - |
| `MaxStretchScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_LookAt`

```text
K2_LookAt(CurrentTransform: FTransform &, TargetPosition: FVector &, LookAtVector: FVector, bUseUpVector: bool, UpVector: FVector, ClampConeInDegree: float) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentTransform` | `FTransform &` | - |
| `TargetPosition` | `FVector &` | - |
| `LookAtVector` | `FVector` | - |
| `bUseUpVector` | `bool` | - |
| `UpVector` | `FVector` | - |
| `ClampConeInDegree` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

## Language

`cpp`
