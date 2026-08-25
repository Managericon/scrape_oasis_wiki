---
id: "api:class:UImage"
title: "UImage"
source: "https://developer.gp.qq.com/api/class/detail/Others/UImage.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UImage

The image widget allows you to display a Slate Brush, or texture or material in the UI.
 
   No Children

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BrushImage` | `TSoftObjectPtr < UObject >` | - |
| `bIsEnhancedImage` | `bool` | - |
| `ForceAsyncLoadReference` | `bool` | - |
| `BrushAssetReference` | `FStringAssetReference` | - |
| `Brush` | `FSlateBrush` | Image to draw |
| `BrushMaterialParamNames` | `FString` | - |
| `BrushDelegate` | `FGetSlateBrush` | A bindable delegate for the Image. |
| `ColorAndOpacity` | `FLinearColor` | Color and opacity |
| `ColorAndOpacityDelegate` | `FGetLinearColor` | A bindable delegate for the ColorAndOpacity. |
| `bIsUseEnhancedHitTest` | `bool` | 是否使用自定义触摸响应区域，在运行时修改无效 |
| `HitTestAreaRadius` | `float` | 圆形响应区域的半径，最大为控件边长一半，-1为控件大小一半 |
| `OnMouseButtonDownEvent` | `FOnPointerEvent` | - |

## Functions

### `GetBrush`

```text
GetBrush() -> FSlateBrush
```

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FLinearColor` | - |

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

### `SetBrushImageReference`

```text
SetBrushImageReference(AssetReference: FStringAssetReference) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetReference` | `FStringAssetReference` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushImageReferenceWithMatchSize`

```text
SetBrushImageReferenceWithMatchSize(AssetReference: FStringAssetReference, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetReference` | `FStringAssetReference` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushImageReferenceWithColor`

```text
SetBrushImageReferenceWithColor(AssetReference: FStringAssetReference, Color: FLinearColor, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AssetReference` | `FStringAssetReference` | - |
| `Color` | `FLinearColor` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOpacity`

```text
SetOpacity(InOpacity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOpacity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrush`

```text
SetBrush(InBrush: FSlateBrush &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBrush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromAsset`

```text
SetBrushFromAsset(Asset: USlateBrushAsset *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Asset` | `USlateBrushAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromTexture`

```text
SetBrushFromTexture(Texture: UTexture2D *, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromTextureDynamic`

```text
SetBrushFromTextureDynamic(Texture: UTexture2DDynamic *, bMatchSize: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2DDynamic *` | - |
| `bMatchSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushFromMaterial`

```text
SetBrushFromMaterial(Material: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDynamicMaterial`

```text
GetDynamicMaterial() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

### `SetDisablePaint`

```text
SetDisablePaint(InDisablePaint: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDisablePaint` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReleaseAsyncSetBrushHandle`

```text
ReleaseAsyncSetBrushHandle() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAsyncLoadImageAssetComplete`

```text
OnAsyncLoadImageAssetComplete() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAsyncLoadAssetComplete`

```text
OnAsyncLoadAssetComplete() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnImageChangeDelegate`

```text
OnImageChangeDelegate(BrushChanged: const FSlateBrush&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BrushChanged` | `const FSlateBrush&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
