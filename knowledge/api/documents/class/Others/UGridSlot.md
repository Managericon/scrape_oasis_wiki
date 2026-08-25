---
id: "api:class:UGridSlot"
title: "UGridSlot"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGridSlot.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGridSlot

A slot for UGridPanel, these slots all share the same size as the largest slot
  in the grid.

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Padding` | `FMargin` | The padding area between the slot and the content it contains. |
| `HorizontalAlignment` | `TEnumAsByte < EHorizontalAlignment >` | The alignment of the object horizontally. |
| `VerticalAlignment` | `TEnumAsByte < EVerticalAlignment >` | The alignment of the object vertically. |
| `Row` | `int32` | The row index of the cell this slot is in |
| `RowSpan` | `int32` | - |
| `Column` | `int32` | The column index of the cell this slot is in |
| `ColumnSpan` | `int32` | - |
| `Layer` | `int32` | Positive values offset this cell to be hit-tested and drawn on top of others. Default is 0; i.e. no offset. |
| `Nudge` | `FVector2D` | Offset this slot's content by some amount; positive values offset to lower right |

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

### `SetRowSpan`

```text
SetRowSpan(InRowSpan: int32) -> void
```

How many rows this this slot spans over

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRowSpan` | `int32` | - |

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

### `SetColumnSpan`

```text
SetColumnSpan(InColumnSpan: int32) -> void
```

How many columns this slot spans over

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColumnSpan` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLayer`

```text
SetLayer(InLayer: int32) -> void
```

Sets positive values offset this cell to be hit-tested and drawn on top of others.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLayer` | `int32` | - |

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
