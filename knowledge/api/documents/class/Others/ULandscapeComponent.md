---
id: "api:class:ULandscapeComponent"
title: "ULandscapeComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULandscapeComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULandscapeComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SectionBaseX` | `int32` | X offset from global components grid origin (in quads) |
| `SectionBaseY` | `int32` | Y offset from global components grid origin (in quads) |
| `ComponentSizeQuads` | `int32` | Total number of quads for this component, has to be >0 |
| `SubsectionSizeQuads` | `int32` | Number of quads for a subsection of the component. SubsectionSizeQuads+1 must be a power of two. |
| `NumSubsections` | `int32` | Number of subsections in X or Y axis |
| `OverrideMaterial` | `UMaterialInterface *` | - |
| `OverrideHoleMaterial` | `UMaterialInterface *` | - |
| `OverrideMaterial_ForPC` | `UMaterialInterface *` | - |
| `OverrideHoleMaterial_ForPC` | `UMaterialInterface *` | - |
| `bShouldSerializationGrassWeightDataForPC` | `bool` | - |
| `OverrideOtherMaterials` | `TMap < FName , UMaterialInterface * >` | - |
| `OverridePhyxMaterial` | `FOverridePhyxMaterial` | - |
| `bOverrideGrassTypes` | `uint8` | - |
| `GrassTypes` | `TArray < ULandscapeGrassType * >` | - |
| `bOverrideGrassTypes_ForPC` | `uint8` | - |
| `GrassTypes_ForPC` | `TArray < ULandscapeGrassType * >` | - |
| `MaterialInstances` | `TArray < UMaterialInstanceConstant * >` | - |
| `OtherMaterialInstances` | `TMap < FName , UMaterialInstanceConstant * >` | - |
| `WeightmapLayerAllocations` | `TArray < FWeightmapLayerAllocationInfo >` | List of layers, and the weightmap and channel they are stored |
| `WeightmapTextures` | `TArray < UTexture2D * >` | Weightmap texture reference |
| `SplatmapTextures` | `TArray < UTexture2D * >` | Helper to getset splatmap data, hold reference to splatmap textures |
| `SplatmapLayerAllocations` | `TArray < FSplatmapLayerAllocationInfo >` | - |
| `bUseMaterialId` | `bool` | Cached value of bUseMaterialId, should be equal to bUseMaterialId in ALandscape |
| `SplatmapG8Texture` | `UTexture2D *` | - |
| `SplatmapG16Texture` | `UTexture2D *` | - |
| `MaterialInstances_ForPC` | `TArray < UMaterialInstanceConstant * >` | - |
| `WeightmapTextures_ForPC` | `TArray < UTexture2D * >` | Weightmap texture reference |
| `VisibilityLayerChannel` | `int32` | Visibility layer channel in weightmap |
| `XYOffsetmapTexture` | `UTexture2D *` | XYOffsetmap texture reference |
| `WeightmapScaleBias` | `FVector4` | UV offset to component's weightmap data from component local coordinates |
| `WeightmapSubsectionOffset` | `float` | U or V offset into the weightmap for the first subsection, in texture UV space |
| `HeightmapScaleBias` | `FVector4` | UV offset to Heightmap data from component local coordinates |
| `HeightmapTexture` | `UTexture2D *` | Heightmap texture reference |
| `MultiVisibilityTextureData` | `TMap < FString , FVisibilityData >` | - |
| `VisibleVisibilityLayer` | `FString` | - |
| `CachedLocalBox` | `FBox` | Cached local-space bounding box, created at heightmap update time |
| `CollisionComponent` | `TLazyObjectPtr < ULandscapeHeightfieldCollisionComponent >` | Reference to associated collision component |
| `SplatmapScaleBias` | `FVector4` | UV offset to component's splatmap data from component local coordinates |
| `FarLandDiffuseTexture` | `UTexture2D *` | - |
| `FarLandNormalTexture` | `UTexture2D *` | - |
| `MapBuildDataId` | `FGuid` | Uniquely identifies this component's built map data. |
| `IrrelevantLights_DEPRECATED` | `TArray < FGuid >` | Legacy irrelevant lights |
| `CollisionMipLevel` | `int32` | Heightfield mipmap used to generate collision |
| `SimpleCollisionMipLevel` | `int32` | Heightfield mipmap used to generate simple collision |
| `NegativeZBoundsExtension` | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the negative Z axis, positive value increases bound size |
| `PositiveZBoundsExtension` | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the positive Z axis, positive value increases bound size |
| `StaticLightingResolution` | `float` | StaticLightingResolution overriding per component, default value 0 means no overriding |
| `ForcedLOD` | `int32` | Forced LOD level to use when rendering |
| `LODBias` | `int32` | LOD level Bias to use when rendering |
| `MobileVertexHoleMaxLOD` | `int32` | The max lod level that allow landscape component to use vertex hole. If the lod level greater than this limitation, all vertex hole on landscape will vanish |
| `LODDeltaVertex` | `TArray < float >` | Subsection's Delta Vertex for fixing LOD level |
| `MaxDeltaVertex` | `float` | - |
| `StateId` | `FGuid` | - |
| `BakedTextureMaterialGuid` | `FGuid` | The Material Guid that used when baking, to detect material recompilations |
| `GIBakedBaseColorTexture` | `UTexture2D *` | Pre-baked Base Color texture for use by distance field GI |
| `FSOCOccluder` | `UFlakeOccluder *` | - |
| `MobileBlendableLayerMask` | `uint8` | For ES2 |
| `MobileMaterialInterface` | `UMaterialInterface *` | Material interface used for ES2. Serialized only when cooking or loading cooked builds. |
| `MatIDFallbackMaterialInterface` | `UMaterialInterface *` | - |
| `OtherMobileMaterialInterfaces` | `TMap < FName , UMaterialInterface * >` | - |
| `MobileWeightmapTextures` | `TArray < UTexture2D * >` | Generated weightnormal map texture used for ES2. Serialized only when cooking or loading cooked builds. |
| `MobileWeightNormalmapTexture` | `UTexture2D *` | - |
| `bMobileMultiLayers` | `uint32` | - |
| `CachedHeightData` | `TArray < uint16 >` | - |
| `CachedHaltonBaseIndex` | `TArray < bool >` | - |
| `CachedAddHaltonBaseIndexList` | `TArray < int32 >` | - |
| `bHasROCData` | `bool` | Has ROCData？ |
| `DeformHeightmap` | `UTexture2D *` | - |
| `UsedOtherMaterialName` | `FName` | - |

## Functions

### `GenerateSplatmapG16AndG8`

```text
GenerateSplatmapG16AndG8() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
