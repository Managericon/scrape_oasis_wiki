---
id: "api:class:UDragDropOperation"
title: "UDragDropOperation"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDragDropOperation.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDragDropOperation

This class is the base drag drop operation for UMG, extend it to add additional data and add new functionality.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Tag` | `FString` | A simple string tag you can optionally use to provide extra metadata about the operation. |
| `Payload` | `UObject *` | The payload of the drag operation.  This can be any UObject that you want to pass along as dragged data.  If you <br>	  were building an inventory screen this would be the UObject representing the item being moved to another slot. |
| `DefaultDragVisual` | `UWidget *` | The Drag Visual is the widget to display when dragging the item.  Normally people create a new widget to represent the <br>	  temporary drag. |
| `Pivot` | `EDragPivot` | Controls where the drag widget visual will appear when dragged relative to the pointer performing<br>	  the drag operation. |
| `Offset` | `FVector2D` | A percentage offset (-1..+1) from the Pivot location, the percentage is of the desired size of the dragged visual. |
| `StartOffset` | `FVector2D` | - |
| `bRemoveMoveAnimDelay` | `bool` | - |

## Functions

### `Drop`

```text
Drop(PointerEvent: FPointerEvent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DragCancelled`

```text
DragCancelled(PointerEvent: FPointerEvent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Dragged`

```text
Dragged(PointerEvent: FPointerEvent &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnDrop`

```text
OnDrop(Operation: UDragDropOperation*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Operation` | `UDragDropOperation*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragCancelled`

```text
OnDragCancelled(Operation: UDragDropOperation*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Operation` | `UDragDropOperation*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragged`

```text
OnDragged(Operation: UDragDropOperation*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Operation` | `UDragDropOperation*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
