---
id: "api:class:UTileView"
title: "UTileView"
source: "https://developer.gp.qq.com/api/class/detail/Others/UTileView.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UTileView

A flow panel that presents the contents as a set of tiles all uniformly sized.

## Inheritance

`UTableViewBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemWidth` | `float` | - |
| `ItemHeight` | `float` | - |
| `Items` | `TArray < UObject * >` | - |
| `SelectionMode` | `TEnumAsByte < ESelectionMode :: Type >` | - |
| `OnGenerateTileEvent` | `FOnGenerateRowUObject` | - |

## Functions

### `SetItemWidth`

```text
SetItemWidth(Width: float) -> void
```

Set item width

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Width` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetItemHeight`

```text
SetItemHeight(Height: float) -> void
```

Set item height

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Height` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RequestListRefresh`

```text
RequestListRefresh() -> void
```

Refreshes the list

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
