---
id: "api:class:UDecalComponent"
title: "UDecalComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDecalComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDecalComponent

A material that is rendered onto the surface of a mesh. A kind of 'bumper sticker' for a model.
 
  @see UDecalActor

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DecalMaterial` | `UMaterialInterface *` | Decal material. |
| `SortOrder` | `int32` | Controls the order in which decal elements are rendered.  Higher values draw later (on top). <br>	  Setting many different sort orders on many different decals prevents sorting by state and can reduce performance. |
| `FadeScreenSize` | `float` | - |
| `FadeStartDelay` | `float` | Time in seconds to wait before beginning to fade out the decal. Set fade duration and start delay to 0 to make persistent. |
| `FadeDuration` | `float` | Time in seconds for the decal to fade out. Set fade duration and start delay to 0 to make persistent. Only fades in active simulation or game. |
| `bDestroyOwnerAfterFade` | `uint8` | Automatically destroys the owning actor after fully fading out. |
| `bDrawToTerrainVT` | `uint8` | - |
| `DecalSize` | `FVector` | Decal size in local space (does not include the component scale), technically redundant but there for convenience |
| `PreviewSurfaceMaterial` | `UMaterialInterface *` | ES31 管线下 Decal Mesh 预览：Surface 域母材质 |
| `bAutoGeneratePreview` | `bool` | 是否在 Transform  DecalSize  Preview 参数变化时自动重新生成 Preview Mesh |
| `SkylightIntensityScale` | `float` | Preview Mesh 的天光强度缩放系数 |
| `TintColor` | `FLinearColor` | Preview  正式 Mesh 的 TintColor，写入顶点色 |
| `bDecalHiddenByPreview` | `bool` | 当前组件是否被 Preview Mesh 隐藏，用于 Clear  PostLoad 恢复 |
| `bBakeWithLandscape` | `uint8` | Whether bake decal to the landscape flatten material |

## Functions

### `SetDrawToTerrainVT`

```text
SetDrawToTerrainVT(DrawToTerrainVT: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DrawToTerrainVT` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFadeStartDelay`

```text
GetFadeStartDelay() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetFadeDuration`

```text
GetFadeDuration() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetFadeOut`

```text
SetFadeOut(StartDelay: float, Duration: float, DestroyOwnerAfterFade: bool) -> void
```

Sets the decal's fade start time, duration and if the owning actor should be destroyed after the decal is fully faded out.
	 The default value of 0 for FadeStartDelay and FadeDuration makes the decal persistent. See DecalLifetimeOpacity material 
	 node to control the look of "fading out."

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartDelay` | `float` | - Time in seconds to wait before beginning to fade out the decal. |
| `Duration` | `float` | - Time in second for the decal to fade out. |
| `DestroyOwnerAfterFade` | `bool` | - Should the owning actor automatically be destroyed after it is completely faded out. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFadeScreenSize`

```text
SetFadeScreenSize(NewFadeScreenSize: float) -> void
```

Set the FadeScreenSize for this decal component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFadeScreenSize` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSortOrder`

```text
SetSortOrder(Value: int32) -> void
```

Sets the sort order for the decal component. Higher values draw later (on top). This will force the decal to reattach

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDecalMaterial`

```text
SetDecalMaterial(NewDecalMaterial: UMaterialInterface *) -> void
```

setting decal material on decal component. This will force the decal to reattach

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDecalMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDecalMaterial`

```text
GetDecalMaterial() -> UMaterialInterface *
```

Accessor for decal material

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `CreateDynamicMaterialInstance`

```text
CreateDynamicMaterialInstance() -> UMaterialInstanceDynamic *
```

Utility to allocate a new Dynamic Material Instance, set its parent to the currently applied material, and assign it

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

## Language

`cpp`
