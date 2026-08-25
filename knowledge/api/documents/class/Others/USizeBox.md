---
id: "api:class:USizeBox"
title: "USizeBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/USizeBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
