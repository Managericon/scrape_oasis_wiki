---
id: "api:class:UPoseableMeshComponent"
title: "UPoseableMeshComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPoseableMeshComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPoseableMeshComponent

UPoseableMeshComponent that allows bone transforms to be driven by blueprint.

## Inheritance

`USkinnedMeshComponent`

## Functions

### `SetBoneTransformByName`

```text
SetBoneTransformByName(BoneName: FName, InTransform: FTransform &, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InTransform` | `FTransform &` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoneLocationByName`

```text
SetBoneLocationByName(BoneName: FName, InLocation: FVector, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InLocation` | `FVector` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoneRotationByName`

```text
SetBoneRotationByName(BoneName: FName, InRotation: FRotator, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InRotation` | `FRotator` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoneScaleByName`

```text
SetBoneScaleByName(BoneName: FName, InScale3D: FVector, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InScale3D` | `FVector` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoneTransformByName`

```text
GetBoneTransformByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetBoneLocationByName`

```text
GetBoneLocationByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetBoneRotationByName`

```text
GetBoneRotationByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetBoneScaleByName`

```text
GetBoneScaleByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ResetBoneTransformByName`

```text
ResetBoneTransformByName(BoneName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyPoseFromSkeletalComponent`

```text
CopyPoseFromSkeletalComponent(InComponentToCopy: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponentToCopy` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
