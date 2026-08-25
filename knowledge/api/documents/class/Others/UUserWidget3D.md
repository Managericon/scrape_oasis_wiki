---
id: "api:class:UUserWidget3D"
title: "UUserWidget3D"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUserWidget3D.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUserWidget3D

UUserWidget3D - A UMG widget that can render a 3D StaticMesh directly to the BackBuffer.
 
  Two rendering modes:
    1. Legacy Slate3D path: Call AddTo3DWidget() to render 2D widget content with 3D rotation via SWindow3D + RT.
    2. Direct Mesh path: Set MeshAsset and the mesh is rendered directly to BackBuffer each frame via ENQUEUE_RENDER_COMMAND.

## Inheritance

`UUserWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FOV` | `float` | - |
| `Brush` | `UTextureRenderTarget2D *` | - |
| `MeshAsset` | `UStaticMesh *` | The StaticMesh asset to render. |
| `MeshRotationYaw` | `float` | Yaw rotation (degrees). Animatable via UMG Animation. |
| `MeshRotationPitch` | `float` | Pitch rotation (degrees). Animatable via UMG Animation. |
| `MeshScale` | `FVector` | Scale of the mesh. |
| `MeshOffset` | `FVector` | Offset of the mesh center (screen pixel coordinates). |
| `MeshCameraDistance` | `float` | Camera distance from the mesh. Controls apparent size. |

## Functions

### `AddTo3DWidget`

```text
AddTo3DWidget() -> void
```

Legacy: Add this widget to the Slate3D rendering pipeline (renders to RT via SWindow3D).

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMeshRotation`

```text
SetMeshRotation(NewYaw: float, NewPitch: float) -> void
```

Set the mesh rotation and refresh the mesh drawer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewYaw` | `float` | - |
| `NewPitch` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
