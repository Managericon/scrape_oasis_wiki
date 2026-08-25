---
id: "api:class:UPanelWidget"
title: "UPanelWidget"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPanelWidget.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPanelWidget

The base class for all UMG panel widgets.  Panel widgets layout a collection of child widgets.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Slots` | `TArray < UPanelSlot * >` | The slots in the widget holding the child widgets of this panel. |
| `CachedContents_ForGC` | `TArray < UWidget * >` | - |

## Functions

### `GetChildrenCount`

```text
GetChildrenCount() -> int32
```

Gets number of child widgets in the container.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetChildAt`

```text
GetChildAt(Index: int32) -> UWidget *
```

Gets the widget at an index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the widget. |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | The widget at the given index, or nothing if there is no widget there. |

### `GetChildIndex`

```text
GetChildIndex(Content: UWidget *) -> int32
```

Gets the index of a specific child widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `HasChild`

```text
HasChild(Content: UWidget *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if panel contains this widget |

### `RemoveChildAt`

```text
RemoveChildAt(Index: int32) -> bool
```

Removes a child by it's index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `AddChild`

```text
AddChild(Content: UWidget *) -> UPanelSlot *
```

Adds a new child widget to the container.  Returns the base slot type, 
	  requires casting to turn it into the type specific to the container.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UPanelSlot *` | - |

### `InsertChildAtIndex`

```text
InsertChildAtIndex(Index: int32, Content: UWidget *) -> UPanelSlot *
```

Insert a widget at a specific index, available in game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UPanelSlot *` | - |

### `ShiftChildToIndex`

```text
ShiftChildToIndex(Index: int32, Child: UWidget *) -> void
```

Moves the child widget from its current index to the new index provided, available in game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |
| `Child` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveChild`

```text
RemoveChild(Content: UWidget *) -> bool
```

Removes a specific widget from the container.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget was found and removed. |

### `HasAnyChildren`

```text
HasAnyChildren() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there are any child widgets in the panel |

### `ClearChildren`

```text
ClearChildren() -> void
```

Remove all child widgets from the panel widget.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
