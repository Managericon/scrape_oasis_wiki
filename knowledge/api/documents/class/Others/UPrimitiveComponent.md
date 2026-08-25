---
id: "api:class:UPrimitiveComponent"
title: "UPrimitiveComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPrimitiveComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
