---
id: "api:cppstruct:FHierarchicalSimplification"
title: "FHierarchicalSimplification"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FHierarchicalSimplification.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FHierarchicalSimplification

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PropertyFilter` | `EHLODPropertyFilter` | Select which mode to display properties for. Grid mode shows Grid-specific properties; Cluster mode shows Cluster-specific properties. |
| `TransitionScreenSize` | `float` | The screen radius an mesh object should reach before swapping to the LOD actor, once one of parent displays, it won't draw any of children. |
| `OverrideDrawDistance` | `float` | - |
| `bUseOverrideDrawDistance` | `bool` | - |
| `bAllowSpecificExclusion` | `uint8` | - |
| `bSimplifyMesh` | `bool` | If this is true, it will simplify mesh but it is slower.<br>	 If false, it will just merge actors but not simplify using the lower LOD if exists.<br>	 For example if you build LOD 1, it will use LOD 1 of the mesh to merge actors if exists.<br>	 If you merge material, it will reduce drawcalls. |
| `ProxySetting` | `FMeshProxySettings` | Simplification Setting if bSimplifyMesh is true |
| `MergeSetting` | `FMeshMergingSettings` | Merge Mesh Setting if bSimplifyMesh is false |
| `DesiredBoundRadius` | `float` | Desired Bounding Radius for clustering - this is not guaranteed but used to calculate filling factor for auto clustering |
| `DesiredFillingPercentage` | `float` | Desired Filling Percentage for clustering - this is not guaranteed but used to calculate filling factor  for auto clustering |
| `DesiredGridSize` | `float` | - |
| `DesiredGridOffset` | `float` | - |
| `DesiredGridScaleFactor` | `int32` | Grid Scale Factor for upper HLOD levels (Grid mode only).<br>	   Must be an integer to guarantee that upper-level Grid boundaries align<br>	   exactly with lower-level Grid boundaries, preventing overlap during HLOD level transitions.<br>	 <br>	   This property is only meaningful for Setup[1] and above:<br>	   - Setup[0]: DesiredGridScaleFactor is IGNORED (Level0 GridSize = DesiredGridSize directly)<br>	   - Setup[1]: Level1 GridSize = Level0 GridSize  Setup[1].ScaleFactor<br>	   - Setup[2]: Level2 GridSize = Level1 GridSize  Setup[2].ScaleFactor<br>	 <br>	   Example: ScaleFactor=2 means each upper Grid cell contains exactly 2x2=4 lower Grid cells. |
| `DesiredGridVolume` | `TArray < FVector4 >` | - |
| `GridIgnoreStaticMeshs` | `TArray < FString >` | - |
| `HLODGroups` | `TArray < FHLODGroup >` | - |
| `MinNumberOfActorsToBuild` | `int32` | Min number of actors to build LODActor |
| `bOnlyGenerateClustersForVolumes` | `bool` | Min number of actors to build LODActor |
| `bReusePreviousLevelClusters` | `bool` | Will reuse the clusters generated for the previous (lower) HLOD level |
| `LOD0ReduceFactor` | `float` | LOD0 percentage-based reduction factor (OriginalTriangles  this value). Corresponds to global r.HLOD.ProxyMeshLOD0ReduceFactor |
| `PerVolumeTriangles` | `float` | Volume-based: triangles allowed per cubic-meter of Bounds. Corresponds to global r.HLOD.ProxyMeshPerVolumeTraingles |
| `LODReduceFactor` | `float` | LOD1~N successive reduction factor. Corresponds to global r.HLOD.ProxyMeshReduceFactor |
| `LODMinTriangles` | `int32` | Minimum triangle threshold (no further LOD generated below this). Corresponds to global r.HLOD.ProxyMeshLODMinTriangles |
| `LODMaxCount` | `int32` | Maximum LOD level count. Corresponds to global r.HLOD.ProxyMeshLODMax |
| `ProxyMeshLOD1SwitchDistance` | `float` | Distance (in cm) at which ProxyMesh switches from LOD0 to LOD1. Overrides legacy triangle-count-based ScreenSize calculation. |
| `bOverrideProxyMeshLOD1SwitchDistance` | `bool` | - |
| `ProxyMeshCullingDistance` | `float` | Distance (in cm) at which ProxyMesh is culled (not rendered). Overrides legacy CVar-based culling distance. |
| `bOverrideProxyMeshCullingDistance` | `bool` | - |
| `ProxyMeshSmallObjectCullThreshold` | `float` | 小物件剔除阈值（cm）：Box 最长边（缩放后）低于此值的实例组件将被剔除，不参与 ProxyMesh 生成，但仍保留为 SubActor。<br>	   设为 0 则禁用小物件剔除。每一层级可独立配置不同阈值。<br>	   例：Level0 设为 800cm，Level1 设为 1500cm（上层级剔除更粗粒度的小物件）。 |
