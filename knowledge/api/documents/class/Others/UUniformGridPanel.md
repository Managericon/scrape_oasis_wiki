---
id: "api:class:UUniformGridPanel"
title: "UUniformGridPanel"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUniformGridPanel.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUniformGridPanel

A panel that evenly divides up available space between all of its children.

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SlotPadding` | `FMargin` | Padding given to each slot |
| `MinDesiredSlotWidth` | `float` | The minimum desired width of the slots |
| `MinDesiredSlotHeight` | `float` | The minimum desired height of the slots |

## Functions

### `SetSlotPadding`

```text
SetSlotPadding(InSlotPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSlotPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredSlotWidth`

```text
SetMinDesiredSlotWidth(InMinDesiredSlotWidth: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredSlotWidth` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinDesiredSlotHeight`

```text
SetMinDesiredSlotHeight(InMinDesiredSlotHeight: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinDesiredSlotHeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddChildToUniformGrid`

```text
AddChildToUniformGrid(Content: UWidget *) -> UUniformGridSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UUniformGridSlot *` | - |

## Language

`cpp`
