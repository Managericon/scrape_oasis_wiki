---
id: "api:class:UKismetInputLibrary"
title: "UKismetInputLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetInputLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetInputLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `CalibrateTilt`

```text
CalibrateTilt() -> void
```

Calibrate the tilt for the input device

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EqualEqual_KeyKey`

```text
EqualEqual_KeyKey(A: FKey, B: FKey) -> bool
```

Test if the input key are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FKey` | - The key to compare against |
| `B` | `FKey` | - The key to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key are equal, false otherwise |

### `EqualEqual_InputChordInputChord`

```text
EqualEqual_InputChordInputChord(A: FInputChord, B: FInputChord) -> bool
```

Test if the input chords are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FInputChord` | - The chord to compare against |
| `B` | `FInputChord` | - The chord to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the chords are equal, false otherwise |

### `Key_IsModifierKey`

```text
Key_IsModifierKey(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a modifier key: Ctrl, Command, Alt, Shift |

### `Key_IsGamepadKey`

```text
Key_IsGamepadKey(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a gamepad button |

### `Key_IsMouseButton`

```text
Key_IsMouseButton(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a mouse button |

### `Key_IsKeyboardKey`

```text
Key_IsKeyboardKey(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a keyboard button |

### `Key_IsFloatAxis`

```text
Key_IsFloatAxis(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a float axis |

### `Key_IsVectorAxis`

```text
Key_IsVectorAxis(Key: FKey &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the key is a vector axis |

### `Key_GetDisplayName`

```text
Key_GetDisplayName(Key: FKey &) -> FText
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | The display name of the key. |

### `InputEvent_IsRepeat`

```text
InputEvent_IsRepeat(Input: FInputEvent &) -> bool
```

Returns whether or not this character is an auto-repeated keystroke

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if this character is a repeat |

### `InputEvent_IsShiftDown`

```text
InputEvent_IsShiftDown(Input: FInputEvent &) -> bool
```

Returns true if either shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if shift is pressed |

### `InputEvent_IsLeftShiftDown`

```text
InputEvent_IsLeftShiftDown(Input: FInputEvent &) -> bool
```

Returns true if left shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left shift is pressed. |

### `InputEvent_IsRightShiftDown`

```text
InputEvent_IsRightShiftDown(Input: FInputEvent &) -> bool
```

Returns true if right shift key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if right shift is pressed. |

### `InputEvent_IsControlDown`

```text
InputEvent_IsControlDown(Input: FInputEvent &) -> bool
```

Returns true if either control key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if control is pressed |

### `InputEvent_IsLeftControlDown`

```text
InputEvent_IsLeftControlDown(Input: FInputEvent &) -> bool
```

Returns true if left control key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left control is pressed |

### `InputEvent_IsRightControlDown`

```text
InputEvent_IsRightControlDown(Input: FInputEvent &) -> bool
```

Returns true if left control key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left control is pressed |

### `InputEvent_IsAltDown`

```text
InputEvent_IsAltDown(Input: FInputEvent &) -> bool
```

Returns true if either alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if alt is pressed |

### `InputEvent_IsLeftAltDown`

```text
InputEvent_IsLeftAltDown(Input: FInputEvent &) -> bool
```

Returns true if left alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left alt is pressed |

### `InputEvent_IsRightAltDown`

```text
InputEvent_IsRightAltDown(Input: FInputEvent &) -> bool
```

Returns true if right alt key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if right alt is pressed |

### `InputEvent_IsCommandDown`

```text
InputEvent_IsCommandDown(Input: FInputEvent &) -> bool
```

Returns true if either command key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if command is pressed |

### `InputEvent_IsLeftCommandDown`

```text
InputEvent_IsLeftCommandDown(Input: FInputEvent &) -> bool
```

Returns true if left command key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if left command is pressed |

### `InputEvent_IsRightCommandDown`

```text
InputEvent_IsRightCommandDown(Input: FInputEvent &) -> bool
```

Returns true if right command key was down when this event occurred

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if right command is pressed |

### `GetKeyByName`

```text
GetKeyByName(KeyName: FName &) -> FKey
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKey` | - |

### `GetKey`

```text
GetKey(Input: FKeyEvent &) -> FKey
```

Returns the key for this event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FKeyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKey` | Key name |

### `GetUserIndex`

```text
GetUserIndex(Input: FKeyEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FKeyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetAnalogValue`

```text
GetAnalogValue(Input: FAnalogInputEvent &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FAnalogInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PointerEvent_GetScreenSpacePosition`

```text
PointerEvent_GetScreenSpacePosition(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The position of the cursor in screen space |

### `PointerEvent_GetLastScreenSpacePosition`

```text
PointerEvent_GetLastScreenSpacePosition(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The position of the cursor in screen space last time we handled an input event |

### `PointerEvent_GetCursorDelta`

```text
PointerEvent_GetCursorDelta(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | the distance the mouse traveled since the last event was handled. |

### `PointerEvent_IsMouseButtonDown`

```text
PointerEvent_IsMouseButtonDown(Input: FPointerEvent &, MouseButton: FKey) -> bool
```

Mouse buttons that are currently pressed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |
| `MouseButton` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `PointerEvent_GetEffectingButton`

```text
PointerEvent_GetEffectingButton(Input: FPointerEvent &) -> FKey
```

Mouse button that caused this event to be raised (possibly EB_None)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKey` | - |

### `PointerEvent_GetWheelDelta`

```text
PointerEvent_GetWheelDelta(Input: FPointerEvent &) -> float
```

How much did the mouse wheel turn since the last mouse event

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PointerEvent_GetUserIndex`

```text
PointerEvent_GetUserIndex(Input: FPointerEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the user that caused the event |

### `PointerEvent_GetPointerIndex`

```text
PointerEvent_GetPointerIndex(Input: FPointerEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The unique identifier of the pointer (e.g., finger index) |

### `PointerEvent_GetTouchpadIndex`

```text
PointerEvent_GetTouchpadIndex(Input: FPointerEvent &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the touch pad that generated this event (for platforms with multiple touch pads per user) |

### `PointerEvent_IsTouchEvent`

```text
PointerEvent_IsTouchEvent(Input: FPointerEvent &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Is this event a result from a touch (as opposed to a mouse) |

### `PointerEvent_TouchForce`

```text
PointerEvent_TouchForce(Input: FPointerEvent &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PointerEvent_GetGestureType`

```text
PointerEvent_GetGestureType(Input: FPointerEvent &) -> ESlateGesture
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `ESlateGesture` | The type of touch gesture |

### `PointerEvent_GetGestureDelta`

```text
PointerEvent_GetGestureDelta(Input: FPointerEvent &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Input` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The change in gesture value since the last gesture event of the same type. |

## Language

`cpp`
