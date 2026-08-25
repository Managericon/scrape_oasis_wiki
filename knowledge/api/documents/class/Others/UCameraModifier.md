---
id: "api:class:UCameraModifier"
title: "UCameraModifier"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCameraModifier.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCameraModifier

A CameraModifier is a base class for objects that may adjust the final camera properties after
  being computed by the APlayerCameraManager (@see ModifyCamera). A CameraModifier
  can be stateful, and is associated uniquely with a specific APlayerCameraManager.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bDebug` | `uint32` | If true, enables certain debug visualization features. |
| `bExclusive` | `uint32` | If true, no other modifiers of same priority allowed. |
| `Priority` | `uint8` | Priority value that determines the order in which modifiers are applied. 0 = highest priority, 255 = lowest. |
| `CameraOwner` | `APlayerCameraManager *` | Camera this object is associated with. |
| `AlphaInTime` | `float` | When blending in, alpha proceeds from 0 to 1 over this time |
| `AlphaOutTime` | `float` | When blending out, alpha proceeds from 1 to 0 over this time |
| `Alpha` | `float` | Current blend alpha. |

## Functions

### `BlueprintModifyCamera`

```text
BlueprintModifyCamera(DeltaTime: float, ViewLocation: FVector, ViewRotation: FRotator, FOV: float, NewViewLocation: FVector &, NewViewRotation: FRotator &, NewFOV: float &) -> void
```

Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's transform. 
	  Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | Change in time since last update |
| `ViewLocation` | `FVector` | The current camera location. |
| `ViewRotation` | `FRotator` | The current camera rotation. |
| `FOV` | `float` | The current camera fov. |
| `NewViewLocation` | `FVector &` | (out) The modified camera location. |
| `NewViewRotation` | `FRotator &` | (out) The modified camera rotation. |
| `NewFOV` | `float &` | (out) The modified camera FOV. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BlueprintModifyPostProcess`

```text
BlueprintModifyPostProcess(DeltaTime: float, PostProcessBlendWeight: float &, PostProcessSettings: FPostProcessSettings &) -> void
```

Called per tick that the modifier is active to allow Blueprinted modifiers to modify the camera's postprocess effects.
	  Scaling by Alpha happens after this in code, so no need to deal with that in the blueprint.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | Change in time since last update |
| `PostProcessBlendWeight` | `float &` | (out) Blend weight applied to the entire postprocess structure. |
| `PostProcessSettings` | `FPostProcessSettings &` | (out) Post process structure defining what settings and values to override. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsDisabled`

```text
IsDisabled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns true if modifier is disabled, false otherwise. |

### `GetViewTarget`

```text
GetViewTarget() -> AActor *
```

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Returns the actor the camera is currently viewing. |

### `DisableModifier`

```text
DisableModifier(bImmediate: bool) -> void
```

Disables this modifier.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bImmediate` | `bool` | - true to disable with no blend out, false (default) to allow blend out |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableModifier`

```text
EnableModifier() -> void
```

Enables this modifier.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
