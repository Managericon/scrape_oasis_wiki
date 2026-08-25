---
id: "api:class:UDrawFrustumComponent"
title: "UDrawFrustumComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDrawFrustumComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDrawFrustumComponent

Utility component for drawing a view frustum. Origin is at the component location, frustum points down position X axis.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FrustumColor` | `FColor` | Color to draw the wireframe frustum. |
| `FrustumAngle` | `float` | Angle of longest dimension of view shape. <br>	   If the angle is 0 then an orthographic projection is used |
| `FrustumAspectRatio` | `float` | Ratio of horizontal size over vertical size. |
| `FrustumStartDist` | `float` | Distance from origin to start drawing the frustum. |
| `FrustumEndDist` | `float` | Distance from origin to stop drawing the frustum. |
| `Texture` | `UTexture *` | optional texture to show on the near plane |

## Language

`cpp`
