---
id: "api:class:UWidgetComponent"
title: "UWidgetComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetComponent

The widget component provides a surface in the 3D environment on which to render widgets normally rendered to the screen.
  Widgets are first rendered to a render target, then that render target is displayed in the world.
 
  Material Properties set by this component on whatever material overrides the default.
  SlateUI [Texture]
  BackColor [Vector]
  TintColorAndOpacity [Vector]
  OpacityFromTexture [Scalar]

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Space` | `EWidgetSpace` | The coordinate space in which to render the widget |
| `TimingPolicy` | `EWidgetTimingPolicy` | How this widget should deal with timing, pausing, etc. |
| `WidgetClass` | `TSubclassOf < UUserWidget >` | The class of User Widget to create and display an instance of |
| `DrawSize` | `FIntPoint` | The size of the displayed quad. |
| `bManuallyRedraw` | `bool` | Should we wait to be told to redraw to actually draw? |
| `bCheckLowDeviceQualityLevel` | `bool` | Should LowDevice Phone draw UI? |
| `bRedrawRequested` | `bool` | Has anyone requested we redraw? |
| `RedrawTime` | `float` | The time in between draws, if 0 - we would redraw every frame.  If 1, we would redraw every second.<br>	  This will work with bManuallyRedraw as well.  So you can say, manually redraw, but only redraw at this<br>	  maximum rate. |
| `CurrentDrawSize` | `FIntPoint` | The actual draw size, this changes based on DrawSize - or the desired size of the widget if<br>	  bDrawAtDesiredSize is true. |
| `bDrawAtDesiredSize` | `bool` | Causes the render target to automatically match the desired size.<br>	 <br>	  WARNING: If you change this every frame, it will be very expensive.  If you need<br>	     that effect, you should keep the outer widget's sized locked and dynamically<br>	     scale or resize some inner widget. |
| `Pivot` | `FVector2D` | The AlignmentPivot point that the widget is placed at relative to the position. |
| `bReceiveHardwareInput` | `bool` | Register with the viewport for hardware input from the true mouse and keyboard.  These widgets<br>	  will more or less react like regular 2D widgets in the viewport, e.g. they can and will steal focus<br>	  from the viewport.<br>	 <br>	  WARNING: If you are making a VR game, definitely do not change this to true.  This option should ONLY be used<br>	  if you're making what would otherwise be a normal menu for a game, just in 3D.  If you also need the game to<br>	  remain responsive and for the player to be able to interact with UI and move around the world (such as a keypad on a door),<br>	  use the WidgetInteractionComponent instead. |
| `bWindowFocusable` | `bool` | Is the virtual window created to host the widget focusable? |
| `OwnerPlayer` | `ULocalPlayer *` | The owner player for a widget component, if this widget is drawn on the screen, this controls<br>	  what player's screen it appears on for split screen, if not set, users player 0. |
| `BackgroundColor` | `FLinearColor` | The background color of the component |
| `TintColorAndOpacity` | `FLinearColor` | Tint color and opacity for this component |
| `OpacityFromTexture` | `float` | Sets the amount of opacity from the widget's UI texture to use when rendering the translucent or masked UI to the viewport (0.0-1.0) |
| `BlendMode` | `EWidgetBlendMode` | The blend mode for the widget. |
| `bIsTwoSided` | `bool` | Is the component visible from behind? |
| `TickWhenOffscreen` | `bool` | Should the component tick the widget when it's off screen? |
| `Widget` | `UUserWidget *` | The User Widget object displayed and managed by this component |
| `BodySetup` | `UBodySetup *` | The body setup of the displayed quad |
| `TranslucentMaterial` | `UMaterialInterface *` | The material instance for translucent widget components |
| `TranslucentMaterial_OneSided` | `UMaterialInterface *` | The material instance for translucent, one-sided widget components |
| `OpaqueMaterial` | `UMaterialInterface *` | The material instance for opaque widget components |
| `OpaqueMaterial_OneSided` | `UMaterialInterface *` | The material instance for opaque, one-sided widget components |
| `MaskedMaterial` | `UMaterialInterface *` | The material instance for masked widget components. |
| `MaskedMaterial_OneSided` | `UMaterialInterface *` | The material instance for masked, one-sided widget components. |
| `RenderTarget` | `UTextureRenderTarget2D *` | The target to which the user widget is rendered |
| `MaterialInstance` | `UMaterialInstanceDynamic *` | The dynamic instance of the material that the render target is attached to |
| `bAddedToScreen` | `bool` | - |
| `bEditTimeUsable` | `bool` | Allows the widget component to be used at editor time.  For use in the VR-Editor. |
| `SharedLayerName` | `FName` | Layer Name the widget will live on |
| `LayerZOrder` | `int32` | ZOrder the layer will be created on, note this only matters on the first time a new layer is created, subsequent additions to the same layer will use the initially defined ZOrder |
| `GeometryMode` | `EWidgetGeometryMode` | Controls the geometry of the widget component. See EWidgetGeometryMode. |
| `CylinderArcAngle` | `float` | Curvature of a cylindrical widget in degrees. |
| `FlipVector` | `FVector` | Curvature of a cylindrical widget in degrees. |
| `bUseBackColorInTwoSideMode` | `bool` | For Two side Color |
| `BackColor` | `FLinearColor` | - |
| `bHideIfOccluded` | `bool` | Hide widget component when the attached parent is occluded in player's view (ONLY VALID IN SCREEN SPACE) |

## Functions

### `GetUserWidgetObject`

```text
GetUserWidgetObject() -> UUserWidget *
```

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | The user widget object displayed by this component |

### `GetRenderTarget`

```text
GetRenderTarget() -> UTextureRenderTarget2D *
```

**Returns**

| Type | Description |
|---|---|
| `UTextureRenderTarget2D *` | The render target to which the user widget is rendered |

### `ForceWidgetUpdateImmediate`

```text
ForceWidgetUpdateImmediate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceWidgetUpdateImmediately`

```text
ForceWidgetUpdateImmediately() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceUpdateRenderTarget`

```text
ForceUpdateRenderTarget() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaterialInstance`

```text
GetMaterialInstance() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | The dynamic material instance used to render the user widget |

