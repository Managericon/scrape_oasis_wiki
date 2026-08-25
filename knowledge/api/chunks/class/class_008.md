---
id: "api-chunk:class:8"
title: "Oasis API class chunk 8"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTexture2DArray.json -->

# UTexture2DArray

## Inheritance

`UTexture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AddressX` | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the X axis. |
| `AddressY` | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the Y axis. |
| `AddressZ` | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the Z axis. |

## Functions

### `FixTexture2dArrayData`

```text
FixTexture2dArrayData() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTexture2DDynamic.json -->

# UTexture2DDynamic

## Inheritance

`UTexture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Format` | `TEnumAsByte < enum EPixelFormat >` | The format of the texture. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextureLightProfile.json -->

# UTextureLightProfile

## Inheritance

`UTexture2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Brightness` | `float` | Light brightness in Lumens, imported from IES profile, <= 0 if the profile is used for masking only. Use with InverseSquareFalloff. |
| `TextureMultiplier` | `float` | Multiplier to map texture value to result to integrate over the sphere to 1.0f |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextureLODSettings.json -->

# UTextureLODSettings

Structure containing all information related to an LOD group and providing helper functions to calculate
  the LOD bias of a given group.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureLODGroups` | `TArray < FTextureLODGroup >` | Array of LOD settings with entries per group. |
| `TextureLODGroupsFilterCache` | `TMap < TEnumAsByte < TextureGroup > , ETextureSamplerFilter >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextureProperty.json -->

# UTextureProperty

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Propertys` | `TArray < FCollectionStructParameter >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextureRenderTarget.json -->

# UTextureRenderTarget

## Inheritance

`UTexture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetGamma` | `float` | Will override FTextureRenderTarget2DResource::GetDisplayGamma if > 0. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextureRenderTarget2D.json -->

# UTextureRenderTarget2D

TextureRenderTarget2D
 
  2D render target texture resource. This can be used as a target
  for rendering as well as rendered as a regular 2D texture resource.

## Inheritance

`UTextureRenderTarget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SizeX` | `int32` | The width of the texture. |
| `SizeY` | `int32` | The height of the texture. |
| `ClearColor` | `FLinearColor` | the color the texture is cleared to |
| `AddressX` | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the X axis. |
| `AddressY` | `TEnumAsByte < enum TextureAddress >` | The addressing mode to use for the Y axis. |
| `bForceLinearGamma` | `uint32` | True to force linear gamma space for this render target |
| `bHDR_DEPRECATED` | `uint32` | Whether to support storing HDR values, which requires more memory. |
| `RenderTargetFormat` | `TEnumAsByte < enum ETextureRenderTargetFormat >` | Format of the texture render target. <br>	  Data written to the render target will be quantized to this format, which can limit the range and precision.<br>	  The largest format (RTF_RGBA32f) uses 16x more memory and bandwidth than the smallest (RTF_R8) and can greatly affect performance.  <br>	  Use the smallest format that has enough precision and range for what you are doing. |
| `bGPUSharedFlag` | `uint32` | Whether to support GPU sharing of the underlying native texture resource. |
| `bAutoGenerateMips` | `uint32` | Whether to support Mip maps for this render target texture |
| `OverrideFormat` | `TEnumAsByte < enum EPixelFormat >` | Normally the format is derived from RenderTargetFormat, this allows code to set the format explicitly. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTextureRenderTargetCube.json -->

# UTextureRenderTargetCube

TextureRenderTargetCube
 
  Cube render target texture resource. This can be used as a target
  for rendering as well as rendered as a regular cube texture resource.

## Inheritance

`UTextureRenderTarget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SizeX` | `int32` | The width of the texture. |
| `ClearColor` | `FLinearColor` | the color the texture is cleared to |
| `OverrideFormat` | `TEnumAsByte < enum EPixelFormat >` | The format of the texture data.											<br>	 Normally the format is derived from bHDR, this allows code to set the format explicitly. |
| `bHDR` | `uint32` | Whether to support storing HDR values, which requires more memory. |
| `bForceLinearGamma` | `uint32` | True to force linear gamma space for this render target |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UThrobber.json -->

# UThrobber

A Throbber widget that shows several zooming circles in a row.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumberOfPieces` | `int32` | How many pieces there are |
| `bAnimateHorizontally` | `bool` | Should the pieces animate horizontally? |
| `bAnimateVertically` | `bool` | Should the pieces animate vertically? |
| `bAnimateOpacity` | `bool` | Should the pieces animate their opacity? |
| `PieceImage_DEPRECATED` | `USlateBrushAsset *` | Image to use for each segment of the throbber |
| `Image` | `FSlateBrush` | - |

## Functions

### `SetNumberOfPieces`

```text
SetNumberOfPieces(InNumberOfPieces: int32) -> void
```

Sets how many pieces there are

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNumberOfPieces` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnimateHorizontally`

```text
SetAnimateHorizontally(bInAnimateHorizontally: bool) -> void
```

Sets whether the pieces animate horizontally.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAnimateHorizontally` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnimateVertically`

```text
SetAnimateVertically(bInAnimateVertically: bool) -> void
```

Sets whether the pieces animate vertically.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAnimateVertically` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnimateOpacity`

```text
SetAnimateOpacity(bInAnimateOpacity: bool) -> void
```

Sets whether the pieces animate their opacity.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInAnimateOpacity` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTileMapBlueprintLibrary.json -->

# UTileMapBlueprintLibrary

A collection of utility methods for working with tile map components
 
  @see UPaperTileMap, UPaperTileMapComponent

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `GetTileUserData`

```text
GetTileUserData(Tile: FPaperTileInfo) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tile` | `FPaperTileInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetTileTransform`

```text
GetTileTransform(Tile: FPaperTileInfo) -> FTransform
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tile` | `FPaperTileInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `BreakTile`

```text
BreakTile(Tile: FPaperTileInfo, TileIndex: int32 &, TileSet: UPaperTileSet * &, bFlipH: bool &, bFlipV: bool &, bFlipD: bool &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tile` | `FPaperTileInfo` | - |
| `TileIndex` | `int32 &` | - |
| `TileSet` | `UPaperTileSet * &` | - |
| `bFlipH` | `bool &` | - |
| `bFlipV` | `bool &` | - |
| `bFlipD` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeTile`

```text
MakeTile(TileIndex: int32, TileSet: UPaperTileSet *, bFlipH: bool, bFlipV: bool, bFlipD: bool) -> FPaperTileInfo
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TileIndex` | `int32` | - |
| `TileSet` | `UPaperTileSet *` | - |
| `bFlipH` | `bool` | - |
| `bFlipV` | `bool` | - |
| `bFlipD` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FPaperTileInfo` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTileView.json -->

# UTileView

A flow panel that presents the contents as a set of tiles all uniformly sized.

## Inheritance

`UTableViewBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemWidth` | `float` | - |
| `ItemHeight` | `float` | - |
| `Items` | `TArray < UObject * >` | - |
| `SelectionMode` | `TEnumAsByte < ESelectionMode :: Type >` | - |
| `OnGenerateTileEvent` | `FOnGenerateRowUObject` | - |

## Functions

### `SetItemWidth`

```text
SetItemWidth(Width: float) -> void
```

Set item width

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Width` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetItemHeight`

```text
SetItemHeight(Height: float) -> void
```

Set item height

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Height` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestListRefresh`

```text
RequestListRefresh() -> void
```

Refreshes the list

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTimelineComponent.json -->

# UTimelineComponent

TimelineComponent holds a series of events, floats, vectors or colors with associated keyframes.
  Events can be triggered at keyframes along the timeline. 
  Floats, vectors, and colors are interpolated between keyframes along the timeline.

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TheTimeline` | `FTimeline` | The actual timeline structure |
| `bIgnoreTimeDilation` | `uint32` | True if global time dilation should be ignored by this timeline, false otherwise. |

## Functions

### `Play`

```text
Play() -> ENGINE_API void
```

Start playback of timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `PlayFromStart`

```text
PlayFromStart() -> ENGINE_API void
```

Start playback of timeline from the start

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `Reverse`

```text
Reverse() -> ENGINE_API void
```

Start playback of timeline in reverse

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ReverseFromEnd`

```text
ReverseFromEnd() -> ENGINE_API void
```

Start playback of timeline in reverse from the end

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `Stop`

```text
Stop() -> ENGINE_API void
```

Stop playback of timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `IsPlaying`

```text
IsPlaying() -> ENGINE_API bool
```

Get whether this timeline is playing or not.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `IsReversing`

```text
IsReversing() -> ENGINE_API bool
```

Get whether we are reversing or not

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetPlaybackPosition`

```text
SetPlaybackPosition(NewPosition: float, bFireEvents: bool, bFireUpdate: bool) -> ENGINE_API void
```

Jump to a position in the timeline.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPosition` | `float` | - |
| `bFireEvents` | `bool` | If true, event functions that are between current position and new playback position will fire. |
| `bFireUpdate` | `bool` | If true, the update output exec will fire after setting the new playback position. |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetPlaybackPosition`

```text
GetPlaybackPosition() -> ENGINE_API float
```

Get the current playback position of the Timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `SetLooping`

```text
SetLooping(bNewLooping: bool) -> ENGINE_API void
```

true means we would loop, false means we should not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `IsLooping`

```text
IsLooping() -> ENGINE_API bool
```

Get whether we are looping or not

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetPlayRate`

```text
SetPlayRate(NewRate: float) -> ENGINE_API void
```

Sets the new play rate for this timeline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetPlayRate`

```text
GetPlayRate() -> ENGINE_API float
```

Get the current play rate for this timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `SetNewTime`

```text
SetNewTime(NewTime: float) -> ENGINE_API void
```

Set the new playback position time to use

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetTimelineLength`

```text
GetTimelineLength() -> ENGINE_API float
```

Get length of the timeline

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | - |

### `SetTimelineLength`

```text
SetTimelineLength(NewLength: float) -> ENGINE_API void
```

Set length of the timeline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLength` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetTimelineLengthMode`

```text
SetTimelineLengthMode(NewLengthMode: ETimelineLengthMode) -> ENGINE_API void
```

Sets the length mode of the timeline

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLengthMode` | `ETimelineLengthMode` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetIgnoreTimeDilation`

```text
SetIgnoreTimeDilation(bNewIgnoreTimeDilation: bool) -> ENGINE_API void
```

Set whether to ignore time dilation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewIgnoreTimeDilation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetIgnoreTimeDilation`

```text
GetIgnoreTimeDilation() -> ENGINE_API bool
```

Get whether to ignore time dilation.

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetFloatCurve`

```text
SetFloatCurve(NewFloatCurve: UCurveFloat *, FloatTrackName: FName) -> ENGINE_API void
```

Update a certain float track's curve

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFloatCurve` | `UCurveFloat *` | - |
| `FloatTrackName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetVectorCurve`

```text
SetVectorCurve(NewVectorCurve: UCurveVector *, VectorTrackName: FName) -> ENGINE_API void
```

Update a certain vector track's curve

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewVectorCurve` | `UCurveVector *` | - |
| `VectorTrackName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetLinearColorCurve`

```text
SetLinearColorCurve(NewLinearColorCurve: UCurveLinearColor *, LinearColorTrackName: FName) -> ENGINE_API void
```

Update a certain linear color track's curve

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLinearColorCurve` | `UCurveLinearColor *` | - |
| `LinearColorTrackName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `OnRep_Timeline`

```text
OnRep_Timeline() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTimelineTemplate.json -->

# UTimelineTemplate

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimelineLength` | `float` | Length of this timeline |
| `LengthMode` | `TEnumAsByte < ETimelineLengthMode >` | How we want the timeline to determine its own length (e.g. specified length, last keyframe) |
| `bAutoPlay` | `uint32` | If we want the timeline to auto-play |
| `bLoop` | `uint32` | If we want the timeline to loop |
| `bReplicated` | `uint32` | If we want the timeline to loop |
| `bValidatedAsWired` | `uint32` | Compiler Validated As Wired up |
| `bIgnoreTimeDilation` | `uint32` | If we want the timeline to ignore global time dilation |
| `EventTracks` | `TArray < struct FTTEventTrack >` | Set of event tracks |
| `FloatTracks` | `TArray < struct FTTFloatTrack >` | Set of float interpolation tracks |
| `VectorTracks` | `TArray < struct FTTVectorTrack >` | Set of vector interpolation tracks |
| `LinearColorTracks` | `TArray < struct FTTLinearColorTrack >` | Set of linear color interpolation tracks |
| `MetaDataArray` | `TArray < struct FBPVariableMetaDataEntry >` | Metadata information for this timeline |
| `TimelineGuid` | `FGuid` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTireType.json -->

# UTireType

DEPRECATED - Only used to allow conversion to new TireConfig in PhysXVehicles plugin

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FrictionScale` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTouchInterface.json -->

# UTouchInterface

Defines an interface by which touch input can be controlled using any number of buttons and virtual joysticks

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Controls` | `TArray < FTouchInputControl >` | - |
| `ActiveOpacity` | `float` | - |
| `InactiveOpacity` | `float` | - |
| `TimeUntilDeactive` | `float` | - |
| `TimeUntilReset` | `float` | - |
| `ActivationDelay` | `float` | - |
| `bPreventRecenter` | `bool` | - |
| `StartupDelay` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UTwitterIntegrationBase.json -->

# UTwitterIntegrationBase

## Inheritance

`UPlatformInterfaceBase`

## Functions

### `Init`

```text
Init() -> void
```

Perform any needed initialization

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanShowTweetUI`

```text
CanShowTweetUI() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the user is allowed to use the Tweet UI |

### `ShowTweetUI`

```text
ShowTweetUI(InitialMessage: FString &, URL: FString &, Picture: FString &) -> bool
```

Kicks off a tweet, using the platform to show the UI. If this returns false, or you are on a platform that doesn't support the UI,
	  you can use the TwitterRequest method to perform a manual tweet using the Twitter API

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InitialMessage` | `FString &` | [optional] Initial message to show |
| `URL` | `FString &` | [optional] URL to attach to the tweet |
| `Picture` | `FString &` | [optional] Name of a picture (stored locally, platform subclass will do the searching for it) to add to the tweet |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if a UI was displayed for the user to interact with, and a TID_TweetUIComplete will be sent |

### `AuthorizeAccounts`

```text
AuthorizeAccounts() -> bool
```

Starts the process of authorizing the local user(s). When TID_AuthorizeComplete is called, then GetNumAccounts() 
	  will return a valid number of accounts

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the authorization process started, and TID_AuthorizeComplete delegates will be called |

### `GetNumAccounts`

```text
GetNumAccounts() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of accounts that were authorized |

### `GetAccountName`

```text
GetAccountName(AccountIndex: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AccountIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the display name of the given Twitter account |

### `TwitterRequest`

```text
TwitterRequest(URL: FString &, ParamKeysAndValues: TArray < FString > &, RequestMethod: ETwitterRequestMethod, AccountIndex: int32) -> bool
```

Kicks off a generic twitter request

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString &` | The URL for the twitter request |
| `ParamKeysAndValues` | `TArray < FString > &` | - |
| `RequestMethod` | `ETwitterRequestMethod` | - |
| `AccountIndex` | `int32` | A user index if an account is needed, or -1 if an account isn't needed for the request |

**Returns**

| Type | Description |
|---|---|
| `bool` | true the request was sent off, and a TID_RequestComplete |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUGCBackpackAvatarHandle.json -->

# UUGCBackpackAvatarHandle

外显装备基类

## Inheritance

`UBackpackAvatarHandle` -> `IUGCItemDataInterface` -> `IUGCObjectItemTableInterface` -> `IUGCItemEquipmentInterface` -> `IUGCItemEquipTargetInterface` -> `IUGCCommonDeadDropItemInterface` -> `IUGCBattleEquipHandleAttachInterface`

## Events

### `OnDurabilityChanged`

```text
OnDurabilityChanged(OriginDurability: float, ChangedDurability: float) -> void
```

当物品耐久度变化时执行
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OriginDurability` | `float` | 原始耐久度 |
| `ChangedDurability` | `float` | 改变后的耐久度 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUGCCommonProduceDropItemComponent.json -->

# UUGCCommonProduceDropItemComponent

掉落组件

## Inheritance

`UCommonProduceDropItemBaseComponent` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StepTime` | `int32` | 每波掉落次数 |
| `StepGap` | `float` | 每波掉落间隔 |
| `DelayDropTime` | `float` | 起始掉落延迟 |
| `StrategySelector` | `FUGCDropItemStrategySelector` | 掉落方案配置 |

## Functions

### `StartDrop`

```text
StartDrop(DropItemActor: AActor *, Killer: AController *, TraceIgnoreActors: TArray < AActor * >, AttachComponent: USceneComponent *) -> void
```

