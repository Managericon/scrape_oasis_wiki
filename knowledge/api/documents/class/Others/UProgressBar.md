---
id: "api:class:UProgressBar"
title: "UProgressBar"
source: "https://developer.gp.qq.com/api/class/detail/Others/UProgressBar.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
