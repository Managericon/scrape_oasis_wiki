---
id: "api:class:UStackBoxSlot"
title: "UStackBoxSlot"
source: "https://developer.gp.qq.com/api/class/detail/Others/UStackBoxSlot.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
