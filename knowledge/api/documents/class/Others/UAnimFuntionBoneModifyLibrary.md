---
id: "api:class:UAnimFuntionBoneModifyLibrary"
title: "UAnimFuntionBoneModifyLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimFuntionBoneModifyLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimFuntionBoneModifyLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Prototype_BoneModifyFuntion`

```text
Prototype_BoneModifyFuntion(Context: FBPAnimComponentSpacePoseContext &, AdditionalPoseBPContext: TArray < FBPAnimComponentSpacePoseContext > &, OutBoneModifyData: TArray < FFunctionBoneModifyData > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FBPAnimComponentSpacePoseContext &` | - |
| `AdditionalPoseBPContext` | `TArray < FBPAnimComponentSpacePoseContext > &` | - |
| `OutBoneModifyData` | `TArray < FFunctionBoneModifyData > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoneTransformLocalSpace`

```text
GetBoneTransformLocalSpace(Context: FBPAnimComponentSpacePoseContext &, BoneName: FName) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FBPAnimComponentSpacePoseContext &` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetBoneTransformComponentSpace`

```text
GetBoneTransformComponentSpace(Context: FBPAnimComponentSpacePoseContext &, BoneName: FName) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FBPAnimComponentSpacePoseContext &` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

## Language

`cpp`
