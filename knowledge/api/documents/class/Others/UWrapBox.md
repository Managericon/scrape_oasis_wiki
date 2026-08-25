---
id: "api:class:UWrapBox"
title: "UWrapBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWrapBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWrapBox

Arranges widgets left-to-right.  When the widgets exceed the Width it will place widgets on the next line.
  
   Many Children
   Flows
   Wraps

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InnerSlotPadding` | `FVector2D` | The inner slot padding goes between slots sharing borders |
| `WrapWidth` | `float` | When this width is exceeded, elements will start appearing on the next line. |
| `bExplicitWrapWidth` | `bool` | Use explicit wrap width whenever possible. It greatly simplifies layout calculations and reduces likelihood of "wiggling UI" |

## Functions

### `SetInnerSlotPadding`

```text
SetInnerSlotPadding(InPadding: FVector2D) -> void
```

Sets the inner slot padding goes between slots sharing borders

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddChildWrapBox`

```text
AddChildWrapBox(Content: UWidget *) -> UWrapBoxSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UWrapBoxSlot *` | - |

## Language

`cpp`
