---
id: "api:class:UHeadMountedDisplayFunctionLibrary"
title: "UHeadMountedDisplayFunctionLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UHeadMountedDisplayFunctionLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UHeadMountedDisplayFunctionLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IsHeadMountedDisplayEnabled`

```text
IsHeadMountedDisplayEnabled() -> bool
```

Returns whether or not we are currently using the head mounted display.

**Returns**

| Type | Description |
|---|---|
| `bool` | (Boolean)  status of HMD |

### `IsHeadMountedDisplayConnected`

```text
IsHeadMountedDisplayConnected() -> bool
```

Returns whether or not the HMD hardware is connected and ready to use.  It may or may not actually be in use.

**Returns**

| Type | Description |
|---|---|
| `bool` | (Boolean)  status whether the HMD hardware is connected and ready to use.  It may or may not actually be in use. |

### `EnableHMD`

```text
EnableHMD(bEnable: bool) -> bool
```

Switches tofrom using HMD and stereo rendering.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | (in) 'true' to enable HMD stereo; 'false' otherwise |

**Returns**

| Type | Description |
|---|---|
| `bool` | (Boolean)		True, if the request was successful. |

### `GetHMDDeviceName`

```text
GetHMDDeviceName() -> FName
```

Returns the name of the device, so scripts can modify their behaviour appropriately

**Returns**

| Type | Description |
|---|---|
| `FName` | FName specific to the currently active HMD device type.  "None" implies no device, "Unknown" implies a device with no description. |

### `GetHMDWornState`

```text
GetHMDWornState() -> EHMDWornState :: Type
```

Returns the worn state of the device.

**Returns**

| Type | Description |
|---|---|
| `EHMDWornState :: Type` | Unknown, Worn, NotWorn.  If the platform does not detect this it will always return Unknown. |

### `GetOrientationAndPosition`

```text
GetOrientationAndPosition(DeviceRotation: FRotator &, DevicePosition: FVector &) -> void
```

Grabs the current orientation and position for the HMD.  If positional tracking is not available, DevicePosition will be a zero vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeviceRotation` | `FRotator &` | (out) The device's current rotation |
| `DevicePosition` | `FVector &` | (out) The device's current position, in its own tracking space |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasValidTrackingPosition`

```text
HasValidTrackingPosition() -> bool
```

If the HMD supports positional tracking, whether or not we are currently being tracked

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetNumOfTrackingSensors`

```text
GetNumOfTrackingSensors() -> int32
```

If the HMD has multiple positional tracking sensors, return a total number of them currently connected.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetTrackingSensorParameters`

```text
GetTrackingSensorParameters(Origin: FVector &, Rotation: FRotator &, LeftFOV: float &, RightFOV: float &, TopFOV: float &, BottomFOV: float &, Distance: float &, NearPlane: float &, FarPlane: float &, IsActive: bool &, Index: int32) -> void
```

If the HMD has a positional sensor, this will return the game-world location of it, as well as the parameters for the bounding region of tracking.
	  This allows an in-game representation of the legal positional tracking range.  All values will be zeroed if the sensor is not available or the HMD does not support it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector &` | (out) Origin, in world-space, of the sensor |
| `Rotation` | `FRotator &` | (out) Rotation, in world-space, of the sensor |
| `LeftFOV` | `float &` | (out) Field-of-view, left from center, in degrees, of the valid tracking zone of the sensor |
| `RightFOV` | `float &` | (out) Field-of-view, right from center, in degrees, of the valid tracking zone of the sensor |
| `TopFOV` | `float &` | (out) Field-of-view, top from center, in degrees, of the valid tracking zone of the sensor |
| `BottomFOV` | `float &` | (out) Field-of-view, bottom from center, in degrees, of the valid tracking zone of the sensor |
| `Distance` | `float &` | (out) Nominal distance to sensor, in world-space |
| `NearPlane` | `float &` | (out) Near plane distance of the tracking volume, in world-space |
| `FarPlane` | `float &` | (out) Far plane distance of the tracking volume, in world-space |
| `IsActive` | `bool &` | (out) True, if the query for the specified sensor succeeded. |
| `Index` | `int32` | (in) Index of the tracking sensor to query |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPositionalTrackingCameraParameters`

```text
GetPositionalTrackingCameraParameters(CameraOrigin: FVector &, CameraRotation: FRotator &, HFOV: float &, VFOV: float &, CameraDistance: float &, NearPlane: float &, FarPlane: float &) -> void
```

