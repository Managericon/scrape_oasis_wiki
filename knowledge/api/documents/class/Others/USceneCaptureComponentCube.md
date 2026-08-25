---
id: "api:class:USceneCaptureComponentCube"
title: "USceneCaptureComponentCube"
source: "https://developer.gp.qq.com/api/class/detail/Others/USceneCaptureComponentCube.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USceneCaptureComponentCube

Used to capture a 'snapshot' of the scene from a 6 planes and feed it to a render target.

## Inheritance

`USceneCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureTarget` | `UTextureRenderTargetCube *` | Temporary render target that can be used by the editor. |

## Functions

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
