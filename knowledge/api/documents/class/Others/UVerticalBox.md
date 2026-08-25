---
id: "api:class:UVerticalBox"
title: "UVerticalBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UVerticalBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UVerticalBox

A vertical box widget is a layout panel allowing child widgets to be automatically laid out
  vertically.
 
   Many Children
   Flows Vertical

## Inheritance

`UPanelWidget`

## Functions

### `AddChildToVerticalBox`

```text
AddChildToVerticalBox(Content: UWidget *) -> UVerticalBoxSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UVerticalBoxSlot *` | - |

### `InsertChild`

```text
InsertChild(Content: UWidget *, Index: int32) -> UVerticalBoxSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UVerticalBoxSlot *` | - |

## Language

`cpp`
