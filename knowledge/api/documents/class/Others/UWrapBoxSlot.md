---
id: "api:class:UWrapBoxSlot"
title: "UWrapBoxSlot"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWrapBoxSlot.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
