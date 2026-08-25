---
id: "api:class:UStereoLayerComponent"
title: "UStereoLayerComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UStereoLayerComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UStereoLayerComponent

A geometry layer within the stereo rendered viewport.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bLiveTexture` | `uint32` | True if the stereo layer texture needs to update itself every frame(scene capture, video, etc.) |
| `bSupportsDepth` | `uint32` | True if the stereo layer needs to support depth intersections with the scene geometry, if available on the platform |
| `bNoAlphaChannel` | `uint32` | True if the texture should not use its own alpha channel (1.0 will be substituted) |
| `Texture` | `UTexture *` | Texture displayed on the stereo layer (is stereocopic textures are supported on the platfrom and more than one texture is provided, this will be the right eye) |
| `LeftTexture` | `UTexture *` | Texture displayed on the stereo layer for left eye, if stereoscopic textures are supported on the platform |
| `bQuadPreserveTextureRatio` | `uint32` | True if the quad should internally set it's Y value based on the set texture's dimensions |
| `QuadSize` | `FVector2D` | Size of the rendered stereo layer quad |
| `UVRect` | `FBox2D` | UV coordinates mapped to the quad face |
| `CylinderRadius` | `float` | Radial size of the rendered stereo layer cylinder |
| `CylinderOverlayArc` | `float` | Arc angle for the stereo layer cylinder |
| `CylinderHeight` | `int` | Height of the stereo layer cylinder |
| `StereoLayerType` | `TEnumAsByte < enum EStereoLayerType >` | Specifies how and where the quad is rendered to the screen |
| `StereoLayerShape` | `TEnumAsByte < enum EStereoLayerShape >` | Specifies which type of layer it is.  Note that some shapes will be supported only on certain platforms! |
| `Priority` | `int32` | Render priority among all stereo layers, higher priority render on top of lower priority |

## Functions

### `SetTexture`

```text
SetTexture(InTexture: UTexture *) -> void
```

Change the texture displayed on the stereo layer quad

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTexture`

```text
GetTexture() -> UTexture *
```

**Returns**

| Type | Description |
|---|---|
| `UTexture *` | - |

### `SetQuadSize`

```text
SetQuadSize(InQuadSize: FVector2D) -> void
```

Change the quad size. This is the unscaled height and width, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InQuadSize` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetQuadSize`

```text
GetQuadSize() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetUVRect`

```text
SetUVRect(InUVRect: FBox2D) -> void
```

Change the UV coordinates mapped to the quad face

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUVRect` | `FBox2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUVRect`

```text
GetUVRect() -> FBox2D
```

**Returns**

| Type | Description |
|---|---|
| `FBox2D` | - |

### `SetPriority`

```text
SetPriority(InPriority: int32) -> void
```

Change the layer's render priority, higher priorities render on top of lower priorities

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPriority` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPriority`

```text
GetPriority() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `MarkTextureForUpdate`

```text
MarkTextureForUpdate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
