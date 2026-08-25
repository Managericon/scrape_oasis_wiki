---
id: "api:class:USceneCaptureComponent2D"
title: "USceneCaptureComponent2D"
source: "https://developer.gp.qq.com/api/class/detail/Others/USceneCaptureComponent2D.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USceneCaptureComponent2D

Used to capture a 'snapshot' of the scene from a single plane and feed it to a render target.

## Inheritance

`USceneCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProjectionType` | `TEnumAsByte < ECameraProjectionMode :: Type >` | - |
| `FOVAngle` | `float` | Camera field of view (in degrees). |
| `OrthoWidth` | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| `TextureTarget` | `UTextureRenderTarget2D *` | Output render target of the scene capture that can be read in materals. |
| `CaptureSource` | `TEnumAsByte < enum ESceneCaptureSource >` | - |
| `CompositeMode` | `TEnumAsByte < enum ESceneCaptureCompositeMode >` | When enabled, the scene capture will composite into the render target instead of overwriting its contents. |
| `PostProcessSettings` | `FPostProcessSettings` | - |
| `PostProcessBlendWeight` | `float` | Range (0.0, 1.0) where 0 indicates no effect, 1 indicates full effect. |
| `bUseCustomProjectionMatrix` | `bool` | Whether a custom projection matrix will be used during rendering. Use with caution. Does not currently affect culling |
| `CustomProjectionMatrix` | `FMatrix` | The custom projection matrix to use |
| `bEnableClipPlane` | `bool` | Enables a clip plane while rendering the scene capture which is useful for portals.  <br>	  The global clip plane must be enabled in the renderer project settings for this to work. |
| `ClipPlaneBase` | `FVector` | Base position for the clip plane, can be any position on the plane. |
| `ClipPlaneNormal` | `FVector` | Normal for the plane. |
| `bCameraCutThisFrame` | `uint32` | True if we did a camera cut this frame. Automatically reset to false at every capture.<br>	  This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur).<br>	  Similar to UPlayerCameraManager::bGameCameraCutThisFrame. |

## Functions

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

### `CaptureScene`

```text
CaptureScene() -> void
```

Render the scene to the texture target immediately.  
	  This should not be used if bCaptureEveryFrame is enabled, or the scene capture will render redundantly.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
