---
id: "api:class:UCanvas"
title: "UCanvas"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCanvas.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCanvas

A drawing canvas.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OrgX` | `float` | - |
| `OrgY` | `float` | - |
| `ClipX` | `float` | - |
| `ClipY` | `float` | - |
| `DrawColor` | `FColor` | - |
| `bCenterX` | `uint32` | - |
| `bCenterY` | `uint32` | - |
| `bNoSmooth` | `uint32` | - |
| `SizeX` | `int32` | - |
| `SizeY` | `int32` | - |
| `ColorModulate` | `FPlane` | - |
| `DefaultTexture` | `UTexture2D *` | - |
| `GradientTexture0` | `UTexture2D *` | - |
| `ReporterGraph` | `UReporterGraph *` | Helper class to render 2d graphs on canvas |

## Functions

### `K2_DrawLine`

```text
K2_DrawLine(ScreenPositionA: FVector2D, ScreenPositionB: FVector2D, Thickness: float, RenderColor: FLinearColor) -> void
```

Draws a line on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenPositionA` | `FVector2D` | Starting position of the line in screen space. |
| `ScreenPositionB` | `FVector2D` | Ending position of the line in screen space. |
| `Thickness` | `float` | How many pixels thick this line should be. |
| `RenderColor` | `FLinearColor` | Color to render the line. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawTexture`

```text
K2_DrawTexture(RenderTexture: UTexture *, ScreenPosition: FVector2D, ScreenSize: FVector2D, CoordinatePosition: FVector2D, CoordinateSize: FVector2D, RenderColor: FLinearColor, BlendMode: EBlendMode, Rotation: float, PivotPoint: FVector2D) -> void
```

Draws a texture on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTexture` | `UTexture *` | Texture to use when rendering. If no texture is set then this will use the default white texture. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the texture. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `CoordinatePosition` | `FVector2D` | Normalized UV starting coordinate to use when rendering the texture. |
| `CoordinateSize` | `FVector2D` | Normalized UV size coordinate to use when rendering the texture. |
| `RenderColor` | `FLinearColor` | Color to use when rendering the texture. |
| `BlendMode` | `EBlendMode` | Blending mode to use when rendering the texture. |
| `Rotation` | `float` | Rotation, in degrees, to render the texture. |
| `PivotPoint` | `FVector2D` | Normalized pivot point to use when rotating the texture. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawMaterial`

```text
K2_DrawMaterial(RenderMaterial: UMaterialInterface *, ScreenPosition: FVector2D, ScreenSize: FVector2D, CoordinatePosition: FVector2D, CoordinateSize: FVector2D, Rotation: float, PivotPoint: FVector2D) -> void
```

Draws a material on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderMaterial` | `UMaterialInterface *` | Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the texture. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `CoordinatePosition` | `FVector2D` | Normalized UV starting coordinate to use when rendering the texture. |
| `CoordinateSize` | `FVector2D` | Normalized UV size coordinate to use when rendering the texture. |
| `Rotation` | `float` | Rotation, in degrees, to render the texture. |
| `PivotPoint` | `FVector2D` | Normalized pivot point to use when rotating the texture. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawText`

```text
K2_DrawText(RenderFont: UFont *, RenderText: FString &, ScreenPosition: FVector2D, RenderColor: FLinearColor, Kerning: float, ShadowColor: FLinearColor, ShadowOffset: FVector2D, bCentreX: bool, bCentreY: bool, bOutlined: bool, OutlineColor: FLinearColor) -> void
```

Draws text on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderFont` | `UFont *` | Font to use when rendering the text. If this is null, then a default engine font is used. |
| `RenderText` | `FString &` | Text to render on the Canvas. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the text. |
| `RenderColor` | `FLinearColor` | Color to render the text. |
| `Kerning` | `float` | Horizontal spacing adjustment to modify the spacing between each letter. |
| `ShadowColor` | `FLinearColor` | Color to render the shadow of the text. |
| `ShadowOffset` | `FVector2D` | Pixel offset relative to the screen space position to render the shadow of the text. |
| `bCentreX` | `bool` | If true, then interpret the screen space position X coordinate as the center of the rendered text. |
| `bCentreY` | `bool` | If true, then interpret the screen space position Y coordinate as the center of the rendered text. |
| `bOutlined` | `bool` | If true, then the text should be rendered with an outline. |
| `OutlineColor` | `FLinearColor` | Color to render the outline for the text. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawBorder`

```text
K2_DrawBorder(BorderTexture: UTexture *, BackgroundTexture: UTexture *, LeftBorderTexture: UTexture *, RightBorderTexture: UTexture *, TopBorderTexture: UTexture *, BottomBorderTexture: UTexture *, ScreenPosition: FVector2D, ScreenSize: FVector2D, CoordinatePosition: FVector2D, CoordinateSize: FVector2D, RenderColor: FLinearColor, BorderScale: FVector2D, BackgroundScale: FVector2D, Rotation: float, PivotPoint: FVector2D, CornerSize: FVector2D) -> void
```

Draws a 3x3 grid border with tiled frame and tiled interior on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BorderTexture` | `UTexture *` | Texture to use for border. |
| `BackgroundTexture` | `UTexture *` | Texture to use for border background. |
| `LeftBorderTexture` | `UTexture *` | Texture to use for the tiling left border. |
| `RightBorderTexture` | `UTexture *` | Texture to use for the tiling right border. |
| `TopBorderTexture` | `UTexture *` | Texture to use for the tiling top border. |
| `BottomBorderTexture` | `UTexture *` | Texture to use for the tiling bottom border. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the texture. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `CoordinatePosition` | `FVector2D` | Normalized UV starting coordinate to use when rendering the border texture. |
| `CoordinateSize` | `FVector2D` | Normalized UV size coordinate to use when rendering the border texture. |
| `RenderColor` | `FLinearColor` | Color to tint the border. |
| `BorderScale` | `FVector2D` | Scale of the border. |
| `BackgroundScale` | `FVector2D` | Scale of the background. |
| `Rotation` | `float` | Rotation, in degrees, to render the texture. |
| `PivotPoint` | `FVector2D` | Normalized pivot point to use when rotating the texture. |
| `CornerSize` | `FVector2D` | Frame corner size in percent of frame texture (should be < 0.5f). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawBox`

```text
K2_DrawBox(ScreenPosition: FVector2D, ScreenSize: FVector2D, Thickness: float) -> void
```

Draws an unfilled box on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenPosition` | `FVector2D` | Screen space position to render the text. |
| `ScreenSize` | `FVector2D` | Screen space size to render the texture. |
| `Thickness` | `float` | How many pixels thick the box lines should be. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawTriangle`

```text
K2_DrawTriangle(RenderTexture: UTexture *, Triangles: TArray < FCanvasUVTri >) -> void
```

Draws a set of triangles on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTexture` | `UTexture *` | Texture to use when rendering the triangles. If no texture is set, then the default white texture is used. |
| `Triangles` | `TArray < FCanvasUVTri >` | Triangles to render. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawMaterialTriangle`

```text
K2_DrawMaterialTriangle(RenderMaterial: UMaterialInterface *, Triangles: TArray < FCanvasUVTri >) -> void
```

Draws a set of triangles on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderMaterial` | `UMaterialInterface *` | Material to use when rendering. Remember that only the emissive channel is able to be rendered as no lighting is performed when rendering to the Canvas. |
| `Triangles` | `TArray < FCanvasUVTri >` | Triangles to render. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DrawPolygon`

```text
K2_DrawPolygon(RenderTexture: UTexture *, ScreenPosition: FVector2D, Radius: FVector2D, NumberOfSides: int32, RenderColor: FLinearColor) -> void
```

Draws a polygon on the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTexture` | `UTexture *` | Texture to use when rendering the triangles. If no texture is set, then the default white texture is used. |
| `ScreenPosition` | `FVector2D` | Screen space position to render the text. |
| `Radius` | `FVector2D` | How large in pixels this polygon should be. |
| `NumberOfSides` | `int32` | How many sides this polygon should have. This should be above or equal to three. |
| `RenderColor` | `FLinearColor` | Color to tint the polygon. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_Project`

```text
K2_Project(WorldLocation: FVector) -> FVector
```

Performs a projection of a world space coordinates using the projection matrix set up for the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector` | World space location to project onto the Canvas rendering plane. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Returns a vector where X, Y defines a screen space position representing the world space location. |