按照配置进行一次掉落行为
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DropItemActor` | `AActor *` | 需要掉落物资的Actor，一般为配置掉落物组件的Actor本身 |
| `Killer` | `AController *` | 击杀者或交互者，当掉落物类型为直接进入背包时或者掉落方向为面相玩家时必须，其他时候可以为Null |
| `TraceIgnoreActors` | `TArray < AActor * >` | 掉落检测射线忽略的Actor数组 |
| `AttachComponent` | `USceneComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StartDropByProduceID`

```text
StartDropByProduceID(ProduceID: int32, ProduceGroupID: int32, EntityType: EUGCGenerateItemEntityType, RelatedPlayer: ACharacter *) -> void
```

指定掉落方案进行一次 Wrapper 掉落
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProduceID` | `int32` | 掉落方案ID |
| `ProduceGroupID` | `int32` | 掉落组方案ID(掉落组ID不为-1，掉落组ID生效。掉落组ID为-1,则掉落ID生效) |
| `EntityType` | `EUGCGenerateItemEntityType` | 掉落物类型 |
| `RelatedPlayer` | `ACharacter *` | 当掉落物方向为面相玩家时必须，当掉落物类型为进入背包时必须，其他时候可以为Null |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBluePrintDropItemConfig`

```text
SetBluePrintDropItemConfig(ConfigItem: TArray < FUGCGenerateDropItemInfo >, EntityType: EUGCGenerateItemEntityType, ConfigID: int32) -> void
```

动态设置掉落物组，会强制将掉落物列表生成方式改为蓝图配置
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigItem` | `TArray < FUGCGenerateDropItemInfo >` | 需要动态修改的掉落物蓝图配置 |
| `EntityType` | `EUGCGenerateItemEntityType` | 掉落物类型 |
| `ConfigID` | `int32` | 需要修改的配置项索引，索引无效时修改失败 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetProduceIDConfig`

```text
SetProduceIDConfig(InProduceID: int32, ProduceGroupID: int32, EntityType: EUGCGenerateItemEntityType, ConfigID: int32) -> void
```

动态设置掉落串，会强制将掉落物列表生成方式改为读表
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InProduceID` | `int32` | 需要动态修改的掉落方案ID |
| `ProduceGroupID` | `int32` | 需要动态修改的掉落方案组ID |
| `EntityType` | `EUGCGenerateItemEntityType` | 掉落物类型 |
| `ConfigID` | `int32` | 需要修改的配置项索引，索引无效时修改失败 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddDropConfig`

```text
AddDropConfig(InProduceID: int32, ProduceGroupID: int32, ConfigItem: TArray < FUGCGenerateDropItemInfo >, EntityType: EUGCGenerateItemEntityType) -> void
```

动态添加掉落，按照选择类型添加
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InProduceID` | `int32` | 需要添加的掉落方案ID，如果不需要添加读表配置方案请传参-1 |
| `ProduceGroupID` | `int32` | 需要添加的掉落方案组ID，如果不需要添加读表配置方案请传参-1 |
| `ConfigItem` | `TArray < FUGCGenerateDropItemInfo >` | 需要添加的掉落物蓝图配置 |
| `EntityType` | `EUGCGenerateItemEntityType` | 掉落物类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearDropConfig`

```text
ClearDropConfig(SelectType: EUGCDropItemListGeneratorType) -> void
```

动态清空配置，蓝图或读表
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectType` | `EUGCDropItemListGeneratorType` | 需要清空的配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGeneratorType`

```text
SetGeneratorType(SelectType: EUGCDropItemListGeneratorType) -> void
```

动态修改掉落物列表生成方式
	  生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectType` | `EUGCDropItemListGeneratorType` | 生成方式 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicCenterOffset`

```text
SetDynamicCenterOffset(InDynamicCenterOffset: FVector) -> void
```

动态设置掉落圆环偏移
      生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDynamicCenterOffset` | `FVector` | 偏移量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnDropOver`

```text
OnDropOver() -> void
```

当前掉落结束后触发
	  最后一个拾取物被创建时就触发，不会等抛物线动效走完
	  广播范围：DS

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUGCGamePartConfig.json -->

# UUGCGamePartConfig

GamePart配置基类

## Inheritance

`UPrimaryDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GamePartName` | `FName` | GamePart名称 |
| `DependentGameParts` | `TArray < FName >` | 依赖的的GamePart列表 |
| `GlobalActorClass` | `TSubclassOf < AActor >` | GlobalActor类配置 |
| `PlayerComponentConfigs` | `TArray < FUGCGamePartPlayerComponentConfig >` | GamePart PlayerComponent配置列表 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUGCItemWarehouseBase.json -->

# UUGCItemWarehouseBase

仓库对象

## Inheritance

`UObject` -> `IUGCItemContainerInterface`

## Delegates

### `ItemChangeDelegate`

```text
ItemChangeDelegate(ChangeType: const EUGCItemChangeType&, DefineID: const FItemDefineID&) -> void
```

当仓库物品实例数据发生改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangeType` | `const EUGCItemChangeType&` | - |
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemAddDelegate`

```text
ItemAddDelegate(DefineID: const FItemDefineID&) -> void
```

当仓库新增物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemUpdateDelegate`

```text
ItemUpdateDelegate(DefineID: const FItemDefineID&) -> void
```

当物品实例数据更新时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemRemoveDelegate`

```text
ItemRemoveDelegate(DefineID: const FItemDefineID&) -> void
```

当移除物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUGCMotionComponent.json -->

# UUGCMotionComponent

运动器组件

## Inheritance

`UActorComponent`

## Functions

### `StartMotion`

```text
StartMotion(ConfigID: int) -> void
```

开始运行特定运动器
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `int` | 运动器索引，默认参数-1(所有运动器) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseMotion`

```text
PauseMotion(ConfigID: int) -> void
```

停止特定运动器
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `int` | 运动器索引，默认参数-1(所有运动器) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetMotion`

```text
ResetMotion(ConfigID: int) -> void
```

重置特定运动器
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `int` | 运动器索引，默认参数-1(所有运动器) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUMGSequencePlayer.json -->

# UUMGSequencePlayer

## Inheritance

`UObject` -> `IMovieScenePlayer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | Animation being played |

## Functions

### `GetUserTag`

```text
GetUserTag() -> FName
```

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `SetUserTag`

```text
SetUserTag(InUserTag: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUserTag` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUniformGridPanel.json -->

# UUniformGridPanel

