---
id: "api:class:UGridVisibilityCaptureComponent"
title: "UGridVisibilityCaptureComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGridVisibilityCaptureComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGridVisibilityCaptureComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FOVAngle` | `float` | Camera field of view (in degrees). |
| `CaptureViewSize` | `FIntPoint` | - |
| `NearClipPlane` | `float` | - |
| `GridMesh` | `UStaticMesh *` | - |
| `GridMeshSizeScale` | `FVector` | - |
| `GridMeshLocationOffset` | `FVector` | - |
| `bForceLowestLOD` | `uint32` | - |
| `bHiddenFoliage` | `uint32` | - |
| `OcclusionDepthDiffThreshold` | `float` | - |
| `bShouldRenderGridMeshInMainPass` | `uint32` | - |
| `MaxNumProcessWaitingResultCmdsPerFrame` | `int32` | - |
| `MaxNumProcessWaitingCalculateCmdsPerFrame` | `int32` | - |
| `GridSize` | `FIntPoint` | - |
| `RenderTargetToCreateRenderer` | `UTextureRenderTarget2D *` | - |
| `GridMeshComp` | `UInstancedStaticMeshComponent *` | - |

## Functions

### `InitGridIDVisibilityCalculation`

```text
InitGridIDVisibilityCalculation(InGridLocations: TArray < FVector > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InGridLocations` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CalculateGridIDVisibility`

```text
CalculateGridIDVisibility(GridID: int32, CameraLocations: TArray < FGridVisibilityCameraInfo > &, PotentialGrids: TArray < int32 > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GridID` | `int32` | - |
| `CameraLocations` | `TArray < FGridVisibilityCameraInfo > &` | - |
| `PotentialGrids` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FinishGridIDVisibilityCalculation`

```text
FinishGridIDVisibilityCalculation() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
