---
id: "api:class:UArrowComponent"
title: "UArrowComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UArrowComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UArrowComponent

A simple arrow rendered using lines. Useful for indicating which way an object is facing.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ArrowColor` | `FColor` | - |
| `ArrowSize` | `float` | - |
| `bIsScreenSizeScaled` | `bool` | Set to limit the screen size of this arrow |
| `ScreenSize` | `float` | The size on screen to limit this arrow to (in screen space) |
| `bTreatAsASprite` | `uint32` | If true, don't show the arrow when EngineShowFlags.BillboardSprites is disabled. |

## Functions

### `SetArrowColor`

```text
SetArrowColor(NewColor: FLinearColor) -> void
```

Updates the arrow's colour, and tells it to refresh

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
