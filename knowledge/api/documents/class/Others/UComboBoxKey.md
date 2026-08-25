---
id: "api:class:UComboBoxKey"
title: "UComboBoxKey"
source: "https://developer.gp.qq.com/api/class/detail/Others/UComboBoxKey.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UComboBoxKey

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.
  Use OnGenerateConentWidgetEvent to return a custom built widget.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Options` | `TArray < TSharedPtr < FName > >` | . |
| `SelectedOption` | `TSharedPtr < FName >` | - |
| `WidgetStyle` | `FComboBoxStyle` | The combobox style. |
| `ItemStyle` | `FTableRowStyle` | The item row style. |
| `ScrollBarStyle` | `FScrollBarStyle` | The scroll bar style. |
| `ForegroundColor` | `FSlateColor` | The foreground color to pass through the hierarchy. |
| `ContentPadding` | `FMargin` | - |
| `MaxListHeight` | `float` | The max height of the combobox list that opens |
| `bHasDownArrow` | `bool` | When false, the down arrow is not generated and it is up to the API consumer<br>	  to make their own visual hint that this is a drop down. |
| `bEnableGamepadNavigationMode` | `bool` | When false, directional keys will change the selection. When true, ComboBox<br>	  must be activated and will only capture arrow input while activated. |
| `bIsFocusable` | `bool` | When true, allows the combo box to receive keyboard focus |

## Functions

### `AddOption`

```text
AddOption(Option: FName) -> UMG_API void
```

Add an element to the option list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Option` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `RemoveOption`

```text
RemoveOption(Option: FName) -> UMG_API bool
```

Remove an element to the option list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Option` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API bool` | - |

### `ClearOptions`

```text
ClearOptions() -> UMG_API void
```

Remove all the elements of the option list.

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `ClearSelection`

```text
ClearSelection() -> UMG_API void
```

Clear the current selection.

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `SetSelectedOption`

```text
SetSelectedOption(Option: FName) -> UMG_API void
```

Set the current selected option.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Option` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetSelectedOption`

```text
GetSelectedOption() -> UMG_API FName
```

Get the current selected option

**Returns**

| Type | Description |
|---|---|
| `UMG_API FName` | - |

### `IsOpen`

```text
IsOpen() -> UMG_API bool
```

Is the combobox menu opened.

**Returns**

| Type | Description |
|---|---|
| `UMG_API bool` | - |

### `SetContentPadding`

```text
SetContentPadding(InPadding: FMargin) -> UMG_API void
```

Set the padding for content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetContentPadding`

```text
GetContentPadding() -> UMG_API FMargin
```

Get the padding for content.

**Returns**

| Type | Description |
|---|---|
| `UMG_API FMargin` | - |

### `IsEnableGamepadNavigationMode`

```text
IsEnableGamepadNavigationMode() -> UMG_API bool
```

Is the combobox navigated by gamepad.

**Returns**

| Type | Description |
|---|---|
| `UMG_API bool` | - |

### `SetEnableGamepadNavigationMode`

```text
SetEnableGamepadNavigationMode(InEnableGamepadNavigationMode: bool) -> UMG_API void
```

Set whether the combobox is navigated by gamepad.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEnableGamepadNavigationMode` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `IsHasDownArrow`

```text
IsHasDownArrow() -> UMG_API bool
```

Is the combobox arrow showing.

**Returns**

| Type | Description |
|---|---|
| `UMG_API bool` | - |

### `SetHasDownArrow`

```text
SetHasDownArrow(InHasDownArrow: bool) -> UMG_API void
```

Set whether the combobox arrow is showing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHasDownArrow` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetMaxListHeight`

```text
GetMaxListHeight() -> UMG_API float
```

Get the maximum height of the combobox list.

**Returns**

| Type | Description |
|---|---|
| `UMG_API float` | - |

### `SetMaxListHeight`

```text
SetMaxListHeight(InMaxHeight: float) -> UMG_API void
```

Set the maximum height of the combobox list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxHeight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetWidgetStyle`

```text
GetWidgetStyle() -> const UMG_API FComboBoxStyle &
```

Get the style of the combobox.

**Returns**

| Type | Description |
|---|---|
| `const UMG_API FComboBoxStyle &` | - |

### `SetWidgetStyle`

```text
SetWidgetStyle(InWidgetStyle: FComboBoxStyle &) -> UMG_API void
```

Set the style of the combobox.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWidgetStyle` | `FComboBoxStyle &` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetItemStyle`

```text
GetItemStyle() -> const UMG_API FTableRowStyle &
```

Get the style of the items.

**Returns**

| Type | Description |
|---|---|
| `const UMG_API FTableRowStyle &` | - |

### `SetItemStyle`

```text
SetItemStyle(InItemStyle: FTableRowStyle &) -> UMG_API void
```

Set the style of the items.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemStyle` | `FTableRowStyle &` | - |

**Returns**

| Type | Description |
|---|---|
| `UMG_API void` | - |

### `GetScrollBarStyle`

```text
GetScrollBarStyle() -> const UMG_API FScrollBarStyle &
```

Get the style of the scrollbar.

**Returns**

| Type | Description |
|---|---|
| `const UMG_API FScrollBarStyle &` | - |

### `IsFocusable`

```text
IsFocusable() -> UMG_API bool
```

Is the combobox focusable.

**Returns**

| Type | Description |
|---|---|
| `UMG_API bool` | - |

### `GetForegroundColor`

```text
GetForegroundColor() -> UMG_API FSlateColor
```

Get the foreground color of the button.

**Returns**

| Type | Description |
|---|---|
| `UMG_API FSlateColor` | - |

## Delegates

### `OnGenerateContentWidget`

```text
OnGenerateContentWidget(Item: FName) -> UWidget*
```

Called when the widget is needed for the content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget*` | - |

### `OnGenerateItemWidget`

```text
OnGenerateItemWidget(Item: FName) -> UWidget*
```

Called when the widget is needed for the item.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Item` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget*` | - |

### `OnSelectionChanged`

```text
OnSelectionChanged(SelectedItem: FName, SelectionType: ESelectInfo::Type) -> void
```

Called when a new item is selected in the combobox.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectedItem` | `FName` | - |
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

## Language

`cpp`
