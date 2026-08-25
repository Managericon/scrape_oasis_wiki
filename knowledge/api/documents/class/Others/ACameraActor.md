---
id: "api:class:ACameraActor"
title: "ACameraActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/ACameraActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ACameraActor

A CameraActor is a camera viewpoint that can be placed in a level.

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AutoActivateForPlayer` | `TEnumAsByte < EAutoReceiveInput :: Type >` | Specifies which player controller, if any, should automatically use this Camera when the controller is active. |
| `CameraComponent` | `UCameraComponent *` | The camera component for this camera |
| `SceneComponent` | `USceneComponent *` | - |
| `bConstrainAspectRatio_DEPRECATED` | `uint32` | - |
| `AspectRatio_DEPRECATED` | `float` | - |
| `FOVAngle_DEPRECATED` | `float` | - |
| `PostProcessBlendWeight_DEPRECATED` | `float` | - |
| `PostProcessSettings_DEPRECATED` | `FPostProcessSettings` | - |

## Functions

### `GetAutoActivatePlayerIndex`

```text
GetAutoActivatePlayerIndex() -> int32
```

Returns index of the player for whom we auto-activate, or INDEX_NONE (-1) if disabled.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`
