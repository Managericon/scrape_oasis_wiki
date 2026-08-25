---
id: "api:class:UMeshComponent"
title: "UMeshComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMeshComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMeshComponent

MeshComponent is an abstract base for any component that is an instance of a renderable collection of triangles.
 
  @see UStaticMeshComponent
  @see USkeletalMeshComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverrideMaterials` | `TArray < UMaterialInterface * >` | Per-Component material overrides.  These must NOT be set directly or a race condition can occur between GC and the rendering thread. |
| `OverlayMaterial` | `UMaterialInterface *` | Translucent material to blend on top of this mesh. Mesh will be rendered twice - once with a base material and once with overlay material |
| `IndexedOverlayMaterials` | `TArray < UMaterialInterface * >` | Overlay materials applied to each material slot. |
| `IndexedOverrideOutlineMaterials` | `TArray < UMaterialInterface * >` | Override overlay outline materials applied to each material slot. |
| `bUseIndexedOverlayMaterials` | `bool` | Whether to use IndexedOverlayMaterials (or OverlayMaterial). |
| `bUseOverlayMaterials` | `bool` | Whether to render overlay materials. (Indexed or not) |
| `OverlayMaterialMaxDrawDistance` | `float` | The max draw distance for overlay material. A distance of 0 indicates that overlay will be culled using primitive max distance. |
| `bIsEnableRetrieveDefaultMat` | `bool` | - |

## Functions

### `GetMaterials`

```text
GetMaterials() -> TArray < class UMaterialInterface * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < class UMaterialInterface * >` | - |

### `GetMaterialIndex`

```text
GetMaterialIndex(MaterialSlotName: FName) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetMaterialSlotNames`

```text
GetMaterialSlotNames() -> TArray < FName >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < FName >` | - |

### `IsMaterialSlotNameValid`

```text
IsMaterialSlotNameValid(MaterialSlotName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EnableMeshClipPlane`

```text
EnableMeshClipPlane(ClipPlane: FPlane &, PlaneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipPlane`

```text
DisableMeshClipPlane(PlaneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClipArc`

```text
EnableMeshClipArc(ClipPlane: FPlane &, ClipSphere: FVector4 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `ClipSphere` | `FVector4 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipArc`

```text
DisableMeshClipArc() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClip4Planes`

```text
EnableMeshClip4Planes(ClipPlanes: TArray < FPlane > &, bBox: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlanes` | `TArray < FPlane > &` | - |
| `bBox` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClip4Planes`

```text
DisableMeshClip4Planes() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOverlayMaterial`

```text
GetOverlayMaterial() -> UMaterialInterface *
```

Get the overlay material used by this instance

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `SetOverlayMaterial`

```text
SetOverlayMaterial(NewOverlayMaterial: UMaterialInterface *) -> void
```

Change the overlay material used by this instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOverlayMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUseIndexedOverlayMaterials`

```text
GetUseIndexedOverlayMaterials() -> bool
```

Get UseIndexedOverlayMaterials

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetUseIndexedOverlayMaterials`

```text
SetUseIndexedOverlayMaterials(bNewUseIndexedOverlayMaterials: bool) -> void
```

Set UseIndexedOverlayMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewUseIndexedOverlayMaterials` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUseOverlayMaterials`

```text
GetUseOverlayMaterials() -> bool
```

Get UseOverlayMaterials

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetUseOverlayMaterials`

```text
SetUseOverlayMaterials(bNewUseOverlayMaterials: bool) -> void
```

Set UseOverlayMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewUseOverlayMaterials` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIndexedOverlayMaterials`

```text
GetIndexedOverlayMaterials() -> TArray < class UMaterialInterface * >
```

Get IndexedOverlayMaterials

**Returns**

| Type | Description |
|---|---|
| `TArray < class UMaterialInterface * >` | - |

### `SetIndexedOverlayMaterial`

```text
SetIndexedOverlayMaterial(ElementIndex: int32, Material: UMaterialInterface *) -> void
```

Set IndexedOverlayMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOverlayMaterialMaxDrawDistance`

```text
SetOverlayMaterialMaxDrawDistance(InMaxDrawDistance: float) -> void
```

Change the overlay material max draw distance used by this instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxDrawDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIndexedOverrideOutlineMaterials`

```text
GetIndexedOverrideOutlineMaterials() -> TArray < class UMaterialInterface * >
```

Get IndexedOverrideOutlineMaterials

**Returns**

| Type | Description |
|---|---|
| `TArray < class UMaterialInterface * >` | - |

### `SetIndexedOverrideOutlineMaterials`

```text
SetIndexedOverrideOutlineMaterials(ElementIndex: int32, Material: UMaterialInterface *) -> void
```

Set IndexedOverrideOutlineMaterials

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PrestreamTextures`

```text
PrestreamTextures(Seconds: float, bPrioritizeCharacterTextures: bool, CinematicTextureGroups: int32) -> void
```

Tell the streaming system to start loading all textures with all mip-levels.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Seconds` | `float` | Number of seconds to force all mip-levels to be resident |
| `bPrioritizeCharacterTextures` | `bool` | Whether character textures should be prioritized for a while by the streaming system |
| `CinematicTextureGroups` | `int32` | Bitfield indicating which texture groups that use extra high-resolution mips |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScalarParameterValueOnMaterials`

```text
SetScalarParameterValueOnMaterials(ParameterName: FName, ParameterValue: float) -> void
```

Material parameter setting and caching 
	 Set all occurrences of Scalar Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `ParameterValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorParameterValueOnMaterials`

```text
SetVectorParameterValueOnMaterials(ParameterName: FName, ParameterValue: FVector) -> void
```

Set all occurrences of Vector Material Parameters with ParameterName in the set of materials of the SkeletalMesh to ParameterValue

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `ParameterValue` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
