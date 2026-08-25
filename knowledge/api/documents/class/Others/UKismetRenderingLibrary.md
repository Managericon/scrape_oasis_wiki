---
id: "api:class:UKismetRenderingLibrary"
title: "UKismetRenderingLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetRenderingLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetRenderingLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `ClearRenderTarget2D`

```text
ClearRenderTarget2D(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, ClearColor: FLinearColor) -> ENGINE_API void
```

Clears the specified render target with the given ClearColor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `ClearColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `CreateRenderTarget2D`

```text
CreateRenderTarget2D(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

### `CreateRenderTarget2DExt`

```text
CreateRenderTarget2DExt(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat, ClearColor: FLinearColor &) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |
| `ClearColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

### `CreateRenderTarget2DWithFilter`

```text
CreateRenderTarget2DWithFilter(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat, Filter: TextureFilter) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |
| `Filter` | `TextureFilter` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

### `ReleaseRenderTarget2D`

```text
ReleaseRenderTarget2D(TextureRenderTarget: UTextureRenderTarget2D *) -> ENGINE_API void
```

Manually releases GPU resources of a render target. This is useful for blueprint creating a lot of render target that would
	  normally be released too late by the garbage collector that can be problematic on platforms that have tight GPU memory constrains.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `DrawMaterialToRenderTarget`

```text
DrawMaterialToRenderTarget(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, Material: UMaterialInterface *) -> ENGINE_API void
```

Renders a quad with the material applied to the specified render target.   
	  This sets the render target even if it is already set, which is an expensive operation. 
	  Use BeginDrawCanvasToRenderTarget  EndDrawCanvasToRenderTarget instead if rendering multiple primitives to the same render target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `RenderTargetCreateStaticTexture2DEditorOnly`

```text
RenderTargetCreateStaticTexture2DEditorOnly(RenderTarget: UTextureRenderTarget2D *, Name: FString, CompressionSettings: TextureCompressionSettings, MipSettings: TextureMipGenSettings) -> ENGINE_API UTexture2D *
```

Creates a new Static Texture from a Render Target 2D. Render Target Must be power of two and use four channels.
	 Only works in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTarget` | `UTextureRenderTarget2D *` | - |
| `Name` | `FString` | - |
| `CompressionSettings` | `TextureCompressionSettings` | - |
| `MipSettings` | `TextureMipGenSettings` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTexture2D *` | - |

### `ConvertRenderTargetToTexture2DEditorOnly`

```text
ConvertRenderTargetToTexture2DEditorOnly(WorldContextObject: UObject *, RenderTarget: UTextureRenderTarget2D *, Texture: UTexture2D *) -> ENGINE_API void
```

Copies the contents of a render target to a UTexture2D
	  Only works in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `RenderTarget` | `UTextureRenderTarget2D *` | - |
| `Texture` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ExportRenderTarget`

```text
ExportRenderTarget(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, FilePath: FString &, FileName: FString &) -> ENGINE_API void
```

Exports a render target as a HDR or PNG image onto the disk (depending on the format of the render target)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `FilePath` | `FString &` | - |
| `FileName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ExportTexture2D`

```text
ExportTexture2D(WorldContextObject: UObject *, Texture: UTexture2D *, FilePath: FString &, FileName: FString &) -> ENGINE_API void
```

Exports a Texture2D as a HDR image onto the disk.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Texture` | `UTexture2D *` | - |
| `FilePath` | `FString &` | - |
| `FileName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `BeginDrawCanvasToRenderTarget`

```text
BeginDrawCanvasToRenderTarget(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, Canvas: UCanvas * &, Size: FVector2D &, Context: FDrawToRenderTargetContext &) -> ENGINE_API void
```

Returns a Canvas object that can be used to draw to the specified render target.
	  Canvas has functions like DrawMaterial with size parameters that can be used to draw to a specific area of a render target.
	  Be sure to call EndDrawCanvasToRenderTarget to complete the rendering!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `Canvas` | `UCanvas * &` | - |
| `Size` | `FVector2D &` | - |
| `Context` | `FDrawToRenderTargetContext &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `EndDrawCanvasToRenderTarget`

```text
EndDrawCanvasToRenderTarget(WorldContextObject: UObject *, Context: FDrawToRenderTargetContext &) -> ENGINE_API void
```

Must be paired with a BeginDrawCanvasToRenderTarget to complete rendering to a render target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Context` | `FDrawToRenderTargetContext &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `MakeSkinWeightInfo`

```text
MakeSkinWeightInfo(Bone0: int32, Weight0: uint8, Bone1: int32, Weight1: uint8, Bone2: int32, Weight2: uint8, Bone3: int32, Weight3: uint8) -> ENGINE_API FSkelMeshSkinWeightInfo
```

Create FSkelMeshSkinWeightInfo

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bone0` | `int32` | - |
| `Weight0` | `uint8` | - |
| `Bone1` | `int32` | - |
| `Weight1` | `uint8` | - |
| `Bone2` | `int32` | - |
| `Weight2` | `uint8` | - |
| `Bone3` | `int32` | - |
| `Weight3` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FSkelMeshSkinWeightInfo` | - |

### `BreakSkinWeightInfo`

```text
BreakSkinWeightInfo(InWeight: FSkelMeshSkinWeightInfo, Bone0: int32 &, Weight0: uint8 &, Bone1: int32 &, Weight1: uint8 &, Bone2: int32 &, Weight2: uint8 &, Bone3: int32 &, Weight3: uint8 &) -> ENGINE_API void
```

Break FSkelMeshSkinWeightInfo

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWeight` | `FSkelMeshSkinWeightInfo` | - |
| `Bone0` | `int32 &` | - |
| `Weight0` | `uint8 &` | - |
| `Bone1` | `int32 &` | - |
| `Weight1` | `uint8 &` | - |
| `Bone2` | `int32 &` | - |
| `Weight2` | `uint8 &` | - |
| `Bone3` | `int32 &` | - |
| `Weight3` | `uint8 &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ReadRenderTargetRawPixel`

```text
ReadRenderTargetRawPixel(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, X: int32, Y: int32) -> ENGINE_API FLinearColor
```

Incredibly inefficient and slow operation! Read a value as-is from a render target using integer pixel coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `X` | `int32` | - |
| `Y` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FLinearColor` | - |

### `ReadRenderTargetRawUV`

```text
ReadRenderTargetRawUV(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, U: float, V: float) -> ENGINE_API FLinearColor
```

Incredibly inefficient and slow operation! Read a value as-is color from a render target using UV [0,1]x[0,1] coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `U` | `float` | - |
| `V` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FLinearColor` | - |

### `NeedsToSwitchVerticalAxis`

```text
NeedsToSwitchVerticalAxis() -> ENGINE_API bool
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetCastInsetShadowForAllAttachments`

```text
SetCastInsetShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, bCastInsetShadow: bool, bLightAttachmentsAsGroup: bool) -> ENGINE_API void
```

Set the inset shadow casting state of the given component and all its child attachments.
	 	Also choose if all attachments should be grouped for the inset shadow rendering. If enabled, one depth target will be shared for all attachments.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `bCastInsetShadow` | `bool` | - |
| `bLightAttachmentsAsGroup` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetupFPPShadowForAllAttachments`

```text
SetupFPPShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetupTPPShadowForAllAttachments`

```text
SetupTPPShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ResetShadowForAllAttachments`

```text
ResetShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `RecordForAllAttachments`

```text
RecordForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetScalabilityQualityLevels`

```text
GetScalabilityQualityLevels() -> ENGINE_API FScalabilityQuality
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FScalabilityQuality` | - |

### `ApplyMaxScalabilityQualityLevels`

```text
ApplyMaxScalabilityQualityLevels() -> ENGINE_API void
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ApplyScalabilityQualityLevels`

```text
ApplyScalabilityQualityLevels(QualityLevels: FScalabilityQuality &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityLevels` | `FScalabilityQuality &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `CreateRenderTarget2D`

```text
CreateRenderTarget2D(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat, bAutoGenerateMipmap: bool) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |
| `bAutoGenerateMipmap` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

## Language

`cpp`
