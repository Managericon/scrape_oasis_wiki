---
id: "api-chunk:class:7"
title: "Oasis API class chunk 7"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlatformInterfaceWebResponse.json -->

# UPlatformInterfaceWebResponse

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OriginalURL` | `FString` | This holds the original requested URL |
| `ResponseCode` | `int32` | Result code from the response (200=OK, 404=Not Found, etc) |
| `Tag` | `int32` | A user-specified tag specified with the request |
| `StringResponse` | `FString` | For string results, this is the response |
| `BinaryResponse` | `TArray < uint8 >` | For non-string results, this is the response |

## Functions

### `GetNumHeaders`

```text
GetNumHeaders() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | the number of headervalue pairs |

### `GetHeader`

```text
GetHeader(HeaderIndex: int32, Header: FString &, Value: FString &) -> void
```

Retrieve the header and value for the given index of headervalue pair

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HeaderIndex` | `int32` | - |
| `Header` | `FString &` | - |
| `Value` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetHeaderValue`

```text
GetHeaderValue(HeaderName: FString &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HeaderName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the value for the given header (or "" if no matching header) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlatformMediaSource.json -->

# UPlatformMediaSource

A media source that selects other media sources based on target platform.
 
  Use this asset to override media sources on a per-platform basis.

## Inheritance

`UMediaSource`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | Default media source.<br>	 <br>	  This media source will be used if no source was specified for a target platform. |
| `PlatformMediaSources` | `TMap < FString , UMediaSource * >` | Media sources per platform. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlayer.json -->

# UPlayer

## Inheritance

`UObject` -> `FExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | The actor this player controls. |
| `CurrentNetSpeed` | `int32` | the current speed of the connection |
| `ConfiguredInternetSpeed` | `int32` | @todo document |
| `ConfiguredLanSpeed` | `int32` | @todo document |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlayerInput.json -->

# UPlayerInput

end: 单条记录，滑屏轨迹中的一个点 

  Object within PlayerController that processes player input.
  Only exists on the client in network games.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableKeyInput` | `bool` | - |
| `InputTouchCacheDataList` | `TArray < FInputTouchCacheData >` | - |
| `DebugExecBindings` | `TArray < struct FKeyBind >` | Generic bindings of keys to Exec()-compatible strings for development purposes only |
| `InvertedAxis` | `TArray < FName >` | List of Axis Mappings that have been inverted |

## Functions

### `SetMouseSensitivity`

```text
SetMouseSensitivity(Sensitivity: float) -> void
```

Exec function to change the mouse sensitivity

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Sensitivity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBind`

```text
SetBind(BindName: FName, Command: FString &) -> void
```

Exec function to add a debug exec command

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindName` | `FName` | - |
| `Command` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvertAxisKey`

```text
InvertAxisKey(AxisKey: FKey) -> void
```

Exec function to invert an axis key

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisKey` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvertAxis`

```text
InvertAxis(AxisName: FName) -> void
```

Exec function to invert an axis mapping

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSmoothing`

```text
ClearSmoothing() -> void
```

Exec function to reset mouse smoothing values

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPlayMontageCallbackProxy.json -->

# UPlayMontageCallbackProxy

## Inheritance

`UObject`

## Functions

### `CreateProxyObjectForPlayMontage`

```text
CreateProxyObjectForPlayMontage(InSkeletalMeshComponent: USkeletalMeshComponent *, MontageToPlay: UAnimMontage *, PlayRate: float, StartingPosition: float, StartingSection: FName) -> UPlayMontageCallbackProxy *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSkeletalMeshComponent` | `USkeletalMeshComponent *` | - |
| `MontageToPlay` | `UAnimMontage *` | - |
| `PlayRate` | `float` | - |
| `StartingPosition` | `float` | - |
| `StartingSection` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UPlayMontageCallbackProxy *` | - |

### `OnMontageBlendingOut`

```text
OnMontageBlendingOut(Montage: UAnimMontage *, bInterrupted: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMontageEnded`

```text
OnMontageEnded(Montage: UAnimMontage *, bInterrupted: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Montage` | `UAnimMontage *` | - |
| `bInterrupted` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyBeginReceived`

```text
OnNotifyBeginReceived(NotifyName: FName, BranchingPointNotifyPayload: FBranchingPointNotifyPayload &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |
| `BranchingPointNotifyPayload` | `FBranchingPointNotifyPayload &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyEndReceived`

```text
OnNotifyEndReceived(NotifyName: FName, BranchingPointNotifyPayload: FBranchingPointNotifyPayload &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |
| `BranchingPointNotifyPayload` | `FBranchingPointNotifyPayload &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnCompleted`

```text
OnCompleted(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBlendOut`

```text
OnBlendOut(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInterrupted`

```text
OnInterrupted(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyBegin`

```text
OnNotifyBegin(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnNotifyEnd`

```text
OnNotifyEnd(NotifyName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NotifyName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPointLightComponent.json -->

# UPointLightComponent

A light component which emits light from a single point equally in all directions.

## Inheritance

`ULightComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Radius_DEPRECATED` | `float` | - |
| `AttenuationRadius` | `float` | Bounds the light's visible influence.  <br>	  This clamping of the light's influence is not physically correct but very important for performance, larger lights cost more. |
| `bUseInverseSquaredFalloff` | `uint32` | Whether to use physically based inverse squared distance falloff, where AttenuationRadius is only clamping the light's contribution.  <br>	  Disabling inverse squared falloff can be useful when placing fill lights (don't want a super bright spot near the light).<br>	  When enabled, the light's Intensity is in units of lumens, where 1700 lumens is a 100W lightbulb.<br>	  When disabled, the light's Intensity is a brightness scale. |
| `LightFalloffExponent` | `float` | Controls the radial falloff of the light when UseInverseSquaredFalloff is disabled. <br>	  2 is almost linear and very unrealistic and around 8 it looks reasonable.<br>	  With large exponents, the light has contribution to only a small area of its influence radius but still costs the same as low exponents. |
| `SourceRadius` | `float` | Radius of light source shape.<br>	  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| `SoftSourceRadius` | `float` | Soft radius of light source shape.<br>	 Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| `SourceLength` | `float` | Length of light source shape.<br>	  Note that light sources shapes which intersect shadow casting geometry can cause shadowing artifacts. |
| `bSimulateRectLight` | `uint32` | By luciuszhang: when in rect light mode, source radius is the rect light source width. |
| `bSimulatePortalLight` | `uint32` | By luciuszhang: Portal light will be used in lightmass for IdeaBake, it is just a flag for Rect Light. |
| `RectLightSourceWidth` | `float` | By luciuszhang: rect light source width. |
| `RectLightSourceHeight` | `float` | By luciuszhang: rect light source height. |
| `bEnableForVertexPointLight` | `uint32` | - |
| `LightmassSettings` | `FLightmassPointLightSettings` | The Lightmass settings for this object. |

## Functions

### `SetAttenuationRadius`

```text
SetAttenuationRadius(NewRadius: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFalloffExponent`

```text
SetLightFalloffExponent(NewLightFalloffExponent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFalloffExponent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSourceRadius`

```text
SetSourceRadius(bNewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSoftSourceRadius`

```text
SetSoftSourceRadius(bNewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSourceLength`

```text
SetSourceLength(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSimulateRectLight`

```text
SetSimulateRectLight(newValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `newValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSimulatePortalLight`

```text
SetSimulatePortalLight(newValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `newValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRectLightSourceWidth`

```text
SetRectLightSourceWidth(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRectLightSourceHeight`

```text
SetRectLightSourceHeight(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPoseableMeshComponent.json -->

# UPoseableMeshComponent

UPoseableMeshComponent that allows bone transforms to be driven by blueprint.

## Inheritance

`USkinnedMeshComponent`

## Functions

### `SetBoneTransformByName`

```text
SetBoneTransformByName(BoneName: FName, InTransform: FTransform &, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InTransform` | `FTransform &` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoneLocationByName`

```text
SetBoneLocationByName(BoneName: FName, InLocation: FVector, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InLocation` | `FVector` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoneRotationByName`

```text
SetBoneRotationByName(BoneName: FName, InRotation: FRotator, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InRotation` | `FRotator` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoneScaleByName`

```text
SetBoneScaleByName(BoneName: FName, InScale3D: FVector, BoneSpace: EBoneSpaces :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InScale3D` | `FVector` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoneTransformByName`

```text
GetBoneTransformByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetBoneLocationByName`

```text
GetBoneLocationByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetBoneRotationByName`

```text
GetBoneRotationByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetBoneScaleByName`

```text
GetBoneScaleByName(BoneName: FName, BoneSpace: EBoneSpaces :: Type) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `BoneSpace` | `EBoneSpaces :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ResetBoneTransformByName`

```text
ResetBoneTransformByName(BoneName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyPoseFromSkeletalComponent`

```text
CopyPoseFromSkeletalComponent(InComponentToCopy: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponentToCopy` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPoseAsset.json -->

# UPoseAsset

Pose Asset that can be blended by weight of curves

## Inheritance

`UAnimationAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PoseContainer` | `FPoseDataContainer` | Animation Pose Data |
| `bAdditivePose` | `bool` | Whether or not Additive Pose or not - these are property that needs post process, so |
| `BasePoseIndex` | `int32` | if -1, use ref pose |
| `RetargetSource` | `FName` | Base pose to use when retargeting |
| `SourceAnimation` | `UAnimSequence *` | - |
| `bOverridePoseNameFrom_0` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPoseWatch.json -->

# UPoseWatch

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Node` | `UEdGraphNode *` | - |
| `PoseWatchColour` | `FColor` | - |
| `CustomPoseDrawColour` | `FColor` | - |
| `CustomBoneText` | `FText` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPostProcessComponent.json -->

# UPostProcessComponent

PostProcessComponent. Enables Post process controls for blueprints.
 	Will use a parent UShapeComponent to provide volume data if available.

## Inheritance

`USceneComponent` -> `IInterface_PostProcessVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `FPostProcessSettings` | Post process settings to use for this volume. |
| `Priority` | `float` | Priority of this volume. In the case of overlapping volumes the one with the highest priority<br>	  overrides the lower priority ones. The order is undefined if two or more overlapping volumes have the same priority. |
| `BlendRadius` | `float` | World space radius around the volume that is used for blending (only if not unbound). |
| `BlendWeight` | `float` | 0:no effect, 1:full effect |
| `bEnabled` | `uint32` | Whether this volume is enabled or not. |
| `bUnbound` | `uint32` | set this to false to use the parent shape component as volume bounds. True affects the whole world regardless. |

## Functions

### `AddOrUpdateBlendable`

```text
AddOrUpdateBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >, InWeight: float) -> ENGINE_API void
```

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendableObject` | `TScriptInterface < IBlendableInterface >` | - |
| `InWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `AddWeatherCompTag`

```text
AddWeatherCompTag() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearCustomGIFallbackSH`

```text
ClearCustomGIFallbackSH() -> ENGINE_API void
```

Clear all Custom GI Fallback SH coefficients (reset to zero)

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GenerateCustomGIFallbackSH`

```text
GenerateCustomGIFallbackSH() -> ENGINE_API void
```

Generate Custom GI Fallback SH coefficients from directional colors using Monte Carlo integration

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GenerateCustomGIFallbackSHFromCubeMap`

```text
GenerateCustomGIFallbackSHFromCubeMap() -> ENGINE_API void
```

Generate Spherical Harmonics coefficients from CubeMap texture using Monte Carlo sampling

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPreviewMeshCollection.json -->

# UPreviewMeshCollection

A simple collection of skeletal meshes used for in-editor preview

## Inheritance

`UDataAsset` -> `IPreviewCollectionInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Skeleton` | `USkeleton *` | - |
| `SkeletalMeshes` | `TArray < FPreviewMeshCollectionEntry >` | The skeletal meshes that this collection contains |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPrimaryAssetLabel.json -->

# UPrimaryAssetLabel

A seed file that is created to mark referenced assets as part of this primary asset

## Inheritance

`UPrimaryDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Rules` | `FPrimaryAssetRules` | Management rules for this specific asset, if set it will override the type rules |
| `LogicChunkName` | `FString` | Pak file name |
| `FinalChunkName` | `FString` | - |
| `ChunkOutputPath` | `FString` | - |
| `bLabelAssetsInMyDirectory` | `uint32` | True to Label everything in this directory and sub directories |
| `AssignedDirectories` | `TArray < FDirectoryPath >` | True to Label everything in this directory and sub directories |
| `ExcludeDirectories` | `TArray < FDirectoryPath >` | - |
| `ExcludeAssets` | `TSet < FName >` | - |
| `bIsRuntimeLabel` | `uint32` | Set to true if the label asset itself should be cooked and available at runtime. This does not affect the assets that are labeled, they are set with cook rule |
| `ExplicitAssets` | `TArray < TSoftObjectPtr < UObject > >` | List of manually specified assets to label |
| `ExplicitBlueprints` | `TArray < TSoftClassPtr < UObject > >` | List of manually specified blueprint assets to label |
| `AssetCollection` | `FCollectionReference` | Collection to load asset references out of |
| `Key` | `FString` | - |
| `IV` | `FString` | - |
| `DataTableAsExplicitAssets` | `TSoftObjectPtr < UDataTable >` | List of manually specified assets to label |
| `ManagerRuleNames` | `TArray < FString >` | - |
| `bTriggerUpdateManagerRules` | `bool` | - |
| `bUpdateManagerRulesWhenSaved` | `bool` | - |
| `bForceReloadManagerRule` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPrimaryDataAsset.json -->

# UPrimaryDataAsset

A DataAsset that implements GetPrimaryAssetId and has asset bundle support, which makes it something that can be manually loadedunloaded from the AssetManager

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AssetBundleData` | `FAssetBundleData` | Asset Bundle data computed at save time. In cooked builds this is accessible from AssetRegistry |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UPrimitiveComponent.json -->

# UPrimitiveComponent

PrimitiveComponents are SceneComponents that contain or generate some sort of geometry, generally to be rendered or used as collision data.
  There are several subclasses for the various types of geometry, but the most common by far are the ShapeComponents (Capsule, Sphere, Box), StaticMeshComponent, and SkeletalMeshComponent.
  ShapeComponents generate geometry that is used for collision detection but are not rendered, while StaticMeshComponents and SkeletalMeshComponents contain pre-built geometry that is rendered, but can also be used for collision detection.

## Inheritance

`USceneComponent` -> `INavRelevantInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExpectedQualityLimit` | `FExpectedQuality` | If limit > actual, primitive won't be rendered. |
| `bFixedLODDistanceFactorSwitch` | `uint8` | open this switch to use r.LOD.FixedDistanceFactor to control lod switch<br>	 for example r.LOD.FixedDistanceFactor=0.5 is half distance of origin to switch new lod |
| `CullingScreenSize` | `float` | If the screen percentage of the bounding box under this value, it will be culled.<br>	 Set "0" to avoid contribution culling |
| `MinDrawDistance` | `float` | The minimum distance at which the primitive should be rendered,<br>	  measured in world space units from the center of the primitive's bounding sphere to the camera position. |
| `LDMaxDrawDistance` | `float` | Max draw distance exposed to LDs. The real max draw distance is the min (disregarding 0) of this and volumes affecting this object. |
| `CachedMaxDrawDistance` | `float` | The distance to cull this primitive at.<br>	  A CachedMaxDrawDistance of 0 indicates that the primitive should not be culled by distance. |
| `DepthPriorityGroup` | `TEnumAsByte < enum ESceneDepthPriorityGroup >` | The scene depth priority group to draw the primitive in. |
| `ViewOwnerDepthPriorityGroup` | `TEnumAsByte < enum ESceneDepthPriorityGroup >` | The scene depth priority group to draw the primitive in, if it's being viewed by its owner. |
| `LightmapType` | `ELightmapType` | Controls the type of lightmap used for this component. |
| `VLMOptimizeType` | `EVLMOptimizeType` | To optimize performance, VLM can select optimization method. |
| `bInstanceCulling` | `uint8` | - |
| `OverrideQueryMobilityType` | `EOverrideQueryMobilityType` | - |
| `bUseAsPVSOC` | `uint8` | - |
| `bUseDynamicPVS` | `uint8` | - |
| `FramePredictionCacheState` | `EFPCacheState` | - |
| `StaticSceneCacheState` | `EFPCacheState` | - |
| `bRenderToTerrainVirtualTexture` | `uint8` | This primitive will be rendered to terrain VT if true |
| `bForceInjectToHierarchicalSurfel` | `uint8` | ------------------------------------Surfel GI Begin------------------------------------<br>	 If true, the primitive intersecting with the surfel volume will be injected into the volume whenever the camera moves. |
| `bForceUseStaticMovability` | `uint8` | If true, the movability of the primitive will be considered as static in Surfel GI pipeline. |
| `bAffectSurfelGIWhenHidden` | `uint8` | If true, always affect global illumination even if hidden in game |
| `bBulletCanBreakThrough` | `uint8` | 子弹碰撞穿透 |
| `bAlwaysCreatePhysicsState` | `uint8` | Indicates if we'd like to create physics state all the time (for collision and simulation).<br>	  If you set this to false, it still will create physics state if collision or simulation activated.<br>	  This can help performance if you'd like to avoid overhead of creating physics state when triggers |
| `bGenerateOverlapEvents` | `uint8` | If true, this component will generate overlap events when it is overlapping other components (eg Begin Overlap).<br>	  Both components (this and the other) must have this enabled for overlap events to occur.<br>	 <br>	  @see UpdateOverlaps(), BeginComponentOverlap(), EndComponentOverlap() |
| `bUpdateOverlapEventsWhenMove` | `uint8` | - |
| `bForceUpdateOverlapEventsWhenMove` | `uint8` | - |
| `bUseSingleSweep` | `uint8` | Use Sweep or single trace |
| `bMultiBodyOverlap` | `uint8` | If true, this component will generate individual overlaps for each overlapping physics body if it is a multi-body component. When false, this component will<br>	  generate only one overlap, regardless of how many physics bodies it has and how many of them are overlapping another componentbody. This flag has no<br>	  influence on single body components. |
| `bCheckAsyncSceneOnMove` | `uint8` | If true, this component will look for collisions on both physic scenes during movement.<br>	  Only required if the asynchronous physics scene is enabled and has geometry in it, and you wish to test for collisions with objects in that scene.<br>	  @see MoveComponent() |
| `bTraceComplexOnMove` | `uint8` | If true, component sweeps with this component should trace against complex collision during movement (for example, each triangle of a mesh).<br>	  If false, collision will be resolved against simple collision bounds instead.<br>	  @see MoveComponent() |
| `bReturnMaterialOnMove` | `uint8` | If true, component sweeps will return the material in their hit result.<br>	  @see MoveComponent(), FHitResult |
| `bUseViewOwnerDepthPriorityGroup` | `uint8` | True if the primitive should be rendered using ViewOwnerDepthPriorityGroup if viewed by its owner. |
| `bAllowCullDistanceVolume` | `uint8` | Whether to accept cull distance volumes to modify cached cull distance. |
| `bHasMotionBlurVelocityMeshes` | `uint8` | true if the primitive has motion blur velocity meshes |
| `bVisibleInReflectionCaptures` | `uint8` | If true, this component will be visible in reflection captures. |
| `bRejectReflectionCapture` | `uint8` | If true, this component won't be affected by any reflection capture. |
| `bRenderInMainPass` | `uint8` | If true, this component will be rendered in the main pass (z prepass, basepass, transparency) |
| `bForceRenderInShadowPass` | `uint8` | If true, this component will force be rendered in the shadow depth pass when bRenderInMainPass is false |
| `HiddenInMainPassLocks` | `TArray < FName >` | If Num() == 0, this component will be rendered in the main pass (z prepass, basepass, transparency) |
| `bRenderInMono` | `uint8` | If true, this component will be rendered in mono only if an HMD is connected and monoscopic far field rendering is activated. |
| `bReceivesDecals` | `uint8` | Whether the primitive receives decals. |
| `bOwnerNoSee` | `uint8` | If this is True, this component won't be visible when the view actor is the component's owner, directly or indirectly. |
| `bOnlyOwnerSee` | `uint8` | If this is True, this component will only be visible when the view actor is the component's owner, directly or indirectly. |
| `bTreatAsBackgroundForOcclusion` | `uint8` | Treat this primitive as part of the background for occlusion purposes. This can be used as an optimization to reduce the cost of rendering skyboxes, large ground planes that are part of the vista, etc. |
| `bDrawIdeaOutline` | `uint8` | Whether to render the primitive's outline |
| `bIdeaOutlineUseNormalInVertexColor` | `uint8` | Whether to use normal vector stored in vertex color |
| `bIdeaOutlineUseOutlineMesh` | `uint8` | - |
| `bIdeaOutlineNew` | `uint8` | Should only be used in UGC and Home branch for now. This may significantly increase outline cost. Be sure you need this feature before you enable it. <br>	 Whether to use new outline pass. |
| `bIdeaOutlineOcclusionHighlight` | `uint8` | Whether to use occlusion highlight |
| `bDisableWriteDepthForOcclusionHighlight` | `uint8` | Whether to occlude other primitive's highlight. if this is already occlude highlight, it won't write depth and this flag make no use. |
| `bIdeaOutlineNewUseBackFace` | `uint8` | use backface for outline drawing in outline pass |
| `bIdeaOverrideOutlineAndOcclusion` | `uint8` | Override outline settings to enable both outline and occlusion |
| `bDrawIdeaOutlineInHighlightPass` | `uint8` | Move old draw outline to highlight pass, not work for outline for separate pass, maybe custom depth outline in the future |
| `IdeaOutlineOcclusionColor` | `FLinearColor` | Edit it when enable Use Both Outline And Occlusion, otherwise use IdeaOutlineColor |
| `bOverrideIdeaOutlineColor` | `uint8` | Whether to override the primitive's outline color |
| `bOverrideIdeaOutlineThickness` | `uint8` | Whether to override the primitive's outline color |
| `IdeaOutlineThickness` | `float` | the primitive's override outline color |
| `IdeaOutlineColor` | `FLinearColor` | the primitive's override outline color |
| `bDrawHighlight` | `uint8` | Whether to draw highlight for this primitive |
| `bHighlightCanBeOccluded` | `uint8` | Whether the highlight mesh of this primitive can be occluded |
| `bOverrideHighlightColor` | `uint8` | Whether to use HighlightColor for highlight rendering, if false, use the default color in HighlightMaterial |
| `HighlightColor` | `FLinearColor` | If bOverrideHighlightColor is true, use this color for highlight rendering |
| `DrawDyeingMode` | `EDrawDyeingMode` | Draw dyeing mode of primitive |
| `VisibleDyeingColor` | `FLinearColor` | Primitive's visible color when dyeing |
| `OccludedDyeingColor` | `FLinearColor` | Primitive's occlued color when dyeing |
| `bDrawDyeing` | `uint8` | Whether to dyeing the primitive |
| `bUseAsEarlyZ` | `uint8` | Whether to render the primitive in the early z pass for mobile platform. |
| `bRenderInTwoPass` | `uint8` | Whether to render the primitive in the early z pass for mobile platform.   <br>	 If the mesh is visibility grid's proxy  <br>	 Whether to render the primitive in two pass - only work on masked hair model |
| `bTwoPassTranslucent` | `uint8` | Whether to render translucency in two pass. |
| `bTranslucentDepthWrite` | `uint8` | Whether to write depth for translucency. |
| `bTranslucentDepthWriteInTwoPass` | `uint8` | Write depth for translucency in two pass. Add a depth-only pass before rendering the translucent object. |
| `bForceIBL` | `uint8` | (TAPD:ID869829499) for SceneProxyIBL |
| `bForceDisableIBL` | `uint8` | - |
| `bForceDynamic` | `uint8` | - |
| `ActiveScopeStatus` | `int32` | - |
| `ScopeLocalTranslation` | `FVector` | - |
| `ScopeLocalRotation` | `FRotator` | - |
| `ScopeRadius` | `float` | - |
| `bIsFppLayer` | `uint8` | - |
| `bIsTppLayer` | `uint8` | When enabled, the component will NOT cast a shadow on components with bIsFppLayer enabled.<br>	  This requires bCastInsetShadow to be enabled. |
| `bUseAsOccluder` | `uint8` | Whether to render the primitive in the depth only pass.<br>	  This should generally be true for all objects, and let the renderer make decisions about whether to render objects in the depth only pass.<br>	  @todo - if any rendering features rely on a complete depth only pass, this variable needs to go away. |
| `bOnlyAsOccluder` | `uint8` | - |
| `bSelectable` | `uint8` | If this is True, this component can be selected in the editor. |
| `bForceMipStreaming` | `uint8` | If true, forces mips for textures used by this component to be resident when this component's level is loaded. |
| `bHasPerInstanceHitProxies` | `uint8` | If true a hit-proxy will be generated for each instance of instanced static meshes |
| `bRecieveShadow` | `uint8` | Controls whether the primitive component should recieve a shadow or not.(by jinglei) |
| `CastShadow` | `uint8` | Controls whether the primitive component should cast a shadow or not.<br>	 <br>	  This flag is ignored (no shadows will be generated) if all materials on this component have an Unlit shading model. |
| `bAffectDynamicIndirectLighting` | `uint8` | Controls whether the primitive should inject light into the Light Propagation Volume.  This flag is only used if CastShadow is true. |
| `bAffectDistanceFieldLighting` | `uint8` | Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. |
| `bCastDynamicShadow` | `uint8` | Controls whether the primitive should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. |
| `bCastStaticShadow` | `uint8` | Whether the object should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true. |
| `bCastVolumetricTranslucentShadow` | `uint8` | Whether the object should cast a volumetric translucent shadow.<br>	  Volumetric translucent shadows are useful for primitives `with smoothly changing opacity like particles representing a volume,<br>	  But have artifacts when used on highly opaque surfaces. |
| `bSelfShadowOnly` | `uint8` | When enabled, the component will only cast a shadow on itself and not other components in the world.<br>	  This is especially useful for first person weapons, and forces bCastInsetShadow to be enabled. |
| `bCastFarShadow` | `uint8` | When enabled, the component will be rendering into the far shadow cascades (only for directional lights). |
| `bCastInDoorShadow` | `uint8` | When enabled, the component will be rendering shadow in door (only for directional lights). |
| `bCastInsetShadow` | `uint8` | Whether this component should create a per-object shadow that gives higher effective shadow resolution.<br>	  Useful for cinematic character shadowing. Assumed to be enabled if bSelfShadowOnly is enabled. |
| `bCastTranslucentShadowAsMask` | `uint8` | - |
| `bCastPhotonShadow` | `uint8` | #if WITH_PHOTON_SHADOW |
| `bCastPhotonPerObjectShadow` | `uint8` | #if WITH_PHOTON_PER_OBEJCT_SHADOW |
| `bNearCascade` | `uint8` | - |
| `bCastCinematicShadow` | `uint8` | Whether this component should cast shadows from lights that have bCastShadowsFromCinematicObjectsOnly enabled.<br>	  This is useful for characters in a cinematic with special cinematic lights, where the cost of shadowmap rendering of the environment is undesired. |
| `bCastHiddenShadow` | `uint8` | If true, the primitive will cast shadows even if bHidden is true.<br>	 	Controls whether the primitive should cast shadows when hidden.<br>	 	This flag is only used if CastShadow is true. |
| `bCastShadowAsTwoSided` | `uint8` | Whether this primitive should cast dynamic shadows as if it were a two sided material. |
| `bLightAsIfStatic_DEPRECATED` | `uint8` | - |
| `bLightAttachmentsAsGroup` | `uint8` | Whether to light this component and any attachments as a group.  This only has effect on the root component of an attachment tree.<br>	  When enabled, attached component shadowing settings like bCastInsetShadow, bCastVolumetricTranslucentShadow, etc, will be ignored.<br>	  This is useful for improving performance when multiple movable components are attached together. |
| `bReceiveCombinedCSMAndStaticShadowsFromStationaryLights` | `uint8` | Mobile only:<br>	  If enabled this component can receive combined static and CSM shadows from a stationary light. (Enabling will increase shading cost.)<br>	  If disabled this component will only receive static shadows from stationary lights. |
| `bReceiveLandscapeShadows` | `uint8` | - |
| `bSingleSampleShadowFromStationaryLights` | `uint8` | Whether the whole component should be shadowed as one from stationary lights, which makes shadow receiving much cheaper.<br>	  When enabled shadowing data comes from the volume lighting samples precomputed by Lightmass, which are very sparse.<br>	  This is currently only used on stationary directional lights. |
| `bIgnoreRadialImpulse` | `uint8` | Will ignore radial impulses applied to this component. |
| `bIgnoreRadialForce` | `uint8` | Will ignore radial forces applied to this component. |
| `bApplyImpulseOnDamage` | `uint8` | True for damage to this component to apply physics impulse, false to opt out of these impulses. |
| `bReplicatePhysicsToAutonomousProxy` | `uint8` | True if physics should be replicated to autonomous proxies. This should be true for<br>		server-authoritative simulations, and false for client authoritative simulations. |
| `bCorrectPXTrans` | `uint8` | - |
| `bCorrectPXTransUsingRemovePhysTargetFunction` | `uint8` | - |
| `AlwaysLoadOnClient` | `uint8` | If this is True, this component must always be loaded on clients, even if Hidden and CollisionEnabled is NoCollision. |
| `AlwaysLoadOnServer` | `uint8` | If this is True, this component must always be loaded on servers, even if Hidden and CollisionEnabled is NoCollision |
| `bUseEditorCompositing` | `uint8` | Composite the drawing of this component onto the scene after post processing (only applies to editor drawing) |
| `bRenderCustomDepth` | `uint8` | If true, this component will be rendered in the CustomDepth pass (usually used for outlines) |
| `bUpdateTransformUseTeleportPhysics` | `uint8` | - |
| `bUseAsyncCompilePSO` | `uint8` | #if WITH_ANDROID_ASYNC_COMPILE_PSO<br>	 whether this mesh is using async compile pso , only used for android |
| `bIgnoreOtherCanBeOverlap` | `uint8` | - |
| `bMoveMultiPenetratingIgnoreFlag` | `uint8` | 是否在移动的时候，有多个渗透，就忽略开启本标志的物体 |
| `bHasCustomNavigableGeometry` | `TEnumAsByte < EHasCustomNavigableGeometry :: Type >` | If true then DoCustomNavigableGeometryExport will be called to collect navigable geometry of this component. |
| `CanCharacterStepUpOn` | `TEnumAsByte < enum ECanBeCharacterBase >` | Determine whether a Character can step up onto this component.<br>	  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.<br>	  @see FWalkableSlopeOverride |
| `JumpOffVelocityFactor` | `float` | 不能站的时候，角色随机移动的最大速度的比率<br>	 如果>0，表示使用本值，移动组件上的值无效；否则使用移动组件上的值 |
| `LightingChannels` | `FLightingChannels` | Channels that this component should be in.  Lights with matching channels will affect the component.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| `IndoorOutdoorMask` | `TEnumAsByte < EIndoorOutdoorMask >` | - |
| `CustomDepthStencilWriteMask` | `ERendererStencilMask` | Mask used for stencil buffer writes. |
| `CustomDepthStencilValue` | `int32` | Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3) |
| `TranslucencySortPriority` | `int32` | Translucent objects with a lower sort priority draw behind objects with a higher priority.<br>	  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.<br>	 <br>	  Ignored if the object is not translucent.  The default priority is zero.<br>	  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly.<br>	  It is especially problematic on dynamic gameplay effects. |
| `TerrainRVTRenderSortPriority` | `int32` | Objects with a lower sort priority draw behind objects with a higher priority.<br>	  Objects with the same priority are rendered from back-to-front based on their bounds origin. |
| `VisibilityId` | `int32` | Used for precomputed visibility |
| `PVSHandlerID` | `int32` | Used for precomputed visibility |
| `NumInstanceVisibilityVolumes` | `int32` | Used for precomputed visibility |
| `SkyLightIntensityScale` | `float` | 天光强度缩放系数：按倍数缩放该 Primitive 接收到的天光强度。1.0 为默认原始强度，大于 1.0 增强天光，小于 1.0 减弱天光，0.0 表示不接收天光。 (ForceVolumeProbeGIWith AO不起效) |
| `MinSkyVisibility` | `float` | 最小天空可见度：限制该 Primitive 接收天光时的最小可见度下限（0~1）。用于防止角落遮蔽区域因烘焙 AO 过暗而完全看不到天光，数值越大底部越亮。 |
| `FakeSkyLightAOIntensity` | `float` | 伪天光 AO 强度：按单个 Primitive 控制 FakeSkyLightAO（伪天光环境光遮蔽）的作用强度。0 表示不施加伪 AO（完全明亮），1 表示完整效果（默认），中间值按比例混合，数值越小接收越多天光。 |
| `bAffectSkyOcclusion` | `uint8` | Whether this primitive affects sky occlusion during Lightmass baking. If false, rays will pass through this mesh for sky occlusionvisibility. |
| `bForceSyncPSO` | `uint32` | #if ALLOW_FORCE_SYNC_CREATE_PSO<br>	  Force this material to link PSO synchronously (on iOS).<br>	  It avoids popping when the material is not suitable for async linking but may introduce stutters.<br>	  remove for IG |
| `OverrideCylinderMaxDrawHeight` | `float` | Used if [r.CylinderMaxDrawHeight] is not zero, override [r.CylinderMaxDrawHeight] global setting |
| `bCanSeparateParticleRendering` | `bool` | - |
| `bDisableDynamicInstancing` | `bool` | - |
| `BoundsScale` | `float` | Scales the bounds of the object.<br>	  This is useful when using World Position Offset to animate the vertices of the object outside of its bounds.<br>	  Warning: Increasing the bounds of an object will reduce performance and shadow quality!<br>	  Currently only used by StaticMeshComponent and SkeletalMeshComponent. |
| `OCBoundsScale` | `float` | - |
| `OCBoundsExtent` | `int32` | ROC Extent the bounds a few pixels during depth test. |
| `LastSubmitTime` | `float` | Last time the component was submitted for rendering (called FScene::AddPrimitive). |
| `LastRenderTime` | `float` | The value of WorldSettings->TimeSeconds for the frame when this component was last rendered.  This is written<br>	  from the render thread, which is up to a frame behind the game thread, so you should allow this time to<br>	  be at least a frame behind the game thread's world time before you consider the actor non-visible. |
| `LastRenderTimeOnScreen` | `float` | - |
| `TouchAsBlockActors` | `TArray < AActor * >` | - |
| `MoveIgnoreComponents` | `TArray < UPrimitiveComponent * >` | Set of components to ignore during component sweeps in MoveComponent().<br>	 These components will be ignored when this component moves or updates overlaps.<br>	 The other components may also need to be told to do the same when they move.<br>	 Does not affect movement of this component when simulating physics.<br>	 @see IgnoreComponentWhenMoving() |
| `BodyInstance` | `FBodyInstance` | Physics scene information for this component, holds a single rigid body with multiple shapes. |
| `LODParentPrimitive` | `UPrimitiveComponent *` | LOD parent primitive to draw instead of this one (multiple UPrim's will point to the same LODParent ) |
| `PostPhysicsComponentTick` | `FPrimitiveComponentPostPhysicsTickFunction` | Tick function for physics ticking |
| `IndirectLightingCacheQuality` | `TEnumAsByte < EIndirectLightingCacheQuality >` | Quality of indirect lighting for Movable primitives.  This has a large effect on Indirect Lighting Cache update time. |
| `bGenerateSurfaceSample` | `uint8` | - |
| `bOccludeLightingRay` | `uint8` | - |
| `bEnableAutoLODGeneration` | `uint8` | If true, and if World setting has bEnableHierarchicalLOD equal to true, then this component will be included when generating a Proxy mesh for the parent Actor |
| `bUseMaxLODAsImposter` | `uint8` | Use the Maximum LOD Mesh (imposter) instead of including Mesh data from this component in the Proxy Generation process |
| `ExcludeForSpecificHLODLevels` | `TArray < int32 >` | Which specific HLOD levels this component should be excluded from |
| `bIsVisibilityGridProxy` | `uint8` | Whether to render the primitive in the early z pass for mobile platform.   <br>	 If the mesh is visibility grid's proxy |
| `CanBeCharacterBase_DEPRECATED` | `TEnumAsByte < enum ECanBeCharacterBase >` | - |
| `LpvBiasMultiplier` | `float` | Multiplier used to scale the Light Propagation Volume light injection bias, to reduce light bleeding.<br>	  Set to 0 for no bias, 1 for default or higher for increased biasing (e.g. for<br>	  thin geometry such as walls) |
| `bCoastline` | `uint8` | if true, primitive will be collected as coastline |

## Functions

### `SetLightingChannels`

```text
SetLightingChannels(bChannel0Open: bool, bChannel1Open: bool, bChannel2Open: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bChannel0Open` | `bool` | - |
| `bChannel1Open` | `bool` | - |
| `bChannel2Open` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IgnoreActorWhenMoving`

```text
IgnoreActorWhenMoving(Actor: AActor *, bShouldIgnore: bool) -> void
```

Tells this component whether to ignore collision with all components of a specific Actor when this component is moved.
	  Components on the other Actor may also need to be told to do the same when they move.
	  Does not affect movement of this component when simulating physics.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `bShouldIgnore` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyArrayOfMoveIgnoreActors`

```text
CopyArrayOfMoveIgnoreActors() -> TArray < AActor * >
```

Returns the list of actors we currently ignore when moving.

**Returns**

| Type | Description |
|---|---|
| `TArray < AActor * >` | - |

### `ClearMoveIgnoreActors`

```text
ClearMoveIgnoreActors() -> void
```

Clear the list of actors we ignore when moving.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IgnoreComponentWhenMoving`

```text
IgnoreComponentWhenMoving(Component: UPrimitiveComponent *, bShouldIgnore: bool) -> void
```

Tells this component whether to ignore collision with another component when this component is moved.
	 The other components may also need to be told to do the same when they move.
	 Does not affect movement of this component when simulating physics.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | - |
| `bShouldIgnore` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyArrayOfMoveIgnoreComponents`

```text
CopyArrayOfMoveIgnoreComponents() -> TArray < UPrimitiveComponent * >
```

Returns the list of actors we currently ignore when moving.

**Returns**

| Type | Description |
|---|---|
| `TArray < UPrimitiveComponent * >` | - |

### `ClearMoveIgnoreComponents`

```text
ClearMoveIgnoreComponents() -> void
```

Clear the list of components we ignore when moving.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsOverlappingComponent`

```text
IsOverlappingComponent(OtherComp: UPrimitiveComponent *) -> bool
```

Check whether this component is overlapping another component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OtherComp` | `UPrimitiveComponent *` | Component to test this component against. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether this component is overlapping another component. |

### `IsOverlappingActor`

```text
IsOverlappingActor(Other: AActor *) -> bool
```

Check whether this component is overlapping any component of the given Actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Other` | `AActor *` | Actor to test this component against. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether this component is overlapping any component of the given Actor. |

### `GetOverlappingActors`

```text
GetOverlappingActors(OverlappingActors: TArray < AActor * > &, ClassFilter: TSubclassOf < AActor >) -> void
```

Returns a list of actors that this component is overlapping.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappingActors` | `TArray < AActor * > &` | [out] Returned list of overlapping actors |
| `ClassFilter` | `TSubclassOf < AActor >` | [optional] If set, only returns actors of this class or subclasses |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOverlappingComponents`

```text
GetOverlappingComponents(InOverlappingComponents: TArray < UPrimitiveComponent * > &) -> void
```

Returns list of components this component is overlapping.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOverlappingComponents` | `TArray < UPrimitiveComponent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoundsScale`

```text
SetBoundsScale(NewBoundsScale: float) -> void
```

Scale the bounds of this object, used for frustum culling. Useful for features like WorldPositionOffset.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBoundsScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoundsScale`

```text
GetBoundsScale() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetMaterial`

```text
GetMaterial(ElementIndex: int32) -> UMaterialInterface *
```

Returns the material used by the element at the specified index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - The element to access the material of. |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | the material used by the indexed element of this mesh. |

### `SetMaterial`

```text
SetMaterial(ElementIndex: int32, Material: UMaterialInterface *) -> void
```

Changes the material applied to an element of the mesh.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - The element to access the material of. |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | the material used by the indexed element of this mesh. |

### `SetMaterialByName`

```text
SetMaterialByName(MaterialSlotName: FName, Material: UMaterialInterface *) -> void
```

Changes the material applied to an element of the mesh.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialSlotName` | `FName` | - The slot name to access the material of. |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | the material used by the indexed element of this mesh. |

### `CreateAndSetMaterialInstanceDynamic`

```text
CreateAndSetMaterialInstanceDynamic(ElementIndex: int32) -> UMaterialInstanceDynamic *
```

Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `CreateAndSetMaterialInstanceDynamicFromMaterial`

```text
CreateAndSetMaterialInstanceDynamicFromMaterial(ElementIndex: int32, Parent: UMaterialInterface *) -> UMaterialInstanceDynamic *
```

Creates a Dynamic Material Instance for the specified element index.  The parent of the instance is set to the material being replaced.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |
| `Parent` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `CreateDynamicMaterialInstance`

```text
CreateDynamicMaterialInstance(ElementIndex: int32, SourceMaterial: UMaterialInterface *) -> UMaterialInstanceDynamic *
```

Creates a Dynamic Material Instance for the specified element index, optionally from the supplied material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElementIndex` | `int32` | - The index of the skin to replace the material for. If invalid, the material is unchanged and NULL is returned. |
| `SourceMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `GetMaterialFromCollisionFaceIndex`

```text
GetMaterialFromCollisionFaceIndex(FaceIndex: int32, SectionIndex: int32 &) -> UMaterialInterface *
```

Try and retrieve the material applied to a particular collision face of mesh. Used with face index returned from collision trace.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FaceIndex` | `int32` | Face index from hit result that was hit by a trace |
| `SectionIndex` | `int32 &` | Section of the mesh that the face belongs to |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | Material applied to section that the hit face belongs to |

### `GetWalkableSlopeOverride`

```text
GetWalkableSlopeOverride() -> const struct FWalkableSlopeOverride &
```

Returns the slope override struct for this component.

**Returns**

| Type | Description |
|---|---|
| `const struct FWalkableSlopeOverride &` | - |

### `SetWalkableSlopeOverride`

```text
SetWalkableSlopeOverride(NewOverride: FWalkableSlopeOverride &) -> void
```

Sets a new slope override for this component instance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOverride` | `FWalkableSlopeOverride &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSimulatePhysics`

```text
SetSimulatePhysics(bSimulate: bool) -> void
```

Sets whether or not a single body should use physics simulation, or should be 'fixed' (kinematic).
	 	Note that if this component is currently attached to something, beginning simulation will detach it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSimulate` | `bool` | New simulation state for single body |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLockedAxis`

```text
SetLockedAxis(LockedAxis: EDOFMode :: Type) -> void
```

Sets the constraint mode of the component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LockedAxis` | `EDOFMode :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintMode`

```text
SetConstraintMode(ConstraintMode: EDOFMode :: Type) -> void
```

Sets the constraint mode of the component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintMode` | `EDOFMode :: Type` | The type of constraint to use. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddImpulse`

```text
AddImpulse(Impulse: FVector, BoneName: FName, bVelChange: bool) -> void
```

Add an impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | Magnitude and direction of impulse to apply. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body. |
| `bVelChange` | `bool` | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddAngularImpulse`

```text
AddAngularImpulse(Impulse: FVector, BoneName: FName, bVelChange: bool) -> void
```

Add an angular impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | - |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |
| `bVelChange` | `bool` | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddAngularImpulseInRadians`

```text
AddAngularImpulseInRadians(Impulse: FVector, BoneName: FName, bVelChange: bool) -> void
```

Add an angular impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | - |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |
| `bVelChange` | `bool` | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddAngularImpulseInDegrees`

```text
AddAngularImpulseInDegrees(Impulse: FVector, BoneName: FName, bVelChange: bool) -> void
```

Add an angular impulse to a single rigid body. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | - |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply angular impulse to. 'None' indicates root body. |
| `bVelChange` | `bool` | If true, the Strength is taken as a change in angular velocity instead of an impulse (ie. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddImpulseAtLocation`

```text
AddImpulseAtLocation(Impulse: FVector, Location: FVector, BoneName: FName) -> void
```

Add an impulse to a single rigid body at a specific location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | Magnitude and direction of impulse to apply. |
| `Location` | `FVector` | Point in world space to apply impulse at. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of bone to apply impulse to. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddRadialImpulse`

```text
AddRadialImpulse(Origin: FVector, Radius: float, Strength: float, Falloff: ERadialImpulseFalloff, bVelChange: bool) -> void
```

Add an impulse to all rigid bodies in this component, radiating out from the specified position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector` | Point of origin for the radial impulse blast, in world space |
| `Radius` | `float` | Size of radial impulse. Beyond this distance from Origin, there will be no affect. |
| `Strength` | `float` | Maximum strength of impulse applied to body. |
| `Falloff` | `ERadialImpulseFalloff` | Allows you to control the strength of the impulse as a function of distance from Origin. |
| `bVelChange` | `bool` | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddForce`

```text
AddForce(Force: FVector, BoneName: FName, bAccelChange: bool) -> void
```

Add a force to a single rigid body.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Force` | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddForce_AssumesLocked`

```text
AddForce_AssumesLocked(Force: FVector, BoneName: FName, bAccelChange: bool) -> void
```

Add a force to a single rigid body.
   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.
 
 	Notice: AssumesLocked   yufeiili 未加锁版本

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Force` | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddForceAtLocation`

```text
AddForceAtLocation(Force: FVector, Location: FVector, BoneName: FName) -> void
```

Add a force to a single rigid body at a particular location in world space.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Force` | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| `Location` | `FVector` | Location to apply force, in world space. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddForceAtLocation_AssumesLocked`

```text
AddForceAtLocation_AssumesLocked(Force: FVector, Location: FVector, BoneName: FName) -> void
```

Add a force to a single rigid body at a particular location in world space.
   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.
 
 	Notice: AssumesLocked   yufeiili 未加锁版本

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Force` | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| `Location` | `FVector` | Location to apply force, in world space. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddForceAtLocationLocal`

```text
AddForceAtLocationLocal(Force: FVector, Location: FVector, BoneName: FName) -> void
```

Add a force to a single rigid body at a particular location. Both Force and Location should be in body space.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Force` | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| `Location` | `FVector` | Location to apply force, in component space. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddRadialForce`

```text
AddRadialForce(Origin: FVector, Radius: float, Strength: float, Falloff: ERadialImpulseFalloff, bAccelChange: bool) -> void
```

Add a force to all bodies in this component, originating from the supplied world-space location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector` | Origin of force in world space. |
| `Radius` | `float` | Radius within which to apply the force. |
| `Strength` | `float` | Strength of force to apply. |
| `Falloff` | `ERadialImpulseFalloff` | Allows you to control the strength of the force as a function of distance from Origin. |
| `bAccelChange` | `bool` | If true, Strength is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTorque`

```text
AddTorque(Torque: FVector, BoneName: FName, bAccelChange: bool) -> void
```

Add a torque to a single rigid body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Torque` | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTorqueInRadians`

```text
AddTorqueInRadians(Torque: FVector, BoneName: FName, bAccelChange: bool) -> void
```

Add a torque to a single rigid body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Torque` | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTorqueInRadians_AssumesLocked`

```text
AddTorqueInRadians_AssumesLocked(Torque: FVector, BoneName: FName, bAccelChange: bool) -> void
```

Add a torque to a single rigid body.
	 	assumesLocked yufeiii 未加锁版本

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Torque` | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTorqueInDegrees`

```text
AddTorqueInDegrees(Torque: FVector, BoneName: FName, bAccelChange: bool) -> void
```

Add a torque to a single rigid body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Torque` | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddTorqueInDegrees_AssumesLocked`

```text
AddTorqueInDegrees_AssumesLocked(Torque: FVector, BoneName: FName, bAccelChange: bool) -> void
```

Add a torque to a single rigid body.
	 	Notice: AssumesLocked   yufeiili 未加锁版本

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Torque` | `FVector` | Torque to apply. Direction is axis of rotation and magnitude is strength of torque. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply torque to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Torque is taken as a change in angular acceleration instead of a physical torque (i.e. mass will have no effect). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsLinearVelocity`

```text
SetPhysicsLinearVelocity(NewVel: FVector, bAddToCurrent: bool, BoneName: FName) -> void
```

Set the linear velocity of a single body.
	 	This should be used cautiously - it may be better to use AddForce or AddImpulse.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVel` | `FVector` | New linear velocity to apply to physics. |
| `bAddToCurrent` | `bool` | If true, NewVel is added to the existing velocity of the body. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to modify velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPhysicsLinearVelocity`

```text
GetPhysicsLinearVelocity(BoneName: FName) -> FVector
```

Get the linear velocity of a single body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetPhysicsLinearVelocity_AssumesLocked`

```text
GetPhysicsLinearVelocity_AssumesLocked(BoneName: FName) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetPhysicsLinearVelocityAtPoint`

```text
GetPhysicsLinearVelocityAtPoint(Point: FVector, BoneName: FName) -> FVector
```

Get the linear velocity of a point on a single body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point is specified in world space. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetAllPhysicsLinearVelocity`

```text
SetAllPhysicsLinearVelocity(NewVel: FVector, bAddToCurrent: bool) -> void
```

Set the linear velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVel` | `FVector` | New linear velocity to apply to physics. |
| `bAddToCurrent` | `bool` | If true, NewVel is added to the existing velocity of the body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsAngularVelocity`

```text
SetPhysicsAngularVelocity(NewAngVel: FVector, bAddToCurrent: bool, BoneName: FName) -> void
```

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngVel` | `FVector` | New angular velocity to apply to body, in degrees per second. |
| `bAddToCurrent` | `bool` | If true, NewAngVel is added to the existing angular velocity of the body. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsAngularVelocityInRadians`

```text
SetPhysicsAngularVelocityInRadians(NewAngVel: FVector, bAddToCurrent: bool, BoneName: FName) -> void
```

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngVel` | `FVector` | New angular velocity to apply to body, in radians per second. |
| `bAddToCurrent` | `bool` | If true, NewAngVel is added to the existing angular velocity of the body. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsAngularVelocityInDegrees`

```text
SetPhysicsAngularVelocityInDegrees(NewAngVel: FVector, bAddToCurrent: bool, BoneName: FName) -> void
```

Set the angular velocity of a single body.
	 	This should be used cautiously - it may be better to use AddTorque or AddImpulse.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngVel` | `FVector` | New angular velocity to apply to body, in degrees per second. |
| `bAddToCurrent` | `bool` | If true, NewAngVel is added to the existing angular velocity of the body. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to modify angular velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsMaxAngularVelocity`

```text
SetPhysicsMaxAngularVelocity(NewMaxAngVel: float, bAddToCurrent: bool, BoneName: FName) -> void
```

Set the maximum angular velocity of a single body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMaxAngVel` | `float` | New maximum angular velocity to apply to body, in degrees per second. |
| `bAddToCurrent` | `bool` | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsMaxAngularVelocityInDegrees`

```text
SetPhysicsMaxAngularVelocityInDegrees(NewMaxAngVel: float, bAddToCurrent: bool, BoneName: FName) -> void
```

Set the maximum angular velocity of a single body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMaxAngVel` | `float` | New maximum angular velocity to apply to body, in degrees per second. |
| `bAddToCurrent` | `bool` | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsMaxAngularVelocityInRadians`

```text
SetPhysicsMaxAngularVelocityInRadians(NewMaxAngVel: float, bAddToCurrent: bool, BoneName: FName) -> void
```

Set the maximum angular velocity of a single body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMaxAngVel` | `float` | New maximum angular velocity to apply to body, in radians per second. |
| `bAddToCurrent` | `bool` | If true, NewMaxAngVel is added to the existing maximum angular velocity of the body. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to modify maximum angular velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPhysicsAngularVelocity`

```text
GetPhysicsAngularVelocity(BoneName: FName) -> FVector
```

Get the angular velocity of a single body, in degrees per second.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetPhysicsAngularVelocity_AssumesLocked`

```text
GetPhysicsAngularVelocity_AssumesLocked(BoneName: FName) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetPhysicsAngularVelocityInDegrees`

```text
GetPhysicsAngularVelocityInDegrees(BoneName: FName) -> FVector
```

Get the angular velocity of a single body, in degrees per second.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetPhysicsAngularVelocityInDegrees_AssumesLocked`

```text
GetPhysicsAngularVelocityInDegrees_AssumesLocked(BoneName: FName) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetPhysicsAngularVelocityInRadians`

```text
GetPhysicsAngularVelocityInRadians(BoneName: FName) -> FVector
```

Get the angular velocity of a single body, in radians per second.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to get velocity of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetPhysicsAngularVelocityInRadians_AssumesLocked`

```text
GetPhysicsAngularVelocityInRadians_AssumesLocked(BoneName: FName) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetCenterOfMass`

```text
GetCenterOfMass(BoneName: FName) -> FVector
```

Get the center of mass of a single body. In the case of a welded body this will return the center of mass of the entire welded body (including its parent and children)
	   Objects that are not simulated return (0,0,0) as they do not have COM

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to get center of mass of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetCenterOfMass`

```text
SetCenterOfMass(CenterOfMassOffset: FVector, BoneName: FName) -> void
```

Set the center of mass of a single body. This will offset the physx-calculated center of mass.
		Note that in the case where multiple bodies are attached together, the center of mass will be set for the entire group.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CenterOfMassOffset` | `FVector` | User specified offset for the center of mass of this object, from the calculated location. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `WakeRigidBody`

```text
WakeRigidBody(BoneName: FName) -> void
```

'Wake' physics simulation for a single body.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to wake. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PutRigidBodyToSleep`

```text
PutRigidBodyToSleep(BoneName: FName) -> void
```

Force a single body back to sleep.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to put to sleep. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNotifyRigidBodyCollision`

```text
SetNotifyRigidBodyCollision(bNewNotifyRigidBodyCollision: bool) -> void
```

Changes the value of bNotifyRigidBodyCollision

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewNotifyRigidBodyCollision` | `bool` | - The value to assign to bNotifyRigidBodyCollision |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOwnerNoSee`

```text
SetOwnerNoSee(bNewOwnerNoSee: bool) -> void
```

Changes the value of bOwnerNoSee.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewOwnerNoSee` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOnlyOwnerSee`

```text
SetOnlyOwnerSee(bNewOnlyOwnerSee: bool) -> void
```

Changes the value of bOnlyOwnerSee.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewOnlyOwnerSee` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDrawIdeaOutline`

```text
SetDrawIdeaOutline(bNewDrawOutline: bool) -> void
```

Changes the value of DrawOutline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewDrawOutline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutlineUseNormalInVertexColor`

```text
SetIdeaOutlineUseNormalInVertexColor(bNewUseNormalInVertexColor: bool) -> void
```

Changes whether use the new outline method which uses normal vectors in vertex colors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewUseNormalInVertexColor` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutlineNew`

```text
SetIdeaOutlineNew(bNew: bool) -> void
```

Should only be used in  and Home branch for now. This may significantly increase outline cost. Be sure you need this feature before you enable it. 
	 Changes whether use the new outline pass.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNew` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutlineUseOutlineMesh`

```text
SetIdeaOutlineUseOutlineMesh(bUseOutlineMesh: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUseOutlineMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutlineOcclusionHighlight`

```text
SetIdeaOutlineOcclusionHighlight(bOcclusionHighlight: bool) -> void
```

Changes whether use the occlusion highlight

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bOcclusionHighlight` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDisableWriteDepthForOcclusionHighlight`

```text
SetDisableWriteDepthForOcclusionHighlight(bDisable: bool) -> void
```

Changes whether to occlude other primitives' highlight. if this is already occlude highlight, it won't write depth and this flag make no use.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDisable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOverrideOutlineAndOcclusion`

```text
SetIdeaOverrideOutlineAndOcclusion(bOutlineAndOcclusion: bool) -> void
```

Override outline settings to enable both outline and occlusion

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bOutlineAndOcclusion` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDrawIdeaOutlineInHighlightPass`

```text
SetDrawIdeaOutlineInHighlightPass(bHighlight: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bHighlight` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutlineNewUseBackFace`

```text
SetIdeaOutlineNewUseBackFace(bUseBackFace: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUseBackFace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OverrideIdeaOutlineColor`

```text
OverrideIdeaOutlineColor(bOverride: bool, InOutlineColor: FLinearColor &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bOverride` | `bool` | - |
| `InOutlineColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OverrideIdeaOutlineThickness`

```text
OverrideIdeaOutlineThickness(bOverride: bool, InThickness: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bOverride` | `bool` | - |
| `InThickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutlineOcclusionColor`

```text
SetIdeaOutlineOcclusionColor(InOcclusionColor: FLinearColor &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOcclusionColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutline_UGC`

```text
SetIdeaOutline_UGC(bDrawOutline: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDrawOutline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIdeaOutlineOcclusionHighlight_UGC`

```text
SetIdeaOutlineOcclusionHighlight_UGC(bOcclusionHighlight: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bOcclusionHighlight` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOutlineMesh`

```text
SetOutlineMesh(StaticMesh: UStaticMesh *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StaticMesh` | `UStaticMesh *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDrawHighlight`

```text
SetDrawHighlight(bNewDrawHighlight: bool) -> void
```

Turn onoff the highlight rendering for this primitive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewDrawHighlight` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHighlightCanBeOccluded`

```text
SetHighlightCanBeOccluded(bInCanBeOccluded: bool) -> void
```

Changes whether the highlight mesh of this primitive can be occluded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInCanBeOccluded` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OverrideHighlightColor`

```text
OverrideHighlightColor(bOverride: bool, InHighlightColor: FLinearColor) -> void
```

Override the highlight color for this primitive

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bOverride` | `bool` | - If true, override the highlight color using InHighlightColor. If false, use the default color in HighlightMaterial. |
| `InHighlightColor` | `FLinearColor` | - New color used for highlight rendering |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDrawDyeing`

```text
SetDrawDyeing(bNewDrawOutline: bool) -> void
```

Changes the value of DrawDyeing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewDrawOutline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDrawDyeingMode`

```text
SetDrawDyeingMode(InDrawDyeingMode: EDrawDyeingMode) -> void
```

Changes the value of DrawDyeingMode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDrawDyeingMode` | `EDrawDyeingMode` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVisibleDyeingColor`

```text
SetVisibleDyeingColor(InColor: FLinearColor &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOccludedDyeingColor`

```text
SetOccludedDyeingColor(InColor: FLinearColor &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReveiceShadow`

```text
SetReveiceShadow(NewReveiceShadow: bool) -> void
```

Changes the value of bReveiceShadow.(by jinglei)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewReveiceShadow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastShadow`

```text
SetCastShadow(NewCastShadow: bool) -> void
```

Changes the value of CastShadow.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCastShadow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastInsetShadow`

```text
SetCastInsetShadow(bInCastInsetShadow: bool) -> void
```

Changes the value of CastInsetShadow.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInCastInsetShadow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightAttachmentsAsGroup`

```text
SetLightAttachmentsAsGroup(bInLightAttachmentsAsGroup: bool) -> void
```

Changes the value of LightAttachmentsAsGroup.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInLightAttachmentsAsGroup` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastPhotonShadow`

```text
SetCastPhotonShadow(bNewCastPhotonShadow: bool) -> void
```

WITH_PHOTON_SHADOW 
	 Set cast photon shadow.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewCastPhotonShadow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSingleSampleShadowFromStationaryLights`

```text
SetSingleSampleShadowFromStationaryLights(bNewSingleSampleShadowFromStationaryLights: bool) -> void
```

Changes the value of bSingleSampleShadowFromStationaryLights.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewSingleSampleShadowFromStationaryLights` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTranslucentSortPriority`

```text
SetTranslucentSortPriority(NewTranslucentSortPriority: int32) -> void
```

Changes the value of TranslucentSortPriority.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTranslucentSortPriority` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReceivesDecals`

```text
SetReceivesDecals(bNewReceivesDecals: bool) -> void
```

Changes the value of bReceivesDecals.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewReceivesDecals` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCollisionEnabled`

```text
SetCollisionEnabled(NewType: ECollisionEnabled :: Type) -> void
```

Controls what kind of collision is enabled for this body

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewType` | `ECollisionEnabled :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCollisionProfileName`

```text
SetCollisionProfileName(InCollisionProfileName: FName) -> void
```

Set Collision Profile Name
	  This function is called by constructors when they set ProfileName
	  This will change current CollisionProfileName to be this, and overwrite Collision Setting

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCollisionProfileName` | `FName` | : New Profile Name |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCollisionProfileName`

```text
GetCollisionProfileName() -> FName
```

Get the collision profile name

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `SetCollisionObjectType`

```text
SetCollisionObjectType(Channel: ECollisionChannel) -> void
```

Changes the collision channel that this object uses when it moves

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Channel` | `ECollisionChannel` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_LineTraceComponent`

```text
K2_LineTraceComponent(TraceStart: FVector, TraceEnd: FVector, bTraceComplex: bool, bShowTrace: bool, HitLocation: FVector &, HitNormal: FVector &, BoneName: FName &, OutHit: FHitResult &) -> bool
```

Perform a line trace against a single component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TraceStart` | `FVector` | - |
| `TraceEnd` | `FVector` | - |
| `bTraceComplex` | `bool` | - |
| `bShowTrace` | `bool` | - |
| `HitLocation` | `FVector &` | - |
| `HitNormal` | `FVector &` | - |
| `BoneName` | `FName &` | - |
| `OutHit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetRenderCustomDepth`

```text
SetRenderCustomDepth(bValue: bool) -> void
```

Sets the bRenderCustomDepth property and marks the render state dirty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomDepthStencilValue`

```text
SetCustomDepthStencilValue(Value: int32) -> void
```

Sets the CustomDepth stencil value (0 - 255) and marks the render state dirty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomDepthStencilWriteMask`

```text
SetCustomDepthStencilWriteMask(WriteMaskBit: ERendererStencilMask) -> void
```

Sets the CustomDepth stencil write mask and marks the render state dirty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WriteMaskBit` | `ERendererStencilMask` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderInMainPass`

```text
SetRenderInMainPass(bValue: bool, LockKey: FName) -> void
```

Sets bRenderInMainPass property and marks the render state dirty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bValue` | `bool` | - |
| `LockKey` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsRenderInMainPass`

```text
IsRenderInMainPass() -> bool
```

Sets bRenderInMainPass property and marks the render state dirty.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetRenderInMono`

```text
SetRenderInMono(bValue: bool) -> void
```

Sets bRenderInMono property and marks the render state dirty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForceIBL`

```text
SetForceIBL(InForceIBL: bool) -> void
```

set bForceIBL

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForceIBL` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForceDisableIBL`

```text
SetForceDisableIBL(InForceDisableIBL: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForceDisableIBL` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsForceDynamic`

```text
IsForceDynamic() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetForceDynamic`

```text
SetForceDynamic(InForceDynamic: bool) -> void
```

set bForceDynamic

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForceDynamic` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActiveScope`

```text
IsActiveScope() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetActiveScope`

```text
SetActiveScope(InIsActiveScope: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsActiveScope` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScopeInfoLocal`

```text
SetScopeInfoLocal(InLocalTranslation: FVector, InLocalRotation: FRotator, InScopeRadius: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLocalTranslation` | `FVector` | - |
| `InLocalRotation` | `FRotator` | - |
| `InScopeRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFppLayer`

```text
SetFppLayer(InIsFppLayer: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsFppLayer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTppLayer`

```text
SetTppLayer(InIsTppLayer: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsTppLayer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTwoPassTranslucent`

```text
SetTwoPassTranslucent(bNewTwoPassTranslucent: bool) -> void
```

Changes the value of Two Pass Translucent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewTwoPassTranslucent` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTranslucentDepthWrite`

```text
SetTranslucentDepthWrite(bNewTranslucentDepthWrite: bool) -> void
```

Changes the value of Translucent Depth Write.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewTranslucentDepthWrite` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTranslucentDepthWriteInTwoPass`

```text
SetTranslucentDepthWriteInTwoPass(bNewTranslucentDepthWriteInTwoPass: bool) -> void
```

Changes the value of Translucent Depth Write In Two Pass.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewTranslucentDepthWriteInTwoPass` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumMaterials`

```text
GetNumMaterials() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | number of material elements in this primitive |

### `GetClosestPointOnCollision`

```text
GetClosestPointOnCollision(Point: FVector &, OutPointOnBody: FVector &, BoneName: FName) -> float
```

Returns the distance and closest point to the collision surface.
	 Component must have simple collision to be queried for closest point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector &` | World 3D vector |
| `OutPointOnBody` | `FVector &` | Point on the surface of collision closest to Point |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to set center of mass of. 'None' indicates root body. |

**Returns**

| Type | Description |
|---|---|
| `float` | Success if returns > 0.f, if returns 0.f, it is either not convex or inside of the point |

### `GetCollisionEnabled`

```text
GetCollisionEnabled() -> ECollisionEnabled :: Type
```

Returns the form of collision for this component

**Returns**

| Type | Description |
|---|---|
| `ECollisionEnabled :: Type` | - |

### `K2_IsCollisionEnabled`

```text
K2_IsCollisionEnabled() -> bool
```

Utility to see if there is any form of collision (query or physics) enabled on this component.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_IsQueryCollisionEnabled`

```text
K2_IsQueryCollisionEnabled() -> bool
```

Utility to see if there is any query collision enabled on this component.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_IsPhysicsCollisionEnabled`

```text
K2_IsPhysicsCollisionEnabled() -> bool
```

Utility to see if there is any physics collision enabled on this component.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCollisionResponseToChannel`

```text
GetCollisionResponseToChannel(Channel: ECollisionChannel) -> ECollisionResponse
```

Gets the response type given a specific channel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Channel` | `ECollisionChannel` | - |

**Returns**

| Type | Description |
|---|---|
| `ECollisionResponse` | - |

### `GetCollisionObjectType`

```text
GetCollisionObjectType() -> ECollisionChannel
```

Gets the collision object type

**Returns**

| Type | Description |
|---|---|
| `ECollisionChannel` | - |

### `SetAllPhysicsAngularVelocity`

```text
SetAllPhysicsAngularVelocity(NewAngVel: FVector &, bAddToCurrent: bool) -> void
```

Set the angular velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngVel` | `FVector &` | New angular velocity to apply to physics, in degrees per second. |
| `bAddToCurrent` | `bool` | If true, NewAngVel is added to the existing angular velocity of all bodies. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllPhysicsAngularVelocityInDegrees`

```text
SetAllPhysicsAngularVelocityInDegrees(NewAngVel: FVector &, bAddToCurrent: bool) -> void
```

Set the angular velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngVel` | `FVector &` | New angular velocity to apply to physics, in degrees per second. |
| `bAddToCurrent` | `bool` | If true, NewAngVel is added to the existing angular velocity of all bodies. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllPhysicsAngularVelocityInRadians`

```text
SetAllPhysicsAngularVelocityInRadians(NewAngVel: FVector &, bAddToCurrent: bool) -> void
```

Set the angular velocity of all bodies in this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAngVel` | `FVector &` | New angular velocity to apply to physics, in radians per second. |
| `bAddToCurrent` | `bool` | If true, NewAngVel is added to the existing angular velocity of all bodies. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `WakeAllRigidBodies`

```text
WakeAllRigidBodies() -> void
```

Ensure simulation is running for all bodies in this component.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableGravity`

```text
SetEnableGravity(bGravityEnabled: bool) -> void
```

Enablesdisables whether this component is affected by gravity. This applies only to components with bSimulatePhysics set to true.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bGravityEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsGravityEnabled`

```text
IsGravityEnabled() -> bool
```

Returns whether this component is affected by gravity. Returns always false if the component is not simulated.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetLinearDamping`

```text
SetLinearDamping(InDamping: float) -> void
```

Sets the linear damping of this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDamping` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLinearDamping`

```text
GetLinearDamping() -> float
```

Returns the linear damping of this component.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetAngularDamping`

```text
SetAngularDamping(InDamping: float) -> void
```

Sets the angular damping of this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDamping` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAngularDamping`

```text
GetAngularDamping() -> float
```

Returns the angular damping of this component.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMassScale`

```text
SetMassScale(BoneName: FName, InMassScale: float) -> void
```

Change the mass scale used to calculate the mass of a single physics body

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `InMassScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMassScale`

```text
GetMassScale(BoneName: FName) -> float
```

Returns the mass scale used to calculate the mass of a single physics body

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetAllMassScale`

```text
SetAllMassScale(InMassScale: float) -> void
```

Change the mass scale used fo all bodies in this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMassScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMassOverrideInKg`

```text
SetMassOverrideInKg(BoneName: FName, MassInKg: float, bOverrideMass: bool) -> void
```

Override the mass (in Kg) of a single physics body.
		Note that in the case where multiple bodies are attached together, the override mass will be set for the entire group.
		Set the Override Mass to false if you want to reset the body's mass to the auto-calculated physx mass.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |
| `MassInKg` | `float` | - |
| `bOverrideMass` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMass`

```text
GetMass() -> float
```

Returns the mass of this component in kg.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetInertiaTensor`

```text
GetInertiaTensor(BoneName: FName) -> FVector
```

Returns the inertia tensor of this component in kg cm^2. The inertia tensor is in local component space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ScaleByMomentOfInertia`

```text
ScaleByMomentOfInertia(InputVector: FVector, BoneName: FName) -> FVector
```

Scales the given vector by the world space moment of inertia. Useful for computing the torque needed to rotate an object.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputVector` | `FVector` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `IsAnyRigidBodyAwake`

```text
IsAnyRigidBodyAwake() -> bool
```

Returns if any body in this component is currently awake and simulating.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetCollisionResponseToChannel`

```text
SetCollisionResponseToChannel(Channel: ECollisionChannel, NewResponse: ECollisionResponse) -> void
```

Changes a member of the ResponseToChannels container for this PrimitiveComponent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Channel` | `ECollisionChannel` | - |
| `NewResponse` | `ECollisionResponse` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCollisionResponseToAllChannels`

```text
SetCollisionResponseToAllChannels(NewResponse: ECollisionResponse) -> void
```

Changes all ResponseToChannels container for this PrimitiveComponent. to be NewResponse

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewResponse` | `ECollisionResponse` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysMaterialOverride`

```text
SetPhysMaterialOverride(NewPhysMaterial: UPhysicalMaterial *) -> void
```

Changes the current PhysMaterialOverride for this component.
	 	Note that if physics is already running on this component, this will _not_ alter its massinertia etc,
	 	it will only change its surface properties like friction.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPhysMaterial` | `UPhysicalMaterial *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPhysMaterial`

```text
GetPhysMaterial(Item: int32) -> UPhysicalMaterial *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UPhysicalMaterial *` | - |

### `SetCullDistance`

```text
SetCullDistance(NewCullDistance: float, EnableIncrease: bool) -> void
```

Changes the value of CullDistance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCullDistance` | `float` | - The value to assign to CullDistance. |
| `EnableIncrease` | `bool` | - Whether or not to increase the cull distance if it is greater than the current cull distance. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanCharacterStepUp`

```text
CanCharacterStepUp(Pawn: APawn *) -> bool
```

Return true if the given Pawn can step up onto this component.
	  This controls whether they can try to step up on it when they bump in to it, not whether they can walk on it after landing on it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pawn` | `APawn *` | the Pawn that wants to step onto this component. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsComponentRenderQualityEnough`

```text
IsComponentRenderQualityEnough() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsComponentDeviceQualityEnough`

```text
IsComponentDeviceQualityEnough() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsComponentMemoryEnough`

```text
IsComponentMemoryEnough() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsComponentDeviceEnough`

```text
IsComponentDeviceEnough() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnComponentHit`

```text
OnComponentHit(HitComponent: UPrimitiveComponent*, OtherActor: AActor*, OtherComp: UPrimitiveComponent*, NormalImpulse: FVector, Hit: const FHitResult&) -> void
```

Event called when a component hits (or is hit by) something solid. This could happen due to things like Character movement, using Set Location with 'sweep' enabled, or physics simulation.
	 	For events when objects overlap (e.g. walking into a trigger) see the 'Overlap' event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitComponent` | `UPrimitiveComponent*` | - |
| `OtherActor` | `AActor*` | - |
| `OtherComp` | `UPrimitiveComponent*` | - |
| `NormalImpulse` | `FVector` | - |
| `Hit` | `const FHitResult&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnComponentBeginOverlap`

```text
OnComponentBeginOverlap(OverlappedComponent: UPrimitiveComponent*, OtherActor: AActor*, OtherComp: UPrimitiveComponent*, OtherBodyIndex: int32, bFromSweep: bool, SweepResult: const FHitResult &) -> void
```

Event called when something starts to overlaps this component, for example a player walking into a trigger.
	 	For events when objects have a blocking collision, for example a player hitting a wall, see 'Hit' events.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappedComponent` | `UPrimitiveComponent*` | - |
| `OtherActor` | `AActor*` | - |
| `OtherComp` | `UPrimitiveComponent*` | - |
| `OtherBodyIndex` | `int32` | - |
| `bFromSweep` | `bool` | - |
| `SweepResult` | `const FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnComponentEndOverlap`

```text
OnComponentEndOverlap(OverlappedComponent: UPrimitiveComponent*, OtherActor: AActor*, OtherComp: UPrimitiveComponent*, OtherBodyIndex: int32) -> void
```

Event called when something stops overlapping this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OverlappedComponent` | `UPrimitiveComponent*` | - |
| `OtherActor` | `AActor*` | - |
| `OtherComp` | `UPrimitiveComponent*` | - |
| `OtherBodyIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnComponentWake`

```text
OnComponentWake(WakingComponent: UPrimitiveComponent*, BoneName: FName) -> void
```

Event called when the underlying physics objects is woken up

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WakingComponent` | `UPrimitiveComponent*` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnComponentSleep`

```text
OnComponentSleep(SleepingComponent: UPrimitiveComponent*, BoneName: FName) -> void
```

Event called when the underlying physics objects is put to sleep

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SleepingComponent` | `UPrimitiveComponent*` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnComponentCollisionSettingsChangedEvent`

```text
OnComponentCollisionSettingsChangedEvent(ChangedComponent: UPrimitiveComponent*) -> void
```

Event called when collision settings change for this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangedComponent` | `UPrimitiveComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBeginCursorOver`

```text
OnBeginCursorOver(TouchedComponent: UPrimitiveComponent*) -> void
```

Event called when the mouse cursor is moved over this component and mouse over events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedComponent` | `UPrimitiveComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEndCursorOver`

```text
OnEndCursorOver(TouchedComponent: UPrimitiveComponent*) -> void
```

Event called when the mouse cursor is moved off this component and mouse over events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedComponent` | `UPrimitiveComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnClicked`

```text
OnClicked(TouchedComponent: UPrimitiveComponent*, ButtonPressed: FKey) -> void
```

Event called when the left mouse button is clicked while the mouse is over this component and click events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedComponent` | `UPrimitiveComponent*` | - |
| `ButtonPressed` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReleased`

```text
OnReleased(TouchedComponent: UPrimitiveComponent*, ButtonReleased: FKey) -> void
```

Event called when the left mouse button is released while the mouse is over this component click events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TouchedComponent` | `UPrimitiveComponent*` | - |
| `ButtonReleased` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchBegin`

```text
OnInputTouchBegin(FingerIndex: ETouchIndex::Type, TouchedComponent: UPrimitiveComponent*) -> void
```

Event called when a touch input is received over this component when touch events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedComponent` | `UPrimitiveComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchEnd`

```text
OnInputTouchEnd(FingerIndex: ETouchIndex::Type, TouchedComponent: UPrimitiveComponent*) -> void
```

Event called when a touch input is released over this component when touch events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedComponent` | `UPrimitiveComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchEnter`

```text
OnInputTouchEnter(FingerIndex: ETouchIndex::Type, TouchedComponent: UPrimitiveComponent*) -> void
```

Event called when a finger is moved over this component when touch over events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedComponent` | `UPrimitiveComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInputTouchLeave`

```text
OnInputTouchLeave(FingerIndex: ETouchIndex::Type, TouchedComponent: UPrimitiveComponent*) -> void
```

Event called when a finger is moved off this component when touch over events are enabled in the player controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FingerIndex` | `ETouchIndex::Type` | - |
| `TouchedComponent` | `UPrimitiveComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProceduralFoliageComponent.json -->

# UProceduralFoliageComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FoliageSpawner` | `UProceduralFoliageSpawner *` | The procedural foliage spawner used to generate foliage instances within this volume. |
| `TileOverlap` | `float` | The amount of overlap between simulation tiles (in cm). |
| `SpawningVolume` | `AVolume *` | - |
| `ProceduralGuid` | `FGuid` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProceduralFoliageSpawner.json -->

# UProceduralFoliageSpawner

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RandomSeed` | `int32` | The seed used for generating the randomness of the simulation. |
| `TileSize` | `float` | Length of the tile (in cm) along one axis. The total area of the tile will be TileSizeTileSize. |
| `NumUniqueTiles` | `int32` | The number of unique tiles to generate. The final simulation is a procedurally determined combination of the various unique tiles. |
| `MinimumQuadTreeSize` | `float` | Minimum size of the quad tree used during the simulation. Reduce if too many instances are in splittable leaf quads (as warned in the log). |
| `FoliageTypes` | `TArray < FFoliageTypeObject >` | The types of foliage to procedurally spawn. |
| `bNeedsSimulation` | `bool` | - |

## Functions

### `Simulate`

```text
Simulate(NumSteps: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NumSteps` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProceduralFoliageTile.json -->

# UProceduralFoliageTile

Procedurally determines where to spawn foliage meshes within a discrete area.
 	Generally, a procedural foliage simulation as a whole is composed of multiple tiles.
 	Tiles are able to overlap one another as well to create a seamless appearance.
 	
 	Note that the tile is not responsible for actually spawning any instances, it only determines where they should be placed.
 	Following a simulation, call ExtractDesiredInstances for information about where each instance should spawn.
 	
 	Note also that, barring any core changes to the ordering of TSet, foliage generation is deterministic 
 	(i.e. given the same inputs, the result of the simulation will always be the same).

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FoliageSpawner` | `UProceduralFoliageSpawner *` | - |
| `InstancesArray` | `TArray < FProceduralFoliageInstance >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProgressBar.json -->

# UProgressBar

The progress bar widget is a simple bar that fills up that can be restyled to fit any number of uses.
 
   No Children

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetStyle` | `FProgressBarStyle` | The progress bar style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | Style used for the progress bar |
| `BackgroundImage_DEPRECATED` | `USlateBrushAsset *` | The brush to use as the background of the progress bar |
| `FillImage_DEPRECATED` | `USlateBrushAsset *` | The brush to use as the fill image |
| `MarqueeImage_DEPRECATED` | `USlateBrushAsset *` | The brush to use as the marquee image |
| `Percent` | `float` | Used to determine the fill position of the progress bar ranging 0..1 |
| `BarFillType` | `TEnumAsByte < EProgressBarFillType :: Type >` | Defines if this progress bar fills Left to right or right to left |
| `bIsMarquee` | `bool` | - |
| `BorderPadding` | `FVector2D` | - |
| `PercentDelegate` | `FGetFloat` | A bindable delegate to allow logic to drive the text of the widget |
| `FillColorAndOpacity` | `FLinearColor` | Fill Color and Opacity |
| `FillColorAndOpacityDelegate` | `FGetLinearColor` | - |

## Functions

### `SetPercent`

```text
SetPercent(InPercent: float) -> void
```

Sets the current value of the ProgressBar.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPercent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOppositePercent`

```text
SetOppositePercent(InPercent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPercent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFillColorAndOpacity`

```text
SetFillColorAndOpacity(InColor: FLinearColor) -> void
```

Sets the fill color of the progress bar.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsMarquee`

```text
SetIsMarquee(InbIsMarquee: bool) -> void
```

Sets the progress bar to show as a marquee.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbIsMarquee` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPercent`

```text
GetPercent() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetOppositePercent`

```text
GetOppositePercent() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Delegates

### `OnPercentChangeDelegate`

```text
OnPercentChangeDelegate(ChangedPercent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangedPercent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProgressWidgetStyle.json -->

# UProgressWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProgressBarStyle` | `FProgressBarStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProjectileActionEffectBase.json -->

# UProjectileActionEffectBase

抛体动作基类

## Inheritance

`UProjectileEffectBase`

## Events

### `ApplyActionEffect`

```text
ApplyActionEffect(TargetData: FPESkillTargetData &) -> void
```

执行动作
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetData` | `FPESkillTargetData &` | 条件触发时的数据 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitBP`

```text
InitBP(InOwnerActor: AActor *) -> void
```

动作初始化接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOwnerActor` | `AActor *` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyParamsBP`

```text
ApplyParamsBP(Params: FProjectileParams &) -> void
```

动作发射时调用的参数
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Params` | `FProjectileParams &` | 发射参数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProjectileMovementComponent.json -->

# UProjectileMovementComponent

ProjectileMovementComponent updates the position of another component during its tick.
 
  Behavior such as bouncing after impacts and homing toward a target are supported.
 
  Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
  If the updated component is simulating physics, only the initial launch parameters (when initial velocity is non-zero)
  will affect the projectile, and the physics sim will take over from there.
 
  @see UMovementComponent

## Inheritance

`UMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InitialSpeed` | `float` | Initial speed of projectile. If greater than zero, this will override the initial Velocity value and instead treat Velocity as a direction. |
| `MaxSpeed` | `float` | Limit on speed of projectile (0 means no limit). |
| `bRotationFollowsVelocity` | `uint8` | If true, this projectile will have its rotation updated each frame to match the direction of its velocity. |
| `bRotationRemainsVertical` | `uint8` | If true, this projectile will have its rotation updated each frame to maintain the rotations Yaw only. (bRotationFollowsVelocity is required to be true) |
| `bShouldBounce` | `uint8` | If true, simple bounces will be simulated. Set this to false to stop simulating on contact. |
| `bInitialVelocityInLocalSpace` | `uint8` | If true, the initial Velocity is interpreted as being in local space upon startup.<br>	  @see SetVelocityInLocalSpace() |
| `bForceSubStepping` | `uint8` | If true, forces sub-stepping to break up movement into discrete smaller steps to improve accuracy of the trajectory.<br>	  Objects that move in a straight line typically do not need to set this, as movement always uses continuous collision detection (sweeps) so collision is not missed.<br>	  Sub-stepping is automatically enabled when under the effects of gravity or when homing towards a target.<br>	  @see MaxSimulationTimeStep, MaxSimulationIterations |
| `bSimulationEnabled` | `uint8` | If true, does normal simulation ticking and update. If false, simulation is halted, but component will still tick (allowing interpolation to run). |
| `bSweepCollision` | `uint8` | If true, movement uses swept collision checks.<br>	  If false, collision effectively teleports to the destination. Note that when this is disabled, movement will never generate blocking collision hits (though overlaps will be updated). |
| `bIsHomingProjectile` | `uint8` | If true, we will accelerate toward our homing target. HomingTargetComponent must be set after the projectile is spawned.<br>	  @see HomingTargetComponent, HomingAccelerationMagnitude |
| `bBounceAngleAffectsFriction` | `uint8` | Controls the effects of friction on velocity parallel to the impact surface when bouncing.<br>	  If true, friction will be modified based on the angle of impact, making friction higher for perpendicular impacts and lower for glancing impacts.<br>	  If false, a bounce will retain a proportion of tangential velocity equal to (1.0 - Friction), acting as a "horizontal restitution". |
| `bIsSliding` | `uint8` | If true, projectile is sliding  rolling along a surface. |
| `bInterpMovement` | `uint8` | If true and there is an interpolated component set, location (and optionally rotation) interpolation is enabled which allows the interpolated object to smooth uneven updates<br>	  of the UpdatedComponent's location (usually to smooth network updates). This requires using SetInterpolatedComponent() to indicate the visual component that lags behind the collision,<br>	  and using MoveInterpolationTarget() when the new target locationrotation is received (usually on a net update).<br>	  @see SetInterpolatedComponent(), MoveInterpolationTarget() |
| `bInterpRotation` | `uint8` | If true and there is an interpolated component set, rotation interpolation is enabled which allows the interpolated object to smooth uneven updates<br>	  of the UpdatedComponent's rotation (usually to smooth network updates).<br>	  Rotation interpolation is only applied if bInterpMovement is also enabled.<br>	  @see SetInterpolatedComponent(), MoveInterpolationTarget() |
| `PreviousHitTime` | `float` | Saved HitResult Time (0 to 1) from previous simulation step. Equal to 1.0 when there was no impact. |
| `PreviousHitNormal` | `FVector` | Saved HitResult Normal from previous simulation step that resulted in an impact. If PreviousHitTime is 1.0, then the hit was not in the last step. |
| `ProjectileGravityScale` | `float` | Custom gravity scale for this projectile. Set to 0 for no gravity. |
| `Buoyancy` | `float` | Buoyancy of UpdatedComponent in fluid. 0.0=sinks as fast as in air, 1.0=neutral buoyancy |
| `Bounciness` | `float` | Percentage of velocity maintained after the bounce in the direction of the normal of impact (coefficient of restitution).<br>	  1.0 = no velocity lost, 0.0 = no bounce. Ignored if bShouldBounce is false. |
| `Friction` | `float` | Coefficient of friction, affecting the resistance to sliding along a surface.<br>	  Normal range is [0,1] : 0.0 = no friction, 1.0+ = very high friction.<br>	  Also affects the percentage of velocity maintained after the bounce in the direction tangent to the normal of impact.<br>	  Ignored if bShouldBounce is false.<br>	  @see bBounceAngleAffectsFriction |
| `BounceVelocityStopSimulatingThreshold` | `float` | If velocity is below this threshold after a bounce, stops simulating and triggers the OnProjectileStop event.<br>	  Ignored if bShouldBounce is false, in which case the projectile stops simulating on the first impact.<br>	  @see StopSimulating(), OnProjectileStop |
| `MinFrictionFraction` | `float` | When bounce angle affects friction, apply at least this fraction of normal friction.<br>	  Helps consistently slow objects sliding or rolling along surfaces or in valleys when the usual friction amount would take a very long time to settle. |
| `HomingAccelerationMagnitude` | `float` | The magnitude of our acceleration towards the homing target. Overall velocity magnitude will still be limited by MaxSpeed. |
| `HomingTargetComponent` | `TWeakObjectPtr < USceneComponent >` | The current target we are homing towards. Can only be set at runtime (when projectile is spawned or updating).<br>	  @see bIsHomingProjectile |
| `MaxSimulationTimeStep` | `float` | Max time delta for each discrete simulation step.<br>	  Lowering this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationIterations, bForceSubStepping |
| `MaxSimulationIterations` | `int32` | Max number of iterations used for each discrete simulation step.<br>	  Increasing this value can address precision issues with fast-moving objects or complex collision scenarios, at the cost of performance.<br>	 <br>	  WARNING: if (MaxSimulationTimeStep  MaxSimulationIterations) is too low for the min framerate, the last simulation step may exceed MaxSimulationTimeStep to complete the simulation.<br>	  @see MaxSimulationTimeStep, bForceSubStepping |
| `BounceAdditionalIterations` | `int32` | On the first few bounces (up to this amount), allow extra iterations over MaxSimulationIterations if necessary. |
| `InterpLocationTime` | `float` | "Time" over which most of the location interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.<br>	  Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.<br>	  A value of zero is effectively instantaneous interpolation. |
| `InterpRotationTime` | `float` | "Time" over which most of the rotation interpolation occurs, when the UpdatedComponent (target) moves ahead of the interpolated component.<br>	  Since the implementation uses exponential lagged smoothing, this is a rough time value and experimentation should inform a final result.<br>	  A value of zero is effectively instantaneous interpolation. |
| `InterpLocationMaxLagDistance` | `float` | Max distance behind UpdatedComponent which the interpolated component is allowed to lag. |
| `InterpLocationSnapToTargetDistance` | `float` | Max distance behind UpdatedComponent beyond which the interpolated component is snapped to the target location instead.<br>	  For instance if the target teleports this far beyond the interpolated component, the interpolation is snapped to match the target. |

## Functions

### `IsVelocityUnderSimulationThreshold`

```text
IsVelocityUnderSimulationThreshold() -> bool
```

Returns true if velocity magnitude is less than BounceVelocityStopSimulatingThreshold.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetVelocityInLocalSpace`

```text
SetVelocityInLocalSpace(NewVelocity: FVector) -> void
```

Sets the velocity to the new value, rotated into Actor space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVelocity` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopSimulating`

```text
StopSimulating(HitResult: FHitResult &) -> void
```

Clears the reference to UpdatedComponent, fires stop event (OnProjectileStop), and stops ticking (if bAutoUpdateTickRegistration is true).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInterpolatedComponent`

```text
SetInterpolatedComponent(Component: USceneComponent *) -> void
```

Assigns the component that will be used for network interpolationsmoothing. It is expected that this is a component attached somewhere below the UpdatedComponent.
	  When network updates use MoveInterpolationTarget() to move the UpdatedComponent, the interpolated component's relative offset will be maintained and smoothed over
	  the course of future component ticks. The current relative location and rotation of the component is saved as the target offset for future interpolation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveInterpolationTarget`

```text
MoveInterpolationTarget(NewLocation: FVector &, NewRotation: FRotator &) -> void
```

Moves the UpdatedComponent, which is also the interpolation target for the interpolated component. If there is not interpolated component, this simply moves UpdatedComponent.
	  Use this typically from PostNetReceiveLocationAndRotation() or similar from an Actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector &` | - |
| `NewRotation` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetInterpolation`

```text
ResetInterpolation() -> void
```

Resets interpolation so that interpolated component snaps back to the initial locationrotation without any additional offsets.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInterpolationComplete`

```text
IsInterpolationComplete() -> bool
```

Returns whether interpolation is complete because the target has been reached. True when interpolation is disabled.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LimitVelocity`

```text
LimitVelocity(NewVelocity: FVector) -> FVector
```

Don't allow velocity magnitude to exceed MaxSpeed, if MaxSpeed is non-zero.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVelocity` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Delegates

### `OnProjectileBounce`

```text
OnProjectileBounce(ImpactResult: const FHitResult&, ImpactVelocity: const FVector&) -> void
```

Called when projectile impacts something and bounces are enabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |
| `ImpactVelocity` | `const FVector&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnProjectileStop`

```text
OnProjectileStop(ImpactResult: const FHitResult&) -> void
```

Called when projectile has come to a stop (velocity is below simulation threshold, bounces are disabled, or it is forcibly stopped).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProjectileMovementPathBase.json -->

# UProjectileMovementPathBase

抛体轨迹基类

## Inheritance

`UProjectileEffectBase`

## Events

### `ApplyParamsBP`

```text
ApplyParamsBP(Params: FProjectileParams &) -> void
```

动作发射时调用的参数
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Params` | `FProjectileParams &` | 发射参数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UProxyLODMeshSimplificationSettings.json -->

# UProxyLODMeshSimplificationSettings

Controls the system used to generate proxy LODs with merged meshes (i.e. the HLOD system).

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProxyLODMeshReductionModuleName` | `FName` | Mesh reduction plugin to use when simplifying mesh geometry for Hierarchical LOD |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URadialForceComponent.json -->

# URadialForceComponent

Used to emit a radial force or impulse that can affect physics objects and or destructible objects.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Radius` | `float` | The radius to apply the force or impulse in |
| `Falloff` | `TEnumAsByte < enum ERadialImpulseFalloff >` | How the force or impulse should fall off as object are further away from the center |
| `ImpulseStrength` | `float` | How strong the impulse should be |
| `bImpulseVelChange` | `uint32` | If true, the impulse will ignore mass of objects and will always result in a fixed velocity change |
| `bIgnoreOwningActor` | `uint32` | If true, do not apply forceimpulse to any physics objects that are part of the Actor that owns this component. |
| `ForceStrength` | `float` | How strong the force should be |
| `DestructibleDamage` | `float` | If > 0.f, will cause damage to destructible meshes as well |
| `ObjectTypesToAffect` | `TArray < TEnumAsByte < enum EObjectTypeQuery > >` | The object types that are affected by this radial force |

## Functions

### `FireImpulse`

```text
FireImpulse() -> void
```

Fire a single impulse

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddObjectTypeToAffect`

```text
AddObjectTypeToAffect(ObjectType: TEnumAsByte < enum EObjectTypeQuery >) -> void
```

Add an object type for this radial force to affect

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectType` | `TEnumAsByte < enum EObjectTypeQuery >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveObjectTypeToAffect`

```text
RemoveObjectTypeToAffect(ObjectType: TEnumAsByte < enum EObjectTypeQuery >) -> void
```

Remove an object type that is affected by this radial force

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectType` | `TEnumAsByte < enum EObjectTypeQuery >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UReflectionCaptureComponent.json -->

# UReflectionCaptureComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CaptureOffsetComponent` | `UBillboardComponent *` | - |
| `ReflectionSourceType` | `EReflectionSourceType` | Indicates where to get the reflection source from. |
| `IndoorOutdoorMask` | `TEnumAsByte < EIndoorOutdoorMask >` | - |
| `Cubemap` | `UTextureCube *` | Cubemap to use for reflection if ReflectionSourceType is set to RS_SpecifiedCubemap. |
| `SourceCubemapAngle` | `float` | Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap. |
| `Brightness` | `float` | A brightness control to scale the captured scene's reflection intensity. |
| `CaptureOffset` | `FVector` | World space offset to apply before capturing. |
| `EnabledPlatform` | `EReflectionPlatform` | - |
| `StateId` | `FGuid` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URendererOverrideSettings.json -->

# URendererOverrideSettings

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSupportAllShaderPermutations` | `uint32` | - |
| `bForceRecomputeTangents` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URendererSettings.json -->

# URendererSettings

Rendering settings.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bMobileHDR` | `uint32` | - |
| `bMobileDisableVertexFog` | `uint32` | - |
| `bMobileVTFLandscape` | `uint32` | - |
| `bMobileLandscapeVertexHole` | `uint32` | - |
| `bIdeaDecalOptimizedIO` | `uint32` | - |
| `MaxMobileCascades` | `int32` | - |
| `MobileMSAASampleCount` | `TEnumAsByte < EMobileMSAASampleCount :: Type >` | - |
| `CharacterDiffuseScale` | `float` | ToolTip = "Character diffuse scale parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| `CharacterDiffuseOffset` | `float` | ToolTip = "Character diffuse offset parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| `CharacterDiffusePower` | `float` | ToolTip = "Character diffuse power parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| `CharacterMinShadowFactor` | `float` | - |
| `StaticMeshDiffuseScale` | `float` | ToolTip = "Character diffuse scale parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| `StaticMeshDiffuseOffset` | `float` | ToolTip = "Static Mesh diffuse offset parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| `StaticMeshDiffusePower` | `float` | ToolTip = "Static Mesh diffuse power parameter for versatile diffuse model formula DiffuseFactor = pow( saturate( DiffuseScale  (dot(N,L) + DiffuseOffset) ), DiffusePower ).", |
| `StaticMeshMinShadowFactor` | `float` | - |
| `bMobileAllowROCCook` | `uint32` | - |
| `bVirtualTextures` | `uint32` | Virtual Texture |
| `bMobileVirtualTextures` | `uint32` | - |
| `bDiscardUnusedQualityLevels` | `uint32` | - |
| `GlobalStaticMeshCullingScreenSize` | `float` | - |
| `bOcclusionCulling` | `uint32` | - |
| `MinScreenRadiusForLights` | `float` | - |
| `MinScreenRadiusForEarlyZPass` | `float` | - |
| `MinScreenRadiusForCSMdepth` | `float` | - |
| `bPrecomputedVisibilityWarning` | `uint32` | - |
| `bTextureStreaming` | `uint32` | - |
| `bUseDXT5NormalMaps` | `uint32` | - |
| `bClearCoatEnableSecondNormal` | `uint32` | - |
| `ReflectionCaptureResolution` | `int32` | - |
| `ReflectionEnvironmentLightmapMixBasedOnRoughness` | `uint32` | - |
| `bForwardShading` | `uint32` | - |
| `bVertexFoggingForOpaque` | `uint32` | - |
| `bAllowStaticLighting` | `uint32` | - |
| `bUseNormalMapsForStaticLighting` | `uint32` | - |
| `bGenerateMeshDistanceFields` | `uint32` | - |
| `bEightBitMeshDistanceFields` | `uint32` | - |
| `bGenerateLandscapeGIData` | `uint32` | - |
| `bCompressMeshDistanceFields` | `uint32` | - |
| `TessellationAdaptivePixelsPerTriangle` | `float` | - |
| `bSeparateTranslucency` | `uint32` | - |
| `TranslucentSortPolicy` | `TEnumAsByte < ETranslucentSortPolicy :: Type >` | - |
| `TranslucentSortAxis` | `FVector` | - |
| `CustomDepthStencil` | `TEnumAsByte < ECustomDepthStencil :: Type >` | - |
| `bCustomDepthTaaJitter` | `uint32` | - |
| `bEnableAlphaChannelInPostProcessing` | `uint32` | - |
| `bDefaultFeatureBloom` | `uint32` | - |
| `bDefaultFeatureAmbientOcclusion` | `uint32` | - |
| `bDefaultFeatureAmbientOcclusionStaticFraction` | `uint32` | - |
| `bDefaultFeatureAutoExposure` | `uint32` | - |
| `DefaultFeatureAutoExposure` | `TEnumAsByte < EAutoExposureMethodUI :: Type >` | - |
| `bDefaultFeatureMotionBlur` | `uint32` | - |
| `bDefaultFeatureLensFlare` | `uint32` | - |
| `DefaultFeatureAntiAliasing` | `TEnumAsByte < EAntiAliasingMethod >` | - |
| `bRenderUnbuiltPreviewShadowsInGame` | `uint32` | - |
| `bStencilForLODDither` | `uint32` | - |
| `EarlyZPass` | `TEnumAsByte < EEarlyZPass :: Type >` | - |
| `bEarlyZPassMovable` | `uint32` | - |
| `bEarlyZPassOnlyMaterialMasking` | `uint32` | - |
| `bDBuffer` | `uint32` | - |
| `ClearSceneMethod` | `TEnumAsByte < EClearSceneOptions :: Type >` | - |
| `bBasePassOutputsVelocity` | `uint32` | - |
| `bSelectiveBasePassOutputs` | `uint32` | - |
| `bDefaultParticleCutouts` | `uint32` | - |
| `bGlobalClipPlane` | `uint32` | - |
| `GBufferFormat` | `TEnumAsByte < EGBufferFormat :: Type >` | - |
| `bUseGPUMorphTargets` | `uint32` | - |
| `bNvidiaAftermathEnabled` | `uint32` | - |
| `bInstancedStereo` | `uint32` | - |
| `bMultiView` | `uint32` | - |
| `bMobileMultiView` | `uint32` | - |
| `bMobileMultiViewDirect` | `uint32` | - |
| `bMonoscopicFarField` | `uint32` | - |
| `bDebugCanvasInLayer` | `uint32` | - |
| `WireframeCullThreshold` | `float` | - |
| `bSupportStationarySkylight` | `uint32` | - |
| `bSupportLowQualityLightmaps` | `uint32` | - |
| `bSupportPointLightWholeSceneShadows` | `uint32` | - |
| `bSupportAtmosphericFog` | `uint32` | - |
| `bSupportSkinCacheShaders` | `uint32` | - |
| `bMobileEnableStaticAndCSMShadowReceivers` | `uint32` | - |
| `bMobileAllowDistanceFieldShadows` | `uint32` | - |
| `bMobileAllowMovableDirectionalLights` | `uint32` | - |
| `MobileNumDynamicPointLights` | `uint32` | - |
| `bMobileAllowMovableSpotlights` | `uint32` | - |
| `SkinCacheSceneMemoryLimitInMB` | `float` | - |
| `bGPUSkinLimit2BoneInfluences` | `uint32` | - |
| `bSupportDepthOnlyIndexBuffers` | `uint32` | - |
| `bSupportReversedIndexBuffers` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UReorganizationTagSettings.json -->

# UReorganizationTagSettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TagGroupConfigs` | `TArray < FReorganizationTagGroupConfig >` | - |
| `DefaultTagColor` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URetainerBox.json -->

# URetainerBox

The Retainer Box renders children widgets to a render target first before
  later rendering that render target to the screen.  This allows both frequency
  and phase to be controlled so that the UI can actually render less often than the
  frequency of the main game render.  It also has the side benefit of allow materials
  to be applied to the render target after drawing the widgets to apply a simple post process.
 
   Single Child
   Caching  Performance

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DisableCache` | `bool` | - |
| `RenderOnInvalidation` | `bool` | Should this widget redraw the contents it has every time it receives an invalidation request<br>	  from it's children, similar to the invalidation panel. |
| `RenderOnPhase` | `bool` | Should this widget redraw the contents it has every time the phase occurs. |
| `Phase` | `int32` | The Phase this widget will draw on.<br>	 <br>	  If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.<br>	  If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every<br>	  other frame.  So in a 60Hz game, the UI would render at 30Hz. |
| `PhaseCount` | `int32` | The PhaseCount controls how many phases are possible know what to modulus the current frame <br>	  count by to determine if this is the current frame to draw the widget on.<br>	  <br>	  If the Phase is 0, and the PhaseCount is 1, the widget will be drawn fresh every frame.  <br>	  If the Phase were 0, and the PhaseCount were 2, this retainer would draw a fresh frame every <br>	  other frame.  So in a 60Hz game, the UI would render at 30Hz. |
| `bHittestRecordOpt` | `bool` | - |
| `bUsedForTickAdapter` | `bool` | - |
| `MaxRendersPerSecond` | `int32` | The maximum number of times this widget will redraw the contents it has every second. |
| `EffectMaterial` | `UMaterialInterface *` | The effect to optionally apply to the render target.  We will set the texture sampler based on the name<br>	  set in the @TextureParameter property.<br>	  <br>	  If you want to adjust transparency of the final image, make sure you set Blend Mode to AlphaComposite (Pre-Multiplied Alpha)<br>	  and make sure to multiply the alpha you're apply across the surface to the color and the alpha of the render target, otherwise<br>	  you won't see the expected color. |
| `TextureParameter` | `FName` | The texture sampler parameter of the @EffectMaterial, that we'll set to the render target. |

## Functions

### `EnableCachedRender`

```text
EnableCachedRender(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderPhase`

```text
SetRenderPhase(InPhase: int32, InPhaseCount: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPhase` | `int32` | - |
| `InPhaseCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableHittestRecordOpt`

```text
EnableHittestRecordOpt(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUsedForTickAdapter`

```text
SetUsedForTickAdapter(bValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestRender`

```text
RequestRender() -> void
```

Requests the retainer redrawn the contents it has.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEffectMaterial`

```text
GetEffectMaterial() -> UMaterialInstanceDynamic *
```

Get the current dynamic effect material applied to the retainer box.

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `SetEffectMaterial`

```text
SetEffectMaterial(EffectMaterial: UMaterialInterface *) -> void
```

Set a new effect material to the retainer widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EffectMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTextureParameter`

```text
SetTextureParameter(TextureParameter: FName) -> void
```

Sets the name of the texture parameter to set the render target to on the material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextureParameter` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UReverbEffect.json -->

# UReverbEffect

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Density` | `float` | Density - 0.0 < 1.0 < 1.0 - Coloration of the late reverb - lower value is more grainy |
| `Diffusion` | `float` | Diffusion - 0.0 < 1.0 < 1.0 - Echo density in the reverberation decay - lower is more grainy |
| `Gain` | `float` | Reverb Gain - 0.0 < 0.32 < 1.0 - overall reverb gain - master volume control |
| `GainHF` | `float` | Reverb Gain High Frequency - 0.0 < 0.89 < 1.0 - attenuates the high frequency reflected sound |
| `DecayTime` | `float` | Decay Time - 0.1 < 1.49 < 20.0 Seconds - larger is more reverb |
| `DecayHFRatio` | `float` | Decay High Frequency Ratio - 0.1 < 0.83 < 2.0 - how much the quicker or slower the high frequencies decay relative to the lower frequencies. |
| `ReflectionsGain` | `float` | Reflections Gain - 0.0 < 0.05 < 3.16 - controls the amount of initial reflections |
| `ReflectionsDelay` | `float` | Reflections Delay - 0.0 < 0.007 < 0.3 Seconds - the time between the listener receiving the direct path sound and the first reflection |
| `LateGain` | `float` | Late Reverb Gain - 0.0 < 1.26 < 10.0 - gain of the late reverb |
| `LateDelay` | `float` | Late Reverb Delay - 0.0 < 0.011 < 0.1 Seconds - time difference between late reverb and first reflections |
| `AirAbsorptionGainHF` | `float` | Air Absorption - 0.0 < 0.994 < 1.0 - lower value means more absorption |
| `RoomRolloffFactor` | `float` | Room Rolloff - 0.0 < 0.0 < 10.0 - multiplies the attenuation due to distance |
| `bChanged` | `uint32` | Transient property used to trigger real-time updates of the reverb for real-time editor previewing |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URichTextBlock.json -->

# URichTextBlock

The rich text block
 
   Fancy Text
   No Children

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text to display |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `Font` | `FSlateFontInfo` | The default font for the text. |
| `Color` | `FLinearColor` | The default color for the text. |
| `Decorators` | `TArray < URichTextBlockDecorator * >` | - |

## Functions

### `GetLocalText`

```text
GetLocalText() -> FText
```

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URichTextBlockDecorator.json -->

# URichTextBlockDecorator

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bReveal` | `bool` | - |
| `RevealedIndex` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URig.json -->

# URig

URig : that has rigging data for skeleton
 		- used for retargeting
 		- support to share different animations

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TransformBases` | `TArray < FTransformBase >` | Skeleton bone tree - each contains name and parent index |
| `Nodes` | `TArray < FNode >` | Skeleton bone tree - each contains name and parent index |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/URotatingMovementComponent.json -->

# URotatingMovementComponent

Performs continuous rotation of a component at a specific rotation rate.
  Rotation can optionally be offset around a pivot point.
  Collision testing is not performed during movement.

## Inheritance

`UMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RotationRate` | `FRotator` | How fast to update rollpitchyaw of the component we update. |
| `PivotTranslation` | `FVector` | Translation of pivot point around which we rotate, relative to current rotation.<br>	  For instance, with PivotTranslation set to (X=+100, Y=0, Z=0), rotation will occur<br>	  around the point +100 units along the local X axis from the center of the object,<br>	  rather than around the object's origin (the default). |
| `bRotationInLocalSpace` | `uint32` | Whether rotation is applied in local or world space. |
| `bCirculatingRotation` | `bool` | - |
| `RotationAngle` | `FRotator` | - |
| `OriginRotator` | `FRotator` | - |
| `bCircleFlag` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USafeZone.json -->

# USafeZone

The Safe-Zone widget is an essential part of developing a game UI that can run on lots of different non-PC platforms.
  While a modern flat panel computer monitor may not have over scan issues, this is a common occurrence for Consoles.  
  It's common for TVs to have extra pixels under the bezel, in addition to projectors and projection TVs having potentially
  several vertical and horizontal columns of pixels hidden behind or against a black border of the projection screen.
  
  Useful testing console commands to help, simulate the safe zone on PC,
    r.DebugSafeZone.TitleRatio 0.96
    r.DebugActionZone.ActionRatio 0.96
  
  To enable a red band to visualize the safe zone, use this console command,
  r.DebugSafeZone.Mode controls the debug visualization overlay (0..2, default 0).
    0: Do not display the safe zone overlay.
    1: Display the overlay for the title safe zone.
    2: Display the overlay for the action safe zone.

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PadLeft` | `bool` | If this safe zone should pad for the left side of the screen's safe zone |
| `PadRight` | `bool` | If this safe zone should pad for the right side of the screen's safe zone |
| `PadTop` | `bool` | If this safe zone should pad for the top side of the screen's safe zone |
| `PadBottom` | `bool` | If this safe zone should pad for the bottom side of the screen's safe zone |

## Functions

### `SetSidesToPad`

```text
SetSidesToPad(InPadLeft: bool, InPadRight: bool, InPadTop: bool, InPadBottom: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadLeft` | `bool` | - |
| `InPadRight` | `bool` | - |
| `InPadTop` | `bool` | - |
| `InPadBottom` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USafeZoneSlot.json -->

# USafeZoneSlot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIsTitleSafe` | `bool` | - |
| `SafeAreaScale` | `FMargin` | - |
| `HAlign` | `TEnumAsByte < EHorizontalAlignment >` | - |
| `VAlign` | `TEnumAsByte < EVerticalAlignment >` | - |
| `Padding` | `FMargin` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UScaleBox.json -->

# UScaleBox

Allows you to place content with a desired size and have it scale to meet the constraints placed on this box's alloted area.  If
  you needed to have a background image scale to fill an area but not become distorted with different aspect ratios, or if you need
  to auto fit some text to an area, this is the control for you.
 
   Single Child
   Aspect Ratio

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Stretch` | `TEnumAsByte < EStretch :: Type >` | The stretching rule to apply when content is stretched |
| `StretchDirection` | `TEnumAsByte < EStretchDirection :: Type >` | Controls in what direction content can be scaled |
| `UserSpecifiedScale` | `float` | Optional scale that can be specified by the User. Used only for UserSpecified stretching. |
| `UserSpecifiedScaleBias` | `float` | Scale bias that can fit to the content, especially for the text exceeded the bounds. <br>	 #if UMG_SCALE_BIAS |
| `IgnoreInheritedScale` | `bool` | Optional bool to ignore the inherited scale. Applies inverse scaling to counteract parents before applying the local scale operation. |
| `UsePcParams` | `bool` | - |
| `StretchPc` | `TEnumAsByte < EStretch :: Type >` | - |
| `StretchDirectionPc` | `TEnumAsByte < EStretchDirection :: Type >` | - |
| `UserSpecifiedScalePc` | `float` | - |
| `UserSpecifiedScaleBiasPc` | `float` | - |
| `IgnoreInheritedScalePc` | `bool` | - |
| `bSingleLayoutPass` | `bool` | Only perform a single layout pass, if you do this, it can save a considerable<br>	  amount of time, however, some things like text may not look correct.  You may also<br>	  see the UI judder between frames.  This generally is caused by not explicitly<br>	  sizing the widget, and instead allowing it to layout based on desired size along<br>	  which won't work in Single Layout Pass mode. |
| `bFroceSlateLayoutCachingCalcSize` | `bool` | - |
| `bForceUseLastUnPrepassChildSize` | `bool` | - |

## Functions

### `SetStretch`

```text
SetStretch(InStretch: EStretch :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStretch` | `EStretch :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStretchDirection`

```text
SetStretchDirection(InStretchDirection: EStretchDirection :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStretchDirection` | `EStretchDirection :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUserSpecifiedScale`

```text
SetUserSpecifiedScale(InUserSpecifiedScale: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUserSpecifiedScale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIgnoreInheritedScale`

```text
SetIgnoreInheritedScale(bInIgnoreInheritedScale: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInIgnoreInheritedScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUserSpecifiedScaleBias`

```text
SetUserSpecifiedScaleBias(InUserSpecifiedScaleBias: float) -> void
```

#if UMG_SCALEBOX_BIAS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUserSpecifiedScaleBias` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPcParamController`

```text
SetPcParamController(InValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUIRectOffsetChange`

```text
OnUIRectOffsetChange() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UScaleBoxSlot.json -->

# UScaleBoxSlot

The Slot for the UScaleBoxSlot, contains the widget displayed in a button's single slot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

## Functions

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(InVerticalAlignment: EVerticalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVerticalAlignment` | `EVerticalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USceneCaptureComponent.json -->

# USceneCaptureComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PrimitiveRenderMode` | `ESceneCapturePrimitiveRenderMode` | Controls what primitives get rendered into the scene capture. |
| `HiddenComponents` | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | The components won't rendered by current component. |
| `HiddenActors` | `TArray < AActor * >` | The actors to hide in the scene capture. |
| `ShowOnlyComponents` | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | The only components to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList. |
| `bShowAttachedActor` | `bool` | - |
| `ShowOnlyActors` | `TArray < AActor * >` | The only actors to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList. |
| `bCaptureEveryFrame` | `bool` | Whether to update the capture's contents every frame.  If disabled, the component will render once on load and then only when moved. |
| `bCaptureOnMovement` | `bool` | Whether to update the capture's contents on movement.  Disable if you are going to capture manually from blueprint. |
| `bAlwaysPersistRenderingState` | `bool` | Whether to persist the rendering state even if bCaptureEveryFrame==false.  This allows velocities for Motion Blur and Temporal AA to be computed. |
| `LODDistanceFactor` | `float` | Scales the distance used by LOD. Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass. |
| `MaxViewDistanceOverride` | `float` | if > 0, sets a maximum render distance override.  Can be used to cull distant objects from a reflection if the reflecting plane is in an enclosed area like a hallway or room |
| `CaptureSortPriority` | `int32` | Capture priority within the frame to sort scene capture on GPU to resolve interdependencies between multiple capture components. Highest come first. |
| `ShowFlagSettings` | `TArray < struct FEngineShowFlagsSetting >` | ShowFlags for the SceneCapture's ViewFamily, to control rendering settings for this view. Hidden but accessible through details customization |
| `LightingChannels` | `FLightingChannels` | - |
| `bUseLightingChannels` | `bool` | - |

## Functions

### `HideComponent`

```text
HideComponent(InComponent: UPrimitiveComponent *) -> void
```

Adds the component to our list of hidden components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UPrimitiveComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HideActorComponents`

```text
HideActorComponents(InActor: AActor *) -> void
```

Adds all primitive components in the actor to our list of hidden components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowOnlyComponent`

```text
ShowOnlyComponent(InComponent: UPrimitiveComponent *) -> void
```

Adds the component to our list of show-only components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UPrimitiveComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowOnlyActorComponents`

```text
ShowOnlyActorComponents(InActor: AActor *) -> void
```

Adds all primitive components in the actor to our list of show-only components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveShowOnlyComponent`

```text
RemoveShowOnlyComponent(InComponent: UPrimitiveComponent *) -> void
```

Removes a component from the Show Only list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UPrimitiveComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveShowOnlyActorComponents`

```text
RemoveShowOnlyActorComponents(InActor: AActor *) -> void
```

Removes a actor's components from the Show Only list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearShowOnlyComponents`

```text
ClearShowOnlyComponents() -> void
```

Clears the Show Only list.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearHiddenComponents`

```text
ClearHiddenComponents() -> void
```

Clears the hidden list.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCaptureSortPriority`

```text
SetCaptureSortPriority(NewCaptureSortPriority: int32) -> void
```

Changes the value of TranslucentSortPriority.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCaptureSortPriority` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USceneCaptureComponent2D.json -->

# USceneCaptureComponent2D

Used to capture a 'snapshot' of the scene from a single plane and feed it to a render target.

## Inheritance

`USceneCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProjectionType` | `TEnumAsByte < ECameraProjectionMode :: Type >` | - |
| `FOVAngle` | `float` | Camera field of view (in degrees). |
| `OrthoWidth` | `float` | The desired width (in world units) of the orthographic view (ignored in Perspective mode) |
| `TextureTarget` | `UTextureRenderTarget2D *` | Output render target of the scene capture that can be read in materals. |
| `CaptureSource` | `TEnumAsByte < enum ESceneCaptureSource >` | - |
| `CompositeMode` | `TEnumAsByte < enum ESceneCaptureCompositeMode >` | When enabled, the scene capture will composite into the render target instead of overwriting its contents. |
| `PostProcessSettings` | `FPostProcessSettings` | - |
| `PostProcessBlendWeight` | `float` | Range (0.0, 1.0) where 0 indicates no effect, 1 indicates full effect. |
| `bUseCustomProjectionMatrix` | `bool` | Whether a custom projection matrix will be used during rendering. Use with caution. Does not currently affect culling |
| `CustomProjectionMatrix` | `FMatrix` | The custom projection matrix to use |
| `bEnableClipPlane` | `bool` | Enables a clip plane while rendering the scene capture which is useful for portals.  <br>	  The global clip plane must be enabled in the renderer project settings for this to work. |
| `ClipPlaneBase` | `FVector` | Base position for the clip plane, can be any position on the plane. |
| `ClipPlaneNormal` | `FVector` | Normal for the plane. |
| `bCameraCutThisFrame` | `uint32` | True if we did a camera cut this frame. Automatically reset to false at every capture.<br>	  This flag affects various things in the renderer (such as whether to use the occlusion queries from last frame, and motion blur).<br>	  Similar to UPlayerCameraManager::bGameCameraCutThisFrame. |

## Functions

### `AddOrUpdateBlendable`

```text
AddOrUpdateBlendable(InBlendableObject: TScriptInterface < IBlendableInterface >, InWeight: float) -> void
```

Adds an Blendable (implements IBlendableInterface) to the array of Blendables (if it doesn't exist) and update the weight

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendableObject` | `TScriptInterface < IBlendableInterface >` | - |
| `InWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USceneCaptureComponentCube.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USceneComponent.json -->

# USceneComponent

A SceneComponent has a transform and supports attachment, but has no rendering or collision capabilities.
  Useful as a 'dummy' component in the hierarchy to offset others.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PhysicsVolume` | `TWeakObjectPtr < APhysicsVolume >` | Physics Volume in which this SceneComponent is located |
| `AttachParent` | `USceneComponent *` | What we are currently attached to. If valid, RelativeLocation etc. are used relative to this object |
| `AttachSocketName` | `FName` | Optional socket name on AttachParent that we are attached to. |
| `AttachChildren` | `TArray < USceneComponent * >` | List of child SceneComponents that are attached to us. |
| `ClientAttachedChildren` | `TArray < USceneComponent * >` | Set of attached SceneComponents that were attached by the client so we can fix up AttachChildren when it is replicated to us. |
| `RelativeLocation` | `FVector` | Location of the component relative to its parent |
| `RelativeRotation` | `FRotator` | Rotation of the component relative to its parent |
| `RelativeScale3D` | `FVector` | Non-uniform scaling of the component relative to its parent.<br>		Note that scaling is always applied in local space (no shearing etc) |
| `ComponentToWorld` | `FTransform` | Current transform of the component, relative to the world |
| `ComponentVelocity` | `FVector` | Velocity of the component.<br>	 @see GetComponentVelocity() |
| `bComponentToWorldUpdated` | `uint8` | True if we have ever updated ComponentToWorld based on RelativeLocationRotationScale. Used at startup to make sure it is initialized. |
| `bAbsoluteLocation` | `uint8` | If RelativeLocation should be considered relative to the world, rather than the parent |
| `bAbsoluteRotation` | `uint8` | If RelativeRotation should be considered relative to the world, rather than the parent |
| `bAbsoluteScale` | `uint8` | If RelativeScale3D should be considered relative to the world, rather than the parent |
| `bVisible` | `uint8` | Whether to completely draw the primitive; if false, the primitive is not drawn, does not cast a shadow. |
| `bHiddenInGame` | `uint8` | Whether to hide the primitive in game, if the primitive is Visible. |
| `bShouldUpdatePhysicsVolume` | `uint8` | Whether or not the cached PhysicsVolume this component overlaps should be updated when the component is moved.<br>	  @see GetPhysicsVolume() |
| `bBoundsChangeTriggersStreamingDataRebuild` | `uint8` | If true, a change in the bounds of the component will call trigger a streaming data rebuild |
| `bUseAttachParentBound` | `uint8` | If true, this component uses its parents bounds when attached.<br>	   This can be a significant optimization with many components attached together. |
| `bShouldUpdateOverLaps` | `uint8` | - |
| `bForceUpdateChildCompTransform` | `uint8` | - |
| `bEnableUpdateTransformOption` | `uint8` | - |
| `bUpdateTransformOptionConsiderAbsolute` | `uint8` | - |
| `bOpenServerOptLite` | `uint8` | Simplify server move<br>		by zoranouyang |
| `bShouldUseTeleportMove` | `uint8` | - |
| `bForceFrameInterpolate` | `uint8` | - |
| `bEnableParallelMove` | `uint8` | - |
| `Mobility` | `TEnumAsByte < EComponentMobility :: Type >` | How often this component is allowed to move, used to make various optimizations. Only safe to set in constructor. |
| `DetailMode` | `TEnumAsByte < enum EDetailMode >` | If detail mode is >= system detail mode, primitive won't be rendered. |
| `UpdateTransformOption` | `EUpdateTransformOption` | - |
| `bIsFppLayerRecursive` | `uint8` | - |
| `bDisableFppLayerRecursive` | `uint8` | - |
| `bAbsoluteTranslation_DEPRECATED` | `uint8` | - |
| `bVisualizeComponent` | `uint8` | - |
| `bVisibilityMayChange` | `uint8` | Let Editor tool, like pvs, to know whether visibility may change |
| `RelativeTranslation_DEPRECATED` | `FVector` | - |

## Functions

### `GetBoundsOirgin`

```text
GetBoundsOirgin() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetBoundsBoxExtent`

```text
GetBoundsBoxExtent() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `OnRep_Transform`

```text
OnRep_Transform() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AttachParent`

```text
OnRep_AttachParent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AttachChildren`

```text
OnRep_AttachChildren() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AttachSocketName`

```text
OnRep_AttachSocketName() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_Visibility`

```text
OnRep_Visibility(OldValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetRelativeLocation`

```text
K2_SetRelativeLocation(NewLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the location of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location of the component relative to its parent. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetRelativeRotation`

```text
K2_SetRelativeRotation(NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | New rotation of the component relative to its parent |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetRelativeTransform`

```text
K2_SetRelativeTransform(NewTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the transform of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTransform` | `FTransform &` | New transform of the component relative to its parent. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetRelativeTransform`

```text
GetRelativeTransform() -> FTransform
```

Returns the transform of the component relative to its parent

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `ResetRelativeTransform`

```text
ResetRelativeTransform() -> void
```

Reset the transform of the component relative to its parent. Sets relative location to zero, relative rotation to no rotation, and Scale to 1.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRelativeScale3D`

```text
SetRelativeScale3D(NewScale3D: FVector) -> void
```

Set the non-uniform scale of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScale3D` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddRelativeLocation`

```text
K2_AddRelativeLocation(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the translation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | Change in location of the component relative to its parent |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddRelativeRotation`

```text
K2_AddRelativeRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta the rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | Change in rotation of the component relative to is parent. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddLocalOffset`

```text
K2_AddLocalOffset(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the location of the component in its local reference frame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | Change in location of the component in its local reference frame. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddLocalRotation`

```text
K2_AddLocalRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the rotation of the component in its local reference frame

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | Change in rotation of the component in its local reference frame. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddLocalTransform`

```text
K2_AddLocalTransform(DeltaTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the transform of the component in its local reference frame. Scale is unchanged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTransform` | `FTransform &` | Change in transform of the component in its local reference frame. Scale is unchanged. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetWorldLocation`

```text
K2_SetWorldLocation(NewLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Put this component at the specified location in world space. Updates relative location to achieve the final world location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetWorldRotation`

```text
K2_SetWorldRotation(NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Put this component at the specified rotation in world space. Updates relative rotation to achieve the final world rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRotation` | `FRotator` | New rotation in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldScale3D`

```text
SetWorldScale3D(NewScale: FVector) -> void
```

Set the relative scale of the component to put it at the supplied scale in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScale` | `FVector` | New scale in world space for this component. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetWorldTransform`

```text
K2_SetWorldTransform(NewTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the transform of the component in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTransform` | `FTransform &` | New transform in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddWorldOffset`

```text
K2_AddWorldOffset(DeltaLocation: FVector, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the location of the component in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaLocation` | `FVector` | Change in location in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddWorldRotation`

```text
K2_AddWorldRotation(DeltaRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the rotation of the component in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaRotation` | `FRotator` | Change in rotation in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination (currently not supported for rotation). |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AddWorldTransform`

```text
K2_AddWorldTransform(DeltaTransform: FTransform &, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Adds a delta to the transform of the component in world space. Scale is unchanged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTransform` | `FTransform &` | Change in transform in world space for the component. Scale is unchanged. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetComponentLocation`

```text
K2_GetComponentLocation() -> FVector
```

Return location of the component, in world space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_GetComponentRotation`

```text
K2_GetComponentRotation() -> FRotator
```

Returns rotation of the component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `K2_GetComponentScale`

```text
K2_GetComponentScale() -> FVector
```

Returns scale of the component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `K2_GetComponentToWorld`

```text
K2_GetComponentToWorld() -> FTransform
```

Get the current component-to-world transform for this component

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetForwardVector`

```text
GetForwardVector() -> FVector
```

Get the forward (X) unit direction vector from this component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetUpVector`

```text
GetUpVector() -> FVector
```

Get the up (Z) unit direction vector from this component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVector`

```text
GetRightVector() -> FVector
```

Get the right (Y) unit direction vector from this component, in world space.

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `IsSimulatingPhysics`

```text
IsSimulatingPhysics(BoneName: FName) -> bool
```

Returns whether the specified body is currently using physics simulation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsAnySimulatingPhysics`

```text
IsAnySimulatingPhysics() -> bool
```

Returns whether the specified body is currently using physics simulation

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetAttachParent`

```text
GetAttachParent() -> USceneComponent *
```

Get the SceneComponent we are attached to.

**Returns**

| Type | Description |
|---|---|
| `USceneComponent *` | - |

### `GetAttachSocketName`

```text
GetAttachSocketName() -> FName
```

Get the socket we are attached to.

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetParentComponents`

```text
GetParentComponents(Parents: TArray < USceneComponent * > &) -> void
```

Gets all parent components up to and including the root component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parents` | `TArray < USceneComponent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumChildrenComponents`

```text
GetNumChildrenComponents() -> int32
```

Gets the number of attached children components

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetChildComponent`

```text
GetChildComponent(ChildIndex: int32) -> USceneComponent *
```

Gets the attached child component at the specified location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChildIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `USceneComponent *` | - |

### `GetChildrenComponents`

```text
GetChildrenComponents(bIncludeAllDescendants: bool, Children: TArray < USceneComponent * > &) -> void
```

Gets all the attached child components

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIncludeAllDescendants` | `bool` | Whether to include all descendants in the list of children (i.e. grandchildren, great grandchildren, etc.) |
| `Children` | `TArray < USceneComponent * > &` | The list of attached child components |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_AttachTo`

```text
K2_AttachTo(InParent: USceneComponent *, InSocketName: FName, AttachType: EAttachLocation :: Type, bWeldSimulatedBodies: bool) -> bool
```

Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParent` | `USceneComponent *` | Parent to attach to. |
| `InSocketName` | `FName` | Optional socket to attach to on the parent. |
| `AttachType` | `EAttachLocation :: Type` | How to handle transform when attaching (Keep relative offset, keep world position, etc). |
| `bWeldSimulatedBodies` | `bool` | Whether to weld together simulated physics bodies. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if attachment is successful (or already attached to requested parentsocket), false if attachment is rejected and there is no change in AttachParent. |

### `K2_AttachToComponent`

```text
K2_AttachToComponent(Parent: USceneComponent *, SocketName: FName, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, bWeldSimulatedBodies: bool) -> bool
```

Attach this component to another scene component, optionally at a named socket. It is valid to call this on components whether or not they have been Registered.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `USceneComponent *` | Parent to attach to. |
| `SocketName` | `FName` | Optional socket to attach to on the parent. |
| `LocationRule` | `EAttachmentRule` | How to handle translation when attaching. |
| `RotationRule` | `EAttachmentRule` | How to handle rotation when attaching. |
| `ScaleRule` | `EAttachmentRule` | How to handle scale when attaching. |
| `bWeldSimulatedBodies` | `bool` | Whether to weld together simulated physics bodies. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if attachment is successful (or already attached to requested parentsocket), false if attachment is rejected and there is no change in AttachParent. |

### `SnapTo`

```text
SnapTo(InParent: USceneComponent *, InSocketName: FName) -> bool
```

Zeroes out the relative transform of the component, and calls AttachTo(). Useful for attaching directly to a scene component or socket location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InParent` | `USceneComponent *` | - |
| `InSocketName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DetachFromParent`

```text
DetachFromParent(bMaintainWorldPosition: bool, bCallModify: bool) -> void
```

Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (See WeldTo)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bMaintainWorldPosition` | `bool` | If true, update the relative location of the component to keep its world position the same |
| `bCallModify` | `bool` | If true, call Modify() on the component and the current attach parent component |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_DetachFromComponent`

```text
K2_DetachFromComponent(LocationRule: EDetachmentRule, RotationRule: EDetachmentRule, ScaleRule: EDetachmentRule, bCallModify: bool) -> void
```

Detach this component from whatever it is attached to. Automatically unwelds components that are welded together (See WeldTo)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocationRule` | `EDetachmentRule` | How to handle translations when detaching. |
| `RotationRule` | `EDetachmentRule` | How to handle rotation when detaching. |
| `ScaleRule` | `EDetachmentRule` | How to handle scales when detaching. |
| `bCallModify` | `bool` | If true, call Modify() on the component and the current attach parent component |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllSocketNames`

```text
GetAllSocketNames() -> TArray < FName >
```

Gets the names of all the sockets on the component.

**Returns**

| Type | Description |
|---|---|
| `TArray < FName >` | Get the names of all the sockets on the component. |

### `GetSocketTransform`

```text
GetSocketTransform(InSocketName: FName, TransformSpace: ERelativeTransformSpace) -> FTransform
```

Get world-space socket transform.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |
| `TransformSpace` | `ERelativeTransformSpace` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketLocation`

```text
GetSocketLocation(InSocketName: FName) -> FVector
```

Get world-space socket or bone location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketRotation`

```text
GetSocketRotation(InSocketName: FName) -> FRotator
```

Get world-space socket or bone  FRotator rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketQuaternion`

```text
GetSocketQuaternion(InSocketName: FName) -> FQuat
```

Get world-space socket or bone FQuat rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `FQuat` | Socket transform in world space if socket if found. Otherwise it will return component's transform in world space. |

### `GetSocketScale`

```text
GetSocketScale(InSocketName: FName) -> FVector
```

Get world-space socket or bone scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the scale |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Socket scale in world space if socket if found. Otherwise it will return component's scale in world space. |

### `DoesSocketExist`

```text
DoesSocketExist(InSocketName: FName) -> bool
```

return true if socket with the given name exists

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | Name of the socket or the bone to get the transform |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the socket with the given name exists. Otherwise, return false |

### `GetComponentVelocity`

```text
GetComponentVelocity() -> FVector
```

Get velocity of the component: either ComponentVelocity, or the velocity of the physics body if simulating physics.

**Returns**

| Type | Description |
|---|---|
| `FVector` | Velocity of the component |

### `IsVisible`

```text
IsVisible() -> bool
```

Is this component visible or not in game

**Returns**

| Type | Description |
|---|---|
| `bool` | true if visible |

### `SetVisibility`

```text
SetVisibility(bNewVisibility: bool, bPropagateToChildren: bool, bForceNoPropagate: bool) -> void
```

Set visibility of the component, if during game use this to turn onoff

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewVisibility` | `bool` | - |
| `bPropagateToChildren` | `bool` | - |
| `bForceNoPropagate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleVisibility`

```text
ToggleVisibility(bPropagateToChildren: bool) -> void
```

Toggle visibility of the component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bPropagateToChildren` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHiddenInGame`

```text
SetHiddenInGame(NewHidden: bool, bPropagateToChildren: bool) -> void
```

Changes the value of HiddenGame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewHidden` | `bool` | - The value to assign to HiddenGame. |
| `bPropagateToChildren` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsForceFrameInterpolate`

```text
IsForceFrameInterpolate() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetForceFrameInterpolate`

```text
SetForceFrameInterpolate(InForceFrameInterpolate: bool) -> void
```

set bForceDynamic

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForceFrameInterpolate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetComponentTransformViewTranslatedBP`

```text
GetComponentTransformViewTranslatedBP() -> FTransform
```

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetComponentLocal`

```text
GetComponentLocal(localTransform: FTransform &) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `localTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetPhysicsVolume`

```text
GetPhysicsVolume() -> APhysicsVolume *
```

Get the PhysicsVolume overlapping this component.

**Returns**

| Type | Description |
|---|---|
| `APhysicsVolume *` | - |

### `K2_SetRelativeLocationAndRotation`

```text
K2_SetRelativeLocationAndRotation(NewLocation: FVector, NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the location and rotation of the component relative to its parent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location of the component relative to its parent. |
| `NewRotation` | `FRotator` | New rotation of the component relative to its parent. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAbsolute`

```text
SetAbsolute(bNewAbsoluteLocation: bool, bNewAbsoluteRotation: bool, bNewAbsoluteScale: bool) -> void
```

Set which parts of the relative transform should be relative to parent, and which should be relative to world

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewAbsoluteLocation` | `bool` | - |
| `bNewAbsoluteRotation` | `bool` | - |
| `bNewAbsoluteScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsAbsoluteLocation`

```text
IsAbsoluteLocation(ContainsParent: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ContainsParent` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `K2_SetWorldLocationAndRotation`

```text
K2_SetWorldLocationAndRotation(NewLocation: FVector, NewRotation: FRotator, bSweep: bool, SweepHitResult: FHitResult &, bTeleport: bool) -> void
```

Set the relative location and rotation of the component to put it at the supplied pose in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLocation` | `FVector` | New location in world space for the component. |
| `NewRotation` | `FRotator` | New rotation in world space for the component. |
| `bSweep` | `bool` | Whether we sweep to the destination location, triggering overlaps along the way and stopping short of the target if blocked by something. |
| `SweepHitResult` | `FHitResult &` | Hit result from any impact if sweep is true. |
| `bTeleport` | `bool` | Whether we teleport the physics state (if physics collision is enabled for this object). |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetMobility`

```text
K2_SetMobility(NewMobility: EComponentMobility :: Type) -> void
```

Set how often this component is allowed to move during runtime. Causes a component re-register if the component is already registered

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMobility` | `EComponentMobility :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFppLayerRecursive`

```text
SetFppLayerRecursive(InIsFppLayer: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsFppLayer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDisableFppLayerRecursive`

```text
SetDisableFppLayerRecursive(bDisable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDisable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `PhysicsVolumeChangedDelegate`

```text
PhysicsVolumeChangedDelegate(NewVolume: APhysicsVolume*) -> void
```

Delegate that will be called when PhysicsVolume has been changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVolume` | `APhysicsVolume*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TransformUpdatedDynamic`

```text
TransformUpdatedDynamic() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UScrollBar.json -->

# UScrollBar

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetStyle` | `FScrollBarStyle` | Style of the scrollbar |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `bAlwaysShowScrollbar` | `bool` | - |
| `Orientation` | `TEnumAsByte < EOrientation >` | - |
| `Thickness` | `FVector2D` | The thickness of the scrollbar thumb |

## Functions

### `SetState`

```text
SetState(InOffsetFraction: float, InThumbSizeFraction: float) -> void
```

Set the offset and size of the track's thumb.
	 Note that the maximum offset is 1.0-ThumbSizeFraction.
	 If the user can view 13 of the items in a single page, the maximum offset will be ~0.667f

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOffsetFraction` | `float` | Offset of the thumbnail from the top as a fraction of the total available scroll space. |
| `InThumbSizeFraction` | `float` | Size of thumbnail as a fraction of the total available scroll space. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UScrollBarWidgetStyle.json -->

# UScrollBarWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScrollBarStyle` | `FScrollBarStyle` | The actual data describing the scrollbox's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UScrollBox.json -->

# UScrollBox

An arbitrary scrollable collection of widgets.  Great for presenting 10-100 widgets in a list.  Doesn't support virtualization.

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetStyle` | `FScrollBoxStyle` | The style |
| `WidgetBarStyle` | `FScrollBarStyle` | The bar style |
| `OverscrollLooseness` | `float` | Overscroll Looseness |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `BarStyle_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `Orientation` | `TEnumAsByte < EOrientation >` | The orientation of the scrolling and stacking in the box. |
| `ScrollBarVisibility` | `ESlateVisibility` | Visibility |
| `ConsumeMouseWheel` | `EConsumeMouseWheel` | Enable to always consume mouse wheel event, even when scrolling is not possible |
| `ScrollbarThickness` | `FVector2D` | - |
| `AlwaysShowScrollbar` | `bool` | - |
| `AllowOverscroll` | `bool` | Disable to stop scrollbars from activating inertial overscrolling |
| `NavigationDestination` | `EDescendantScrollDestination` | - |
| `NavigationScrollPadding` | `float` | The amount of padding to ensure exists between the item being navigated to, at the edge of the<br>	  scrollbox.  Use this if you want to ensure there's a preview of the next item the user could scroll to. |
| `bAllowRightClickDragScrolling` | `bool` | Option to disable right-click-drag scrolling |
| `bScrollEnabled` | `bool` | 启用滑动 |
| `bScrollDisableHandled` | `bool` | 启用滑动 |
| `bPreciseScroll` | `bool` | 启用精准滑动 |
| `bDisableDragListScroll` | `bool` | 依旧可以通过拖拽bar或者鼠标滚轮滑动, 仅PC版生效 |
| `bScrollFocus` | `bool` | 滑动时获得焦点 |

## Functions

### `SetOrientation`

```text
SetOrientation(NewOrientation: EOrientation) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOrientation` | `EOrientation` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollBarVisibility`

```text
SetScrollBarVisibility(NewScrollBarVisibility: ESlateVisibility) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScrollBarVisibility` | `ESlateVisibility` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollbarThickness`

```text
SetScrollbarThickness(NewScrollbarThickness: FVector2D &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScrollbarThickness` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAlwaysShowScrollbar`

```text
SetAlwaysShowScrollbar(NewAlwaysShowScrollbar: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAlwaysShowScrollbar` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllowOverscroll`

```text
SetAllowOverscroll(NewAllowOverscroll: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAllowOverscroll` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCacheOverscrollOffset`

```text
GetCacheOverscrollOffset() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetOverscrollLooseness`

```text
SetOverscrollLooseness(v: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `v` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollEnabled`

```text
SetScrollEnabled(InScrollEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollDisableHandled`

```text
SetScrollDisableHandled(InScrollDisableHandled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollDisableHandled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollPrecise`

```text
SetScrollPrecise(InScrollPrecise: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollPrecise` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollFocus`

```text
SetScrollFocus(InScrollFocus: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollFocus` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDragListScrollEnabled`

```text
SetDragListScrollEnabled(InDragListScrollEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDragListScrollEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsReachEnd`

```text
IsReachEnd() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsLargerThanContentSize`

```text
IsLargerThanContentSize() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetScrollOffset`

```text
SetScrollOffset(NewScrollOffset: float) -> void
```

Updates the scroll offset of the scrollbox.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScrollOffset` | `float` | is in Slate Units. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScrollOffset`

```text
GetScrollOffset() -> float
```

Gets the scroll offset of the scrollbox in Slate Units.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `ScrollToStart`

```text
ScrollToStart() -> void
```

Scrolls the ScrollBox to the top instantly

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScrollToEnd`

```text
ScrollToEnd() -> void
```

Scrolls the ScrollBox to the bottom instantly during the next layout pass.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopScroll`

```text
StopScroll() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScrollWidgetIntoView`

```text
ScrollWidgetIntoView(WidgetToFind: UWidget *, AnimateScroll: bool, ScrollDestination: EDescendantScrollDestination) -> void
```

Scrolls the ScrollBox to the widget during the next layout pass.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetToFind` | `UWidget *` | - |
| `AnimateScroll` | `bool` | - |
| `ScrollDestination` | `EDescendantScrollDestination` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnUserScrolled`

```text
OnUserScrolled(CurrentOffset: float) -> void
```

Called when the scroll has changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUserScrolledUnused`

```text
OnUserScrolledUnused(CurrentOffset: float) -> void
```

Called when the scroll has changed,the value is mouse movement in another direction -zhenzhai

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTouchFinish`

```text
OnTouchFinish() -> void
```

Called when the touch has end

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UScrollBoxSlot.json -->

# UScrollBoxSlot

The Slot for the UScrollBox, contains the widget that are scrollable

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |

## Functions

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UScrollBoxWidgetStyle.json -->

# UScrollBoxWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScrollBoxStyle` | `FScrollBoxStyle` | The actual data describing the scrollbox's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USCS_Node.json -->

# USCS_Node

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentClass` | `UClass *` | Component class |
| `ComponentTemplate` | `UActorComponent *` | Template for the component to create |
| `CookedComponentInstancingData` | `FBlueprintCookedComponentInstancingData` | Cached data for faster runtime instancing (only used in cooked builds) |
| `VariableName` | `FName` | If non-None, creates a variable in the class and assigns the created blueprint to it |
| `AttachToName` | `FName` | SocketBone that Node might attach to |
| `ParentComponentOrVariableName` | `FName` | Component template or variable that Node might be parented to |
| `ParentComponentOwnerClassName` | `FName` | If the node is attached to another node inherited from a parent Blueprint, this contains the name of the Blueprint parent class that owns the component template |
| `bIsParentComponentNative` | `bool` | If the node is parented, this indicates whether or not the template is found in the CDO's Components array |
| `ChildNodes` | `TArray < USCS_Node * >` | Set of child nodes |
| `MetaDataArray` | `TArray < struct FBPVariableMetaDataEntry >` | Metadata information for this Node |
| `VariableGuid` | `FGuid` | - |
| `bIsFalseRoot_DEPRECATED` | `bool` | (DEPRECATED) |
| `bIsNative_DEPRECATED` | `bool` | (DEPRECATED) Indicates if this is a native component or not |
| `NativeComponentName_DEPRECATED` | `FName` | (DEPRECATED) If this is a native component, this is the name of the UActorComponent |
| `bVariableNameAutoGenerated_DEPRECATED` | `bool` | (DEPRECATED) If true, the variable name was a autogenerated and is not presented to the user |
| `InternalVariableName` | `FName` | Internal variable name. This is used for: |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UShaderPlatformQualitySettings.json -->

# UShaderPlatformQualitySettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QualityOverrides` | `FMaterialQualityOverrides` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UShadowMapTexture2D.json -->

# UShadowMapTexture2D

## Inheritance

`UTexture2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ShadowmapFlags` | `TEnumAsByte < enum EShadowMapFlags >` | Bit-field with shadowmap flags. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UShapeComponent.json -->

# UShapeComponent

ShapeComponent is a PrimitiveComponent that is represented by a simple geometrical shape (sphere, capsule, box, etc).

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ShapeColor` | `FColor` | Color used to draw the shape. |
| `ShapeBodySetup` | `UBodySetup *` | Description of collision |
| `bDrawOnlyIfSelected` | `uint8` | Only show this component if the actor is selected |
| `bShouldCollideWhenPlacing` | `uint8` | If true it allows Collision when placing even if collision is not enabled |
| `bDynamicObstacle` | `uint8` | If set, shape will be exported for navigation as dynamic modifier instead of using regular collision data |
| `AreaClass` | `TSubclassOf < UNavArea >` | Navigation area type (empty = default obstacle) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USimpleConstructionScript.json -->

# USimpleConstructionScript

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RootNodes` | `TArray < USCS_Node * >` | Root nodes of the construction script |
| `AllNodes` | `TArray < USCS_Node * >` | All nodes that exist in the hierarchy of this SimpleConstructionScript |
| `NodesRemovedInCompile` | `TArray < USCS_Node * >` | junyuandeng: temp container |
| `AllNodesIncludeEditorOnly` | `TArray < USCS_Node * >` | - |
| `DefaultSceneRootNode` | `USCS_Node *` | Default scene root node; used when no other nodes are available to use as the root |
| `RootNode_DEPRECATED` | `USCS_Node *` | (DEPRECATED) Root node of the construction script |
| `ActorComponentNodes_DEPRECATED` | `TArray < USCS_Node * >` | (DEPRECATED) Actor Component based nodes are stored here.  They cannot be in the tree hierarchy |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USimpleMeshComponent.json -->

# USimpleMeshComponent

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MeshSections` | `TArray < FSimpleMeshSection >` | - |
| `LocalBounds` | `FBoxSphereBounds` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USizeBox.json -->

# USizeBox

A widget that allows you to specify the size it reports to have and desire.  Not all widgets report a desired size
  that you actually desire.  Wrapping them in a SizeBox lets you have the Size Box force them to be a particular size.
 
   Single Child
   Fixed Size

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverride_WidthOverride` | `uint32` | - |
| `bOverride_HeightOverride` | `uint32` | - |
| `bOverride_MinDesiredWidth` | `uint32` | - |
| `bOverride_MinDesiredHeight` | `uint32` | - |
| `bOverride_MaxDesiredWidth` | `uint32` | - |
| `bOverride_MaxDesiredHeight` | `uint32` | - |
| `bOverride_MaxAspectRatio` | `uint32` | - |
| `WidthOverride` | `float` | When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width. |
| `HeightOverride` | `float` | When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height. |
| `MinDesiredWidth` | `float` | When specified, will report the MinDesiredWidth if larger than the content's desired width. |
| `MinDesiredHeight` | `float` | When specified, will report the MinDesiredHeight if larger than the content's desired height. |
| `MaxDesiredWidth` | `float` | When specified, will report the MaxDesiredWidth if smaller than the content's desired width. |
| `MaxDesiredHeight` | `float` | When specified, will report the MaxDesiredHeight if smaller than the content's desired height. |
| `MaxAspectRatio` | `float` | - |

## Functions

### `SetWidthOverride`

```text
SetWidthOverride(InWidthOverride: float) -> void
```

When specified, ignore the content's desired size and report the WidthOverride as the Box's desired width.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWidthOverride` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearWidthOverride`

```text
ClearWidthOverride() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHeightOverride`

```text
SetHeightOverride(InHeightOverride: float) -> void
```

When specified, ignore the content's desired size and report the HeightOverride as the Box's desired height.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHeightOverride` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearHeightOverride`

```text
ClearHeightOverride() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredWidth`

```text
SetMinDesiredWidth(InMinDesiredWidth: float) -> void
```

When specified, will report the MinDesiredWidth if larger than the content's desired width.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredWidth` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMinDesiredWidth`

```text
ClearMinDesiredWidth() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredHeight`

```text
SetMinDesiredHeight(InMinDesiredHeight: float) -> void
```

When specified, will report the MinDesiredHeight if larger than the content's desired height.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredHeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMinDesiredHeight`

```text
ClearMinDesiredHeight() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaxDesiredWidth`

```text
SetMaxDesiredWidth(InMaxDesiredWidth: float) -> void
```

When specified, will report the MaxDesiredWidth if smaller than the content's desired width.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxDesiredWidth` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMaxDesiredWidth`

```text
ClearMaxDesiredWidth() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaxDesiredHeight`

```text
SetMaxDesiredHeight(InMaxDesiredHeight: float) -> void
```

When specified, will report the MaxDesiredHeight if smaller than the content's desired height.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxDesiredHeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMaxDesiredHeight`

```text
ClearMaxDesiredHeight() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaxAspectRatio`

```text
SetMaxAspectRatio(InMaxAspectRatio: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxAspectRatio` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMaxAspectRatio`

```text
ClearMaxAspectRatio() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USizeBoxSlot.json -->

# USizeBoxSlot

The Slot for the USizeBoxSlot, contains the widget displayed in a button's single slot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

## Functions

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(InVerticalAlignment: EVerticalAlignment) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVerticalAlignment` | `EVerticalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkeletalBodySetup.json -->

# USkeletalBodySetup

## Inheritance

`UBodySetup`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bClientOnlyBody` | `bool` | - |
| `PhysicalAnimationData` | `TArray < FPhysicalAnimationProfile >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkeletalMesh.json -->

# USkeletalMesh

SkeletalMesh is geometry bound to a hierarchical skeleton of bones which can be animated for the purpose of deforming the mesh.
  Skeletal Meshes are built up of two parts; a set of polygons composed to make up the surface of the mesh, and a hierarchical skeleton which can be used to animate the polygons.
  The 3D models, rigging, and animations are created in an external modeling and animation application (3DSMax, Maya, Softimage, etc).

## Inheritance

`UObject` -> `IInterface_CollisionDataProvider` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Skeleton` | `USkeleton *` | Skeleton of this skeletal mesh |
| `bAllowCPUAccess` | `bool` | - |
| `bForceAllowCPUAccess` | `bool` | Ignore "FreeSkeletalMeshBuffers" console value. |
| `EncodeBits_Position` | `int32` | - |
| `EncodeBits_TexCoord` | `int32` | - |
| `EncodeBits_Normal` | `int32` | - |
| `EncodeBits_Generic` | `int32` | - |
| `EncodeBits_VertexColor` | `int32` | - |
| `EncodeSpeed` | `int32` | - |
| `DecodeSpeed` | `int32` | - |
| `ImportedBounds` | `FBoxSphereBounds` | Original imported mesh bounds |
| `ExtendedBounds` | `FBoxSphereBounds` | Bounds extended by user values below |
| `PositiveBoundsExtension` | `FVector` | Bound extension values in addition to imported bound in the positive direction of XYZ, <br>	 	positive value increases bound size and negative value decreases bound size. <br>	 	The final bound would be from [Imported Bound - Negative Bound] to [Imported Bound + Positive Bound]. |
| `NegativeBoundsExtension` | `FVector` | Bound extension values in addition to imported bound in the negative direction of XYZ, <br>	 	positive value increases bound size and negative value decreases bound size. <br>	 	The final bound would be from [Imported Bound - Negative Bound] to [Imported Bound + Positive Bound]. |
| `bIsStreamable` | `bool` | Streamable flag, determine whether to split the lod serialization, WITH_STREAMING_SM_LOD |
| `bCompressData` | `bool` | - |
| `IndirectLightingCachePositionOffset` | `FVector` | - |
| `NotInlineLODCount` | `uint8` | - |
| `Materials` | `TArray < FSkeletalMaterial >` | List of materials applied to this mesh. |
| `ReplaceMaterialInterface` | `UMaterialInterface *` | Replace for async compile pso. |
| `SkelMirrorTable` | `TArray < FBoneMirrorInfo >` | List of bones that should be mirrored. |
| `SkelMirrorAxis` | `TEnumAsByte < EAxis :: Type >` | - |
| `SkelMirrorFlipAxis` | `TEnumAsByte < EAxis :: Type >` | - |
| `CullingScreenSize` | `float` | Culling screen size |
| `LODInfo` | `TArray < FSkeletalMeshLODInfo >` | Struct containing information for each LOD level, such as materials to use, and when use the LOD. |
| `bUseAnyLODFeature` | `bool` | - |
| `PerLODBiasTypeInfo` | `TArray < FMeshPerLODBiasArray >` | When autonomous or simulated pawn needs special LOD bias |
| `bUseLODBiasExt` | `bool` | - |
| `bAutoUpdateLODBiasExt` | `bool` | - |
| `PerLODBiasTypeInfoExt` | `TArray < FMeshLODBiasCondition >` | - |
| `bUseFullPrecisionUVs` | `uint32` | If true, use 32 bit UVs. If false, use 16 bit UVs to save memory |
| `bUsedWithDynamicInstancing` | `uint32` | Whether or not this mesh can be used with dynamic instancing. |
| `bHasBeenSimplified` | `uint32` | true if this mesh has ever been simplified with Simplygon. |
| `bHasVertexColors` | `uint32` | Whether or not the mesh has vertex colors |
| `bEnablePerPolyCollision` | `uint32` | Uses skinned data for collision data. Per poly collision cannot be used for simulation, in most cases you are better off using the physics asset |
| `bEnableSelfCollision` | `uint32` | Need self-collision in an aggregate. In most cases you don't need if the aggregate isn't containing the ragdoll. submit by elvisxu |
| `BodySetup` | `UBodySetup *` | - |
| `PhysicsAsset` | `UPhysicsAsset *` | Physics and collision information used for this USkeletalMesh, set up in Physics Asset Editor.<br>	 	This is used for per-bone hit detection, accurate bounding box calculation and ragdoll physics for example. |
| `ShadowPhysicsAsset` | `UPhysicsAsset *` | Physics asset whose shapes will be used for shadowing when components have bCastCharacterCapsuleDirectShadow or bCastCharacterCapsuleIndirectShadow enabled.<br>	  Only spheres and sphyl shapes in the physics asset can be supported.  The more shapes used, the higher the cost of the capsule shadows will be. |
| `NodeMappingData` | `TArray < UNodeMappingContainer * >` | Mapping data that is saved |
| `LodModelsHasSkinweight` | `bool` | use for FStaticLODModel Serialize SkinweightProfilesData |
| `MorphTargets` | `TArray < UMorphTarget * >` | - |
| `ClothingAssets_DEPRECATED` | `TArray < FClothingAssetData_Legacy >` | Legacy clothing asset data, will be converted to new assets after loading |
| `PostProcessAnimBlueprint` | `TSubclassOf < UAnimInstance >` | Animation Blueprint class to run as a post process for this mesh.<br>	   This blueprint will be ran before physics, but after the main<br>	   anim instance for any skeletal mesh component using this mesh. |
| `MeshClothingAssets` | `TArray < UClothingAssetBase * >` | Clothing assets imported to this mesh. May or may not be in use currently on the mesh.<br>	  Ordering not guaranteed, use the provided getters to access elements in this array<br>	  whenever possible |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `Sockets` | `TArray < USkeletalMeshSocket * >` | Array of named socket locations, set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent. |
| `TemplateRetargetSource` | `FName` | - |
| `RefBoneNames` | `TArray < FName >` | - |
| `SkinWeightProfiles` | `TArray < FSkinWeightProfileInfo >` | Set of skin weight profiles associated with this mesh |
| `ScreenSizeCullingRoughDistance` | `float` | Rough Distance of Screen size Culling |
| `bCloseDraco` | `bool` | - |
| `AssetImportData` | `UAssetImportData *` | Importing data and options used for this mesh |
| `SourceFilePath_DEPRECATED` | `FString` | Path to the resource used to construct this skeletal mesh |
| `SourceFileTimestamp_DEPRECATED` | `FString` | DateTime-stamp of the file from the last import |
| `ThumbnailInfo` | `UThumbnailInfo *` | Information for thumbnail rendering |
| `bHasCustomDefaultEditorCamera` | `bool` | Should we use a custom camera transform when viewing this mesh in the tools |
| `DefaultEditorCameraLocation` | `FVector` | Default camera location |
| `DefaultEditorCameraRotation` | `FRotator` | Default camera rotation |
| `DefaultEditorCameraLookAt` | `FVector` | Default camera look at |
| `DefaultEditorCameraOrthoZoom` | `float` | Default camera ortho zoom |
| `OptimizationSettings` | `TArray < FSkeletalMeshOptimizationSettings >` | Optimization settings used to simplify LODs of this mesh. |
| `PreviewAttachedAssetContainer` | `FPreviewAssetAttachContainer` | Attached assets component for this mesh |
| `bPreviewDraco` | `bool` | - |
| `bUseHighPrecision` | `bool` | - |
| `SelectedEditorSection` | `int32` | The section currently selected in the Editor. Used for highlighting |
| `SelectedEditorMaterial` | `int32` | The Material currently selected. need to remember this index for reimporting cloth |
| `SelectedClothingSection` | `int32` | The section currently selected for clothing. need to remember this index for reimporting cloth |
| `FloorOffset` | `float` | Height offset for the floor mesh in the editor |
| `RetargetBasePose` | `TArray < FTransform >` | This is buffer that saves pose that is used by retargeting |

## Functions

### `GetBounds`

```text
GetBounds() -> FBoxSphereBounds
```

Get the extended bounds of this mesh (imported bounds plus bounds extension)

**Returns**

| Type | Description |
|---|---|
| `FBoxSphereBounds` | - |

### `GetImportedBounds`

```text
GetImportedBounds() -> FBoxSphereBounds
```

Get the original imported bounds of the skel mesh

**Returns**

| Type | Description |
|---|---|
| `FBoxSphereBounds` | - |

### `GetNodeMappingContainer`

```text
GetNodeMappingContainer(SourceAsset: UBlueprint *) -> UNodeMappingContainer *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceAsset` | `UBlueprint *` | - |

**Returns**

| Type | Description |
|---|---|
| `UNodeMappingContainer *` | - |

### `GetRefBonePose`

```text
GetRefBonePose() -> const TArray < FTransform > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < FTransform > &` | - |

### `GetRefBoneInfo`

```text
GetRefBoneInfo() -> const TArray < FName > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < FName > &` | - |

### `FindSocket`

```text
FindSocket(InSocketName: FName) -> USkeletalMeshSocket *
```

Find a socket object in this SkeletalMesh by name. 
	 	Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshSocket *` | - |

### `AddDynamicSocket`

```text
AddDynamicSocket(InSocket: USkeletalMeshSocket *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocket` | `USkeletalMeshSocket *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindSocketAndIndex`

```text
FindSocketAndIndex(InSocketName: FName, OutIndex: int32 &) -> USkeletalMeshSocket *
```

Find a socket object in this SkeletalMesh by name.
		Entering NAME_None will return NULL. If there are multiple sockets with the same name, will return the first one.
	   Also returns the index for the socket allowing for future fast access via GetSocketByIndex()

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | - |
| `OutIndex` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshSocket *` | - |

### `NumSockets`

```text
NumSockets() -> int32
```

Returns the number of sockets available. Both on this mesh and it's skeleton.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetSocketByIndex`

```text
GetSocketByIndex(Index: int32) -> USkeletalMeshSocket *
```

Returns a socket by index. Max index is NumSockets(). The meshes sockets are accessed first, then the skeletons.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `USkeletalMeshSocket *` | - |

### `IsSectionUsingCloth`

```text
IsSectionUsingCloth(InSectionIndex: int32, bCheckCorrespondingSections: bool) -> bool
```

Checks whether the provided section is using APEX cloth. if bCheckCorrespondingSections is true
	  disabled sections will defer to correspond sections to see if they use cloth (non-cloth sections
	  are disabled and another section added when cloth is enabled, using this flag allows for a check
	  on the original section to succeed)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSectionIndex` | `int32` | Index to check |
| `bCheckCorrespondingSections` | `bool` | Whether to check corresponding sections for disabled sections |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddCopySocket`

```text
AddCopySocket(InSocket: USkeletalMeshSocket *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocket` | `USkeletalMeshSocket *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkeletalMeshComponent.json -->

# USkeletalMeshComponent

SkeletalMeshComponent is used to create an instance of an animated SkeletalMesh asset.
 
  @see USkeletalMesh

## Inheritance

`USkinnedMeshComponent` -> `IInterface_CollisionDataProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimationMode` | `TEnumAsByte < EAnimationMode :: Type >` | Animation<br>	 <br>	 @Todo anim: Matinee related data start - this needs to be replaced to new system. <br>	 @Todo anim: Matinee related data end - this needs to be replaced to new system. <br>	 Whether to use Animation Blueprint or play Single Animation Asset. |
| `AnimBlueprintGeneratedClass` | `UAnimBlueprintGeneratedClass *` | - |
| `AnimClass` | `TSubclassOf < UAnimInstance >` | The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime. |
| `bAutoInitAnimInstance` | `bool` | The AnimBlueprint class to use. Use 'SetAnimInstanceClass' to change at runtime. |
| `AnimScriptInstance` | `UAnimInstance *` | The active animation graph program instance. |
| `SubInstances` | `TArray < UAnimInstance * >` | Any running sub anim instances that need to be updates on the game thread |
| `NewSubInstances` | `TArray < UAnimInstance * >` | - |
| `DirtySubInstances` | `TArray < UAnimInstance * >` | - |
| `StopTickSubInstances` | `TArray < UAnimInstance * >` | - |
| `PostProcessAnimInstance` | `UAnimInstance *` | An instance created from the PostPhysicsBlueprint property of the skeletal mesh we're using,<br>	   Runs after physics has been blended |
| `AnimationData` | `FSingleAnimationPlayData` | - |
| `CachedBoneSpaceTransforms` | `TArray < FTransform >` | Cached BoneSpaceTransforms for Update Rate optimization. |
| `CachedComponentSpaceTransforms` | `TArray < FTransform >` | Cached SpaceBases for Update Rate optimization. |
| `GlobalAnimRateScale` | `float` | Used to scale speed of all animations on this skeletal mesh. |
| `UseAsyncScene` | `EDynamicActorScene` | The simulation scene to use for this instance. By default we use what's in the physics asset (which defaults to the sync scene) |
| `bHasValidBodies` | `uint32` | If true, there is at least one body in the current PhysicsAsset with a valid bone in the current SkeletalMesh |
| `KinematicBonesUpdateType` | `TEnumAsByte < EKinematicBonesUpdateToPhysics :: Type >` | If we are running physics, should we update non-simulated bones based on the animation bone positions. |
| `UpdateKinematicBonesRate` | `int32` | - |
| `PhysicsTransformUpdateMode` | `TEnumAsByte < EPhysicsTransformUpdateMode :: Type >` | Whether physics simulation updates component transform. |
| `bBlendPhysics` | `uint32` | Enables blending in of physics bodies whether Simulate or not |
| `bEnablePhysicsOnDedicatedServer` | `uint32` | If true, simulate physics for this component on a dedicated server.<br>	   This should be set if simulating physics and replicating with a dedicated server.<br>	 	Note: This property cannot be changed at runtime. |
| `bEnableCreatePhysicsOnDedicatedServer` | `uint32` | - |
| `bNeedUpdatePhysicsTickRegisteredState` | `bool` | - |
| `bUpdateJointsFromAnimation` | `uint32` | If we should pass joint position to joints each frame, so that they can be used by motorized joints to drive the<br>	 	ragdoll based on the animation. |
| `bDisableClothSimulation` | `uint32` | Disable cloth simulation and play original animation without simulation |
| `bAllowAnimCurveEvaluation` | `uint32` | Disable animation curves for this component. If this is set true, no curves will be processed |
| `bDisableAnimCurves_DEPRECATED` | `uint32` | DEPRECATED. Use bAllowAnimCurveEvaluation instead |
| `DisallowedAnimCurves` | `TArray < FName >` | You can choose to disable certain curves if you prefer.<br>	  This is transient curves that will be ignored by animation system if you choose this |
| `bCollideWithEnvironment` | `uint32` | can't collide with part of environment if total collision volumes exceed 16 capsules or 32 planes per convex |
| `bCollideWithAttachedChildren` | `uint32` | can't collide with part of attached children if total collision volumes exceed 16 capsules or 32 planes per convex |
| `bLocalSpaceSimulation` | `uint32` | It's worth trying this option when you feel that the current cloth simulation is unstable.<br>	  The scale of the actor is maintained during the simulation.<br>	  It is possible to add the inertia effects to the simulation, through the inertiaScale parameter of the clothing material.<br>	  So with an inertiaScale of 1.0 there should be no visible difference between local space and global space simulation.<br>	  Known issues: - Currently there's simulation issues when this feature is used in 3.x (DE4076) So if localSpaceSim is enabled there's no inertia effect when the global pose of the clothing actor changes. |
| `bClothMorphTarget` | `uint32` | cloth morph target option<br>	  This option will be applied only before playing because should do pre-calculation to reduce computation time for run-time play<br>	  so it's impossible to change this option in run-time |
| `bResetAfterTeleport` | `uint32` | reset the clothing after moving the clothing position (called teleport) |
| `ClothBlendWeight` | `float` | weight to blend between simulated results and key-framed positions<br>	  if weight is 1.0, shows only cloth simulation results and 0.0 will show only skinned results |
| `RootBoneTranslation` | `FVector` | Offset of the root bone from the reference pose. Used to offset bounding box. |
| `bDeferMovementFromSceneQueries` | `uint32` | Optimization<br>	 <br>	  Whether animation and world transform updates are deferred. If this is on, the kinematic bodies (scene query data) will not update until the next time the physics simulation is run |
| `bNoSkeletonUpdate` | `uint32` | Skips Ticking and Bone Refresh. |
| `bPauseAnims` | `uint32` | pauses this component's animations (doesn't tick them, but still refreshes bones) |
| `bUseRefPoseOnInitAnim` | `bool` | On InitAnim should we set to ref pose (if false use first tick of animation data) |
| `bEnablePerPolyCollision` | `uint32` | Uses skinned data for collision data. |
| `BodySetup` | `UBodySetup *` | Used for per poly collision. In 99% of cases you will be better off using a Physics Asset.<br>	 This BodySetup is per instance because all modification of vertices is done in place |
| `bForceRefpose` | `bool` | Misc<br>	 <br>	 If true, force the mesh into the reference pose - is an optimization. |
| `bOnlyAllowAutonomousTickPose` | `uint32` | If true TickPose() will not be called from the Component's TickComponent function.<br>	 It will instead be called from Autonomous networking updates. See ACharacter. |
| `bIsAutonomousTickPose` | `uint32` | True if calling TickPose() from Autonomous networking updates. See ACharacter. |
| `bOldForceRefPose` | `uint32` | If bForceRefPose was set last tick. |
| `bShowPrePhysBones` | `uint32` | Bool that enables debug drawing of the skeleton before it is passed to the physics. Useful for debugging animation-driven physics. |
| `bRequiredBonesUpToDate` | `uint32` | If false, indicates that on the next call to UpdateSkelPose the RequiredBones array should be recalculated. |
| `bAnimTreeInitialised` | `uint32` | If true, AnimTree has been initialised. |
| `bIncludeComponentLocationIntoBounds` | `uint32` | If true, the Location of this Component will be included into its bounds calculation<br>	 (this can be useful when using SMU_OnlyTickPoseWhenRendered on a character that moves away from the root and no bones are left near the origin of the component) |
| `bEnableLineCheckWithBounds` | `uint32` | If true, line checks will test against the bounding box of this skeletal mesh component and return a hit if there is a collision. |
| `CachedAnimCurveUidVersion` | `uint16` | Cache AnimCurveUidVersion from Skeleton and this will be used to identify if it needs to be updated |
| `LineCheckBoundsScale` | `FVector` | If bEnableLineCheckWithBounds is true, scale the bounds by this value before doing line check. |
| `OnConstraintBroken` | `FConstraintBrokenSignature` | Notification when constraint is broken. |
| `SaveBoneSpaceTransfroms` | `TArray < FTransform >` | - |
| `ClothingSimulationFactory` | `TSubclassOf < UClothingSimulationFactory >` | Class of the object responsible for |
| `TeleportDistanceThreshold` | `float` | Conduct teleportation if the character's movement is greater than this threshold in 1 frame.<br>	 Zero or negative values will skip the check.<br>	 You can also do force teleport manually using ForceNextUpdateTeleport()  ForceNextUpdateTeleportAndReset(). |
| `TeleportRotationThreshold` | `float` | Rotation threshold in degrees, ranging from 0 to 180.<br>	 Conduct teleportation if the character's rotation is greater than this threshold in 1 frame.<br>	 Zero or negative values will skip the check. |
| `bEnableUpdateOverlapsEvent` | `uint8` | - |
| `bEnableAsyncAnimUpdate` | `bool` | ImmediatePhysics Evaluation End<br>	 <br>	 Whether to enable async anim update for this component |
| `SequenceToPlay_DEPRECATED` | `UAnimSequence *` | - |
| `AnimToPlay_DEPRECATED` | `UAnimationAsset *` | - |
| `bDefaultLooping_DEPRECATED` | `uint32` | - |
| `bDefaultPlaying_DEPRECATED` | `uint32` | - |
| `DefaultPosition_DEPRECATED` | `float` | - |
| `DefaultPlayRate_DEPRECATED` | `float` | - |
| `LastPoseTickFrame` | `uint32` | - |
| `LastPoseTickTime` | `float` | Keep track of when animation has been ticked to ensure it is ticked only once per frame. |
| `bNeedsQueuedAnimEventsDispatched` | `bool` | - |
| `bIsNeedUpdate` | `bool` | - |
| `bSkeletalMeshDirty` | `bool` | - |
| `BoneRetargetSource` | `FName` | - |
| `MeshShiftTransform` | `FTransform` | - |
| `MeshShiftRefBone` | `FName` | - |
| `MeshShiftAnchorRefBone` | `FName` | - |
| `bUseMeshShiftFeature` | `bool` | - |
| `bOnlyPartOfShiftRefBoneAsRoot` | `bool` | - |
| `MeshShiftCompensationType` | `EMeshShiftCompensationType` | - |
| `MeshShiftCompensationBaseSkelComp` | `TWeakObjectPtr < USkeletalMeshComponent >` | - |
| `AnimOverrideMeshShiftParam` | `FMeshShiftParam` | - |
| `DynamicBoneScaleFeature_Scale3D` | `FVector` | - |
| `DynamicBoneScaleFeature_BoneNameList` | `TArray < FName >` | - |
| `bUseDynamicBoneScaleFeature` | `bool` | - |
| `bIsOverrideScale` | `bool` | - |
| `bIsEnableBatchSection` | `bool` | For Dynamic Bone Scale Feature End |
| `BatchSectionList` | `TArray < FDynamicBatchSectionInfo >` | - |
| `OriginalMaterials` | `TArray < UMaterialInterface * >` | - |
| `AnimationBlueprint_DEPRECATED` | `UAnimBlueprint *` | The blueprint for creating an AnimationScript. |
| `bUpdateAnimationInEditor` | `uint32` | If true, this will Tick until disabled |
| `BoneRetargetBaseRefMesh` | `USkeletalMesh *` | For Bone Retarget Feature Start |

## Functions

### `SetAnimInstanceClass`

```text
SetAnimInstanceClass(NewClass: UClass *, bTickAnimationNow: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewClass` | `UClass *` | - |
| `bTickAnimationNow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CopyBoneSpaceTransfroms`

```text
CopyBoneSpaceTransfroms(InputTransforms: TArray < FTransform >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputTransforms` | `TArray < FTransform >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoneSpaceTransfromsForCopy`

```text
GetBoneSpaceTransfromsForCopy(Other: USkeletalMeshComponent *) -> TArray < FTransform >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Other` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < FTransform >` | - |

### `GetAnimInstance`

```text
GetAnimInstance() -> UAnimInstance *
```

Returns the animation instance that is driving the class (if available). This is typically an instance of
	  the class set as AnimBlueprintGeneratedClass (generated by an animation blueprint)
	  Since this instance is transient, it is not safe to be used during construction script

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `GetSubAnimInstances`

```text
GetSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `GetNewSubAnimInstances`

```text
GetNewSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `GetAllSubAnimInstances`

```text
GetAllSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `GetDirtySubAnimInstances`

```text
GetDirtySubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `GetStopTickSubAnimInstances`

```text
GetStopTickSubAnimInstances() -> TArray < UAnimInstance * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UAnimInstance * >` | - |

### `ClearDirtySubAnimInstances`

```text
ClearDirtySubAnimInstances() -> void
```

清理所有脏标记的SubAnimInstance
	  从SubInstances、NewSubInstances、StopTickSubInstances中移除，并调用UninitializeAnimation、PendingDestroy等清理逻辑

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddNewSubAnimInstance`

```text
AddNewSubAnimInstance(NewInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddDirtySubAnimInstance`

```text
AddDirtySubAnimInstance(NewInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddStopTickSubAnimInstance`

```text
AddStopTickSubAnimInstance(NewInstance: UAnimInstance *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInstance` | `UAnimInstance *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPostProcessInstance`

```text
GetPostProcessInstance() -> UAnimInstance *
```

Returns the active post process instance is one is available. This is set on the mesh that this
	  component is using, and is evaluated immediately after the main instance.

**Returns**

| Type | Description |
|---|---|
| `UAnimInstance *` | - |

### `SetAnimationMode`

```text
SetAnimationMode(InAnimationMode: EAnimationMode :: Type) -> void
```

Below are the interface to control animation when animation mode, not blueprint mode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimationMode` | `EAnimationMode :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAnimationMode`

```text
GetAnimationMode() -> EAnimationMode :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EAnimationMode :: Type` | - |

### `GetAnimationPosition`

```text
GetAnimationPosition(Animation: UAnimationAsset *) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UAnimationAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PlayAnimation`

```text
PlayAnimation(NewAnimToPlay: UAnimationAsset *, bLooping: bool) -> void
```

Animation play functions
	 
	  These changes status of animation instance, which is transient data, which means it won't serialize with this component
	  Because of that reason, it is not safe to be used during construction script
	  Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAnimToPlay` | `UAnimationAsset *` | - |
| `bLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnimation`

```text
SetAnimation(NewAnimToPlay: UAnimationAsset *) -> void
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAnimToPlay` | `UAnimationAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Play`

```text
Play(bLooping: bool) -> void
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetPosition`

```text
SetPosition(InPos: float, bFireNotifies: bool) -> void
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPos` | `float` | - |
| `bFireNotifies` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPosition`

```text
GetPosition() -> float
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetPlayRate`

```text
SetPlayRate(Rate: float) -> void
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlayRate`

```text
GetPlayRate() -> float
```

Animation play functions
	
	 These changes status of animation instance, which is transient data, which means it won't serialize with this component
	 Because of that reason, it is not safe to be used during construction script
	 Please use OverrideAnimationDatat for construction script. That will override AnimationData to be serialized

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `OverrideAnimationData`

```text
OverrideAnimationData(InAnimToPlay: UAnimationAsset *, bIsLooping: bool, bIsPlaying: bool, Position: float, PlayRate: float) -> void
```

This overrides current AnimationData parameter in the SkeletalMeshComponent. This will serialize when the component serialize
	  so it can be used during construction script. However note that this will override current existing data
	  This can be useful if you'd like to make a blueprint with custom default animation per component
	  This sets single player mode, which means you can't use AnimBlueprint with it

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimToPlay` | `UAnimationAsset *` | - |
| `bIsLooping` | `bool` | - |
| `bIsPlaying` | `bool` | - |
| `Position` | `float` | - |
| `PlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMorphTarget`

```text
SetMorphTarget(MorphTargetName: FName, Value: float, bRemoveZeroWeight: bool) -> void
```

Set Morph Target with Name and Value(0-1)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MorphTargetName` | `FName` | - |
| `Value` | `float` | - |
| `bRemoveZeroWeight` | `bool` | : Used by editor code when it should stay in the active list with zero weight |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMorphTargets`

```text
ClearMorphTargets() -> void
```

Clear all Morph Target that are set to this mesh

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMorphTarget`

```text
GetMorphTarget(MorphTargetName: FName) -> float
```

Get Morph target with given name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MorphTargetName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SnapshotPose`

```text
SnapshotPose(Snapshot: FPoseSnapshot &) -> void
```

Takes a snapshot of this skeletal mesh component's pose and saves it to the specified snapshot.
	  The snapshot is taken at the current LOD, so if for example you took the snapshot at LOD1
	  and then used it at LOD0 any bones not in LOD1 will use the reference pose

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Snapshot` | `FPoseSnapshot &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetClothMaxDistanceScale`

```text
GetClothMaxDistanceScale() -> float
```

GetSet the max distance scale of clothing mesh vertices

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetClothMaxDistanceScale`

```text
SetClothMaxDistanceScale(Scale: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Scale` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceClothNextUpdateTeleport`

```text
ForceClothNextUpdateTeleport() -> void
```

Used to indicate we should force 'teleport' during the next call to UpdateClothState,
	  This will transform positions and velocities and thus keep the simulation state, just translate it to a new pose.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceClothNextUpdateTeleportAndReset`

```text
ForceClothNextUpdateTeleportAndReset() -> void
```

Used to indicate we should force 'teleport and reset' during the next call to UpdateClothState.
	  This can be used to reset it from a bad state or by a teleport where the old state is not important anymore.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SuspendClothingSimulation`

```text
SuspendClothingSimulation() -> void
```

Stops simulating clothing, but does not show clothing ref pose. Keeps the last known simulation state

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumeClothingSimulation`

```text
ResumeClothingSimulation() -> void
```

Resumes a previously suspended clothing simulation, teleporting the clothing on the next tick

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsClothingSimulationSuspended`

```text
IsClothingSimulationSuspended() -> bool
```

Gets whether or not the clothing simulation is currently suspended

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ResetClothTeleportMode`

```text
ResetClothTeleportMode() -> void
```

Reset the teleport mode of a next update to 'Continuous'

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindClothToMasterPoseComponent`

```text
BindClothToMasterPoseComponent() -> void
```

If this component has a valid MasterPoseComponent then this function makes cloth items on the slave component
	  take the transforms of the cloth items on the master component instead of simulating separately.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindClothFromMasterPoseComponent`

```text
UnbindClothFromMasterPoseComponent(bRestoreSimulationSpace: bool) -> void
```

If this component has a valid MasterPoseComponent and has previously had its cloth bound to the
	  MCP, this function will unbind the cloth and resume simulation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bRestoreSimulationSpace` | `bool` | if true and the master pose cloth was originally simulating in world |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUpdateAnimationInEditor`

```text
SetUpdateAnimationInEditor(NewUpdateState: bool) -> void
```

Sets whether or not to force tick component in order to update animation and refresh transform for this component
	 This is supported only in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewUpdateState` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDisableAnimCurves`

```text
SetDisableAnimCurves(bInDisableAnimCurves: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInDisableAnimCurves` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDisableAnimCurves`

```text
GetDisableAnimCurves() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetAllowAnimCurveEvaluation`

```text
SetAllowAnimCurveEvaluation(bInAllow: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAllow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllowedAnimCurveEvaluate`

```text
GetAllowedAnimCurveEvaluate() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AllowAnimCurveEvaluation`

```text
AllowAnimCurveEvaluation(NameOfCurve: FName, bAllow: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NameOfCurve` | `FName` | - |
| `bAllow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllowedAnimCurveEvaluation`

```text
ResetAllowedAnimCurveEvaluation() -> void
```

By reset, it will allow all the curves to be evaluated

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllowedAnimCurvesEvaluation`

```text
SetAllowedAnimCurvesEvaluation(List: TArray < FName > &, bAllow: bool) -> void
```

resets, and then only allow the following list to be alloweddisallowed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `List` | `TArray < FName > &` | - |
| `bAllow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTeleportRotationThreshold`

```text
GetTeleportRotationThreshold() -> float
```

Gets the teleportation rotation threshold.

**Returns**

| Type | Description |
|---|---|
| `float` | Threshold in degrees. |

### `SetTeleportRotationThreshold`

```text
SetTeleportRotationThreshold(Threshold: float) -> void
```

Sets the teleportation rotation threshold.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Threshold` | `float` | Threshold in degrees. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTeleportDistanceThreshold`

```text
GetTeleportDistanceThreshold() -> float
```

Gets the teleportation distance threshold.

**Returns**

| Type | Description |
|---|---|
| `float` | Threshold value. |

### `SetTeleportDistanceThreshold`

```text
SetTeleportDistanceThreshold(Threshold: float) -> void
```

Sets the teleportation distance threshold.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Threshold` | `float` | Threshold value. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBodyNotifyRigidBodyCollision`

```text
SetBodyNotifyRigidBodyCollision(bNewNotifyRigidBodyCollision: bool, BoneName: FName) -> void
```

Changes the value of bNotifyRigidBodyCollision for a given body

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewNotifyRigidBodyCollision` | `bool` | The value to assign to bNotifyRigidBodyCollision |
| `BoneName` | `FName` | Name of the body to turn hit notifies onoff. None implies root body |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNotifyRigidBodyCollisionBelow`

```text
SetNotifyRigidBodyCollisionBelow(bNewNotifyRigidBodyCollision: bool, BoneName: FName, bIncludeSelf: bool) -> void
```

Changes the value of bNotifyRigidBodyCollision on all bodies below a given bone

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewNotifyRigidBodyCollision` | `bool` | The value to assign to bNotifyRigidBodyCollision |
| `BoneName` | `FName` | Name of the body to turn hit notifies on (and below) |
| `bIncludeSelf` | `bool` | Whether to modify the given body (useful for roots with multiple children) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableBodyGravity`

```text
SetEnableBodyGravity(bEnableGravity: bool, BoneName: FName) -> void
```

Enables or disables gravity for the given bone.
	 	NAME_None indicates the root body will be edited.
	 	If the bone name given is otherwise invalid, nothing happens.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableGravity` | `bool` | Whether gravity should be enabled or disabled. |
| `BoneName` | `FName` | The name of the bone to modify. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBodyGravityEnabled`

```text
IsBodyGravityEnabled(BoneName: FName) -> bool
```

Checks whether or not gravity is enabled on the given bone.
	 	NAME_None indicates the root body should be queried.
	 	If the bone name given is otherwise invalid, false is returned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | The name of the bone to check. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if gravity is enabled on the bone. |

### `SetEnableGravityOnAllBodiesBelow`

```text
SetEnableGravityOnAllBodiesBelow(bEnableGravity: bool, BoneName: FName, bIncludeSelf: bool) -> void
```

Enables or disables gravity to all bodies below the given bone.
	   NAME_None indicates all bodies will be edited.
		In that case, consider using UPrimitiveComponent::EnableGravity.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableGravity` | `bool` | Whether gravity should be enabled or disabled. |
| `BoneName` | `FName` | The name of the top most bone. |
| `bIncludeSelf` | `bool` | Whether the bone specified should be edited. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_GetClosestPointOnPhysicsAsset`

```text
K2_GetClosestPointOnPhysicsAsset(WorldPosition: FVector &, ClosestWorldPosition: FVector &, Normal: FVector &, BoneName: FName &, Distance: float &) -> bool
```

Given a world position, find the closest point on the physics asset. Note that this is independent of collision and welding. This is based purely on animation position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldPosition` | `FVector &` | The point we want the closest point to (i.e. for all bodies in the physics asset, find the one that has a point closest to WorldPosition) |
| `ClosestWorldPosition` | `FVector &` | - |
| `Normal` | `FVector &` | - |
| `BoneName` | `FName &` | - |
| `Distance` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if we found a closest point |

### `GetBoneMass`

```text
GetBoneMass(BoneName: FName, bScaleMass: bool) -> float
```

Returns the mass (in kg) of the given bone

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of the body to return. 'None' indicates root body. |
| `bScaleMass` | `bool` | If true, the mass is scaled by the bone's MassScale. |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetSkeletalCenterOfMass`

```text
GetSkeletalCenterOfMass() -> FVector
```

Returns the center of mass of the skeletal mesh, instead of the root body's location

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `AddForceToAllBodiesBelow`

```text
AddForceToAllBodiesBelow(Force: FVector, BoneName: FName, bAccelChange: bool, bIncludeSelf: bool) -> void
```

Add a force to all rigid bodies below.
	   This is like a 'thruster'. Good for adding a burst over some (non zero) time. Should be called every frame for the duration of the force.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Force` | `FVector` | Force vector to apply. Magnitude indicates strength of force. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply force to. 'None' indicates root body. |
| `bAccelChange` | `bool` | If true, Force is taken as a change in acceleration instead of a physical force (i.e. mass will have no affect). |
| `bIncludeSelf` | `bool` | If false, Force is only applied to bodies below but not given bone name. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddImpulseToAllBodiesBelow`

```text
AddImpulseToAllBodiesBelow(Impulse: FVector, BoneName: FName, bVelChange: bool, bIncludeSelf: bool) -> void
```

Add impulse to all single rigid bodies below. Good for one time instant burst.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | Magnitude and direction of impulse to apply. |
| `BoneName` | `FName` | If a SkeletalMeshComponent, name of body to apply impulse to. 'None' indicates root body. |
| `bVelChange` | `bool` | If true, the Strength is taken as a change in velocity instead of an impulse (ie. mass will have no affect). |
| `bIncludeSelf` | `bool` | If false, Force is only applied to bodies below but not given bone name. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsEnableAnimBoneStateDirtyFeature`

```text
IsEnableAnimBoneStateDirtyFeature() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetAllBodiesSimulatePhysics`

```text
SetAllBodiesSimulatePhysics(bNewSimulate: bool) -> void
```

Set bSimulatePhysics to true for all bone bodies. Does not change the component bSimulatePhysics flag.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewSimulate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPhysicsBlendWeight`

```text
SetPhysicsBlendWeight(PhysicsBlendWeight: float) -> void
```

This is global set up for setting physics blend weight
	  This does multiple things automatically
	  If PhysicsBlendWeight == 1.f, it will enable Simulation, and if PhysicsBlendWeight == 0.f, it will disable Simulation.
	  Also it will respect each body's setup, so if the body is fixed, it won't simulate. Vice versa
	  So if you'd like all bodies to change manually, do not use this function, but SetAllBodiesPhysicsBlendWeight

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PhysicsBlendWeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnablePhysicsBlending`

```text
SetEnablePhysicsBlending(bNewBlendPhysics: bool) -> void
```

Disable physics blending of bones

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewBlendPhysics` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllBodiesBelowSimulatePhysics`

```text
SetAllBodiesBelowSimulatePhysics(InBoneName: FName &, bNewSimulate: bool, bIncludeSelf: bool) -> void
```

Set all of the bones below passed in bone to be simulated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName &` | - |
| `bNewSimulate` | `bool` | - |
| `bIncludeSelf` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetAllBodiesSimulatePhysics`

```text
ResetAllBodiesSimulatePhysics() -> void
```

Allows you to reset bodies Simulate state based on where bUsePhysics is set to true in the BodySetup.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllBodiesPhysicsBlendWeight`

```text
SetAllBodiesPhysicsBlendWeight(PhysicsBlendWeight: float, bSkipCustomPhysicsType: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PhysicsBlendWeight` | `float` | - |
| `bSkipCustomPhysicsType` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllBodiesBelowPhysicsBlendWeight`

```text
SetAllBodiesBelowPhysicsBlendWeight(InBoneName: FName &, PhysicsBlendWeight: float, bSkipCustomPhysicsType: bool, bIncludeSelf: bool) -> void
```

Set all of the bones below passed in bone to be simulated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName &` | - |
| `PhysicsBlendWeight` | `float` | - |
| `bSkipCustomPhysicsType` | `bool` | - |
| `bIncludeSelf` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AccumulateAllBodiesBelowPhysicsBlendWeight`

```text
AccumulateAllBodiesBelowPhysicsBlendWeight(InBoneName: FName &, AddPhysicsBlendWeight: float, bSkipCustomPhysicsType: bool) -> void
```

Accumulate AddPhysicsBlendWeight to physics blendweight for all of the bones below passed in bone to be simulated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName &` | - |
| `AddPhysicsBlendWeight` | `float` | - |
| `bSkipCustomPhysicsType` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllMotorsAngularPositionDrive`

```text
SetAllMotorsAngularPositionDrive(bEnableSwingDrive: bool, bEnableTwistDrive: bool, bSkipCustomPhysicsType: bool) -> void
```

Enable or Disable AngularPositionDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSwingDrive` | `bool` | - |
| `bEnableTwistDrive` | `bool` | - |
| `bSkipCustomPhysicsType` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllMotorsAngularVelocityDrive`

```text
SetAllMotorsAngularVelocityDrive(bEnableSwingDrive: bool, bEnableTwistDrive: bool, bSkipCustomPhysicsType: bool) -> void
```

Enable or Disable AngularVelocityDrive. If motor is in SLERP mode it will be turned on if either EnableSwingDrive OR EnableTwistDrive are enabled. In Twist and Swing mode the twist and the swing can be controlled individually.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnableSwingDrive` | `bool` | - |
| `bEnableTwistDrive` | `bool` | - |
| `bSkipCustomPhysicsType` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllMotorsAngularDriveParams`

```text
SetAllMotorsAngularDriveParams(InSpring: float, InDamping: float, InForceLimit: float, bSkipCustomPhysicsType: bool) -> void
```

Set Angular Drive motors params for all constraint instances

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSpring` | `float` | - |
| `InDamping` | `float` | - |
| `InForceLimit` | `float` | - |
| `bSkipCustomPhysicsType` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintProfile`

```text
SetConstraintProfile(JointName: FName, ProfileName: FName, bDefaultIfNotFound: bool) -> void
```

Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset. If profile name is not found the joint is set to use the default constraint profile.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `JointName` | `FName` | - |
| `ProfileName` | `FName` | - |
| `bDefaultIfNotFound` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConstraintProfileForAll`

```text
SetConstraintProfileForAll(ProfileName: FName, bDefaultIfNotFound: bool) -> void
```

Sets the constraint profile properties (limits, motors, etc...) to match the constraint profile as defined in the physics asset for all constraints. If profile name is not found the joint is set to use the default constraint profile.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProfileName` | `FName` | - |
| `bDefaultIfNotFound` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindConstraintBoneName`

```text
FindConstraintBoneName(ConstraintIndex: int32) -> FName
```

Find Constraint Name from index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConstraintIndex` | `int32` | Index of constraint to look for |

**Returns**

| Type | Description |
|---|---|
| `FName` | Constraint Joint Name |

### `BreakConstraint`

```text
BreakConstraint(Impulse: FVector, HitLocation: FVector, InBoneName: FName) -> void
```

Break a constraint off a Gore mesh.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impulse` | `FVector` | vector of impulse |
| `HitLocation` | `FVector` | location of the hit |
| `InBoneName` | `FName` | Name of bone to break constraint for |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAngularLimits`

```text
SetAngularLimits(InBoneName: FName, Swing1LimitAngle: float, TwistLimitAngle: float, Swing2LimitAngle: float) -> void
```

Sets the Angular Motion Ranges for a named bone

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName` | Name of bone to adjust constraint ranges for |
| `Swing1LimitAngle` | `float` | Size of limit in degrees, 0 means locked, 180 means free |
| `TwistLimitAngle` | `float` | Size of limit in degrees, 0 means locked, 180 means free |
| `Swing2LimitAngle` | `float` | Size of limit in degrees, 0 means locked, 180 means free |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentJointAngles`

```text
GetCurrentJointAngles(InBoneName: FName, Swing1Angle: float &, TwistAngle: float &, Swing2Angle: float &) -> void
```

Gets the current Angular state for a named bone constraint

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoneName` | `FName` | Name of bone to get constraint ranges for |
| `Swing1Angle` | `float &` | current angular state of the constraint |
| `TwistAngle` | `float &` | current angular state of the constraint |
| `Swing2Angle` | `float &` | current angular state of the constraint |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleExistingParallelEvaluationTask`

```text
HandleExistingParallelEvaluationTask(bBlockOnTask: bool, bPerformPostAnimEvaluation: bool, bBlockOnAsyncAnimUpdateTasks: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bBlockOnTask` | `bool` | - |
| `bPerformPostAnimEvaluation` | `bool` | - |
| `bBlockOnAsyncAnimUpdateTasks` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `HandleExistingParallelIMPhysicsEvaluationTask`

```text
HandleExistingParallelIMPhysicsEvaluationTask(bBlockOnTask: bool) -> bool
```

ImmediatePhysics Evaluation Start

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bBlockOnTask` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetLastPoseTickFrame_BP`

```text
GetLastPoseTickFrame_BP() -> int64
```

Checked whether we have already ticked the pose this frame

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `SetNeedUpdateChildTransformsOnFinalizeAnimationUpdate`

```text
SetNeedUpdateChildTransformsOnFinalizeAnimationUpdate(bUpdate: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUpdate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseIMSimulation`

```text
PauseIMSimulation(InPauseFrameCount: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPauseFrameCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MarkMeshShiftFeature`

```text
MarkMeshShiftFeature(InIsUseShiftFeature: bool, InIsOnlyPartOfShiftRefBoneAsRoot: bool, InShiftTransform: FTransform &, InShiftRefBone: FName, InAnchorRefBone: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsUseShiftFeature` | `bool` | - |
| `InIsOnlyPartOfShiftRefBoneAsRoot` | `bool` | - |
| `InShiftTransform` | `FTransform &` | - |
| `InShiftRefBone` | `FName` | - |
| `InAnchorRefBone` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MarkMeshShiftCompensation`

```text
MarkMeshShiftCompensation(InMeshShiftCompensationType: EMeshShiftCompensationType, InCompensationBaseSkelComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMeshShiftCompensationType` | `EMeshShiftCompensationType` | - |
| `InCompensationBaseSkelComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AnimOverrideMeshShiftParam_Start`

```text
AnimOverrideMeshShiftParam_Start(InAnimMeshShiftParam: FMeshShiftParam &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimMeshShiftParam` | `FMeshShiftParam &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AnimOverrideMeshShiftParam_Stop`

```text
AnimOverrideMeshShiftParam_Stop(InAnimMeshShiftParam: FMeshShiftParam &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimMeshShiftParam` | `FMeshShiftParam &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetRawCurveValue`

```text
GetRawCurveValue(InCurveName: FName &) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCurveName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRetargetBoneRelativeTMInBaseRefPose`

```text
GetRetargetBoneRelativeTMInBaseRefPose(InTargetBoneName: FName &) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetBoneName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `SingleNodeInstance_ActiveBoneRetargetFeature`

```text
SingleNodeInstance_ActiveBoneRetargetFeature(InIsActive: bool, InTargetSkelComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsActive` | `bool` | - |
| `InTargetSkelComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SingleNodeInstance_OverrideBoneRetargetParam`

```text
SingleNodeInstance_OverrideBoneRetargetParam(InIsUseRetargetFeature: bool, InIsConsiderMasterPoseRetarget: bool, InIsForeceUseBaseSkeletonAsRetargetSource: bool, InTargetSkelComp: USkeletalMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsUseRetargetFeature` | `bool` | - |
| `InIsConsiderMasterPoseRetarget` | `bool` | - |
| `InIsForeceUseBaseSkeletonAsRetargetSource` | `bool` | - |
| `InTargetSkelComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInitAnimTickDelay`

```text
IsInitAnimTickDelay() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsInitRefreshPoseDelay`

```text
IsInitRefreshPoseDelay() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DelayInitAnimTick`

```text
DelayInitAnimTick(InInitAnimTickParam: FDelayInitAnimTickParam &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInitAnimTickParam` | `FDelayInitAnimTickParam &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DelayInitRefreshPose`

```text
DelayInitRefreshPose() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PerformDelayedInitAnimTick`

```text
PerformDelayedInitAnimTick() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PerformDelayedInitRefreshPose`

```text
PerformDelayedInitRefreshPose() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MarkDynamicBoneScaleFeature`

```text
MarkDynamicBoneScaleFeature(InIsUseDynamicBoneScaleFeature: bool, InIsOverrideScale: bool, InTargetBoneNameList: TArray < FName > &, InDynamicScale3D: FVector &) -> void
```

For Bone Retarget Feature End 
	 
	
	  For Dynamic Bone Scale Feature Start

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsUseDynamicBoneScaleFeature` | `bool` | - |
| `InIsOverrideScale` | `bool` | - |
| `InTargetBoneNameList` | `TArray < FName > &` | - |
| `InDynamicScale3D` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSectionBatched`

```text
IsSectionBatched(LODIndex: int32) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BatchSectionsWithAtlas`

```text
BatchSectionsWithAtlas(LODIdx: int32, IsBatchSection: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIdx` | `int32` | - |
| `IsBatchSection` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AutoBatchSection`

```text
AutoBatchSection(LODIdx: int32, BatchIndices: TArray < int32 >, IsBatchSection: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIdx` | `int32` | - |
| `BatchIndices` | `TArray < int32 >` | - |
| `IsBatchSection` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearInterpolateBoneCache`

```text
ClearInterpolateBoneCache(DurationTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DurationTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnAnimInitialized`

```text
OnAnimInitialized() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPreAnimClearScriptInstance`

```text
OnPreAnimClearScriptInstance() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCompletePostAnimationEvaluationEnd`

```text
OnCompletePostAnimationEvaluationEnd() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DynamicMulticastDelegate_OnFinalizeBoneTransform`

```text
DynamicMulticastDelegate_OnFinalizeBoneTransform(InTargetSkelComp: USkeletalMeshComponent*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTargetSkelComp` | `USkeletalMeshComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnSkeletalUpdateOverlapsEvent`

```text
OnSkeletalUpdateOverlapsEvent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMeshLODChangeDelegate`

```text
OnMeshLODChangeDelegate(InCurLOD: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCurLOD` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkeletalMeshReductionSettings.json -->

# USkeletalMeshReductionSettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `TArray < FSkeletalMeshLODGroupSettings >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkeletalMeshSocket.json -->

# USkeletalMeshSocket

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SocketName` | `FName` | Defines a named attachment location on the USkeletalMesh. <br>	 	These are set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent.<br>	 	The Outer of a SkeletalMeshSocket should always be the USkeletalMesh. |
| `BoneName` | `FName` | - |
| `RelativeLocation` | `FVector` | - |
| `RelativeRotation` | `FRotator` | - |
| `RelativeScale` | `FVector` | - |
| `BaseLocation` | `FVector` | - |
| `BaseRotation` | `FRotator` | - |
| `BaseScale` | `FVector` | - |
| `bDynamicCreate` | `bool` | - |
| `RelativeBoneName` | `FName` | - |
| `bForceAlwaysAnimated` | `bool` | If true then the hierarchy of bones this socket is attached to will always be <br>	    evaluated, even if it had previously been removed due to the current lod setting |

## Functions

### `GetSocketLocation`

```text
GetSocketLocation(SkelComp: USkeletalMeshComponent *) -> ENGINE_API FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkelComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | - |

### `InitializeSocketFromLocation`

```text
InitializeSocketFromLocation(SkelComp: USkeletalMeshComponent *, WorldLocation: FVector, WorldNormal: FVector) -> ENGINE_API void
```

Sets BoneName, RelativeLocation and RelativeRotation based on closest bone to WorldLocation and WorldNormal

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkelComp` | `USkeletalMeshComponent *` | - |
| `WorldLocation` | `FVector` | - |
| `WorldNormal` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkeleton.json -->

# USkeleton

USkeleton : that links between mesh and animation
 		- Bone hierarchy for animations
 		- Bonetrack linkup between mesh and animation
 		- Retargetting related
 		- Mirror table

## Inheritance

`UObject` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoneTree` | `TArray < struct FBoneNode >` | Skeleton bone tree - each contains name and parent index |
| `OverrideBoneTranslationRetargetingModeConfigMap` | `TMap < FName , FOverrideBoneTranslationRetargetingModeConfig >` | - |
| `RefLocalPoses_DEPRECATED` | `TArray < FTransform >` | Reference skeleton poses in local space |
| `VirtualBoneGuid` | `FGuid` | Guid for virtual bones.<br>	   Separate so that we don't have to dirty the original guid when only changing virtual bones |
| `VirtualBones` | `TArray < FVirtualBone >` | Array of this skeletons virtual bones. These are new bones are links between two existing bones<br>	  and are baked into all the skeletons animations |
| `CompatibleSkeletons` | `TArray < TSoftObjectPtr < USkeleton > >` | The list of compatible skeletons.<br>	  This is an array of TSoftObjectPtr in order to prevent all skeletons to be loaded, as we only want to load things on demand.<br>	  As this is EditAnywhere and an array of TSoftObjectPtr, checking validity of pointers is needed. |
| `MultiSkeletonNameMap` | `TMap < TSoftObjectPtr < USkeleton > , FCustomSkeletonName >` | - |
| `CustomSkeletonNameMap` | `TMap < FName , FName >` | key名称对应其他骨骼的名字 做骨骼兼容时 会被当作本骨骼的value使用 |
| `SkeletonNotOffsetName` | `TMap < FName , FBoneOffset >` | 是否要在骨骼兼容后不应用offset |
| `RefBoneNames` | `TArray < FName >` | 该名称对应的骨骼 做骨骼兼容时 只会应用旋转 |
| `ExcludeBoneInfos` | `TArray < FSkinWeightInfoForFPP >` | 该名称对应的骨骼 做骨骼兼容时排除该骨骼的信息 |
| `ExcludeBoneNameForAvatar` | `TArray < FName >` | - |
| `bIsFPPSkeleton` | `bool` | - |
| `Sockets` | `TArray < USkeletalMeshSocket * >` | Array of named socket locations, set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent. |
| `SmartNames` | `FSmartNameContainer` | - |
| `BlendProfiles` | `TArray < UBlendProfile * >` | List of blend profiles available in this skeleton |
| `SlotGroups` | `TArray < FAnimSlotGroup >` | Slot Groups |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `bSkipGenerateGuidWhenSkeletonHierarchyAdd` | `bool` | 当骨架增加骨骼时，跳过 Guid 更新和 DDC 重新构建 |
| `PreviewSkeletalMesh` | `TSoftObjectPtr < USkeletalMesh >` | The default skeletal mesh to use when previewing this skeleton |
| `AdditionalPreviewSkeletalMeshes` | `TSoftObjectPtr < UDataAsset >` | The additional skeletal meshes to use when previewing this skeleton |
| `RigConfig` | `FRigConfiguration` | - |
| `AnimationNotifies` | `TArray < FName >` | AnimNotifiers that has been created. Right now there is no delete step for this, but in the future we'll supply delete |
| `PreviewAttachedAssetContainer` | `FPreviewAssetAttachContainer` | Attached assets component for this skeleton |

## Functions

### `AddCompatibleSkeleton`

```text
AddCompatibleSkeleton(SourceSkeleton: USkeleton *) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceSkeleton` | `USkeleton *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `AddCompatibleSkeletonSoft`

```text
AddCompatibleSkeletonSoft(SourceSkeleton: TSoftObjectPtr < USkeleton > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceSkeleton` | `TSoftObjectPtr < USkeleton > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkinnedMeshComponent.json -->

# USkinnedMeshComponent

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SkeletalMesh` | `USkeletalMesh *` | The skeletal mesh used by this component. |
| `MasterPoseComponent` | `TWeakObjectPtr < USkinnedMeshComponent >` | If set, this SkeletalMeshComponent will not use its SpaceBase for bone transform, but will<br>	 	use the component space transforms from the MasterPoseComponent. This is used when constructing a character using multiple skeletal meshes sharing the same<br>	 	skeleton within the same Actor. |
| `ComponentSpaceBoneExtraTransform` | `TArray < FTransform >` | - |
| `bUseBoundsFromMasterPoseComponent` | `uint32` | When true, we will just using the bounds from our MasterPoseComponent.  This is useful for when we have a Mesh Parented<br>	  to the main SkelMesh (e.g. outline mesh or a full body overdraw effect that is toggled) that is always going to be the same<br>	  bounds as parent.  We want to do no calculations in that case. |
| `PhysicsAssetOverride` | `UPhysicsAsset *` | PhysicsAsset is set in SkeletalMesh by default, but you can override with this value |
| `bOverrideMinLod` | `uint8` | Whether we should use the min lod specified in MinLodModel for this component instead of the min lod in the mesh |
| `ForcedLodModel` | `int32` | If 0, auto-select LOD level. if >0, force to (ForcedLodModel-1). |
| `MinLodModel` | `int32` | This is the min LOD that this component will use.  (e.g. if set to 2 then only 2+ LOD Models will be used.) This is useful to set on<br>	  meshes which are known to be a certain distance away and still want to have better LODs when zoomed in on them. |
| `MaxLodModel` | `int32` | - |
| `LODDynamicMask` | `TArray < bool >` | - |
| `LODInfo` | `TArray < struct FSkelMeshComponentLODInfo >` | LOD array info. Each index will correspond to the LOD index |
| `StreamingDistanceMultiplier` | `float` | Allows adjusting the desired streaming distance of streaming textures that uses UV 0.<br>	  1.0 is the default, whereas a higher value makes the textures stream in sooner from far away.<br>	  A lower value (0.0-1.0) makes the textures stream in later (you have to be closer).<br>	  Value can be < 0 (from legcay content, or code changes) |
| `WireframeColor` | `FColor` | Wireframe color |
| `bForceWireframe` | `uint32` | Forces the mesh to draw in wireframe mode. |
| `bDisplayBones_DEPRECATED` | `uint32` | Draw the skeleton hierarchy for this skel mesh. |
| `bDisableMorphTarget` | `uint32` | Disable Morphtarget for this component. |
| `bHideSkin` | `uint32` | Don't bother rendering the skin. |
| `bPerBoneMotionBlur` | `uint32` | If true, use per-bone motion blur on this skeletal mesh (requires additional rendering, can be disabled to save performance). |
| `UpdateBoundsRate` | `uint8` | - |
| `bComponentUseFixedSkelBounds` | `uint32` | When true, skip using the physics asset etc. and always use the fixed bounds defined in the SkeletalMesh. |
| `bConsiderAllBodiesForBounds` | `uint32` | If true, when updating bounds from a PhysicsAsset, consider _all_ BodySetups, not just those flagged with bConsiderForBounds. |
| `bFixCachedLocalBoundsIssue` | `uint32` | If true, cache correct local bounds. Otherwise cache a bounds transformed twice. See USkeletalMeshComponent::CalcBounds() --lyonarzhang |
| `MeshComponentUpdateFlag` | `TEnumAsByte < EMeshComponentUpdateFlag :: Type >` | This is update frequency flag even when our Owner has not been rendered recently |
| `NeedUpdateEveryFrame` | `bool` | - |
| `NeedRateTickWhenNoRender` | `bool` | - |
| `bIndirectLightingCachePositionUsingActorPosition` | `uint32` | If true, IndirectLightingCache will use actor postion to sample |
| `bForceMeshObjectUpdate` | `uint32` | If true, UpdateTransform will always result in a call to MeshObject->Update. |
| `bCanHighlightSelectedSections` | `uint32` | Whether or not we can highlight selected sections - this should really only be done in the editor |
| `bRecentlyRendered` | `uint32` | true if mesh has been recently rendered, false otherwise |
| `bAnimOptimizationBasedOnMaxDistanceFactor` | `bool` | - |
| `CustomSortAlternateIndexMode` | `uint8` | Editor only. Used for manually selecting the alternate indices for<br>	   TRISORT_CustomLeftRight sections. |
| `bCastCapsuleDirectShadow` | `uint32` | Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for direct shadowing from lights.<br>	  This type of shadowing is approximate but handles extremely wide area shadowing well.  The softness of the shadow depends on the light's LightSourceAngle  SourceRadius.<br>	  This flag will force bCastInsetShadow to be enabled. |
| `bCastCapsuleIndirectShadow` | `uint32` | Whether to use the capsule representation (when present) from a skeletal mesh's ShadowPhysicsAsset for shadowing indirect lighting (from lightmaps or skylight). |
| `CapsuleIndirectShadowMinVisibility` | `float` | Controls how dark the capsule indirect shadow can be. |
| `bCPUSkinning` | `uint32` | Whether or not to CPU skin this component, requires render data refresh after changing |
| `CachedLocalBounds` | `FBoxSphereBounds` | LocalBounds cached, so they're computed just once. |
| `bCachedLocalBoundsUpToDate` | `bool` | true when CachedLocalBounds is up to date. |
| `bEnableUpdateRateOptimizations` | `bool` | if TRUE, Owner will determine how often animation will be updated and evaluated. See AnimUpdateRateTick()<br>	  This allows to skip frames for performance. (For example based on visibility and size on screen). |
| `bDisplayDebugUpdateRateOptimizations` | `bool` | Enable on screen debugging of update rate optimization.<br>	  Red = Skipping 0 frames, Green = skipping 1 frame, Blue = skipping 2 frames, black = skipping more than 2 frames.<br>	  @todo: turn this into a console command. |
| `bRenderStatic` | `uint8` | If true, render as static in reference pose. |
| `bUseBoneVisibilityPropagateFeature` | `bool` | Engine modify Start +++++++++ |
| `bOverrideAnimUpdateRateParameters` | `bool` | - |
| `bOverrideAnimUpdateRateParameters_ByComponent` | `bool` | - |
| `bRunWithOverrideAnimUpdateRateParameters` | `bool` | - |
| `CustomAnimUpdateRateParams` | `FAnimUpdateRateParameters` | - |

## Functions

### `SetPhysicsAsset`

```text
SetPhysicsAsset(NewPhysicsAsset: UPhysicsAsset *, bForceReInit: bool) -> void
```

Override the Physics Asset of the mesh. It uses SkeletalMesh.PhysicsAsset, but if you'd like to override use this function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPhysicsAsset` | `UPhysicsAsset *` | New PhysicsAsset |
| `bForceReInit` | `bool` | Force reinitialize |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumLODs`

```text
GetNumLODs() -> int32
```

Get the number of LODs on this component

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetMinLOD`

```text
SetMinLOD(InNewMinLOD: int32) -> void
```

Set MinLodModel of the mesh component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewMinLOD` | `int32` | Set new MinLodModel that make sure the LOD does not go below of this value. Range from [0, Max Number of LOD - 1]. This will affect in the next tick update. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForcedLOD`

```text
SetForcedLOD(InNewForcedLOD: int32) -> void
```

Set MinLodModel of the mesh component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewForcedLOD` | `int32` | Set new ForcedLODModel that forces to set the incoming LOD. Range from [1, Max Number of LOD]. This will affect in the next tick update. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastCapsuleDirectShadow`

```text
SetCastCapsuleDirectShadow(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastCapsuleIndirectShadow`

```text
SetCastCapsuleIndirectShadow(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCapsuleIndirectShadowMinVisibility`

```text
SetCapsuleIndirectShadowMinVisibility(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumBones`

```text
GetNumBones() -> int32
```

Returns the number of bones in the skeleton.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetBoneIndex`

```text
GetBoneIndex(BoneName: FName) -> int32
```

Find the index of bone by name. Looks in the current SkeletalMesh being used by this SkeletalMeshComponent.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of bone to look up |

**Returns**

| Type | Description |
|---|---|
| `int32` | Index of the named bone in the current SkeletalMesh. Will return INDEX_NONE if bone not found. |

### `GetBoneName`

```text
GetBoneName(BoneIndex: int32) -> FName
```

Get Bone Name from index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneIndex` | `int32` | Index of the bone |

**Returns**

| Type | Description |
|---|---|
| `FName` | the name of the bone at the specified index |

### `GetSocketBoneName`

```text
GetSocketBoneName(InSocketName: FName) -> FName
```

Returns bone name linked to a given named socket on the skeletal mesh component.
	  If you're unsure to deal with sockets or bones names, you can use this function to filter through, and always return the bone name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSocketName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | bone name |

### `SetSkeletalMesh`

```text
SetSkeletalMesh(NewMesh: USkeletalMesh *, bReinitPose: bool, bCheckBoneMap: bool, bTickAnimationNow: bool) -> void
```

Change the SkeletalMesh that is rendered for this Component. Will re-initialize the animation tree etc.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMesh` | `USkeletalMesh *` | New mesh to set for this component |
| `bReinitPose` | `bool` | Whether we should keep current pose or reinitialize. |
| `bCheckBoneMap` | `bool` | - |
| `bTickAnimationNow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSkeletalMesh`

```text
GetSkeletalMesh() -> USkeletalMesh *
```

Return SkeletalMesh.

**Returns**

| Type | Description |
|---|---|
| `USkeletalMesh *` | - |

### `GetParentBone`

```text
GetParentBone(BoneName: FName) -> FName
```

Get Parent Bone of the input bone

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of the bone |

**Returns**

| Type | Description |
|---|---|
| `FName` | the name of the parent bone for the specified bone. Returns 'None' if the bone does not exist or it is the root bone |

### `ClearBoneExtraOffset`

```text
ClearBoneExtraOffset() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OffsetBoneExtraOffsprings`

```text
OffsetBoneExtraOffsprings(InputBoneName: FName, InputTranslation: FVector) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputBoneName` | `FName` | - |
| `InputTranslation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RotateBoneExtraOffsprings`

```text
RotateBoneExtraOffsprings(InputBoneName: FName, InputRotation: FRotator) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputBoneName` | `FName` | - |
| `InputRotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `ScaleBoneExtraOffsprings`

```text
ScaleBoneExtraOffsprings(InputBoneName: FName, InputScale: FVector) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InputBoneName` | `FName` | - |
| `InputScale` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetVertexColorOverride_LinearColor`

```text
SetVertexColorOverride_LinearColor(LODIndex: int32, VertexColors: TArray < FLinearColor > &) -> void
```

Allow override of vertex colors on a per-component basis, taking array of Blueprint-friendly LinearColors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIndex` | `int32` | - |
| `VertexColors` | `TArray < FLinearColor > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearVertexColorOverride`

```text
ClearVertexColorOverride(LODIndex: int32) -> void
```

Clear any applied vertex color override

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSkinWeightOverride`

```text
SetSkinWeightOverride(LODIndex: int32, SkinWeights: TArray < FSkelMeshSkinWeightInfo > &) -> void
```

Allow override of skin weights on a per-component basis.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIndex` | `int32` | - |
| `SkinWeights` | `TArray < FSkelMeshSkinWeightInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSkinWeightOverride`

```text
ClearSkinWeightOverride(LODIndex: int32) -> void
```

Clear any applied skin weight override

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSkinWeightProfile`

```text
SetSkinWeightProfile(InProfileName: FName) -> bool
```

Setup an override Skin Weight Profile for this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InProfileName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearSkinWeightProfile`

```text
ClearSkinWeightProfile() -> void
```

Clear the Skin Weight Profile from this component, in case it is set

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UpdateSkinWeightForRemapping`

```text
UpdateSkinWeightForRemapping(WeightInfo: FSkinWeightInfoForFPP) -> void
```

Update Skin weight for remapping skeleton

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WeightInfo` | `FSkinWeightInfoForFPP` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnloadSkinWeightProfile`

```text
UnloadSkinWeightProfile(InProfileName: FName) -> void
```

Unload a Skin Weight Profile's skin weight buffer (if created)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InProfileName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasSkinweightProfileByName`

```text
HasSkinweightProfileByName(InProfileName: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InProfileName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetCurrentSkinWeightProfileName`

```text
GetCurrentSkinWeightProfileName() -> FName
```

Return the name of the Skin Weight Profile that is currently set otherwise returns 'None'

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `IsUsingSkinWeightProfile`

```text
IsUsingSkinWeightProfile() -> bool
```

Check whether or not a Skin Weight Profile is currently set

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SwitchToOverrideSkinWeights`

```text
SwitchToOverrideSkinWeights(LODIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvalidateCachedBounds`

```text
InvalidateCachedBounds() -> void
```

Invalidate Cached Bounds, when Mesh Component has been updated.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshUpdateRateParams`

```text
RefreshUpdateRateParams() -> void
```

Recreates update rate params and internal tracker data

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshUpdateRateParamsEnsureTrackerOrder`

```text
RefreshUpdateRateParamsEnsureTrackerOrder() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMasterPoseComponent`

```text
SetMasterPoseComponent(NewMasterBoneComponent: USkinnedMeshComponent *, bForceUpdate: bool) -> void
```

Set MasterPoseComponent for this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMasterBoneComponent` | `USkinnedMeshComponent *` | New MasterPoseComponent |
| `bForceUpdate` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveMasterPoseComponent`

```text
RemoveMasterPoseComponent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TryRemoveDirtySlaveComponent`

```text
TryRemoveDirtySlaveComponent(DirtySlaveMeshComponent: USkinnedMeshComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DirtySlaveMeshComponent` | `USkinnedMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoneTransform`

```text
GetBoneTransform(BoneIndex: int32) -> FTransform
```

Get Bone Transform from index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneIndex` | `int32` | Index of the bone |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | the transform of the bone at the specified index |

### `GetBoneLocation`

```text
GetBoneLocation(BoneName: FName, Space: EBoneSpaces :: Type) -> FVector
```

Get Bone Location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of the bone |
| `Space` | `EBoneSpaces :: Type` | 0 == World, 1 == Local (Component) |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector of the bone |

### `BoneIsChildOf`

```text
BoneIsChildOf(BoneName: FName, ParentBoneName: FName) -> bool
```

Tests if BoneName is child of (or equal to) ParentBoneName.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of the bone |
| `ParentBoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if child (strictly, not same). false otherwise |

### `TransformToBoneSpace`

```text
TransformToBoneSpace(BoneName: FName, InPosition: FVector, InRotation: FRotator, OutPosition: FVector &, OutRotation: FRotator &) -> void
```

Transform a locationrotation from world space to bone relative space.
	 	This is handy if you know the location in world space for a bone attachment, as AttachComponent takes locationrotation in bone-relative space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of bone |
| `InPosition` | `FVector` | Input position |
| `InRotation` | `FRotator` | Input rotation |
| `OutPosition` | `FVector &` | (out) Transformed position |
| `OutRotation` | `FRotator &` | (out) Transformed rotation |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `TransformFromBoneSpace`

```text
TransformFromBoneSpace(BoneName: FName, InPosition: FVector, InRotation: FRotator, OutPosition: FVector &, OutRotation: FRotator &) -> void
```

Transform a locationrotation in bone relative space to world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of bone |
| `InPosition` | `FVector` | Input position |
| `InRotation` | `FRotator` | Input rotation |
| `OutPosition` | `FVector &` | (out) Transformed position |
| `OutRotation` | `FRotator &` | (out) Transformed rotation |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindClosestBone_K2`

```text
FindClosestBone_K2(TestLocation: FVector, BoneLocation: FVector &, IgnoreScale: float, bRequirePhysicsAsset: bool) -> FName
```

finds the closest bone to the given location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TestLocation` | `FVector` | the location to test against |
| `BoneLocation` | `FVector &` | (optional, out) if specified, set to the world space location of the bone that was found, or (0,0,0) if no bone was found |
| `IgnoreScale` | `float` | (optional) if specified, only bones with scaling larger than the specified factor are considered |
| `bRequirePhysicsAsset` | `bool` | (optional) if true, only bones with physics will be considered |

**Returns**

| Type | Description |
|---|---|
| `FName` | the name of the bone that was found, or 'None' if no bone was found |

### `HideBoneByName`

```text
HideBoneByName(BoneName: FName, PhysBodyOption: EPhysBodyOp) -> void
```

Hides the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
	 	Compoared to HideBone By Index - This keeps track of list of bones and update when LOD changes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of bone to hide |
| `PhysBodyOption` | `EPhysBodyOp` | Option for physics bodies that attach to the bones to be hidden |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnHideBoneByName`

```text
UnHideBoneByName(BoneName: FName) -> void
```

UnHide the specified bone with name.  Currently this just enforces a scale of 0 for the hidden bones.
	 	Compoared to HideBone By Index - This keeps track of list of bones and update when LOD changes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of bone to unhide |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsBoneHiddenByName`

```text
IsBoneHiddenByName(BoneName: FName) -> bool
```

Determines if the specified bone is hidden.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneName` | `FName` | Name of bone to check |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if hidden |

### `PropagateBoneHidden`

```text
PropagateBoneHidden(BoneIndex: int32, PhysBodyOption: EPhysBodyOp) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneIndex` | `int32` | - |
| `PhysBodyOption` | `EPhysBodyOp` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PropagateBoneUnHidden`

```text
PropagateBoneUnHidden(BoneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BoneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FollowBoneHidden`

```text
FollowBoneHidden(InHiddenLeaderComp: USkinnedMeshComponent *, BoneName: FName, PhysBodyOption: EPhysBodyOp) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHiddenLeaderComp` | `USkinnedMeshComponent *` | - |
| `BoneName` | `FName` | - |
| `PhysBodyOption` | `EPhysBodyOp` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FollowBoneUnHidden`

```text
FollowBoneUnHidden(InUnHiddenLeaderComp: USkinnedMeshComponent *, BoneName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUnHiddenLeaderComp` | `USkinnedMeshComponent *` | - |
| `BoneName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClipPlane`

```text
EnableMeshClipPlane(ClipPlane: FPlane &, PlaneIndex: int32) -> void
```

Engine modify End -----------

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipPlane`

```text
DisableMeshClipPlane(PlaneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClipArc`

```text
EnableMeshClipArc(ClipPlane: FPlane &, ClipSphere: FVector4 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `ClipSphere` | `FVector4 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipArc`

```text
DisableMeshClipArc() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClip4Planes`

```text
EnableMeshClip4Planes(ClipPlanes: TArray < FPlane > &, bBox: bool) -> void
```

Num of ClipPlanes is 4
	  0: Top Plane
	  1: Down Plane
	  2: Left Plane
	  3: Right Plane

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlanes` | `TArray < FPlane > &` | - |
| `bBox` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClip4Planes`

```text
DisableMeshClip4Planes() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderStatic`

```text
SetRenderStatic(bNewValue: bool) -> void
```

Set whether this skinned mesh should be rendered as static mesh in a reference pose

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSectionBatched`

```text
IsSectionBatched(LODIndex: int32) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LODIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USkyLightComponent.json -->

# USkyLightComponent

## Inheritance

`ULightComponentBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceType` | `TEnumAsByte < enum ESkyLightSourceType >` | Indicates where to get the light contribution from. |
| `Cubemap` | `UTextureCube *` | Cubemap to use for sky lighting if SourceType is set to SLS_SpecifiedCubemap. |
| `SourceCubemapAngle` | `float` | Angle to rotate the source cubemap when SourceType is set to SLS_SpecifiedCubemap. |
| `CubemapResolution` | `int32` | Maximum resolution for the very top processed cubemap mip. Must be a power of 2. |
| `SkyDistanceThreshold` | `float` | Distance from the sky light at which any geometry should be treated as part of the sky.<br>	  This is also used by reflection captures, so update reflection captures to see the impact. |
| `bCaptureEmissiveOnly` | `bool` | Only capture emissive materials. Skips all lighting making the capture cheaper. Recomended when using CaptureEveryFrame |
| `bLowerHemisphereIsBlack` | `bool` | Whether all distant lighting from the lower hemisphere should be set to LowerHemisphereColor.<br>	  Enabling this is accurate when lighting a scene on a planet where the ground blocks the sky,<br>	  However disabling it can be useful to approximate skylight bounce lighting (eg Movable light). |
| `LowerHemisphereColor` | `FLinearColor` | - |
| `OcclusionMaxDistance` | `float` | Max distance that the occlusion of one point will affect another.<br>	  Higher values increase the cost of Distance Field AO exponentially. |
| `Contrast` | `float` | Contrast S-curve applied to the computed AO.  A value of 0 means no contrast increase, 1 is a significant contrast increase. |
| `OcclusionExponent` | `float` | Exponent applied to the computed AO.  Values lower than 1 brighten occlusion overall without losing contact shadows. |
| `MinOcclusion` | `float` | Controls the darkest that a fully occluded area can get.  This tends to destroy contact shadows, use Contrast or OcclusionExponent instead. |
| `OcclusionTint` | `FColor` | Tint color on occluded areas, artistic control. |
| `OcclusionCombineMode` | `TEnumAsByte < enum EOcclusionCombineMode >` | Controls how occlusion from Distance Field Ambient Occlusion is combined with Screen Space Ambient Occlusion. |
| `bForceHide` | `uint8` | Whether to hide the primitive in game, if the primitive is Visible. |
| `FakeSkyLightAOClampMin` | `float` | - |
| `BlendDestinationCubemap` | `UTextureCube *` | - |

## Functions

### `SetIntensity`

```text
SetIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIndirectLightingIntensity`

```text
SetIndirectLightingIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricScatteringIntensity`

```text
SetVolumetricScatteringIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightColor`

```text
SetLightColor(NewLightColor: FLinearColor) -> void
```

Set color of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCubemap`

```text
SetCubemap(NewCubemap: UTextureCube *) -> void
```

Sets the cubemap used when SourceType is set to SpecifiedCubemap, and causes a skylight update on the next tick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCubemap` | `UTextureCube *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCubemapBlend`

```text
SetCubemapBlend(SourceCubemap: UTextureCube *, DestinationCubemap: UTextureCube *, InBlendFraction: float) -> void
```

Creates sky lighting from a blend between two cubemaps, which is only valid when SourceType is set to SpecifiedCubemap.
	  This can be used to seamlessly transition sky lighting between different times of day.
	  The caller should continue to update the blend until BlendFraction is 0 or 1 to reduce rendering cost.
	  The caller is responsible for avoiding pops due to changing the source or destination.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceCubemap` | `UTextureCube *` | - |
| `DestinationCubemap` | `UTextureCube *` | - |
| `InBlendFraction` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionTint`

```text
SetOcclusionTint(InTint: FColor &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTint` | `FColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionContrast`

```text
SetOcclusionContrast(InOcclusionContrast: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOcclusionContrast` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionExponent`

```text
SetOcclusionExponent(InOcclusionExponent: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOcclusionExponent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinOcclusion`

```text
SetMinOcclusion(InMinOcclusion: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinOcclusion` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForceHide`

```text
SetForceHide(bInForceHide: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInForceHide` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecaptureSky`

```text
RecaptureSky() -> void
```

Recaptures the scene for the skylight.
	  This is useful for making sure the sky light is up to date after changing something in the world that it would capture.
	  Warning: this is very costly and will definitely cause a hitch.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlateBlueprintLibrary.json -->

# USlateBlueprintLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IsUnderLocation`

```text
IsUnderLocation(Geometry: FGeometry &, AbsoluteCoordinate: FVector2D &) -> bool
```

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |
| `AbsoluteCoordinate` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the provided location in absolute coordinates is within the bounds of this geometry. |

### `AbsoluteToLocal`

```text
AbsoluteToLocal(Geometry: FGeometry &, AbsoluteCoordinate: FVector2D) -> FVector2D
```

Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |
| `AbsoluteCoordinate` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Transforms AbsoluteCoordinate into the local space of this Geometry. |

### `LocalToAbsolute`

```text
LocalToAbsolute(Geometry: FGeometry &, LocalCoordinate: FVector2D) -> FVector2D
```

Translates local coordinates into absolute coordinates
	 
	  Absolute coordinates could be either desktop or window space depending on what space the root of the widget hierarchy is in.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |
| `LocalCoordinate` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | Absolute coordinates |

### `GetLocalSize`

```text
GetLocalSize(Geometry: FGeometry &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | the size of the geometry in local space. |

### `GetAbsoluteSize`

```text
GetAbsoluteSize(Geometry: FGeometry &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | the size of the geometry in absolute space. |

### `GetAbsolutePosition`

```text
GetAbsolutePosition(Geometry: FGeometry &) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Geometry` | `FGeometry &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `EqualEqual_SlateBrush`

```text
EqualEqual_SlateBrush(A: FSlateBrush &, B: FSlateBrush &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FSlateBrush &` | - |
| `B` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether brushes A and B are identical. |

### `LocalToViewport`

```text
LocalToViewport(WorldContextObject: UObject *, Geometry: FGeometry &, LocalCoordinate: FVector2D, PixelPosition: FVector2D &, ViewportPosition: FVector2D &) -> void
```

Translates local coordinate of the geometry provided into local viewport coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Geometry` | `FGeometry &` | - |
| `LocalCoordinate` | `FVector2D` | - |
| `PixelPosition` | `FVector2D &` | The position in the game's viewport, usable for line traces and |
| `ViewportPosition` | `FVector2D &` | The position in the space of other widgets in the viewport. Like if you wanted |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AbsoluteToViewport`

```text
AbsoluteToViewport(WorldContextObject: UObject *, AbsoluteDesktopCoordinate: FVector2D, PixelPosition: FVector2D &, ViewportPosition: FVector2D &) -> void
```

Translates absolute coordinate in desktop space of the geometry provided into local viewport coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `AbsoluteDesktopCoordinate` | `FVector2D` | - |
| `PixelPosition` | `FVector2D &` | The position in the game's viewport, usable for line traces and |
| `ViewportPosition` | `FVector2D &` | The position in the space of other widgets in the viewport. Like if you wanted |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScreenToWidgetLocal`

```text
ScreenToWidgetLocal(WorldContextObject: UObject *, Geometry: FGeometry &, ScreenPosition: FVector2D, LocalCoordinate: FVector2D &) -> void
```

Translates a screen position in pixels into the local space of a widget with the given geometry.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Geometry` | `FGeometry &` | - |
| `ScreenPosition` | `FVector2D` | - |
| `LocalCoordinate` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScreenToWidgetAbsolute`

```text
ScreenToWidgetAbsolute(WorldContextObject: UObject *, ScreenPosition: FVector2D, AbsoluteCoordinate: FVector2D &) -> void
```

Translates a screen position in pixels into absolute application coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ScreenPosition` | `FVector2D` | - |
| `AbsoluteCoordinate` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScreenToViewport`

```text
ScreenToViewport(WorldContextObject: UObject *, ScreenPosition: FVector2D, ViewportPosition: FVector2D &) -> void
```

Translates a screen position in pixels into the local space of the viewport widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ScreenPosition` | `FVector2D` | - |
| `ViewportPosition` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSlateConstant_GlobalScrollAmount`

```text
GetSlateConstant_GlobalScrollAmount() -> float
```

Provide GetGlobalScrollAmount() to Lua.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `ReleaseAllMouseCapture`

```text
ReleaseAllMouseCapture() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseMouseCaptureWithIndex`

```text
ReleaseMouseCaptureWithIndex(InIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseAllMousePassThroughCapture`

```text
ReleaseAllMousePassThroughCapture() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseMousePassThroughCaptureWithIndex`

```text
ReleaseMousePassThroughCaptureWithIndex(InIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMouseCaptor`

```text
SetMouseCaptor(PointerIndex: int32, Widget: UWidget *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerIndex` | `int32` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetMousePassThroughCaptor`

```text
SetMousePassThroughCaptor(PointerIndex: int32, Widget: UWidget *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerIndex` | `int32` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlateBrushAsset.json -->

# USlateBrushAsset

An asset describing how a texture can exist in slate's DPI-aware environment
  and how this texture responds to resizing. e.g. Scale9-stretching? Tiling?

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Brush` | `FSlateBrush` | The slate brush resource describing the texture's behavior. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlateDataSheet.json -->

# USlateDataSheet

A texture used for communicating data to the GPU.
  Used in combination with SlateVectorArtData and SlateVectorArtInstanceData to
  pass data to UI materials.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataTexture` | `UTexture2D *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlateSettings.json -->

# USlateSettings

Settings that control Slate functionality

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bExplicitCanvasChildZOrder` | `bool` | Allow children of SConstraintCanvas to share render layers. Children must set explicit ZOrder on their slots to control render order. <br>	  Recommendation: Enable for mobile platforms. |
| `bEnableFixedLayerFeature` | `bool` | Force Image Widgets render in a given render layers to make them share one render layer. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlateThemeManager.json -->

# USlateThemeManager

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CurrentThemeId` | `FGuid` | - |
| `ActiveColors` | `FStyleColorList` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlateVectorArtData.json -->

# USlateVectorArtData

Turn static mesh data into Slate's simple vector art format.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VertexData` | `TArray < FSlateMeshVertex >` | @see GetVertexData() |
| `IndexData` | `TArray < uint32 >` | @see GetIndexData() |
| `Material` | `UMaterialInterface *` | @see GetMaterial() |
| `ExtentMin` | `FVector2D` | - |
| `ExtentMax` | `FVector2D` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlateWidgetStyleAsset.json -->

# USlateWidgetStyleAsset

Just a wrapper for the struct with real data in it.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CustomStyle` | `USlateWidgetStyleContainerBase *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USlider.json -->

# USlider

A simple widget that shows a sliding bar with a handle that allows you to control the value between 0..1.
 
   No Children

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `float` | The volume value to display. |
| `ValueDelegate` | `FGetFloat` | A bindable delegate to allow logic to drive the value of the widget |
| `WidgetStyle` | `FSliderStyle` | The progress bar style |
| `Orientation` | `TEnumAsByte < EOrientation >` | The slider's orientation. |
| `SliderBarColor` | `FLinearColor` | The color to draw the slider bar in. |
| `SliderHandleColor` | `FLinearColor` | The color to draw the slider handle in. |
| `IndentHandle` | `bool` | Whether the slidable area should be indented to fit the handle. |
| `Locked` | `bool` | Whether the handle is interactive or fixed. |
| `StepSize` | `float` | The amount to adjust the value by, when using a controller or keyboard |
| `IsFocusable` | `bool` | Should the slider be focusable? |
| `SupportClickChange` | `bool` | - |

## Functions

### `GetValue`

```text
GetValue() -> float
```

Gets the current value of the slider.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetValue`

```text
SetValue(InValue: float) -> void
```

Sets the current value of the slider.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIndentHandle`

```text
SetIndentHandle(InValue: bool) -> void
```

Sets if the slidable area should be indented to fit the handle

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLocked`

```text
SetLocked(InValue: bool) -> void
```

Sets the handle to be interactive or fixed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStepSize`

```text
SetStepSize(InValue: float) -> void
```

Sets the amount to adjust the value by, when using a controller or keyboard

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSliderBarColor`

```text
SetSliderBarColor(InValue: FLinearColor) -> void
```

Sets the color of the slider bar

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSliderHandleColor`

```text
SetSliderHandleColor(InValue: FLinearColor) -> void
```

Sets the color of the handle bar

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnMouseCaptureBegin`

```text
OnMouseCaptureBegin() -> void
```

Invoked when the mouse is pressed and a capture begins.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseCaptureEnd`

```text
OnMouseCaptureEnd() -> void
```

Invoked when the mouse is released and a capture ends.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnControllerCaptureBegin`

```text
OnControllerCaptureBegin() -> void
```

Invoked when the controller capture begins.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnControllerCaptureEnd`

```text
OnControllerCaptureEnd() -> void
```

Invoked when the controller capture ends.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnValueChanged`

```text
OnValueChanged(Value: float) -> void
```

Called when the value is changed by slider or typing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundAttenuation.json -->

# USoundAttenuation

Defines how a sound changes volume with distance to the listener

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Attenuation` | `FSoundAttenuationSettings` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundBase.json -->

# USoundBase

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundClassObject` | `USoundClass *` | Sound class this sound belongs to |
| `bDebug` | `uint32` | When "stat sounds -debug" has been specified, draw this sound's attenuation shape when the sound is audible. For debugging purpose only. |
| `bOverrideConcurrency` | `uint32` | Whether or not to override the sound concurrency object with local concurrency settings. |
| `bOutputToBusOnly` | `uint32` | Whether or not to only send this audio's output to a bus. If true, will not be this sound won't be audible except through bus sends. |
| `bIgnoreFocus_DEPRECATED` | `uint32` | - |
| `SoundConcurrencySettings` | `USoundConcurrency *` | If Override Concurrency is false, the sound concurrency settings to use for this sound. |
| `ConcurrencyOverrides` | `FSoundConcurrencySettings` | If Override Concurrency is true, concurrency settings to use. |
| `MaxConcurrentResolutionRule_DEPRECATED` | `TEnumAsByte < enum EMaxConcurrentResolutionRule :: Type >` | - |
| `MaxConcurrentPlayCount_DEPRECATED` | `int32` | Maximum number of times this sound can be played concurrently. |
| `Duration` | `float` | Duration of sound in seconds. |
| `AttenuationSettings` | `USoundAttenuation *` | Attenuation settings package for the sound |
| `Priority` | `float` | Sound priority (higher value is higher priority) used for concurrency resolution. This priority value is weighted against the final volume of the sound. |
| `SoundSubmixObject` | `USoundSubmix *` | Sound submix this sound belongs to. <br>	   Audio will play here and traverse through the submix graph. <br>	   A null entry will make the sound obey the default master effects graph. |
| `SoundSubmixSends` | `TArray < FSoundSubmixSendInfo >` | An array of submix sends. Audio from this sound will send a portion of its audio to these effects. |
| `SourceEffectChain` | `USoundEffectSourcePresetChain *` | The source effect chain to use for this sound. |
| `BusSends` | `TArray < FSoundSourceBusSendInfo >` | This sound will send it's audio output to this list of buses if there are bus instances playing. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundClass.json -->

# USoundClass

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Properties` | `FSoundClassProperties` | Configurable properties like volume and priority. |
| `ChildClasses` | `TArray < USoundClass * >` | - |
| `PassiveSoundMixModifiers` | `TArray < struct FPassiveSoundMixModifier >` | SoundMix Modifiers to activate automatically when a sound of this class is playing. |
| `ParentClass` | `USoundClass *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundConcurrency.json -->

# USoundConcurrency

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Concurrency` | `FSoundConcurrencySettings` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundCue.json -->

# USoundCue

The behavior of audio playback is defined within Sound Cues.

## Inheritance

`USoundBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverrideAttenuation` | `uint32` | Indicates whether attenuation should use the Attenuation Overrides or the Attenuation Settings asset |
| `FirstNode` | `USoundNode *` | - |
| `VolumeMultiplier` | `float` | Volume multiplier for the Sound Cue |
| `PitchMultiplier` | `float` | Pitch multiplier for the Sound Cue |
| `AttenuationOverrides` | `FSoundAttenuationSettings` | Attenuation settings to use if Override Attenuation is set to true |
| `SubtitlePriority` | `float` | - |
| `AllNodes` | `TArray < USoundNode * >` | - |
| `SoundCueGraph` | `UEdGraph *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundEffectSourcePresetChain.json -->

# USoundEffectSourcePresetChain

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Chain` | `TArray < FSourceEffectChainEntry >` | Chain of source effects to use for this sound source. |
| `bPlayEffectChainTails` | `uint32` | Whether to keep the source alive for the duration of the effect chain tails. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundGroups.json -->

# USoundGroups

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundGroupProfiles` | `TArray < FSoundGroup >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundMix.json -->

# USoundMix

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bApplyEQ` | `uint32` | Whether to apply the EQ effect |
| `EQPriority` | `float` | - |
| `EQSettings` | `FAudioEQEffect` | - |
| `SoundClassEffects` | `TArray < struct FSoundClassAdjuster >` | Array of changes to be applied to groups. |
| `InitialDelay` | `float` | Initial delay in seconds before the the mix is applied. |
| `FadeInTime` | `float` | Time taken in seconds for the mix to fade in. |
| `Duration` | `float` | Duration of mix, negative means it will be applied until another mix is set. |
| `FadeOutTime` | `float` | Time taken in seconds for the mix to fade out. |
| `bChanged` | `uint32` | Transient property used to trigger real-time updates of the active EQ filter for editor previewing |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNode.json -->

# USoundNode

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChildNodes` | `TArray < USoundNode * >` | - |
| `GraphNode` | `UEdGraphNode *` | Node's Graph representation, used to get position. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeAttenuation.json -->

# USoundNodeAttenuation

Defines how a sound's volume changes based on distance to the listener

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AttenuationSettings` | `USoundAttenuation *` | - |
| `AttenuationOverrides` | `FSoundAttenuationSettings` | - |
| `bOverrideAttenuation` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeBranch.json -->

# USoundNodeBranch

Selects a child node based on the value of a boolean parameter

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BoolParameterName` | `FName` | The name of the boolean parameter to use to determine which branch we should take |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeConcatenator.json -->

# USoundNodeConcatenator

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputVolume` | `TArray < float >` | Volume multiplier for each input. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeDelay.json -->

# USoundNodeDelay

Defines a delay

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DelayMin` | `float` | The lower bound of delay time in seconds. |
| `DelayMax` | `float` | The upper bound of delay time in seconds. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeDialoguePlayer.json -->

# USoundNodeDialoguePlayer

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DialogueWaveParameter` | `FDialogueWaveParameter` | - |
| `bLooping` | `uint32` | Whether the dialogue line should be played looping |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeDistanceCrossFade.json -->

# USoundNodeDistanceCrossFade

SoundNodeDistanceCrossFade
  
  This node's purpose is to play different sounds based on the distance to the listener.  
  The node mixes between the N different sounds which are valid for the distance.  One should
  think of a SoundNodeDistanceCrossFade as Mixer node which determines the set of nodes to
  "mix in" based on their distance to the sound.
  
  Example:
  You have a gun that plays a fire sound.  At long distances you want a different sound than
  if you were up close.   So you use a SoundNodeDistanceCrossFade which will calculate the distance
  a listener is from the sound and play either:  short distance, long distance, mix of short and long sounds.
 
  A SoundNodeDistanceCrossFade differs from an SoundNodeAttenuation in that any sound is only going
  be played if it is within the MinRadius and MaxRadius.  So if you want the short distance sound to be 
  heard by people close to it, the MinRadius should probably be 0
 
  The volume curve for a SoundNodeDistanceCrossFade will look like this:
 
                           Volume (of the input) 
     FadeInDistance.Max --> _________________ <-- FadeOutDistance.Min
                                            \
                                             \
                                              \
  FadeInDistance.Min -->                       \ <-- FadeOutDistance.Max

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CrossFadeInput` | `TArray < struct FDistanceDatum >` | Each input needs to have the correct data filled in so the SoundNodeDistanceCrossFade is able<br>	  to determine which sounds to play |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeDoppler.json -->

# USoundNodeDoppler

Computes doppler pitch shift

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DopplerIntensity` | `float` | How much to scale the doppler shift (1.0 is normal). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeEnveloper.json -->

# USoundNodeEnveloper

Allows manipulation of volume and pitch over a set time period

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LoopStart` | `float` | - |
| `LoopEnd` | `float` | - |
| `DurationAfterLoop` | `float` | - |
| `LoopCount` | `int32` | - |
| `bLoopIndefinitely` | `uint32` | - |
| `bLoop` | `uint32` | - |
| `VolumeInterpCurve_DEPRECATED` | `UDistributionFloatConstantCurve *` | - |
| `PitchInterpCurve_DEPRECATED` | `UDistributionFloatConstantCurve *` | - |
| `VolumeCurve` | `FRuntimeFloatCurve` | - |
| `PitchCurve` | `FRuntimeFloatCurve` | - |
| `PitchMin` | `float` | - |
| `PitchMax` | `float` | - |
| `VolumeMin` | `float` | - |
| `VolumeMax` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeGroupControl.json -->

# USoundNodeGroupControl

Plays different sounds depending on the number of active sounds
  Any time a new sound is played, the first group that has an available slot will be chosen

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GroupSizes` | `TArray < int32 >` | How many active sounds are allowed for each group |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeLooping.json -->

# USoundNodeLooping

Defines how a sound loops; either indefinitely, or for a set number of times.
  Note: The Looping node should only be used for logical or procedural looping such as introducing a delay.
  These sounds will not be played seamlessly. If you want a sound to loop seamlessly and indefinitely,
  use the Looping flag on the Wave Player node for that sound.

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LoopCount` | `int32` | The amount of times to loop |
| `bLoopIndefinitely` | `uint32` | If enabled, the node will continue to loop indefinitely regardless of the Loop Count value. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeMixer.json -->

# USoundNodeMixer

Defines how concurrent sounds are mixed together

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InputVolume` | `TArray < float >` | A volume for each input.  Automatically sized. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeModulator.json -->

# USoundNodeModulator

Defines a random volume and pitch modification when a sound starts

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PitchMin` | `float` | The lower bound of pitch (1.0 is no change). |
| `PitchMax` | `float` | The upper bound of pitch (1.0 is no change). |
| `VolumeMin` | `float` | The lower bound of volume (1.0 is no change). |
| `VolumeMax` | `float` | The upper bound of volume (1.0 is no change). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeModulatorContinuous.json -->

# USoundNodeModulatorContinuous

Allows named parameter based manipulation of pitch and volume

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PitchModulationParams` | `FModulatorContinuousParams` | - |
| `VolumeModulationParams` | `FModulatorContinuousParams` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeOscillator.json -->

# USoundNodeOscillator

Defines how a sound oscillates

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bModulateVolume` | `uint32` | Whether to oscillate volume. |
| `bModulatePitch` | `uint32` | Whether to oscillate pitch. |
| `AmplitudeMin` | `float` | An amplitude of 0.25 would oscillate between 0.75 and 1.25. |
| `AmplitudeMax` | `float` | An amplitude of 0.25 would oscillate between 0.75 and 1.25. |
| `FrequencyMin` | `float` | A frequency of 20 would oscillate at 10Hz. |
| `FrequencyMax` | `float` | A frequency of 20 would oscillate at 10Hz. |
| `OffsetMin` | `float` | Offset into the sine wave. Value modded by 2  PI. |
| `OffsetMax` | `float` | Offset into the sine wave. Value modded by 2  PI. |
| `CenterMin` | `float` | A center of 0.5 would oscillate around 0.5. |
| `CenterMax` | `float` | A center of 0.5 would oscillate around 0.5. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeParamCrossFade.json -->

# USoundNodeParamCrossFade

Crossfades between different sounds based on a parameter

## Inheritance

`USoundNodeDistanceCrossFade`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamName` | `FName` | Parameter controlling cross fades. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeRandom.json -->

# USoundNodeRandom

Selects sounds from a random set

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Weights` | `TArray < float >` | - |
| `PreselectAtLevelLoad` | `int32` | If greater than 0, then upon each level load such a number of inputs will be randomly selected<br>	   and the rest will be removed. This can be used to cut down the memory usage of large randomizing<br>	   cues. |
| `bRandomizeWithoutReplacement` | `uint32` | Determines whether or not this SoundNodeRandom should randomize with or without<br>	  replacement.  <br>	 <br>	  WithoutReplacement means that only nodes left will be valid for <br>	  selection.  So with that, you are guarenteed to have only one occurrence of the<br>	  sound played until all of the other sounds in the set have all been played.<br>	 <br>	  WithReplacement means that a node will be chosen and then placed back into the set.<br>	  So one could play the same sound over and over if the probabilities don't go your way :-) |
| `HasBeenUsed` | `TArray < bool >` | Internal state of which sounds have been played.  This is only used at runtime<br>	  to keep track of which sounds have been played |
| `NumRandomUsed` | `int32` | Counter var so we don't have to count all of the used sounds each time we choose a sound |
| `PIEHiddenNodes` | `TArray < int32 >` | Editor only list of nodes hidden to duplicate behavior of PreselectAtLevelLoad |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeSoundClass.json -->

# USoundNodeSoundClass

Remaps the SoundClass of SoundWaves underneath this

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundClassOverride` | `USoundClass *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeSwitch.json -->

# USoundNodeSwitch

Selects a child node based on the value of a integer parameter

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IntParameterName` | `FName` | The name of the integer parameter to use to determine which branch we should take |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeWaveParam.json -->

# USoundNodeWaveParam

Sound node that takes a runtime parameter for the wave to play

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WaveParameterName` | `FName` | The name of the wave parameter to use to look up the SoundWave we should play |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundNodeWavePlayer.json -->

# USoundNodeWavePlayer

Sound node that contains a reference to the raw wave file to be played

## Inheritance

`USoundNodeAssetReferencer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SoundWaveAssetPtr` | `TSoftObjectPtr < USoundWave >` | - |
| `SoundWave` | `USoundWave *` | - |
| `bLooping` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundSourceBus.json -->

# USoundSourceBus

## Inheritance

`USoundWave`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceBusChannels` | `ESourceBusChannels` | How many channels to use for the source bus. |
| `SourceBusDuration` | `float` | The duration (in seconds) to use for the source bus. A duration of 0.0 indicates to play the source bus indefinitely. |
| `bAutoDeactivateWhenSilent` | `uint32` | Stop the source bus when the volume goes to zero. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundSubmix.json -->

# USoundSubmix

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChildSubmixes` | `TArray < USoundSubmix * >` | - |
| `ParentSubmix` | `USoundSubmix *` | - |
| `SubmixEffectChain` | `TArray < USoundEffectSubmixPreset * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USoundWave.json -->

# USoundWave

## Inheritance

`USoundBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CompressionQuality` | `int32` | Platform agnostic compression quality. 1..100 with 1 being best compression and 100 being best quality. |
| `bLooping` | `uint32` | If set, when played directly (not through a sound cue) the wave will be played looping. |
| `bStreaming` | `uint32` | Whether this sound can be streamed to avoid increased memory usage |
| `StreamingPriority` | `int32` | Priority of this sound when streaming (lower priority streams may not always play) |
| `bMature` | `uint32` | If set to true if this sound is considered to contain matureadult content. |
| `bManualWordWrap` | `uint32` | If set to true will disable automatic generation of line breaks - use if the subtitles have been split manually. |
| `bSingleLine` | `uint32` | If set to true the subtitles display as a sequence of single lines as opposed to multiline. |
| `bVirtualizeWhenSilent` | `uint32` | Allows sound to play at 0 volume, otherwise will stop the sound when the sound is silent. |
| `SoundGroup` | `TEnumAsByte < ESoundGroup >` | - |
| `SpokenText` | `FString` | A localized version of the text that is actually spoken phonetically in the audio. |
| `SubtitlePriority` | `float` | The priority of the subtitle. |
| `Volume` | `float` | Playback volume of sound 0 to 1 - Default is 1.0. |
| `Pitch` | `float` | Playback pitch for sound. |
| `NumChannels` | `int32` | Number of channels of multichannel data; 1 or 2 for regular mono and stereo files |
| `SampleRate` | `int32` | Cached sample rate for displaying in the tools |
| `RawPCMDataSize` | `int32` | Size of RawPCMData, or what RawPCMData would be if the sound was fully decompressed |
| `Subtitles` | `TArray < struct FSubtitleCue >` | Subtitle cues.  If empty, use SpokenText as the subtitle.  Will often be empty,<br>	  as the contents of the subtitle is commonly identical to what is spoken. |
| `LocalizedSubtitles` | `TArray < struct FLocalizedSubtitle >` | The array of the subtitles for each language. Generated at cook time. |
| `Curves` | `UCurveTable *` | Curves associated with this sound wave |
| `InternalCurves` | `UCurveTable *` | Hold a reference to our internal curve so we can switch back to it if we want to |
| `ChannelOffsets` | `TArray < int32 >` | Offsets into the bulk data for the source wav data |
| `ChannelSizes` | `TArray < int32 >` | Sizes of the bulk data for the source wav data |
| `Comment` | `FString` | Provides contextual information for the sound to the translator. |
| `SourceFilePath_DEPRECATED` | `FString` | - |
| `SourceFileTimestamp_DEPRECATED` | `FString` | - |
| `AssetImportData` | `UAssetImportData *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USpacer.json -->

# USpacer

A spacer widget; it does not have a visual representation, and just provides padding between other widgets.
 
   No Children

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Size` | `FVector2D` | The size of the spacer |
| `UsePcParams` | `bool` | - |
| `SizePc` | `FVector2D` | - |

## Functions

### `SetSize`

```text
SetSize(InSize: FVector2D) -> void
```

Sets the size of the spacer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSize` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPcParamController`

```text
SetPcParamController(InValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USpectatorPawnMovement.json -->

# USpectatorPawnMovement

## Inheritance

`UFloatingPawnMovement`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIgnoreTimeDilation` | `uint32` | If true, component moves at full speed no matter the time dilation. Default is false. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USphereComponent.json -->

# USphereComponent

A sphere generally used for simple collision. Bounds are rendered as lines in the editor.

## Inheritance

`UShapeComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SphereRadius` | `float` | The radius of the sphere |

## Functions

### `SetSphereRadius`

```text
SetSphereRadius(InSphereRadius: float, bUpdateOverlaps: bool) -> void
```

Change the sphere radius. This is the unscaled radius, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSphereRadius` | `float` | - |
| `bUpdateOverlaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScaledSphereRadius`

```text
GetScaledSphereRadius() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetUnscaledSphereRadius`

```text
GetUnscaledSphereRadius() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetShapeScale`

```text
GetShapeScale() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USphereReflectionCaptureComponent.json -->

# USphereReflectionCaptureComponent

## Inheritance

`UReflectionCaptureComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InfluenceRadius` | `float` | Radius of the area that can receive reflections from this capture. |
| `PerformShapeTestOnMobile` | `bool` | - |
| `CaptureDistanceScale` | `float` | Not needed anymore, not yet removed in case the artist setup values are needed in the future |
| `PreviewInfluenceRadius` | `UDrawSphereComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USpinBox.json -->

# USpinBox

A numerical entry box that allows for direct entry of the number or allows the user to click and slide the number.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `float` | Value stored in this spin box |
| `ValueDelegate` | `FGetFloat` | A bindable delegate to allow logic to drive the value of the widget |
| `WidgetStyle` | `FSpinBoxStyle` | The Style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `Delta` | `float` | The amount by which to change the spin box value as the slider moves. |
| `SliderExponent` | `float` | The exponent by which to increase the delta as the mouse moves. 1 is constant (never increases the delta). |
| `Font` | `FSlateFontInfo` | Font color and opacity (overrides style) |
| `Justification` | `TEnumAsByte < ETextJustify :: Type >` | The justification the value text should appear as. |
| `MinDesiredWidth` | `float` | The minimum width of the spin box |
| `ClearKeyboardFocusOnCommit` | `bool` | Whether to remove the keyboard focus from the spin box when the value is committed |
| `SelectAllTextOnCommit` | `bool` | Whether to select the text in the spin box when the value is committed |
| `ForegroundColor` | `FSlateColor` | - |
| `bOverride_MinValue` | `uint32` | Whether the optional MinValue attribute of the widget is set |
| `bOverride_MaxValue` | `uint32` | Whether the optional MaxValue attribute of the widget is set |
| `bOverride_MinSliderValue` | `uint32` | Whether the optional MinSliderValue attribute of the widget is set |
| `bOverride_MaxSliderValue` | `uint32` | Whether the optional MaxSliderValue attribute of the widget is set |
| `MinValue` | `float` | The minimum allowable value that can be manually entered into the spin box |
| `MaxValue` | `float` | The maximum allowable value that can be manually entered into the spin box |
| `MinSliderValue` | `float` | The minimum allowable value that can be specified using the slider |
| `MaxSliderValue` | `float` | The maximum allowable value that can be specified using the slider |

## Functions

### `GetValue`

```text
GetValue() -> float
```

Get the current value of the spin box.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetValue`

```text
SetValue(NewValue: float) -> void
```

Set the value of the spin box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMinValue`

```text
GetMinValue() -> float
```

Get the current minimum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMinValue`

```text
SetMinValue(NewValue: float) -> void
```

Set the minimum value that can be manually set in the spin box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMinValue`

```text
ClearMinValue() -> void
```

Clear the minimum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaxValue`

```text
GetMaxValue() -> float
```

Get the current maximum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMaxValue`

```text
SetMaxValue(NewValue: float) -> void
```

Set the maximum value that can be manually set in the spin box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMaxValue`

```text
ClearMaxValue() -> void
```

Clear the maximum value that can be manually set in the spin box.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMinSliderValue`

```text
GetMinSliderValue() -> float
```

Get the current minimum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMinSliderValue`

```text
SetMinSliderValue(NewValue: float) -> void
```

Set the minimum value that can be specified using the slider.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMinSliderValue`

```text
ClearMinSliderValue() -> void
```

Clear the minimum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaxSliderValue`

```text
GetMaxSliderValue() -> float
```

Get the current maximum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetMaxSliderValue`

```text
SetMaxSliderValue(NewValue: float) -> void
```

Set the maximum value that can be specified using the slider.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMaxSliderValue`

```text
ClearMaxSliderValue() -> void
```

Clear the maximum value that can be specified using the slider.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForegroundColor`

```text
SetForegroundColor(InForegroundColor: FSlateColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForegroundColor` | `FSlateColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnValueChanged`

```text
OnValueChanged(InValue: float) -> void
```

Called when the value is changed interactively by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnValueCommitted`

```text
OnValueCommitted(InValue: float, CommitMethod: ETextCommit::Type) -> void
```

Called when the value is committed. Occurs when the user presses Enter or the text box loses focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |
| `CommitMethod` | `ETextCommit::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBeginSliderMovement`

```text
OnBeginSliderMovement() -> void
```

Called right before the slider begins to move

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnEndSliderMovement`

```text
OnEndSliderMovement(InValue: float) -> void
```

Called right after the slider handle is released by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USpinBoxWidgetStyle.json -->

# USpinBoxWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SpinBoxStyle` | `FSpinBoxStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USplineComponent.json -->

# USplineComponent

A spline component is a spline shape which can be used for other purposes (e.g. animating objects). It contains debug rendering capabilities.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SplineCurves` | `FSplineCurves` | - |
| `SplineInfo_DEPRECATED` | `FInterpCurveVector` | Deprecated - please use GetSplinePointsPosition() to fetch this FInterpCurve |
| `SplineRotInfo_DEPRECATED` | `FInterpCurveQuat` | Deprecated - please use GetSplinePointsRotation() to fetch this FInterpCurve |
| `SplineScaleInfo_DEPRECATED` | `FInterpCurveVector` | Deprecated - please use GetSplinePointsScale() to fetch this FInterpCurve |
| `SplineReparamTable_DEPRECATED` | `FInterpCurveFloat` | - |
| `bAllowSplineEditingPerInstance_DEPRECATED` | `bool` | - |
| `ReparamStepsPerSegment` | `int32` | Number of steps per spline segment to place in the reparameterization table |
| `Duration` | `float` | Specifies the duration of the spline in seconds |
| `bStationaryEndpoints` | `bool` | Whether the endpoints of the spline are considered stationary when traversing the spline at non-constant velocity.  Essentially this sets the endpoints' tangents to zero vectors. |
| `bSplineHasBeenEdited` | `bool` | Whether the spline has been edited from its default by the spline component visualizer |
| `bModifiedByConstructionScript` | `bool` | Whether the UCS has made changes to the spline points |
| `bInputSplinePointsToConstructionScript` | `bool` | Whether the spline points should be passed to the User Construction Script so they can be further manipulated by it.<br>	  If false, they will not be visible to it, and it will not be able to influence the per-instance positions set in the editor. |
| `bDrawDebug` | `bool` | If true, the spline will be rendered if the Splines showflag is set. |
| `bClosedLoop` | `bool` | Whether the spline is to be considered as a closed loop.<br>	  Use SetClosedLoop() to set this property, and IsClosedLoop() to read it. |
| `bLoopPositionOverride` | `bool` | - |
| `LoopPosition` | `float` | - |
| `DefaultUpVector` | `FVector` | Default up vector in local space to be used when calculating transforms along the spline |
| `bUseConfigRotation` | `bool` | Engine Modify Start |
| `bUseConfigRotationXY` | `bool` | - |
| `EditorUnselectedSplineSegmentColor` | `FLinearColor` | Engine Modify End<br>	 <br>	 Color of an unselected spline component segment in the editor |
| `EditorSelectedSplineSegmentColor` | `FLinearColor` | Color of a selected spline component segment in the editor |
| `bAllowDiscontinuousSpline` | `bool` | Whether the spline's leave and arrive tangents can be different |
| `bShouldVisualizeScale` | `bool` | Whether scale visualization should be displayed |
| `ScaleVisualizationWidth` | `float` | Width of spline in editor for use with scale visualization |
| `PostionModifyer` | `USplineComponentEditorModifer *` | - |
| `SelectedIndexs` | `TSet < int32 >` | - |
| `SnappingType` | `ESplineSnappingType` | - |
| `SnapInterval` | `float` | - |
| `SnapTopDownRange` | `FVector2D` | - |
| `TraceLength` | `float` | - |

## Functions

### `UpdateSpline`

```text
UpdateSpline() -> void
```

Update the spline tangents and SplineReparamTable

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDistanceAlongSplineAtSplineInputKey`

```text
GetDistanceAlongSplineAtSplineInputKey(InKey: float) -> float
```

Get distance along the spline at the provided input key value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InKey` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetUnselectedSplineSegmentColor`

```text
SetUnselectedSplineSegmentColor(SegmentColor: FLinearColor &) -> void
```

Specify unselected spline component segment color in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SegmentColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectedSplineSegmentColor`

```text
SetSelectedSplineSegmentColor(SegmentColor: FLinearColor &) -> void
```

Specify selected spline component segment color in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SegmentColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EditorSnapToGround`

```text
EditorSnapToGround() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EditorNormalizeSplineTangent`

```text
EditorNormalizeSplineTangent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDrawDebug`

```text
SetDrawDebug(bShow: bool) -> void
```

Specify whether this spline should be rendered when the EditorGame spline show flag is set

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClosedLoop`

```text
SetClosedLoop(bInClosedLoop: bool, bUpdateSpline: bool) -> void
```

Specify whether the spline is a closed loop or not. The loop position will be at 1.0 after the last point's input key

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInClosedLoop` | `bool` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClosedLoopAtPosition`

```text
SetClosedLoopAtPosition(bInClosedLoop: bool, Key: float, bUpdateSpline: bool) -> void
```

Specify whether the spline is a closed loop or not, and if so, the input key corresponding to the loop point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInClosedLoop` | `bool` | - |
| `Key` | `float` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsClosedLoop`

```text
IsClosedLoop() -> bool
```

Check whether the spline is a closed loop or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearSplinePoints`

```text
ClearSplinePoints(bUpdateSpline: bool) -> void
```

Clears all the points in the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddPoint`

```text
AddPoint(Point: FSplinePoint &, bUpdateSpline: bool) -> void
```

Adds an FSplinePoint to the spline. This contains its input key, position, tangent, rotation and scale.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FSplinePoint &` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddPoints`

```text
AddPoints(Points: TArray < FSplinePoint > &, bUpdateSpline: bool) -> void
```

Adds an array of FSplinePoints to the spline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FSplinePoint > &` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplinePoint`

```text
AddSplinePoint(Position: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Adds a point to the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplinePointAtIndex`

```text
AddSplinePointAtIndex(Position: FVector &, Index: int32, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Adds a point to the spline at the specified index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |
| `Index` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveSplinePoint`

```text
RemoveSplinePoint(Index: int32, bUpdateSpline: bool) -> void
```

Removes point at specified index from the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplineWorldPoint`

```text
AddSplineWorldPoint(Position: FVector &) -> void
```

Adds a world space point to the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSplineLocalPoint`

```text
AddSplineLocalPoint(Position: FVector &) -> void
```

Adds a local space point to the spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSplinePoints`

```text
SetSplinePoints(Points: TArray < FVector > &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Sets the spline to an array of points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FVector > &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSplineWorldPoints`

```text
SetSplineWorldPoints(Points: TArray < FVector > &) -> void
```

Sets the spline to an array of world space points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSplineLocalPoints`

```text
SetSplineLocalPoints(Points: TArray < FVector > &) -> void
```

Sets the spline to an array of local space points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLocationAtSplinePoint`

```text
SetLocationAtSplinePoint(PointIndex: int32, InLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Move an existing point to a new location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldLocationAtSplinePoint`

```text
SetWorldLocationAtSplinePoint(PointIndex: int32, InLocation: FVector &) -> void
```

Move an existing point to a new world location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTangentAtSplinePoint`

```text
SetTangentAtSplinePoint(PointIndex: int32, InTangent: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Specify the tangent at a given spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InTangent` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTangentsAtSplinePoint`

```text
SetTangentsAtSplinePoint(PointIndex: int32, InArriveTangent: FVector &, InLeaveTangent: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Specify the tangents at a given spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InArriveTangent` | `FVector &` | - |
| `InLeaveTangent` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUpVectorAtSplinePoint`

```text
SetUpVectorAtSplinePoint(PointIndex: int32, InUpVector: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUpdateSpline: bool) -> void
```

Specify the up vector at a given spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `InUpVector` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSplinePointType`

```text
GetSplinePointType(PointIndex: int32) -> ESplinePointType :: Type
```

Get the type of a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ESplinePointType :: Type` | - |

### `SetSplinePointType`

```text
SetSplinePointType(PointIndex: int32, Type: ESplinePointType :: Type, bUpdateSpline: bool) -> void
```

Specify the type of a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `Type` | `ESplinePointType :: Type` | - |
| `bUpdateSpline` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumberOfSplinePoints`

```text
GetNumberOfSplinePoints() -> int32
```

Get the number of points that make up this spline

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetLocationAtSplinePoint`

```text
GetLocationAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the location at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldLocationAtSplinePoint`

```text
GetWorldLocationAtSplinePoint(PointIndex: int32) -> FVector
```

Get the world location at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDirectionAtSplinePoint`

```text
GetDirectionAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the location at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTangentAtSplinePoint`

```text
GetTangentAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the tangent at spline point. This fetches the Leave tangent of the point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetArriveTangentAtSplinePoint`

```text
GetArriveTangentAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the arrive tangent at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetLeaveTangentAtSplinePoint`

```text
GetLeaveTangentAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the leave tangent at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRotationAtSplinePoint`

```text
GetRotationAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FRotator
```

Get the rotation at spline point as a rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetUpVectorAtSplinePoint`

```text
GetUpVectorAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the up vector at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVectorAtSplinePoint`

```text
GetRightVectorAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Get the right vector at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRollAtSplinePoint`

```text
GetRollAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type) -> float
```

Get the amount of roll at spline point, in degrees

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetScaleAtSplinePoint`

```text
GetScaleAtSplinePoint(PointIndex: int32) -> FVector
```

Get the scale at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTransformAtSplinePoint`

```text
GetTransformAtSplinePoint(PointIndex: int32, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseScale: bool) -> FTransform
```

Get the transform at spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetLocationAndTangentAtSplinePoint`

```text
GetLocationAndTangentAtSplinePoint(PointIndex: int32, Location: FVector &, Tangent: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> void
```

Get location and tangent at a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `Location` | `FVector &` | - |
| `Tangent` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLocalLocationAndTangentAtSplinePoint`

```text
GetLocalLocationAndTangentAtSplinePoint(PointIndex: int32, LocalLocation: FVector &, LocalTangent: FVector &) -> void
```

Get local location and tangent at a spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |
| `LocalLocation` | `FVector &` | - |
| `LocalTangent` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDistanceAlongSplineAtSplinePoint`

```text
GetDistanceAlongSplineAtSplinePoint(PointIndex: int32) -> float
```

Get the distance along the spline at the spline point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetSplineLength`

```text
GetSplineLength() -> float
```

Returns total length along this spline

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetDefaultUpVector`

```text
SetDefaultUpVector(UpVector: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> void
```

Sets the default up vector used by this spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UpVector` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDefaultUpVector`

```text
GetDefaultUpVector(CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Gets the default up vector used by this spline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetInputKeyAtDistanceAlongSpline`

```text
GetInputKeyAtDistanceAlongSpline(Distance: float) -> float
```

Given a distance along the length of this spline, return the corresponding input key at that point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTimeAtDistanceAlongSpline`

```text
GetTimeAtDistanceAlongSpline(Distance: float) -> float
```

Given a distance along the length of this spline, return the corresponding time at that point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetLocationAtDistanceAlongSpline`

```text
GetLocationAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldLocationAtDistanceAlongSpline`

```text
GetWorldLocationAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return the point in world space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDirectionAtDistanceAlongSpline`

```text
GetDirectionAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldDirectionAtDistanceAlongSpline`

```text
GetWorldDirectionAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector of the spline tangent there, in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTangentAtDistanceAlongSpline`

```text
GetTangentAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return the tangent vector of the spline there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldTangentAtDistanceAlongSpline`

```text
GetWorldTangentAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return the tangent vector of the spline there, in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRotationAtDistanceAlongSpline`

```text
GetRotationAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FRotator
```

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetWorldRotationAtDistanceAlongSpline`

```text
GetWorldRotationAtDistanceAlongSpline(Distance: float) -> FRotator
```

Given a distance along the length of this spline, return a rotation corresponding to the spline's rotation there, in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetUpVectorAtDistanceAlongSpline`

```text
GetUpVectorAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's up vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVectorAtDistanceAlongSpline`

```text
GetRightVectorAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a distance along the length of this spline, return a unit direction vector corresponding to the spline's right vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRollAtDistanceAlongSpline`

```text
GetRollAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type) -> float
```

Given a distance along the length of this spline, return the spline's roll there, in degrees.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetScaleAtDistanceAlongSpline`

```text
GetScaleAtDistanceAlongSpline(Distance: float) -> FVector
```

Given a distance along the length of this spline, return the spline's scale there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTransformAtDistanceAlongSpline`

```text
GetTransformAtDistanceAlongSpline(Distance: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseScale: bool) -> FTransform
```

Given a distance along the length of this spline, return an FTransform corresponding to that point on the spline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Distance` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetLocationAtTime`

```text
GetLocationAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldLocationAtTime`

```text
GetWorldLocationAtTime(Time: float, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the point in space where this puts you

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDirectionAtTime`

```text
GetDirectionAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetWorldDirectionAtTime`

```text
GetWorldDirectionAtTime(Time: float, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return a unit direction vector of the spline tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTangentAtTime`

```text
GetTangentAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's tangent there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRotationAtTime`

```text
GetRotationAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FRotator
```

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetWorldRotationAtTime`

```text
GetWorldRotationAtTime(Time: float, bUseConstantVelocity: bool) -> FRotator
```

Given a time from 0 to the spline duration, return a rotation corresponding to the spline's position and direction there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetUpVectorAtTime`

```text
GetUpVectorAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's up vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVectorAtTime`

```text
GetRightVectorAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's right vector there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTransformAtTime`

```text
GetTransformAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool, bUseScale: bool) -> FTransform
```

Given a time from 0 to the spline duration, return the spline's transform at the corresponding position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `GetRollAtTime`

```text
GetRollAtTime(Time: float, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseConstantVelocity: bool) -> float
```

Given a time from 0 to the spline duration, return the spline's roll there, in degrees.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetScaleAtTime`

```text
GetScaleAtTime(Time: float, bUseConstantVelocity: bool) -> FVector
```

Given a time from 0 to the spline duration, return the spline's scale there.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bUseConstantVelocity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindInputKeyClosestToWorldLocation`

```text
FindInputKeyClosestToWorldLocation(WorldLocation: FVector &) -> float
```

Given a location, in world space, return the input key closest to that location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FindLocationClosestToWorldLocation`

```text
FindLocationClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return the point on the curve that is closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindDirectionClosestToWorldLocation`

```text
FindDirectionClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world spcae, return a unit direction vector of the spline tangent closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindTangentClosestToWorldLocation`

```text
FindTangentClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return the tangent vector of the spline closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindRotationClosestToWorldLocation`

```text
FindRotationClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FRotator
```

Given a location, in world space, return rotation corresponding to the spline's rotation closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `FindUpVectorClosestToWorldLocation`

```text
FindUpVectorClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return a unit direction vector corresponding to the spline's up vector closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindRightVectorClosestToWorldLocation`

```text
FindRightVectorClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> FVector
```

Given a location, in world space, return a unit direction vector corresponding to the spline's right vector closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindRollClosestToWorldLocation`

```text
FindRollClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type) -> float
```

Given a location, in world space, return the spline's roll closest to the location, in degrees.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FindScaleClosestToWorldLocation`

```text
FindScaleClosestToWorldLocation(WorldLocation: FVector &) -> FVector
```

Given a location, in world space, return the spline's scale closest to the location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `FindTransformClosestToWorldLocation`

```text
FindTransformClosestToWorldLocation(WorldLocation: FVector &, CoordinateSpace: ESplineCoordinateSpace :: Type, bUseScale: bool) -> FTransform
```

Given a location, in world space, return an FTransform closest to that location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldLocation` | `FVector &` | - |
| `CoordinateSpace` | `ESplineCoordinateSpace :: Type` | - |
| `bUseScale` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USplineComponentEditorModifer.json -->

# USplineComponentEditorModifer

## Inheritance

`UObject`

## Functions

### `ModifyPostion`

```text
ModifyPostion(InPosition: FVector) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosition` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USplineMeshComponent.json -->

# USplineMeshComponent

A Spline Mesh Component is a derivation of a Static Mesh Component which can be deformed using a spline. Only a start and end position (and tangent) can be specified.

## Inheritance

`UStaticMeshComponent` -> `IInterface_CollisionDataProvider`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SplineParams` | `FSplineMeshParams` | Spline that is used to deform mesh |
| `SplineUpDir` | `FVector` | Axis (in component space) that is used to determine X axis for co-ordinates along spline |
| `bAllowSplineEditingPerInstance` | `uint32` | If true, spline keys may be edited per instance in the level viewport. Otherwise, the spline should be initialized in the construction script. |
| `bSmoothInterpRollScale` | `uint32` | If true, will use smooth interpolation (ease inout) for Scale, Roll, and Offset along this section of spline. If false, uses linear |
| `ForwardAxis` | `TEnumAsByte < ESplineMeshAxis :: Type >` | Chooses the forward axis for the spline mesh orientation |
| `SplineBoundaryMin` | `float` | Minimum coordinate along the spline forward axis which corresponds to start of spline. If set to 0.0, will use bounding box to determine bounds |
| `SplineBoundaryMax` | `float` | Maximum coordinate along the spline forward axis which corresponds to end of spline. If set to 0.0, will use bounding box to determine bounds |
| `BodySetup` | `UBodySetup *` | - |
| `CachedMeshBodySetupGuid` | `FGuid` | - |
| `bMeshDirty` | `uint32` | - |
| `bHasBeenBakedWithLandcape` | `uint32` | - |

## Functions

### `UpdateMesh`

```text
UpdateMesh() -> void
```

Update the collision and render state on the spline mesh following changes to its geometry

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartPosition`

```text
GetStartPosition() -> FVector
```

Get the start position of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetStartPosition`

```text
SetStartPosition(StartPos: FVector, bUpdateMesh: bool) -> void
```

Set the start position of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartPos` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartTangent`

```text
GetStartTangent() -> FVector
```

Get the start tangent vector of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetStartTangent`

```text
SetStartTangent(StartTangent: FVector, bUpdateMesh: bool) -> void
```

Set the start tangent vector of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartTangent` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndPosition`

```text
GetEndPosition() -> FVector
```

Get the end position of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetEndPosition`

```text
SetEndPosition(EndPos: FVector, bUpdateMesh: bool) -> void
```

Set the end position of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndPos` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndTangent`

```text
GetEndTangent() -> FVector
```

Get the end tangent vector of spline in local space

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetEndTangent`

```text
SetEndTangent(EndTangent: FVector, bUpdateMesh: bool) -> void
```

Set the end tangent vector of spline in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndTangent` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStartAndEnd`

```text
SetStartAndEnd(StartPos: FVector, StartTangent: FVector, EndPos: FVector, EndTangent: FVector, bUpdateMesh: bool) -> void
```

Set the start and end, position and tangent, all in local space

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartPos` | `FVector` | - |
| `StartTangent` | `FVector` | - |
| `EndPos` | `FVector` | - |
| `EndTangent` | `FVector` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartScale`

```text
GetStartScale() -> FVector2D
```

Get the start scaling

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetStartScale`

```text
SetStartScale(StartScale: FVector2D, bUpdateMesh: bool) -> void
```

Set the start scaling

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartScale` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartRoll`

```text
GetStartRoll() -> float
```

Get the start roll

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetStartRoll`

```text
SetStartRoll(StartRoll: float, bUpdateMesh: bool) -> void
```

Set the start roll

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartRoll` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStartOffset`

```text
GetStartOffset() -> FVector2D
```

Get the start offset

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetStartOffset`

```text
SetStartOffset(StartOffset: FVector2D, bUpdateMesh: bool) -> void
```

Set the start offset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartOffset` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndScale`

```text
GetEndScale() -> FVector2D
```

Get the end scaling

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetEndScale`

```text
SetEndScale(EndScale: FVector2D, bUpdateMesh: bool) -> void
```

Set the end scaling

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndScale` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndRoll`

```text
GetEndRoll() -> float
```

Get the end roll

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetEndRoll`

```text
SetEndRoll(EndRoll: float, bUpdateMesh: bool) -> void
```

Set the end roll

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndRoll` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetEndOffset`

```text
GetEndOffset() -> FVector2D
```

Get the end offset

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetEndOffset`

```text
SetEndOffset(EndOffset: FVector2D, bUpdateMesh: bool) -> void
```

Set the end offset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EndOffset` | `FVector2D` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetForwardAxis`

```text
GetForwardAxis() -> ESplineMeshAxis :: Type
```

Get the forward axis

**Returns**

| Type | Description |
|---|---|
| `ESplineMeshAxis :: Type` | - |

### `SetForwardAxis`

```text
SetForwardAxis(InForwardAxis: ESplineMeshAxis :: Type, bUpdateMesh: bool) -> void
```

Set the forward axis

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForwardAxis` | `ESplineMeshAxis :: Type` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSplineUpDir`

```text
GetSplineUpDir() -> FVector
```

Get the spline up direction

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetSplineUpDir`

```text
SetSplineUpDir(InSplineUpDir: FVector &, bUpdateMesh: bool) -> void
```

Set the spline up direction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSplineUpDir` | `FVector &` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoundaryMin`

```text
GetBoundaryMin() -> float
```

Get the boundary min

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetBoundaryMin`

```text
SetBoundaryMin(InBoundaryMin: float, bUpdateMesh: bool) -> void
```

Set the boundary min

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoundaryMin` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBoundaryMax`

```text
GetBoundaryMax() -> float
```

Get the boundary max

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetBoundaryMax`

```text
SetBoundaryMax(InBoundaryMax: float, bUpdateMesh: bool) -> void
```

Set the boundary max

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBoundaryMax` | `float` | - |
| `bUpdateMesh` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USpotLightComponent.json -->

# USpotLightComponent

A spot light component emits a directional cone shaped light (Eg a Torch).

## Inheritance

`UPointLightComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InnerConeAngle` | `float` | Degrees. |
| `OuterConeAngle` | `float` | Degrees. |
| `bCastPhotonShadow` | `uint32` | #if WITH_PHOTON_SHADOW<br>	 Whether the light should cast photon shadow for character<br>	 #endif |
| `NearPlaneOffset` | `float` | - |
| `FarPlaneOffset` | `float` | - |
| `LightShaftConeAngle` | `float` | Degrees. <br>	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category=LightShaft, meta=(UIMin = "1.0", UIMax = "180.0")) |

## Functions

### `SetInnerConeAngle`

```text
SetInnerConeAngle(NewInnerConeAngle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInnerConeAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOuterConeAngle`

```text
SetOuterConeAngle(NewOuterConeAngle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOuterConeAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USpringArmComponent.json -->

# USpringArmComponent

This component tries to maintain its children at a fixed distance from the parent,
  but will retract the children if there is a collision, and spring back when there is no collision.
 
  Example: Use as a 'camera boom' to keep the follow camera for a player from colliding into the world.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetArmLength` | `float` | Natural length of the spring arm when there are no collisions |
| `SocketOffset` | `FVector` | offset at end of spring arm; use this instead of the relative offset of the attached component to ensure the line trace works as desired |
| `TargetOffset` | `FVector` | Offset at start of spring, applied in world space. Use this if you want a world-space offset from the parent component instead of the usual relative-space offset. |
| `ProbeSize` | `float` | How big should the query probe sphere be (in unreal units) |
| `ProbeChannel` | `TEnumAsByte < ECollisionChannel >` | Collision channel of the query probe (defaults to ECC_Camera) |
| `bDoCollisionTest` | `uint32` | If true, do a collision test using ProbeChannel and ProbeSize to prevent camera clipping into level. |
| `bUsePawnControlRotation` | `uint32` | If this component is placed on a pawn, should it use the viewcontrol rotation of the pawn where possible?<br>	  When disabled, the component will revert to using the stored RelativeRotation of the component.<br>	  Note that this component itself does not rotate, but instead maintains its relative rotation to its parent as normal,<br>	  and just repositions and rotates its children as desired by the inherited rotation settings. Use GetTargetRotation()<br>	  if you want the rotation target based on all the settings (UsePawnControlRotation, InheritPitch, etc).<br>	 <br>	  @see GetTargetRotation(), APawn::GetViewRotation() |
| `bInheritPitch` | `uint32` | Should we inherit pitch from parent component. Does nothing if using Absolute Rotation. |
| `bInheritYaw` | `uint32` | Should we inherit yaw from parent component. Does nothing if using Absolute Rotation. |
| `bInheritRoll` | `uint32` | Should we inherit roll from parent component. Does nothing if using Absolute Rotation. |
| `bEnableCameraLag` | `uint32` | If true, camera lags behind target position to smooth its movement.<br>	  @see CameraLagSpeed |
| `bEnableCameraRotationLag` | `uint32` | If true, camera lags behind target rotation to smooth its movement.<br>	  @see CameraRotationLagSpeed |
| `bUseCameraLagSubstepping` | `uint32` | If bUseCameraLagSubstepping is true, sub-step camera damping so that it handles fluctuating frame rates well (though this comes at a cost).<br>	  @see CameraLagMaxTimeStep |
| `bDrawDebugLagMarkers` | `uint32` | If true and camera location lag is enabled, draws markers at the camera target (in green) and the lagged position (in yellow).<br>	  A line is drawn between the two locations, in green normally but in red if the distance to the lag target has been clamped (by CameraLagMaxDistance). |
| `CameraLagSpeed` | `float` | If bEnableCameraLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag). |
| `CameraRotationLagSpeed` | `float` | If bEnableCameraRotationLag is true, controls how quickly camera reaches target position. Low values are slower (more lag), high values are faster (less lag), while zero is instant (no lag). |
| `CameraLagMaxTimeStep` | `float` | Max time step used when sub-stepping camera lag. |
| `CameraLagMaxDistance` | `float` | Max distance the camera target may lag behind the current location. If set to zero, no max distance is enforced. |
| `IgnoredActors` | `TArray < AActor * >` | - |
| `CacheHit` | `FHitResult` | - |

## Functions

### `GetTargetRotation`

```text
GetTargetRotation() -> FRotator
```

Get the target rotation we inherit, used as the base target for the boom rotation.
	  This is derived from attachment to our parent and considering the UsePawnControlRotation and absolute rotation flags.

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetActive`

```text
SetActive(bNewActive: bool, bReset: bool) -> void
```

Sets whether the component is active or not

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewActive` | `bool` | - The new active state of the component |
| `bReset` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UpdateDesiredArmLocationCustom`

```text
UpdateDesiredArmLocationCustom(bDoTrace: bool, bDoLocationLag: bool, bDoRotationLag: bool, DeltaTime: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDoTrace` | `bool` | - |
| `bDoLocationLag` | `bool` | - |
| `bDoRotationLag` | `bool` | - |
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetExtraIgnoreActors`

```text
GetExtraIgnoreActors() -> TArray < AActor * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < AActor * >` | - |

### `GetExtraIgnoreCompoents`

```text
GetExtraIgnoreCompoents() -> TArray < UPrimitiveComponent * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UPrimitiveComponent * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStackBox.json -->

# UStackBox

A stack box widget is a layout panel allowing child widgets to be automatically laid out
  vertically or horizontally.
 
   Many Children
   Flows Vertical or Horizontal

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Orientation` | `TEnumAsByte < EOrientation >` | The orientation of the stack box. |

## Functions

### `GetOrientation`

```text
GetOrientation() -> UMG_API EOrientation
```

Get the orientation of the stack box.

**Returns**

| Type | Description |
|---|---|
| `UMG_API EOrientation` | - |

### `SetOrientation`

```text
SetOrientation(InType: EOrientation) -> UMG_API void
```

Set the orientation of the stack box. The existing elements will be rearranged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InType` | `EOrientation` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `AddChildToStackBox`

```text
AddChildToStackBox(Content: UWidget *) -> UMG_API UStackBoxSlot *
```

Adds a new child widget to the container.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API UStackBoxSlot *` | - |

### `ReplaceStackBoxChildAt`

```text
ReplaceStackBoxChildAt(Index: int32, Content: UWidget *) -> UMG_API bool
```

Replace the widget at the given index it with a different widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStackBoxSlot.json -->

# UStackBoxSlot

The Slot for the UStackBox, contains the widget that is flowed vertically or horizontally.

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `Size` | `FSlateChildSize` | How much space this slot should occupy in the direction of the panel. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |

## Functions

### `GetPadding`

```text
GetPadding() -> UMG_API FMargin
```

**Returns**

| Type | Description |
|---|---|
| `UMG_API FMargin` | - |

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> UMG_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetSize`

```text
GetSize() -> UMG_API FSlateChildSize
```

**Returns**

| Type | Description |
|---|---|
| `UMG_API FSlateChildSize` | - |

### `SetSize`

```text
SetSize(InSize: FSlateChildSize) -> UMG_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSize` | `FSlateChildSize` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetHorizontalAlignment`

```text
GetHorizontalAlignment() -> UMG_API EHorizontalAlignment
```

**Returns**

| Type | Description |
|---|---|
| `UMG_API EHorizontalAlignment` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(InHorizontalAlignment: EHorizontalAlignment) -> UMG_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHorizontalAlignment` | `EHorizontalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetVerticalAlignment`

```text
GetVerticalAlignment() -> UMG_API EVerticalAlignment
```

**Returns**

| Type | Description |
|---|---|
| `UMG_API EVerticalAlignment` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(InVerticalAlignment: EVerticalAlignment) -> UMG_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVerticalAlignment` | `EVerticalAlignment` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStaticMesh.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStaticMeshComponent.json -->

# UStaticMeshComponent

StaticMeshComponent is used to create an instance of a UStaticMesh.
  A static mesh is a piece of geometry that consists of a static set of polygons.
 
  @see UStaticMesh

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ForcedLodModel` | `int32` | If 0, auto-select LOD level. if >0, force to (ForcedLodModel-1). |
| `PreviousLODLevel` | `int32` | LOD that was desired for rendering this StaticMeshComponent last frame. |
| `MinLOD` | `int32` | Specifies the smallest LOD that will be used for this component.<br>	  This is ignored if ForcedLodModel is enabled. |
| `MaxLOD` | `int32` | - |
| `StaticMesh` | `UStaticMesh *` | The static mesh that this component uses to render |
| `TightBoundsOrigin` | `FVector` | - |
| `TightBoundsBoxExtent` | `FVector` | - |
| `TightBoundsSphereRadius` | `float` | - |
| `CanUseTightBound` | `bool` | - |
| `VisibilityCollisionColor` | `FColor` | Whether you want to turn on the collision display preview |
| `bEnableSimpleMaterial` | `bool` | If true, WireframeColorOverride will be used. If false, color is determined based on mobility and physics simulation settings |
| `bOverrideWireframeColor` | `uint8` | If true, WireframeColorOverride will be used. If false, color is determined based on mobility and physics simulation settings |
| `bOverrideMinLOD` | `uint8` | Whether to override the MinLOD setting of the static mesh asset with the MinLOD of this component. |
| `bOverrideNavigationExport` | `uint8` | If true, bForceNavigationObstacle flag will take priority over navigation data stored in StaticMesh |
| `bForceNavigationObstacle` | `uint8` | Allows overriding navigation export behavior per component: full collisions or dynamic obstacle |
| `bDisallowMeshPaintPerInstance` | `uint8` | If true, mesh painting is disallowed on this instance. Set if vertex colors are overridden in a construction script. |
| `bHasHLODTag` | `uint8` | Whether this component participates in HLOD (computed from ReorganizationTags) |
| `bIgnoreInstanceForTextureStreaming` | `uint8` | Ignore this instance of this static mesh when calculating streaming information.<br>	 	This can be useful when doing things like applying character textures to static geometry,<br>	 	to avoid them using distance-based streaming. |
| `bOverrideLightMapRes` | `uint8` | Whether to override the lightmap resolution defined in the static mesh. |
| `bOverrideCullingScreenSize` | `uint8` | - |
| `bCastDistanceFieldIndirectShadow` | `uint8` | Whether to use the mesh distance field representation (when present) for shadowing indirect lighting (from lightmaps or skylight) on Movable components.<br>	  This works like capsule shadows on skeletal meshes, except using the mesh distance field so no physics asset is required.<br>	  The StaticMesh must have 'Generate Mesh Distance Field' enabled, or the project must have 'Generate Mesh Distance Fields' enabled for this feature to work. |
| `bOverrideDistanceFieldSelfShadowBias` | `uint8` | Whether to override the DistanceFieldSelfShadowBias setting of the static mesh asset with the DistanceFieldSelfShadowBias of this component. |
| `bUseSubDivisions` | `uint8` | Whether to use subdivisions or just the triangle's vertices. |
| `bUseDefaultCollision` | `uint8` | Use the collision profile specified in the StaticMesh asset. |
| `bForceNotHzbOccluder` | `uint8` | not a hzb Occluder |
| `bUseAsOccluderIgnoreMobility` | `uint8` | - |
| `bCanBeOccludeed` | `uint8` | - |
| `bCustomWaterBeOccludeed` | `uint8` | - |
| `bAllowCopyExpectedQualityFromMesh` | `uint8` | - |
| `OverriddenLightMapRes` | `int32` | Light map resolution to use on this component, used if bOverrideLightMapRes is true and there is a valid StaticMesh. |
| `StreamingDistanceMultiplier` | `float` | Allows adjusting the desired streaming distance of streaming textures that uses UV 0.<br>	  1.0 is the default, whereas a higher value makes the textures stream in sooner from far away.<br>	  A lower value (0.0-1.0) makes the textures stream in later (you have to be closer).<br>	  Value can be < 0 (from legcay content, or code changes) |
| `LODData` | `TArray < FStaticMeshComponentLODInfo >` | Static mesh LOD data.  Contains static lighting data along with instanced mesh vertex colors. |
| `StreamingTextureData` | `TArray < FStreamingTextureBuildInfo >` | The list of texture, bounds and scales. As computed in the texture streaming build process. |
| `IsDynamicInstancingParametersEnabled` | `bool` | Is dynamic instancing parameters enabled |
| `DynamicInstancingParameters` | `TMap < FString , FVector4 >` | Dynamic instancing parameters |
| `LightmassSettings` | `FLightmassPrimitiveSettings` | The Lightmass settings for this object. |
| `IdeaBakingSettings` | `FIdeaBakingPrimitiveSettings` | Add by luciuszhang: The IdeaBaking settings for this object. |
| `AffectPointLightBPActors` | `TArray < TWeakObjectPtr < AActor > >` | - |
| `PointLightStaticMeshLODResources` | `TArray < FStaticMeshPointLightVertexDataBuffer >` | - |
| `bEnableISMbatching` | `uint8` | - |
| `bForceUseDynamicElement` | `uint8` | - |
| `LODSectionHiddenFlags` | `TArray < uint8 >` | Hidden Flags for Rendering Section (8 bits = flags, Support 8 Sections), add by connerxiong 2022.6.16. |
| `OutlineStaticMesh` | `UStaticMesh *` | Outline Static Mesh |
| `SubDivisionStepSize` | `int32` | Subdivision step size for static vertex lighting. |
| `WireframeColorOverride` | `FColor` | Wireframe color to use if bOverrideWireframeColor is true |
| `SelectedEditorSection` | `int32` | The section currently selected in the Editor. Used for highlighting |
| `SelectedEditorMaterial` | `int32` | The material currently selected in the Editor. Used for highlighting |
| `SectionIndexPreview` | `int32` | Index of the section to preview. If set to INDEX_NONE, all section will be rendered. Used for isolating in Static Mesh Tool |
| `MaterialIndexPreview` | `int32` | Index of the material to preview. If set to INDEX_NONE, all section will be rendered. Used for isolating in Static Mesh Tool |
| `ReorganizationTags` | `FReorganizationTagsContainer` | Reorganization tags for Level Partition system (inherits from StaticMesh by default) |
| `bOverrideReorganizationTags` | `bool` | Legacy serialized switch. New editorruntime logic uses per-group override flags on ReorganizationTags entries. |
| `StaticMeshImportVersion` | `int32` | The import version of the static mesh when it was assign this is update when:<br>	  - The user assign a new staticmesh to the component<br>	  - The component is serialize (IsSaving)<br>	  - Default value is BeforeImportStaticMeshVersionWasAdded<br>	 <br>	  If when the component get load (PostLoad) the version of the attach staticmesh is newer<br>	  then this value, we will remap the material override because the order of the materials list<br>	  in the staticmesh can be changed. Hopefully there is a remap table save in the staticmesh. |
| `bCustomOverrideVertexColorPerLOD` | `uint8` | The component has some custom painting on LODs or not. |
| `bDisplayVertexColors` | `uint8` | - |
| `DistanceFieldIndirectShadowMinVisibility` | `float` | Controls how dark the dynamic indirect shadow can be. |
| `DistanceFieldSelfShadowBias` | `float` | Useful for reducing self shadowing from distance field methods when using world position offset to animate the mesh's vertices. |
| `IrrelevantLights_DEPRECATED` | `TArray < FGuid >` | - |
| `StaticMeshDerivedDataKey` | `FString` | Derived data key of the static mesh, used to determine if an update from the source static mesh is required. |
| `MaterialStreamingRelativeBoxes` | `TArray < uint32 >` | Material Bounds used for texture streaming. |

## Functions

### `OnRep_StaticMesh`

```text
OnRep_StaticMesh(OldStaticMesh: UStaticMesh *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldStaticMesh` | `UStaticMesh *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStaticMesh`

```text
SetStaticMesh(NewMesh: UStaticMesh *) -> bool
```

Change the StaticMesh used by this instance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMesh` | `UStaticMesh *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetDirty`

```text
SetDirty() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVisibilityCollisionColor`

```text
SetVisibilityCollisionColor(CollisionColor: FColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CollisionColor` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetVisibilityCollisionColor`

```text
GetVisibilityCollisionColor() -> FColor
```

**Returns**

| Type | Description |
|---|---|
| `FColor` | - |

### `K2_GetStaticMesh`

```text
K2_GetStaticMesh() -> UStaticMesh *
```

**Returns**

| Type | Description |
|---|---|
| `UStaticMesh *` | - |

### `SetOutlineMesh`

```text
SetOutlineMesh(InStaticMesh: UStaticMesh *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStaticMesh` | `UStaticMesh *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForcedLodModel`

```text
SetForcedLodModel(NewForcedLodModel: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewForcedLodModel` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDistanceFieldSelfShadowBias`

```text
SetDistanceFieldSelfShadowBias(NewValue: float) -> void
```

Sets the component's DistanceFieldSelfShadowBias.  bOverrideDistanceFieldSelfShadowBias must be enabled for this to have an effect.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLocalBounds`

```text
GetLocalBounds(Min: FVector &, Max: FVector &) -> void
```

Get Local bounds

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `FVector &` | - |
| `Max` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicInstancingParameter`

```text
SetDynamicInstancingParameter(MaterialIndex: int, Name: FString &, Value: FVector4 &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MaterialIndex` | `int` | - |
| `Name` | `FString &` | - |
| `Value` | `FVector4 &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `EnableMeshClipPlane`

```text
EnableMeshClipPlane(ClipPlane: FPlane &, PlaneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipPlane`

```text
DisableMeshClipPlane(PlaneIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlaneIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClipArc`

```text
EnableMeshClipArc(ClipPlane: FPlane &, ClipSphere: FVector4 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlane` | `FPlane &` | - |
| `ClipSphere` | `FVector4 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClipArc`

```text
DisableMeshClipArc() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableMeshClip4Planes`

```text
EnableMeshClip4Planes(ClipPlanes: TArray < FPlane > &, bBox: bool) -> void
```

Num of ClipPlanes is 4
	  0: Top Plane
	  1: Down Plane
	  2: Left Plane
	  3: Right Plane

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClipPlanes` | `TArray < FPlane > &` | - |
| `bBox` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableMeshClip4Planes`

```text
DisableMeshClip4Planes() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckSwitchSimpleMaterial`

```text
CheckSwitchSimpleMaterial() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStaticMeshIndoorVolumeComponent.json -->

# UStaticMeshIndoorVolumeComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StaticMesh` | `UStaticMesh *` | - |
| `SplitSizeScale` | `float` | - |
| `SplitFadeSizeScale` | `float` | - |
| `bLockGenerateSplit` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStaticMeshIndoorVolumeContainerComponent.json -->

# UStaticMeshIndoorVolumeContainerComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StaticMeshes` | `TArray < UStaticMesh * >` | - |
| `InstanceRuns` | `TArray < FInstanceRun >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStaticMeshSocket.json -->

# UStaticMeshSocket

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SocketName` | `FName` | Defines a named attachment location on the UStaticMesh. <br>	 	These are set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the StaticMeshComponent.<br>	 	The Outer of a StaticMeshSocket should always be the UStaticMesh. |
| `RelativeLocation` | `FVector` | - |
| `RelativeRotation` | `FRotator` | - |
| `RelativeScale` | `FVector` | - |
| `Tag` | `FString` | - |
| `bDynamicCreate` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStaticMeshWidget.json -->

# UStaticMeshWidget

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StaticMeshAsset` | `USlateVectorArtData *` | - |
| `MeshScale` | `FVector2D` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/Buff/USTBaseBuffSystemComponent.json -->

# USTBaseBuffSystemComponent

Buff管理组件

## Inheritance

`UActorComponent` -> `IUTSkillInstanceNodeContainerInterface` -> `IObjectPoolInterface`

## Delegates

### `UGC_BuffAttachedDelegate`

```text
UGC_BuffAttachedDelegate(BuffName: const FName&) -> void
```

Buff添加委托
	  生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuffName` | `const FName&` | Buff名字 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_BuffDetachedDelegate`

```text
UGC_BuffDetachedDelegate(BuffName: const FName&) -> void
```

Buff移除委托
	  生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuffName` | `const FName&` | Buff名字 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStereoLayerComponent.json -->

# UStereoLayerComponent

A geometry layer within the stereo rendered viewport.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bLiveTexture` | `uint32` | True if the stereo layer texture needs to update itself every frame(scene capture, video, etc.) |
| `bSupportsDepth` | `uint32` | True if the stereo layer needs to support depth intersections with the scene geometry, if available on the platform |
| `bNoAlphaChannel` | `uint32` | True if the texture should not use its own alpha channel (1.0 will be substituted) |
| `Texture` | `UTexture *` | Texture displayed on the stereo layer (is stereocopic textures are supported on the platfrom and more than one texture is provided, this will be the right eye) |
| `LeftTexture` | `UTexture *` | Texture displayed on the stereo layer for left eye, if stereoscopic textures are supported on the platform |
| `bQuadPreserveTextureRatio` | `uint32` | True if the quad should internally set it's Y value based on the set texture's dimensions |
| `QuadSize` | `FVector2D` | Size of the rendered stereo layer quad |
| `UVRect` | `FBox2D` | UV coordinates mapped to the quad face |
| `CylinderRadius` | `float` | Radial size of the rendered stereo layer cylinder |
| `CylinderOverlayArc` | `float` | Arc angle for the stereo layer cylinder |
| `CylinderHeight` | `int` | Height of the stereo layer cylinder |
| `StereoLayerType` | `TEnumAsByte < enum EStereoLayerType >` | Specifies how and where the quad is rendered to the screen |
| `StereoLayerShape` | `TEnumAsByte < enum EStereoLayerShape >` | Specifies which type of layer it is.  Note that some shapes will be supported only on certain platforms! |
| `Priority` | `int32` | Render priority among all stereo layers, higher priority render on top of lower priority |

## Functions

### `SetTexture`

```text
SetTexture(InTexture: UTexture *) -> void
```

Change the texture displayed on the stereo layer quad

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTexture`

```text
GetTexture() -> UTexture *
```

**Returns**

| Type | Description |
|---|---|
| `UTexture *` | - |

### `SetQuadSize`

```text
SetQuadSize(InQuadSize: FVector2D) -> void
```

Change the quad size. This is the unscaled height and width, before component scale is applied.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InQuadSize` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetQuadSize`

```text
GetQuadSize() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetUVRect`

```text
SetUVRect(InUVRect: FBox2D) -> void
```

Change the UV coordinates mapped to the quad face

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUVRect` | `FBox2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUVRect`

```text
GetUVRect() -> FBox2D
```

**Returns**

| Type | Description |
|---|---|
| `FBox2D` | - |

### `SetPriority`

```text
SetPriority(InPriority: int32) -> void
```

Change the layer's render priority, higher priorities render on top of lower priorities

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPriority` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPriority`

```text
GetPriority() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `MarkTextureForUpdate`

```text
MarkTextureForUpdate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStereoLayerFunctionLibrary.json -->

# UStereoLayerFunctionLibrary

StereoLayer Extensions Function Library

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SetSplashScreen`

```text
SetSplashScreen(Texture: UTexture *, Scale: FVector2D, Offset: FVector2D, bShowLoadingMovie: bool, bShowOnSet: bool) -> void
```

Set splash screen attributes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture *` | (in) A texture to be used for the splash. B8R8G8A8 format. |
| `Scale` | `FVector2D` | (in) Scale of the texture. |
| `Offset` | `FVector2D` | (in) Position from which to start rendering the texture. |
| `bShowLoadingMovie` | `bool` | - |
| `bShowOnSet` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowSplashScreen`

```text
ShowSplashScreen() -> void
```

Show the splash screen and override the VR display

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HideSplashScreen`

```text
HideSplashScreen() -> void
```

Hide the splash screen and return to normal display.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableAutoLoadingSplashScreen`

```text
EnableAutoLoadingSplashScreen(InAutoShowEnabled: bool) -> void
```

Enablesdisables splash screen to be automatically shown when LoadMap is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAutoShowEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USTExtraGameMagnitudeCalculation.json -->

# USTExtraGameMagnitudeCalculation

伤害公式

## Inheritance

`UGameMagnitudeCalculationBase` -> `ILocalCalculationVariableSupportInterface`

## Functions

### `IsHeadDamage`

```text
IsHeadDamage(Context: FGameMagnitudeContext &) -> bool
```

获取是否是爆头伤害

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext &` | 公式的上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否是爆头伤害 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStreamingSettings.json -->

# UStreamingSettings

Streaming settings.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AsyncLoadingThreadEnabled` | `uint32` | - |
| `WarnIfTimeLimitExceeded` | `uint32` | - |
| `TimeLimitExceededMultiplier` | `float` | - |
| `TimeLimitExceededMinTime` | `float` | - |
| `MinBulkDataSizeForAsyncLoading` | `int32` | - |
| `UseBackgroundLevelStreaming` | `uint32` | - |
| `AsyncLoadingUseFullTimeLimit` | `uint32` | Whether to use the entire time limit even if blocked on IO |
| `AsyncLoadingTimeLimit` | `float` | - |
| `PriorityAsyncLoadingExtraTime` | `float` | - |
| `LevelStreamingActorsUpdateTimeLimit` | `float` | Maximum allowed time to spend for actor registration steps during level streaming (ms per frame) |
| `LevelStreamingComponentsRegistrationGranularity` | `int32` | Batching granularity used to register actor components during level streaming |
| `LevelStreamingUnregisterComponentsTimeLimit` | `float` | Maximum allowed time to spend while unregistering components during level streaming (ms per frame) |
| `LevelStreamingComponentsUnregistrationGranularity` | `int32` | Batching granularity used to unregister actor components during level streaming |
| `EventDrivenLoaderEnabled` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UStreamMediaSource.json -->

# UStreamMediaSource

## Inheritance

`UBaseMediaSource`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StreamUrl` | `FString` | The URL to the media stream to be played. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USubmixEffectDynamicsProcessorPreset.json -->

# USubmixEffectDynamicsProcessorPreset

## Inheritance

`USoundEffectSubmixPreset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `FSubmixEffectDynamicsProcessorSettings` | - |

## Functions

### `SetSettings`

```text
SetSettings(InSettings: FSubmixEffectDynamicsProcessorSettings &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSettings` | `FSubmixEffectDynamicsProcessorSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USubmixEffectReverbPreset.json -->

# USubmixEffectReverbPreset

## Inheritance

`USoundEffectSubmixPreset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `FSubmixEffectReverbSettings` | - |

## Functions

### `SetSettings`

```text
SetSettings(InSettings: FSubmixEffectReverbSettings &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSettings` | `FSubmixEffectReverbSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSettingsWithReverbEffect`

```text
SetSettingsWithReverbEffect(InReverbEffect: UReverbEffect *, WetLevel: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InReverbEffect` | `UReverbEffect *` | - |
| `WetLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USubmixEffectSubmixEQPreset.json -->

# USubmixEffectSubmixEQPreset

## Inheritance

`USoundEffectSubmixPreset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `FSubmixEffectSubmixEQSettings` | - |

## Functions

### `SetSettings`

```text
SetSettings(InSettings: FSubmixEffectSubmixEQSettings &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSettings` | `FSubmixEffectSubmixEQSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USubsurfaceProfile.json -->

# USubsurfaceProfile

Subsurface Scattering profile asset, can be specified at the material. Only for "Subsurface Profile" materials, is use during Screenspace Subsurface Scattering
  Don't change at runtime. All properties in here are per material - texture like variations need to come from properties that are in the GBuffer.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Settings` | `FSubsurfaceProfileStruct` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USubUVAnimation.json -->

# USubUVAnimation

SubUV animation asset, which caches bounding geometry for regions in the SubUVTexture with non-zero opacity.
  Particle emitters with a SubUV module which use this asset leverage the optimal bounding geometry to reduce overdraw.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SubUVTexture` | `UTexture2D *` | Texture to generate bounding geometry from. |
| `SubImages_Horizontal` | `int32` | The number of sub-images horizontally in the texture |
| `SubImages_Vertical` | `int32` | The number of sub-images vertically in the texture |
| `BoundingMode` | `TEnumAsByte < enum ESubUVBoundingVertexCount >` | More bounding vertices results in reduced overdraw, but adds more triangle overhead.<br>	  The eight vertex mode is best used when the SubUV texture has a lot of space to cut out that is not captured by the four vertex version,<br>	  and when the particles using the texture will be few and large. |
| `OpacitySourceMode` | `TEnumAsByte < enum EOpacitySourceMode >` | - |
| `AlphaThreshold` | `float` | Alpha channel values larger than the threshold are considered occupied and will be contained in the bounding geometry.<br>	  Raising this threshold slightly can reduce overdraw in particles using this animation asset. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/USynthComponent.json -->

# USynthComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoDestroy` | `uint8` | Auto destroy this component on completion |
| `bStopWhenOwnerDestroyed` | `uint8` | Stop sound when owner is destroyed |
| `bAllowSpatialization` | `uint8` | Is this audio component allowed to be spatialized? |
| `bOverrideAttenuation` | `uint8` | Should the Attenuation Settings asset be used (false) or should the properties set directly on the component be used for attenuation properties |
| `AttenuationSettings` | `USoundAttenuation *` | If bOverrideSettings is false, the asset to use to determine attenuation properties for sounds generated by this component |
| `AttenuationOverrides` | `FSoundAttenuationSettings` | If bOverrideSettings is true, the attenuation properties to use for sounds generated by this component |
| `ConcurrencySettings` | `USoundConcurrency *` | What sound concurrency to use for sounds generated by this audio component |
| `SoundClass` | `USoundClass *` | Sound class this sound belongs to |
| `SourceEffectChain` | `USoundEffectSourcePresetChain *` | The source effect chain to use for this sound. |
| `SoundSubmix` | `USoundSubmix *` | Submix this sound belongs to |
| `SoundSubmixSends` | `TArray < FSoundSubmixSendInfo >` | An array of submix sends. Audio from this sound will send a portion of its audio to these effects. |
| `bIsUISound` | `uint8` | Whether or not this sound plays when the game is paused in the UI |
| `Synth` | `USynthSound *` | - |
| `AudioComponent` | `UAudioComponent *` | - |

## Functions

### `Start`

```text
Start() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Returns true if this component is currently playing.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSubmixSend`

```text
SetSubmixSend(Submix: USoundSubmix *, SendLevel: float) -> void
```

Sets how much audio the sound should send to the given submix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Submix` | `USoundSubmix *` | - |
| `SendLevel` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextBinding.json -->

# UTextBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetTextValue`

```text
GetTextValue() -> FText
```

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `GetStringValue`

```text
GetStringValue() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextBlock.json -->

# UTextBlock

A simple static text widget.
 
   No Children
   Text

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text to display |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `ColorAndOpacity` | `FSlateColor` | The color of the text |
| `ColorAndOpacityDelegate` | `FGetSlateColor` | A bindable delegate for the ColorAndOpacity. |
| `Font` | `FSlateFontInfo` | The font to render the text with |
| `ShadowOffset` | `FVector2D` | The direction the shadow is cast |
| `ShadowColorAndOpacity` | `FLinearColor` | The color of the shadow |
| `ShadowColorAndOpacityDelegate` | `FGetLinearColor` | A bindable delegate for the ShadowColorAndOpacity. |
| `MinDesiredWidth` | `float` | The minimum desired size for the text |
| `AutoEllipsisText` | `bool` | - |
| `MutiEllipsisText` | `bool` | - |
| `MutiEllipsisLine` | `int32` | - |
| `bWrapWithInvalidationPanel` | `bool` | If true, it will automatically wrap this text widget with an invalidation panel |

## Functions

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FSlateColor) -> void
```

Sets the color and opacity of the text in this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FSlateColor` | The new text color and opacity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorRGBStr`

```text
SetColorRGBStr(HexString: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HexString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOpacity`

```text
SetOpacity(InOpacity: float) -> void
```

Sets the opacity of the text in this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOpacity` | `float` | The new text opacity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetShadowColorAndOpacity`

```text
SetShadowColorAndOpacity(InShadowColorAndOpacity: FLinearColor) -> void
```

Sets the color and opacity of the text drop shadow
	  Note: if opacity is zero no shadow will be drawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShadowColorAndOpacity` | `FLinearColor` | The new drop shadow color and opacity |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetShadowOffset`

```text
SetShadowOffset(InShadowOffset: FVector2D) -> void
```

Sets the offset that the text drop shadow should be drawn at

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShadowOffset` | `FVector2D` | The new offset |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFont`

```text
SetFont(InFontInfo: FSlateFontInfo) -> void
```

Dynamically set the font info for this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFontInfo` | `FSlateFontInfo` | THe new font info |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetJustification`

```text
SetJustification(InJustification: ETextJustify :: Type) -> void
```

Set the text justification for this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InJustification` | `ETextJustify :: Type` | new justification |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalJustification`

```text
SetVerticalJustification(InJustification: ETextVerticalJustify :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InJustification` | `ETextVerticalJustify :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNeedVerticalJustificationWhenOverflow`

```text
SetNeedVerticalJustificationWhenOverflow(InEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredWidth`

```text
SetMinDesiredWidth(InMinDesiredWidth: float) -> void
```

Set the minimum desired width for this text block

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredWidth` | `float` | new minimum desired width |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAutoEllipsisText`

```text
SetAutoEllipsisText(InAutoEllipsisText: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAutoEllipsisText` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWrapTextAt`

```text
SetWrapTextAt(InWrapTextAt: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWrapTextAt` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMutiEllipsisText`

```text
SetMutiEllipsisText(InMutiEllipsisText: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMutiEllipsisText` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetText`

```text
GetText() -> FText
```

Gets the widget text

**Returns**

| Type | Description |
|---|---|
| `FText` | The widget text |

### `GetLocalText`

```text
GetLocalText() -> FText
```

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `SetText`

```text
SetText(InText: FText) -> void
```

Directly sets the widget text.
	  Warning: This will wipe any binding created for the Text property!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | The text to assign to the widget |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnTextBlockTextChangeDelegate`

```text
OnTextBlockTextChangeDelegate(TextChanged: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextChanged` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextBlockWidgetStyle.json -->

# UTextBlockWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextBlockStyle` | `FTextBlockStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextLayoutWidget.json -->

# UTextLayoutWidget

Base class for all widgets that use a text layout.
  Contains the common options that should be exposed for the underlying Slate widget.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ShapedTextOptions` | `FShapedTextOptions` | Controls how the text within this widget should be shaped. |
| `Justification` | `TEnumAsByte < ETextJustify :: Type >` | How the text should be aligned with the margin. |
| `VerticalJustification` | `TEnumAsByte < ETextVerticalJustify :: Type >` | - |
| `bNeedVerticalJustificationWhenOverflow` | `bool` | Should the text still be justified vertically when it overflow its block. |
| `AutoWrapText` | `bool` | True if we're wrapping text automatically based on the computed horizontal space for this widget. |
| `WrapTextAt` | `float` | Whether text wraps onto a new line when it's length exceeds this width; if this value is zero or negative, no wrapping occurs. |
| `WrappingPolicy` | `ETextWrappingPolicy` | The wrapping policy to use. |
| `Margin` | `FMargin` | The amount of blank space left around the edges of text area. |
| `LineHeightPercentage` | `float` | The amount to scale each lines height by. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextPropertyTestObject.json -->

# UTextPropertyTestObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultedText` | `FText` | - |
| `UndefaultedText` | `FText` | - |
| `TransientText` | `FText` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextRenderComponent.json -->

# UTextRenderComponent

Renders text in the world with given font. Contains usual font related attributes such as Scale, Alignment, Color etc.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | Text content, can be multi line using   <br>as line separator |
| `TextMaterial` | `UMaterialInterface *` | Text material |
| `Font` | `UFont *` | Text font |
| `HorizontalAlignment` | `TEnumAsByte < enum EHorizTextAligment >` | Horizontal text alignment |
| `VerticalAlignment` | `TEnumAsByte < enum EVerticalTextAligment >` | Vertical text alignment |
| `TextRenderColor` | `FColor` | Color of the text, can be accessed as vertex color |
| `XScale` | `float` | Horizontal scale, default is 1.0 |
| `YScale` | `float` | Vertical scale, default is 1.0 |
| `WorldSize` | `float` | Vertical size of the fonts largest character in world units. Transform, XScale and YScale will affect final size. |
| `InvDefaultSize` | `float` | The inverse of the Font's character height. |
| `HorizSpacingAdjust` | `float` | Horizontal adjustment per character, default is 0.0 |
| `VertSpacingAdjust` | `float` | Vertical adjustment per character, default is 0.0 |
| `bAlwaysRenderAsText` | `uint32` | Allows text to draw unmodified when using debug visualization modes. |

## Functions

### `SetText`

```text
SetText(Value: FString &) -> void
```

Change the text value and signal the primitives to be rebuilt 
	  The FString variant is deprecated in favor of the FText variant

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetText`

```text
K2_SetText(Value: FText &) -> void
```

Change the text value and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTextMaterial`

```text
SetTextMaterial(Material: UMaterialInterface *) -> void
```

Change the text material and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFont`

```text
SetFont(Value: UFont *) -> void
```

Change the font and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `UFont *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizontalAlignment`

```text
SetHorizontalAlignment(Value: EHorizTextAligment) -> void
```

Change the horizontal alignment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `EHorizTextAligment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVerticalAlignment`

```text
SetVerticalAlignment(Value: EVerticalTextAligment) -> void
```

Change the vertical alignment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `EVerticalTextAligment` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTextRenderColor`

```text
SetTextRenderColor(Value: FColor) -> void
```

Change the text render color and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetXScale`

```text
SetXScale(Value: float) -> void
```

Change the text X scale and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetYScale`

```text
SetYScale(Value: float) -> void
```

Change the text Y scale and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHorizSpacingAdjust`

```text
SetHorizSpacingAdjust(Value: float) -> void
```

Change the text horizontal spacing adjustment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVertSpacingAdjust`

```text
SetVertSpacingAdjust(Value: float) -> void
```

Change the text vertical spacing adjustment and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldSize`

```text
SetWorldSize(Value: float) -> void
```

Change the world size of the text and signal the primitives to be rebuilt

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTextLocalSize`

```text
GetTextLocalSize() -> FVector
```

Get local size of text

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetTextWorldSize`

```text
GetTextWorldSize() -> FVector
```

Get world space size of text

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextTextureAtlas.json -->

# UTextTextureAtlas

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextAtlases` | `TArray < UTexture2D * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTexture.json -->

# UTexture

## Inheritance

`UObject` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightingGuid` | `FGuid` | Unique ID for this material, used for caching during distributed lighting |
| `LODBias` | `int32` | --------------------------------------------------------------------------<br>	--------------------------------------------------------------------------<br>	 A bias to the index of the top mip level to use. |
| `ExpectedQualityLimit` | `FExpectedQuality` | - |
| `NumCinematicMipLevels` | `int32` | Number of mip-levels to use for cinematic quality. |
| `SRGB` | `uint32` | This should be unchecked if using alpha channels individually as masks. |
| `bNotUsedInUltimateHighQuality` | `uint32` | - |
| `bNotUsedInHighQuality` | `uint32` | - |
| `bNotUsedInMediumQuality` | `uint32` | - |
| `bNotUsedInLowQuality` | `uint32` | - |
| `NeverStream` | `uint32` | - |
| `bNoTiling` | `uint32` | If true, the RHI texture will be created using TexCreate_NoTiling |
| `bUseCinematicMipLevels` | `uint32` | Whether to use the extra cinematic quality mip-levels, when we're forcing mip-levels to be resident. |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `CachedCombinedLODBias` | `int32` | Cached combined group and texture LOD bias to use. |
| `bAsyncResourceReleaseHasBeenStarted` | `uint32` | Whether the async resource release process has already been kicked off or not |
| `CompressionSettings` | `TEnumAsByte < enum TextureCompressionSettings >` | Compression settings to use when building the texture. |
| `Filter` | `TEnumAsByte < enum TextureFilter >` | The texture filtering mode to use when sampling this texture. |
| `LODGroup` | `TEnumAsByte < enum TextureGroup >` | Texture group this texture belongs to |
| `CrunchSetting` | `TEnumAsByte < enum ETextureCrunchSetting >` | - |
| `bOverrideCrunchCompressionAmount` | `uint32` | - |
| `CrunchCompressionAmount` | `float` | - |
| `BasisSetting` | `TEnumAsByte < enum ETextureBasisSetting >` | - |
| `bOverrideBasisCompressionAmount` | `uint32` | - |
| `BasisCompressionAmount` | `float` | - |
| `Source` | `FTextureSource` | --------------------------------------------------------------------------<br>	-------------------------------------------------------------------------- |
| `SourceFilePath_DEPRECATED` | `FString` | - |
| `AssetImportData` | `UAssetImportData *` | - |
| `AdjustBrightness` | `float` | Static texture brightness adjustment (scales HSV value.)  (Non-destructive; Requires texture source art to be available.) |
| `AdjustBrightnessCurve` | `float` | Static texture curve adjustment (raises HSV value to the specified power.)  (Non-destructive; Requires texture source art to be available.) |
| `AdjustVibrance` | `float` | Static texture "vibrance" adjustment (0 - 1) (HSV saturation algorithm adjustment.)  (Non-destructive; Requires texture source art to be available.) |
| `AdjustSaturation` | `float` | Static texture saturation adjustment (scales HSV saturation.)  (Non-destructive; Requires texture source art to be available.) |
| `AdjustRGBCurve` | `float` | Static texture RGB curve adjustment (raises linear-space RGB color to the specified power.)  (Non-destructive; Requires texture source art to be available.) |
| `AdjustHue` | `float` | Static texture hue adjustment (0 - 360) (offsets HSV hue by value in degrees.)  (Non-destructive; Requires texture source art to be available.) |
| `AdjustMinAlpha` | `float` | Remaps the alpha to the specified minmax range, defines the new value of 0 (Non-destructive; Requires texture source art to be available.) |
| `AdjustMaxAlpha` | `float` | Remaps the alpha to the specified minmax range, defines the new value of 1 (Non-destructive; Requires texture source art to be available.) |
| `CompressionNoAlpha` | `uint32` | If enabled, the texture's alpha channel will be discarded during compression |
| `CompressionNone` | `uint32` | - |
| `DeferCompression` | `uint32` | If enabled, defer compression of the texture until save. |
| `MaxTextureSize` | `int32` | The maximum resolution for generated textures. A value of 0 means the maximum size for the format on each platform, except HDR longlat cubemaps, which default to a resolution of 512. |
| `MaxTextureSizeHD` | `int32` | - |
| `MaxTextureSizeWinOB` | `int32` | - |
| `MaxTextureSizePC` | `int32` | - |
| `CompressionQuality` | `TEnumAsByte < enum ETextureCompressionQuality >` | The compression quality for generated textures. |
| `bDitherMipMapAlpha` | `uint32` | When true, the alpha channel of mip-maps and the base image are dithered for smooth LOD transitions. |
| `AlphaCoverageThresholds` | `FVector4` | Alpha values per channel to compare to when preserving alpha coverage. |
| `bPreserveBorder` | `uint32` | When true the texture's border will be preserved during mipmap generation. |
| `bFlipGreenChannel` | `uint32` | When true the texture's green channel will be inverted. This is useful for some normal maps. |
| `bForcePVRTC4` | `uint32` | For DXT1 textures, setting this will cause the texture to be twice the size, but better looking, on iPhone |
| `bUseASTCForCookTargetPlatform` | `uint32` | Whether to use astc for cook target platform . |
| `PowerOfTwoMode` | `TEnumAsByte < enum ETexturePowerOfTwoSetting :: Type >` | How to pad the texture to a power of 2 size (if necessary) |
| `PaddingColor` | `FColor` | The color used to pad the texture out if it is resized due to PowerOfTwoMode |
| `bChromaKeyTexture` | `bool` | Whether to chroma key the image, replacing any pixels that match ChromaKeyColor with transparent black |
| `ChromaKeyThreshold` | `float` | The threshold that components have to match for the texel to be considered equal to the ChromaKeyColor when chroma keying (<=, set to 0 to require a perfect exact match) |
| `ChromaKeyColor` | `FColor` | The color that will be replaced with transparent black if chroma keying is enabled |
| `MipGenSettings` | `TEnumAsByte < enum TextureMipGenSettings >` | Per asset specific setting to define the mip-map generation properties like sharpening and kernel size. |
| `bUseNewFilter_UE4` | `bool` | New Tex Mip Filter  Tex MaxSize Filter from UE5 |
| `FloodFillByNearestThreshold` | `float` | For masked texture which using alpha channel as the clip value, flood fill background zone RGB values with nearest valid pixels.<br>	  Mask texture should setup this to actual clip value to avoid polluting color in high mip level.<br>	  All pixels has lower alpha value than this threshold will be filled by nearest valid pixel(which has higher value than threshold). Value of 0.0 means no flood fill process at all. |
| `CompositeTexture` | `UTexture *` | Can be defined to modify the roughness based on the normal map variation (mostly from mip maps).<br>	  MaxAlpha comes in handy to define a base roughness if no source alpha was there.<br>	  Make sure the normal map has at least as many mips as this texture. |
| `CompositeTextureMode` | `TEnumAsByte < enum ECompositeTextureMode >` | defines how the CompositeTexture is applied, e.g. CTM_RoughnessFromNormalAlpha |
| `CompositePower` | `float` | default 1, high values result in a stronger effect e.g 1, 2, 4, 8<br>	  this is no slider because the texture update would not be fast enough |
| `bIsCookingHDTexture` | `bool` | - |
| `bIsCookingPCTexture` | `bool` | - |
| `bUseLegacyGamma` | `uint32` | A flag for using the simplified legacy gamma space e.g pow(color,12.2) for converting from FColor to FLinearColor, if we're doing sRGB. |
| `bKeepSourceDataWhenCookingUGCEditor` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTexture2D.json -->

# UTexture2D

## Inheritance

`UTexture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StreamingIndex` | `int32` | FStreamingTexture index used by the texture streaming system. |
| `LevelIndex` | `int32` | Level scope index of this texture. It is used to reduce the amount of lookup to map a texture to its level index.<br>	  Useful when building texture streaming data, as well as when filling the texture streamer with precomputed data.<br>      It relates to FStreamingTextureBuildInfo::TextureLevelIndex and also the index in ULevel::StreamingTextureGuids. <br>	  Default value of -1, indicates that the texture has an unknown index (not yet processed). At level load time, <br>	  -2 is also used to indicate that the texture has been processed but no entry were found in the level table.<br>	  After any of these processes, the LevelIndex is reset to INDEX_NONE. Making it ready for the next level task. |
| `FirstResourceMemMip` | `int32` | keep track of first mip level used for ResourceMem creation |
| `bSuperSamplingMipBiasResponsive` | `uint32` | - |
| `PerTextureMipBias` | `int32` | - |
| `bUseForTerrainRVT` | `uint32` | - |
| `ImportedSize` | `FIntPoint` | The imported size of the texture. Only valid on cooked builds when texture source is not<br>	  available. Access ONLY via the GetImportedSize() accessor! |
| `ForceMipLevelsToBeResidentTimestamp` | `double` | WorldSettings timestamp that tells the streamer to force all miplevels to be resident up until that time. |
| `bTemporarilyDisableStreaming` | `bool` | True if streaming is temporarily disabled so we can update subregions of this texture's resource <br>	without streaming clobbering it. Automatically cleared before saving. |
| `bIsStreamable` | `bool` | Whether the texture is currently streamable or not. |
| `bHasStreamingUpdatePending` | `uint32` | Whether some mips might be streamed soon. If false, the texture is not planned resolution will be stable. |
| `bForceMiplevelsToBeResident` | `uint32` | Override whether to fully stream even if texture hasn't been rendered. |
| `bIgnoreStreamingMipBias` | `uint32` | Ignores the streaming mip bias used to accommodate memory constraints. |
| `bGlobalForceMipLevelsToBeResident` | `uint32` | Global and serialized version of ForceMiplevelsToBeResident. |
| `bIsTransient` | `uint32` | - |
| `AddressX` | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the X axis. |
| `AddressY` | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the Y axis. |
| `NotInlineMipCountOverride` | `uint8` | - |
| `bTryDownloadWhenSplit` | `bool` | - |
| `bHasBeenPaintedInEditor` | `uint32` | Whether the texture has been painted in the editor. |

## Functions

### `Blueprint_GetSizeX`

```text
Blueprint_GetSizeX() -> int32
```

Gets the X size of the texture, in pixels

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Blueprint_GetSizeY`

```text
Blueprint_GetSizeY() -> int32
```

Gets the Y size of the texture, in pixels

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RefreshBulkNotExistsMipCount`

```text
RefreshBulkNotExistsMipCount() -> ENGINE_API void
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`

