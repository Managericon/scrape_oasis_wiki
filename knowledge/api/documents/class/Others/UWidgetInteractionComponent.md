---
id: "api:class:UWidgetInteractionComponent"
title: "UWidgetInteractionComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetInteractionComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetInteractionComponent

This is a component to allow interaction with the Widget Component.  This class allows you to 
  simulate a sort of laser pointer device, when it hovers over widgets it will send the basic signals 
  to show as if the mouse were moving on top of it.  You'll then tell the component to simulate key presses, 
  like Left Mouse, down and up, to simulate a mouse click.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VirtualUserIndex` | `int32` | Represents the Virtual User Index.  Each virtual user should be represented by a different <br>	  index number, this will maintain separate capture and focus states for them.  Each<br>	  controller or finger-tip should get a unique PointerIndex. |
| `PointerIndex` | `float` | Each user virtual controller or virtual finger tips being simulated should use a different pointer index. |
| `TraceChannel` | `TEnumAsByte < ECollisionChannel >` | The trace channel to use when tracing for widget components in the world. |
| `InteractionDistance` | `float` | The distance in game units the component should be able to interact with a widget component. |
| `InteractionSource` | `EWidgetInteractionSource` | Should we project from the world location of the component?  If you set this to false, you'll<br>	  need to call SetCustomHitResult(), and provide the result of a custom hit test form whatever<br>	  location you wish. |
| `bEnableHitTesting` | `bool` | Should the interaction component perform hit testing (Automatic or Custom) and attempt to <br>	  simulate hover - if you were going to emulate a keyboard you would want to turn this option off<br>	  if the virtual keyboard was separate from the virtual pointer device and used a second interaction<br>	  component. |
| `bSimulateTouchEvents` | `bool` | When true, pointer events will be sent as touch events instead of mouse events.<br>	  This enables drag-scrolling on ScrollBoxListView widgets in 3D UI,<br>	  since those widgets only respond to touch-based drag gestures. |
| `bShowDebug` | `bool` | Shows some debugging lines and a hit sphere to help you debug interactions. |
| `DebugColor` | `FLinearColor` | Determines the color of the debug lines. |
| `CustomHitResult` | `FHitResult` | Stores the custom hit result set by the player. |
| `LocalHitLocation` | `FVector2D` | The 2D location on the widget component that was hit. |
| `LastLocalHitLocation` | `FVector2D` | The last 2D location on the widget component that was hit. |
| `HoveredWidgetComponent` | `UWidgetComponent *` | The widget component we're currently hovering over. |
| `LastHitResult` | `FHitResult` | The last hit result we used. |
| `bIsHoveredWidgetInteractable` | `bool` | Are we hovering over any interactive widgets. |
| `bIsHoveredWidgetFocusable` | `bool` | Are we hovering over any focusable widget? |
| `bIsHoveredWidgetHitTestVisible` | `bool` | Are we hovered over a widget that is hit test visible? |

## Functions

### `PressPointerKey`

```text
PressPointerKey(Key: FKey) -> void
```

Presses a key as if the mousepointer were the source of it.  Normally you would just use
	  LeftRight mouse button for the Key.  However - advanced uses could also be imagined where you
	  send other keys to signal widgets to take special actions if they're under the cursor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleasePointerKey`

```text
ReleasePointerKey(Key: FKey) -> void
```

Releases a key as if the mousepointer were the source of it.  Normally you would just use
	  LeftRight mouse button for the Key.  However - advanced uses could also be imagined where you
	  send other keys to signal widgets to take special actions if they're under the cursor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PressKey`

```text
PressKey(Key: FKey, bRepeat: bool) -> bool
```

Press a key as if it had come from the keyboard.  Avoid using this for 'a-z|A-Z', things like
	  the Editable Textbox in Slate expect OnKeyChar to be called to signal a specific character being
	  send to the widget.  So for those cases you should use SendKeyChar.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |
| `bRepeat` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReleaseKey`

```text
ReleaseKey(Key: FKey) -> bool
```

Releases a key as if it had been released by the keyboard.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `PressAndReleaseKey`

```text
PressAndReleaseKey(Key: FKey) -> bool
```

Does both the press and release of a simulated keyboard key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SendKeyChar`

```text
SendKeyChar(Characters: FString, bRepeat: bool) -> bool
```

Transmits a list of characters to a widget by simulating a OnKeyChar event for each key listed in
	  the string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Characters` | `FString` | - |
| `bRepeat` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ScrollWheel`

```text
ScrollWheel(ScrollDelta: float) -> void
```

Sends a scroll wheel event to the widget under the last hit result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScrollDelta` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetHoveredWidgetComponent`

```text
GetHoveredWidgetComponent() -> UWidgetComponent *
```

Get the currently hovered widget component.

**Returns**

| Type | Description |
|---|---|
| `UWidgetComponent *` | - |

### `IsOverInteractableWidget`

```text
IsOverInteractableWidget() -> bool
```

Returns true if a widget under the hit result is interactive.  e.g. Slate widgets 
	  that return true for IsInteractable().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsOverFocusableWidget`

```text
IsOverFocusableWidget() -> bool
```

Returns true if a widget under the hit result is focusable.  e.g. Slate widgets that 
	  return true for SupportsKeyboardFocus().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsOverHitTestVisibleWidget`

```text
IsOverHitTestVisibleWidget() -> bool
```

Returns true if a widget under the hit result is has a visibility that makes it hit test 
	  visible.  e.g. Slate widgets that return true for GetVisibility().IsHitTestVisible().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetLastHitResult`

```text
GetLastHitResult() -> const FHitResult &
```

Gets the last hit result generated by the component.  Returns the custom hit result if that was set.

**Returns**

| Type | Description |
|---|---|
| `const FHitResult &` | - |

### `Get2DHitLocation`

```text
Get2DHitLocation() -> FVector2D
```

Gets the last hit location on the widget in 2D, local pixel units of the render target.

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetCustomHitResult`

```text
SetCustomHitResult(HitResult: FHitResult &) -> void
```

Set custom hit result.  This is only taken into account if InteractionSource is set to EWidgetInteractionSource::Custom.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnHoveredWidgetChanged`

```text
OnHoveredWidgetChanged(WidgetComponent: UWidgetComponent*, PreviousWidgetComponent: UWidgetComponent*) -> void
```

Called when the hovered Widget Component changes.  The interaction component functions at the Slate
	  level - so it's unable to report anything about what UWidget is under the hit result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetComponent` | `UWidgetComponent*` | - |
| `PreviousWidgetComponent` | `UWidgetComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
