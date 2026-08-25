---
id: "api:class:UComboBoxString"
title: "UComboBoxString"
source: "https://developer.gp.qq.com/api/class/detail/Others/UComboBoxString.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UComboBoxString

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultOptions` | `TArray < FString >` | The default list of items to be displayed on the combobox. |
| `SelectedOption` | `FString` | The item in the combobox to select by default |
| `WidgetStyle` | `FComboBoxStyle` | The style. |
| `ItemStyle` | `FTableRowStyle` | The item row style. |
| `ScrollBarStyle` | `FScrollBarStyle` | The scroll bar style. |
| `ContentPadding` | `FMargin` | - |
| `MaxListHeight` | `float` | The max height of the combobox list that opens |
| `HasDownArrow` | `bool` | When false, the down arrow is not generated and it is up to the API consumer<br>	  to make their own visual hint that this is a drop down. |
| `EnableGamepadNavigationMode` | `bool` | When false, directional keys will change the selection. When true, ComboBox <br>	 must be activated and will only capture arrow input while activated. |
| `Font` | `FSlateFontInfo` | The default font to use in the combobox, only applies if you're not implementing OnGenerateWidgetEvent<br>	  to factory each new entry. |
| `ForegroundColor` | `FSlateColor` | The foreground color to pass through the hierarchy. |
| `bIsFocusable` | `bool` | - |
| `bForceNotify` | `bool` | - |
| `OnGenerateWidgetEvent` | `FGenerateWidgetForString` | Called when the widget is needed for the item. |
| `OnGenerateSelectWidgetEvent` | `FGenerateWidgetForString` | - |

## Functions

### `AddOption`

```text
AddOption(Option: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Option` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveOption`

```text
RemoveOption(Option: FString &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Option` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FindOptionIndex`

```text
FindOptionIndex(Option: FString &) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Option` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetOptionAtIndex`

```text
GetOptionAtIndex(Index: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `ClearOptions`

```text
ClearOptions() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSelection`

```text
ClearSelection() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshOptions`

```text
RefreshOptions() -> void
```

Refreshes the list of options.  If you added new ones, and want to update the list even if it's
	  currently being displayed use this.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectedOption`

```text
SetSelectedOption(Option: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Option` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectedOption`

```text
GetSelectedOption() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetOptionCount`

```text
GetOptionCount() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of options |

## Delegates

### `OnSelectionChanged`

```text
OnSelectionChanged(SelectedItem: FString, SelectionType: ESelectInfo::Type) -> void
```

Called when a new item is selected in the combobox.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectedItem` | `FString` | - |
| `SelectionType` | `ESelectInfo::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnOpening`

```text
OnOpening() -> void
```

Called when the combobox is opening

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnClosing`

```text
OnClosing() -> void
```

Called when the combobox is closing

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
