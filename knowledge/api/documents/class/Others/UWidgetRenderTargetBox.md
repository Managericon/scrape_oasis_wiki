---
id: "api:class:UWidgetRenderTargetBox"
title: "UWidgetRenderTargetBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetRenderTargetBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetRenderTargetBox

Renders its single child widget into a transparent render target.
 
  It redraws the child widget into an offscreen RT, so pixels where
  no child UI is drawn stay transparent (alpha = 0).

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderTarget` | `UTextureRenderTarget2D *` | Optional external render target. If unset and bAutoCreateRenderTarget is true, a transient RT is created. |
| `bRenderEnabled` | `bool` | Whether to render the child widget into the RT. |
| `bRenderEveryFrame` | `bool` | Redraw the child widget into the RT every paint. Disable this for static UI and call RequestRender when content changes. |
| `bAutoCreateRenderTarget` | `bool` | Create an internal transient render target if RenderTarget is not set. |
| `bAutoResizeRenderTarget` | `bool` | Resize the active RT to match the childwidget draw size. |
| `bMatchWidgetSize` | `bool` | Match RT size to this widget's allotted size in pixels. If false, FixedRenderTargetSize is used. |
| `FixedRenderTargetSize` | `FIntPoint` | RT size used when bMatchWidgetSize is false. |
| `RenderTargetFormat` | `TEnumAsByte < enum ETextureRenderTargetFormat >` | Pixel format used when creatingresizing the RT. |
| `ClearColor` | `FLinearColor` | Clear color. Use transparent to keep areas with no UI at alpha = 0. |
| `bDrawToScreen` | `bool` | Also draw the produced RT back to this widget's screen rect. Usually false for mesh sampling workflows. |
| `DisplayMaterial` | `UMaterialInterface *` | Optional UI material used only when bDrawToScreen is true. |
| `TextureParameterName` | `FName` | Texture parameter name used by DisplayMaterial. |
| `ColorAndOpacity` | `FLinearColor` | Tint used only when bDrawToScreen is true. |
| `OwnedRenderTarget` | `UTextureRenderTarget2D *` | - |
| `DynamicDisplayMaterial` | `UMaterialInstanceDynamic *` | - |
| `DisplayBrush` | `FSlateBrush` | - |

## Functions

### `GetActiveRenderTarget`

```text
GetActiveRenderTarget() -> UTextureRenderTarget2D *
```

Returns the external RT if set, otherwise the internally created RT.

**Returns**

| Type | Description |
|---|---|
| `UTextureRenderTarget2D *` | - |

### `RefreshDisplayResource`

```text
RefreshDisplayResource() -> void
```

Forces the RT display brushmaterial to refresh.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestRender`

```text
RequestRender() -> void
```

Request the child widget be redrawn into the render target on the next paint.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
