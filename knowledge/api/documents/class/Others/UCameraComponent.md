---
id: "api:class:UCameraComponent"
title: "UCameraComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCameraComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCameraComponent

Represents a camera viewpoint and settings, such as projection type, field of view, and post-process overrides.
   The default behavior for an actor used as the camera view target is to look for an attached camera component and use its location, rotation, and settings.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FieldOfView` | `float` | The horizontal field of view (in degrees) in perspective mode (ignored in Orthographic mode) |
| `FirstPersonFieldOfView` | `float` | The horizontal field of view (in degrees) used for primitives tagged as "IsFirstPerson". |
| `FirstPersonScale` | `float` | The scale to apply to primitives tagged as "IsFirstPerson". This is used to scale down primitives towards the camera such that they are small enough not to intersect with the scene. |
| `FirstPersonScaleCurveNearValue` | `float` | - |
| `FirstPersonScaleMaxLength` | `float` | - |
| `FirstPersonScaleCurvePow` | `float` | - |
| `bEnableFirstPersonFieldOfView` | `uint8` | True if the first person field of view should be used for primitives tagged as "IsFirstPerson". |
| `bEnableFirstPersonScale` | `uint8` | True if the first person scale should be used for primitives tagged as "IsFirstPerson". |
| `OrthoWidth` | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| `OrthoNearClipPlane` | `float` | The near plane distance of the orthographic view (in world units) |
| `OrthoFarClipPlane` | `float` | The far plane distance of the orthographic view (in world units) |
| `AspectRatio` | `float` | - |
| `WidthHeight` | `FVector2D` | - |
| `bConstrainAspectRatio` | `uint32` | - |
| `bUseFieldOfViewForLOD` | `uint32` | - |
| `bLockToHmd` | `uint32` | True if the camera's orientation and position should be locked to the HMD |
| `bUsePawnControlRotation` | `uint32` | If this camera component is placed on a pawn, should it use the viewcontrol rotation of the pawn where possible?<br>	  @see APawn::GetViewRotation() |
| `bEnableModifyAdditiveOffset` | `uint32` | - |
| `ProjectionMode` | `TEnumAsByte < ECameraProjectionMode :: Type >` | - |
| `PostProcessBlendWeight` | `float` | Indicates if PostProcessSettings should be used when using this Camera to view through. |
| `PostProcessSettings` | `FPostProcessSettings` | Post process settings to use for this camera. Don't forget to check the properties you want to override |
| `bUseControllerViewRotation_DEPRECATED` | `uint32` | DEPRECATED: use bUsePawnControlRotation instead |

## Functions

### `SetFieldOfView`

```text
SetFieldOfView(InFieldOfView: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFieldOfView` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFirstPersonFieldOfView`

```text
SetFirstPersonFieldOfView(InFirstPersonFieldOfView: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstPersonFieldOfView` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFirstPersonScale`

```text
SetFirstPersonScale(InFirstPersonScale: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstPersonScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFirstPersonScaleParams`

```text
SetFirstPersonScaleParams(InFirstPersonScale: float, InFPScaleCurveNearValue: float, InFPScaleMaxLen: float, InFPScaleCurvePow: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFirstPersonScale` | `float` | - |
| `InFPScaleCurveNearValue` | `float` | - |
| `InFPScaleMaxLen` | `float` | - |
| `InFPScaleCurvePow` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableFirstPersonFieldOfView`

```text
SetEnableFirstPersonFieldOfView(bInEnableFirstPersonFieldOfView: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInEnableFirstPersonFieldOfView` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableFirstPersonScale`

```text
SetEnableFirstPersonScale(bInEnableFirstPersonScale: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInEnableFirstPersonScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActive`

```text
SetActive(bNewActive: bool, bReset: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewActive` | `bool` | - |
| `bReset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyDrawDistanceOffset`

```text
ApplyDrawDistanceOffset(InFieldOfView: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFieldOfView` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrthoWidth`

```text
SetOrthoWidth(InOrthoWidth: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOrthoWidth` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrthoNearClipPlane`

```text
SetOrthoNearClipPlane(InOrthoNearClipPlane: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOrthoNearClipPlane` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOrthoFarClipPlane`

```text
SetOrthoFarClipPlane(InOrthoFarClipPlane: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOrthoFarClipPlane` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAspectRatio`

```text
SetAspectRatio(InAspectRatio: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAspectRatio` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWidthHeight`

```text
SetWidthHeight(InWidthHeight: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWidthHeight` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintAspectRatio`

```text
SetConstraintAspectRatio(bInConstrainAspectRatio: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInConstrainAspectRatio` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUseFieldOfViewForLOD`

```text
SetUseFieldOfViewForLOD(bInUseFieldOfViewForLOD: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInUseFieldOfViewForLOD` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetProjectionMode`

```text
SetProjectionMode(InProjectionMode: ECameraProjectionMode :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InProjectionMode` | `ECameraProjectionMode :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPostProcessBlendWeight`

```text
SetPostProcessBlendWeight(InPostProcessBlendWeight: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPostProcessBlendWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCameraView`

```text
GetCameraView(DeltaTime: float, DesiredView: FMinimalViewInfo &) -> void
```

Returns camera's Point of View.
	  Called by Camera class. Subclass and postprocess to add any effects.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |
| `DesiredView` | `FMinimalViewInfo &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddOrUpdateBlendable`

```text
AddOrUpdateBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >, InWeight: float) -> void
```

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendableObject` | `TScriptInterface < IBlendableInterface >` | - |
| `InWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveBlendable`

```text
RemoveBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >) -> void
```

Removes a blendable.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendableObject` | `TScriptInterface < IBlendableInterface >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetbEnableModifyAdditiveOffset`

```text
SetbEnableModifyAdditiveOffset(InEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEnableModifyAdditiveOffset`

```text
GetEnableModifyAdditiveOffset() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddAdditiveOffset`

```text
AddAdditiveOffset(Transform: FTransform &, FOV: float) -> void
```

Applies the given additive offset, preserving any existing offset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform &` | - |
| `FOV` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAdditiveOffset`

```text
ClearAdditiveOffset() -> void
```

Removes any additive offset.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAddtiveInfo`

```text
GetAddtiveInfo(OutIsAddtive: bool &, OutAddtiveOffset: float &, OutAddtiveTrans: FTransform &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutIsAddtive` | `bool &` | - |
| `OutAddtiveOffset` | `float &` | - |
| `OutAddtiveTrans` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
