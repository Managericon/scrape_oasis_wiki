---
id: "api:class:UPaperGroupedSpriteComponent"
title: "UPaperGroupedSpriteComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPaperGroupedSpriteComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPaperGroupedSpriteComponent

A component that handles rendering and collision for many instances of one or more UPaperSprite assets.
 
  @see UPrimitiveComponent, UPaperSprite

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceMaterials` | `TArray < UMaterialInterface * >` | Array of materials used by the instances |
| `PerInstanceSpriteData` | `TArray < FSpriteInstanceData >` | Array of instances |

## Functions

### `AddInstance`

```text
AddInstance(Transform: FTransform &, Sprite: UPaperSprite *, bWorldSpace: bool, Color: FLinearColor) -> int32
```

Add an instance to this component. Transform can be given either in the local space of this component or world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform &` | - |
| `Sprite` | `UPaperSprite *` | - |
| `bWorldSpace` | `bool` | - |
| `Color` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetInstanceTransform`

```text
GetInstanceTransform(InstanceIndex: int32, OutInstanceTransform: FTransform &, bWorldSpace: bool) -> bool
```

Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `OutInstanceTransform` | `FTransform &` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateInstanceTransform`

```text
UpdateInstanceTransform(InstanceIndex: int32, NewInstanceTransform: FTransform &, bWorldSpace: bool, bMarkRenderStateDirty: bool, bTeleport: bool) -> bool
```

Update the transform for the instance specified. Instance is given in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `NewInstanceTransform` | `FTransform &` | - |
| `bWorldSpace` | `bool` | - |
| `bMarkRenderStateDirty` | `bool` | - |
| `bTeleport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateInstanceColor`

```text
UpdateInstanceColor(InstanceIndex: int32, NewInstanceColor: FLinearColor, bMarkRenderStateDirty: bool) -> bool
```

Update the color for the instance specified. Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `NewInstanceColor` | `FLinearColor` | - |
| `bMarkRenderStateDirty` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveInstance`

```text
RemoveInstance(InstanceIndex: int32) -> bool
```

Remove the instance specified. Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearInstances`

```text
ClearInstances() -> void
```

Clear all instances being rendered by this component

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceCount`

```text
GetInstanceCount() -> int32
```

Get the number of instances in this component

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SortInstancesAlongAxis`

```text
SortInstancesAlongAxis(WorldSpaceSortAxis: FVector) -> void
```

Sort all instances by their world space position along the specified axis

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldSpaceSortAxis` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
