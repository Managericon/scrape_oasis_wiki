---
id: "api:class:UBillboardComponent"
title: "UBillboardComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBillboardComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBillboardComponent

A 2d texture that will be rendered always facing the camera.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sprite` | `UTexture2D *` | - |
| `bIsScreenSizeScaled` | `uint32` | - |
| `ScreenSize` | `float` | - |
| `U` | `float` | - |
| `UL` | `float` | - |
| `V` | `float` | - |
| `VL` | `float` | - |
| `SpriteCategoryName_DEPRECATED` | `FName` | Sprite category that the component belongs to. Value serves as a key into the localization file. |
| `SpriteInfo` | `FSpriteCategoryInfo` | Sprite category information regarding the component |
| `bUseInEditorScaling` | `bool` | Whether to use in-editor arrow scaling (i.e. to be affected by the global arrow scale) |

## Functions

### `SetSprite`

```text
SetSprite(NewSprite: UTexture2D *) -> void
```

Change the sprite texture used by this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSprite` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUV`

```text
SetUV(NewU: int32, NewUL: int32, NewV: int32, NewVL: int32) -> void
```

Change the sprite's UVs

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewU` | `int32` | - |
| `NewUL` | `int32` | - |
| `NewV` | `int32` | - |
| `NewVL` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpriteAndUV`

```text
SetSpriteAndUV(NewSprite: UTexture2D *, NewU: int32, NewUL: int32, NewV: int32, NewVL: int32) -> void
```

Change the sprite texture and the UV's used by this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSprite` | `UTexture2D *` | - |
| `NewU` | `int32` | - |
| `NewUL` | `int32` | - |
| `NewV` | `int32` | - |
| `NewVL` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