If the HMD has a positional sensor, this will return the game-world location of it, as well as the parameters for the bounding region of tracking.
	  This allows an in-game representation of the legal positional tracking range.  All values will be zeroed if the sensor is not available or the HMD does not support it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CameraOrigin` | `FVector &` | - |
| `CameraRotation` | `FRotator &` | - |
| `HFOV` | `float &` | (out) Field-of-view, horizontal, in degrees, of the valid tracking zone of the sensor |
| `VFOV` | `float &` | (out) Field-of-view, vertical, in degrees, of the valid tracking zone of the sensor |
| `CameraDistance` | `float &` | (out) Nominal distance to sensor, in world-space |
| `NearPlane` | `float &` | (out) Near plane distance of the tracking volume, in world-space |
| `FarPlane` | `float &` | (out) Far plane distance of the tracking volume, in world-space |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInLowPersistenceMode`

```text
IsInLowPersistenceMode() -> bool
```

Returns true, if HMD is in low persistence mode. 'false' otherwise.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EnableLowPersistenceMode`

```text
EnableLowPersistenceMode(bEnable: bool) -> void
```

Switches between low and full persistence modes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | (in) 'true' to enable low persistence mode; 'false' otherwise |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetOrientationAndPosition`

```text
ResetOrientationAndPosition(Yaw: float, Options: EOrientPositionSelector :: Type) -> void
```

Resets orientation by setting roll and pitch to 0, assuming that current yaw is forward direction and assuming
	  current position as a 'zero-point' (for positional tracking).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Yaw` | `float` | (in) the desired yaw to be set after orientation reset. |
| `Options` | `EOrientPositionSelector :: Type` | (in) specifies either position, orientation or both should be reset. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClippingPlanes`

```text
SetClippingPlanes(Near: float, Far: float) -> void
```

Sets near and far clipping planes (NCP and FCP) for stereo rendering. Similar to 'stereo ncp= fcp' console command, but NCP and FCP set by this
	  call won't be saved in .ini file.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Near` | `float` | (in) Near clipping plane, in centimeters |
| `Far` | `float` | (in) Far clipping plane, in centimeters |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScreenPercentage`

```text
GetScreenPercentage() -> float
```

Returns screen percentage to be used in VR mode.

**Returns**

| Type | Description |
|---|---|
| `float` | (float)	The screen percentage to be used in VR mode. |

### `SetWorldToMetersScale`

```text
SetWorldToMetersScale(WorldContext: UObject *, NewScale: float) -> void
```

Sets the World to Meters scale, which changes the scale of the world as perceived by the player

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject *` | - |
| `NewScale` | `float` | Specifies how many Unreal units correspond to one meter in the real world |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetWorldToMetersScale`

```text
GetWorldToMetersScale(WorldContext: UObject *) -> float
```

Returns the World to Meters scale, which corresponds to the scale of the world as perceived by the player

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | How many Unreal units correspond to one meter in the real world |

### `SetTrackingOrigin`

```text
SetTrackingOrigin(Origin: TEnumAsByte < EHMDTrackingOrigin :: Type >) -> void
```

Sets current tracking origin type (eye level or floor level).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `TEnumAsByte < EHMDTrackingOrigin :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTrackingOrigin`

```text
GetTrackingOrigin() -> TEnumAsByte < EHMDTrackingOrigin :: Type >
```

Returns current tracking origin type (eye level or floor level).

**Returns**

| Type | Description |
|---|---|
| `TEnumAsByte < EHMDTrackingOrigin :: Type >` | - |

### `GetVRFocusState`

```text
GetVRFocusState(bUseFocus: bool &, bHasFocus: bool &) -> void
```

Returns current state of VR focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUseFocus` | `bool &` | (out) if set to true, then this App does use VR focus. |
| `bHasFocus` | `bool &` | (out) if set to true, then this App currently has VR focus. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSpectatorScreenModeControllable`

```text
IsSpectatorScreenModeControllable() -> bool
```

Return true if spectator screen mode control is available.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSpectatorScreenMode`

```text
SetSpectatorScreenMode(Mode: ESpectatorScreenMode) -> void
```

Sets the social screen mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mode` | `ESpectatorScreenMode` | (in) The social screen Mode. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpectatorScreenTexture`

```text
SetSpectatorScreenTexture(InTexture: UTexture *) -> void
```

Change the texture displayed on the social screen

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpectatorScreenModeTexturePlusEyeLayout`

```text
SetSpectatorScreenModeTexturePlusEyeLayout(EyeRectMin: FVector2D, EyeRectMax: FVector2D, TextureRectMin: FVector2D, TextureRectMax: FVector2D, bDrawEyeFirst: bool, bClearBlack: bool) -> void
```

Setup the layout for ESpectatorScreenMode::TexturePlusEye.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EyeRectMin` | `FVector2D` | - |
| `EyeRectMax` | `FVector2D` | - |
| `TextureRectMin` | `FVector2D` | - |
| `TextureRectMax` | `FVector2D` | - |
| `bDrawEyeFirst` | `bool` | - |
| `bClearBlack` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
