---
id: "api:class:UVerticalBoxSlot"
title: "UVerticalBoxSlot"
source: "https://developer.gp.qq.com/api/class/detail/Others/UVerticalBoxSlot.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UVerticalBoxSlot

The Slot for the UVerticalBox, contains the widget that is flowed vertically

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

### `SetSize`

```text
SetSize(InSize: FSlateChildSize) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSize` | `FSlateChildSize` | - |

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
