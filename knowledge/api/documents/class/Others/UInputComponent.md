---
id: "api:class:UInputComponent"
title: "UInputComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInputComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInputComponent

Implement an Actor component for input bindings.
 
  An Input Component is a transient component that enables an Actor to bind various forms of input events to delegate functions.  
  Input components are processed from a stack managed by the PlayerController and processed by the PlayerInput.
  Each binding can consume the input event preventing other components on the input stack from processing the input.

## Inheritance

`UActorComponent`

## Functions

### `IsControllerKeyDown`

```text
IsControllerKeyDown(Key: FKey) -> bool
```

Returns true if the given keybutton is pressed on the input of the controller (if present)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `WasControllerKeyJustPressed`

```text
WasControllerKeyJustPressed(Key: FKey) -> bool
```

Returns true if the given keybutton was up last frame and down this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `WasControllerKeyJustReleased`

```text
WasControllerKeyJustReleased(Key: FKey) -> bool
```

Returns true if the given keybutton was down last frame and up this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetControllerAnalogKeyState`

```text
GetControllerAnalogKeyState(Key: FKey) -> float
```

Returns the analog value for the given keybutton.  If analog isn't supported, returns 1 for down and 0 for up.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetControllerVectorKeyState`

```text
GetControllerVectorKeyState(Key: FKey) -> FVector
```

Returns the vector value for the given keybutton.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTouchState`

```text
GetTouchState(FingerIndex: int32, LocationX: float &, LocationY: float &, bIsCurrentlyPressed: bool &) -> void
```

Returns the location of a touch, and if it's held down

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `int32` | - |
| `LocationX` | `float &` | - |
| `LocationY` | `float &` | - |
| `bIsCurrentlyPressed` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetControllerKeyTimeDown`

```text
GetControllerKeyTimeDown(Key: FKey) -> float
```

Returns how long the given keybutton has been down.  Returns 0 if it's up or it just went down this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetControllerMouseDelta`

```text
GetControllerMouseDelta(DeltaX: float &, DeltaY: float &) -> void
```

Retrieves how far the mouse moved this frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaX` | `float &` | - |
| `DeltaY` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetControllerAnalogStickState`

```text
GetControllerAnalogStickState(WhichStick: EControllerAnalogStick :: Type, StickX: float &, StickY: float &) -> void
```

Retrieves the X and Y displacement of the given analog stick.  For WhickStick, 0 = left, 1 = right.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WhichStick` | `EControllerAnalogStick :: Type` | - |
| `StickX` | `float &` | - |
| `StickY` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
