---
id: "api:class:UDecalBakingParameterComponent"
title: "UDecalBakingParameterComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDecalBakingParameterComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDecalBakingParameterComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DecalTexture` | `UTexture2D *` | - |
| `DecalSize` | `FVector` | - |
| `UVScaleBias` | `FVector4` | - |
| `TintColor` | `FLinearColor` | - |
| `CropUVScaleBias` | `FVector4` | - |
| `CropRotation` | `float` | - |
| `bEnableDepthCompare` | `bool` | - |

## Functions

### `GetUVScaleBias`

```text
GetUVScaleBias() -> FORCEINLINE FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FORCEINLINE FLinearColor` | - |

### `GetCropUVScaleBias`

```text
GetCropUVScaleBias() -> FORCEINLINE FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FORCEINLINE FLinearColor` | - |

### `GetDecalBounds`

```text
GetDecalBounds() -> FBoxSphereBounds
```

**Returns**

| Type | Description |
|---|---|
| `FBoxSphereBounds` | - |

## Language

`cpp`