### `SetWidget`

```text
SetWidget(Widget: UUserWidget *) -> void
```

Sets the widget to use directly. This function will keep track of the widget till the next time it's called
	 	with either a newer widget or a nullptr

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOwnerPlayer`

```text
SetOwnerPlayer(LocalPlayer: ULocalPlayer *) -> void
```

Sets the local player that owns this widget component.  Setting the owning player controls
	  which player's viewport the widget appears on in a split screen scenario.  Additionally it
	  forwards the owning player to the actual UserWidget that is spawned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalPlayer` | `ULocalPlayer *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwnerPlayer`

```text
GetOwnerPlayer() -> ULocalPlayer *
```

Gets the local player that owns this widget component.

**Returns**

| Type | Description |
|---|---|
| `ULocalPlayer *` | - |

### `GetDrawSize`

```text
GetDrawSize() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The draw size of the quad in the world |

### `GetCurrentDrawSize`

```text
GetCurrentDrawSize() -> FVector2D
```

Returns the "actual" draw size of the quad in the world

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetDrawSize`

```text
SetDrawSize(Size: FVector2D) -> void
```

Sets the draw size of the quad in the world

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Size` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestRedraw`

```text
RequestRedraw() -> void
```

Requests that the widget be redrawn.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTickWhenOffscreen`

```text
GetTickWhenOffscreen() -> bool
```

Gets whether the widget ticks when offscreen or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTickWhenOffscreen`

```text
SetTickWhenOffscreen(bWantTickWhenOffscreen: bool) -> void
```

Sets whether the widget ticks when offscreen or not

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bWantTickWhenOffscreen` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBackgroundColor`

```text
SetBackgroundColor(NewBackgroundColor: FLinearColor) -> void
```

Sets the background color and opacityscale for this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBackgroundColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTintColorAndOpacity`

```text
SetTintColorAndOpacity(NewTintColorAndOpacity: FLinearColor) -> void
```

Sets the tint color and opacity scale for this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTintColorAndOpacity` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
