---
id: "api:class:UUniformGridSlot"
title: "UUniformGridSlot"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUniformGridSlot.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
