---
id: "api:class:UWidgetLayoutLibrary"
title: "UWidgetLayoutLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetLayoutLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetLayoutLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `ProjectWorldLocationToWidgetPosition`

```text
ProjectWorldLocationToWidgetPosition(PlayerController: APlayerController *, WorldLocation: FVector, ScreenPosition: FVector2D &) -> bool
```

Gets the projected world to screen position for a player, then converts it into a widget
	  position, which takes into account any quality scaling.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | The player controller to project the position in the world to their screen. |
| `WorldLocation` | `FVector` | The world location to project from. |
| `ScreenPosition` | `FVector2D &` | The position in the viewport with quality scale removed and DPI scale remove. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the position projects onto the screen. |

### `GetViewportScale`

```text
GetViewportScale(WorldContextObject: UObject *) -> float
```

Gets the current DPI Scale being applied to the viewport and all the Widgets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetViewportSize`

```text
GetViewportSize(WorldContextObject: UObject *) -> FVector2D
```

Gets the size of the game viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetViewportWidgetGeometry`

```text
GetViewportWidgetGeometry(WorldContextObject: UObject *) -> FGeometry
```

Gets the geometry of the widget holding all widgets added to the "Viewport".  You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FGeometry` | - |

### `GetPlayerScreenWidgetGeometry`

```text
GetPlayerScreenWidgetGeometry(PlayerController: APlayerController *) -> FGeometry
```

Gets the geometry of the widget holding all widgets added to the "Player Screen". You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `FGeometry` | - |

### `GetMousePositionOnPlatform`

```text
GetMousePositionOnPlatform() -> FVector2D
```

Gets the platform's mouse cursor position.  This is the 'absolute' desktop location of the mouse.

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetMousePositionOnViewport`

```text
GetMousePositionOnViewport(WorldContextObject: UObject *) -> FVector2D
```

Gets the platform's mouse cursor position in the local space of the viewport widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetMousePositionScaledByDPI`

```text
GetMousePositionScaledByDPI(Player: APlayerController *, LocationX: float &, LocationY: float &) -> bool
```

Gets the mouse position of the player controller, scaled by the DPI.  If you're trying to go from raw mouse screenspace coordinates
	  to fullscreen widget space, you'll need to transform the mouse into DPI Scaled space.  This function performs that scaling.
	 
	  MousePositionScaledByDPI = MousePosition  (1  ViewportScale).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | - |
| `LocationX` | `float &` | - |
| `LocationY` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SlotAsBorderSlot`

```text
SlotAsBorderSlot(Widget: UWidget *) -> UBorderSlot *
```

Gets the slot object on the child widget as a Border Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a border panel. |

**Returns**

| Type | Description |
|---|---|
| `UBorderSlot *` | - |

### `SlotAsCanvasSlot`

```text
SlotAsCanvasSlot(Widget: UWidget *) -> UCanvasPanelSlot *
```

Gets the slot object on the child widget as a Canvas Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a canvas panel. |

**Returns**

| Type | Description |
|---|---|
| `UCanvasPanelSlot *` | - |

### `SlotAsGridSlot`

```text
SlotAsGridSlot(Widget: UWidget *) -> UGridSlot *
```

Gets the slot object on the child widget as a Grid Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a grid panel. |

**Returns**

| Type | Description |
|---|---|
| `UGridSlot *` | - |

### `SlotAsHorizontalBoxSlot`

```text
SlotAsHorizontalBoxSlot(Widget: UWidget *) -> UHorizontalBoxSlot *
```

Gets the slot object on the child widget as a Horizontal Box Slot, allowing you to manipulate its information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a Horizontal Box. |

**Returns**

| Type | Description |
|---|---|
| `UHorizontalBoxSlot *` | - |

### `SlotAsOverlaySlot`

```text
SlotAsOverlaySlot(Widget: UWidget *) -> UOverlaySlot *
```

Gets the slot object on the child widget as a Overlay Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a overlay panel. |

**Returns**

| Type | Description |
|---|---|
| `UOverlaySlot *` | - |

### `SlotAsUniformGridSlot`

```text
SlotAsUniformGridSlot(Widget: UWidget *) -> UUniformGridSlot *
```

Gets the slot object on the child widget as a Uniform Grid Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a uniform grid panel. |

**Returns**

| Type | Description |
|---|---|
| `UUniformGridSlot *` | - |

### `SlotAsVerticalBoxSlot`

```text
SlotAsVerticalBoxSlot(Widget: UWidget *) -> UVerticalBoxSlot *
```

Gets the slot object on the child widget as a Vertical Box Slot, allowing you to manipulate its information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a Vertical Box. |

**Returns**

| Type | Description |
|---|---|
| `UVerticalBoxSlot *` | - |

### `RemoveAllWidgets`

```text
RemoveAllWidgets(WorldContextObject: UObject *) -> void
```

Removes all widgets from the viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNewUsedLayerPolicy`

```text
SetNewUsedLayerPolicy(Widget: UWidget *, NewLayerPolicy: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | - |
| `NewLayerPolicy` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
