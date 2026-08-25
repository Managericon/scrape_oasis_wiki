---
id: "api:class:UStackBox"
title: "UStackBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UStackBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UStackBox

A stack box widget is a layout panel allowing child widgets to be automatically laid out
  vertically or horizontally.
 
   Many Children
   Flows Vertical or Horizontal

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Orientation` | `TEnumAsByte < EOrientation >` | The orientation of the stack box. |

## Functions

### `GetOrientation`

```text
GetOrientation() -> UMG_API EOrientation
```

Get the orientation of the stack box.

**Returns**

| Type | Description |
|---|---|
| `UMG_API EOrientation` | - |

### `SetOrientation`

```text
SetOrientation(InType: EOrientation) -> UMG_API void
```

Set the orientation of the stack box. The existing elements will be rearranged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InType` | `EOrientation` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `AddChildToStackBox`

```text
AddChildToStackBox(Content: UWidget *) -> UMG_API UStackBoxSlot *
```

Adds a new child widget to the container.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API UStackBoxSlot *` | - |

### `ReplaceStackBoxChildAt`

```text
ReplaceStackBoxChildAt(Index: int32, Content: UWidget *) -> UMG_API bool
```

Replace the widget at the given index it with a different widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API bool` | - |

## Language

`cpp`
