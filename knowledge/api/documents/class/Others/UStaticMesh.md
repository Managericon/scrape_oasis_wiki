---
id: "api:class:UStaticMesh"
title: "UStaticMesh"
source: "https://developer.gp.qq.com/api/class/detail/Others/UStaticMesh.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UStaticMesh

A StaticMesh is a piece of geometry that consists of a static set of polygons.
  Static Meshes can be translated, rotated, and scaled, but they cannot have their vertices animated in any way. As such, they are more efficient
  to render than other types of geometry such as USkeletalMesh, and they are often the basic building block of levels created in the engine.
 
  @see AStaticMeshActor, UStaticMeshComponent

## Inheritance

`UObject` -> `IInterface_CollisionDataProvider` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSkipHISMBoundCheck` | `bool` | - |
| `bHasROCData` | `bool` | - |
| `FSOCOccluder` | `UFlakeOccluder *` | - |
| `ReplaceMaterial` | `UMaterialInterface *` | - |
| `ShadowProxyMesh` | `UStaticMesh *` | Proxy mesh used by TA tools to generate hidden shadow caster components for components using this StaticMesh. |
| `PerLODBiasTypeInfo` | `TArray < FMeshPerLODBiasArray >` | When autonomous or simulated pawn needs special LOD bias |
| `bUseLODBiasExt` | `bool` | - |
| `bAutoUpdateLODBiasExt` | `bool` | - |
| `PerLODBiasTypeInfoExt` | `TArray < FMeshLODBiasCondition >` | - |
| `MinLOD` | `int32` | Minimum LOD to use for rendering.  This is the default setting for the mesh and can be overridden by component settings. |
| `Materials_DEPRECATED` | `TArray < UMaterialInterface * >` | Materials used by this static mesh. Individual sections index in to this array. |
| `StaticMaterials` | `TArray < FStaticMaterial >` | - |
| `LightmapUVDensity` | `float` | - |
| `LightMapResolution` | `int32` | - |
| `LightMapCoordinateIndex` | `int32` | The light map coordinate index |
| `DistanceFieldSelfShadowBias` | `float` | Useful for reducing self shadowing from distance field methods when using world position offset to animate the mesh's vertices. |
| `ExpectedQualityLimit` | `FExpectedQuality` | - |
| `bGenerateMeshDistanceField` | `uint32` | Whether to generate a distance field for this mesh, which can be used by DistanceField Indirect Shadows.<br>	  This is ignored if the project's 'Generate Mesh Distance Fields' setting is enabled. |
| `bLazyLoadBulkData` | `uint32` | Lazy load bulk data for reduce memory used |
| `bAllowMinLodBiasCfg` | `uint32` | allow MinLodBias for global config (r.StaticMeshMinLodBias) |
| `bDisableGenerateHLOD` | `uint32` | - |
| `bHasHLODTag` | `uint32` | Runtime flag: whether this StaticMesh participates in HLOD (computed from ReorganizationTags at PreSave) |
| `MinLodBiasDeviceGrade` | `uint8` | allow min lod bias if device grade < this |
| `bUseFSOCOccluderIgnoreBlend` | `uint8` | - |
| `BodySetup` | `UBodySetup *` | - |
| `LODForCollision` | `int32` | Specifies which mesh LOD to use for complex (per-poly) collision.<br>	 	Sometimes it can be desirable to use a lower poly representation for collision to reduce memory usage, improve performance and behaviour.<br>	 	Collision representation does not change based on distance to camera. |
| `CullingScreenSize` | `float` | Culling screen size |
| `bUseScreenSizeModifier` | `bool` | - |
| `ScreenSizeCullingRoughDistance` | `float` | Rough Distance of Screen size Culling |
| `bIsGrass` | `bool` | grass flag, we need this special flag since grasses are so important in pubg game |
| `bIsTree` | `bool` | - |
| `bStripComplexCollisionForConsole_DEPRECATED` | `uint32` | If true, strips unwanted complex collision data aka kDOP tree when cooking for consoles.<br>		On the Playstation 3 data of this mesh will be stored in video memory. |
| `bHasNavigationData` | `uint32` | If true, mesh will have NavCollision property with additional data for navmesh generation and usage.<br>	    Set to false for distant meshes (always outside navigation bounds) to save memory on collision data. |
| `bIsStreamable` | `bool` | Streamable flag, determine whether to split the lod serialization, WITH_STREAMING_SM_LOD |
| `HiddenStreamFactor` | `uint8` | - |
| `bCompressData` | `bool` | - |
| `bUseCoarseGIMip` | `bool` | - |
| `NotInlineLODCount` | `uint8` | - |
| `bSupportUniformlyDistributedSampling` | `uint32` | - |
| `LpvBiasMultiplier` | `float` | Bias multiplier for Light Propagation Volume lighting |
| `bAllowCPUAccess` | `bool` | If true, will keep geometry data CPU-accessible in cooked builds, rather than uploading to GPU memory and releasing it from CPU memory.<br>	 	This is required if you wish to access StaticMesh geometry data on the CPU at runtime in cooked builds (e.g. to convert StaticMesh to ProceduralMeshComponent) |
| `bCustomWaterBeOccludeed` | `bool` | - |
| `EncodeBits_Position` | `int32` | - |
| `EncodeBits_TexCoord` | `int32` | - |
| `EncodeBits_Normal` | `int32` | - |
| `EncodeBits_Generic` | `int32` | - |
| `EncodeBits_VertexColor` | `int32` | - |
| `EncodeSpeed` | `int32` | - |
| `DecodeSpeed` | `int32` | - |
| `Sockets` | `TArray < UStaticMeshSocket * >` | Array of named socket locations, set up in editor and used as a shortcut instead of specifying<br>	 	everything explicitly to AttachComponent in the StaticMeshComponent. |
| `PositiveBoundsExtension` | `FVector` | Bound extension values in the positive direction of XYZ, positive value increases bound size |
| `NegativeBoundsExtension` | `FVector` | Bound extension values in the negative direction of XYZ, positive value increases bound size |
| `ExtendedBounds` | `FBoxSphereBounds` | Original mesh bounds extended with PositiveNegativeBoundsExtension |
| `SubLocalBounds` | `TArray < FBoxSphereBounds >` | - |
| `OcclusionCullingVertex` | `TArray < FVector4 >` | - |
| `IndirectLightingCachePositionOffset` | `FVector` | - |
| `bUseQuantization` | `bool` | - |
| `ElementToIgnoreForTexFactor` | `int32` | Index of an element to ignore while gathering streaming texture factors.<br>	  This is useful to disregard automatically generated vertex data which breaks texture factor heuristics. |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `NavCollision` | `UNavCollision *` | Pre-build navigation collision |
| `SimpleMaterials` | `TArray < FStaticSimpleMaterial >` | Simple material setting |
| `bCloseMeshOpt` | `bool` | - |
| `UVDensityMultiplier` | `float` | - |
| `SourceModels` | `TArray < FStaticMeshSourceModel >` | Imported raw mesh bulk data. |
| `MeshDescriptions` | `UStaticMeshDescriptions *` | Container holding mesh descriptions for each LOD |
| `SectionInfoMap` | `FMeshSectionInfoMap` | Map of LOD+Section index to per-section info. |
| `OriginalSectionInfoMap` | `FMeshSectionInfoMap` | We need the OriginalSectionInfoMap to be able to build mesh in a non destructive way. Reduce has to play with SectionInfoMap in case some sections disappear.<br>	  This member will be update in the following situation<br>	  1. After a static mesh importreimport<br>	  2. Postload, if the OriginalSectionInfoMap is empty, we will fill it with the current SectionInfoMap<br>	 <br>	  We do not update it when the user shuffle section in the staticmesh editor because the OriginalSectionInfoMap must always be in sync with the saved rawMesh bulk data. |
| `LODGroup` | `FName` | The LOD group to which this mesh belongs. |
| `bAutoComputeLODScreenSize` | `uint32` | If true, the screen sizees at which LODs swap are computed automatically. |
| `ImportVersion` | `int32` | The last import version |
| `MaterialRemapIndexPerImportVersion` | `TArray < FMaterialRemapIndex >` | - |
| `LightmapUVVersion` | `int32` | The lightmap UV generation version used during the last derived data build |
| `Id_DEPRECATED` | `FGuid` | The following is unique identifier for UStaticMesh. for generating cache key. |
| `bIsUsedInLandscapeFlaten` | `bool` | Whether to Flaten Landscape |
| `FlattenXHalfLength` | `float` | Default to Bound.X0.5 + 100 |
| `FlattenYHalfLength` | `float` | Default to Bound.Y0.5 + 100 |
| `FlattenZHeight` | `float` | Default to 0 |
| `FlattenFallOffDistance` | `float` | Default to 1000 |
| `AssetImportData` | `UAssetImportData *` | Importing data and options used for this mesh |
| `SourceFilePath_DEPRECATED` | `FString` | Path to the resource used to construct this static mesh |
| `SourceFileTimestamp_DEPRECATED` | `FString` | DateTime-stamp of the file from the last import |
| `ThumbnailInfo` | `UThumbnailInfo *` | Information for thumbnail rendering |
| `EditorCameraPosition` | `FAssetEditorOrbitCameraPosition` | The stored camera position to use as a default for the static mesh editor |
| `bCustomizedCollision` | `bool` | If the user has modified collision in any way or has custom collision imported. Used for determining if to auto generate collision on import |
| `bUseFSOCOccluder` | `bool` | 是否使用FSOC遮挡体。当为true时，在运行时使用FSOCOccluder进行遮挡剔除。 |
| `OccluderMesh` | `UStaticMesh *` | Specifies the custom occluder mesh for software occlusion |
| `OccluderBadFaceMesh` | `UStaticMesh *` | - |
| `OccluderAvgValidRate` | `float` | - |
| `OccluderAvgErrorRate` | `float` | - |
| `bUseAsCustomOccluder` | `bool` | 标记该Mesh是否作为其他Mesh的自定义Occluder使用。<br>	  当此属性为true时，在编辑器保存资产时会自动构建FSOCOccluder数据，<br>	  供其他Mesh作为OccluderMesh引用使用。<br>	  注意：设置OccluderMesh的Mesh会在Cook时复用OccluderMesh的FSOCOccluder数据。 |
| `bPreviewDraco` | `bool` | - |
| `bUseHighPrecision` | `bool` | - |
| `bUseUVAverage` | `bool` | - |
| `bOptimizeNormal` | `bool` | - |
| `SubBoundsIncludedVertices` | `TArray < FSubBoundsIncludedVertices >` | - |
| `ReorganizationTags` | `FReorganizationTagsContainer` | Reorganization tags for Level Partition system |
| `LightmapType` | `ELightmapType` | Controls the Lightmap type used by the Component when creating an Actor from this StaticMesh |
| `bGenerateSurfaceSample` | `uint8` | Controls whether the Component generates surface samples (VolumeProbeGI) when creating an Actor from this StaticMesh |

## Functions

### `GetAllSectionTexelDensities`

```text
GetAllSectionTexelDensities() -> ENGINE_API TArray < FSectionTexelDensity >
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API TArray < FSectionTexelDensity >` | - |

### `GetNumLODs`

```text
GetNumLODs() -> ENGINE_API int32
```

Returns the number of LODs used by the mesh.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API int32` | - |

### `GetBounds`

```text
GetBounds() -> ENGINE_API FBoxSphereBounds
```

Returns the number of bounds of the mesh.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FBoxSphereBounds` | The bounding box represented as box origin with extents and also a sphere that encapsulates that box |

### `GetBoundingBox`

```text
GetBoundingBox() -> ENGINE_API FBox
```

Returns the bounding box, in local space including bounds extension(s), of the StaticMesh asset

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FBox` | - |

### `GetNumSections`

```text
GetNumSections(InLOD: int32) -> ENGINE_API int32
```

Returns number of Sections that this StaticMesh has, in the supplied LOD (LOD 0 is the highest)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLOD` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API int32` | - |

### `GetMaterial`

```text
GetMaterial(MaterialIndex: int32) -> ENGINE_API UMaterialInterface *
```

Gets a Material given a Material Index and an LOD number

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UMaterialInterface *` | Requested material |

### `GetMaterialIndex`

```text
GetMaterialIndex(MaterialSlotName: FName) -> ENGINE_API int32
```

Gets a Material index given a slot name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialSlotName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API int32` | Requested material |

### `GenerateLODForHLODMesh`

```text
GenerateLODForHLODMesh(Flags: int) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Flags` | `int` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`
