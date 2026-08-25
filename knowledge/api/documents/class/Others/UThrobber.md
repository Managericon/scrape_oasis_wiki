---
id: "api:class:UThrobber"
title: "UThrobber"
source: "https://developer.gp.qq.com/api/class/detail/Others/UThrobber.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