### `K2_Deproject`

```text
K2_Deproject(ScreenPosition: FVector2D, WorldOrigin: FVector &, WorldDirection: FVector &) -> void
```

Performs a deprojection of a screen space coordinate using the projection matrix set up for the Canvas.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScreenPosition` | `FVector2D` | Screen space position to deproject to the World. |
| `WorldOrigin` | `FVector &` | Vector which is the world position of the screen space position. |
| `WorldDirection` | `FVector &` | Vector which can be used in a trace to determine what is "behind" the screen space position. Useful for object picking. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_StrLen`

```text
K2_StrLen(RenderFont: UFont *, RenderText: FString &) -> FVector2D
```

Returns the wrapped text size in screen space coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderFont` | `UFont *` | Font to use when determining the size of the text. If this is null, then a default engine font is used. |
| `RenderText` | `FString &` | Text to determine the size of. |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Returns the screen space size of the text. |

### `K2_TextSize`

```text
K2_TextSize(RenderFont: UFont *, RenderText: FString &, Scale: FVector2D) -> FVector2D
```

Returns the clipped text size in screen space coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderFont` | `UFont *` | Font to use when determining the size of the text. If this is null, then a default engine font is used. |
| `RenderText` | `FString &` | Text to determine the size of. |
| `Scale` | `FVector2D` | Scale of the font to use when determining the size of the text. |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Returns the screen space size of the text. |

## Language

`cpp`
