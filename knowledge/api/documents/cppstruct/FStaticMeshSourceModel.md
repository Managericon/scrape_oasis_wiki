---
id: "api:cppstruct:FStaticMeshSourceModel"
title: "FStaticMeshSourceModel"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FStaticMeshSourceModel.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FStaticMeshSourceModel

-----------------------------------------------------------------------------
-----------------------------------------------------------------------------

  Source model from which a renderable static mesh is built.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BuildSettings` | `FMeshBuildSettings` | Settings applied when building the mesh. |
| `ReductionSettings` | `FMeshReductionSettings` | Reduction settings to apply when building render data. |
| `RemeshingSettings_DEPRECATED` | `FSimplygonRemeshingSettings` | - |
| `bHasBeenSimplified` | `bool` | - |
| `OptimizationSettings` | `FGroupedStaticMeshOptimizationSettings` | - |
| `LODDistance_DEPRECATED` | `float` | Allow per-LOD overriding of lightmap resolution <br>	UPROPERTY(EditAnywhere, Category=Lighting)<br>	int32 OverriddenLightMapRes; |
| `ScreenSize` | `float` | ScreenSize to display this LOD.<br>	  The screen size is based around the projected diameter of the bounding<br>	  sphere of the model. i.e. 0.5 means half the screen's maximum dimension. |
| `SourceImportFilename` | `FString` | The file path that was used to import this LOD. |
| `bImportWithBaseMesh` | `bool` | Weather this LOD was imported in the same file as the base mesh. |