A panel that evenly divides up available space between all of its children.

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SlotPadding` | `FMargin` | Padding given to each slot |
| `MinDesiredSlotWidth` | `float` | The minimum desired width of the slots |
| `MinDesiredSlotHeight` | `float` | The minimum desired height of the slots |

## Functions

### `SetSlotPadding`

```text
SetSlotPadding(InSlotPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSlotPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredSlotWidth`

```text
SetMinDesiredSlotWidth(InMinDesiredSlotWidth: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredSlotWidth` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredSlotHeight`

```text
SetMinDesiredSlotHeight(InMinDesiredSlotHeight: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredSlotHeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddChildToUniformGrid`

```text
AddChildToUniformGrid(Content: UWidget *) -> UUniformGridSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UUniformGridSlot *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUniformGridSlot.json -->

# UUniformGridSlot

A slot for UUniformGridPanel, these slots all share the same size as the largest slot
  in the grid.

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |
| `Row` | `int32` | The row index of the cell this slot is in |
| `Column` | `int32` | The column index of the cell this slot is in |

## Functions

### `SetRow`

```text
SetRow(InRow: int32) -> void
```

Sets the row index of the slot, this determines what cell the slot is in the panel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRow` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColumn`

```text
SetColumn(InColumn: int32) -> void
```

Sets the column index of the slot, this determines what cell the slot is in the panel

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColumn` | `int32` | - |

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUniversalProjectileFilter.json -->

# UUniversalProjectileFilter

过滤器

## Inheritance

`UObject`

## Events

### `Filter`

```text
Filter(InActor: AActor *, Causer: AActor *, Instigator: AController *) -> bool
```

过滤器的过滤方法
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | 当前判断过滤的对象 |
| `Causer` | `AActor *` | 发起过滤的对象（可能为抛体，法术场等） |
| `Instigator` | `AController *` | 发起过滤的对象的Controller（一般在服务端使用） |

**Returns**

| Type | Description |
|---|---|
| `bool` | bool 过滤结果 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserDefinedEnum.json -->

# UUserDefinedEnum

An Enumeration is a list of named values.

## Inheritance

`UEnum`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DisplayNameMap` | `TMap < FName , FText >` | De-facto display names for enum entries mapped against their raw enum name (UEnum::GetNameByIndex).<br>	  To sync DisplayNameMap use FEnumEditorUtils::EnsureAllDisplayNamesExist. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserDefinedStruct.json -->

# UUserDefinedStruct

## Inheritance

`UScriptStruct`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Guid` | `FGuid` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserInterfaceSettings.json -->

# UUserInterfaceSettings

User Interface settings that control Slate and UMG.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderFocusRule` | `ERenderFocusRule` | Rule to determine if we should render the Focus Brush for widgets that have user focus. |
| `HardwareCursors` | `TMap < TEnumAsByte < EMouseCursor :: Type > , FHardwareCursorReference >` | - |
| `SoftwareCursors` | `TMap < TEnumAsByte < EMouseCursor :: Type > , FSoftClassPath >` | - |
| `DefaultCursor_DEPRECATED` | `FSoftClassPath` | - |
| `TextEditBeamCursor_DEPRECATED` | `FSoftClassPath` | - |
| `CrosshairsCursor_DEPRECATED` | `FSoftClassPath` | - |
| `HandCursor_DEPRECATED` | `FSoftClassPath` | - |
| `GrabHandCursor_DEPRECATED` | `FSoftClassPath` | - |
| `GrabHandClosedCursor_DEPRECATED` | `FSoftClassPath` | - |
| `SlashedCircleCursor_DEPRECATED` | `FSoftClassPath` | - |
| `ApplicationScale` | `float` | An optional application scale to apply on top of the custom scaling rules.  So if you want to expose a <br>	  property in your game title, you can modify this underlying value to scale the entire UI. |
| `UIScaleRule` | `EUIScalingRule` | The rule used when trying to decide what scale to apply. |
| `CustomScalingRuleClass` | `FSoftClassPath` | Set DPI Scale Rule to Custom, and this class will be used instead of any of the built-in rules. |
| `UIScaleCurve` | `FRuntimeFloatCurve` | Controls how the UI is scaled at different resolutions based on the DPI Scale Rule |
| `ExtendUIScaleCurves` | `TArray < FRuntimeFloatCurve >` | - |
| `ExtendUIScaleCurveIndex` | `int32` | - |
| `DefaultUIScaleCurveIndex` | `int32` | - |
| `bScreenAdaption` | `bool` | - |
| `bUseFixedDPIMapping` | `bool` | - |
| `FixedDPIScaleConfig` | `TArray < FFixedDPIValueEntry >` | - |
| `bUseAndroidHarmonyFixedDPIScaleConfig` | `bool` | - |
| `AndroidHarmonyFixedDPIScaleConfig` | `TMap < FString , FFixedDPIValueEntry >` | - |
| `bLoadWidgetsOnDedicatedServer` | `bool` | If false, widget references will be stripped during cook for server builds and not loaded at runtime. |
| `FixDPIScaleCurveIndex` | `int32` | - |
| `CursorClasses` | `TArray < UObject * >` | - |
| `CustomScalingRuleClassInstance` | `UClass *` | - |
| `CustomScalingRule` | `UDPICustomScalingRule *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserRefStyle.json -->

# UUserRefStyle

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RefStylesInfo` | `TArray < FUserRefStyleInfo >` | - |

## Functions

### `ResetRefStylesInfo`

```text
ResetRefStylesInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserWidget.json -->

# UUserWidget

The user widget is extensible by users through the WidgetBlueprint.

## Inheritance

`UWidget` -> `INamedSlotInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorAndOpacity` | `FLinearColor` | The color and opacity of this widget.  Tints all child widgets. |
| `ColorAndOpacityDelegate` | `FGetLinearColor` | - |
| `ForegroundColor` | `FSlateColor` | The foreground color of the widget, this is inherited by sub widgets.  Any color property<br>	  that is marked as inherit will use this color. |
| `ForegroundColorDelegate` | `FGetSlateColor` | - |
| `Padding` | `FMargin` | The padding area around the content. |
| `ActiveSequencePlayers` | `TArray < UUMGSequencePlayer * >` | All the sequence players currently playing |
| `StoppedSequencePlayers` | `TArray < UUMGSequencePlayer * >` | List of sequence players to cache and clean up when safe |
| `NamedSlotBindings` | `TArray < FNamedSlotBinding >` | Stores the widgets being assigned to named slots |
| `WidgetTree` | `UWidgetTree *` | The widget tree contained inside this user widget initialized by the blueprint |
| `bOptimiseAnimation` | `bool` | - |
| `bNoBubbleUpEvent` | `bool` | - |
| `Priority` | `int32` | - |
| `bSupportsKeyboardFocus_DEPRECATED` | `uint8` | - |
| `bIsFocusable` | `uint8` | Setting this flag to true, allows this widget to accept focus when clicked, or when navigated to. |
| `bStopAction` | `uint8` | - |
| `CanDisableDrag` | `uint8` | - |
| `bCanEverTick` | `uint8` | If a widget doesn't ever need to tick the blueprint, setting this to false is an optimization. |
| `bCanEverPaint` | `uint8` | If a widget doesn't ever need to do custom painting in the blueprint, setting this to false is an optimization. |
| `bCookedWidgetTree` | `uint8` | If this user widget was created using a cooked widget tree.  If that's true, we want to skip a lot of the normal<br>	  initialization logic for widgets, because these widgets have already been initialized. |
| `WidgetSkinProxy` | `UObject *` | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "WidgetSkin") |
| `InputComponent` | `UInputComponent *` | - |
| `AnimationCallbacks` | `TArray < FAnimationEventBinding >` | - |

## Functions

### `AddToViewport`

```text
AddToViewport(ZOrder: int32) -> void
```

Adds it to the game's viewport and fills the entire screen, unless SetDesiredSizeInViewport is called
	  to explicitly set the size.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZOrder` | `int32` | The higher the number, the more on top this widget will be. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddToPlayerScreen`

```text
AddToPlayerScreen(ZOrder: int32) -> bool
```

Adds the widget to the game's viewport in a section dedicated to the player.  This is valuable in a split screen
	  game where you need to only show a widget over a player's portion of the viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZOrder` | `int32` | The higher the number, the more on top this widget will be. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveFromViewport`

```text
RemoveFromViewport() -> void
```

Removes the widget from the viewport.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetZOrderOfViewportWidget`

```text
GetZOrderOfViewportWidget() -> int
```

Get Z-order of Viewport Widget, added by fourthchen

**Returns**

| Type | Description |
|---|---|
| `int` | - |

### `SetPositionInViewport`

```text
SetPositionInViewport(Position: FVector2D, bRemoveDPIScale: bool) -> void
```

Sets the widgets position in the viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector2D` | The 2D position to set the widget to in the viewport. |
| `bRemoveDPIScale` | `bool` | If you've already calculated inverse DPI, set this to false. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDesiredSizeInViewport`

```text
SetDesiredSizeInViewport(Size: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Size` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOffsetsInViewport`

```text
SetOffsetsInViewport(Margin: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Margin` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnchorsInViewport`

```text
SetAnchorsInViewport(Anchors: FAnchors) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Anchors` | `FAnchors` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAlignmentInViewport`

```text
SetAlignmentInViewport(Alignment: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Alignment` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAnchorsInViewport`

```text
GetAnchorsInViewport() -> FAnchors
```

**Returns**

| Type | Description |
|---|---|
| `FAnchors` | - |

### `GetAlignmentInViewport`

```text
GetAlignmentInViewport() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetIsVisible`

```text
GetIsVisible() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsInViewport`

```text
IsInViewport() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget was added to the viewport using AddToViewport. |

### `GetOwningLocalPlayer`

```text
GetOwningLocalPlayer() -> ULocalPlayer *
```

Gets the local player associated with this UI.

**Returns**

| Type | Description |
|---|---|
| `ULocalPlayer *` | The owning local player. |

### `SetOwningLocalPlayer`

```text
SetOwningLocalPlayer(LocalPlayer: ULocalPlayer *) -> void
```

Sets the player associated with this UI via LocalPlayer reference.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalPlayer` | `ULocalPlayer *` | The local player you want to be the conceptual owner of this UI. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwningPlayer`

```text
GetOwningPlayer() -> APlayerController *
```

Gets the player controller associated with this UI.

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | The player controller that owns the UI. |

### `SetOwningPlayer`

```text
SetOwningPlayer(LocalPlayerController: APlayerController *) -> void
```

Sets the local player associated with this UI via PlayerController reference.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalPlayerController` | `APlayerController *` | The PlayerController of the local player you want to be the conceptual owner of this UI. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwningPlayerPawn`

```text
GetOwningPlayerPawn() -> APawn *
```

Gets the player pawn associated with this UI.

**Returns**

| Type | Description |
|---|---|
| `APawn *` | Gets the owning player pawn that's owned by the player controller assigned to this widget. |

### `PreConstruct`

```text
PreConstruct(IsDesignTime: bool) -> void
```

Called by both the game and the editor.  Allows users to run initial setup for their widgets to better preview
	  the setup in the designer and since generally that same setup code is required at runtime, it's called there
	  as well.
	 
	  WARNING
	  This is intended purely for cosmetic updates using locally owned data, you can not safely access any game related
	  state, if you call something that doesn't expect to be run at editor time, you may crash the editor.
	 
	  In the event you save the asset with blueprint code that causes a crash on evaluation.  You can turn off
	  PreConstruct evaluation in the Widget Designer settings in the Editor Preferences.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsDesignTime` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Construct`

```text
Construct() -> void
```

Called after the underlying slate widget is constructed.  Depending on how the slate object is used
	  this event may be called multiple times due to adding and removing from the hierarchy.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ConstructForLua`

```text
ConstructForLua() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Destruct`

```text
Destruct() -> void
```

Called when a widget is no longer referenced causing the slate resource to destroyed.  Just like
	  Construct this event can be called multiple times.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Tick`

```text
Tick(MyGeometry: FGeometry, InDeltaTime: float) -> void
```

Ticks this widget.  Override in derived classes, but always call the parent implementation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The space allotted for this widget |
| `InDeltaTime` | `float` | Real time passed since last tick |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPaint`

```text
OnPaint(Context: FPaintContext &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInteractable`

```text
IsInteractable() -> bool
```

Gets a value indicating if the widget is interactive.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnFocusReceived`

```text
OnFocusReceived(MyGeometry: FGeometry, InFocusEvent: FFocusEvent) -> FEventReply
```

Called when keyboard focus is given to this widget.  This event does not bubble.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnFocusLost`

```text
OnFocusLost(InFocusEvent: FFocusEvent) -> void
```

Called when this widget loses focus.  This event does not bubble.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAddedToFocusPath`

```text
OnAddedToFocusPath(InFocusEvent: FFocusEvent) -> void
```

If focus is gained on on this widget or on a child widget and this widget is added
	  to the focus path, and wasn't previously part of it, this event is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRemovedFromFocusPath`

```text
OnRemovedFromFocusPath(InFocusEvent: FFocusEvent) -> void
```

If focus is lost on on this widget or on a child widget and this widget is
	  no longer part of the focus path.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnKeyChar`

```text
OnKeyChar(MyGeometry: FGeometry, InCharacterEvent: FCharacterEvent) -> FEventReply
```

Called after a character is entered while this widget has focus

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InCharacterEvent` | `FCharacterEvent` | Character event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnPreviewKeyDown`

```text
OnPreviewKeyDown(MyGeometry: FGeometry, InKeyEvent: FKeyEvent) -> FEventReply
```

Called after a key (keyboard, controller, ...) is pressed when this widget or a child of this widget has focus
	  If a widget handles this event, OnKeyDown will not be passed to the focused widget.
	 
	  This event is primarily to allow parent widgets to consume an event before a child widget processes
	  it and it should be used only when there is no better design alternative.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InKeyEvent` | `FKeyEvent` | Key event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnKeyDown`

```text
OnKeyDown(MyGeometry: FGeometry, InKeyEvent: FKeyEvent) -> FEventReply
```

Called after a key (keyboard, controller, ...) is pressed when this widget has focus (this event bubbles if not handled)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InKeyEvent` | `FKeyEvent` | Key event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnKeyUp`

```text
OnKeyUp(MyGeometry: FGeometry, InKeyEvent: FKeyEvent) -> FEventReply
```

Called after a key (keyboard, controller, ...) is released when this widget has focus

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InKeyEvent` | `FKeyEvent` | Key event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnAnalogValueChanged`

```text
OnAnalogValueChanged(MyGeometry: FGeometry, InAnalogInputEvent: FAnalogInputEvent) -> FEventReply
```

Called when an analog value changes on a button that supports analog

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InAnalogInputEvent` | `FAnalogInputEvent` | Analog Event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnMouseButtonDown`

```text
OnMouseButtonDown(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

The system calls this method to notify the widget that a mouse button was pressed within it. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnPreviewMouseButtonDown`

```text
OnPreviewMouseButtonDown(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

Just like OnMouseButtonDown, but tunnels instead of bubbling.
	  If this even is handled, OnMouseButtonDown will not be sent.
	  
	  Use this event sparingly as preview events generally make UIs more
	  difficult to reason about.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnMouseButtonUp`

```text
OnMouseButtonUp(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

The system calls this method to notify the widget that a mouse button was release within it. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnMouseMove`

```text
OnMouseMove(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

The system calls this method to notify the widget that a mouse moved within it. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnMouseEnter`

```text
OnMouseEnter(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> void
```

The system will use this event to notify a widget that the cursor has entered it. This event is NOT bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseLeave`

```text
OnMouseLeave(MouseEvent: FPointerEvent &) -> void
```

The system will use this event to notify a widget that the cursor has left it. This event is NOT bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseWheel`

```text
OnMouseWheel(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

Called when the mouse wheel is spun. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `MouseEvent` | `FPointerEvent &` | Mouse event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnMouseButtonDoubleClick`

```text
OnMouseButtonDoubleClick(InMyGeometry: FGeometry, InMouseEvent: FPointerEvent &) -> FEventReply
```

Called when a mouse button is double clicked.  Override this in derived classes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMyGeometry` | `FGeometry` | Widget geometry |
| `InMouseEvent` | `FPointerEvent &` | Mouse button event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnDragDetected`

```text
OnDragDetected(MyGeometry: FGeometry, PointerEvent: FPointerEvent &, Operation: UDragDropOperation * &) -> void
```

Called when Slate detects that a widget started to be dragged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `PointerEvent` | `FPointerEvent &` | MouseMove that triggered the drag |
| `Operation` | `UDragDropOperation * &` | The drag operation that was detected. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragCancelled`

```text
OnDragCancelled(PointerEvent: FPointerEvent &, Operation: UDragDropOperation *) -> void
```

Called when the user cancels the drag operation, typically when they simply release the mouse button after
	  beginning a drag operation, but failing to complete the drag.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent &` | Last mouse event from when the drag was canceled. |
| `Operation` | `UDragDropOperation *` | The drag operation that was canceled. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragEnter`

```text
OnDragEnter(MyGeometry: FGeometry, PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> void
```

Called during drag and drop when the drag enters the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag entered the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation that entered the widget. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragLeave`

```text
OnDragLeave(PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> void
```

Called during drag and drop when the drag leaves the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag left the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation that entered the widget. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragOver`

```text
OnDragOver(MyGeometry: FGeometry, PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> bool
```

Called during drag and drop when the the mouse is being dragged over a widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag occurred over the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation over the widget. |

**Returns**

| Type | Description |
|---|---|
| `bool` | 'true' to indicate that you handled the drag over operation.  Returning 'false' will cause the operation to continue to bubble up. |

### `OnDrop`

```text
OnDrop(MyGeometry: FGeometry, PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> bool
```

Called when the user is dropping something onto a widget.  Ends the drag and drop operation, even if no widget handles this.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag occurred over the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation over the widget. |

**Returns**

| Type | Description |
|---|---|
| `bool` | 'true' to indicate you handled the drop operation. |

### `OnTouchGesture`

```text
OnTouchGesture(MyGeometry: FGeometry, GestureEvent: FPointerEvent &) -> FEventReply
```

Called when the user performs a gesture on trackpad. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `GestureEvent` | `FPointerEvent &` | gesture event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnTouchStarted`

```text
OnTouchStarted(MyGeometry: FGeometry, InTouchEvent: FPointerEvent &) -> FEventReply
```

Called when a touchpad touch is started (finger down)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InTouchEvent` | `FPointerEvent &` | The touch event generated |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnTouchMoved`

```text
OnTouchMoved(MyGeometry: FGeometry, InTouchEvent: FPointerEvent &) -> FEventReply
```

Called when a touchpad touch is moved  (finger moved)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InTouchEvent` | `FPointerEvent &` | The touch event generated |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnTouchEnded`

```text
OnTouchEnded(MyGeometry: FGeometry, InTouchEvent: FPointerEvent &) -> FEventReply
```

Called when a touchpad touch is ended (finger lifted)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InTouchEvent` | `FPointerEvent &` | The touch event generated |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnMotionDetected`

```text
OnMotionDetected(MyGeometry: FGeometry, InMotionEvent: FMotionEvent) -> FEventReply
```

Called when motion is detected (controller or device)
	  e.g. Someone tilts or shakes their controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InMotionEvent` | `FMotionEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnMouseCaptureLost`

```text
OnMouseCaptureLost() -> void
```

Called when mouse capture is lost if it was owned by this widget.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllChildrenOfType`

```text
GetAllChildrenOfType(Type: FString, Children: TArray < UWidget * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Type` | `FString` | - |
| `Children` | `TArray < UWidget * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTypedChildrenOfWidget`

```text
GetTypedChildrenOfWidget(Parent: UWidget *, Type: FString, Children: TArray < UWidget * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `UWidget *` | - |
| `Type` | `FString` | - |
| `Children` | `TArray < UWidget * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationStarted`

```text
BindToAnimationStarted(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Bind an animation started delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationStarted`

```text
UnbindFromAnimationStarted(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Unbind an animation started delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationStarted`

```text
UnbindAllFromAnimationStarted(Animation: UWidgetAnimation *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationFinished`

```text
BindToAnimationFinished(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Bind an animation finished delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationFinished`

```text
UnbindFromAnimationFinished(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Unbind an animation finished delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationFinished`

```text
UnbindAllFromAnimationFinished(Animation: UWidgetAnimation *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationEvent`

```text
BindToAnimationEvent(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent, AnimationEvent: EWidgetAnimationEvent, UserTag: FName) -> void
```

Allows binding to a specific animation's event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |
| `AnimationEvent` | `EWidgetAnimationEvent` | the event to watch for. |
| `UserTag` | `FName` | Scopes the delegate to only be called when the animation completes with a specific tag set on it when it was played. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimationStarted`

```text
OnAnimationStarted(Animation: UWidgetAnimation *) -> void
```

Called when an animation is started.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation that started |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimationFinished`

```text
OnAnimationFinished(Animation: UWidgetAnimation *) -> void
```

Called when an animation has either played all the way through or is stopped

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | The animation that has finished playing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FLinearColor) -> void
```

Sets the tint of the widget, this affects all child widgets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FLinearColor` | The tint to apply to all child widgets. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForegroundColor`

```text
SetForegroundColor(InForegroundColor: FSlateColor) -> void
```

Sets the foreground color of the widget, this is inherited by sub widgets.  Any color property 
	  that is marked as inherit will use this color.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForegroundColor` | `FSlateColor` | The foreground color. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

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

### `PlayAnimation`

```text
PlayAnimation(InAnimation: UWidgetAnimation *, StartAtTime: float, NumLoopsToPlay: int32, PlayMode: EUMGSequencePlayMode :: Type, PlaybackSpeed: float) -> void
```

Plays an animation in this widget a specified number of times

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to play |
| `StartAtTime` | `float` | The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation. |
| `NumLoopsToPlay` | `int32` | The number of times to loop this animation (0 to loop indefinitely) |
| `PlayMode` | `EUMGSequencePlayMode :: Type` | Specifies the playback mode |
| `PlaybackSpeed` | `float` | The speed at which the animation should play |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayAnimationTo`

```text
PlayAnimationTo(InAnimation: UWidgetAnimation *, StartAtTime: float, EndAtTime: float, NumLoopsToPlay: int32, PlayMode: EUMGSequencePlayMode :: Type, PlaybackSpeed: float) -> void
```

Plays an animation in this widget a specified number of times stoping at a specified time

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to play |
| `StartAtTime` | `float` | The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation. |
| `EndAtTime` | `float` | The absolute time in the animation where to stop, this is only considered in the last loop. |
| `NumLoopsToPlay` | `int32` | The number of times to loop this animation (0 to loop indefinitely) |
| `PlayMode` | `EUMGSequencePlayMode :: Type` | Specifies the playback mode |
| `PlaybackSpeed` | `float` | The speed at which the animation should play |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAnimation`

```text
StopAnimation(InAnimation: UWidgetAnimation *) -> void
```

Stops an already running animation in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpAnimation`

```text
JumpAnimation(InAnimation: UWidgetAnimation *, JumpAtTime: float) -> void
```

Stop and jump to the specified time in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to jump |
| `JumpAtTime` | `float` | specified time |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseAnimation`

```text
PauseAnimation(InAnimation: UWidgetAnimation *) -> float
```

Pauses an already running animation in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | the time point the animation was at when it was paused, relative to its start position.  Use this as the StartAtTime when you trigger PlayAnimation. |

### `GetAnimationCurrentTime`

```text
GetAnimationCurrentTime(InAnimation: UWidgetAnimation *) -> float
```

Gets the current time of the animation in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | the current time of the animation. |

### `IsAnimationPlaying`

```text
IsAnimationPlaying(InAnimation: UWidgetAnimation *) -> bool
```

Gets whether an animation is currently playing on this widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to check the playback status of |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the animation is currently playing |

### `IsAnyAnimationPlaying`

```text
IsAnyAnimationPlaying() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | True if any animation is currently playing |

### `SetNumLoopsToPlay`

```text
SetNumLoopsToPlay(InAnimation: UWidgetAnimation *, NumLoopsToPlay: int32) -> void
```

Changes the number of loops to play given a playing animation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation that is already playing |
| `NumLoopsToPlay` | `int32` | The number of loops to play. (0 to loop indefinitely) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaybackSpeed`

```text
SetPlaybackSpeed(InAnimation: UWidgetAnimation *, PlaybackSpeed: float) -> void
```

Changes the playback rate of a playing animation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation that is already playing |
| `PlaybackSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReverseAnimation`

```text
ReverseAnimation(InAnimation: UWidgetAnimation *) -> void
```

If an animation is playing, this function will reverse the playback.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The playing animation that we want to reverse |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsAnimationPlayingForward`

```text
IsAnimationPlayingForward(InAnimation: UWidgetAnimation *) -> bool
```

returns true if the animation is currently playing forward, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The playing animation that we want to know about |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `PlaySound`

```text
PlaySound(SoundToPlay: USoundBase *) -> void
```

Plays a sound through the UI

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoundToPlay` | `USoundBase *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetWidgetFromName`

```text
GetWidgetFromName(Name: FName &) -> UWidget *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | The uobject widget corresponding to a given name |

### `GetVariableWidgetFromName`

```text
GetVariableWidgetFromName(Name: FName &) -> UWidget *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

### `IsPlayingAnimation`

```text
IsPlayingAnimation() -> bool
```

Are we currently playing any animations?

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NewWidgetObjectBP`

```text
NewWidgetObjectBP(Outer: UObject *, UserWidgetClass: UClass *) -> UUserWidget *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject *` | - |
| `UserWidgetClass` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | - |

### `GetCacheLayerId`

```text
GetCacheLayerId() -> int32
```

return CacheLayerId only windows

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `ListenForInputAction`

```text
ListenForInputAction(ActionName: FName, EventType: TEnumAsByte < EInputEvent >, bConsume: bool, Callback: FOnInputAction) -> void
```

Listens for a particular Player Input Action by name.  This requires that those actions are being executed, and
	  that we're not currently in UI-Only Input Mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName` | - |
| `EventType` | `TEnumAsByte < EInputEvent >` | - |
| `bConsume` | `bool` | - |
| `Callback` | `FOnInputAction` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopListeningForInputAction`

```text
StopListeningForInputAction(ActionName: FName, EventType: TEnumAsByte < EInputEvent >) -> void
```

Removes the binding for a particular action's callback.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName` | - |
| `EventType` | `TEnumAsByte < EInputEvent >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopListeningForAllInputActions`

```text
StopListeningForAllInputActions() -> void
```

Stops listening to all input actions, and unregisters the input component with the player controller.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterInputComponent`

```text
RegisterInputComponent() -> void
```

ListenForInputAction will automatically Register an Input Component with the player input system.
	  If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
	  UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterInputComponent`

```text
UnregisterInputComponent() -> void
```

StopListeningForAllInputActions will automatically Register an Input Component with the player input system.
	  If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
	  UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsListeningForInputAction`

```text
IsListeningForInputAction(ActionName: FName) -> bool
```

Checks if the action has a registered callback with the input component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetInputActionPriority`

```text
SetInputActionPriority(NewPriority: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPriority` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputActionBlocking`

```text
SetInputActionBlocking(bShouldBlock: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShouldBlock` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserWidget3D.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserWidgetSkin.json -->

# UUserWidgetSkin

The user widget skin

## Inheritance

`UUserWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetSkin` | `UWidgetSkin *` | Widget skin data. |

## Functions

### `PreReceiveApply`

```text
PreReceiveApply() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveApply`

```text
ReceiveApply() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PreReceiveRevert`

```text
PreReceiveRevert() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveRevert`

```text
ReceiveRevert() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveCleanup`

```text
ReceiveCleanup() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveShow`

```text
ReceiveShow() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveHide`

```text
ReceiveHide() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMountedWidgetByIndex`

```text
GetMountedWidgetByIndex(MountInfoIndex: int32) -> UWidget *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MountInfoIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserWidgetStyle.json -->

# UUserWidgetStyle

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StylesInfo` | `TArray < FUserWidgetStyleInfo >` | - |
| `bShouldHidenJoystick` | `bool` | - |
| `bShowHidenJoystick_NoDestory` | `bool` | - |
| `bShouldHidenCrosshair` | `bool` | - |
| `bUseBLEBlackList` | `bool` | - |
| `BLEBlackList` | `TArray < FBLEEnumInfo >` | - |
| `bShouldReport` | `bool` | - |
| `UnloadDurationTime` | `float` | - |
| `IsPCUIStyle` | `bool` | - |
| `UnloadTimerHandle` | `FTimerHandle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UUserWidgetUI.json -->

# UUserWidgetUI

The user widget UI

## Inheritance

`UUserWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayoutDataList` | `TMap < int32 , FMainUILayoutData >` | Widget Main UI. |
| `WidgetType` | `int32` | - |
| `WidgetUIBlueprintType` | `TEnumAsByte < EWidgetUIBlueprintType >` | - |

## Functions

### `ReceiveApply`

```text
ReceiveApply() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveRevert`

```text
ReceiveRevert() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveCleanup`

```text
ReceiveCleanup() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E6%8A%80%E8%83%BD/UUTSkillManagerComponent.json -->

# UUTSkillManagerComponent

技能组件

## Inheritance

`UActorComponent` -> `IUTSkillInstanceNodeContainerInterface` -> `IObjectPoolInterface`

## Delegates

### `UGC_SkillActiveDelegate`

```text
UGC_SkillActiveDelegate(SkillPath: FString) -> void
```

技能激活
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_SkillStartDelegate`

```text
UGC_SkillStartDelegate(SkillPath: FString) -> void
```

技能开始
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_SkillEndDelegate`

```text
UGC_SkillEndDelegate(SkillPath: FString) -> void
```

技能结束
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_SkillCDDelegate`

```text
UGC_SkillCDDelegate(SkillPath: FString) -> void
```

技能进入冷却
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVectorField.json -->

# UVectorField

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Bounds` | `FBox` | Bounds of the volume in local space. |
| `Intensity` | `float` | The intensity with which to multiplie vectors in this field. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVectorFieldAnimated.json -->

# UVectorFieldAnimated

## Inheritance

`UVectorField`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | The texture from which to create the vector field. |
| `ConstructionOp` | `TEnumAsByte < enum EVectorFieldConstructionOp >` | The operation used to construct the vector field. |
| `VolumeSizeX` | `int32` | The size of the volume. Valid sizes: 16, 32, 64. |
| `VolumeSizeY` | `int32` | The size of the volume. Valid sizes: 16, 32, 64. |
| `VolumeSizeZ` | `int32` | The size of the volume. Valid sizes: 16, 32, 64. |
| `SubImagesX` | `int32` | The number of horizontal subimages in the texture atlas. |
| `SubImagesY` | `int32` | The number of vertical subimages in the texture atlas. |
| `FrameCount` | `int32` | The number of frames in the atlas. |
| `FramesPerSecond` | `float` | The rate at which to interpolate between frames. |
| `bLoop` | `uint32` | Whether or not the simulation should loop. |
| `NoiseField` | `UVectorFieldStatic *` | A static vector field used to add noise. |
| `NoiseScale` | `float` | Scale to apply to vectors in the noise field. |
| `NoiseMax` | `float` | The maximum magnitude of noise vectors to apply. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVectorFieldComponent.json -->

# UVectorFieldComponent

A Component referencing a vector field.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VectorField` | `UVectorField *` | The vector field asset. |
| `Intensity` | `float` | The intensity at which the vector field is applied. |
| `Tightness` | `float` | How tightly particles follow the vector field. |
| `bPreviewVectorField` | `uint32` | If true, the vector field is only used for preview visualizations. |

## Functions

### `SetIntensity`

```text
SetIntensity(NewIntensity: float) -> void
```

Set the intensity of the vector field.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - The new intensity of the vector field. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVectorFieldStatic.json -->

# UVectorFieldStatic

## Inheritance

`UVectorField`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SizeX` | `int32` | Size of the vector field volume. |
| `SizeY` | `int32` | Size of the vector field volume. |
| `SizeZ` | `int32` | Size of the vector field volume. |
| `SourceFilePath_DEPRECATED` | `FString` | - |
| `AssetImportData` | `UAssetImportData *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVehicleCommonComponent.json -->

# UVehicleCommonComponent

载具通用逻辑组件类

## Inheritance

`UVehicleComponent`

## Delegates

### `UGC_OnVehicleHPChangedDelegate`

```text
UGC_OnVehicleHPChangedDelegate(HP: float, HPMax: float) -> void
```

载具血量变化
	 生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HP` | `float` | 当前血量 |
| `HPMax` | `float` | 最大血量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleFuelChangedDelegate`

```text
UGC_OnVehicleFuelChangedDelegate(Fuel: float, FuelMax: float) -> void
```

载具油量变化
	 生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Fuel` | `float` | 当前血量 |
| `FuelMax` | `float` | 最大血量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleWheelsHPChangedDelegate`

```text
UGC_OnVehicleWheelsHPChangedDelegate() -> void
```

生效范围C
	 载具轮子血量发生变化

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleFuelUsedUpDelegate`

```text
UGC_OnVehicleFuelUsedUpDelegate() -> void
```

生效范围CS
	 油量消耗完

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVehicleSeatComponent.json -->

# UVehicleSeatComponent

载具座位组件类

## Inheritance

`UVehicleComponent`

## Delegates

### `UGC_OnSeatAttachedDelegate`

```text
UGC_OnSeatAttachedDelegate(Character: ASTExtraPlayerCharacter*, SeatType: ESTExtraVehicleSeatType, SeatIdx: int32) -> void
```

使用座位
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter*` | 乘客 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |
| `SeatIdx` | `int32` | 座位Index |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnSeatDetachedDelegate`

```text
UGC_OnSeatDetachedDelegate(Character: ASTExtraPlayerCharacter*, SeatType: ESTExtraVehicleSeatType, SeatIdx: int32) -> void
```

离开座位
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter*` | 乘客 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |
| `SeatIdx` | `int32` | 座位Index |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnSeatChangedDelegate`

```text
UGC_OnSeatChangedDelegate(Character: ASTExtraPlayerCharacter*, LastSeatType: ESTExtraVehicleSeatType, LastSeatIdx: int32, NewSeatType: ESTExtraVehicleSeatType, NewSeatIdx: int32) -> void
```

离开座位
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter*` | 乘客 |
| `LastSeatType` | `ESTExtraVehicleSeatType` | 旧座位类型 |
| `LastSeatIdx` | `int32` | 旧座位Index |
| `NewSeatType` | `ESTExtraVehicleSeatType` | 新座位类型 |
| `NewSeatIdx` | `int32` | 新座位Index |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDriverChange`

```text
OnDriverChange(OldChara: ASTExtraPlayerCharacter*, NewChara: ASTExtraPlayerCharacter*) -> void
```

驾驶员变更事件Delegate

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldChara` | `ASTExtraPlayerCharacter*` | - |
| `NewChara` | `ASTExtraPlayerCharacter*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVerticalBox.json -->

# UVerticalBox

A vertical box widget is a layout panel allowing child widgets to be automatically laid out
  vertically.
 
   Many Children
   Flows Vertical

## Inheritance

`UPanelWidget`

## Functions

### `AddChildToVerticalBox`

```text
AddChildToVerticalBox(Content: UWidget *) -> UVerticalBoxSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UVerticalBoxSlot *` | - |

### `InsertChild`

```text
InsertChild(Content: UWidget *, Index: int32) -> UVerticalBoxSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UVerticalBoxSlot *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVerticalBoxSlot.json -->

# UVerticalBoxSlot

The Slot for the UVerticalBox, contains the widget that is flowed vertically

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

### `SetSize`

```text
SetSize(InSize: FSlateChildSize) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSize` | `FSlateChildSize` | - |

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVideoCaptureSettings.json -->

# UVideoCaptureSettings

## Inheritance

`UFrameGrabberProtocolSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseCompression` | `bool` | - |
| `CompressionQuality` | `float` | - |
| `VideoCodec` | `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UViewport.json -->

# UViewport

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BackgroundColor` | `FLinearColor` | - |

## Functions

### `GetViewportWorld`

```text
GetViewportWorld() -> UWorld *
```

**Returns**

| Type | Description |
|---|---|
| `UWorld *` | - |

### `GetViewLocation`

```text
GetViewLocation() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetViewLocation`

```text
SetViewLocation(Location: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewRotation`

```text
GetViewRotation() -> FRotator
```

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetViewRotation`

```text
SetViewRotation(Rotation: FRotator) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Spawn`

```text
Spawn(ActorClass: TSubclassOf < AActor >) -> AActor *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorClass` | `TSubclassOf < AActor >` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVirtualJoystickResource.json -->

# UVirtualJoystickResource

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrushList` | `TArray < FSlateBrush >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVisibilityBinding.json -->

# UVisibilityBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> ESlateVisibility
```

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVisualLoggerKismetLibrary.json -->

# UVisualLoggerKismetLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `LogText`

```text
LogText(WorldContextObject: UObject *, Text: FString, LogCategory: FName) -> void
```

Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Text` | `FString` | - |
| `LogCategory` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LogLocation`

```text
LogLocation(WorldContextObject: UObject *, Location: FVector, Text: FString, ObjectColor: FLinearColor, Radius: float, LogCategory: FName) -> void
```

Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector` | - |
| `Text` | `FString` | - |
| `ObjectColor` | `FLinearColor` | - |
| `Radius` | `float` | - |
| `LogCategory` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LogBox`

```text
LogBox(WorldContextObject: UObject *, BoxShape: FBox, Text: FString, ObjectColor: FLinearColor, LogCategory: FName) -> void
```

Logs box shape - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BoxShape` | `FBox` | - |
| `Text` | `FString` | - |
| `ObjectColor` | `FLinearColor` | - |
| `LogCategory` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVolumetricFogBoxComponent.json -->

# UVolumetricFogBoxComponent

Used to create local volumetric fog.

## Inheritance

`UBoxComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VolumetricFogAlbedo` | `FColor` | The height fog particle reflectiveness used by volumetric fog.<br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |
| `VolumetricFogEmissive` | `FLinearColor` | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,<br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |
| `VolumetricFogExtinctionScale` | `float` | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |

## Functions

### `SetVolumetricFogExtinctionScale`

```text
SetVolumetricFogExtinctionScale(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogAlbedo`

```text
SetVolumetricFogAlbedo(NewValue: FColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogEmissive`

```text
SetVolumetricFogEmissive(NewValue: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UVolumetricFogSphereComponent.json -->

# UVolumetricFogSphereComponent

Used to create local volumetric fog.

## Inheritance

`USphereComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VolumetricFogAlbedo` | `FColor` | The height fog particle reflectiveness used by volumetric fog.<br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |
| `VolumetricFogEmissive` | `FLinearColor` | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting,<br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |
| `VolumetricFogExtinctionScale` | `float` | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |

## Functions

### `SetVolumetricFogExtinctionScale`

```text
SetVolumetricFogExtinctionScale(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogAlbedo`

```text
SetVolumetricFogAlbedo(NewValue: FColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogEmissive`

```text
SetVolumetricFogEmissive(NewValue: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWeakRefImage.json -->

# UWeakRefImage

## Inheritance

`UImage`

## Functions

### `LoadTextureResource`

```text
LoadTextureResource(bAsync: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bAsync` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnloadTextureResource`

```text
UnloadTextureResource() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWeightmapToMatIDData.json -->

# UWeightmapToMatIDData

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConfigDatas` | `TMap < FName , FWeightmapToMatIDConfig >` | - |
| `MatIDBiomesInfo` | `ULandscapeBiomesInfoObject *` | - |
| `MatIDMaterial` | `UMaterialInterface *` | - |

## Functions

### `CreateNewBiomesInfo`

```text
CreateNewBiomesInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyConfigDataToBiomesInfo`

```text
ApplyConfigDataToBiomesInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidget.json -->

# UWidget

This is the base class for all wrapped Slate controls that are exposed to UObjects.

## Inheritance

`UVisual`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Slot` | `UPanelSlot *` | The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget. |
| `CachedPanel_ForGC` | `UPanelWidget *` | - |
| `ToolTipText` | `FText` | Tooltip text to show when the user hovers over the widget with the mouse |
| `ToolTipWidget` | `UWidget *` | Tooltip widget to show when the user hovers over the widget with the mouse |
| `IgnorePixelSnapping` | `bool` | - |
| `RelatedStyleWidgetName` | `FName` | - |
| `RelatedStyleWidget` | `TWeakObjectPtr < UWidget >` | - |
| `RenderTransform` | `FWidgetTransform` | The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget. |
| `RenderTransformPivot` | `FVector2D` | The render transform pivot controls the location about which transforms are applied.<br>	  This value is a normalized coordinate about which things like rotations will occur. |
| `bIsVariable` | `uint8` | Allows controls to be exposed as variables in a blueprint.  Not all controls need to be exposed<br>	  as variables, so this allows only the most useful ones to end up being exposed. |
| `bCreatedByConstructionScript` | `uint8` | Flag if the Widget was created from a blueprint |
| `bIsEnabled` | `uint8` | Sets whether this widget can be modified interactively by the user |
| `bOverride_Cursor` | `uint8` | - |
| `bIsVolatile` | `uint8` | Engine modify End<br>	<br>	<br>	  If true prevents the widget or its child's geometry or layout information from being cached.  If this widget<br>	  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile<br>	  instead of invalidating it every frame, which would prevent the invalidation panel from actually<br>	  ever caching anything. |
| `bWriteSceneZBuffer` | `uint8` | - |
| `UsedLayerPolicy` | `uint8` | DrawLayer's policy, 0: default, 1: prevent increasing layer to force batch |
| `PreservedLayerNum` | `uint8` | - |
| `FixedLayerPolicy` | `uint8` | DrawLayer's policy, 0: default, 1: Fixed layer to force batch |
| `FixedLayerNum` | `uint8` | - |
| `IngoreRectMove` | `uint8` | - |
| `CareRectMove` | `uint8` | - |
| `Cursor` | `TEnumAsByte < EMouseCursor :: Type >` | The cursor to show when the mouse is over the widget |
| `Clipping` | `EWidgetClipping` | Controls how the clipping behavior of this widget.  Normally content that overflows the<br>	  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content<br>	  from being seen.<br>	 <br>	  NOTE: Elements in different clipping spaces can not be batched together, and so there is a<br>	  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent<br>	  content from showing up outside its bounds. |
| `Visibility` | `ESlateVisibility` | The visibility of the widget |
| `RenderOpacity` | `float` | The opacity of the widget |
| `Navigation` | `UWidgetNavigation *` | The navigation object for this widget is optionally created if the user has configured custom<br>	  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions<br>	  can occur between widgets. |
| `bCatchVisibilityChangedEvent` | `bool` | True if you want to enable auto destroy user widget stragegy |
| `NativeBindings` | `TArray < UPropertyBinding * >` | Native property bindings. |
| `AreaTypeFlags` | `int32` | - |
| `ZValue` | `int32` | - |
| `bLogTraceVisibilityChange` | `uint8` | Engine modify Start |
| `bHiddenInDesigner` | `uint8` | Stores the design time flag setting if the widget is hidden inside the designer |
| `bExpandedInDesigner` | `uint8` | Stores the design time flag setting if the widget is expanded inside the designer |
| `bLockedInDesigner` | `uint8` | Stores the design time flag setting if the widget is locked inside the designer |
| `DesignerFlags` | `TEnumAsByte < EWidgetDesignFlags :: Type >` | Any flags used by the designer at edit time. |
| `DisplayLabel` | `FString` | The friendly name for this widget displayed in the designer and BP graph. |
| `bStyleHidding` | `bool` | - |
| `bStyleRemove` | `bool` | - |
| `bStyleInsertInvBox` | `bool` | - |
| `bStyleInsertRetainerBox` | `bool` | - |

## Functions

### `SetRenderTransform`

```text
SetRenderTransform(InTransform: FWidgetTransform) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTransform` | `FWidgetTransform` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderScale`

```text
SetRenderScale(Scale: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Scale` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderShear`

```text
SetRenderShear(Shear: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Shear` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderAngle`

```text
SetRenderAngle(Angle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Angle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderTranslation`

```text
SetRenderTranslation(Translation: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Translation` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderTransformPivot`

```text
SetRenderTransformPivot(Pivot: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pivot` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIsEnabled`

```text
GetIsEnabled() -> bool
```

Gets the current enabled status of the widget

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIsEnabled`

```text
SetIsEnabled(bInIsEnabled: bool) -> void
```

Sets the current enabled status of the widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInIsEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetToolTipText`

```text
SetToolTipText(InToolTipText: FText &) -> void
```

Sets the tooltip text for the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InToolTipText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetToolTip`

```text
SetToolTip(Widget: UWidget *) -> void
```

Sets a custom widget as the tooltip of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCursor`

```text
SetCursor(InCursor: EMouseCursor :: Type) -> void
```

Sets the cursor to show over the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCursor` | `EMouseCursor :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetCursor`

```text
ResetCursor() -> void
```

Resets the cursor to use on the widget, removing any customization for it.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVisible`

```text
IsVisible() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget is Visible, HitTestInvisible or SelfHitTestInvisible. |

### `GetVisibility`

```text
GetVisibility() -> ESlateVisibility
```

Gets the current visibility of the widget.

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `GetUVisibility`

```text
GetUVisibility() -> ESlateVisibility
```

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `SetLocalVisibility`

```text
SetLocalVisibility(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLocalVisibilityWithoutPCUIStyle`

```text
SetLocalVisibilityWithoutPCUIStyle(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPCVisibility`

```text
GetPCVisibility() -> ESlateVisibility
```

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `IsPCVisible`

```text
IsPCVisible() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetVisibility`

```text
SetVisibility(InVisibility: ESlateVisibility) -> void
```

Sets the visibility of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAdvancedCollapsed`

```text
SetAdvancedCollapsed(IsAdvancedCollapsed: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsAdvancedCollapsed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetRenderOpacity`

```text
GetRenderOpacity() -> float
```

Gets the current visibility of the widget.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetRenderOpacity`

```text
SetRenderOpacity(InOpacity: float) -> void
```

Sets the visibility of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOpacity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetClipping`

```text
GetClipping() -> EWidgetClipping
```

Gets the clipping state of this widget.

**Returns**

| Type | Description |
|---|---|
| `EWidgetClipping` | - |

### `SetClipping`

```text
SetClipping(InClipping: EWidgetClipping) -> void
```

Sets the clipping state of this widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClipping` | `EWidgetClipping` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceVolatile`

```text
ForceVolatile(bForce: bool) -> void
```

Sets the forced volatility of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bForce` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVolatile`

```text
IsVolatile() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsHovered`

```text
IsHovered() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget is currently being hovered by a pointer device |

### `SetWriteSceneZBuffer`

```text
SetWriteSceneZBuffer(bInWriteSceneZBuffer: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInWriteSceneZBuffer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasKeyboardFocus`

```text
HasKeyboardFocus() -> bool
```

Checks to see if this widget currently has the keyboard focus

**Returns**

| Type | Description |
|---|---|
| `bool` | True if this widget has keyboard focus |

### `HasMouseCapture`

```text
HasMouseCapture() -> bool
```

Checks to see if this widget is the current mouse captor

**Returns**

| Type | Description |
|---|---|
| `bool` | True if this widget has captured the mouse |

### `SetKeyboardFocus`

```text
SetKeyboardFocus() -> void
```

Sets the focus to this widget.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasUserFocus`

```text
HasUserFocus(PlayerController: APlayerController *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this widget is focused by a specific user. |

### `HasAnyUserFocus`

```text
HasAnyUserFocus() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this widget is focused by any user. |

### `HasFocusedDescendants`

```text
HasFocusedDescendants() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if any descendant widget is focused by any user. |

### `HasUserFocusedDescendants`

```text
HasUserFocusedDescendants(PlayerController: APlayerController *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if any descendant widget is focused by a specific user. |

### `SetUserFocus`

```text
SetUserFocus(PlayerController: APlayerController *) -> void
```

Sets the focus to this widget for a specific user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceLayoutPrepass`

```text
ForceLayoutPrepass() -> void
```

Forces a pre-pass.  A pre-pass caches the desired size of the widget hierarchy owned by this widget.
	  One pre-pass is already happens for every widget before Tick occurs.  You only need to perform another
	  pre-pass if you are adding child widgets this frame and want them to immediately be visible this frame.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvalidateLayoutAndVolatility`

```text
InvalidateLayoutAndVolatility() -> void
```

Invalidates the widget from the view of a layout caching widget that may own this widget.
	  will force the owning widget to redraw and cache children on the next paint pass.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDesiredSize`

```text
GetDesiredSize() -> FVector2D
```

Gets the widgets desired size.
	  NOTE: The underlying Slate widget must exist and be valid, also at least one pre-pass must
	        have occurred before this value will be of any use.

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The widget's desired size |

### `SetAllNavigationRules`

```text
SetAllNavigationRules(Rule: EUINavigationRule, WidgetToFocus: FName) -> void
```

Sets the widget navigation rules for all directions. This can only be called on widgets that are in a widget tree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rule` | `EUINavigationRule` | The rule to use when navigation is taking place |
| `WidgetToFocus` | `FName` | When using the Explicit rule, focus on this widget |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNavigationRule`

```text
SetNavigationRule(Direction: EUINavigation, Rule: EUINavigationRule, WidgetToFocus: FName) -> void
```

Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Direction` | `EUINavigation` | - |
| `Rule` | `EUINavigationRule` | The rule to use when navigation is taking place |
| `WidgetToFocus` | `FName` | When using the Explicit rule, focus on this widget |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetParent`

```text
GetParent() -> UPanelWidget *
```

Gets the parent widget

**Returns**

| Type | Description |
|---|---|
| `UPanelWidget *` | - |

### `RemoveFromParent`

```text
RemoveFromParent() -> void
```

Removes the widget from its parent widget.  If this widget was added to the player's screen or the viewport
	  it will also be removed from those containers.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCachedGeometry`

```text
GetCachedGeometry() -> const FGeometry &
```

Gets the last geometry used to Tick the widget.  This data may not exist yet if this call happens prior to
	  the widget having been tickedpainted, or it may be out of date, or a frame behind.
	 
	  We recommend not to use this data unless there's no other way to solve your problem.  Normally in Slate we
	  try and handle these issues by making a dependent widget part of the hierarchy, as to avoid frame behind
	  or what are referred to as hysteresis problems, both caused by depending on geometry from the previous frame
	  being used to advise how to layout a dependent object the current frame.

**Returns**

| Type | Description |
|---|---|
| `const FGeometry &` | - |

### `GetCachedAllottedGeometry`

```text
GetCachedAllottedGeometry() -> const FGeometry &
```

**Returns**

| Type | Description |
|---|---|
| `const FGeometry &` | - |

### `SetIgnorePixelSnapping`

```text
SetIgnorePixelSnapping(Ignore: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Ignore` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwningPlayer`

```text
GetOwningPlayer() -> APlayerController *
```

Gets the player controller associated with this UI.

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | The player controller that owns the UI. |

### `AddAdvancedCollapsedCount`

```text
AddAdvancedCollapsedCount(Num: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Num` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SubAdvancedCollapsedCount`

```text
SubAdvancedCollapsedCount(Num: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Num` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAdvancedCollapsedCount`

```text
GetAdvancedCollapsedCount() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetWidgetOutlineName`

```text
GetWidgetOutlineName() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `IsCachedWidgetValid`

```text
IsCachedWidgetValid() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `bIsEnabledDelegate`

```text
bIsEnabledDelegate() -> bool
```

A bindable delegate for bIsEnabled

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ToolTipTextDelegate`

```text
ToolTipTextDelegate() -> FText
```

A bindable delegate for ToolTipText

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `ToolTipWidgetDelegate`

```text
ToolTipWidgetDelegate() -> UWidget*
```

A bindable delegate for ToolTipWidget

**Returns**

| Type | Description |
|---|---|
| `UWidget*` | - |

### `VisibilityDelegate`

```text
VisibilityDelegate() -> ESlateVisibility
```

A bindable delegate for Visibility

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `IgnorePixelSnappingDelegate`

```text
IgnorePixelSnappingDelegate() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnWidgetVisibilityChanged`

```text
OnWidgetVisibilityChanged(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWidgetSlateVisibilityChanged`

```text
OnWidgetSlateVisibilityChanged(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWidgetIsEnabledSet`

```text
OnWidgetIsEnabledSet(bIsEnabled: bool, Widget: UWidget*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsEnabled` | `bool` | - |
| `Widget` | `UWidget*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidget3DInstancedComponent.json -->

# UWidget3DInstancedComponent

## Inheritance

`UWidgetComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PerInstanceData` | `TArray < FInstancedWidget3DInstanceData >` | - |
| `InstancingRandomSeed` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetAnimation.json -->

# UWidgetAnimation

## Inheritance

`UMovieSceneSequence`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MovieScene` | `UMovieScene *` | Pointer to the movie scene that controls this animation. |
| `AnimationBindings` | `TArray < FWidgetAnimationBinding >` | - |

## Functions

### `GetStartTime`

```text
GetStartTime() -> UMG_API float
```

Get the start time of this animation.

**Returns**

| Type | Description |
|---|---|
| `UMG_API float` | Start time in seconds. |

### `GetEndTime`

```text
GetEndTime() -> UMG_API float
```

Get the end time of this animation.

**Returns**

| Type | Description |
|---|---|
| `UMG_API float` | End time in seconds. |

### `BindToAnimationStarted`

```text
BindToAnimationStarted(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationStarted`

```text
UnbindFromAnimationStarted(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationStarted`

```text
UnbindAllFromAnimationStarted(Widget: UUserWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationFinished`

```text
BindToAnimationFinished(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationFinished`

```text
UnbindFromAnimationFinished(Widget: UUserWidget *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |
| `Delegate` | `FWidgetAnimationDynamicEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationFinished`

```text
UnbindAllFromAnimationFinished(Widget: UUserWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnAnimationStarted`

```text
OnAnimationStarted() -> void
```

Fires when the widget animation starts playing. compatible for lua, to be deleted

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimationFinished`

```text
OnAnimationFinished() -> void
```

Fires when the widget animation is finished. compatible for lua, to be deleted

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetAnimationDelegateBinding.json -->

# UWidgetAnimationDelegateBinding

## Inheritance

`UDynamicBlueprintBinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetAnimationDelegateBindings` | `TArray < FBlueprintWidgetAnimationDelegateBinding >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetBinding.json -->

# UWidgetBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> UWidget *
```

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetBlueprintGeneratedClass.json -->

# UWidgetBlueprintGeneratedClass

The widget blueprint generated class allows us to create blueprint-able widgets for UMG at runtime.
  All WBPGC's are of UUserWidget classes, and they perform special post initialization using this class
  to give themselves many of the same capabilities as AActor blueprints, like dynamic delegate binding for
  widgets.

## Inheritance

`UBlueprintGeneratedClass`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetTree` | `UWidgetTree *` | A tree of the widget templates to be created |
| `WidgetTreePath` | `FSoftObjectPath` | - |
| `bAutoReleaseWidgetTree` | `uint8` | - |
| `bAllowTemplate` | `uint8` | - |
| `bValidTemplate` | `uint8` | - |
| `bTemplateInitialized` | `uint8` | - |
| `bCookedTemplate` | `uint8` | - |
| `Bindings` | `TArray < FDelegateRuntimeBinding >` | - |
| `Animations` | `TArray < UWidgetAnimation * >` | - |
| `NamedSlots` | `TArray < FName >` | - |
| `TemplateAsset` | `TSoftObjectPtr < UUserWidget >` | - |
| `Template` | `UUserWidget *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetBlueprintLibrary.json -->

# UWidgetBlueprintLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Create`

```text
Create(WorldContextObject: UObject *, WidgetType: TSubclassOf < UUserWidget >, OwningPlayer: APlayerController *) -> UUserWidget *
```

Creates a widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `WidgetType` | `TSubclassOf < UUserWidget >` | - |
| `OwningPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | - |

### `CreateDragDropOperation`

```text
CreateDragDropOperation(OperationClass: TSubclassOf < UDragDropOperation >) -> UDragDropOperation *
```

Creates a new drag and drop operation that can be returned from a drag begin to inform the UI what i
	  being dragged and dropped and what it looks like.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OperationClass` | `TSubclassOf < UDragDropOperation >` | - |

**Returns**

| Type | Description |
|---|---|
| `UDragDropOperation *` | - |

### `SetInputMode_UIOnly`

```text
SetInputMode_UIOnly(Target: APlayerController *, InWidgetToFocus: UWidget *, bLockMouseToViewport: bool) -> void
```

Setup an input mode that allows only the UI to respond to user input.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `bLockMouseToViewport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_UIOnlyEx`

```text
SetInputMode_UIOnlyEx(Target: APlayerController *, InWidgetToFocus: UWidget *, InMouseLockMode: EMouseLockMode) -> void
```

Setup an input mode that allows only the UI to respond to user input.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `InMouseLockMode` | `EMouseLockMode` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_GameAndUI`

```text
SetInputMode_GameAndUI(Target: APlayerController *, InWidgetToFocus: UWidget *, bLockMouseToViewport: bool, bHideCursorDuringCapture: bool) -> void
```

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `bLockMouseToViewport` | `bool` | - |
| `bHideCursorDuringCapture` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_GameAndUIEx`

```text
SetInputMode_GameAndUIEx(Target: APlayerController *, InWidgetToFocus: UWidget *, InMouseLockMode: EMouseLockMode, bHideCursorDuringCapture: bool) -> void
```

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `InMouseLockMode` | `EMouseLockMode` | - |
| `bHideCursorDuringCapture` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_GameOnly`

```text
SetInputMode_GameOnly(Target: APlayerController *) -> void
```

Setup an input mode that allows only player input  player controller to respond to user input.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFocusToGameViewport`

```text
SetFocusToGameViewport() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawBox`

```text
DrawBox(Context: FPaintContext &, Position: FVector2D, Size: FVector2D, Brush: USlateBrushAsset *, Tint: FLinearColor) -> void
```

Draws a box

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `Position` | `FVector2D` | - |
| `Size` | `FVector2D` | - |
| `Brush` | `USlateBrushAsset *` | - |
| `Tint` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawLine`

```text
DrawLine(Context: FPaintContext &, PositionA: FVector2D, PositionB: FVector2D, Tint: FLinearColor, bAntiAlias: bool) -> void
```

Draws a line.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `PositionA` | `FVector2D` | Starting position of the line in local space. |
| `PositionB` | `FVector2D` | Ending position of the line in local space. |
| `Tint` | `FLinearColor` | Color to render the line. |
| `bAntiAlias` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawLines`

```text
DrawLines(Context: FPaintContext &, Points: TArray < FVector2D > &, Tint: FLinearColor, bAntiAlias: bool) -> void
```

Draws several line segments.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `Points` | `TArray < FVector2D > &` | Line pairs, each line needs to be 2 separate points in the array. |
| `Tint` | `FLinearColor` | Color to render the line. |
| `bAntiAlias` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawText`

```text
DrawText(Context: FPaintContext &, InString: FString &, Position: FVector2D, Tint: FLinearColor) -> void
```

Draws text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `InString` | `FString &` | The string to draw. |
| `Position` | `FVector2D` | The starting position where the text is drawn in local space. |
| `Tint` | `FLinearColor` | Color to render the line. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawTextFormatted`

```text
DrawTextFormatted(Context: FPaintContext &, Text: FText &, Position: FVector2D, Font: UFont *, FontSize: int32, FontTypeFace: FName, Tint: FLinearColor) -> void
```

Draws text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `Text` | `FText &` | The string to draw. |
| `Position` | `FVector2D` | The starting position where the text is drawn in local space. |
| `Font` | `UFont *` | - |
| `FontSize` | `int32` | - |
| `FontTypeFace` | `FName` | - |
| `Tint` | `FLinearColor` | Color to render the line. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Handled`

```text
Handled() -> FEventReply
```

The event reply to use when you choose to handle an event.  This will prevent the event 
	  from continuing to bubble up  down the widget hierarchy.

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `Unhandled`

```text
Unhandled() -> FEventReply
```

The event reply to use when you choose not to handle an event.

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `CaptureMouse`

```text
CaptureMouse(Reply: FEventReply &, CapturingWidget: UWidget *) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `CapturingWidget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `ReleaseMouseCapture`

```text
ReleaseMouseCapture(Reply: FEventReply &) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `LockMouse`

```text
LockMouse(Reply: FEventReply &, CapturingWidget: UWidget *) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `CapturingWidget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `UnlockMouse`

```text
UnlockMouse(Reply: FEventReply &) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `SetUserFocus`

```text
SetUserFocus(Reply: FEventReply &, FocusWidget: UWidget *, bInAllUsers: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `FocusWidget` | `UWidget *` | - |
| `bInAllUsers` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `CaptureJoystick`

```text
CaptureJoystick(Reply: FEventReply &, CapturingWidget: UWidget *, bInAllJoysticks: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `CapturingWidget` | `UWidget *` | - |
| `bInAllJoysticks` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `ClearUserFocus`

```text
ClearUserFocus(Reply: FEventReply &, bInAllUsers: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `bInAllUsers` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `ReleaseJoystickCapture`

```text
ReleaseJoystickCapture(Reply: FEventReply &, bInAllJoysticks: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `bInAllJoysticks` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `SetMousePosition`

```text
SetMousePosition(Reply: FEventReply &, NewMousePosition: FVector2D) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `NewMousePosition` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `DetectDrag`

```text
DetectDrag(Reply: FEventReply &, WidgetDetectingDrag: UWidget *, DragKey: FKey) -> FEventReply
```

Ask Slate to detect if a user starts dragging in this widget later.  Slate internally tracks the movement
	  and if it surpasses the drag threshold, Slate will send an OnDragDetected event to the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `WidgetDetectingDrag` | `UWidget *` | Detect dragging in this widget |
| `DragKey` | `FKey` | This button should be pressed to detect the drag |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `DetectDragIfPressed`

```text
DetectDragIfPressed(PointerEvent: FPointerEvent &, WidgetDetectingDrag: UWidget *, DragKey: FKey) -> FEventReply
```

Given the pointer event, emit the DetectDrag reply if the provided key was pressed.
	  If the DragKey is a touch key, that will also automatically work.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent &` | The pointer device event coming in. |
| `WidgetDetectingDrag` | `UWidget *` | Detect dragging in this widget. |
| `DragKey` | `FKey` | This button should be pressed to detect the drag, won't emit the DetectDrag FEventReply unless this is pressed. |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `EndDragDrop`

```text
EndDragDrop(Reply: FEventReply &) -> FEventReply
```

An event should return FReply::Handled().EndDragDrop() to request that the current dragdrop operation be terminated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `IsDragDropping`

```text
IsDragDropping() -> bool
```

Returns true if a dragdrop event is occurring that a widget can handle.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDragDroppingContent`

```text
GetDragDroppingContent() -> UDragDropOperation *
```

Returns the drag and drop operation that is currently occurring if any, otherwise nothing.

**Returns**

| Type | Description |
|---|---|
| `UDragDropOperation *` | - |

### `CancelDragDrop`

```text
CancelDragDrop() -> void
```

Cancels any current drag drop operation.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeBrushFromAsset`

```text
MakeBrushFromAsset(BrushAsset: USlateBrushAsset *) -> FSlateBrush
```

Creates a Slate Brush from a Slate Brush Asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BrushAsset` | `USlateBrushAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush using the asset's brush. |

### `MakeBrushFromTexture`

```text
MakeBrushFromTexture(Texture: UTexture2D *, Width: int32, Height: int32) -> FSlateBrush
```

Creates a Slate Brush from a Texture2D

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - |
| `Width` | `int32` | When less than or equal to zero, the Width of the brush will default to the Width of the Texture |
| `Height` | `int32` | When less than or equal to zero, the Height of the brush will default to the Height of the Texture |

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush using the texture. |

### `MakeBrushFromMaterial`

```text
MakeBrushFromMaterial(Material: UMaterialInterface *, Width: int32, Height: int32) -> FSlateBrush
```

Creates a Slate Brush from a Material.  Materials don't have an implicit size, so providing a widget and height
	  is required to hint slate with how large the image wants to be by default.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush using the material. |

### `GetBrushResource`

```text
GetBrushResource(Brush: FSlateBrush &) -> UObject *
```

Gets the resource object on a brush.  This could be a UTexture2D or a UMaterialInterface.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetBrushResourceConst`

```text
GetBrushResourceConst(Brush: FSlateBrush &) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetBrushResourceAsTexture2D`

```text
GetBrushResourceAsTexture2D(Brush: FSlateBrush &) -> UTexture2D *
```

Gets the brush resource as a texture 2D.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UTexture2D *` | - |

### `GetBrushResourceAsMaterial`

```text
GetBrushResourceAsMaterial(Brush: FSlateBrush &) -> UMaterialInterface *
```

Gets the brush resource as a material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `SetBrushResourceToTexture`

```text
SetBrushResourceToTexture(Brush: FSlateBrush &, Texture: UTexture2D *) -> void
```

Sets the resource on a brush to be a UTexture2D.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |
| `Texture` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushResourceToMaterial`

```text
SetBrushResourceToMaterial(Brush: FSlateBrush &, Material: UMaterialInterface *) -> void
```

Sets the resource on a brush to be a Material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `NoResourceBrush`

```text
NoResourceBrush() -> FSlateBrush
```

Creates a Slate Brush that wont draw anything, the "Null Brush".

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush that wont draw anything. |

### `GetDynamicMaterial`

```text
GetDynamicMaterial(Brush: FSlateBrush &) -> UMaterialInstanceDynamic *
```

Gets the material that allows changes to parameters at runtime.  The brush must already have a material assigned to it, 
	  if it does it will automatically be converted to a MID.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | A material that supports dynamic input from the game. |

### `DismissAllMenus`

```text
DismissAllMenus() -> void
```

Closes any popup menu

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllWidgetsOfClass`

```text
GetAllWidgetsOfClass(WorldContextObject: UObject *, FoundWidgets: TArray < UUserWidget * > &, WidgetClass: TSubclassOf < UUserWidget >, TopLevelOnly: bool) -> void
```

Find all widgets of a certain class.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `FoundWidgets` | `TArray < UUserWidget * > &` | The widgets that were found matching the filter. |
| `WidgetClass` | `TSubclassOf < UUserWidget >` | The widget class to filter by. |
| `TopLevelOnly` | `bool` | Only the widgets that are direct children of the viewport will be returned. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllWidgetsWithInterface`

```text
GetAllWidgetsWithInterface(WorldContextObject: UObject *, Interface: TSubclassOf < UInterface >, FoundWidgets: TArray < UUserWidget * > &, TopLevelOnly: bool) -> void
```

Find all widgets in the world with the specified interface.
	 This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Interface` | `TSubclassOf < UInterface >` | The interface to find. Must be specified or result array will be empty. |
| `FoundWidgets` | `TArray < UUserWidget * > &` | Output array of widgets that implement the specified interface. |
| `TopLevelOnly` | `bool` | Only the widgets that are direct children of the viewport will be returned. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInputEventFromKeyEvent`

```text
GetInputEventFromKeyEvent(Event: FKeyEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FKeyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetKeyEventFromAnalogInputEvent`

```text
GetKeyEventFromAnalogInputEvent(Event: FAnalogInputEvent &) -> FKeyEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FAnalogInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKeyEvent` | - |

### `GetInputEventFromCharacterEvent`

```text
GetInputEventFromCharacterEvent(Event: FCharacterEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FCharacterEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetInputEventFromPointerEvent`

```text
GetInputEventFromPointerEvent(Event: FPointerEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetInputEventFromNavigationEvent`

```text
GetInputEventFromNavigationEvent(Event: FNavigationEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FNavigationEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetSafeZonePadding`

```text
GetSafeZonePadding(WorldContextObject: UObject *, SafePadding: FVector2D &, SafePaddingScale: FVector2D &, SpillOverPadding: FVector2D &) -> void
```

Gets the amount of padding that needs to be added when accounting for the safe zone on TVs.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SafePadding` | `FVector2D &` | - |
| `SafePaddingScale` | `FVector2D &` | - |
| `SpillOverPadding` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHardwareCursor`

```text
SetHardwareCursor(WorldContextObject: UObject *, CursorShape: EMouseCursor :: Type, CursorName: FName, HotSpot: FVector2D) -> bool
```

Loads or sets a hardware cursor from the content directory in the game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `CursorShape` | `EMouseCursor :: Type` | - |
| `CursorName` | `FName` | - |
| `HotSpot` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ApplyUserWidgetSkin`

```text
ApplyUserWidgetSkin(UserWidget: UUserWidget *, SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >, bAsyncLoad: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UserWidget` | `UUserWidget *` | - |
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |
| `bAsyncLoad` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertUserWidgetSkin`

```text
RevertUserWidgetSkin(UserWidget: UUserWidget *, SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UserWidget` | `UUserWidget *` | - |
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetComponent.json -->

# UWidgetComponent

The widget component provides a surface in the 3D environment on which to render widgets normally rendered to the screen.
  Widgets are first rendered to a render target, then that render target is displayed in the world.
 
  Material Properties set by this component on whatever material overrides the default.
  SlateUI [Texture]
  BackColor [Vector]
  TintColorAndOpacity [Vector]
  OpacityFromTexture [Scalar]

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Space` | `EWidgetSpace` | The coordinate space in which to render the widget |
| `TimingPolicy` | `EWidgetTimingPolicy` | How this widget should deal with timing, pausing, etc. |
| `WidgetClass` | `TSubclassOf < UUserWidget >` | The class of User Widget to create and display an instance of |
| `DrawSize` | `FIntPoint` | The size of the displayed quad. |
| `bManuallyRedraw` | `bool` | Should we wait to be told to redraw to actually draw? |
| `bCheckLowDeviceQualityLevel` | `bool` | Should LowDevice Phone draw UI? |
| `bRedrawRequested` | `bool` | Has anyone requested we redraw? |
| `RedrawTime` | `float` | The time in between draws, if 0 - we would redraw every frame.  If 1, we would redraw every second.<br>	  This will work with bManuallyRedraw as well.  So you can say, manually redraw, but only redraw at this<br>	  maximum rate. |
| `CurrentDrawSize` | `FIntPoint` | The actual draw size, this changes based on DrawSize - or the desired size of the widget if<br>	  bDrawAtDesiredSize is true. |
| `bDrawAtDesiredSize` | `bool` | Causes the render target to automatically match the desired size.<br>	 <br>	  WARNING: If you change this every frame, it will be very expensive.  If you need<br>	     that effect, you should keep the outer widget's sized locked and dynamically<br>	     scale or resize some inner widget. |
| `Pivot` | `FVector2D` | The AlignmentPivot point that the widget is placed at relative to the position. |
| `bReceiveHardwareInput` | `bool` | Register with the viewport for hardware input from the true mouse and keyboard.  These widgets<br>	  will more or less react like regular 2D widgets in the viewport, e.g. they can and will steal focus<br>	  from the viewport.<br>	 <br>	  WARNING: If you are making a VR game, definitely do not change this to true.  This option should ONLY be used<br>	  if you're making what would otherwise be a normal menu for a game, just in 3D.  If you also need the game to<br>	  remain responsive and for the player to be able to interact with UI and move around the world (such as a keypad on a door),<br>	  use the WidgetInteractionComponent instead. |
| `bWindowFocusable` | `bool` | Is the virtual window created to host the widget focusable? |
| `OwnerPlayer` | `ULocalPlayer *` | The owner player for a widget component, if this widget is drawn on the screen, this controls<br>	  what player's screen it appears on for split screen, if not set, users player 0. |
| `BackgroundColor` | `FLinearColor` | The background color of the component |
| `TintColorAndOpacity` | `FLinearColor` | Tint color and opacity for this component |
| `OpacityFromTexture` | `float` | Sets the amount of opacity from the widget's UI texture to use when rendering the translucent or masked UI to the viewport (0.0-1.0) |
| `BlendMode` | `EWidgetBlendMode` | The blend mode for the widget. |
| `bIsTwoSided` | `bool` | Is the component visible from behind? |
| `TickWhenOffscreen` | `bool` | Should the component tick the widget when it's off screen? |
| `Widget` | `UUserWidget *` | The User Widget object displayed and managed by this component |
| `BodySetup` | `UBodySetup *` | The body setup of the displayed quad |
| `TranslucentMaterial` | `UMaterialInterface *` | The material instance for translucent widget components |
| `TranslucentMaterial_OneSided` | `UMaterialInterface *` | The material instance for translucent, one-sided widget components |
| `OpaqueMaterial` | `UMaterialInterface *` | The material instance for opaque widget components |
| `OpaqueMaterial_OneSided` | `UMaterialInterface *` | The material instance for opaque, one-sided widget components |
| `MaskedMaterial` | `UMaterialInterface *` | The material instance for masked widget components. |
| `MaskedMaterial_OneSided` | `UMaterialInterface *` | The material instance for masked, one-sided widget components. |
| `RenderTarget` | `UTextureRenderTarget2D *` | The target to which the user widget is rendered |
| `MaterialInstance` | `UMaterialInstanceDynamic *` | The dynamic instance of the material that the render target is attached to |
| `bAddedToScreen` | `bool` | - |
| `bEditTimeUsable` | `bool` | Allows the widget component to be used at editor time.  For use in the VR-Editor. |
| `SharedLayerName` | `FName` | Layer Name the widget will live on |
| `LayerZOrder` | `int32` | ZOrder the layer will be created on, note this only matters on the first time a new layer is created, subsequent additions to the same layer will use the initially defined ZOrder |
| `GeometryMode` | `EWidgetGeometryMode` | Controls the geometry of the widget component. See EWidgetGeometryMode. |
| `CylinderArcAngle` | `float` | Curvature of a cylindrical widget in degrees. |
| `FlipVector` | `FVector` | Curvature of a cylindrical widget in degrees. |
| `bUseBackColorInTwoSideMode` | `bool` | For Two side Color |
| `BackColor` | `FLinearColor` | - |
| `bHideIfOccluded` | `bool` | Hide widget component when the attached parent is occluded in player's view (ONLY VALID IN SCREEN SPACE) |

## Functions

### `GetUserWidgetObject`

```text
GetUserWidgetObject() -> UUserWidget *
```

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | The user widget object displayed by this component |

### `GetRenderTarget`

```text
GetRenderTarget() -> UTextureRenderTarget2D *
```

**Returns**

| Type | Description |
|---|---|
| `UTextureRenderTarget2D *` | The render target to which the user widget is rendered |

### `ForceWidgetUpdateImmediate`

```text
ForceWidgetUpdateImmediate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceWidgetUpdateImmediately`

```text
ForceWidgetUpdateImmediately() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceUpdateRenderTarget`

```text
ForceUpdateRenderTarget() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetMaterialInstance`

```text
GetMaterialInstance() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | The dynamic material instance used to render the user widget |

### `SetWidget`

```text
SetWidget(Widget: UUserWidget *) -> void
```

Sets the widget to use directly. This function will keep track of the widget till the next time it's called
	 	with either a newer widget or a nullptr

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOwnerPlayer`

```text
SetOwnerPlayer(LocalPlayer: ULocalPlayer *) -> void
```

Sets the local player that owns this widget component.  Setting the owning player controls
	  which player's viewport the widget appears on in a split screen scenario.  Additionally it
	  forwards the owning player to the actual UserWidget that is spawned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalPlayer` | `ULocalPlayer *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwnerPlayer`

```text
GetOwnerPlayer() -> ULocalPlayer *
```

Gets the local player that owns this widget component.

**Returns**

| Type | Description |
|---|---|
| `ULocalPlayer *` | - |

### `GetDrawSize`

```text
GetDrawSize() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The draw size of the quad in the world |

### `GetCurrentDrawSize`

```text
GetCurrentDrawSize() -> FVector2D
```

Returns the "actual" draw size of the quad in the world

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetDrawSize`

```text
SetDrawSize(Size: FVector2D) -> void
```

Sets the draw size of the quad in the world

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Size` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestRedraw`

```text
RequestRedraw() -> void
```

Requests that the widget be redrawn.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTickWhenOffscreen`

```text
GetTickWhenOffscreen() -> bool
```

Gets whether the widget ticks when offscreen or not

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTickWhenOffscreen`

```text
SetTickWhenOffscreen(bWantTickWhenOffscreen: bool) -> void
```

Sets whether the widget ticks when offscreen or not

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bWantTickWhenOffscreen` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBackgroundColor`

```text
SetBackgroundColor(NewBackgroundColor: FLinearColor) -> void
```

Sets the background color and opacityscale for this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBackgroundColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTintColorAndOpacity`

```text
SetTintColorAndOpacity(NewTintColorAndOpacity: FLinearColor) -> void
```

Sets the tint color and opacity scale for this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTintColorAndOpacity` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetInteractionComponent.json -->

# UWidgetInteractionComponent

This is a component to allow interaction with the Widget Component.  This class allows you to 
  simulate a sort of laser pointer device, when it hovers over widgets it will send the basic signals 
  to show as if the mouse were moving on top of it.  You'll then tell the component to simulate key presses, 
  like Left Mouse, down and up, to simulate a mouse click.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VirtualUserIndex` | `int32` | Represents the Virtual User Index.  Each virtual user should be represented by a different <br>	  index number, this will maintain separate capture and focus states for them.  Each<br>	  controller or finger-tip should get a unique PointerIndex. |
| `PointerIndex` | `float` | Each user virtual controller or virtual finger tips being simulated should use a different pointer index. |
| `TraceChannel` | `TEnumAsByte < ECollisionChannel >` | The trace channel to use when tracing for widget components in the world. |
| `InteractionDistance` | `float` | The distance in game units the component should be able to interact with a widget component. |
| `InteractionSource` | `EWidgetInteractionSource` | Should we project from the world location of the component?  If you set this to false, you'll<br>	  need to call SetCustomHitResult(), and provide the result of a custom hit test form whatever<br>	  location you wish. |
| `bEnableHitTesting` | `bool` | Should the interaction component perform hit testing (Automatic or Custom) and attempt to <br>	  simulate hover - if you were going to emulate a keyboard you would want to turn this option off<br>	  if the virtual keyboard was separate from the virtual pointer device and used a second interaction<br>	  component. |
| `bSimulateTouchEvents` | `bool` | When true, pointer events will be sent as touch events instead of mouse events.<br>	  This enables drag-scrolling on ScrollBoxListView widgets in 3D UI,<br>	  since those widgets only respond to touch-based drag gestures. |
| `bShowDebug` | `bool` | Shows some debugging lines and a hit sphere to help you debug interactions. |
| `DebugColor` | `FLinearColor` | Determines the color of the debug lines. |
| `CustomHitResult` | `FHitResult` | Stores the custom hit result set by the player. |
| `LocalHitLocation` | `FVector2D` | The 2D location on the widget component that was hit. |
| `LastLocalHitLocation` | `FVector2D` | The last 2D location on the widget component that was hit. |
| `HoveredWidgetComponent` | `UWidgetComponent *` | The widget component we're currently hovering over. |
| `LastHitResult` | `FHitResult` | The last hit result we used. |
| `bIsHoveredWidgetInteractable` | `bool` | Are we hovering over any interactive widgets. |
| `bIsHoveredWidgetFocusable` | `bool` | Are we hovering over any focusable widget? |
| `bIsHoveredWidgetHitTestVisible` | `bool` | Are we hovered over a widget that is hit test visible? |

## Functions

### `PressPointerKey`

```text
PressPointerKey(Key: FKey) -> void
```

Presses a key as if the mousepointer were the source of it.  Normally you would just use
	  LeftRight mouse button for the Key.  However - advanced uses could also be imagined where you
	  send other keys to signal widgets to take special actions if they're under the cursor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleasePointerKey`

```text
ReleasePointerKey(Key: FKey) -> void
```

Releases a key as if the mousepointer were the source of it.  Normally you would just use
	  LeftRight mouse button for the Key.  However - advanced uses could also be imagined where you
	  send other keys to signal widgets to take special actions if they're under the cursor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PressKey`

```text
PressKey(Key: FKey, bRepeat: bool) -> bool
```

Press a key as if it had come from the keyboard.  Avoid using this for 'a-z|A-Z', things like
	  the Editable Textbox in Slate expect OnKeyChar to be called to signal a specific character being
	  send to the widget.  So for those cases you should use SendKeyChar.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |
| `bRepeat` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReleaseKey`

```text
ReleaseKey(Key: FKey) -> bool
```

Releases a key as if it had been released by the keyboard.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `PressAndReleaseKey`

```text
PressAndReleaseKey(Key: FKey) -> bool
```

Does both the press and release of a simulated keyboard key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Key` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SendKeyChar`

```text
SendKeyChar(Characters: FString, bRepeat: bool) -> bool
```

Transmits a list of characters to a widget by simulating a OnKeyChar event for each key listed in
	  the string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Characters` | `FString` | - |
| `bRepeat` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ScrollWheel`

```text
ScrollWheel(ScrollDelta: float) -> void
```

Sends a scroll wheel event to the widget under the last hit result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ScrollDelta` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetHoveredWidgetComponent`

```text
GetHoveredWidgetComponent() -> UWidgetComponent *
```

Get the currently hovered widget component.

**Returns**

| Type | Description |
|---|---|
| `UWidgetComponent *` | - |

### `IsOverInteractableWidget`

```text
IsOverInteractableWidget() -> bool
```

Returns true if a widget under the hit result is interactive.  e.g. Slate widgets 
	  that return true for IsInteractable().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsOverFocusableWidget`

```text
IsOverFocusableWidget() -> bool
```

Returns true if a widget under the hit result is focusable.  e.g. Slate widgets that 
	  return true for SupportsKeyboardFocus().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsOverHitTestVisibleWidget`

```text
IsOverHitTestVisibleWidget() -> bool
```

Returns true if a widget under the hit result is has a visibility that makes it hit test 
	  visible.  e.g. Slate widgets that return true for GetVisibility().IsHitTestVisible().

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetLastHitResult`

```text
GetLastHitResult() -> const FHitResult &
```

Gets the last hit result generated by the component.  Returns the custom hit result if that was set.

**Returns**

| Type | Description |
|---|---|
| `const FHitResult &` | - |

### `Get2DHitLocation`

```text
Get2DHitLocation() -> FVector2D
```

Gets the last hit location on the widget in 2D, local pixel units of the render target.

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetCustomHitResult`

```text
SetCustomHitResult(HitResult: FHitResult &) -> void
```

Set custom hit result.  This is only taken into account if InteractionSource is set to EWidgetInteractionSource::Custom.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnHoveredWidgetChanged`

```text
OnHoveredWidgetChanged(WidgetComponent: UWidgetComponent*, PreviousWidgetComponent: UWidgetComponent*) -> void
```

Called when the hovered Widget Component changes.  The interaction component functions at the Slate
	  level - so it's unable to report anything about what UWidget is under the hit result.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetComponent` | `UWidgetComponent*` | - |
| `PreviousWidgetComponent` | `UWidgetComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetLayoutLibrary.json -->

# UWidgetLayoutLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `ProjectWorldLocationToWidgetPosition`

```text
ProjectWorldLocationToWidgetPosition(PlayerController: APlayerController *, WorldLocation: FVector, ScreenPosition: FVector2D &) -> bool
```

Gets the projected world to screen position for a player, then converts it into a widget
	  position, which takes into account any quality scaling.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | The player controller to project the position in the world to their screen. |
| `WorldLocation` | `FVector` | The world location to project from. |
| `ScreenPosition` | `FVector2D &` | The position in the viewport with quality scale removed and DPI scale remove. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the position projects onto the screen. |

### `GetViewportScale`

```text
GetViewportScale(WorldContextObject: UObject *) -> float
```

Gets the current DPI Scale being applied to the viewport and all the Widgets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetViewportSize`

```text
GetViewportSize(WorldContextObject: UObject *) -> FVector2D
```

Gets the size of the game viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetViewportWidgetGeometry`

```text
GetViewportWidgetGeometry(WorldContextObject: UObject *) -> FGeometry
```

Gets the geometry of the widget holding all widgets added to the "Viewport".  You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FGeometry` | - |

### `GetPlayerScreenWidgetGeometry`

```text
GetPlayerScreenWidgetGeometry(PlayerController: APlayerController *) -> FGeometry
```

Gets the geometry of the widget holding all widgets added to the "Player Screen". You
	  can use this geometry to convert between absolute and local space of widgets held on this
	  widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `FGeometry` | - |

### `GetMousePositionOnPlatform`

```text
GetMousePositionOnPlatform() -> FVector2D
```

Gets the platform's mouse cursor position.  This is the 'absolute' desktop location of the mouse.

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetMousePositionOnViewport`

```text
GetMousePositionOnViewport(WorldContextObject: UObject *) -> FVector2D
```

Gets the platform's mouse cursor position in the local space of the viewport widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetMousePositionScaledByDPI`

```text
GetMousePositionScaledByDPI(Player: APlayerController *, LocationX: float &, LocationY: float &) -> bool
```

Gets the mouse position of the player controller, scaled by the DPI.  If you're trying to go from raw mouse screenspace coordinates
	  to fullscreen widget space, you'll need to transform the mouse into DPI Scaled space.  This function performs that scaling.
	 
	  MousePositionScaledByDPI = MousePosition  (1  ViewportScale).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | - |
| `LocationX` | `float &` | - |
| `LocationY` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SlotAsBorderSlot`

```text
SlotAsBorderSlot(Widget: UWidget *) -> UBorderSlot *
```

Gets the slot object on the child widget as a Border Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a border panel. |

**Returns**

| Type | Description |
|---|---|
| `UBorderSlot *` | - |

### `SlotAsCanvasSlot`

```text
SlotAsCanvasSlot(Widget: UWidget *) -> UCanvasPanelSlot *
```

Gets the slot object on the child widget as a Canvas Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a canvas panel. |

**Returns**

| Type | Description |
|---|---|
| `UCanvasPanelSlot *` | - |

### `SlotAsGridSlot`

```text
SlotAsGridSlot(Widget: UWidget *) -> UGridSlot *
```

Gets the slot object on the child widget as a Grid Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a grid panel. |

**Returns**

| Type | Description |
|---|---|
| `UGridSlot *` | - |

### `SlotAsHorizontalBoxSlot`

```text
SlotAsHorizontalBoxSlot(Widget: UWidget *) -> UHorizontalBoxSlot *
```

Gets the slot object on the child widget as a Horizontal Box Slot, allowing you to manipulate its information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a Horizontal Box. |

**Returns**

| Type | Description |
|---|---|
| `UHorizontalBoxSlot *` | - |

### `SlotAsOverlaySlot`

```text
SlotAsOverlaySlot(Widget: UWidget *) -> UOverlaySlot *
```

Gets the slot object on the child widget as a Overlay Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a overlay panel. |

**Returns**

| Type | Description |
|---|---|
| `UOverlaySlot *` | - |

### `SlotAsUniformGridSlot`

```text
SlotAsUniformGridSlot(Widget: UWidget *) -> UUniformGridSlot *
```

Gets the slot object on the child widget as a Uniform Grid Slot, allowing you to manipulate layout information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a uniform grid panel. |

**Returns**

| Type | Description |
|---|---|
| `UUniformGridSlot *` | - |

### `SlotAsVerticalBoxSlot`

```text
SlotAsVerticalBoxSlot(Widget: UWidget *) -> UVerticalBoxSlot *
```

Gets the slot object on the child widget as a Vertical Box Slot, allowing you to manipulate its information.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | The child widget of a Vertical Box. |

**Returns**

| Type | Description |
|---|---|
| `UVerticalBoxSlot *` | - |

### `RemoveAllWidgets`

```text
RemoveAllWidgets(WorldContextObject: UObject *) -> void
```

Removes all widgets from the viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNewUsedLayerPolicy`

```text
SetNewUsedLayerPolicy(Widget: UWidget *, NewLayerPolicy: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | - |
| `NewLayerPolicy` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetNavigation.json -->

# UWidgetNavigation

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Up` | `FWidgetNavigationData` | Happens when the user presses up arrow, joystick, d-pad. |
| `Down` | `FWidgetNavigationData` | Happens when the user presses down arrow, joystick, d-pad. |
| `Left` | `FWidgetNavigationData` | Happens when the user presses left arrow, joystick, d-pad. |
| `Right` | `FWidgetNavigationData` | Happens when the user presses right arrow, joystick, d-pad. |
| `Next` | `FWidgetNavigationData` | Happens when the user presses Tab. |
| `Previous` | `FWidgetNavigationData` | Happens when the user presses Shift+Tab. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetRenderTargetBox.json -->

# UWidgetRenderTargetBox

Renders its single child widget into a transparent render target.
 
  It redraws the child widget into an offscreen RT, so pixels where
  no child UI is drawn stay transparent (alpha = 0).

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RenderTarget` | `UTextureRenderTarget2D *` | Optional external render target. If unset and bAutoCreateRenderTarget is true, a transient RT is created. |
| `bRenderEnabled` | `bool` | Whether to render the child widget into the RT. |
| `bRenderEveryFrame` | `bool` | Redraw the child widget into the RT every paint. Disable this for static UI and call RequestRender when content changes. |
| `bAutoCreateRenderTarget` | `bool` | Create an internal transient render target if RenderTarget is not set. |
| `bAutoResizeRenderTarget` | `bool` | Resize the active RT to match the childwidget draw size. |
| `bMatchWidgetSize` | `bool` | Match RT size to this widget's allotted size in pixels. If false, FixedRenderTargetSize is used. |
| `FixedRenderTargetSize` | `FIntPoint` | RT size used when bMatchWidgetSize is false. |
| `RenderTargetFormat` | `TEnumAsByte < enum ETextureRenderTargetFormat >` | Pixel format used when creatingresizing the RT. |
| `ClearColor` | `FLinearColor` | Clear color. Use transparent to keep areas with no UI at alpha = 0. |
| `bDrawToScreen` | `bool` | Also draw the produced RT back to this widget's screen rect. Usually false for mesh sampling workflows. |
| `DisplayMaterial` | `UMaterialInterface *` | Optional UI material used only when bDrawToScreen is true. |
| `TextureParameterName` | `FName` | Texture parameter name used by DisplayMaterial. |
| `ColorAndOpacity` | `FLinearColor` | Tint used only when bDrawToScreen is true. |
| `OwnedRenderTarget` | `UTextureRenderTarget2D *` | - |
| `DynamicDisplayMaterial` | `UMaterialInstanceDynamic *` | - |
| `DisplayBrush` | `FSlateBrush` | - |

## Functions

### `GetActiveRenderTarget`

```text
GetActiveRenderTarget() -> UTextureRenderTarget2D *
```

Returns the external RT if set, otherwise the internally created RT.

**Returns**

| Type | Description |
|---|---|
| `UTextureRenderTarget2D *` | - |

### `RefreshDisplayResource`

```text
RefreshDisplayResource() -> void
```

Forces the RT display brushmaterial to refresh.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestRender`

```text
RequestRender() -> void
```

Request the child widget be redrawn into the render target on the next paint.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetSkin.json -->

# UWidgetSkin

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BasicUserWidget` | `TSubclassOf < UUserWidget >` | - |
| `bNeedRevertSkin` | `bool` | - |
| `ParentMatchingKey` | `int32` | - |
| `LuaModulePath` | `FString` | - |
| `bAutoLoadSubDefaultSkin` | `bool` | - |
| `bAutoReplayAnim` | `bool` | - |
| `ModifiedProperties` | `FWSPropContext` | - |
| `SkinMountInfos` | `TArray < FSkinMountInfo >` | - |
| `OriginalPropertiesMap` | `TMap < TWeakObjectPtr < UWidgetTree > , FWSPropContext >` | - |
| `ModifiedPropertiesEditorOnly` | `FWSPropContext` | - |
| `DynamicElemsEditorOnly` | `FWSDynamicPropContext` | - |
| `DynamicElementInstanceID_EditorOnly` | `int32` | - |
| `TransientDynamicElemsEditorOnly` | `FWSDynamicPropContext` | - |
| `TransientDynamicDynamicElementInstanceID_EditorOnly` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetSkinProxy.json -->

# UWidgetSkinProxy

The user widget proxy, using this proxy to activate widget skin for an user widget.

## Inheritance

`UObject` -> `IWidgetSkinProxyInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bHideBeforeLoadSkin` | `bool` | - |
| `ActiveSkins` | `TArray < UUserWidgetSkin * >` | - |

## Functions

### `ApplySkin`

```text
ApplySkin(SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >, bAsyncLoad: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |
| `bAsyncLoad` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertSkin`

```text
RevertSkin(SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertRevertableSkin`

```text
RevertRevertableSkin() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetActiveSkins`

```text
GetActiveSkins() -> TArray < UUserWidgetSkin * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UUserWidgetSkin * >` | - |

### `GetRevertableSkin`

```text
GetRevertableSkin() -> UUserWidgetSkin *
```

**Returns**

| Type | Description |
|---|---|
| `UUserWidgetSkin *` | - |

### `ContainsSkin`

```text
ContainsSkin(InSkin: UUserWidgetSkin *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSkin` | `UUserWidgetSkin *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOwnerUserWidget`

```text
GetOwnerUserWidget() -> UUserWidget *
```

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetSwitcher.json -->

# UWidgetSwitcher

A widget switcher is like a tab control, but without tabs. At most one widget is visible at time.

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveWidgetIndex` | `int32` | The slot index to display |
| `bHideInactiveWidgets` | `bool` | - |
| `ActiveWidgetIndexDelegate` | `FGetInt32` | - |

## Functions

### `GetNumWidgets`

```text
GetNumWidgets() -> int32
```

Gets the number of widgets that this switcher manages.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetActiveWidgetIndex`

```text
GetActiveWidgetIndex() -> int32
```

Gets the slot index of the currently active widget

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetLocalActiveWidgetIndex`

```text
GetLocalActiveWidgetIndex() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetActiveWidgetIndex`

```text
SetActiveWidgetIndex(Index: int32) -> void
```

Activates the widget at the specified index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActiveWidget`

```text
SetActiveWidget(Widget: UWidget *) -> void
```

Activates the widget and makes it the active index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetWidgetAtIndex`

```text
GetWidgetAtIndex(Index: int32) -> UWidget *
```

Get a widget at the provided index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

### `GetActiveWidget`

```text
GetActiveWidget() -> UWidget *
```

Get the reference of the currently active widget

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

## Delegates

### `OnActiveIndexChanged`

```text
OnActiveIndexChanged(WidgetIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnActiveIndexChangeDelegate`

```text
OnActiveIndexChangeDelegate(Percent: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Percent` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetSwitcherSlot.json -->

# UWidgetSwitcherSlot

The Slot for the UWidgetSwitcher, contains the widget that is flowed vertically

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWidgetTree.json -->

# UWidgetTree

The widget tree manages the collection of widgets in a blueprint widget.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RootWidget` | `UWidget *` | The root widget of the tree |
| `VariableWidgetMarks` | `TArray < int32 >` | - |
| `AllWidgets` | `TArray < UWidget * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWindDirectionalSourceComponent.json -->

# UWindDirectionalSourceComponent

Component that provides a directional wind source. Only affects SpeedTree assets.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Strength` | `float` | - |
| `Speed` | `float` | - |
| `MinGustAmount` | `float` | - |
| `MaxGustAmount` | `float` | - |
| `Radius` | `float` | - |
| `bPointWind` | `uint32` | - |

## Functions

### `SetStrength`

```text
SetStrength(InNewStrength: float) -> void
```

Because the actual data used to query wind is stored on the render thread in
	  an instance of FWindSourceSceneProxy all of our properties are read only.
	  The data can be manipulated with the following functions which will queue 
	  a render thread update for this component
	 
	 Sets the strength of the generated wind

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewStrength` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpeed`

```text
SetSpeed(InNewSpeed: float) -> void
```

Sets the windspeed of the generated wind

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinimumGustAmount`

```text
SetMinimumGustAmount(InNewMinGust: float) -> void
```

Set minimum deviation for wind gusts

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewMinGust` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaximumGustAmount`

```text
SetMaximumGustAmount(InNewMaxGust: float) -> void
```

Set maximum deviation for wind gusts

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewMaxGust` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRadius`

```text
SetRadius(InNewRadius: float) -> void
```

Set the effect radius for point wind

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWindType`

```text
SetWindType(InNewType: EWindSourceType) -> void
```

Set the type of wind generator to use

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewType` | `EWindSourceType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWindow.json -->

# UWindow

## Inheritance

`UUserWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Title` | `FText` | - |
| `InitSize` | `FVector2D` | - |
| `ContentSlot` | `UWindowSlot *` | - |

## Functions

### `SetTitle`

```text
SetTitle(InTitle: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTitle` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetContent`

```text
SetContent(Content: UWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Resize`

```text
Resize(NewSize: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSize` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWindowTitleBarArea.json -->

# UWindowTitleBarArea

A panel for defining a region of the UI that should allow users to drag the window on desktop platforms.

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bDoubleClickTogglesFullscreen` | `bool` | Should double clicking the title bar area toggle fullscreen instead of maximizing the window. |

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWindowTitleBarAreaSlot.json -->

# UWindowTitleBarAreaSlot

The Slot for the UWindowTitleBarArea

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWorldComposition.json -->

# UWorldComposition

WorldComposition represents world structure:
 	- Holds list of all level packages participating in this world and theirs base parameters (bounding boxes, offset from origin)
 	- Holds list of streaming level objects to stream in and out based on distance from current view point
   - Handles properly levels repositioning during level loading and saving

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Package2WorldTileExtraInfo` | `TMap < FName , FWorldTileExtraInfo >` | - |
| `LODStealConfigs` | `TArray < FLODStealConfig >` | - |
| `TilesStreaming` | `TArray < ULevelStreaming * >` | - |
| `TilesStreamingTimeThreshold` | `double` | - |
| `bLoadAllTilesDuringCinematic` | `bool` | - |
| `bRebaseOriginIn3DSpace` | `bool` | - |
| `RebaseOriginDistance` | `float` | - |
| `TileBoundsVerifyScale` | `float` | - |
| `bFlushPool` | `bool` | - |
| `ServerExcludedLevels` | `TArray < FString >` | - |
| `ClientExcludedLevels` | `TArray < FString >` | - |
| `UGCPIEMapBlackList` | `TArray < FString >` | - |
| `UGCWhiteListSubLevelPaths` | `TArray < FString >` | - |
| `DeviceExcludedLevels` | `TArray < FString >` | - |
| `DynamicSubLevelPaths` | `TArray < FString >` | - |
| `BlackLevelPaths` | `TArray < FString >` | - |
| `SpecifiedBuildingLevels` | `TArray < FString >` | - |
| `ClientLoadRadiusFactor` | `float` | - |

## Functions

### `CheckBisNeedSavedLevelToFileInServer`

```text
CheckBisNeedSavedLevelToFileInServer() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWorldParallelismBlueprintUtils.json -->

# UWorldParallelismBlueprintUtils

## Inheritance

`UObject`

## Functions

### `WorldParallelismIDWrapperToString`

```text
WorldParallelismIDWrapperToString(Wrapper: FWorldParallelismIDWrapper) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Wrapper` | `FWorldParallelismIDWrapper` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWrapBox.json -->

# UWrapBox

Arranges widgets left-to-right.  When the widgets exceed the Width it will place widgets on the next line.
  
   Many Children
   Flows
   Wraps

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InnerSlotPadding` | `FVector2D` | The inner slot padding goes between slots sharing borders |
| `WrapWidth` | `float` | When this width is exceeded, elements will start appearing on the next line. |
| `bExplicitWrapWidth` | `bool` | Use explicit wrap width whenever possible. It greatly simplifies layout calculations and reduces likelihood of "wiggling UI" |

## Functions

### `SetInnerSlotPadding`

```text
SetInnerSlotPadding(InPadding: FVector2D) -> void
```

Sets the inner slot padding goes between slots sharing borders

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddChildWrapBox`

```text
AddChildWrapBox(Content: UWidget *) -> UWrapBoxSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UWrapBoxSlot *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWrapBoxSlot.json -->

# UWrapBoxSlot

The Slot for the UWrapBox, contains the widget that is flowed vertically

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `bFillEmptySpace` | `bool` | Should this slot fill the remaining space on the line? |
| `bForceNewLine` | `bool` | Force this slot display to a new line |
| `FillSpanWhenLessThan` | `float` | If the total available space in the wrap panel drops below this threshold, this slot will attempt to fill an entire line.<br>	  NOTE: A value of 0, denotes no filling will occur. |
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

### `SetFillEmptySpace`

```text
SetFillEmptySpace(InbFillEmptySpace: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbFillEmptySpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFillSpanWhenLessThan`

```text
SetFillSpanWhenLessThan(InFillSpanWhenLessThan: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFillSpanWhenLessThan` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForceNewLine`

```text
SetForceNewLine(bInForceNewLine: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInForceNewLine` | `bool` | - |

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

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_AnchorData.json -->

# UWST_AnchorData

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FAnchorData` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Bool.json -->

# UWST_Bool

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_ButtonListenAction.json -->

# UWST_ButtonListenAction

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ListenActions` | `TArray < FButtonListenAction >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_ButtonStyle.json -->

# UWST_ButtonStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FButtonStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_CheckBoxStyle.json -->

# UWST_CheckBoxStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FCheckBoxStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_ComboBoxStyle.json -->

# UWST_ComboBoxStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FComboBoxStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_EditableTextBoxStyle.json -->

# UWST_EditableTextBoxStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FEditableTextBoxStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_EditableTextStyle.json -->

# UWST_EditableTextStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FEditableTextStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Float.json -->

# UWST_Float

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Int32.json -->

# UWST_Int32

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_LinearColor.json -->

# UWST_LinearColor

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Margin.json -->

# UWST_Margin

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FMargin` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Name.json -->

# UWST_Name

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FName` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Object.json -->

# UWST_Object

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `UObject *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_ProgressBarStyle.json -->

# UWST_ProgressBarStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FProgressBarStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_ScrollBarStyle.json -->

# UWST_ScrollBarStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FScrollBarStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_ScrollBoxStyle.json -->

# UWST_ScrollBoxStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FScrollBoxStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_SlateBrush.json -->

# UWST_SlateBrush

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FSlateBrush` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_SlateChildSize.json -->

# UWST_SlateChildSize

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FSlateChildSize` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_SlateColor.json -->

# UWST_SlateColor

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FSlateColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_SlateFontInfo.json -->

# UWST_SlateFontInfo

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FSlateFontInfo` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_SlateSound.json -->

# UWST_SlateSound

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FSlateSound` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_SliderStyle.json -->

# UWST_SliderStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FSliderStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_SpinBoxStyle.json -->

# UWST_SpinBoxStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FSpinBoxStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_String.json -->

# UWST_String

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Text.json -->

# UWST_Text

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FText` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_TextBlockStyle.json -->

# UWST_TextBlockStyle

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FTextBlockStyle` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_UInt8.json -->

# UWST_UInt8

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `uint8` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Vector.json -->

# UWST_Vector

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FVector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_Vector2D.json -->

# UWST_Vector2D

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FVector2D` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UWST_WidgetTransform.json -->

# UWST_WidgetTransform

## Inheritance

`UWigetSkinType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FWidgetTransform` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/VirtualItemManager.json -->

# VirtualItemManager

UGC虚拟物品全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VirtualItemManager.OnVirtualItemNumUpdatedDelegate` | `-` | 生效范围：客户端<br>虚拟物品数量发生变化时触发 |
| `VirtualItemManager.OnItemNumUpdatedDelegate` | `-` | 生效范围：客户端<br>物品数量（包括背包物品）发生变化时触发 |
| `VirtualItemManager.AddItemResultDelegate` | `-` | 添加物品后触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemAddItemResult @添加结果 |
| `VirtualItemManager.RemoveItemResultDelegate` | `-` | 移除物品后触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemRemoveItemResult @移除结果 |
| `VirtualItemManager.TransferToBackpackResultDelegate` | `-` | 转移虚拟物品到背包时触发<br>生效范围：客户端&&服务器<br>@param Result VirtualItemTransferResult @转移结果 |
| `VirtualItemManager.TableDataReadyDelegate` | `-` | 表格配置数据加载好时触发<br>生效范围：客户端&&服务器 |

## Functions

### `AddVirtualItems`

```text
AddVirtualItems(PlayerController: UUGCPlayerController, ItemList: table, RequestMark: string) -> boolean
```

添加多种虚拟物品
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemList` | `table` | 物品列表，key为物品ID，value为数量 |
| `RequestMark` | `string` | 发起请求标记。会传回AddItemResultDelegate的Result中，可以省略 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否添加成功 |

### `AddVirtualItem`

```text
AddVirtualItem(PlayerController: UUGCPlayerController, ItemID: number, Num: number, RequestMark: string) -> boolean
```

添加虚拟物品 
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemID` | `number` | 虚拟物品ID |
| `Num` | `number` | 添加的物品数量 |
| `RequestMark` | `string` | 发起请求标记。会传回AddItemResultDelegate的Result中，可以省略 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否添加成功 |

### `RemoveVirtualItem`

```text
RemoveVirtualItem(PlayerController: UUGCPlayerController, ItemID: number, Num: number, Callback: Delegate)
```

移除虚拟物品 
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemID` | `number` | 虚拟物品ID |
| `Num` | `number` | 移除的物品数量 |
| `Callback` | `Delegate` | 回调，可不传参 |

### `RemoveItem`

```text
RemoveItem(PlayerController: UUGCPlayerController, ItemID: number, Num: number, Callback: Delegate|function)
```

移除虚拟物品，如果物品配置了到背包的映射，则只以背包中的数量为准
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器 |
| `ItemID` | `number` | 虚拟物品ID |
| `Num` | `number` | 移除的物品数量 |
| `Callback` | `Delegate\|function` | 回调，可不传参 |

### `GetVirtualItemNum`

```text
GetVirtualItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取虚拟物品数量（不包含已转移背包的数量）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetItemNum`

```text
GetItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取虚拟物品数量（包括已转移到背包的物品）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetFreeItemNum`

```text
GetFreeItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取非绿洲币购买的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetOasisItemNum`

```text
GetOasisItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取绿洲币购买的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetMappedItemNum`

```text
GetMappedItemNum(ItemID: number, PlayerController: UUGCPlayerController) -> number
```

获取已映射到背包的物品数量
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `TransferToBackpack`

```text
TransferToBackpack(PlayerController: PlayerController, ItemID: number, ItemNum: number, bPartial: boolean)
```

将虚拟物品转移到背包（需配置映射表UGCObjectMapping）
 生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `ItemID` | `number` | 物品ID |
| `ItemNum` | `number` | 数量, 不传则默认全部转移 |
| `bPartial` | `boolean` | 是否在背包空间不足时部分转移, 默认false |

### `GetItemDatas`

```text
GetItemDatas() -> table
```

获取所有虚拟物品ID的信息
 生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetItemData`

```text
GetItemData(ItemID: number) -> table
```

获取虚拟物品ID的信息
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | 如果没有对应的值则返回nil |

### `GetClassicItemID`

```text
GetClassicItemID(ItemID: number) -> number
```

【废弃】请使用 GetMappedItemID
 获取经典物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 虚拟物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 如果没有对应的值则返回nil |

### `GetMappedItemID`

```text
GetMappedItemID(ItemID: number) -> number
```

获取虚拟物品ID对应的背包物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 虚拟物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包物品ID，如果没有配置虚拟物品ID到UGCObjectMapping表中，则返回nil |

### `GetReverseMappingDatas`

```text
GetReverseMappingDatas() -> table
```

获取所有经典物品ID到虚拟物品ID映射数据
 生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetIsEnableMappingItem`

```text
GetIsEnableMappingItem() -> boolean
```

获取是否已启用虚拟物品到背包物品的映射
 生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetVirtualItemID`

```text
GetVirtualItemID(ClassicItemID: number) -> number
```

获取虚拟物品ID
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ClassicItemID` | `number` | 经典物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 如果没有对应的值则返回nil |

### `GetOwnedVirtualItems`

```text
GetOwnedVirtualItems(PlayerController: UUGCPlayerController) -> table
```

获取所有已持有的虚拟物品
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetOwnedItems`

```text
GetOwnedItems(PlayerController: UUGCPlayerController) -> table
```

获取所有已持有的物品（包括已映射到背包的经典物品）
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetUntransferredItems`

```text
GetUntransferredItems(PlayerController: UUGCPlayerController) -> table
```

获取未转移到背包的物品
 生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端调用可以不传参，即默认主控玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `SetAutoTransferActive`

```text
SetAutoTransferActive(bActive: boolean)
```

设置是否开启自动转移背包
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bActive` | `boolean` | 是否开启自动转移 |

### `SetGetItemUIActive`

```text
SetGetItemUIActive(bShow: bool)
```

设置是否显示获得物品弹窗
如果在已显示弹窗后设置为不显示，则在当前所有弹窗显示结束后再生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShow` | `bool` | 是否显示 |

## Language

`lua`

