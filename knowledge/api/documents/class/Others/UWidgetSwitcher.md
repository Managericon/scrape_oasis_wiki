---
id: "api:class:UWidgetSwitcher"
title: "UWidgetSwitcher"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetSwitcher.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetSwitcher

A widget switcher is like a tab control, but without tabs. At most one widget is visible at time.

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActiveWidgetIndex` | `int32` | The slot index to display |
| `bHideInactiveWidgets` | `bool` | - |
| `ActiveWidgetIndexDelegate` | `FGetInt32` | - |

## Functions

### `GetNumWidgets`

```text
GetNumWidgets() -> int32
```

Gets the number of widgets that this switcher manages.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetActiveWidgetIndex`

```text
GetActiveWidgetIndex() -> int32
```

Gets the slot index of the currently active widget

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetLocalActiveWidgetIndex`

```text
GetLocalActiveWidgetIndex() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetActiveWidgetIndex`

```text
SetActiveWidgetIndex(Index: int32) -> void
```

Activates the widget at the specified index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActiveWidget`

```text
SetActiveWidget(Widget: UWidget *) -> void
```

Activates the widget and makes it the active index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetWidgetAtIndex`

```text
GetWidgetAtIndex(Index: int32) -> UWidget *
```

Get a widget at the provided index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

### `GetActiveWidget`

```text
GetActiveWidget() -> UWidget *
```

Get the reference of the currently active widget

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

## Delegates

### `OnActiveIndexChanged`

```text
OnActiveIndexChanged(WidgetIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnActiveIndexChangeDelegate`

```text
OnActiveIndexChangeDelegate(Percent: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Percent` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
