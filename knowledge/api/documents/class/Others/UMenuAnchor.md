---
id: "api:class:UMenuAnchor"
title: "UMenuAnchor"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMenuAnchor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMenuAnchor

The Menu Anchor allows you to specify an location that a popup menu should be anchored to, 
  and should be summoned from.
   Single Child
   Popup

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MenuClass` | `TSubclassOf < UUserWidget >` | The widget class to spawn when the menu is required.  Creates the widget freshly each time.  <br>	  If you want to customize the creation of the popup, you should bind a function to OnGetMenuContentEvent <br>	  instead. |
| `OnGetMenuContentEvent` | `FGetWidget` | Called when the menu content is requested to allow a more customized handling over what to display |
| `Placement` | `TEnumAsByte < EMenuPlacement >` | The placement location of the summoned widget. |
| `ShouldDeferPaintingAfterWindowContent` | `bool` | - |
| `UseApplicationMenuStack` | `bool` | Does this menu behave like a normal stacked menu? Set it to false to control the menu's lifetime yourself. |

## Functions

### `ToggleOpen`

```text
ToggleOpen(bFocusOnOpen: bool) -> void
```

Toggles the menus open state.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bFocusOnOpen` | `bool` | Should we focus the popup as soon as it opens? |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Open`

```text
Open(bFocusMenu: bool) -> void
```

Opens the menu if it is not already open

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bFocusMenu` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Close`

```text
Close() -> void
```

Closes the menu if it is currently open.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsOpen`

```text
IsOpen() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the popup is open; false otherwise. |

### `ShouldOpenDueToClick`

```text
ShouldOpenDueToClick() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if we should open the menu due to a click. Sometimes we should not, if |

### `GetMenuPosition`

```text
GetMenuPosition() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The current menu position |

### `HasOpenSubMenus`

```text
HasOpenSubMenus() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether this menu has open submenus |

## Delegates

### `OnMenuOpenChanged`

```text
OnMenuOpenChanged(bIsOpen: bool) -> void
```

Called when the opened state of the menu changes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsOpen` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
