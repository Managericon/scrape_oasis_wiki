---
id: "api:class:UCircularThrobber"
title: "UCircularThrobber"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCircularThrobber.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCircularThrobber

A throbber widget that orients images in a spinning circle.
  
   No Children
   Spinner Progress

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumberOfPieces` | `int32` | How many pieces there are |
| `Period` | `float` | The amount of time for a full circle (in seconds) |
| `Radius` | `float` | The radius of the circle. If the throbber is a child of Canvas Panel, the 'Size to Content' option must be enabled in order to set Radius. |
| `PieceImage_DEPRECATED` | `USlateBrushAsset *` | Image to use for each segment of the throbber |
| `Image` | `FSlateBrush` | - |
| `bEnableRadius` | `bool` | - |

## Functions

### `SetNumberOfPieces`

```text
SetNumberOfPieces(InNumberOfPieces: int32) -> void
```

Sets how many pieces there are.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNumberOfPieces` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPeriod`

```text
SetPeriod(InPeriod: float) -> void
```

Sets the amount of time for a full circle (in seconds).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPeriod` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRadius`

```text
SetRadius(InRadius: float) -> void
```

Sets the radius of the circle.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
