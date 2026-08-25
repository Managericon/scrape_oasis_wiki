---
id: "api-chunk:class:3"
title: "Oasis API class chunk 3"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UColorPicker.json -->

# UColorPicker

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorHSV` | `FLinearColor` | - |
| `ColorHSVDelegate` | `FGetLinearColor` | - |
| `Brush` | `FSlateBrush` | - |

## Functions

### `GetColor`

```text
GetColor() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetColor`

```text
SetColor(InColorHSV: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorHSV` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleHexSRGBBoxText`

```text
HandleHexSRGBBoxText() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `HandleHexLinearString`

```text
HandleHexLinearString() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Delegates

### `OnValueChanged`

```text
OnValueChanged(InValue: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseCaptureBegin`

```text
OnMouseCaptureBegin() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseCaptureEnd`

```text
OnMouseCaptureEnd() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UColorSlider.json -->

# UColorSlider

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorHSVDelegate` | `FGetLinearColor` | - |
| `SliderHandleColorDelegate` | `FGetLinearColor` | - |
| `bUseHandleColorOrCurrentColor` | `bool` | - |
| `ColorHSV` | `FLinearColor` | - |
| `SliderHandleColor` | `FLinearColor` | - |
| `Channel` | `EColorSliderChannels` | - |
| `SliderStyle` | `FSliderStyle` | - |
| `SliderBarFrame` | `FSlateBrush` | - |

## Functions

### `GetColor`

```text
GetColor() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetColor`

```text
SetColor(InColorHSV: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorHSV` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSliderHandleColor`

```text
SetSliderHandleColor(InSliderHandleColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSliderHandleColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetColorSliderChannels`

```text
GetColorSliderChannels() -> EColorSliderChannels
```

**Returns**

| Type | Description |
|---|---|
| `EColorSliderChannels` | - |

### `SetColorSliderChannels`

```text
SetColorSliderChannels(InChannel: EColorSliderChannels) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InChannel` | `EColorSliderChannels` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUseHandleColorOrCurrentColor`

```text
SetUseHandleColorOrCurrentColor(bUse: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bUse` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnInteractiveChangeBegin`

```text
OnInteractiveChangeBegin() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInteractiveChangeEnd`

```text
OnInteractiveChangeEnd() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnValueChanged`

```text
OnValueChanged(InValue: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UComboBox.json -->

# UComboBox

The combobox allows you to display a list of options to the user in a dropdown menu for them to select one.

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Items` | `TArray < UObject * >` | The list of items to be displayed on the combobox. |
| `OnGenerateWidgetEvent` | `FGenerateWidgetForObject` | Called when the widget is needed for the item. |
| `bIsFocusable` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UComboBoxKey.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UComboBoxString.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UComboBoxWidgetStyle.json -->

# UComboBoxWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComboBoxStyle` | `FComboBoxStyle` | The actual data describing the combo box's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UComboButtonWidgetStyle.json -->

# UComboButtonWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComboButtonStyle` | `FComboButtonStyle` | The actual data describing the combo button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCommandlet.json -->

# UCommandlet

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `HelpDescription` | `FString` | Description of the commandlet's purpose |
| `HelpUsage` | `FString` | Usage template to show for "ucc help" |
| `HelpWebLink` | `FString` | Hyperlink for more info |
| `HelpParamNames` | `TArray < FString >` | The name of the parameter the commandlet takes |
| `HelpParamDescriptions` | `TArray < FString >` | The description of the parameter |
| `IsServer` | `uint32` | Whether to load objects required in server, client, and editor context.  If IsEditor is set to false, then a<br>	  UGameEngine (or whatever the value of ScriptEngine.Engine.GameEngine is) will be created for the commandlet instead<br>	  of a UEditorEngine (or ScriptEngine.Engine.EditorEngine), unless the commandlet overrides the CreateCustomEngine method. |
| `IsClient` | `uint32` | - |
| `IsEditor` | `uint32` | - |
| `LogToConsole` | `uint32` | Whether to redirect standard log to the console |
| `ShowErrorCount` | `uint32` | Whether to show standard error and warning count on exit |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCommonBattleItemHandleBase.json -->

# UCommonBattleItemHandleBase

通用扩展 ItemHandle 基类

## Inheritance

`UBattleItemHandleBase` -> `ICommonBattleItemUseInterface`

## Events

### `CanCreateItemHandleV2`

```text
CanCreateItemHandleV2() -> bool
```

能否创建物品 Handle
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许创建物品 Handle |

### `OnCreateItemHandleV2`

```text
OnCreateItemHandleV2() -> void
```

当创建物品 Handle 后回调
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanDestoryItemHandleV2`

```text
CanDestoryItemHandleV2() -> bool
```

能否销毁物品 Handle
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许销毁物品 Handle |

### `OnDestoryItemHandleV2`

```text
OnDestoryItemHandleV2() -> void
```

销毁物品 Handle 前回调
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanUpdateItemCountV2`

```text
CanUpdateItemCountV2(NewItemCount: int32, OldItemCount: int32) -> bool
```

能否更新此物品实例的数量
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewItemCount` | `int32` | - |
| `OldItemCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许物品数量更新 |

### `OnUpdateItemCountV2`

```text
OnUpdateItemCountV2(NewItemCount: int32, OldItemCount: int32) -> void
```

物品数量更新后回调
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewItemCount` | `int32` | - |
| `OldItemCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCommonDeviceProfileMatchingRules.json -->

# UCommonDeviceProfileMatchingRules

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SwitcerMatchProfile` | `TArray < FDPProfileMatch >` | Array of rules to match |
| `ChangeQualityMatchProfile` | `TArray < FDPProfileMatch >` | Array of rules to match |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UComponentDelegateBinding.json -->

# UComponentDelegateBinding

## Inheritance

`UDynamicBlueprintBinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentDelegateBindings` | `TArray < FBlueprintComponentDelegateBinding >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCompositionGraphCaptureSettings.json -->

# UCompositionGraphCaptureSettings

## Inheritance

`UMovieSceneCaptureProtocolSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IncludeRenderPasses` | `FCompositionGraphCapturePasses` | A list of render passes to include in the capture. Leave empty to export all available passes. |
| `bCaptureFramesInHDR` | `bool` | Whether to capture the frames as HDR textures (.exr format) |
| `HDRCompressionQuality` | `int32` | Compression Quality for HDR Frames (0 for no compression, 1 for default compression which can be slow) |
| `CaptureGamut` | `TEnumAsByte < enum EHDRCaptureGamut >` | The color gamut to use when storing HDR captured data. The gamut depends on whether the bCaptureFramesInHDR option is enabled. |
| `PostProcessingMaterial` | `FSoftObjectPath` | Custom post processing material to use for rendering |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UConfigOverriderFor120fps.json -->

# UConfigOverriderFor120fps

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConfigFor120fps` | `TArray < FConfigOverriderSetting >` | - |
| `ConfigForEnergySaving` | `TArray < FConfigOverriderSetting >` | - |
| `TextureLODGroupFilterOverride` | `TArray < FTextureLODGroupFilterOverride >` | - |
| `bHadApplyConfigFor120fps` | `bool` | - |
| `bHadApplyForEnergySaving` | `bool` | - |

## Functions

### `Enable120fpsConfigs`

```text
Enable120fpsConfigs(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableEnergySavingModeConfigs`

```text
EnableEnergySavingModeConfigs(bEnergySaving: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnergySaving` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecoverConfigs`

```text
RecoverConfigs() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Recover120fpsConfigs`

```text
Recover120fpsConfigs() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecoverEnergySavingModeConfigs`

```text
RecoverEnergySavingModeConfigs() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableTextureFilterOverrider`

```text
EnableTextureFilterOverrider(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UConsole.json -->

# UConsole

A basic command line console that accepts most commands.

## Inheritance

`UObject` -> `FOutputDevice`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConsoleTargetPlayer` | `ULocalPlayer *` | The player which the next console command should be executed in the context of.  If nullptr, execute in the viewport. |
| `DefaultTexture_Black` | `UTexture2D *` | - |
| `DefaultTexture_White` | `UTexture2D *` | - |
| `HistoryBuffer` | `TArray < FString >` | Holds the history buffer, order is old to new |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UConsoleSettings.json -->

# UConsoleSettings

Implements the settings for the UConsole class.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxScrollbackSize` | `int32` | Visible Console stuff |
| `ManualAutoCompleteList` | `TArray < struct FAutoCompleteCommand >` | Manual list of auto-complete commands and info specified in BaseInput.ini |
| `AutoCompleteMapPaths` | `TArray < FString >` | List of relative paths (e.g. ContentMaps) to search for map names for auto-complete usage. Specified in BaseInput.ini. |
| `BackgroundOpacityPercentage` | `float` | Amount of transparency of the console background. |
| `bOrderTopToBottom` | `bool` | Whether we legacy bottom-to-top ordering or regular top-to-bottom ordering |
| `InputColor` | `FColor` | The color used for text input. |
| `HistoryColor` | `FColor` | The color used for the previously typed commands history. |
| `AutoCompleteCommandColor` | `FColor` | The autocomplete color used for executable commands. |
| `AutoCompleteCVarColor` | `FColor` | The autocomplete color used for mutable CVars. |
| `AutoCompleteFadedColor` | `FColor` | The autocomplete color used for command descriptions and read-only CVars. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UContentWidget.json -->

# UContentWidget

## Inheritance

`UPanelWidget`

## Functions

### `GetContentSlot`

```text
GetContentSlot() -> UPanelSlot *
```

**Returns**

| Type | Description |
|---|---|
| `UPanelSlot *` | - |

### `SetContent`

```text
SetContent(Content: UWidget *) -> UPanelSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UPanelSlot *` | - |

### `GetContent`

```text
GetContent() -> UWidget *
```

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCopyMotionMathLibrary.json -->

# UCopyMotionMathLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `CopyMotionReOrientDeltaQuat`

```text
CopyMotionReOrientDeltaQuat(DeltaQuat: FQuat, NewOrientation: FQuat) -> FQuat
```

Returns result of vector A rotated by AngleDeg around Axis

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaQuat` | `FQuat` | - |
| `NewOrientation` | `FQuat` | - |

**Returns**

| Type | Description |
|---|---|
| `FQuat` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCrowdFollowingComponent.json -->

# UCrowdFollowingComponent

## Inheritance

`UPathFollowingComponent` -> `ICrowdAgentInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CrowdAgentMoveDirection` | `FVector` | - |
| `CharacterMovement` | `UCharacterMovementComponent *` | - |
| `AvoidanceGroup_DEPRECATED` | `FNavAvoidanceMask` | DEPRECATED: Group mask for this agent - use property from CharacterMovementComponent instead |
| `GroupsToAvoid_DEPRECATED` | `FNavAvoidanceMask` | DEPRECATED: Will avoid other agents if they are in one of specified groups - use property from CharacterMovementComponent instead |
| `GroupsToIgnore_DEPRECATED` | `FNavAvoidanceMask` | DEPRECATED: Will NOT avoid other agents if they are in one of specified groups, higher priority than GroupsToAvoid - use property from CharacterMovementComponent instead |

## Functions

### `SuspendCrowdSteering`

```text
SuspendCrowdSteering(bSuspend: bool) -> void
```

master switch for crowd steering & avoidance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSuspend` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCrowdManager.json -->

# UCrowdManager

## Inheritance

`UCrowdManagerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MyNavData` | `ANavigationData *` | - |
| `AvoidanceConfig` | `TArray < FCrowdAvoidanceConfig >` | obstacle avoidance params |
| `SamplingPatterns` | `TArray < FCrowdAvoidanceSamplingPattern >` | obstacle avoidance params |
| `MaxAgents` | `int32` | max number of agents supported by crowd |
| `MaxAgentRadius` | `float` | max radius of agent that can be added to crowd |
| `MaxAvoidedAgents` | `int32` | max number of neighbor agents for velocity avoidance |
| `MaxAvoidedWalls` | `int32` | max number of wall segments for velocity avoidance |
| `NavmeshCheckInterval` | `float` | how often should agents check their position after moving off navmesh? |
| `PathOptimizationInterval` | `float` | how often should agents try to optimize their paths? |
| `SeparationDirClamp` | `float` | clamp separation force to leftright when neighbor is behind (dot between forward and dirToNei, -1 = disabled) |
| `PathOffsetRadiusMultiplier` | `float` | agent radius multiplier for offsetting path around corners |
| `bResolveCollisions` | `uint32` | should crowd simulation resolve collisions between agents? if not, this will be handled by their movement components |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCurveBase.json -->

# UCurveBase

Defines a curve of interpolated points to evaluate over a given range

## Inheritance

`UObject` -> `FCurveOwnerInterface`

## Functions

### `GetTimeRange`

```text
GetTimeRange(MinTime: float &, MaxTime: float &) -> void
```

Get the time range across all curves

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MinTime` | `float &` | - |
| `MaxTime` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetValueRange`

```text
GetValueRange(MinValue: float &, MaxValue: float &) -> void
```

Get the value range across all curves

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MinValue` | `float &` | - |
| `MaxValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCurveFloat.json -->

# UCurveFloat

## Inheritance

`UCurveBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FloatCurve` | `FRichCurve` | Keyframe data |
| `bIsEventCurve` | `bool` | Flag to represent event curve |

## Functions

### `GetFloatValue`

```text
GetFloatValue(InTime: float) -> float
```

Evaluate this float curve at the specified time

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCurveLinearColor.json -->

# UCurveLinearColor

## Inheritance

`UCurveBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FloatCurves` | `FRichCurve` | Keyframe data, one curve for red, green, blue, and alpha |

## Functions

### `GetLinearColorValue`

```text
GetLinearColorValue(InTime: float) -> FLinearColor
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `GetRotationValue`

```text
GetRotationValue(InTime: float) -> FQuat
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FQuat` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCurveLinearColorAtlas.json -->

# UCurveLinearColorAtlas

Manages gradient LUT textures for registered actors and assigns them to the corresponding materials on the actor

## Inheritance

`UTexture2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureSize` | `uint32` | - |
| `bSquareResolution` | `uint32` | Set texture height equal to texture width. |
| `TextureHeight` | `uint32` | - |
| `GradientCurves` | `TArray < UCurveLinearColor * >` | - |
| `bIsDirty` | `uint32` | - |
| `bDisableAllAdjustments` | `uint32` | Disable all color adjustments to preserve negative values in curves. Color adjustments clamp to 0 when enabled. |
| `bHasCachedColorAdjustments` | `uint32` | - |
| `CachedColorAdjustments` | `FCurveAtlasColorAdjustments` | - |

## Functions

### `GetCurvePosition`

```text
GetCurvePosition(InCurve: UCurveLinearColor *, Position: float &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCurve` | `UCurveLinearColor *` | - |
| `Position` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCurveVector.json -->

# UCurveVector

## Inheritance

`UCurveBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FloatCurves` | `FRichCurve` | Keyframe data, one curve for X, Y and Z |

## Functions

### `GetVectorValue`

```text
GetVectorValue(InTime: float) -> ENGINE_API FVector
```

Evaluate this float curve at the specified time

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCustomActorMoveComponent.json -->

# UCustomActorMoveComponent

一个给ActivityBaseActor移动功能的组件，用于移动所挂载的ActivityBaseActor

## Inheritance

`UActorComponent`

## Functions

### `StartMove`

```text
StartMove() -> void
```

生效范围：S
	  开始移动

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopMove`

```text
StopMove() -> void
```

生效范围：S
	  结束移动

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMoveSpeed`

```text
SetMoveSpeed(InSpeed: float) -> void
```

生效范围：S
	  设置移动速度

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSpeed` | `float` | 速度 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGlideTime`

```text
SetGlideTime(GlideTime: float) -> void
```

生效范围：S
	  设置固定的滑行时间, 而不是使用起始点到终点位置除以速度得到这个数值

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GlideTime` | `float` | 滑行时间 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPosition`

```text
SetPosition(InStart: FVector, InEnd: FVector) -> void
```

生效范围：S
	  设置移动的起始点和终点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStart` | `FVector` | 起点 |
| `InEnd` | `FVector` | 终点 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsMoving`

```text
IsMoving() -> bool
```

生效范围：SC
	  获取Actor是否在移动
	  return 是否在移动

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `ActorMoveEvent`

```text
ActorMoveEvent(bIsMove: bool) -> void
```

移动状态改变事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsMove` | `bool` | 是否正在移动 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCustomInstancedStaticMeshComponent.json -->

# UCustomInstancedStaticMeshComponent

A custom component that efficiently renders multiple instances of the same StaticMesh.

## Inheritance

`UStaticMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseCustomBounds` | `bool` | - |
| `PerInstanceSMData` | `TArray < FInstancedStaticMeshInstanceData >` | Array of instances, bulk serialized. |
| `PerInstanceSMCustomData` | `TArray < FVector4 >` | Array of custom data for instances. This will contains NumCustomDataFloatsInstanceCount entries. The entries are represented sequantially, in instance order. Can be read in a material and manipulated through Blueprints.<br>	 	Example: If NumCustomDataFloats is 1, then each entry will belong to an instance. Custom data 0 will belong to Instance 0. Custom data 1 will belong to Instance 1 etc.<br>	 	Example: If NumCustomDataFloats is 2, then each pair of sequential entries belong to an instance. Custom data 0 and 1 will belong to Instance 0. Custom data 2 and 3 will belong to Instance 2 etc. |
| `PerInstanceSMCustomDataAdd` | `TArray < FVector4 >` | - |
| `InstancingRandomSeed` | `int32` | Value used to seed the random number stream that generates random numbers for each of this mesh's instances.<br>		this is set to zero (default), it will be populated automatically by the editor. |
| `InstanceStartCullDistance` | `int32` | Distance from camera at which each instance begins to fade out. |
| `InstanceEndCullDistance` | `int32` | Distance from camera at which each instance completely fades out. |
| `InstanceNearCullDistance` | `int32` | Distance from camera at which each instance. |
| `InstanceReorderTable` | `TArray < int32 >` | Mapping from PerInstanceSMData order to instance render buffer order. If empty, the PerInstanceSMData order is used. |
| `RemovedInstances` | `TArray < int32 >` | - |
| `InstanceVisibilityMapping` | `TMap < int32 , FInstanceVisibilityData >` | - |
| `UseDynamicInstanceBuffer` | `bool` | Set to true to permit updating the vertex buffer used in the instance buffer without recreating it completely. This should be used if you plan on dynamically changing the instances at run-time. |
| `KeepInstanceBufferCPUAccess` | `bool` | Set to true to keep instance buffer accessible by the CPU, otherwise it's discarded and considered never changing, only GPU has a copy of the data. |
| `PhysicsSerializer` | `UPhysicsSerializer *` | Serialization of all the InstanceBodies. Helps speed up physics creation time. |
| `StashInstanceTransform` | `TMap < int32 , FMatrix >` | - |
| `NumPendingLightmaps` | `int32` | Number of pending lightmaps still to be calculated (Apply()'d). |

## Functions

### `AddInstance`

```text
AddInstance(InstanceTransform: FTransform &) -> int32
```

Add an instance to this component. Transform is given in local space of this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddInstanceWorldSpace`

```text
AddInstanceWorldSpace(WorldTransform: FTransform &) -> int32
```

Add an instance to this component. Transform is given in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetCustomDataValue`

```text
SetCustomDataValue(InstanceIndex: int32, CustomDataValue: FVector4, CustomDataAddValue: FVector4, bMarkRenderStateDirty: bool) -> bool
```

Update custom data for specific instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `CustomDataValue` | `FVector4` | - |
| `CustomDataAddValue` | `FVector4` | - |
| `bMarkRenderStateDirty` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetInstanceTransform`

```text
GetInstanceTransform(InstanceIndex: int32, OutInstanceTransform: FTransform &, bWorldSpace: bool) -> bool
```

Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `OutInstanceTransform` | `FTransform &` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateInstanceTransform`

```text
UpdateInstanceTransform(InstanceIndex: int32, NewInstanceTransform: FTransform &, bWorldSpace: bool, bMarkRenderStateDirty: bool, bTeleport: bool) -> bool
```

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | The index of the instance to update |
| `NewInstanceTransform` | `FTransform &` | The new transform |
| `bWorldSpace` | `bool` | If true, the new transform interpreted as a World Space transform, otherwise it is interpreted as Local Space |
| `bMarkRenderStateDirty` | `bool` | If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance. |
| `bTeleport` | `bool` | Whether or not the instance's physics should be moved normally, or teleported (moved instantly, ignoring velocity). |

**Returns**

| Type | Description |
|---|---|
| `bool` | True on success. |

### `BatchUpdateInstancesData`

```text
BatchUpdateInstancesData(StartInstanceIndex: int32, NumInstances: int32, StartCustomData: TArray < FVector4 > &, StartCustomDataAdd: TArray < FVector4 > &, bMarkRenderStateDirty: bool, bTeleport: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartInstanceIndex` | `int32` | - |
| `NumInstances` | `int32` | - |
| `StartCustomData` | `TArray < FVector4 > &` | - |
| `StartCustomDataAdd` | `TArray < FVector4 > &` | - |
| `bMarkRenderStateDirty` | `bool` | - |
| `bTeleport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveInstance`

```text
RemoveInstance(InstanceIndex: int32) -> bool
```

Remove the instance specified. Returns True on success. Note that this will leave the array in order, but may shrink it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearInstances`

```text
ClearInstances() -> void
```

Clear all instances being rendered by this component.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceCount`

```text
GetInstanceCount() -> int32
```

Get the number of instances in this component.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetCullDistances`

```text
SetCullDistances(StartCullDistance: int32, EndCullDistance: int32) -> void
```

Sets the fading start and culling end distances for this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartCullDistance` | `int32` | - |
| `EndCullDistance` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNearCullDistance`

```text
SetNearCullDistance(CullDistance: int32) -> void
```

Sets the cull near distance for this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CullDistance` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstancesOverlappingSphere`

```text
GetInstancesOverlappingSphere(Center: FVector &, Radius: float, bSphereInWorldSpace: bool) -> TArray < int32 >
```

Returns the instances with instance bounds overlapping the specified sphere. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector &` | - |
| `Radius` | `float` | - |
| `bSphereInWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < int32 >` | - |

### `GetInstancesOverlappingBox`

```text
GetInstancesOverlappingBox(Box: FBox &, bBoxInWorldSpace: bool) -> TArray < int32 >
```

Returns the instances with instance bounds overlapping the specified box. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Box` | `FBox &` | - |
| `bBoxInWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < int32 >` | - |

### `HideInstance`

```text
HideInstance(InstanceIndices: TArray < int32 > &, bForceLocalLocation: bool) -> bool
```

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndices` | `TArray < int32 > &` | - |
| `bForceLocalLocation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True on success. |

### `ShowInstance`

```text
ShowInstance(InstanceIndices: TArray < int32 > &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndices` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UCustomWeightConfig.json -->

# UCustomWeightConfig

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CustomWeightAllocations` | `TArray < FLandscapeCustomWeightAllocation >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDamageType.json -->

# UDamageType

A DamageType is intended to define and describe a particular form of damage and to provide an avenue 
  for customizing responses to damage from various sources.
 
  For example, a game could make a DamageType_Fire set it up to ignite the damaged actor.
 
  DamageTypes are never instanced and should be treated as immutable data holders with static code
  functionality.  They should never be stateful.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCausedByWorld` | `uint32` | True if this damagetype is caused by the world (falling off level, into lava, etc). |
| `bScaleMomentumByMass` | `uint32` | True to scale imparted momentum by the receiving pawn's mass for pawns using character movement |
| `bRadialDamageVelChange` | `uint32` | When applying radial impulses, whether to treat as impulse or velocity change. |
| `DamageImpulse` | `float` | The magnitude of impulse to apply to the Actors damaged by this type. |
| `DestructibleImpulse` | `float` | How large the impulse should be applied to destructible meshes |
| `DestructibleDamageSpreadScale` | `float` | How much the damage spreads on a destructible mesh |
| `DamageFalloff` | `float` | Damage fall-off for radius damage (exponent).  Default 1.0=linear, 2.0=square of distance, etc. |

## Functions

### `HasDamageTypeTags_DamageType`

```text
HasDamageTypeTags_DamageType() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDamageTypeTags_DamageType`

```text
GetDamageTypeTags_DamageType(OutTags: TArray < FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutTags` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDataAsset.json -->

# UDataAsset

Base class for a simple asset containing data. The editor will list this in the content browser if you inherit from this class

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NativeClass` | `TSubclassOf < UDataAsset >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDataTable.json -->

# UDataTable

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RowStruct` | `UScriptStruct *` | Structure to use for each row of the table, must inherit from FTableRowBase |
| `RowNameToCategoryMap` | `TMap < FName , FName >` | - |
| `CategoryMap` | `TMap < FName , int32 >` | - |
| `AssetImportData` | `UAssetImportData *` | - |
| `ImportPath_DEPRECATED` | `FString` | The filename imported to create this object. Relative to this object's package, BaseDir() or absolute |
| `RowStructName` | `FName` | The name of the RowStruct we were using when we were last saved |
| `IgnoreEmptyRowError` | `bool` | 是否忽略空数据错误,added by fourthchen |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDataTableFunctionLibrary.json -->

# UDataTableFunctionLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `EvaluateCurveTableRow`

```text
EvaluateCurveTableRow(CurveTable: UCurveTable *, RowName: FName, InXY: float, OutResult: TEnumAsByte < EEvaluateCurveTableResult :: Type > &, OutXY: float &, ContextString: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurveTable` | `UCurveTable *` | - |
| `RowName` | `FName` | - |
| `InXY` | `float` | - |
| `OutResult` | `TEnumAsByte < EEvaluateCurveTableResult :: Type > &` | - |
| `OutXY` | `float &` | - |
| `ContextString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDataTableRowNames`

```text
GetDataTableRowNames(Table: UDataTable *, OutRowNames: TArray < FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Table` | `UDataTable *` | - |
| `OutRowNames` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDataTableRowFromName`

```text
GetDataTableRowFromName(Table: UDataTable *, RowName: FName, OutRow: FTableRowBase &) -> bool
```

Get a Row from a DataTable given a RowName

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Table` | `UDataTable *` | - |
| `RowName` | `FName` | - |
| `OutRow` | `FTableRowBase &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FillDataTableFromCSVString`

```text
FillDataTableFromCSVString(DataTable: UDataTable *, CSVString: FString &) -> bool
```

Empty and fill a Data Table from CSV string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DataTable` | `UDataTable *` | - |
| `CSVString` | `FString &` | The Data that representing the contents of a CSV file. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the operation succeeds, check the log for errors if it didn't succeed. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDecalBakingParameterComponent.json -->

# UDecalBakingParameterComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DecalTexture` | `UTexture2D *` | - |
| `DecalSize` | `FVector` | - |
| `UVScaleBias` | `FVector4` | - |
| `TintColor` | `FLinearColor` | - |
| `CropUVScaleBias` | `FVector4` | - |
| `CropRotation` | `float` | - |
| `bEnableDepthCompare` | `bool` | - |

## Functions

### `GetUVScaleBias`

```text
GetUVScaleBias() -> FORCEINLINE FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FORCEINLINE FLinearColor` | - |

### `GetCropUVScaleBias`

```text
GetCropUVScaleBias() -> FORCEINLINE FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FORCEINLINE FLinearColor` | - |

### `GetDecalBounds`

```text
GetDecalBounds() -> FBoxSphereBounds
```

**Returns**

| Type | Description |
|---|---|
| `FBoxSphereBounds` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDecalComponent.json -->

# UDecalComponent

A material that is rendered onto the surface of a mesh. A kind of 'bumper sticker' for a model.
 
  @see UDecalActor

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DecalMaterial` | `UMaterialInterface *` | Decal material. |
| `SortOrder` | `int32` | Controls the order in which decal elements are rendered.  Higher values draw later (on top). <br>	  Setting many different sort orders on many different decals prevents sorting by state and can reduce performance. |
| `FadeScreenSize` | `float` | - |
| `FadeStartDelay` | `float` | Time in seconds to wait before beginning to fade out the decal. Set fade duration and start delay to 0 to make persistent. |
| `FadeDuration` | `float` | Time in seconds for the decal to fade out. Set fade duration and start delay to 0 to make persistent. Only fades in active simulation or game. |
| `bDestroyOwnerAfterFade` | `uint8` | Automatically destroys the owning actor after fully fading out. |
| `bDrawToTerrainVT` | `uint8` | - |
| `DecalSize` | `FVector` | Decal size in local space (does not include the component scale), technically redundant but there for convenience |
| `PreviewSurfaceMaterial` | `UMaterialInterface *` | ES31 管线下 Decal Mesh 预览：Surface 域母材质 |
| `bAutoGeneratePreview` | `bool` | 是否在 Transform  DecalSize  Preview 参数变化时自动重新生成 Preview Mesh |
| `SkylightIntensityScale` | `float` | Preview Mesh 的天光强度缩放系数 |
| `TintColor` | `FLinearColor` | Preview  正式 Mesh 的 TintColor，写入顶点色 |
| `bDecalHiddenByPreview` | `bool` | 当前组件是否被 Preview Mesh 隐藏，用于 Clear  PostLoad 恢复 |
| `bBakeWithLandscape` | `uint8` | Whether bake decal to the landscape flatten material |

## Functions

### `SetDrawToTerrainVT`

```text
SetDrawToTerrainVT(DrawToTerrainVT: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DrawToTerrainVT` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFadeStartDelay`

```text
GetFadeStartDelay() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetFadeDuration`

```text
GetFadeDuration() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetFadeOut`

```text
SetFadeOut(StartDelay: float, Duration: float, DestroyOwnerAfterFade: bool) -> void
```

Sets the decal's fade start time, duration and if the owning actor should be destroyed after the decal is fully faded out.
	 The default value of 0 for FadeStartDelay and FadeDuration makes the decal persistent. See DecalLifetimeOpacity material 
	 node to control the look of "fading out."

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartDelay` | `float` | - Time in seconds to wait before beginning to fade out the decal. |
| `Duration` | `float` | - Time in second for the decal to fade out. |
| `DestroyOwnerAfterFade` | `bool` | - Should the owning actor automatically be destroyed after it is completely faded out. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFadeScreenSize`

```text
SetFadeScreenSize(NewFadeScreenSize: float) -> void
```

Set the FadeScreenSize for this decal component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewFadeScreenSize` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSortOrder`

```text
SetSortOrder(Value: int32) -> void
```

Sets the sort order for the decal component. Higher values draw later (on top). This will force the decal to reattach

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDecalMaterial`

```text
SetDecalMaterial(NewDecalMaterial: UMaterialInterface *) -> void
```

setting decal material on decal component. This will force the decal to reattach

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDecalMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDecalMaterial`

```text
GetDecalMaterial() -> UMaterialInterface *
```

Accessor for decal material

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `CreateDynamicMaterialInstance`

```text
CreateDynamicMaterialInstance() -> UMaterialInstanceDynamic *
```

Utility to allocate a new Dynamic Material Instance, set its parent to the currently applied material, and assign it

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDefaultLevelSequenceInstanceData.json -->

# UDefaultLevelSequenceInstanceData

Default instance data class that level sequences understand. Implements IMovieSceneTransformOrigin.

## Inheritance

`UObject` -> `IMovieSceneTransformOrigin`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TransformOriginActor` | `AActor *` | When set, this actor's world position will be used as the transform origin for all absolute transform sections |
| `TransformOrigin` | `FTransform` | Specifies a transform that offsets all absolute transform sections in this sequence. Will compound with attach tracks. Scale is ignored. Not applied to Relative or Additive sections. |
| `ShouldIgnoreScale` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDemoNetConnection.json -->

# UDemoNetConnection

Simulated network connection for recording and playing back game sessions.

## Inheritance

`UNetConnection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MinRegionActorTickDelta` | `float` | - |
| `MaxRegionActorTickDelta` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDemoNetDriver.json -->

# UDemoNetDriver

Simulated network driver for recording and playing back game sessions.

## Inheritance

`UNetDriver`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RollbackNetStartupActors` | `TMap < FString , FRollbackNetStartupActorInfo >` | Net startup actors that need to be rolled back during scrubbing by being destroyed and re-spawned <br>	  NOTE - DeletedNetStartupActors will take precedence here, and destroy the actor instead |
| `CheckpointSaveMaxMSPerFrame` | `float` | Maximum time allowed each frame to spend on saving a checkpoint. If 0, it will save the checkpoint in a single frame, regardless of how long it takes.<br>	  See also demo.CheckpointSaveMaxMSPerFrameOverride. |
| `bIsLocalReplay` | `bool` | - |
| `GameInstance` | `UGameInstance *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDeviceProfile.json -->

# UDeviceProfile

## Inheritance

`UTextureLODSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeviceType` | `FString` | The type of this profile, I.e. IOS, Windows, PS4 etc |
| `BaseProfileName` | `FString` | The name of the parent profile of this object |
| `Parent` | `UObject *` | The parent object of this profile, it is the object matching this DeviceType with the BaseProfileName |
| `CVars` | `TArray < FString >` | The collection of CVars which is set from this profile |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDeviceProfileManager.json -->

# UDeviceProfileManager

Implements a helper class that manages all profiles in the Device

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Profiles` | `TArray < UObject * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDialogueVoice.json -->

# UDialogueVoice

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Gender` | `TEnumAsByte < EGrammaticalGender :: Type >` | - |
| `Plurality` | `TEnumAsByte < EGrammaticalNumber :: Type >` | - |
| `LocalizationGUID` | `FGuid` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDialogueWave.json -->

# UDialogueWave

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bMature` | `uint32` | true if this dialogue is considered to contain matureadult content. |
| `bOverride_SubtitleOverride` | `uint32` | - |
| `SpokenText` | `FString` | A localized version of the text that is actually spoken phonetically in the audio. |
| `SubtitleOverride` | `FString` | A localized version of the subtitle text that should be displayed for this audio. By default this will be the same as the Spoken Text. |
| `ContextMappings` | `TArray < FDialogueContextMapping >` | Mappings between dialogue contexts and associated soundwaves. |
| `LocalizationGUID` | `FGuid` | - |
| `VoiceActorDirection` | `FString` | Provides general notes to the voice actor intended to direct their performance, as well as contextual information to the translator. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDirectionalLightComponent.json -->

# UDirectionalLightComponent

A light component that has parallel rays. Will provide a uniform lighting across any affected surface (eg. The Sun). This will affect all objects in the defined light-mass importance volume.

## Inheritance

`ULightComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableLightShaftOcclusion` | `uint32` | Whether to occlude fog and atmosphere inscattering with screenspace blurred occlusion from this light. |
| `OcclusionMaskDarkness` | `float` | Controls how dark the occlusion masking is, a value of 1 results in no darkening term. |
| `OcclusionDepthRange` | `float` | Everything closer to the camera than this distance will occlude light shafts. |
| `LightShaftOverrideDirection` | `FVector` | Can be used to make light shafts come from somewhere other than the light's actual direction.<br>	  This will only be used when non-zero.  It does not have to be normalized. |
| `WholeSceneDynamicShadowRadius_DEPRECATED` | `float` | - |
| `DynamicShadowDistanceMovableLight` | `float` | How far Cascaded Shadow Map dynamic shadows will cover for a movable light, measured from the camera.<br>	  A value of 0 disables the dynamic shadow. |
| `DynamicShadowDistanceStationaryLight` | `float` | How far Cascaded Shadow Map dynamic shadows will cover for a stationary light, measured from the camera.<br>	  A value of 0 disables the dynamic shadow. |
| `DynamicShadowCascades` | `int32` | Number of cascades to split the view frustum into for the whole scene dynamic shadow.<br>	  More cascades result in better shadow resolution, but adds significant rendering cost. |
| `CascadeDistributionExponent` | `float` | Controls whether the cascades are distributed closer to the camera (larger exponent) or further from the camera (smaller exponent).<br>	  An exponent of 1 means that cascade transitions will happen at a distance proportional to their resolution. |
| `CascadeTransitionFraction` | `float` | Proportion of the fade region between cascades.<br>	  Pixels within the fade region of two cascades have their shadows blended to avoid hard transitions between quality levels.<br>	  A value of zero eliminates the fade region, creating hard transitions.<br>	  Higher values increase the size of the fade region, creating a more gradual transition between cascades.<br>	  The value is expressed as a percentage proportion (i.e. 0.1 = 10% overlap).<br>	  Ideal values are the smallest possible which still hide the transition.<br>	  An increased fade region size causes an increase in shadow rendering cost. |
| `ShadowDistanceFadeoutFraction` | `float` | Controls the size of the fade out region at the far extent of the dynamic shadow's influence.<br>	  This is specified as a fraction of DynamicShadowDistance. |
| `bUseIndependentShadowBound` | `uint32` | - |
| `ShadowCenterOffset` | `float` | Offset of the CSM shadow center in the viewing direction. |
| `ShadowIndependentRadius` | `float` | - |
| `bUseInsetShadowsForMovableObjects` | `uint32` | Stationary lights only: Whether to use per-object inset shadows for movable components, even though cascaded shadow maps are enabled.<br>	  This allows dynamic objects to have a shadow even when they are outside of the cascaded shadow map, which is important when DynamicShadowDistanceStationaryLight is small.<br>	  If DynamicShadowDistanceStationaryLight is large (currently > 8000), this will be forced off.<br>	  Disabling this can reduce shadowing cost significantly with many movable objects. |
| `FarShadowCascadeCount` | `int32` | 0: no DistantShadowCascades, otherwise the count of cascades between WholeSceneDynamicShadowRadius and DistantShadowDistance that are covered by distant shadow cascades. |
| `FarShadowDistance` | `float` | Distance at which the far shadow cascade should end.  Far shadows will cover the range between 'Dynamic Shadow Distance' and this distance. |
| `DistanceFieldShadowDistance` | `float` | Distance at which the ray traced shadow cascade should end.  Distance field shadows will cover the range between 'Dynamic Shadow Distance' this distance. |
| `ForwardShadingPriority` | `int32` | Forward lighting priority for the single directional light that will be used for forward shading, translucent, single layer water and volumetric fog.<br>	 When two lights have equal priorities, the selection will be based on their overall brightness as a fallback. |
| `LightSourceAngle` | `float` | Light source angle in degrees, used for dynamic shadowing methods.<br>	  Currently only Ray Traced Distance Field shadows and Capsule shadows support area shadows, and therefore make use of LightSourceAngle. |
| `TraceDistance` | `float` | Determines how far shadows can be cast, in world units.  Larger values increase the shadowing cost. |
| `LightmassSettings` | `FLightmassDirectionalLightSettings` | The Lightmass settings for this object. |
| `bCastModulatedShadows` | `uint32` | Whether the light should cast modulated shadows from dynamic objects (mobile only).  Also requires Cast Shadows to be set to True. |
| `bCastsLandscapeShadow` | `uint32` | - |
| `LandscapeShadowColor` | `float` | - |
| `LandscapeShadowOffset` | `float` | - |
| `LandscapeShadowSoftHeight` | `float` | - |
| `LandscapeShadowPixelPrecision` | `float` | - |
| `LandscapeGeometry` | `ULandscapeGeometryAsset *` | - |
| `bCastPhotonShadow` | `uint32` | #if WITH_PHOTON_SHADOW<br>	 Whether the light should cast photon shadow for character<br>	 #endif |
| `bCastPhotonPerObjectShadow` | `uint32` | - |
| `SoftShadowSoftness` | `float` | - |
| `ShadowBlendFactor` | `float` | - |
| `BoundsScale` | `float` | - |
| `NearPlaneOffset` | `float` | - |
| `FarPlaneOffset` | `float` | - |
| `SplitNearOffset` | `float` | - |
| `SplitFarOffset` | `float` | - |
| `ShadowMapResolution` | `float` | - |
| `ModulatedShadowColor` | `FColor` | Color to modulate against the scene color when rendering modulated shadows. (mobile only) |
| `ACESParameters` | `TArray < FACESParameter >` | - |
| `bUsedAsAtmosphereSunLight` | `uint32` | - |
| `bCastsCloudShadow` | `uint32` | - |
| `CloudShadowTexture` | `UTexture *` | - |
| `CloudShadowTileSize` | `float` | - |
| `CloudShadowDensity` | `float` | - |
| `CloudShadowWinSpeed` | `FVector2D` | - |
| `bUseGridShadow` | `uint32` | - |
| `GridShadowSplitSettings` | `TArray < FGridShadowSplitSettings >` | - |

## Functions

### `SetCastPhotonPerObjectShadow`

```text
SetCastPhotonPerObjectShadow(InValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicShadowDistanceMovableLight`

```text
SetDynamicShadowDistanceMovableLight(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicShadowDistanceStationaryLight`

```text
SetDynamicShadowDistanceStationaryLight(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicShadowCascades`

```text
SetDynamicShadowCascades(NewValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCascadeDistributionExponent`

```text
SetCascadeDistributionExponent(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCascadeTransitionFraction`

```text
SetCascadeTransitionFraction(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetShadowDistanceFadeoutFraction`

```text
SetShadowDistanceFadeoutFraction(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForwardShadingPriority`

```text
SetForwardShadingPriority(NewValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableLightShaftOcclusion`

```text
SetEnableLightShaftOcclusion(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOcclusionMaskDarkness`

```text
SetOcclusionMaskDarkness(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightShaftOverrideDirection`

```text
SetLightShaftOverrideDirection(NewValue: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastsCloudShadow`

```text
SetCastsCloudShadow(InValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowTexture`

```text
SetCloudShadowTexture(InTexture: UTexture *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTexture` | `UTexture *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowTileSize`

```text
SetCloudShadowTileSize(InValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowDensity`

```text
SetCloudShadowDensity(InDensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCloudShadowWinSpeed`

```text
SetCloudShadowWinSpeed(InWinSpeed: FVector2D &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWinSpeed` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionFloat.json -->

# UDistributionFloat

## Inheritance

`UDistribution`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanBeBaked` | `uint32` | Can this variable be baked out to a FRawDistribution? Should be true 99% of the time |
| `bBakedDataSuccesfully` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionFloatConstant.json -->

# UDistributionFloatConstant

## Inheritance

`UDistributionFloat`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Constant` | `float` | This float will be returned for all values of time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionFloatConstantCurve.json -->

# UDistributionFloatConstantCurve

## Inheritance

`UDistributionFloat`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstantCurve` | `FInterpCurveFloat` | Keyframe data for how output constant varies over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionFloatParameterBase.json -->

# UDistributionFloatParameterBase

## Inheritance

`UDistributionFloatConstant`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | todo document |
| `MinInput` | `float` | todo document |
| `MaxInput` | `float` | todo document |
| `MinOutput` | `float` | todo document |
| `MaxOutput` | `float` | todo document |
| `ParamMode` | `TEnumAsByte < enum DistributionParamMode >` | todo document |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionFloatUniform.json -->

# UDistributionFloatUniform

## Inheritance

`UDistributionFloat`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Min` | `float` | Low end of output float distribution. |
| `Max` | `float` | High end of output float distribution. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionFloatUniformCurve.json -->

# UDistributionFloatUniformCurve

## Inheritance

`UDistributionFloat`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstantCurve` | `FInterpCurveVector2D` | Keyframe data for how output constant varies over time. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionVector.json -->

# UDistributionVector

## Inheritance

`UDistribution`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCanBeBaked` | `uint32` | Can this variable be baked out to a FRawDistribution? Should be true 99% of the time |
| `bIsDirty` | `uint32` | Set internally when the distribution is updated so that that FRawDistribution can know to update itself |
| `bBakedDataSuccesfully` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorConstant.json -->

# UDistributionVectorConstant

## Inheritance

`UDistributionVector`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Constant` | `FVector` | This FVector will be returned for all input times. |
| `bLockAxes` | `uint32` | If true, X == Y == Z ie. only one degree of freedom. If false, each axis is picked independently. |
| `LockedAxes` | `TEnumAsByte < enum EDistributionVectorLockFlags >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorConstantCurve.json -->

# UDistributionVectorConstantCurve

## Inheritance

`UDistributionVector`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstantCurve` | `FInterpCurveVector` | Keyframe data for each component (X,Y,Z) over time. |
| `bLockAxes` | `uint32` | If true, X == Y == Z ie. only one degree of freedom. If false, each axis is picked independently. |
| `LockedAxes` | `TEnumAsByte < enum EDistributionVectorLockFlags >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorParameterBase.json -->

# UDistributionVectorParameterBase

## Inheritance

`UDistributionVectorConstant`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `MinInput` | `FVector` | - |
| `MaxInput` | `FVector` | - |
| `MinOutput` | `FVector` | - |
| `MaxOutput` | `FVector` | - |
| `ParamModes` | `TEnumAsByte < DistributionParamMode >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorUniform.json -->

# UDistributionVectorUniform

## Inheritance

`UDistributionVector`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Max` | `FVector` | Upper end of FVector magnitude range. |
| `Min` | `FVector` | Lower end of FVector magnitude range. |
| `bLockAxes` | `uint32` | If true, X == Y == Z ie. only one degree of freedom. If false, each axis is picked independently. |
| `LockedAxes` | `TEnumAsByte < enum EDistributionVectorLockFlags >` | - |
| `MirrorFlags` | `TEnumAsByte < enum EDistributionVectorMirrorFlags >` | - |
| `bUseExtremes` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDistributionVectorUniformCurve.json -->

# UDistributionVectorUniformCurve

## Inheritance

`UDistributionVector`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstantCurve` | `FInterpCurveTwoVectors` | Keyframe data for how output constant varies over time. |
| `bLockAxes1` | `uint32` | If true, X == Y == Z ie. only one degree of freedom. If false, each axis is picked independently. |
| `bLockAxes2` | `uint32` | - |
| `LockedAxes` | `TEnumAsByte < enum EDistributionVectorLockFlags >` | - |
| `MirrorFlags` | `TEnumAsByte < enum EDistributionVectorMirrorFlags >` | - |
| `bUseExtremes` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDragDropOperation.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDrawFrustumComponent.json -->

# UDrawFrustumComponent

Utility component for drawing a view frustum. Origin is at the component location, frustum points down position X axis.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FrustumColor` | `FColor` | Color to draw the wireframe frustum. |
| `FrustumAngle` | `float` | Angle of longest dimension of view shape. <br>	   If the angle is 0 then an orthographic projection is used |
| `FrustumAspectRatio` | `float` | Ratio of horizontal size over vertical size. |
| `FrustumStartDist` | `float` | Distance from origin to start drawing the frustum. |
| `FrustumEndDist` | `float` | Distance from origin to stop drawing the frustum. |
| `Texture` | `UTexture *` | optional texture to show on the near plane |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDynamicAtlasTexture2D.json -->

# UDynamicAtlasTexture2D

## Inheritance

`UTexture2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChildTexures_EditorOnly` | `TArray < UTexture2D * >` | - |

## Functions

### `CreateAtlasTexture2D`

```text
CreateAtlasTexture2D(MergedTexture: FAtlasTextures &, StandardAtlas: FAtlasTextures *) -> ENGINE_API UDynamicAtlasTexture2D *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MergedTexture` | `FAtlasTextures &` | - |
| `StandardAtlas` | `FAtlasTextures *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UDynamicAtlasTexture2D *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UDynamicInputBindingComponent.json -->

# UDynamicInputBindingComponent

## Inheritance

`UActorComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActionBindingClusters` | `TArray < FActionBindingCluster >` | - |
| `AxisBindingClusters` | `TArray < FAxisBindingCluster >` | - |

## Functions

### `BindAction`

```text
BindAction(ActionName: FName &, ActorInputEvent: EActorInputEvent, FunctionName: FName &, bConsumeInput: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName &` | - |
| `ActorInputEvent` | `EActorInputEvent` | - |
| `FunctionName` | `FName &` | - |
| `bConsumeInput` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindAxis`

```text
BindAxis(AxisName: FName &, FunctionName: FName &, bConsumeInput: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisName` | `FName &` | - |
| `FunctionName` | `FName &` | - |
| `bConsumeInput` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveActionBinding`

```text
RemoveActionBinding(ActionName: FName &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAxisBinding`

```text
RemoveAxisBinding(AxisName: FName &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisName` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindActionCluster`

```text
BindActionCluster(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindAxisCluster`

```text
BindAxisCluster(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveActionClusterBinding`

```text
RemoveActionClusterBinding(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAxisClusterBinding`

```text
RemoveAxisClusterBinding(Index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEdGraph.json -->

# UEdGraph

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Schema` | `TSubclassOf < UEdGraphSchema >` | The schema that this graph obeys |
| `Nodes` | `TArray < UEdGraphNode * >` | Set of all nodes in this graph |
| `bEditable` | `uint32` | If true, graph can be edited by the user |
| `bAllowDeletion` | `uint32` | - |
| `bAllowRenaming` | `uint32` | If true, graph can be renamed; Note: Graph can also be renamed if bAllowDeletion is true currently |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEdGraphNode.json -->

# UEdGraphNode

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeprecatedPins` | `TArray < UEdGraphPin_Deprecated * >` | List of connector pins |
| `NodePosX` | `int32` | X position of node in the editor |
| `NodePosY` | `int32` | Y position of node in the editor |
| `NodeWidth` | `int32` | Width of node in the editor; only used when the node can be resized |
| `NodeHeight` | `int32` | Height of node in the editor; only used when the node can be resized |
| `AdvancedPinDisplay` | `TEnumAsByte < ENodeAdvancedPins :: Type >` | Enum to indicate if a node has advanced-display-pins, and if they are shown |
| `EnabledState` | `ENodeEnabledState` | Indicates in what state the node is enabled, which may eliminate it from being compiled |
| `bUserSetEnabledState` | `uint8` | Indicates whether or not the user explicitly set the enabled state |
| `bIsNodeEnabled_DEPRECATED` | `uint8` | (DEPRECATED) FALSE if the node is a disabled, which eliminates it from being compiled |
| `bHasCompilerMessage` | `uint8` | Flag to check for compile errorwarning |
| `bCommentBubblePinned` | `uint8` | Comment bubble pinned state |
| `bCommentBubbleVisible` | `uint8` | Comment bubble visibility |
| `bCommentBubbleMakeVisible` | `uint8` | Make comment bubble visible |
| `NodeComment` | `FString` | Comment string that is drawn on the node |
| `ReferenceObjCategory` | `FString` | ReferenceObjCategory that is drawn on the node |
| `ErrorType` | `int32` | Flag to store node specific compile errorwarning |
| `ErrorMsg` | `FString` | ErrorWarning description |
| `NodeGuid` | `FGuid` | GUID to uniquely identify this node, to facilitate diffing versions of this graph |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEdGraphNode_Documentation.json -->

# UEdGraphNode_Documentation

## Inheritance

`UEdGraphNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Link` | `FString` | Documentation Link |
| `Excerpt` | `FString` | Documentation Excerpt |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEdGraphPin_Deprecated.json -->

# UEdGraphPin_Deprecated

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PinName` | `FString` | Name of this pin |
| `PinToolTip` | `FString` | The tool-tip describing this pin's purpose |
| `Direction` | `TEnumAsByte < enum EEdGraphPinDirection >` | Direction of flow of this pin (input or output) |
| `PinType` | `FEdGraphPinType` | The type of information carried on this pin |
| `DefaultValue` | `FString` | Default value for this pin (used if the pin has no connections), stored as a string |
| `AutogeneratedDefaultValue` | `FString` | Initial default value (the autogenerated value, to identify if the user has modified the value), stored as a string |
| `DefaultObject` | `UObject *` | If the default value for this pin should be an object, we store a pointer to it |
| `DefaultTextValue` | `FText` | If the default value for this pin should be an FText, it is stored here. |
| `LinkedTo` | `TArray < UEdGraphPin_Deprecated * >` | Set of pins that we are linked to |
| `SubPins` | `TArray < UEdGraphPin_Deprecated * >` | The pins created when a pin is split and hidden |
| `ParentPin` | `UEdGraphPin_Deprecated *` | The pin that was split and generated this pin |
| `ReferencePassThroughConnection` | `UEdGraphPin_Deprecated *` | Pin that this pin uses for passing through reference connection |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQuery.json -->

# UEditableGameplayTagQuery

This is an editor-only representation of a query, designed to be editable with a typical property window.
  To edit a query in the editor, an FGameplayTagQuery is converted to a set of UObjects and edited,  When finished,
  the query struct is rewritten and these UObjects are discarded.
  This query representation is not intended for runtime use.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UserDescription` | `FString` | User-supplied description, shown in property details. Auto-generated description is shown if not supplied. |
| `RootExpression` | `UEditableGameplayTagQueryExpression *` | The base expression of this query. |
| `TagQueryExportText_Helper` | `FGameplayTagQuery` | Property to hold a gameplay tag query so we can use the exporttext path to get a string representation. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQueryExpression_AllExprMatch.json -->

# UEditableGameplayTagQueryExpression_AllExprMatch

## Inheritance

`UEditableGameplayTagQueryExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Expressions` | `TArray < UEditableGameplayTagQueryExpression * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQueryExpression_AllTagsMatch.json -->

# UEditableGameplayTagQueryExpression_AllTagsMatch

## Inheritance

`UEditableGameplayTagQueryExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Tags` | `FGameplayTagContainer` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQueryExpression_AnyExprMatch.json -->

# UEditableGameplayTagQueryExpression_AnyExprMatch

## Inheritance

`UEditableGameplayTagQueryExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Expressions` | `TArray < UEditableGameplayTagQueryExpression * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQueryExpression_AnyTagsMatch.json -->

# UEditableGameplayTagQueryExpression_AnyTagsMatch

## Inheritance

`UEditableGameplayTagQueryExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Tags` | `FGameplayTagContainer` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQueryExpression_NoExprMatch.json -->

# UEditableGameplayTagQueryExpression_NoExprMatch

## Inheritance

`UEditableGameplayTagQueryExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Expressions` | `TArray < UEditableGameplayTagQueryExpression * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableGameplayTagQueryExpression_NoTagsMatch.json -->

# UEditableGameplayTagQueryExpression_NoTagsMatch

## Inheritance

`UEditableGameplayTagQueryExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Tags` | `FGameplayTagContainer` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableText.json -->

# UEditableText

Editable text box widget

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `WidgetStyle` | `FEditableTextStyle` | The style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | Text style |
| `BackgroundImageSelected_DEPRECATED` | `USlateBrushAsset *` | Background image for the selected text (overrides Style) |
| `BackgroundImageComposing_DEPRECATED` | `USlateBrushAsset *` | Background image for the composing text (overrides Style) |
| `CaretImage_DEPRECATED` | `USlateBrushAsset *` | Image brush used for the caret (overrides Style) |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `ColorAndOpacity_DEPRECATED` | `FSlateColor` | Text color and opacity (overrides Style) |
| `IsReadOnly` | `bool` | Sets whether this text box can actually be modified interactively by the user |
| `IsPassword` | `bool` | Sets whether this text box is for storing a password |
| `MinimumDesiredWidth` | `float` | Minimum width that a text block should be |
| `IsCaretMovedWhenGainFocus` | `bool` | Workaround as we lose focus when the auto completion closes. |
| `SelectAllTextWhenFocused` | `bool` | Whether to select all text when the user clicks to give focus on the widget |
| `RevertTextOnEscape` | `bool` | Whether to allow the user to back out of changes when they press the escape key |
| `ClearKeyboardFocusOnCommit` | `bool` | Whether to clear keyboard focus when pressing enter to commit changes |
| `SelectAllTextOnCommit` | `bool` | Whether to select all text when pressing enter to commit changes |
| `AllowContextMenu` | `bool` | Whether the context menu can be opened |
| `KeyboardType` | `TEnumAsByte < EVirtualKeyboardType :: Type >` | If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use? |
| `ShapedTextOptions` | `FShapedTextOptions` | Controls how the text within this widget should be shaped. |

## Functions

### `GetText`

```text
GetText() -> FText
```

Gets the widget text

**Returns**

| Type | Description |
|---|---|
| `FText` | The widget text |

### `SetText`

```text
SetText(InText: FText) -> void
```

Directly sets the widget text.
	  Warning: This will wipe any binding created for the Text property!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | The text to assign to the widget |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsPassword`

```text
SetIsPassword(InbIsPassword: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbIsPassword` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHintText`

```text
SetHintText(InHintText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHintText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsReadOnly`

```text
SetIsReadOnly(InbIsReadyOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbIsReadyOnly` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFont`

```text
SetFont(Font: FSlateFontInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Font` | `FSlateFontInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(Color: FSlateColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Color` | `FSlateColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnTextChanged`

```text
OnTextChanged(Text: const FText&) -> void
```

Called whenever the text is changed interactively by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextCommitted`

```text
OnTextCommitted(Text: const FText&, CommitMethod: ETextCommit::Type) -> void
```

Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |
| `CommitMethod` | `ETextCommit::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextBeginEditTransation`

```text
OnTextBeginEditTransation() -> void
```

Called to begin an undoable editable text transaction

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextEndEditTransaction`

```text
OnTextEndEditTransaction(Text: const FText&) -> void
```

Called to end an undoable editable text transaction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextFocusReceived`

```text
OnTextFocusReceived() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableTextBox.json -->

# UEditableTextBox

Allows the user to type in custom text.  Only permits a single line of text to be entered.
  
   No Children
   Text Entry

## Inheritance

`UWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text content for this editable text box widget |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `WidgetStyle` | `FEditableTextBoxStyle` | The style |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | Style used for the text box |
| `HintText` | `FText` | Hint text that appears when there is no text in the text box |
| `HintTextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the hint text of the widget |
| `Font_DEPRECATED` | `FSlateFontInfo` | Font color and opacity (overrides Style) |
| `ForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity (overrides Style) |
| `BackgroundColor_DEPRECATED` | `FLinearColor` | The color of the backgroundborder around the editable text (overrides Style) |
| `ReadOnlyForegroundColor_DEPRECATED` | `FLinearColor` | Text color and opacity when read-only (overrides Style) |
| `IsReadOnly` | `bool` | Sets whether this text box can actually be modified interactively by the user |
| `IsPassword` | `bool` | Sets whether this text box is for storing a password |
| `MinimumDesiredWidth` | `float` | Minimum width that a text block should be |
| `Padding_DEPRECATED` | `FMargin` | Padding between the boxborder and the text widget inside (overrides Style) |
| `IsCaretMovedWhenGainFocus` | `bool` | Workaround as we lose focus when the auto completion closes. |
| `SelectAllTextWhenFocused` | `bool` | Whether to select all text when the user clicks to give focus on the widget |
| `RevertTextOnEscape` | `bool` | Whether to allow the user to back out of changes when they press the escape key |
| `ClearKeyboardFocusOnCommit` | `bool` | Whether to clear keyboard focus when pressing enter to commit changes |
| `SelectAllTextOnCommit` | `bool` | Whether to select all text when pressing enter to commit changes |
| `AllowContextMenu` | `bool` | Whether the context menu can be opened |
| `KeyboardType` | `TEnumAsByte < EVirtualKeyboardType :: Type >` | If we're on a platform that requires a virtual keyboard, what kind of keyboard should this widget use? |
| `ShapedTextOptions` | `FShapedTextOptions` | Controls how the text within this widget should be shaped. |

## Functions

### `GetText`

```text
GetText() -> FText
```

Provide a alternative mechanism for error reporting.

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `SetText`

```text
SetText(InText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHintText`

```text
SetHintText(InText: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetError`

```text
SetError(InError: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InError` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsReadOnly`

```text
SetIsReadOnly(bReadOnly: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bReadOnly` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearError`

```text
ClearError() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasError`

```text
HasError() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnTextChanged`

```text
OnTextChanged(Text: const FText&) -> void
```

Called whenever the text is changed interactively by the user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTextCommitted`

```text
OnTextCommitted(Text: const FText&, CommitMethod: ETextCommit::Type) -> void
```

Called whenever the text is committed.  This happens when the user presses enter or the text box loses focus.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `const FText&` | - |
| `CommitMethod` | `ETextCommit::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableTextBoxWidgetStyle.json -->

# UEditableTextBoxWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EditableTextBoxStyle` | `FEditableTextBoxStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEditableTextWidgetStyle.json -->

# UEditableTextWidgetStyle

## Inheritance

`USlateWidgetStyleContainerBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EditableTextStyle` | `FEditableTextStyle` | The actual data describing the button's appearance. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEndUserSettings.json -->

# UEndUserSettings

## Inheritance

`UObject` -> `IImportantToggleSettingInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bSendAnonymousUsageDataToEpic` | `bool` | Determines whether the engine sends anonymous usage information about game sessions to Epic Games in order to improve Unreal Engine. Information will never be shared with 3rd parties. |
| `bSendMeanTimeBetweenFailureDataToEpic` | `bool` | Determines whether the engine sends anonymous crashabnormal-shutdown data about game sessions to Epic Games in order to improve Unreal Engine. Information will never be shared with 3rd parties. |
| `bAllowUserIdInUsageData` | `bool` | If enabled, adds user identifying data to the otherwise anonymous reports sent to Epic Games. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEngine.json -->

# UEngine

Abstract base class of all Engine classes, responsible for management of systems critical to editor or game systems.
  Also defines default classes for certain engine systems.

## Inheritance

`UObject` -> `FExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TinyFont` | `UFont *` | - |
| `TinyFontName` | `FSoftObjectPath` | @todo document |
| `SmallFont` | `UFont *` | @todo document |
| `SmallFontName` | `FSoftObjectPath` | @todo document |
| `MediumFont` | `UFont *` | @todo document |
| `MediumFontName` | `FSoftObjectPath` | @todo document |
| `LargeFont` | `UFont *` | @todo document |
| `LargeFontName` | `FSoftObjectPath` | @todo document |
| `SubtitleFont` | `UFont *` | @todo document |
| `SubtitleFontName` | `FSoftObjectPath` | @todo document |
| `AdditionalFonts` | `TArray < UFont * >` | Any additional fonts that script may use without hard-referencing the font. |
| `AdditionalFontNames` | `TArray < FString >` | @todo document |
| `ConsoleClass` | `TSubclassOf < UConsole >` | The class to use for the game console. |
| `ConsoleClassName` | `FSoftClassPath` | @todo document |
| `GameViewportClientClass` | `TSubclassOf < UGameViewportClient >` | The class to use for the game viewport client. |
| `GameViewportClientClassName` | `FSoftClassPath` | @todo document |
| `LocalPlayerClass` | `TSubclassOf < ULocalPlayer >` | The class to use for local players. |
| `LocalPlayerClassName` | `FSoftClassPath` | @todo document |
| `WorldSettingsClass` | `TSubclassOf < AWorldSettings >` | The class for WorldSettings |
| `WorldSettingsClassName` | `FSoftClassPath` | @todo document |
| `NavigationSystemClassName` | `FSoftClassPath` | @todo document |
| `NavigationSystemClass` | `TSubclassOf < UNavigationSystem >` | The class for NavigationSystem |
| `AvoidanceManagerClassName` | `FSoftClassPath` | Name of behavior tree manager class |
| `AvoidanceManagerClass` | `TSubclassOf < UAvoidanceManager >` | The class for behavior tree manager |
| `PhysicsCollisionHandlerClass` | `TSubclassOf < UPhysicsCollisionHandler >` | PhysicsCollisionHandler class we should use by default |
| `PhysicsCollisionHandlerClassName` | `FSoftClassPath` | Name of PhysicsCollisionHandler class we should use by default. |
| `GameUserSettingsClassName` | `FSoftClassPath` | - |
| `GameUserSettingsClass` | `TSubclassOf < UGameUserSettings >` | - |
| `AIControllerClassName` | `FSoftClassPath` | name of Controller class to be used as default AIController class for pawns |
| `GameUserSettings` | `UGameUserSettings *` | Global instance of the user game settings |
| `LevelScriptActorClass` | `TSubclassOf < ALevelScriptActor >` | @todo document |
| `LevelScriptActorClassName` | `FSoftClassPath` | @todo document |
| `DefaultBlueprintBaseClassName` | `FSoftClassPath` | Name of the base class to use for new blueprints, configurable on a per-game basis |
| `GameSingletonClassName` | `FSoftClassPath` | Name of a singleton class to create at startup time, configurable per game |
| `GameSingleton` | `UObject *` | A UObject spawned at initialization time to handle game-specific data |
| `AssetManagerClassName` | `FSoftClassPath` | Name of a singleton class to spawn as the AssetManager, configurable per game. If empty, it will not spawn one |
| `AssetManager` | `UAssetManager *` | A UObject spawned at initialization time to handle game-specific data |
| `DefaultTexture` | `UTexture2D *` | A global default texture. |
| `DefaultTextureName` | `FSoftObjectPath` | @todo document |
| `DefaultDiffuseTexture` | `UTexture *` | A global default diffuse texture. |
| `DefaultDiffuseTextureName` | `FSoftObjectPath` | @todo document |
| `DefaultTextureArray` | `UTexture2DArray *` | A global default texture array. |
| `DefaultBSPVertexTexture` | `UTexture2D *` | @todo document |
| `DefaultBSPVertexTextureName` | `FSoftObjectPath` | @todo document |
| `HighFrequencyNoiseTexture` | `UTexture2D *` | Texture used to get random image grain values for post processing |
| `HighFrequencyNoiseTextureName` | `FSoftObjectPath` | @todo document |
| `DefaultBokehTexture` | `UTexture2D *` | Texture used to blur out of focus content, mimics the Bokeh shape of actual cameras |
| `DefaultBokehTextureName` | `FSoftObjectPath` | @todo document |
| `DefaultBloomKernelTexture` | `UTexture2D *` | Texture used to bloom when using FFT, mimics characteristic bloom produced in a camera from a signle bright source |
| `DefaultBloomKernelTextureName` | `FSoftObjectPath` | @todo document |
| `WireframeMaterial` | `UMaterial *` | The material used to render wireframe meshes. |
| `WireframeMaterialName` | `FString` | @todo document |
| `DebugMeshMaterial` | `UMaterial *` | A material used to render debug meshes. |
| `DebugMeshMaterialName` | `FSoftObjectPath` | @todo document |
| `LevelColorationLitMaterial` | `UMaterial *` | Material used for visualizing level membership in lit view port modes. |
| `LevelColorationLitMaterialName` | `FString` | @todo document |
| `LevelColorationUnlitMaterial` | `UMaterial *` | Material used for visualizing level membership in unlit view port modes. |
| `LevelColorationUnlitMaterialName` | `FString` | @todo document |
| `LightingTexelDensityMaterial` | `UMaterial *` | Material used for visualizing lighting only w lightmap texel density. |
| `LightingTexelDensityName` | `FString` | @todo document |
| `ShadedLevelColorationLitMaterial` | `UMaterial *` | Material used for visualizing level membership in lit view port modes. Uses shading to show axis directions. |
| `ShadedLevelColorationLitMaterialName` | `FString` | @todo document |
| `ShadedLevelColorationUnlitMaterial` | `UMaterial *` | Material used for visualizing level membership in unlit view port modes.  Uses shading to show axis directions. |
| `ShadedLevelColorationUnlitMaterialName` | `FString` | @todo document |
| `NewShadedLevelColorationUnlitMaterial` | `UMaterial *` | Material used for visualizing level membership in unlit view port modes.  Uses shading to show axis directions. |
| `NewShadedLevelColorationUnlitMaterialName` | `FString` | @todo document |
| `RemoveSurfaceMaterial` | `UMaterial *` | Material used to indicate that the associated BSP surface should be removed. |
| `RemoveSurfaceMaterialName` | `FSoftObjectPath` | @todo document |
| `VertexColorMaterial` | `UMaterial *` | Material that renders vertex color as emmissive. |
| `VertexColorMaterialName` | `FString` | @todo document |
| `VertexColorViewModeMaterial_ColorOnly` | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (color only, no alpha) |
| `VertexColorViewModeMaterialName_ColorOnly` | `FString` | @todo document |
| `VertexColorViewModeMaterial_AlphaAsColor` | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (alpha channel as color) |
| `VertexColorViewModeMaterialName_AlphaAsColor` | `FString` | @todo document |
| `VertexColorViewModeMaterial_RedOnly` | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (red only) |
| `VertexColorViewModeMaterialName_RedOnly` | `FString` | @todo document |
| `VertexColorViewModeMaterial_GreenOnly` | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (green only) |
| `VertexColorViewModeMaterialName_GreenOnly` | `FString` | @todo document |
| `VertexColorViewModeMaterial_BlueOnly` | `UMaterial *` | Material for visualizing vertex colors on meshes in the scene (blue only) |
| `VertexColorViewModeMaterialName_BlueOnly` | `FString` | @todo document |
| `DebugEditorMaterialName` | `FSoftObjectPath` | A material used to render debug opaque material. Used in various animation editor viewport features. |
| `ConstraintLimitMaterial` | `UMaterial *` | Material used to render constraint limits |
| `ConstraintLimitMaterialX` | `UMaterialInstanceDynamic *` | - |
| `ConstraintLimitMaterialXAxis` | `UMaterialInstanceDynamic *` | - |
| `ConstraintLimitMaterialY` | `UMaterialInstanceDynamic *` | - |
| `ConstraintLimitMaterialYAxis` | `UMaterialInstanceDynamic *` | - |
| `ConstraintLimitMaterialZ` | `UMaterialInstanceDynamic *` | - |
| `ConstraintLimitMaterialZAxis` | `UMaterialInstanceDynamic *` | - |
| `ConstraintLimitMaterialPrismatic` | `UMaterialInstanceDynamic *` | - |
| `InvalidLightmapSettingsMaterial` | `UMaterial *` | Material that renders a message about lightmap settings being invalid. |
| `InvalidLightmapSettingsMaterialName` | `FSoftObjectPath` | @todo document |
| `PreviewShadowsIndicatorMaterial` | `UMaterial *` | Material that renders a message about preview shadows being used. |
| `PreviewShadowsIndicatorMaterialName` | `FSoftObjectPath` | @todo document |
| `ArrowMaterial` | `UMaterial *` | Material that 'fakes' lighting, used for arrows, widgets. |
| `ArrowMaterialName` | `FSoftObjectPath` | @todo document |
| `OutlineMaterial` | `UMaterial *` | Material IdeaOutline. |
| `OutlineMaterialName` | `FSoftObjectPath` | @todo document |
| `OutlineMaskedMaterial` | `UMaterial *` | - |
| `OutlineMaskedMaterialName` | `FSoftObjectPath` | - |
| `OutlineMaterialNewOpaque` | `UMaterial *` | - |
| `OutlineMaterialNewOpaqueName` | `FSoftObjectPath` | - |
| `OutlineMaterialNewTranslucent` | `UMaterial *` | - |
| `OutlineMaterialNewTranslucentName` | `FSoftObjectPath` | - |
| `OutlineMaskedMaterialNewOpaque` | `UMaterial *` | - |
| `OutlineMaskedMaterialNewOpaqueName` | `FSoftObjectPath` | - |
| `OutlineMaskedMaterialNewTranslucent` | `UMaterial *` | - |
| `OutlineMaskedMaterialNewTranslucentName` | `FSoftObjectPath` | - |
| `HighlightMaterial` | `UMaterial *` | - |
| `HighlightMaterialName` | `FSoftObjectPath` | - |
| `SmaaAreaTexName` | `FSoftObjectPath` | SMAA AreaTex name |
| `SmaaSearchTexName` | `FSoftObjectPath` | SMAA SearchTex name |
| `SmaaAreaTex` | `UTexture2D *` | SMAA AreaTex |
| `SmaaSearchTex` | `UTexture2D *` | SMAA SearchTex |
| `DyeingColorMaterial` | `UMaterial *` | Material IdeaOutline. |
| `DyeingColorMaterialName` | `FSoftObjectPath` | @todo document |
| `LightingOnlyBrightness` | `FLinearColor` | @todo document |
| `ShaderComplexityColors` | `TArray < FLinearColor >` | The colors used to render shader complexity. |
| `QuadComplexityColors` | `TArray < FLinearColor >` | The colors used to render quad complexity. |
| `LightComplexityColors` | `TArray < FLinearColor >` | The colors used to render light complexity. |
| `StationaryLightOverlapColors` | `TArray < FLinearColor >` | The colors used to render stationary light overlap. |
| `LODColorationColors` | `TArray < FLinearColor >` | The colors used to render LOD coloration. |
| `HLODColorationColors` | `TArray < FLinearColor >` | The colors used to render LOD coloration. |
| `LightmapColorationColors` | `TArray < FLinearColor >` | The colors used to render Lightmap type coloration. |
| `StreamingAccuracyColors` | `TArray < FLinearColor >` | The colors used for texture streaming accuracy debug view modes. |
| `DesiredTexelDensity` | `int32` | - |
| `TexelDensityTextureSuffixList` | `TArray < FString >` | - |
| `TexelDensityAccuracyColors` | `TArray < FLinearColor >` | - |
| `MaxPixelShaderAdditiveComplexityCount` | `float` | Complexity limits for the various complexity view mode combinations.<br>	 These limits are used to map instruction counts to ShaderComplexityColors. |
| `MaxES2PixelShaderAdditiveComplexityCount` | `float` | - |
| `MinLightMapDensity` | `float` | Range for the lightmap density view mode. <br>	 Minimum lightmap density value for coloring. |
| `IdealLightMapDensity` | `float` | Ideal lightmap density value for coloring. |
| `MaxLightMapDensity` | `float` | Maximum lightmap density value for coloring. |
| `bRenderLightMapDensityGrayscale` | `uint32` | If true, then render gray scale density. |
| `RenderLightMapDensityGrayscaleScale` | `float` | The scale factor when rendering gray scale density. |
| `RenderLightMapDensityColorScale` | `float` | The scale factor when rendering color density. |
| `LightMapDensityVertexMappedColor` | `FLinearColor` | The color to render vertex mapped objects in for LightMap Density view mode. |
| `LightMapDensitySelectedColor` | `FLinearColor` | The color to render selected objects in for LightMap Density view mode. |
| `StatColorMappings` | `TArray < FStatColorMapping >` | @todo document |
| `DefaultPhysMaterial` | `UPhysicalMaterial *` | PhysicalMaterial to use if none is defined for a particular object. |
| `DefaultPhysMaterialName` | `FSoftObjectPath` | @todo document |
| `ActiveGameNameRedirects` | `TArray < FGameNameRedirect >` | - |
| `ActiveClassRedirects` | `TArray < FClassRedirect >` | - |
| `ActivePluginRedirects` | `TArray < FPluginRedirect >` | - |
| `ActiveStructRedirects` | `TArray < FStructRedirect >` | - |
| `PreIntegratedSkinBRDFTexture` | `UTexture2D *` | Texture used for pre-integrated skin shading |
| `PreIntegratedSkinBRDFTextureName` | `FSoftObjectPath` | @todo document |
| `MiniFontTexture` | `UTexture2D *` | Texture used to do font rendering in shaders |
| `MiniFontTextureName` | `FSoftObjectPath` | @todo document |
| `WeightMapPlaceholderTexture` | `UTexture *` | Texture used as a placeholder for terrain weight-maps to give the material the correct texture format. |
| `WeightMapPlaceholderTextureName` | `FSoftObjectPath` | @todo document |
| `LightMapDensityTexture` | `UTexture2D *` | Texture used to display LightMapDensity |
| `LightMapDensityTextureName` | `FSoftObjectPath` | @todo document |
| `GameViewport` | `UGameViewportClient *` | The view port representing the current game instance. Can be 0 so don't use without checking. |
| `DeferredCommands` | `TArray < FString >` | Array of deferred command strings execs that get executed at the end of the frame |
| `TickCycles` | `int32` | @todo document |
| `GameCycles` | `int32` | @todo document |
| `ClientCycles` | `int32` | @todo document |
| `NearClipPlane` | `float` | The distance of the camera's near clipping plane. |
| `bHardwareSurveyEnabled_DEPRECATED` | `uint32` | DEPRECATED - Can a runtime gameapplication report anonymous hardware survey statistics (such as display resolution and GPU model) back to Epic? |
| `bSubtitlesEnabled` | `uint32` | Flag for completely disabling subtitles for localized sounds. |
| `bSubtitlesForcedOff` | `uint32` | Flag for forcibly disabling subtitles even if you try to turn them back on they will be off |
| `MaximumLoopIterationCount` | `int32` | Script maximum loop iteration count used as a threshold to warn users about script execution runaway |
| `bCanBlueprintsTickByDefault` | `uint32` | - |
| `bOptimizeAnimBlueprintMemberVariableAccess` | `uint32` | Controls whether anim blueprint nodes that access member variables of their class directly should use the optimized path that avoids a thunk to the Blueprint VM. This will force all anim blueprints to be recompiled. |
| `bAllowMultiThreadedAnimationUpdate` | `uint32` | Controls whether by default we allow anim blueprint graph updates to be performed on non-game threads. This enables some extra checks in the anim blueprint compiler that will warn when unsafe operations are being attempted. This will force all anim blueprints to be recompiled. |
| `bEnableEditorPSysRealtimeLOD` | `uint32` | @todo document |
| `bSmoothFrameRate` | `uint32` | Whether to enable framerate smoothing. |
| `bUseFixedFrameRate` | `uint32` | Whether to use a fixed framerate. |
| `FixedFrameRate` | `float` | The fixed framerate to use. |
| `SmoothedFrameRateRange` | `FFloatRange` | Range of framerates in which smoothing will kick in |
| `bCheckForMultiplePawnsSpawnedInAFrame` | `uint32` | Whether we should check for more than N pawns spawning in a single frame.<br>	  Basically, spawning pawns and all of their attachments can be slow.  And on consoles it<br>	  can be really slow.  If this bool is true we will display a |
| `NumPawnsAllowedToBeSpawnedInAFrame` | `int32` | If bCheckForMultiplePawnsSpawnedInAFrame==true, then we will check to see that no more than this number of pawns are spawned in a frame. |
| `bShouldGenerateLowQualityLightmaps_DEPRECATED` | `uint32` | Whether or not the LQ lightmaps should be generated during lighting rebuilds.  This has been moved to r.SupportLowQualityLightmaps. |
| `C_WorldBox` | `FColor` | - |
| `C_BrushWire` | `FColor` | @todo document |
| `C_AddWire` | `FColor` | @todo document |
| `C_SubtractWire` | `FColor` | @todo document |
| `C_SemiSolidWire` | `FColor` | @todo document |
| `C_NonSolidWire` | `FColor` | @todo document |
| `C_WireBackground` | `FColor` | @todo document |
| `C_ScaleBoxHi` | `FColor` | @todo document |
| `C_VolumeCollision` | `FColor` | @todo document |
| `C_BSPCollision` | `FColor` | @todo document |
| `C_OrthoBackground` | `FColor` | @todo document |
| `C_Volume` | `FColor` | @todo document |
| `C_BrushShape` | `FColor` | @todo document |
| `StreamingDistanceFactor` | `float` | Fudge factor for tweaking the distance based miplevel determination |
| `GameScreenshotSaveDirectory` | `FDirectoryPath` | The save directory for newly created screenshots |
| `TransitionType` | `TEnumAsByte < enum ETransitionType >` | The current transition type. |
| `TransitionDescription` | `FString` | The current transition description text. |
| `TransitionGameMode` | `FString` | The gamemode for the destination map |
| `MeshLODRange` | `float` | Level of detail range control for meshes |
| `bAllowMatureLanguage` | `uint32` | whether mature language is allowed |
| `CameraRotationThreshold` | `float` | camera rotation (deg) beyond which occlusion queries are ignored from previous frame (because they are likely not valid) |
| `CameraTranslationThreshold` | `float` | camera movement beyond which occlusion queries are ignored from previous frame (because they are likely not valid) |
| `PrimitiveProbablyVisibleTime` | `float` | The amount of time a primitive is considered to be probably visible after it was last actually visible. |
| `MaxOcclusionPixelsFraction` | `float` | Max screen pixel fraction where retesting when unoccluded is worth the GPU time. |
| `bPauseOnLossOfFocus` | `uint32` | Whether to pause the game if focus is lost. |
| `MaxParticleResize` | `int32` | The maximum allowed size to a ParticleEmitterInstance::Resize call.<br>	 	If larger, the function will return without resizing. |
| `MaxParticleResizeWarn` | `int32` | If the resize request is larger than this, spew out a warning to the log |
| `PendingDroppedNotes` | `TArray < FDropNoteInfo >` | @todo document |
| `PhysicErrorCorrection` | `FRigidBodyErrorCorrection` | Error correction data for replicating simulated physics (rigid bodies) |
| `NetClientTicksPerSecond` | `float` | Number of times to tick each client per second |
| `DisplayGamma` | `float` | Current display gamma setting |
| `MinDesiredFrameRate` | `float` | Minimum desired framerate setting |
| `ShaderPrecompileProgress` | `int32` | - |
| `DefaultSelectedMaterialColor` | `FLinearColor` | Default color of selected objects in the level viewport (additive) |
| `SelectedMaterialColor` | `FLinearColor` | Color of selected objects in the level viewport (additive) |
| `SelectionOutlineColor` | `FLinearColor` | Color of the selection outline color.  Generally the same as selected material color unless the selection material color is being overridden |
| `SubduedSelectionOutlineColor` | `FLinearColor` | Subdued version of the selection outline color. Used for indicating sub-selection of components vs actors |
| `SelectedMaterialColorOverride` | `FLinearColor` | An override to use in some cases instead of the selected material color |
| `bIsOverridingSelectedColor` | `bool` | Whether or not selection color is being overridden |
| `bEnableOnScreenDebugMessages` | `uint32` | If true, then disable OnScreenDebug messages. Can be toggled in real-time. |
| `bEnableOnScreenDebugMessagesDisplay` | `uint32` | If true, then disable the display of OnScreenDebug messages (used when running) |
| `bSuppressMapWarnings` | `uint32` | If true, then skip drawing map warnings on screen even in non (UE_BUILD_SHIPPING \|\| UE_BUILD_TEST) builds |
| `bDisableAILogging` | `uint32` | determines whether AI logging should be processed or not |
| `bEnableVisualLogRecordingOnStart` | `uint32` | - |
| `BlueNoiseScalarTexture` | `UTexture2D *` | Tiled blue-noise texture |
| `BlueNoiseVec2Texture` | `UTexture2D *` | Spatial-temporal blue noise texture with two channel output |
| `BlueNoiseScalarTextureName` | `FSoftObjectPath` | Path of the tiled blue-noise texture |
| `BlueNoiseVec2TextureName` | `FSoftObjectPath` | Path of the tiled blue-noise texture |
| `ScreenSaverInhibitorSemaphore` | `int32` | Semaphore to control screen saver inhibitor thread access. |
| `bLockReadOnlyLevels` | `uint32` | true if the the user cannot modify levels that are read only. |
| `ParticleEventManagerClassPath` | `FString` | Particle event manager |
| `SelectionHighlightIntensity` | `float` | Used to alter the intensity level of the selection highlight on selected objects |
| `SelectionMeshSectionHighlightIntensity` | `float` | Used to alter the intensity level of the selection highlight on selected mesh sections in mesh editors |
| `BSPSelectionHighlightIntensity` | `float` | Used to alter the intensity level of the selection highlight on selected BSP surfaces |
| `HoverHighlightIntensity` | `float` | Used to alter the intensity level of the selection highlight on hovered objects |
| `SelectionHighlightIntensityBillboards` | `float` | Used to alter the intensity level of the selection highlight on selected billboard objects |
| `NetDriverDefinitions` | `TArray < FNetDriverDefinition >` | A list of named UNetDriver definitions |
| `ServerActors` | `TArray < FString >` | A configurable list of actors that are automatically spawned upon server startup (just prior to InitGame) |
| `RuntimeServerActors` | `TArray < FString >` | Runtime-modified list of server actors, allowing plugins to use serveractors, without permanently adding them to config files |
| `bStartedLoadMapMovie` | `uint32` | true if the loading movie was started during LoadMap(). |
| `NextWorldContextHandle` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEngineMessage.json -->

# UEngineMessage

## Inheritance

`ULocalMessage`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FailedPlaceMessage` | `FString` | Message displayed in message dialog when player pawn fails to spawn because no playerstart was available. |
| `MaxedOutMessage` | `FString` | Message when player join attempt is refused because the server is at capacity. |
| `EnteredMessage` | `FString` | Message when a new player enters the game. |
| `LeftMessage` | `FString` | Message when a player leaves the game. |
| `GlobalNameChange` | `FString` | Message when a player changes his name. |
| `SpecEnteredMessage` | `FString` | Message when a new spectator enters the server (if spectator has a player name). |
| `NewPlayerMessage` | `FString` | Message when a new player enters the server (if player is unnamed). |
| `NewSpecMessage` | `FString` | Message when a new spectator enters the server (if spectator is unnamed). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQuery.json -->

# UEnvQuery

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryName` | `FName` | - |
| `Options` | `TArray < UEnvQueryOption * >` | - |
| `EdGraph` | `UEdGraph *` | Graph for query |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryContext_BlueprintBase.json -->

# UEnvQueryContext_BlueprintBase

## Inheritance

`UEnvQueryContext`

## Functions

### `ProvideSingleActor`

```text
ProvideSingleActor(QuerierObject: UObject *, QuerierActor: AActor *, ResultingActor: AActor * &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingActor` | `AActor * &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProvideSingleLocation`

```text
ProvideSingleLocation(QuerierObject: UObject *, QuerierActor: AActor *, ResultingLocation: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProvideActorsSet`

```text
ProvideActorsSet(QuerierObject: UObject *, QuerierActor: AActor *, ResultingActorsSet: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingActorsSet` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProvideLocationsSet`

```text
ProvideLocationsSet(QuerierObject: UObject *, QuerierActor: AActor *, ResultingLocationSet: TArray < FVector > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingLocationSet` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator.json -->

# UEnvQueryGenerator

## Inheritance

`UEnvQueryNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OptionName` | `FString` | - |
| `ItemType` | `TSubclassOf < UEnvQueryItemType >` | type of generated items |
| `bAutoSortTests` | `uint32` | if set, tests will be automatically sorted for best performance before running query |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_ActorsOfClass.json -->

# UEnvQueryGenerator_ActorsOfClass

## Inheritance

`UEnvQueryGenerator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SearchedActorClass` | `TSubclassOf < AActor >` | - |
| `GenerateOnlyActorsInRadius` | `FAIDataProviderBoolValue` | If true, this will only returns actors of the specified class within the SearchRadius of the SearchCenter context.  If false, it will return ALL actors of the specified class in the world. |
| `SearchRadius` | `FAIDataProviderFloatValue` | Max distance of path between point and context.  NOTE: Zero and negative values will never return any results if<br>	   UseRadius is true.  "Within" requires Distance < Radius.  Actors ON the circle (Distance == Radius) are excluded. |
| `SearchCenter` | `TSubclassOf < UEnvQueryContext >` | context |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_BlueprintBase.json -->

# UEnvQueryGenerator_BlueprintBase

## Inheritance

`UEnvQueryGenerator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GeneratorsActionDescription` | `FText` | A short description of what test does, like "Generate pawn named Joe" |
| `Context` | `TSubclassOf < UEnvQueryContext >` | context |
| `GeneratedItemType` | `TSubclassOf < UEnvQueryItemType >` | @todo this should show up only in the generator's BP, but <br>	 	due to the way EQS editor is generating widgets it's there as well<br>	 	It's a bug and we'll fix it |

## Functions

### `DoItemGeneration`

```text
DoItemGeneration(ContextLocations: TArray < FVector > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ContextLocations` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddGeneratedVector`

```text
AddGeneratedVector(GeneratedVector: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GeneratedVector` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddGeneratedActor`

```text
AddGeneratedActor(GeneratedActor: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GeneratedActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetQuerier`

```text
GetQuerier() -> UObject *
```

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_Composite.json -->

# UEnvQueryGenerator_Composite

Composite generator allows using multiple generators in single query option
  All child generators must produce exactly the same item type!

## Inheritance

`UEnvQueryGenerator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Generators` | `TArray < UEnvQueryGenerator * >` | - |
| `bAllowDifferentItemTypes` | `uint32` | allow generators with different item types, use at own risk!<br>	 <br>	   WARNING: <br>	   generator will use ForcedItemType for raw data, you MUST ensure proper memory layout<br>	   child generators will be writing to memory block through their own item types:<br>	   - data must fit info block allocated by ForcedItemType<br>	   - tests will read item locationproperties through ForcedItemType |
| `bHasMatchingItemType` | `uint32` | - |
| `ForcedItemType` | `TSubclassOf < UEnvQueryItemType >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_Cone.json -->

# UEnvQueryGenerator_Cone

## Inheritance

`UEnvQueryGenerator_ProjectedPoints`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AlignedPointsDistance` | `FAIDataProviderFloatValue` | Distance between each point of the same angle |
| `ConeDegrees` | `FAIDataProviderFloatValue` | Maximum degrees of the generated cone |
| `AngleStep` | `FAIDataProviderFloatValue` | The step of the angle increase. Angle step must be >=1<br>	   Smaller values generate less items |
| `Range` | `FAIDataProviderFloatValue` | Generation distance |
| `CenterActor` | `TSubclassOf < UEnvQueryContext >` | The actor (or actors) that will generate a cone in their facing direction |
| `bIncludeContextLocation` | `uint8` | Whether to include CenterActors' locations when generating items. <br>	 	Note that this option skips the MinAngledPointsDistance parameter. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_CurrentLocation.json -->

# UEnvQueryGenerator_CurrentLocation

## Inheritance

`UEnvQueryGenerator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryContext` | `TSubclassOf < UEnvQueryContext >` | context |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_Donut.json -->

# UEnvQueryGenerator_Donut

## Inheritance

`UEnvQueryGenerator_ProjectedPoints`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InnerRadius` | `FAIDataProviderFloatValue` | min distance between point and context |
| `OuterRadius` | `FAIDataProviderFloatValue` | max distance between point and context |
| `NumberOfRings` | `FAIDataProviderIntValue` | number of rings to generate |
| `PointsPerRing` | `FAIDataProviderIntValue` | number of items to generate for each ring |
| `ArcDirection` | `FEnvDirection` | If you generate items on a piece of circle you define direction of Arc cut here |
| `ArcAngle` | `FAIDataProviderFloatValue` | If you generate items on a piece of circle you define angle of Arc cut here |
| `bUseSpiralPattern` | `bool` | If true, the rings of the wheel will be rotated in a spiral pattern.  If false, they will all be at a zero<br>	   rotation, looking more like the spokes on a wheel. |
| `Center` | `TSubclassOf < UEnvQueryContext >` | context |
| `bDefineArc` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_OnCircle.json -->

# UEnvQueryGenerator_OnCircle

## Inheritance

`UEnvQueryGenerator_ProjectedPoints`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CircleRadius` | `FAIDataProviderFloatValue` | max distance of path between point and context |
| `SpaceBetween` | `FAIDataProviderFloatValue` | items will be generated on a circle this much apart |
| `NumberOfPoints` | `FAIDataProviderIntValue` | this many items will be generated on a circle |
| `PointOnCircleSpacingMethod` | `EPointOnCircleSpacingMethod` | how we are choosing where the points are in the circle |
| `ArcDirection` | `FEnvDirection` | If you generate items on a piece of circle you define direction of Arc cut here |
| `ArcAngle` | `FAIDataProviderFloatValue` | If you generate items on a piece of circle you define angle of Arc cut here |
| `AngleRadians` | `float` | - |
| `CircleCenter` | `TSubclassOf < UEnvQueryContext >` | context |
| `bIgnoreAnyContextActorsWhenGeneratingCircle` | `bool` | ignore tracing into context actors when generating the circle |
| `CircleCenterZOffset` | `FAIDataProviderFloatValue` | context offset |
| `TraceData` | `FEnvTraceData` | horizontal trace for nearest obstacle |
| `bDefineArc` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_PathingGrid.json -->

# UEnvQueryGenerator_PathingGrid

Navigation grid, generates points on navmesh
   with paths tofrom context no further than given limit

## Inheritance

`UEnvQueryGenerator_SimpleGrid`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PathToItem` | `FAIDataProviderBoolValue` | pathfinding direction |
| `NavigationFilter` | `TSubclassOf < UNavigationQueryFilter >` | navigation filter to use in pathfinding |
| `ScanRangeMultiplier` | `FAIDataProviderFloatValue` | multiplier for max distance between point and context |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_ProjectedPoints.json -->

# UEnvQueryGenerator_ProjectedPoints

## Inheritance

`UEnvQueryGenerator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProjectionData` | `FEnvTraceData` | trace params |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_SimpleGrid.json -->

# UEnvQueryGenerator_SimpleGrid

Simple grid, generates points in 2D square around context

## Inheritance

`UEnvQueryGenerator_ProjectedPoints`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GridSize` | `FAIDataProviderFloatValue` | half of square's extent, like a radius |
| `SpaceBetween` | `FAIDataProviderFloatValue` | generation density |
| `GenerateAround` | `TSubclassOf < UEnvQueryContext >` | context |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryInstanceBlueprintWrapper.json -->

# UEnvQueryInstanceBlueprintWrapper

## Inheritance

`UObject` -> `IEQSQueryResultSourceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryID` | `int32` | - |
| `ItemType` | `TSubclassOf < UEnvQueryItemType >` | - |
| `OptionIndex` | `int32` | index of query option, that generated items |

## Functions

### `GetItemScore`

```text
GetItemScore(ItemIndex: int32) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetResultsAsActors`

```text
GetResultsAsActors() -> TArray < AActor * >
```

return an array filled with resulting actors. Note that it makes sense only if ItemType is a EnvQueryItemType_ActorBase-derived type

**Returns**

| Type | Description |
|---|---|
| `TArray < AActor * >` | - |

### `GetResultsAsLocations`

```text
GetResultsAsLocations() -> TArray < FVector >
```

returns an array of locations generated by the query. If the query generated Actors the the array is filled with their locations

**Returns**

| Type | Description |
|---|---|
| `TArray < FVector >` | - |

### `SetNamedParam`

```text
SetNamedParam(ParamName: FName, Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParamName` | `FName` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnQueryFinishedEvent`

```text
OnQueryFinishedEvent(QueryInstance: UEnvQueryInstanceBlueprintWrapper*, QueryStatus: EEnvQueryStatus::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QueryInstance` | `UEnvQueryInstanceBlueprintWrapper*` | - |
| `QueryStatus` | `EEnvQueryStatus::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryManager.json -->

# UEnvQueryManager

## Inheritance

`UObject` -> `FTickableGameObject` -> `FSelfRegisteringExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceCache` | `TArray < FEnvQueryInstanceCache >` | cache of instances |
| `LocalContexts` | `TArray < UEnvQueryContext * >` | local cache of context objects for managing BP based objects |
| `GCShieldedWrappers` | `TArray < UEnvQueryInstanceBlueprintWrapper * >` | - |
| `MaxAllowedTestingTime` | `float` | how long are we allowed to test per update, in seconds. |
| `bTestQueriesUsingBreadth` | `bool` | whether we update EQS queries based on:<br>	    or test an entire query before moving to the next one (depth). |
| `QueryCountWarningThreshold` | `int32` | if greater than zero, we will warn once when the number of queries is greater than or equal to this number, and log the queries out |
| `QueryCountWarningInterval` | `double` | how often (in seconds) we will warn about the number of queries (allows us to catch multiple occurrences in a session) |

## Functions

### `RunEQSQuery`

```text
RunEQSQuery(WorldContextObject: UObject *, QueryTemplate: UEnvQuery *, Querier: UObject *, RunMode: TEnumAsByte < EEnvQueryRunMode :: Type >, WrapperClass: TSubclassOf < UEnvQueryInstanceBlueprintWrapper >) -> UEnvQueryInstanceBlueprintWrapper *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `QueryTemplate` | `UEnvQuery *` | - |
| `Querier` | `UObject *` | - |
| `RunMode` | `TEnumAsByte < EEnvQueryRunMode :: Type >` | - |
| `WrapperClass` | `TSubclassOf < UEnvQueryInstanceBlueprintWrapper >` | - |

**Returns**

| Type | Description |
|---|---|
| `UEnvQueryInstanceBlueprintWrapper *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryNode.json -->

# UEnvQueryNode

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `VerNum` | `int32` | Versioning for updating deprecated properties |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryOption.json -->

# UEnvQueryOption

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Generator` | `UEnvQueryGenerator *` | - |
| `Tests` | `TArray < UEnvQueryTest * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest.json -->

# UEnvQueryTest

## Inheritance

`UEnvQueryNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TestOrder` | `int32` | Number of test as defined in data asset |
| `TestPurpose` | `TEnumAsByte < EEnvTestPurpose :: Type >` | The purpose of this test.  Should it be used for filtering possible results, scoring them, or both? |
| `TestComment` | `FString` | Optional comment or explanation about what this test is for.  Useful when the purpose of tests may not be clear,<br>	   especially when there are multiple tests of the same type. |
| `MultipleContextFilterOp` | `TEnumAsByte < EEnvTestFilterOperator :: Type >` | Determines filtering operator when context returns multiple items |
| `MultipleContextScoreOp` | `TEnumAsByte < EEnvTestScoreOperator :: Type >` | Determines scoring operator when context returns multiple items |
| `FilterType` | `TEnumAsByte < EEnvTestFilterType :: Type >` | Does this test filter out results that are below a lower limit, above an upper limit, or both?  Or does it just look for a matching value? |
| `BoolValue` | `FAIDataProviderBoolValue` | Desired boolean value of the test for scoring to occur or filtering test to pass. |
| `FloatValueMin` | `FAIDataProviderFloatValue` | Minimum limit (inclusive) of valid values for the raw test value. Lower values will be discarded as invalid. |
| `FloatValueMax` | `FAIDataProviderFloatValue` | Maximum limit (inclusive) of valid values for the raw test value. Higher values will be discarded as invalid. |
| `ScoringEquation` | `TEnumAsByte < EEnvTestScoreEquation :: Type >` | The shape of the curve equation to apply to the normalized score before multiplying by factor. |
| `ClampMinType` | `TEnumAsByte < EEnvQueryTestClamping :: Type >` | How should the lower bound for normalization of the raw test value before applying the scoring formula be determined?<br>	    Should it use the lowest value found (tested), the lower threshold for filtering, or a separate specified normalization minimum? |
| `ClampMaxType` | `TEnumAsByte < EEnvQueryTestClamping :: Type >` | How should the upper bound for normalization of the raw test value before applying the scoring formula be determined?<br>	    Should it use the highest value found (tested), the upper threshold for filtering, or a separate specified normalization maximum? |
| `NormalizationType` | `EEQSNormalizationType` | Specifies how to determine value span used to normalize scores |
| `ScoreClampMin` | `FAIDataProviderFloatValue` | Minimum value to use to normalize the raw test value before applying scoring formula. |
| `ScoreClampMax` | `FAIDataProviderFloatValue` | Maximum value to use to normalize the raw test value before applying scoring formula. |
| `ScoringFactor` | `FAIDataProviderFloatValue` | The weight (factor) by which to multiply the normalized score after the scoring equation is applied. |
| `ReferenceValue` | `FAIDataProviderFloatValue` | When specified gets used to normalize test's results in such a way that the closer a value is to ReferenceValue<br>	 	the higher normalized result it will produce. Value farthest from ReferenceValue will be normalized<br>	 	to 0, and all the other values in between will get normalized linearly with the distance to ReferenceValue. |
| `bDefineReferenceValue` | `bool` | When set to true enables usage of ReferenceValue. It's false by default |
| `bWorkOnFloatValues` | `uint32` | When set, test operates on float values (e.g. distance, with AtLeast, UpTo conditions),<br>	   otherwise it will accept bool values (e.g. visibility, with Equals condition) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Distance.json -->

# UEnvQueryTest_Distance

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TestMode` | `TEnumAsByte < EEnvTestDistance :: Type >` | testing mode |
| `DistanceTo` | `TSubclassOf < UEnvQueryContext >` | context |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Dot.json -->

# UEnvQueryTest_Dot

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LineA` | `FEnvDirection` | defines direction of first line used by test |
| `LineB` | `FEnvDirection` | defines direction of second line used by test |
| `TestMode` | `EEnvTestDot` | - |
| `bAbsoluteValue` | `bool` | If true, this test uses the absolute value of the dot product rather than the dot product itself.  Useful<br>	   when you want to compare "how lateral" something is.  I.E. values closer to zero are further to the side, <br>	   and values closer to 1 are more in front or behind (without distinguishing forwardbackward). |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_GameplayTags.json -->

# UEnvQueryTest_GameplayTags

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TagQueryToMatch` | `FGameplayTagQuery` | - |
| `bUpdatedToUseQuery` | `bool` | - |
| `TagsToMatch` | `EGameplayContainerMatchType` | - |
| `GameplayTags` | `FGameplayTagContainer` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Overlap.json -->

# UEnvQueryTest_Overlap

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverlapData` | `FEnvOverlapData` | Overlap data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Pathfinding.json -->

# UEnvQueryTest_Pathfinding

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TestMode` | `TEnumAsByte < EEnvTestPathfinding :: Type >` | testing mode |
| `Context` | `TSubclassOf < UEnvQueryContext >` | context: other end of pathfinding test |
| `PathFromContext` | `FAIDataProviderBoolValue` | pathfinding direction |
| `SkipUnreachable` | `FAIDataProviderBoolValue` | if set, items with failed path will be invalidated (PathCost, PathLength) |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | navigation filter to use in pathfinding |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_PathfindingBatch.json -->

# UEnvQueryTest_PathfindingBatch

## Inheritance

`UEnvQueryTest_Pathfinding`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ScanRangeMultiplier` | `FAIDataProviderFloatValue` | multiplier for max distance between point and context |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Project.json -->

# UEnvQueryTest_Project

Projects points on navigation or geometry, will modify value of projected items.
  Works only on item type: point

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ProjectionData` | `FEnvTraceData` | trace params |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryTest_Trace.json -->

# UEnvQueryTest_Trace

## Inheritance

`UEnvQueryTest`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TraceData` | `FEnvTraceData` | trace data |
| `TraceFromContext` | `FAIDataProviderBoolValue` | trace direction |
| `ItemHeightOffset` | `FAIDataProviderFloatValue` | Z offset from item |
| `ContextHeightOffset` | `FAIDataProviderFloatValue` | Z offset from querier |
| `Context` | `TSubclassOf < UEnvQueryContext >` | context: other end of trace test |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UExpandableArea.json -->

# UExpandableArea

## Inheritance

`UWidget` -> `INamedSlotInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Style` | `FExpandableAreaStyle` | - |
| `BorderBrush` | `FSlateBrush` | - |
| `BorderColor` | `FSlateColor` | - |
| `bIsExpanded` | `bool` | - |
| `MaxHeight` | `float` | The maximum height of the area |
| `HeaderPadding` | `FMargin` | - |
| `AreaPadding` | `FMargin` | - |
| `HeaderContent` | `UWidget *` | - |
| `BodyContent` | `UWidget *` | - |

## Functions

### `GetIsExpanded`

```text
GetIsExpanded() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIsExpanded`

```text
SetIsExpanded(IsExpanded: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsExpanded` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsExpanded_Animated`

```text
SetIsExpanded_Animated(IsExpanded: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsExpanded` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnExpansionChanged`

```text
OnExpansionChanged(Area: UExpandableArea*, bIsExpanded: bool) -> void
```

A bindable delegate for the IsChecked.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Area` | `UExpandableArea*` | - |
| `bIsExpanded` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UExponentialHeightFogComponent.json -->

# UExponentialHeightFogComponent

Used to create fogging effects such as clouds but with a density that is related to the height of the fog.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FogDensity` | `float` | Global density factor. |
| `CustomHightFogDensity` | `TArray < FCustomHeightFog >` | - |
| `bUseCustomFog` | `bool` | - |
| `CustomFogLow_Height` | `float` | - |
| `CustomFogLow_DensityCoefficient` | `float` | - |
| `CustomFogLow_Color` | `FLinearColor` | - |
| `CustomFogHigh_Height` | `float` | - |
| `CustomFogHigh_DensityCoefficient` | `float` | - |
| `CustomFogHigh_Color` | `FLinearColor` | - |
| `FogInscatteringColor` | `FLinearColor` | - |
| `InscatteringColorCubemap` | `UTextureCube *` | Cubemap that can be specified for fog color, which is useful to make distant, heavily fogged scene elements match the sky.<br>	  When the cubemap is specified, FogInscatteringColor is ignored and Directional inscattering is disabled. |
| `InscatteringColorCubemapAngle` | `float` | Angle to rotate the InscatteringColorCubemap around the Z axis. |
| `InscatteringTextureTint` | `FLinearColor` | Tint color used when InscatteringColorCubemap is specified, for quick edits without having to reimport InscatteringColorCubemap. |
| `FullyDirectionalInscatteringColorDistance` | `float` | Distance at which InscatteringColorCubemap should be used directly for the Inscattering Color. |
| `NonDirectionalInscatteringColorDistance` | `float` | Distance at which only the average color of InscatteringColorCubemap should be used as Inscattering Color. |
| `DirectionalInscatteringExponent` | `float` | Controls the size of the directional inscattering cone, which is used to approximate inscattering from a directional light.  <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| `DirectionalInscatteringStartDistance` | `float` | Controls the start distance from the viewer of the directional inscattering, which is used to approximate inscattering from a directional light. <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| `DirectionalInscatteringColor` | `FLinearColor` | Controls the color of the directional inscattering, which is used to approximate inscattering from a directional light. <br>	  Note: there must be a directional light with bUsedAsAtmosphereSunLight enabled for DirectionalInscattering to be used. |
| `FogHeightFalloff` | `float` | Height density factor, controls how the density increases as height decreases.  <br>	  Smaller values make the visible transition larger. |
| `FogMaxOpacity` | `float` | Maximum opacity of the fog.  <br>	  A value of 1 means the fog can become fully opaque at a distance and replace scene color completely,<br>	  A value of 0 means the fog color will not be factored in at all. |
| `StartDistance` | `float` | Distance from the camera that the fog will start, in world units. |
| `FogCutoffDistance` | `float` | Scene elements past this distance will not have fog applied.  This is useful for excluding skyboxes which already have fog baked in. |
| `Priority` | `int32` | Priority to be rendered with, useful if more than one exponential fogs are visible concurrently |
| `bEnableVolumetricFog` | `bool` | Whether to enable Volumetric fog.  Scalability settings control the resolution of the fog simulation. <br>	  Note that Volumetric fog currently does not support StartDistance, FogMaxOpacity and FogCutoffDistance.<br>	  Volumetric fog also can't match exponential height fog in general as exponential height fog has non-physical behavior. |
| `VolumetricFogScatteringDistribution` | `float` | Controls the scattering phase function - how much incoming light scatters in various directions.<br>	  A distribution value of 0 scatters equally in all directions, while .9 scatters predominantly in the light direction.  <br>	  In order to have visible volumetric fog light shafts from the side, the distribution will need to be closer to 0. |
| `VolumetricFogAlbedo` | `FColor` | The height fog particle reflectiveness used by volumetric fog. <br>	  Water particles in air have an albedo near white, while dust has slightly darker value. |
| `VolumetricFogEmissive` | `FLinearColor` | Light emitted by height fog.  This is a density so more light is emitted the further you are looking through the fog.<br>	  In most cases skylight is a better choice, however right now volumetric fog does not support precomputed lighting, <br>	  So stationary skylights are unshadowed and static skylights don't affect volumetric fog at all. |
| `VolumetricFogExtinctionScale` | `float` | Scales the height fog particle extinction amount used by volumetric fog.  Values larger than 1 cause fog particles everywhere absorb more light. |
| `VolumetricFogDistance` | `float` | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |
| `VolumetricFogStaticLightingScatteringIntensity` | `float` | - |
| `bOverrideLightColorsWithFogInscatteringColors` | `bool` | Whether to use FogInscatteringColor for the Sky Light volumetric scattering color and DirectionalInscatteringColor for the Directional Light scattering color. <br>	  Make sure your directional light has 'Atmosphere Sun Light' enabled!<br>	  Enabling this allows Volumetric fog to better match Height fog in the distance, but produces non-physical volumetric lighting that may not match surface lighting. |
| `VolumetricFogStartDistance` | `float` | Distance over which volumetric fog should be computed.  Larger values extend the effect into the distance but expose under-sampling artifacts in details. |
| `VolumetricFogNoiseTexture` | `UTexture2D *` | - |
| `VolumetricFogNoiseTransform` | `FTransform` | - |

## Functions

### `SetFogDensity`

```text
SetFogDensity(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomFogHeight`

```text
SetCustomFogHeight(Value: float, index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomFogDensityCoefficient`

```text
SetCustomFogDensityCoefficient(Value: float, index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCustomFogInscatteringColor`

```text
SetCustomFogInscatteringColor(Value: FLinearColor, index: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |
| `index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogInscatteringColor`

```text
SetFogInscatteringColor(Value: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInscatteringColorCubemap`

```text
SetInscatteringColorCubemap(Value: UTextureCube *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `UTextureCube *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInscatteringColorCubemapAngle`

```text
SetInscatteringColorCubemapAngle(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFullyDirectionalInscatteringColorDistance`

```text
SetFullyDirectionalInscatteringColorDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNonDirectionalInscatteringColorDistance`

```text
SetNonDirectionalInscatteringColorDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInscatteringTextureTint`

```text
SetInscatteringTextureTint(Value: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDirectionalInscatteringExponent`

```text
SetDirectionalInscatteringExponent(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDirectionalInscatteringStartDistance`

```text
SetDirectionalInscatteringStartDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDirectionalInscatteringColor`

```text
SetDirectionalInscatteringColor(Value: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogHeightFalloff`

```text
SetFogHeightFalloff(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogMaxOpacity`

```text
SetFogMaxOpacity(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStartDistance`

```text
SetStartDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFogCutoffDistance`

```text
SetFogCutoffDistance(Value: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFog`

```text
SetVolumetricFog(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogScatteringDistribution`

```text
SetVolumetricFogScatteringDistribution(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogExtinctionScale`

```text
SetVolumetricFogExtinctionScale(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogAlbedo`

```text
SetVolumetricFogAlbedo(NewValue: FColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogEmissive`

```text
SetVolumetricFogEmissive(NewValue: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogDistance`

```text
SetVolumetricFogDistance(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogStartDistance`

```text
SetVolumetricFogStartDistance(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogNoiseTexture`

```text
SetVolumetricFogNoiseTexture(NewValue: UTexture2D *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricFogNoiseTransform`

```text
SetVolumetricFogNoiseTransform(Transform: FTransform) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UExporter.json -->

# UExporter

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SupportedClass` | `TSubclassOf < UObject >` | Supported class of this exporter |
| `ExportRootScope` | `UObject *` | The root scope of objects to be exported, only used if PPF_ExportsNotFullyQualfied is set<br>	  Objects being exported that are contained within ExportRootScope will use just their name instead of a full path |
| `FormatExtension` | `TArray < FString >` | The root scope of objects to be exported, only used if PPF_ExportsNotFullyQualfied is set<br>	  Objects being exported that are contained within ExportRootScope will use just their name instead of a full path<br>	 <br>	 File extension to use for this exporter |
| `FormatDescription` | `TArray < FString >` | Descriptiong of the export format |
| `PreferredFormatIndex` | `int32` | Index into FormatExtensionFormatDescription of the preferred export format. |
| `TextIndent` | `int32` | Current indentation of spaces of the exported text |
| `bText` | `uint32` | If true, this will export the data as text |
| `bSelectedOnly` | `uint32` | If true, this will export only the selected objects |
| `bForceFileOperations` | `uint32` | If true, this will force the exporter code to create a file-based Ar (this can keep large output files from taking too much memory) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFileMediaSource.json -->

# UFileMediaSource

## Inheritance

`UBaseMediaSource`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FilePath` | `FString` | The path to the media file to be played.<br>	 <br>	  @see SetFilePath |
| `PrecacheFile` | `bool` | Load entire media file into memory and play from there (if possible). |

## Functions

### `SetFilePath`

```text
SetFilePath(Path: FString &) -> void
```

Set the path to the media file that this source represents.
	 
	  Automatically converts full paths to media sources that reside in the
	  Engine's or project's ContentMovies directory into relative paths.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Path` | `FString &` | The path to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFloatBinding.json -->

# UFloatBinding

## Inheritance

`UPropertyBinding`

## Functions

### `GetValue`

```text
GetValue() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFloatingPawnMovement.json -->

# UFloatingPawnMovement

FloatingPawnMovement is a movement component that provides simple movement for any Pawn class.
  Limits on speed and acceleration are provided, while gravity is not implemented.
 
  Normally the root component of the owning actor is moved, however another component may be selected (see SetUpdatedComponent()).
  During swept (non-teleporting) movement only collision of UpdatedComponent is considered, attached components will teleport to the end location ignoring collision.

## Inheritance

`UPawnMovementComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxSpeed` | `float` | Maximum velocity magnitude allowed for the controlled Pawn. |
| `Acceleration` | `float` | Acceleration applied by input (rate of change of velocity) |
| `Deceleration` | `float` | Deceleration applied when there is no input (rate of change of velocity) |
| `TurningBoost` | `float` | Setting affecting extra force applied when changing direction, making turns have less drift and become more responsive.<br>	  Velocity magnitude is not allowed to increase, that only happens due to normal acceleration. It may decrease with large direction changes.<br>	  Larger values apply extra force to reach the target direction more quickly, while a zero value disables any extra turn force. |
| `FloatingMoveSpeedScale` | `float` | Engine Modify Start<br>	 <br>	 Maximum velocity magnitude allowed for the controlled Pawn. |
| `bPositionCorrected` | `uint32` | Set to true when a position correction is applied. Used to avoid recalculating velocity when this occurs. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFoliageInstancedStaticMeshComponent.json -->

# UFoliageInstancedStaticMeshComponent

## Inheritance

`UHierarchicalInstancedStaticMeshComponent`

## Delegates

### `OnInstanceTakePointDamage`

```text
OnInstanceTakePointDamage(InstanceIndex: int32, Damage: float, InstigatedBy: AController*, HitLocation: FVector, ShotFromDirection: FVector, DamageType: const class UDamageType*, DamageCauser: AActor*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `Damage` | `float` | - |
| `InstigatedBy` | `AController*` | - |
| `HitLocation` | `FVector` | - |
| `ShotFromDirection` | `FVector` | - |
| `DamageType` | `const class UDamageType*` | - |
| `DamageCauser` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInstanceTakeRadialDamage`

```text
OnInstanceTakeRadialDamage(Instances: const TArray<int32>&, Damages: const TArray<float>&, InstigatedBy: AController*, Origin: FVector, MaxRadius: float, DamageType: const class UDamageType*, DamageCauser: AActor*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instances` | `const TArray&` | - |
| `Damages` | `const TArray&` | - |
| `InstigatedBy` | `AController*` | - |
| `Origin` | `FVector` | - |
| `MaxRadius` | `float` | - |
| `DamageType` | `const class UDamageType*` | - |
| `DamageCauser` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFoliageStatistics.json -->

# UFoliageStatistics

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `FoliageOverlappingSphereCount`

```text
FoliageOverlappingSphereCount(WorldContextObject: UObject *, StaticMesh: UStaticMesh *, CenterPosition: FVector, Radius: float) -> int32
```

Counts how many foliage instances overlap a given sphere

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `StaticMesh` | `UStaticMesh *` | - |
| `CenterPosition` | `FVector` | The center position of the sphere |
| `Radius` | `float` | The radius of the sphere. |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `FoliageOverlappingBoxCount`

```text
FoliageOverlappingBoxCount(WorldContextObject: UObject *, StaticMesh: UStaticMesh *, Box: FBox) -> int32
```

Gets the number of instances overlapping a provided box

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `StaticMesh` | `UStaticMesh *` | Mesh to count |
| `Box` | `FBox` | Box to overlap |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFoliageType.json -->

# UFoliageType

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UpdateGuid` | `FGuid` | A GUID that is updated every time the foliage type is modified,<br>	   so foliage placed in the level can detect the FoliageType has changed. |
| `Density` | `float` | Foliage instances will be placed at this density, specified in instances per 1000x1000 unit area |
| `DensityAdjustmentFactor` | `float` | The factor by which to adjust the density of instances. Values >1 will increase density while values <1 will decrease it. |
| `Radius` | `float` | The minimum distance between foliage instances |
| `Scaling` | `EFoliageScaling` | Specifies foliage instance scaling behavior when painting. |
| `ScaleX` | `FFloatInterval` | Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's X Scale property |
| `ScaleY` | `FFloatInterval` | Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Y Scale property |
| `ScaleZ` | `FFloatInterval` | Specifies the range of scale, from minimum to maximum, to apply to a foliage instance's Z Scale property |
| `VertexColorMaskByChannel` | `FFoliageVertexColorChannelMask` | - |
| `VertexColorMask_DEPRECATED` | `TEnumAsByte < enum FoliageVertexColorMask >` | When painting on static meshes, foliage instance placement can be limited to areas where the static mesh has values in the selected vertex color channel(s).<br>	   This allows a static mesh to mask out certain areas to prevent foliage from being placed there |
| `VertexColorMaskThreshold_DEPRECATED` | `float` | Specifies the threshold value above which the static mesh vertex color value must be, in order for foliage instances to be placed in a specific area |
| `VertexColorMaskInvert_DEPRECATED` | `uint32` | When unchecked, foliage instances will be placed only when the vertex color in the specified channel(s) is above the threshold amount.<br>	   When checked, the vertex color must be less than the threshold amount |
| `ZOffset` | `FFloatInterval` | Specifies a range from minimum to maximum of the offset to apply to a foliage instance's Z location |
| `AlignToNormal` | `uint32` | Whether foliage instances should have their angle adjusted away from vertical to match the normal of the surface they're painted on<br>	   If AlignToNormal is enabled and RandomYaw is disabled, the instance will be rotated so that the +X axis points down-slope |
| `AlignMaxAngle` | `float` | The maximum angle in degrees that foliage instances will be adjusted away from the vertical |
| `RandomYaw` | `uint32` | If selected, foliage instances will have a random yaw rotation around their vertical axis applied |
| `RandomPitchAngle` | `float` | A random pitch adjustment can be applied to each instance, up to the specified angle in degrees, from the original vertical |
| `GroundSlopeAngle` | `FFloatInterval` | Foliage instances will only be placed on surfaces sloping in the specified angle range from the horizontal |
| `Height` | `FFloatInterval` | The valid altitude range where foliage instances will be placed, specified using minimum and maximum world coordinate Z values |
| `LandscapeLayers` | `TArray < FName >` | If a layer name is specified, painting on landscape will limit the foliage to areas of landscape with the specified layer painted |
| `LandscapeLayer_DEPRECATED` | `FName` | - |
| `CollisionWithWorld` | `uint32` | If checked, an overlap test with existing world geometry is performed before each instance is placed |
| `CollisionScale` | `FVector` | The foliage instance's collision bounding box will be scaled by the specified amount before performing the overlap check |
| `MinimumLayerWeight` | `float` | Specifies the minimum value above which the landscape layer weight value must be, in order for foliage instances to be placed in a specific area |
| `MeshBounds` | `FBoxSphereBounds` | - |
| `LowBoundOriginRadius` | `FVector` | - |
| `Mobility` | `TEnumAsByte < EComponentMobility :: Type >` | Mobility property to apply to foliage components |
| `CullDistance` | `FInt32Interval` | The distance where instances will begin to fade out if using a PerInstanceFadeAmount material node. 0 disables.<br>	  When the entire cluster is beyond this distance, the cluster is completely culled and not rendered at all. |
| `NearCullDistance` | `int32` | - |
| `bIsFlyType` | `bool` | - |
| `bEnableStaticLighting_DEPRECATED` | `uint32` | Deprecated. Now use the Mobility setting to control staticdynamic lighting |
| `CastShadow` | `uint32` | Controls whether the foliage should cast a shadow or not. |
| `bAffectDynamicIndirectLighting` | `uint32` | Controls whether the foliage should inject light into the Light Propagation Volume.  This flag is only used if CastShadow is true. |
| `bAffectDistanceFieldLighting` | `uint32` | Controls whether the primitive should affect dynamic distance field lighting methods.  This flag is only used if CastShadow is true. |
| `bCastDynamicShadow` | `uint32` | Controls whether the foliage should cast shadows in the case of non precomputed shadowing.  This flag is only used if CastShadow is true. |
| `bCastStaticShadow` | `uint32` | Whether the foliage should cast a static shadow from shadow casting lights.  This flag is only used if CastShadow is true. |
| `bGenerateSurfaceSample` | `uint32` | - |
| `bOccludeLightingRay` | `uint32` | - |
| `bCastShadowAsTwoSided` | `uint32` | Whether this foliage should cast dynamic shadows as if it were a two sided material. |
| `bReceivesDecals` | `uint32` | Whether the foliage receives decals. |
| `bOverrideLightMapRes` | `uint32` | Whether to override the lightmap resolution defined in the static mesh. |
| `OverriddenLightMapRes` | `int32` | Overrides the lightmap resolution defined in the static mesh |
| `LightmapType` | `ELightmapType` | Controls the type of lightmap used for this component. |
| `FakeSkyLightAOIntensity` | `float` | Controls the intensity of FakeSkyLightAO. 0 = no fake AO (full bright), 1 = full effect (default). |
| `bUseAsOccluder` | `uint32` | If enabled, foliage will render a pre-pass which allows it to occlude other primitives, and also allows<br>	  it to correctly receive DBuffer decals. Enabling this setting may have a negative performance impact. |
| `BodyInstance` | `FBodyInstance` | Custom collision for foliage |
| `CustomNavigableGeometry` | `TEnumAsByte < EHasCustomNavigableGeometry :: Type >` | Force navmesh |
| `LightingChannels` | `FLightingChannels` | Lighting channels that placed foliage will be assigned. Lights with matching channels will affect the foliage.<br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| `bRenderCustomDepth` | `uint32` | If true, the foliage will be rendered in the CustomDepth pass (usually used for outlines) |
| `CustomDepthStencilValue` | `int32` | Optionally write this 0-255 value to the stencil buffer in CustomDepth pass (Requires project setting or r.CustomDepth == 3) |
| `CollisionRadius` | `float` | The CollisionRadius determines when two instances overlap. When two instances overlap a winner will be picked based on rules and priority. |
| `ShadeRadius` | `float` | The ShadeRadius determines when two instances overlap. If an instance can grow in the shade this radius is ignored. |
| `NumSteps` | `int32` | The number of times we age the species and spread its seeds. |
| `InitialSeedDensity` | `float` | Specifies the number of seeds to populate along 10 meters. The number is implicitly squared to cover a 10m x 10m area |
| `AverageSpreadDistance` | `float` | The average distance between the spreading instance and its seeds. For example, a tree with an AverageSpreadDistance 10 will ensure the average distance between the tree and its seeds is 10cm |
| `SpreadVariance` | `float` | Specifies how much seed distance varies from the average. For example, a tree with an AverageSpreadDistance 10 and a SpreadVariance 1 will produce seeds with an average distance of 10cm plus or minus 1cm |
| `SeedsPerStep` | `int32` | The number of seeds an instance will spread in a single step of the simulation. |
| `DistributionSeed` | `int32` | The seed that determines placement of initial seeds. |
| `MaxInitialSeedOffset` | `float` | The seed that determines placement of initial seeds. |
| `bCanGrowInShade` | `bool` | If true, seeds of this type will ignore shade radius during overlap tests with other types. |
| `bSpawnsInShade` | `bool` | Whether new seeds are spawned exclusively in shade. Occurs in a second pass after all types that do not spawn in shade have been simulated.<br>	  Only valid when CanGrowInShade is true. |
| `MaxInitialAge` | `float` | Allows a new seed to be older than 0 when created. New seeds will be randomly assigned an age in the range [0,MaxInitialAge] |
| `MaxAge` | `float` | Specifies the oldest a seed can be. After reaching this age the instance will still spread seeds, but will not get any older |
| `OverlapPriority` | `float` | When two instances overlap we must determine which instance to remove.<br>	  The instance with a lower OverlapPriority will be removed.<br>	  In the case where OverlapPriority is the same regular simulation rules apply. |
| `ProceduralScale` | `FFloatInterval` | The scale range of this type when being procedurally generated. Configured with the Scale Curve. |
| `ScaleCurve` | `FRuntimeFloatCurve` | Instance scale factor as a function of normalized age (i.e. Current Age  Max Age).<br>	  X = 0 corresponds to Age = 0, X = 1 corresponds to Age = Max Age.<br>	  Y = 0 corresponds to Min Scale, Y = 1 corresponds to Max Scale. |
| `ChangeCount` | `int32` | - |
| `ReapplyDensity` | `uint32` | If checked, the density of foliage instances already placed will be adjusted by the density adjustment factor. |
| `ReapplyRadius` | `uint32` | If checked, foliage instances not meeting the new Radius constraint will be removed |
| `ReapplyAlignToNormal` | `uint32` | If checked, foliage instances will have their normal alignment adjusted by the Reapply tool |
| `ReapplyRandomYaw` | `uint32` | If checked, foliage instances will have their yaw adjusted by the Reapply tool |
| `ReapplyScaling` | `uint32` | If checked, foliage instances will have their scale adjusted to fit the specified scaling behavior by the Reapply tool |
| `ReapplyScaleX` | `uint32` | If checked, foliage instances will have their X scale adjusted by the Reapply tool |
| `ReapplyScaleY` | `uint32` | If checked, foliage instances will have their Y scale adjusted by the Reapply tool |
| `ReapplyScaleZ` | `uint32` | If checked, foliage instances will have their Z scale adjusted by the Reapply tool |
| `ReapplyRandomPitchAngle` | `uint32` | If checked, foliage instances will have their pitch adjusted by the Reapply tool |
| `ReapplyGroundSlope` | `uint32` | If checked, foliage instances not meeting the ground slope condition will be removed by the Reapply too |
| `ReapplyHeight` | `uint32` | If checked, foliage instances not meeting the valid Z height condition will be removed by the Reapply tool |
| `ReapplyLandscapeLayers` | `uint32` | If checked, foliage instances painted on areas that do not have the appropriate landscape layer painted will be removed by the Reapply tool |
| `ReapplyZOffset` | `uint32` | If checked, foliage instances will have their Z offset adjusted by the Reapply tool |
| `ReapplyCollisionWithWorld` | `uint32` | If checked, foliage instances will have an overlap test with the world reapplied, and overlapping instances will be removed by the Reapply tool |
| `ReapplyVertexColorMask` | `uint32` | If checked, foliage instances no longer matching the vertex color constraint will be removed by the Reapply too |
| `bEnableDensityScaling` | `uint32` | Whether this foliage type should be affected by the Engine Scalability system's Foliage scalability setting.<br>	  Enable for detail meshes that don't really affect the game. Disable for anything important.<br>	  Typically, this will be enabled for small meshes without collision (e.g. grass) and disabled for large meshes with collision (e.g. trees) |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFoliageType_Actor.json -->

# UFoliageType_Actor

## Inheritance

`UFoliageType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActorClass` | `TSubclassOf < AActor >` | - |
| `bShouldAttachToBaseComponent` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFoliageType_InstancedStaticMesh.json -->

# UFoliageType_InstancedStaticMesh

## Inheritance

`UFoliageType`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Mesh` | `UStaticMesh *` | - |
| `OverrideMaterials` | `TArray < UMaterialInterface * >` | - |
| `ComponentClass` | `TSubclassOf < UFoliageInstancedStaticMeshComponent >` | The component class to use for foliage instances. <br>	   You can make a Blueprint subclass of FoliageInstancedStaticMeshComponent to implement custom behavior and assign that class here. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFont.json -->

# UFont

A font object, for use by Slate, UMG, and Canvas.
 
  A font can either be:
     Runtime cached - The font contains a series of TTF files that combine to form a composite font. The glyphs are cached on demand when required at runtime.
     Offline cached - The font contains a series of textures containing pre-baked cached glyphs and their associated texture coordinates.

## Inheritance

`UObject` -> `IFontProviderInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FontCacheType` | `EFontCacheType` | What kind of font caching should we use? This controls which options we see |
| `Characters` | `TArray < FFontCharacter >` | List of characters in the font.  For a MultiFont, this will include all characters in all sub-fonts!  Thus,<br>		the number of characters in this array isn't necessary the number of characters available in the font |
| `Textures` | `TArray < UTexture2D * >` | Textures that store this font's glyph image data |
| `IsRemapped` | `int32` | True if font is 'remapped'.  That is, the character array is not a direct mapping to unicode values.  Instead,<br>		all characters are indexed indirectly through the CharRemap array |
| `EmScale` | `float` | Font metrics. |
| `Ascent` | `float` | @todo document |
| `Descent` | `float` | @todo document |
| `Leading` | `float` | @todo document |
| `Kerning` | `int32` | Default horizontal spacing between characters when rendering text with this font |
| `ImportOptions` | `FFontImportOptionsData` | Options used when importing this font |
| `NumCharacters` | `int32` | Number of characters in the font, not including multiple instances of the same character (for multi-fonts).<br>		This is cached at load-time or creation time, and is never serialized. |
| `MaxCharHeight` | `TArray < int32 >` | The maximum height of a character in this font.  For multi-fonts, this array will contain a maximum<br>		cached at load-time or creation time, and is never serialized. |
| `ScalingFactor` | `float` | Scale to apply to the font. |
| `LegacyFontSize` | `int32` | The default size of the font used for legacy Canvas APIs that don't specify a font size |
| `LegacyFontName` | `FName` | The default font name to use for legacy Canvas APIs that don't specify a font name |
| `CompositeFont` | `FCompositeFont` | Embedded composite font data |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFontFace.json -->

# UFontFace

A font face asset contains the raw payload data for a source TTFOTF file as used by FreeType.
  During cook this asset type generates a ".ufont" file containing the raw payload data (unless loaded "Inline").

## Inheritance

`UObject` -> `IFontFaceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceFilename` | `FString` | The filename of the font face we were created from. This may not always exist on disk, as we may have previously loaded and cached the font data inside this asset. |
| `Hinting` | `EFontHinting` | The hinting algorithm to use with the font face. |
| `LoadingPolicy` | `EFontLoadingPolicy` | Enum controlling how this font face should be loaded at runtime. See the enum for more explanations of the options. |
| `LayoutMethod` | `EFontLayoutMethod` | Which method should we use when laying out the font? Try changing this if you notice clipping or height issues with your font. |
| `FontFaceData_DEPRECATED` | `TArray < uint8 >` | The data associated with the font face. This should always be filled in providing the source filename is valid. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UFontImportOptions.json -->

# UFontImportOptions

Holds options for importing fonts.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Data` | `FFontImportOptionsData` | The actual data for this object.  We wrap it in a struct so that we can copy it around between objects. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UForceFeedbackAttenuation.json -->

# UForceFeedbackAttenuation

Wrapper class that can be created as an asset for force feedback attenuation properties which allows reuse
  of the properties for multiple attenuation components

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Attenuation` | `FForceFeedbackAttenuationSettings` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UForceFeedbackComponent.json -->

# UForceFeedbackComponent

ForceFeedbackComponent allows placing a rumble effect in to the world and having it apply to player characters who come near it

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | The feedback effect to be played |
| `bAutoDestroy` | `uint8` | Auto destroy this component on completion |
| `bStopWhenOwnerDestroyed` | `uint8` | Stop effect when owner is destroyed |
| `bLooping` | `uint8` | - |
| `bIgnoreTimeDilation` | `uint8` | Should the playback of the forcefeedback pattern ignore time dilation and use the app's delta time |
| `bOverrideAttenuation` | `uint8` | Should the Attenuation Settings asset be used (false) or should the properties set directly on the component be used for attenuation properties |
| `IntensityMultiplier` | `float` | The intensity multiplier to apply to effects generated by this component |
| `AttenuationSettings` | `UForceFeedbackAttenuation *` | If bOverrideSettings is false, the asset to use to determine attenuation properties for effects generated by this component |
| `AttenuationOverrides` | `FForceFeedbackAttenuationSettings` | If bOverrideSettings is true, the attenuation properties to use for effects generated by this component |

## Functions

### `SetForceFeedbackEffect`

```text
SetForceFeedbackEffect(NewForceFeedbackEffect: UForceFeedbackEffect *) -> void
```

Set what force feedback effect is played by this component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewForceFeedbackEffect` | `UForceFeedbackEffect *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Play`

```text
Play(StartTime: float) -> void
```

Start a feedback effect playing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Stop`

```text
Stop() -> void
```

Stop playing the feedback effect

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIntensityMultiplier`

```text
SetIntensityMultiplier(NewIntensityMultiplier: float) -> void
```

Set a new intensity multiplier

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensityMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AdjustAttenuation`

```text
AdjustAttenuation(InAttenuationSettings: FForceFeedbackAttenuationSettings &) -> void
```

Modify the attenuation settings of the component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAttenuationSettings` | `FForceFeedbackAttenuationSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BP_GetAttenuationSettingsToApply`

```text
BP_GetAttenuationSettingsToApply(OutAttenuationSettings: FForceFeedbackAttenuationSettings &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutAttenuationSettings` | `FForceFeedbackAttenuationSettings &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnForceFeedbackFinished`

```text
OnForceFeedbackFinished(ForceFeedbackComponent: UForceFeedbackComponent*) -> void
```

called when we finish playing audio, either because it played to completion or because a Stop() call turned it off early

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ForceFeedbackComponent` | `UForceFeedbackComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UForceFeedbackEffect.json -->

# UForceFeedbackEffect

A predefined force-feedback effect to be played on a controller

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChannelDetails` | `TArray < FForceFeedbackChannelDetails >` | - |
| `Duration` | `float` | Duration of force feedback pattern in seconds. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameEngine.json -->

# UGameEngine

Engine that manages core systems that enable a game.

## Inheritance

`UEngine`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxDeltaTime` | `float` | Maximium delta time the engine uses to populate FApp::DeltaTime. If 0, unbound. |
| `ServerFlushLogInterval` | `float` | Maximium time (in seconds) between the flushes of the logs on the server (best effort). If 0, this will happen every tick. |
| `GameInstance` | `UGameInstance *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameInstance.json -->

# UGameInstance

GameInstance: high-level manager object for an instance of the running game.
  Spawned at game creation and not destroyed until game instance is shut down.
  Running as a standalone game, there will be one of these.
  Running in PIE (play-in-editor) will generate one of these per PIE instance.

## Inheritance

`UObject` -> `FExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EncryptedLocalPlayers` | `TArray < int64 >` | - |
| `LocalPlayers` | `TArray < ULocalPlayer * >` | - |
| `OnlineSession` | `UOnlineSession *` | Class to manage online services |
| `bUseEncryptLocalPlayerPtr` | `bool` | - |
| `DSHUD` | `UObject *` | - |
| `CachedConsoleVariableBunch_Groups` | `TArray < TArray < uint8 > >` | - |
| `CachedConsoleVariableBunch_BigWorld` | `TArray < uint8 >` | - |
| `CachedConsoleVariableBunch_Permanent` | `TArray < uint8 >` | - |
| `SpecialPakResStates` | `TMap < ESpecialPakID , EPakResState >` | - |

## Functions

### `ReceiveInit`

```text
ReceiveInit() -> void
```

Opportunity for blueprints to handle the game instance being initialized.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveShutdown`

```text
ReceiveShutdown() -> void
```

Opportunity for blueprints to handle the game instance being shutdown.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleNetworkError`

```text
HandleNetworkError(FailureType: ENetworkFailure :: Type, bIsServer: bool) -> void
```

Opportunity for blueprints to handle network errors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FailureType` | `ENetworkFailure :: Type` | - |
| `bIsServer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleTravelError`

```text
HandleTravelError(FailureType: ETravelFailure :: Type) -> void
```

Opportunity for blueprints to handle travel errors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FailureType` | `ETravelFailure :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCreatePlayer`

```text
DebugCreatePlayer(ControllerId: int32) -> void
```

Local player access 
	
	  Debug console command to create a player.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControllerId` | `int32` | - The controller ID the player should accept input from. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugRemovePlayer`

```text
DebugRemovePlayer(ControllerId: int32) -> void
```

Debug console command to remove the player with a given controller ID.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControllerId` | `int32` | - The controller ID to search for. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetDynaConfigAndDynaCVar`

```text
ResetDynaConfigAndDynaCVar() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetDynaConfig`

```text
ResetDynaConfig() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SendConsoleVariableBunch`

```text
SendConsoleVariableBunch(CVarType: ECVarType, Connection: UNetConnection *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |
| `Connection` | `UNetConnection *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveConsoleVariableBunch_BigWorld`

```text
ReceiveConsoleVariableBunch_BigWorld(InConsoleVariablesBunch: TArray < uint8 >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InConsoleVariablesBunch` | `TArray < uint8 >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveConsoleVariableBunch_Permanent`

```text
ReceiveConsoleVariableBunch_Permanent(InConsoleVariablesBunch: TArray < uint8 >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InConsoleVariablesBunch` | `TArray < uint8 >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableConsoleVariableBunch`

```text
EnableConsoleVariableBunch(CVarType: ECVarType, bMapIsBigWorld: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |
| `bMapIsBigWorld` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearConsoleVariableBunch`

```text
ClearConsoleVariableBunch(CVarType: ECVarType) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetConsoleVariable`

```text
ResetConsoleVariable(CVarType: ECVarType) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPakResState`

```text
SetPakResState(InPakID: ESpecialPakID, InPakState: EPakResState) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |
| `InPakState` | `EPakResState` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPakResState`

```text
GetPakResState(InPakID: ESpecialPakID) -> EPakResState
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |

**Returns**

| Type | Description |
|---|---|
| `EPakResState` | - |

### `IsPlatformSplitPakRes`

```text
IsPlatformSplitPakRes(InPakID: ESpecialPakID) -> EPakSplitState
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |

**Returns**

| Type | Description |
|---|---|
| `EPakSplitState` | - |

### `InitPakResState`

```text
InitPakResState() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPakResStateChanged`

```text
OnPakResStateChanged(InPakID: ESpecialPakID, InPakOldState: EPakResState, InPakNewState: EPakResState) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |
| `InPakOldState` | `EPakResState` | - |
| `InPakNewState` | `EPakResState` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameMapsSettings.json -->

# UGameMapsSettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EditorStartupMap` | `FSoftObjectPath` | If set, this map will be loaded when the Editor starts up. |
| `LocalMapOptions` | `FString` | The default options that will be appended to a map being loaded. |
| `TransitionMap` | `FSoftObjectPath` | The map loaded when transition from one map to another. |
| `bUseSplitscreen` | `bool` | Whether the screen should be split or not when multiple local players are present |
| `TwoPlayerSplitscreenLayout` | `TEnumAsByte < ETwoPlayerSplitScreenType :: Type >` | The viewport layout to use if the screen should be split and there are two local players |
| `ThreePlayerSplitscreenLayout` | `TEnumAsByte < EThreePlayerSplitScreenType :: Type >` | The viewport layout to use if the screen should be split and there are three local players |
| `bOffsetPlayerGamepadIds` | `bool` | If enabled, this will make so that gamepads start being assigned to the second controller ID in local multiplayer games.<br>	 In PIE sessions with multiple windows, this has the same effect as enabling "Route 1st Gamepad to 2nd Client" |
| `GameInstanceClass` | `FSoftClassPath` | The class to use when instantiating the transient GameInstance class |
| `GameDefaultMap` | `FSoftObjectPath` | The map that will be loaded by default when no other map is loaded. |
| `HSCDefaultMap` | `FSoftObjectPath` | - |
| `UGCMDefaultMap` | `FSoftObjectPath` | - |
| `ServerDefaultMap` | `FSoftObjectPath` | The map that will be loaded by default when no other map is loaded (DEDICATED SERVER). |
| `GlobalDefaultGameMode` | `FSoftClassPath` | GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL). |
| `GlobalDefaultServerGameMode` | `FSoftClassPath` | GameMode to use if not specified in any other way. (e.g. per-map DefaultGameMode or on the URL) (DEDICATED SERVERS)<br>	  If not set, the GlobalDefaultGameMode value will be used. |
| `GameModeMapPrefixes` | `TArray < FGameModeName >` | Overrides the GameMode to use when loading a map that starts with a specific prefix |
| `GameModeClassAliases` | `TArray < FGameModeName >` | List of GameModes to load when game= is specified in the URL (e.g. "DM" could be an alias for "MyProject.MyGameModeMP_DM") |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameModeGeneralDataAsset.json -->

# UGameModeGeneralDataAsset

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CampConfigs` | `TArray < FCampConfigInfo >` | - |
| `CampRelationConfigs` | `TArray < FCampReleation >` | - |
| `DefaultCampRelation` | `ECampRelation` | - |
| `bDifferentTeamHasDifferentCamp` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameNetworkManagerSettings.json -->

# UGameNetworkManagerSettings

Holds the settings for the AGameNetworkManager class.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MinDynamicBandwidth` | `int32` | Minimum bandwidth dynamically set per connection. |
| `MaxDynamicBandwidth` | `int32` | Maximum bandwidth dynamically set per connection. |
| `TotalNetBandwidth` | `int32` | Total available bandwidth for listen server, split dynamically across net connections. |
| `BadPingThreshold` | `int32` | The point we determine the server is either delaying packets or has bad upstream. |
| `bIsStandbyCheckingEnabled` | `uint32` | Used to determine if checking for standby cheats should occur. |
| `StandbyRxCheatTime` | `float` | The amount of time without packets before triggering the cheat code. |
| `StandbyTxCheatTime` | `float` | The amount of time without packets before triggering the cheat code. |
| `PercentMissingForRxStandby` | `float` | The percentage of clients missing RX data before triggering the standby code. |
| `PercentMissingForTxStandby` | `float` | The percentage of clients missing TX data before triggering the standby code. |
| `PercentForBadPing` | `float` | The percentage of clients with bad ping before triggering the standby code. |
| `JoinInProgressStandbyWaitTime` | `float` | The amount of time to wait before checking a connection for standby issues. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayDataCollectHelperBase.json -->

# UGameplayDataCollectHelperBase

## Inheritance

`UObject`

## Functions

### `GMPEvent_SkillUseDelay`

```text
GMPEvent_SkillUseDelay(SkillUID: int32, bRealUsed: bool) -> void
```

老技能释放延迟时间（客户端点击到实际释放的时间差）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillUID` | `int32` | - |
| `bRealUsed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GMPEvent_SkillUseFaildRate`

```text
GMPEvent_SkillUseFaildRate(SkillUID: int32, bUseFailed: bool) -> void
```

老技能释放失败率

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillUID` | `int32` | - |
| `bUseFailed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%BC%95%E6%93%8E/%E5%B8%B8%E7%94%A8%E5%85%A8%E5%B1%80%E7%B1%BB/UGameplayStatics.json -->

# UGameplayStatics

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SpawnObject`

```text
SpawnObject(ObjectClass: TSubclassOf < UObject >, Outer: UObject *) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectClass` | `TSubclassOf < UObject >` | - |
| `Outer` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `BeginSpawningActorFromBlueprint`

```text
BeginSpawningActorFromBlueprint(WorldContextObject: UObject *, Blueprint: UBlueprint *, SpawnTransform: FTransform &, bNoCollisionFail: bool) -> AActor *
```

生成指定蓝图类的实例，但不自动执行构造函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `Blueprint` | `UBlueprint *` | 蓝图类 |
| `SpawnTransform` | `FTransform &` | 生成Actor的Transform |
| `bNoCollisionFail` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor实例 |

### `BeginSpawningActorFromClass`

```text
BeginSpawningActorFromClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, SpawnTransform: FTransform &, bNoCollisionFail: bool, Owner: AActor *) -> AActor *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | - |
| `SpawnTransform` | `FTransform &` | - |
| `bNoCollisionFail` | `bool` | - |
| `Owner` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `BeginDeferredActorSpawnFromClass`

```text
BeginDeferredActorSpawnFromClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, SpawnTransform: FTransform &, CollisionHandlingOverride: ESpawnActorCollisionHandlingMethod, Owner: AActor *) -> AActor *
```

Spawns an instance of an actor class, but does not automatically run its construction script.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | - |
| `SpawnTransform` | `FTransform &` | - |
| `CollisionHandlingOverride` | `ESpawnActorCollisionHandlingMethod` | - |
| `Owner` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `FinishSpawningActor`

```text
FinishSpawningActor(Actor: AActor *, SpawnTransform: FTransform &) -> AActor *
```

结束生成Actor，执行Actor的构造函数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | Actor实例 |
| `SpawnTransform` | `FTransform &` | 生成Actor的Transform |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | Actor实例 |

### `GetActorArrayAverageLocation`

```text
GetActorArrayAverageLocation(Actors: TArray < AActor * > &) -> FVector
```

Find the average location (centroid) of an array of Actors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actors` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetActorArrayBounds`

```text
GetActorArrayBounds(Actors: TArray < AActor * > &, bOnlyCollidingComponents: bool, Center: FVector &, BoxExtent: FVector &) -> void
```

Bind the bounds of an array of Actors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actors` | `TArray < AActor * > &` | - |
| `bOnlyCollidingComponents` | `bool` | - |
| `Center` | `FVector &` | - |
| `BoxExtent` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllActorsOfClass`

```text
GetAllActorsOfClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >, OutActors: TArray < AActor * > &) -> void
```

Find all Actors in the world of the specified class.
	 	This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | Class of Actor to find. Must be specified or result array will be empty. |
| `OutActors` | `TArray < AActor * > &` | Output array of Actors of the specified class. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFirstActorOfClass`

```text
GetFirstActorOfClass(WorldContextObject: UObject *, ActorClass: TSubclassOf < AActor >) -> AActor *
```

Find one Actor in the world of the specified class.
		This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ActorClass` | `TSubclassOf < AActor >` | Class of Actor to find. Must be specified or result array will be empty. |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

### `GetAllActorsWithInterface`

```text
GetAllActorsWithInterface(WorldContextObject: UObject *, Interface: TSubclassOf < UInterface >, OutActors: TArray < AActor * > &) -> void
```

Find all Actors in the world with the specified interface.
	 	This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Interface` | `TSubclassOf < UInterface >` | Interface to find. Must be specified or result array will be empty. |
| `OutActors` | `TArray < AActor * > &` | Output array of Actors of the specified interface. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllActorsWithTag`

```text
GetAllActorsWithTag(WorldContextObject: UObject *, Tag: FName, OutActors: TArray < AActor * > &) -> void
```

获取拥有指定Tag的所有Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `Tag` | `FName` | Tag名称 |
| `OutActors` | `TArray < AActor * > &` | 输出的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetGameInstance`

```text
GetGameInstance(WorldContextObject: UObject *) -> UGameInstance *
```

获取GameInstance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `UGameInstance *` | GameInstance |

### `GetCurrentGameInstance`

```text
GetCurrentGameInstance() -> UGameInstance *
```

**Returns**

| Type | Description |
|---|---|
| `UGameInstance *` | - |

### `GetPlayerController`

```text
GetPlayerController(WorldContextObject: UObject *, PlayerIndex: int32) -> APlayerController *
```

获取PlayerController

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | PlayerController |

### `GetPlayerPawn`

```text
GetPlayerPawn(WorldContextObject: UObject *, PlayerIndex: int32) -> APawn *
```

获取PlayerPawn

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `APawn *` | PlayerPawn |

### `GetPlayerCharacter`

```text
GetPlayerCharacter(WorldContextObject: UObject *, PlayerIndex: int32) -> ACharacter *
```

获取PlayerCharacter

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ACharacter *` | PlayerCharacter |

### `GetPlayerCameraManager`

```text
GetPlayerCameraManager(WorldContextObject: UObject *, PlayerIndex: int32) -> APlayerCameraManager *
```

获取PlayerCameraManager

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `APlayerCameraManager *` | PlayerCameraManager |

### `CreatePlayer`

```text
CreatePlayer(WorldContextObject: UObject *, ControllerId: int32, bSpawnPawn: bool) -> APlayerController *
```

Create a new player for this game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ControllerId` | `int32` | The ID of the controller that the should control the newly created player. A value of -1 specifies to use the next available ID |
| `bSpawnPawn` | `bool` | Whether a pawn should be spawned immediately. If false a pawn will not be created until transition to the next map. |

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | - |

### `RemovePlayer`

```text
RemovePlayer(Player: APlayerController *, bDestroyPawn: bool) -> void
```

Removes a player from this game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | The player controller of the player to be removed |
| `bDestroyPawn` | `bool` | Whether the controlled pawn should be deleted as well |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlayerControllerID`

```text
GetPlayerControllerID(Player: APlayerController *) -> int32
```

Gets what controller ID a Player is using

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | The player controller of the player to get the ID of |

**Returns**

| Type | Description |
|---|---|
| `int32` | The ID of the passed in player. -1 if there is no controller for the passed in player |

### `SetPlayerControllerID`

```text
SetPlayerControllerID(Player: APlayerController *, ControllerId: int32) -> void
```

Sets what controller ID a Player should be using

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | The player controller of the player to change the controller ID of |
| `ControllerId` | `int32` | The controller ID to assign to this player |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LoadStreamLevel`

```text
LoadStreamLevel(WorldContextObject: UObject *, LevelName: FName, bMakeVisibleAfterLoad: bool, bShouldBlockOnLoad: bool, LatentInfo: FLatentActionInfo) -> void
```

加载子关卡

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `LevelName` | `FName` | 子关卡名称 |
| `bMakeVisibleAfterLoad` | `bool` | 加载后是否显示 |
| `bShouldBlockOnLoad` | `bool` | 加载时是否阻塞 |
| `LatentInfo` | `FLatentActionInfo` | 回调信息结构 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnloadStreamLevel`

```text
UnloadStreamLevel(WorldContextObject: UObject *, LevelName: FName, LatentInfo: FLatentActionInfo) -> void
```

加载子关卡

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `LevelName` | `FName` | 子关卡名称 |
| `LatentInfo` | `FLatentActionInfo` | 回调信息结构 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetStreamingLevel`

```text
GetStreamingLevel(WorldContextObject: UObject *, PackageName: FName) -> ULevelStreaming *
```

Returns level streaming object with specified level package name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PackageName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `ULevelStreaming *` | - |

### `FlushLevelStreaming`

```text
FlushLevelStreaming(WorldContextObject: UObject *) -> void
```

刷新关卡流，直到所有子关卡加载完毕时返回

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushLevelStreamingBasedOnCharacterLocation`

```text
FlushLevelStreamingBasedOnCharacterLocation(WorldContextObject: UObject *, CharacterLocation: FVector) -> void
```

更新玩家的位置，触发LevelBounds，然后加载所有关卡

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `CharacterLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushAllStreamingResource`

```text
FlushAllStreamingResource(WorldContextObject: UObject *) -> void
```

触发TextureStreaming， 将贴图全部加载完毕

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CancelAsyncLoading`

```text
CancelAsyncLoading() -> void
```

Cancels all currently queued streaming packages

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OpenLevel`

```text
OpenLevel(WorldContextObject: UObject *, LevelName: FName, bAbsolute: bool, Options: FString) -> void
```

Travel to another level

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `LevelName` | `FName` | the level to open |
| `bAbsolute` | `bool` | if true options are reset, if false options are carried over from current level |
| `Options` | `FString` | a string of options to use for the travel URL |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OpenShaderLibrary`

```text
OpenShaderLibrary(Name: FString &, VersionNum: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FString &` | - |
| `VersionNum` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CloseShaderLibrary`

```text
CloseShaderLibrary(Name: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableShaderGroup`

```text
EnableShaderGroup(GroupName: FString &, ShaderPlatform: int32) -> void
```

Enable a new ShaderGroup for all opened ShaderCodeLibrary

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GroupName` | `FString &` | - |
| `ShaderPlatform` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableShaderLevel`

```text
EnableShaderLevel(ShaderLevelName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderLevelName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableShaderPak`

```text
EnableShaderPak(ShaderPakName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderPakName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableShaderLevel`

```text
DisableShaderLevel(ShaderLevelName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderLevelName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableShaderPak`

```text
DisableShaderPak(ShaderPakName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShaderPakName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RestartShaderPrecompile`

```text
RestartShaderPrecompile() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OpenShaderCodeLibrary`

```text
OpenShaderCodeLibrary(Version: FString &, bUseContentShaders: bool) -> void
```

OpenShaderCodeLibrary in Saved Folder

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Version` | `FString &` | - |
| `bUseContentShaders` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentLevelName`

```text
GetCurrentLevelName(WorldContextObject: UObject *, bRemovePrefixString: bool) -> FString
```

获得当前关卡名称

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `bRemovePrefixString` | `bool` | 是否移除prefix的字符串 |

**Returns**

| Type | Description |
|---|---|
| `FString` | 关卡名称 |

### `GetGameMode`

```text
GetGameMode(WorldContextObject: UObject *) -> AGameModeBase *
```

获得当前GameMode

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `AGameModeBase *` | 当前GameMode |

### `GetGameState`

```text
GetGameState(WorldContextObject: UObject *) -> AGameStateBase *
```

获得当前GameState

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `AGameStateBase *` | 当前GameState |

### `GetGameStateByWorldContext`

```text
GetGameStateByWorldContext(WorldContextObject: UObject *) -> AGameStateBase *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `AGameStateBase *` | - |

### `GetObjectClass`

```text
GetObjectClass(Object: UObject *) -> UClass *
```

获得对象的类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | 指定对象 |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | 对象的类型 |

### `GetGlobalTimeDilation`

```text
GetGlobalTimeDilation(WorldContextObject: UObject *) -> float
```

获得当前时间膨胀

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | Current time dilation. |

### `SetGlobalTimeDilation`

```text
SetGlobalTimeDilation(WorldContextObject: UObject *, TimeDilation: float) -> void
```

设置时间膨胀

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `TimeDilation` | `float` | 世界的时间膨胀 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGamePaused`

```text
SetGamePaused(WorldContextObject: UObject *, bPaused: bool) -> bool
```

设置游戏是否暂停

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `bPaused` | `bool` | 是否暂停 |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the game was successfully pausedunpaused |

### `IsGamePaused`

```text
IsGamePaused(WorldContextObject: UObject *) -> bool
```

判断游戏是否暂停

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the game is currently paused or not |

### `ApplyRadialDamage`

```text
ApplyRadialDamage(WorldContextObject: UObject *, BaseDamage: float, Origin: FVector &, DamageRadius: float, DamageTypeClass: TSubclassOf < UDamageType >, IgnoreActors: TArray < AActor * > &, DamageCauser: AActor *, InstigatedByController: AController *, bDoFullDamage: bool, DamagePreventionChannel: ECollisionChannel, DamageTag: int32) -> bool
```

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BaseDamage` | `float` | - The base damage to apply, i.e. the damage at the origin. |
| `Origin` | `FVector &` | - Epicenter of the damage area. |
| `DamageRadius` | `float` | - Radius of the damage area, from Origin |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `IgnoreActors` | `TArray < AActor * > &` | - |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded). This actor will not be damaged and it will not block damage. |
| `InstigatedByController` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |
| `bDoFullDamage` | `bool` | - |
| `DamagePreventionChannel` | `ECollisionChannel` | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if damage was applied to at least one actor. |

### `ApplyRadialDamageWithFalloff`

```text
ApplyRadialDamageWithFalloff(WorldContextObject: UObject *, BaseDamage: float, MinimumDamage: float, Origin: FVector &, DamageInnerRadius: float, DamageOuterRadius: float, DamageFalloff: float, DamageTypeClass: TSubclassOf < UDamageType >, IgnoreActors: TArray < AActor * > &, DamageCauser: AActor *, InstigatedByController: AController *, DamagePreventionChannel: ECollisionChannel, DamageTag: int32) -> bool
```

Hurt locally authoritative actors within the radius. Will only hit components that block the Visibility channel.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BaseDamage` | `float` | - The base damage to apply, i.e. the damage at the origin. |
| `MinimumDamage` | `float` | - |
| `Origin` | `FVector &` | - Epicenter of the damage area. |
| `DamageInnerRadius` | `float` | - Radius of the full damage area, from Origin |
| `DamageOuterRadius` | `float` | - Radius of the minimum damage area, from Origin |
| `DamageFalloff` | `float` | - Falloff exponent of damage from DamageInnerRadius to DamageOuterRadius |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `IgnoreActors` | `TArray < AActor * > &` | - |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| `InstigatedByController` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who threw the grenade) |
| `DamagePreventionChannel` | `ECollisionChannel` | - Damage will not be applied to victim if there is something between the origin and the victim which blocks traces on this channel |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if damage was applied to at least one actor. |

### `ApplyPointDamage`

```text
ApplyPointDamage(DamagedActor: AActor *, BaseDamage: float, HitFromDirection: FVector &, HitInfo: FHitResult &, EventInstigator: AController *, DamageCauser: AActor *, DamageTypeClass: TSubclassOf < UDamageType >, DamageTag: int32) -> float
```

Hurts the specified actor with the specified impact.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `AActor *` | - Actor that will be damaged. |
| `BaseDamage` | `float` | - The base damage to apply. |
| `HitFromDirection` | `FVector &` | - Direction the hit came FROM |
| `HitInfo` | `FHitResult &` | - Collision or trace result that describes the hit |
| `EventInstigator` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | Actual damage the ended up being applied to the actor. |

### `ApplyDamage`

```text
ApplyDamage(DamagedActor: AActor *, BaseDamage: float, EventInstigator: AController *, DamageCauser: AActor *, DamageTypeClass: TSubclassOf < UDamageType >, DamageTag: int32) -> float
```

Hurts the specified actor with generic damage.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamagedActor` | `AActor *` | - Actor that will be damaged. |
| `BaseDamage` | `float` | - The base damage to apply. |
| `EventInstigator` | `AController *` | - Controller that was responsible for causing this damage (e.g. player who shot the weapon) |
| `DamageCauser` | `AActor *` | - Actor that actually caused the damage (e.g. the grenade that exploded) |
| `DamageTypeClass` | `TSubclassOf < UDamageType >` | - Class that describes the damage that was done. |
| `DamageTag` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | Actual damage the ended up being applied to the actor. |

### `PlayWorldCameraShake`

```text
PlayWorldCameraShake(WorldContextObject: UObject *, Shake: TSubclassOf < UCameraShake >, Epicenter: FVector, InnerRadius: float, OuterRadius: float, Falloff: float, bOrientShakeTowardsEpicenter: bool) -> void
```

Plays an in-world camera shake that affects all nearby local players, with distance-based attenuation. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - Object that we can obtain a world context from |
| `Shake` | `TSubclassOf < UCameraShake >` | - Camera shake asset to use |
| `Epicenter` | `FVector` | - location to place the effect in world space |
| `InnerRadius` | `float` | - Cameras inside this radius are ignored |
| `OuterRadius` | `float` | - Cameras outside of InnerRadius and inside this are effected |
| `Falloff` | `float` | - Affects falloff of effect as it nears OuterRadius |
| `bOrientShakeTowardsEpicenter` | `bool` | - Changes the rotation of shake to point towards epicenter instead of forward |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnEmitterAtLocation`

```text
SpawnEmitterAtLocation(WorldContextObject: UObject *, EmitterTemplate: UParticleSystem *, Location: FVector, Rotation: FRotator, Scale: FVector, bAutoDestroy: bool) -> UParticleSystemComponent *
```

Plays the specified effect at the given location and rotation, fire and forget. The system will go away when the effect is complete. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - Object that we can obtain a world context from |
| `EmitterTemplate` | `UParticleSystem *` | - particle system to create |
| `Location` | `FVector` | - location to place the effect in world space |
| `Rotation` | `FRotator` | - rotation to place the effect in world space |
| `Scale` | `FVector` | - scale to create the effect at |
| `bAutoDestroy` | `bool` | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent *` | - |

### `SpawnEmitterAttached`

```text
SpawnEmitterAttached(EmitterTemplate: UParticleSystem *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, Scale: FVector, LocationType: EAttachLocation :: Type, bAutoDestroy: bool) -> UParticleSystemComponent *
```

Plays the specified effect attached to and following the specified component. The system will go away when the effect is complete. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterTemplate` | `UParticleSystem *` | - particle system to create |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to spawn the emitter at |
| `Location` | `FVector` | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world location that will be translated to a relative offset (if LocationType is KeepWorldPosition). |
| `Rotation` | `FRotator` | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset (if LocationType is KeepWorldPosition). |
| `Scale` | `FVector` | - Depending on the value of LocationType this is either a relative scale from the attach component or an absolute world scale that will be translated to a relative scale (if LocationType is KeepWorldPosition). |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bAutoDestroy` | `bool` | - Whether the component will automatically be destroyed when the particle system completes playing or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent *` | - |

### `SpawnEmitterAttachedToActor`

```text
SpawnEmitterAttachedToActor(EmitterTemplate: UParticleSystem *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, Scale: FVector, LocationType: EAttachLocation :: Type, bAutoDestroy: bool) -> UParticleSystemComponent *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EmitterTemplate` | `UParticleSystem *` | - |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - |
| `Location` | `FVector` | - |
| `Rotation` | `FRotator` | - |
| `Scale` | `FVector` | - |
| `LocationType` | `EAttachLocation :: Type` | - |
| `bAutoDestroy` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UParticleSystemComponent *` | - |

### `AreAnyListenersWithinRange`

```text
AreAnyListenersWithinRange(WorldContextObject: UObject *, Location: FVector, MaximumRange: float) -> bool
```

Determines if any audio listeners are within range of the specified location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector` | The location to potentially play a sound at |
| `MaximumRange` | `float` | The maximum distance away from Location that a listener can be |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetGlobalPitchModulation`

```text
SetGlobalPitchModulation(WorldContextObject: UObject *, PitchModulation: float, TimeSec: float) -> void
```

Sets a global pitch modulation scalar that will apply to all non-UI sounds
	
	  Fire and Forget.
	  Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PitchModulation` | `float` | - A pitch modulation value to globally set. |
| `TimeSec` | `float` | - A time value to linearly interpolate the global modulation pitch over from it's current value. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetGlobalListenerFocusParameters`

```text
SetGlobalListenerFocusParameters(WorldContextObject: UObject *, FocusAzimuthScale: float, NonFocusAzimuthScale: float, FocusDistanceScale: float, NonFocusDistanceScale: float, FocusVolumeScale: float, NonFocusVolumeScale: float, FocusPriorityScale: float, NonFocusPriorityScale: float) -> void
```

Sets the global listener focus parameters which will scale focus behavior of sounds based on their focus azimuth settings in their attenuation settings.
	
	  Fire and Forget.
	  Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `FocusAzimuthScale` | `float` | - An angle scale value used to scale the azimuth angle that defines where sounds are in-focus. |
| `NonFocusAzimuthScale` | `float` | - |
| `FocusDistanceScale` | `float` | - A distance scale value to use for sounds which are in-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |
| `NonFocusDistanceScale` | `float` | - A distance scale value to use for sounds which are out-of-focus. Values < 1.0 will reduce perceived distance to sounds, values > 1.0 will increase perceived distance to in-focus sounds. |
| `FocusVolumeScale` | `float` | - |
| `NonFocusVolumeScale` | `float` | - |
| `FocusPriorityScale` | `float` | - A priority scale value (> 0.0) to use for sounds which are in-focus. Values < 1.0 will reduce the priority of in-focus sounds, values > 1.0 will increase the priority of in-focus sounds. |
| `NonFocusPriorityScale` | `float` | - A priority scale value (> 0.0) to use for sounds which are out-of-focus. Values < 1.0 will reduce the priority of sounds out-of-focus sounds, values > 1.0 will increase the priority of out-of-focus sounds. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlaySound2D`

```text
PlaySound2D(WorldContextObject: UObject *, Sound: USoundBase *, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: USoundConcurrency *, OwningActor: AActor *) -> void
```

Plays a sound directly with no attenuation, perfect for UI sounds.
	 
	   Fire and Forget.
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - Sound to play. |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `OwningActor` | `AActor *` | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnSound2D`

```text
SpawnSound2D(WorldContextObject: UObject *, Sound: USoundBase *, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: USoundConcurrency *, bPersistAcrossLevelTransition: bool, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a sound with no attenuation, perfect for UI sounds.
	 
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - Sound to play. |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bPersistAcrossLevelTransition` | `bool` | - |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `CreateSound2D`

```text
CreateSound2D(WorldContextObject: UObject *, Sound: USoundBase *, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, ConcurrencySettings: USoundConcurrency *, bPersistAcrossLevelTransition: bool, bAutoDestroy: bool) -> UAudioComponent *
```

Creates a sound with no attenuation, perfect for UI sounds. This does NOT play the sound
	 
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - Sound to create. |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bPersistAcrossLevelTransition` | `bool` | - |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the created sound |

### `PlaySoundAtLocation`

```text
PlaySoundAtLocation(WorldContextObject: UObject *, Sound: USoundBase *, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, ConcurrencySettings: USoundConcurrency *, OwningActor: AActor *) -> void
```

Plays a sound at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - sound to play |
| `Location` | `FVector` | - World position to play sound at |
| `Rotation` | `FRotator` | - World rotation to play sound at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `OwningActor` | `AActor *` | - The actor to use as the "owner" for concurrency settings purposes. Allows PlaySound calls to do a concurrency limit per owner. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnSoundAtLocation`

```text
SpawnSoundAtLocation(WorldContextObject: UObject *, Sound: USoundBase *, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, ConcurrencySettings: USoundConcurrency *, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a sound at the given location. This does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Sound` | `USoundBase *` | - sound to play |
| `Location` | `FVector` | - World position to play sound at |
| `Rotation` | `FRotator` | - World rotation to play sound at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `SpawnSoundAttached`

```text
SpawnSoundAttached(Sound: USoundBase *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, bStopWhenAttachedToDestroyed: bool, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, ConcurrencySettings: USoundConcurrency *, bAutoDestroy: bool) -> UAudioComponent *
```

Plays a sound attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Sound` | `USoundBase *` | - sound to play |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to play the sound at |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bStopWhenAttachedToDestroyed` | `bool` | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the sound to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `ConcurrencySettings` | `USoundConcurrency *` | - Override concurrency settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `PlayDialogue2D`

```text
PlayDialogue2D(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float) -> void
```

Plays a dialogue directly with no attenuation, perfect for UI.
	 
	   Fire and Forget.
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnDialogue2D`

```text
SpawnDialogue2D(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a dialogue with no attenuation, perfect for UI.
	 
	   Not Replicated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `VolumeMultiplier` | `float` | - Multiplied with the volume to make the sound louder or softer. |
| `PitchMultiplier` | `float` | - Multiplies the pitch. |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | An audio component to manipulate the spawned sound |

### `PlayDialogueAtLocation`

```text
PlayDialogueAtLocation(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *) -> void
```

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `Location` | `FVector` | - World position to play dialogue at |
| `Rotation` | `FRotator` | - World rotation to play dialogue at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - Pitch multiplier |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SpawnDialogueAtLocation`

```text
SpawnDialogueAtLocation(WorldContextObject: UObject *, Dialogue: UDialogueWave *, Context: FDialogueContext &, Location: FVector, Rotation: FRotator, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, bAutoDestroy: bool) -> UAudioComponent *
```

Plays a dialogue at the given location. This is a fire and forget sound and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `Location` | `FVector` | - World position to play dialogue at |
| `Rotation` | `FRotator` | - World rotation to play dialogue at |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | Audio Component to manipulate the playing dialogue with |

### `SpawnDialogueAttached`

```text
SpawnDialogueAttached(Dialogue: UDialogueWave *, Context: FDialogueContext &, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, bStopWhenAttachedToDestroyed: bool, VolumeMultiplier: float, PitchMultiplier: float, StartTime: float, AttenuationSettings: USoundAttenuation *, bAutoDestroy: bool) -> UAudioComponent *
```

Spawns a dialogue attached to and following the specified component. This is a fire and forget sound. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Dialogue` | `UDialogueWave *` | - dialogue to play |
| `Context` | `FDialogueContext &` | - context the dialogue is to play in |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to play the sound at |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bStopWhenAttachedToDestroyed` | `bool` | - Specifies whether the sound should stop playing when the owner of the attach to component is destroyed. |
| `VolumeMultiplier` | `float` | - Volume multiplier |
| `PitchMultiplier` | `float` | - PitchMultiplier |
| `StartTime` | `float` | - How far in to the dialogue to begin playback at |
| `AttenuationSettings` | `USoundAttenuation *` | - Override attenuation settings package to play sound with |
| `bAutoDestroy` | `bool` | - Whether the returned audio component will be automatically cleaned up when the sound finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UAudioComponent *` | Audio Component to manipulate the playing dialogue with |

### `SpawnForceFeedbackAtLocation`

```text
SpawnForceFeedbackAtLocation(WorldContextObject: UObject *, ForceFeedbackEffect: UForceFeedbackEffect *, Location: FVector, Rotation: FRotator, bLooping: bool, IntensityMultiplier: float, StartTime: float, AttenuationSettings: UForceFeedbackAttenuation *, bAutoDestroy: bool) -> UForceFeedbackComponent *
```

Plays a force feedback effect at the given location. This is a fire and forget effect and does not travel with any actor. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | - effect to play |
| `Location` | `FVector` | - World position to center the effect at |
| `Rotation` | `FRotator` | - World rotation to center the effect at |
| `bLooping` | `bool` | - |
| `IntensityMultiplier` | `float` | - Intensity multiplier |
| `StartTime` | `float` | - How far in to the feedback effect to begin playback at |
| `AttenuationSettings` | `UForceFeedbackAttenuation *` | - Override attenuation settings package to play effect with |
| `bAutoDestroy` | `bool` | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UForceFeedbackComponent *` | Force Feedback Component to manipulate the playing feedback effect with |

### `SpawnForceFeedbackAttached`

```text
SpawnForceFeedbackAttached(ForceFeedbackEffect: UForceFeedbackEffect *, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, bStopWhenAttachedToDestroyed: bool, bLooping: bool, IntensityMultiplier: float, StartTime: float, AttenuationSettings: UForceFeedbackAttenuation *, bAutoDestroy: bool) -> UForceFeedbackComponent *
```

Plays a force feedback effect attached to and following the specified component. This is a fire and forget effect. Replication is also not handled at this point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ForceFeedbackEffect` | `UForceFeedbackEffect *` | - effect to play |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to attach to |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a relative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `bStopWhenAttachedToDestroyed` | `bool` | - Specifies whether the feedback effect should stop playing when the owner of the attach to component is destroyed. |
| `bLooping` | `bool` | - |
| `IntensityMultiplier` | `float` | - Intensity multiplier |
| `StartTime` | `float` | - How far in to the feedback effect to begin playback at |
| `AttenuationSettings` | `UForceFeedbackAttenuation *` | - Override attenuation settings package to play effect with |
| `bAutoDestroy` | `bool` | - Whether the returned force feedback component will be automatically cleaned up when the feedback patern finishes (by completing or stopping) or whether it can be reactivated |

**Returns**

| Type | Description |
|---|---|
| `UForceFeedbackComponent *` | Force Feedback Component to manipulate the playing feedback effect with |

### `SetSubtitlesEnabled`

```text
SetSubtitlesEnabled(bEnabled: bool) -> void
```

Will set subtitles to be enabled or disabled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | will enable subtitle drawing if true, disable if false. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AreSubtitlesEnabled`

```text
AreSubtitlesEnabled() -> bool
```

Returns whether or not subtitles are currently enabled.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if subtitles are enabled. |

### `SetBaseSoundMix`

```text
SetBaseSoundMix(WorldContextObject: UObject *, InSoundMix: USoundMix *) -> void
```

Set the sound mix of the audio system for special EQing

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMix` | `USoundMix *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSoundMixClassOverride`

```text
SetSoundMixClassOverride(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *, InSoundClass: USoundClass *, Volume: float, Pitch: float, FadeInTime: float, bApplyToChildren: bool) -> void
```

Overrides the sound class adjuster in the given sound mix. If the sound class does not exist in the input sound mix, the sound class adjustment will be added to the sound mix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | The sound mix to modify. |
| `InSoundClass` | `USoundClass *` | The sound class to override (or add) in the sound mix. |
| `Volume` | `float` | The volume scale to set the sound class adjuster to. |
| `Pitch` | `float` | The pitch scale to set the sound class adjuster to. |
| `FadeInTime` | `float` | The interpolation time to use to go from the current sound class adjuster values to the new values. |
| `bApplyToChildren` | `bool` | Whether or not to apply this override to the sound class' children or to just the specified sound class. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSoundMixClassOverride`

```text
ClearSoundMixClassOverride(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *, InSoundClass: USoundClass *, FadeOutTime: float) -> void
```

Clears the override of the sound class adjuster in the given sound mix. If the override did not exist in the sound mix, this will do nothing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | The sound mix to modify. |
| `InSoundClass` | `USoundClass *` | The sound class to override (or add) in the sound mix. |
| `FadeOutTime` | `float` | The interpolation time to use to go from the current sound class adjuster override values to the non-override values. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PushSoundMixModifier`

```text
PushSoundMixModifier(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *) -> void
```

Push a sound mix modifier onto the audio system

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PopSoundMixModifier`

```text
PopSoundMixModifier(WorldContextObject: UObject *, InSoundMixModifier: USoundMix *) -> void
```

Pop a sound mix modifier from the audio system

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InSoundMixModifier` | `USoundMix *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSoundMixModifiers`

```text
ClearSoundMixModifiers(WorldContextObject: UObject *) -> void
```

Clear all sound mix modifiers from the audio system

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ActivateReverbEffect`

```text
ActivateReverbEffect(WorldContextObject: UObject *, ReverbEffect: UReverbEffect *, TagName: FName, Priority: float, Volume: float, FadeTime: float) -> void
```

Activates a Reverb Effect without the need for a volume

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `ReverbEffect` | `UReverbEffect *` | Reverb Effect to use |
| `TagName` | `FName` | Tag to associate with Reverb Effect |
| `Priority` | `float` | Priority of the Reverb Effect |
| `Volume` | `float` | Volume level of Reverb Effect |
| `FadeTime` | `float` | Time before Reverb Effect is fully active |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DeactivateReverbEffect`

```text
DeactivateReverbEffect(WorldContextObject: UObject *, TagName: FName) -> void
```

Deactivates a Reverb Effect not applied by a volume

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TagName` | `FName` | Tag associated with Reverb Effect to remove |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentReverbEffect`

```text
GetCurrentReverbEffect(WorldContextObject: UObject *) -> UReverbEffect *
```

Returns the highest priority reverb settings currently active from any source (volumes or manual setting).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `UReverbEffect *` | - |

### `SpawnDecalAtLocation`

```text
SpawnDecalAtLocation(WorldContextObject: UObject *, DecalMaterial: UMaterialInterface *, DecalSize: FVector, Location: FVector, Rotation: FRotator, LifeSpan: float) -> UDecalComponent *
```

Spawns a decal at the given location and rotation, fire and forget. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `DecalMaterial` | `UMaterialInterface *` | - decal's material |
| `DecalSize` | `FVector` | - size of decal |
| `Location` | `FVector` | - location to place the decal in world space |
| `Rotation` | `FRotator` | - rotation to place the decal in world space |
| `LifeSpan` | `float` | - destroy decal component after time runs out (0 = infinite) |

**Returns**

| Type | Description |
|---|---|
| `UDecalComponent *` | - |

### `SpawnDecalAttached`

```text
SpawnDecalAttached(DecalMaterial: UMaterialInterface *, DecalSize: FVector, AttachToComponent: USceneComponent *, AttachPointName: FName, Location: FVector, Rotation: FRotator, LocationType: EAttachLocation :: Type, LifeSpan: float) -> UDecalComponent *
```

Spawns a decal attached to and following the specified component. Does not replicate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DecalMaterial` | `UMaterialInterface *` | - decal's material |
| `DecalSize` | `FVector` | - size of decal |
| `AttachToComponent` | `USceneComponent *` | - |
| `AttachPointName` | `FName` | - Optional named point within the AttachComponent to spawn the emitter at |
| `Location` | `FVector` | - Depending on the value of Location Type this is either a relative offset from the attach componentpoint or an absolute world position that will be translated to a relative offset |
| `Rotation` | `FRotator` | - Depending on the value of LocationType this is either a relative offset from the attach componentpoint or an absolute world rotation that will be translated to a realative offset |
| `LocationType` | `EAttachLocation :: Type` | - Specifies whether Location is a relative offset or an absolute world position |
| `LifeSpan` | `float` | - destroy decal component after time runs out (0 = infinite) |

**Returns**

| Type | Description |
|---|---|
| `UDecalComponent *` | - |

### `BreakHitResult`

```text
BreakHitResult(Hit: FHitResult &, bBlockingHit: bool &, bInitialOverlap: bool &, Time: float &, Distance: float &, Location: FVector &, ImpactPoint: FVector &, Normal: FVector &, ImpactNormal: FVector &, PhysMat: UPhysicalMaterial * &, HitActor: AActor * &, HitComponent: UPrimitiveComponent * &, HitBoneName: FName &, HitItem: int32 &, FaceIndex: int32 &, TraceStart: FVector &, TraceEnd: FVector &) -> void
```

Extracts data from a HitResult.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | The source HitResult. |
| `bBlockingHit` | `bool &` | True if there was a blocking hit, false otherwise. |
| `bInitialOverlap` | `bool &` | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |
| `Time` | `float &` | 'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |
| `Distance` | `float &` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| `Location` | `FVector &` | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. |
| `ImpactPoint` | `FVector &` | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. |
| `Normal` | `FVector &` | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. |
| `ImpactNormal` | `FVector &` | Normal of the hit in world space, for the object that was hit by the sweep. |
| `PhysMat` | `UPhysicalMaterial * &` | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |
| `HitActor` | `AActor * &` | Actor hit by the trace. |
| `HitComponent` | `UPrimitiveComponent * &` | PrimitiveComponent hit by the trace. |
| `HitBoneName` | `FName &` | Name of the bone hit (valid only if we hit a skeletal mesh). |
| `HitItem` | `int32 &` | Primitive-specific data recording which item in the primitive was hit |
| `FaceIndex` | `int32 &` | If colliding with trimesh or landscape, index of face that was hit. |
| `TraceStart` | `FVector &` | - |
| `TraceEnd` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeHitResult`

```text
MakeHitResult(bBlockingHit: bool, bInitialOverlap: bool, Time: float, Distance: float, Location: FVector, ImpactPoint: FVector, Normal: FVector, ImpactNormal: FVector, PhysMat: UPhysicalMaterial *, HitActor: AActor *, HitComponent: UPrimitiveComponent *, HitBoneName: FName, HitItem: int32, FaceIndex: int32, TraceStart: FVector, TraceEnd: FVector) -> FHitResult
```

Create a HitResult struct

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bBlockingHit` | `bool` | True if there was a blocking hit, false otherwise. |
| `bInitialOverlap` | `bool` | True if the hit started in an initial overlap. In this case some other values should be interpreted differently. Time will be 0, ImpactPoint will equal Location, and normals will be equal and indicate a depenetration vector. |
| `Time` | `float` | 'Time' of impact along trace direction ranging from [0.0 to 1.0) if there is a hit, indicating time between start and end. Equals 1.0 if there is no hit. |
| `Distance` | `float` | The distance from the TraceStart to the Location in world space. This value is 0 if there was an initial overlap (trace started inside another colliding object). |
| `Location` | `FVector` | Location of the hit in world space. If this was a swept shape test, this is the location where we can place the shape in the world where it will not penetrate. |
| `ImpactPoint` | `FVector` | Location of the actual contact point of the trace shape with the surface of the hit object. Equal to Location in the case of an initial overlap. |
| `Normal` | `FVector` | Normal of the hit in world space, for the object that was swept (e.g. for a sphere trace this points towards the sphere's center). Equal to ImpactNormal for line tests. |
| `ImpactNormal` | `FVector` | Normal of the hit in world space, for the object that was hit by the sweep. |
| `PhysMat` | `UPhysicalMaterial *` | Physical material that was hit. Must set bReturnPhysicalMaterial to true in the query params for this to be returned. |
| `HitActor` | `AActor *` | Actor hit by the trace. |
| `HitComponent` | `UPrimitiveComponent *` | PrimitiveComponent hit by the trace. |
| `HitBoneName` | `FName` | Name of the bone hit (valid only if we hit a skeletal mesh). |
| `HitItem` | `int32` | Primitive-specific data recording which item in the primitive was hit |
| `FaceIndex` | `int32` | If colliding with trimesh or landscape, index of face that was hit. |
| `TraceStart` | `FVector` | - |
| `TraceEnd` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | - |

### `GetSurfaceType`

```text
GetSurfaceType(Hit: FHitResult &) -> EPhysicalSurface
```

Returns the EPhysicalSurface type of the given Hit.
	  To edit surface type for your project, use ProjectSettingsPhysicsPhysicalSurface section

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `EPhysicalSurface` | - |

### `FindCollisionUV`

```text
FindCollisionUV(Hit: FHitResult &, UVChannel: int32, UV: FVector2D &) -> bool
```

Try and find the UV for a collision impact. Note this ONLY works if 'Support UV From Hit Results' is enabled in Physics Settings.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |
| `UVChannel` | `int32` | - |
| `UV` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CreateSaveGameObject`

```text
CreateSaveGameObject(SaveGameClass: TSubclassOf < USaveGame >) -> USaveGame *
```

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SaveGameClass` | `TSubclassOf < USaveGame >` | Class of SaveGame to create |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | New SaveGame object to write data to |

### `CreateSaveGameObjectFromBlueprint`

```text
CreateSaveGameObjectFromBlueprint(SaveGameBlueprint: UBlueprint *) -> USaveGame *
```

Create a new, empty SaveGame object to set data on and then pass to SaveGameToSlot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SaveGameBlueprint` | `UBlueprint *` | Blueprint of SaveGame to create |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | New SaveGame object to write data to |

### `SaveGameToSlot`

```text
SaveGameToSlot(SaveGameObject: USaveGame *, SlotName: FString &, UserIndex: int32) -> bool
```

Save the contents of the SaveGameObject to a slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SaveGameObject` | `USaveGame *` | Object that contains data about the save game that we want to write out |
| `SlotName` | `FString &` | Name of save game slot to save to. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the saving. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether we successfully saved this information |

### `DoesSaveGameExist`

```text
DoesSaveGameExist(SlotName: FString &, UserIndex: int32) -> bool
```

See if a save game exists with the specified name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of save game slot. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the saving. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BindLoadGameGuardEntranceCheckDelegate`

```text
BindLoadGameGuardEntranceCheckDelegate(Obj: UObject *, FuncName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Obj` | `UObject *` | - |
| `FuncName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindLoadGameGuardExitCheckDelegate`

```text
BindLoadGameGuardExitCheckDelegate(Obj: UObject *, FuncName: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Obj` | `UObject *` | - |
| `FuncName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LoadGameFromSlot`

```text
LoadGameFromSlot(SlotName: FString &, UserIndex: int32) -> USaveGame *
```

Load the contents from a given slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of the save game slot to load from. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the loading. |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | SaveGameObject	Object containing loaded game state (NULL if load fails) |

### `LoadGameFromSlotWithSizeLimit`

```text
LoadGameFromSlotWithSizeLimit(SlotName: FString &, UserIndex: int32, MaxSerSize: int32) -> USaveGame *
```

Load the contents from a given slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of the save game slot to load from. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the loading. |
| `MaxSerSize` | `int32` | Specify the maxserializesize of archive, just working for fstring. |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | SaveGameObject	Object containing loaded game state (NULL if load fails) |

### `LoadGameFromMemory`

```text
LoadGameFromMemory(ObjectBytes: TArray < uint8 > &, MaxSerSize: int32) -> USaveGame *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectBytes` | `TArray < uint8 > &` | - |
| `MaxSerSize` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | - |

### `LoadGameFromMemoryWithSizeLimit`

```text
LoadGameFromMemoryWithSizeLimit(ObjectBytes: TArray < uint8 > &, MaxSerSize: int32) -> USaveGame *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectBytes` | `TArray < uint8 > &` | - |
| `MaxSerSize` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `USaveGame *` | - |

### `DeleteGameInSlot`

```text
DeleteGameInSlot(SlotName: FString &, UserIndex: int32) -> bool
```

Delete a save game in a particular slot.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotName` | `FString &` | Name of save game slot to delete. |
| `UserIndex` | `int32` | For some platforms, master user index to identify the user doing the deletion. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if a file was actually able to be deleted. use DoesSaveGameExist to distinguish between delete failures and failure due to file not existing. |

### `GetWorldDeltaSeconds`

```text
GetWorldDeltaSeconds(WorldContextObject: UObject *) -> float
```

获得当前每帧的delta time，单位秒

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 每帧的delta time |

### `GetTimeSeconds`

```text
GetTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的时间，单位秒，受时间膨胀和游戏暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetUnpausedTimeSeconds`

```text
GetUnpausedTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的时间，单位秒，受时间膨胀影响，但不受游戏暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetRealTimeSeconds`

```text
GetRealTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的真实时间，单位秒，不受时间膨胀和游戏暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetAudioTimeSeconds`

```text
GetAudioTimeSeconds(WorldContextObject: UObject *) -> float
```

获得当前游戏开始之后的时间，单位秒，不受时间膨胀影响，但受时间暂停影响

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `float` | 游戏时间 |

### `GetAccurateRealTime`

```text
GetAccurateRealTime(WorldContextObject: UObject *, Seconds: int32 &, PartialSeconds: float &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Seconds` | `int32 &` | - |
| `PartialSeconds` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableLiveStreaming`

```text
EnableLiveStreaming(Enable: bool) -> void
```

~ DVRStreaming API 
	
	  Toggle live DVR streaming.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enable` | `bool` | If true enable streaming, otherwise disable. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPlatformName`

```text
GetPlatformName() -> FString
```

Returns the string name of the current platform, to perform different behavior based on platform.
	  (Platform names include Windows, Mac, IOS, Android, PS4, XboxOne, HTML5, Linux)

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `BlueprintSuggestProjectileVelocity`

```text
BlueprintSuggestProjectileVelocity(WorldContextObject: UObject *, TossVelocity: FVector &, StartLocation: FVector, EndLocation: FVector, LaunchSpeed: float, OverrideGravityZ: float, TraceOption: ESuggestProjVelocityTraceOption :: Type, CollisionRadius: float, bFavorHighArc: bool, bDrawDebug: bool) -> bool
```

Calculates an launch velocity for a projectile to hit a specified point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TossVelocity` | `FVector &` | (output) Result launch velocity. |
| `StartLocation` | `FVector` | Intended launch location |
| `EndLocation` | `FVector` | Desired landing location |
| `LaunchSpeed` | `float` | Desired launch speed |
| `OverrideGravityZ` | `float` | Optional gravity override. 0 means "do not override". |
| `TraceOption` | `ESuggestProjVelocityTraceOption :: Type` | Controls whether or not to validate a clear path by tracing along the calculated arc |
| `CollisionRadius` | `float` | Radius of the projectile (assumed spherical), used when tracing |
| `bFavorHighArc` | `bool` | If true and there are 2 valid solutions, will return the higher arc. If false, will favor the lower arc. |
| `bDrawDebug` | `bool` | When true, a debug arc is drawn (red for an invalid arc, green for a valid arc) |

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns false if there is no valid solution or the valid solutions are blocked.  Returns true otherwise. |

### `Blueprint_PredictProjectilePath_ByObjectType`

```text
Blueprint_PredictProjectilePath_ByObjectType(WorldContextObject: UObject *, OutHit: FHitResult &, OutPathPositions: TArray < FVector > &, OutLastTraceDestination: FVector &, StartPos: FVector, LaunchVelocity: FVector, bTracePath: bool, ProjectileRadius: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, DrawDebugTime: float, SimFrequency: float, MaxSimTime: float, OverrideGravityZ: float) -> bool
```

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `OutHit` | `FHitResult &` | Predicted hit result, if the projectile will hit something |
| `OutPathPositions` | `TArray < FVector > &` | Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |
| `OutLastTraceDestination` | `FVector &` | Goal position of the final trace it did. Will not be in the path if there is a hit. |
| `StartPos` | `FVector` | First start trace location |
| `LaunchVelocity` | `FVector` | Velocity the "virtual projectile" is launched at |
| `bTracePath` | `bool` | Trace along the entire path to look for blocking hits |
| `ProjectileRadius` | `float` | Radius of the virtual projectile to sweep against the environment |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | ObjectTypes to trace against, if bTracePath is true. |
| `bTraceComplex` | `bool` | Use TraceComplex (trace against triangles not primitives) |
| `ActorsToIgnore` | `TArray < AActor * > &` | Actors to exclude from the traces |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | Debug type (one-frame, duration, persistent) |
| `DrawDebugTime` | `float` | Duration of debug lines (only relevant for DrawDebugType::Duration) |
| `SimFrequency` | `float` | Determines size of each sub-step in the simulation (chopping up MaxSimTime) |
| `MaxSimTime` | `float` | Maximum simulation time for the virtual projectile. |
| `OverrideGravityZ` | `float` | Optional override of Gravity (if 0, uses WorldGravityZ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if hit something along the path if tracing for collision. |

### `Blueprint_PredictProjectilePath_ByTraceChannel`

```text
Blueprint_PredictProjectilePath_ByTraceChannel(WorldContextObject: UObject *, OutHit: FHitResult &, OutPathPositions: TArray < FVector > &, OutLastTraceDestination: FVector &, StartPos: FVector, LaunchVelocity: FVector, bTracePath: bool, ProjectileRadius: float, TraceChannel: TEnumAsByte < ECollisionChannel >, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, DrawDebugTime: float, SimFrequency: float, MaxSimTime: float, OverrideGravityZ: float) -> bool
```

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc. Returns a list of positions of the simulated arc and the destination reached by the simulation.
	 Returns true if it hit something (if tracing with collision).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `OutHit` | `FHitResult &` | Predicted hit result, if the projectile will hit something |
| `OutPathPositions` | `TArray < FVector > &` | Predicted projectile path. Ordered series of positions from StartPos to the end. Includes location at point of impact if it hit something. |
| `OutLastTraceDestination` | `FVector &` | Goal position of the final trace it did. Will not be in the path if there is a hit. |
| `StartPos` | `FVector` | First start trace location |
| `LaunchVelocity` | `FVector` | Velocity the "virtual projectile" is launched at |
| `bTracePath` | `bool` | Trace along the entire path to look for blocking hits |
| `ProjectileRadius` | `float` | Radius of the virtual projectile to sweep against the environment |
| `TraceChannel` | `TEnumAsByte < ECollisionChannel >` | TraceChannel to trace against, if bTracePath is true. |
| `bTraceComplex` | `bool` | Use TraceComplex (trace against triangles not primitives) |
| `ActorsToIgnore` | `TArray < AActor * > &` | Actors to exclude from the traces |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | Debug type (one-frame, duration, persistent) |
| `DrawDebugTime` | `float` | Duration of debug lines (only relevant for DrawDebugType::Duration) |
| `SimFrequency` | `float` | Determines size of each sub-step in the simulation (chopping up MaxSimTime) |
| `MaxSimTime` | `float` | Maximum simulation time for the virtual projectile. |
| `OverrideGravityZ` | `float` | Optional override of Gravity (if 0, uses WorldGravityZ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if hit something along the path (if tracing with collision). |

### `Blueprint_PredictProjectilePath_Advanced`

```text
Blueprint_PredictProjectilePath_Advanced(WorldContextObject: UObject *, PredictParams: FPredictProjectilePathParams &, PredictResult: FPredictProjectilePathResult &) -> bool
```

Predict the arc of a virtual projectile affected by gravity with collision checks along the arc.
	 Returns true if it hit something.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PredictParams` | `FPredictProjectilePathParams &` | Input params to the trace (start location, velocity, time to simulate, etc). |
| `PredictResult` | `FPredictProjectilePathResult &` | Output result of the trace (Hit result, array of locationvelocitytimes for each trace step, etc). |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if hit something along the path (if tracing with collision). |

### `SuggestProjectileVelocity_CustomArc`

```text
SuggestProjectileVelocity_CustomArc(WorldContextObject: UObject *, OutLaunchVelocity: FVector &, StartPos: FVector, EndPos: FVector, OverrideGravityZ: float, ArcParam: float) -> bool
```

Returns the launch velocity needed for a projectile at rest at StartPos to land on EndPos.
	 Assumes a medium arc (e.g. 45 deg on level ground). Projectile velocity is variable and unconstrained.
	 Does no tracing.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `OutLaunchVelocity` | `FVector &` | Returns the launch velocity required to reach the EndPos |
| `StartPos` | `FVector` | Start position of the simulation |
| `EndPos` | `FVector` | Desired end location for the simulation |
| `OverrideGravityZ` | `float` | Optional override of WorldGravityZ |
| `ArcParam` | `float` | Change height of arc between 0.0-1.0 where 0.5 is the default medium arc |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetWorldOriginLocation`

```text
GetWorldOriginLocation(WorldContextObject: UObject *) -> FIntVector
```

获取世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `FIntVector` | 世界原点 |

### `SetWorldOriginLocation`

```text
SetWorldOriginLocation(WorldContextObject: UObject *, NewLocation: FIntVector) -> void
```

设置世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `NewLocation` | `FIntVector` | 世界原点 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWorldOriginLocationByLua`

```text
SetWorldOriginLocationByLua(WorldContextObject: UObject *, X: int32, Y: int32, Z: int32) -> void
```

设置世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Z` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SyncSetNewWorldOrigin`

```text
SyncSetNewWorldOrigin(WorldContextObject: UObject *, X: int32, Y: int32, Z: int32) -> void
```

同步设置世界原点位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `X` | `int32` | - |
| `Y` | `int32` | - |
| `Z` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RebaseLocalOriginOntoZero`

```text
RebaseLocalOriginOntoZero(WorldContextObject: UObject *, WorldLocation: FVector) -> FVector
```

返回基于原点坐标的local坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `WorldLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | origin based position |

### `RebaseZeroOriginOntoLocal`

```text
RebaseZeroOriginOntoLocal(WorldContextObject: UObject *, WorldLocation: FVector) -> FVector
```

返回local坐标基于原点的坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `WorldLocation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | local location |

### `GrassOverlappingSphereCount`

```text
GrassOverlappingSphereCount(WorldContextObject: UObject *, StaticMesh: UStaticMesh *, CenterPosition: FVector, Radius: float) -> int32
```

Counts how many grass foliage instances overlap a given sphere.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `StaticMesh` | `UStaticMesh *` | - |
| `CenterPosition` | `FVector` | The center position of the sphere. |
| `Radius` | `float` | The radius of the sphere. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of foliage instances with their mesh set to Mesh that overlap the sphere. |

### `DeprojectScreenToWorld`

```text
DeprojectScreenToWorld(Player: APlayerController *, ScreenPosition: FVector2D &, WorldPosition: FVector &, WorldDirection: FVector &) -> bool
```

获取给定2D屏幕空间中的坐标投影到3D世界空间中的坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | 玩家的PlayerController |
| `ScreenPosition` | `FVector2D &` | 屏幕空间中的坐标 |
| `WorldPosition` | `FVector &` | 输出的世界空间坐标 |
| `WorldDirection` | `FVector &` | 输出的方向向量，世界空间中，给定点远离相机方向的方向向量 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否转换成功 |

### `ProjectWorldToScreen`

```text
ProjectWorldToScreen(Player: APlayerController *, WorldPosition: FVector &, ScreenPosition: FVector2D &, bPlayerViewportRelative: bool) -> bool
```

获取给定3D世界空间中的坐标投影到2D屏幕空间中的坐标

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `APlayerController *` | 玩家的PlayerController |
| `WorldPosition` | `FVector &` | 世界空间中的坐标 |
| `ScreenPosition` | `FVector2D &` | 输出的屏幕空间坐标 |
| `bPlayerViewportRelative` | `bool` | 是否与玩家视口相关 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否转换成功 |

### `MarkNetPropertyDirtyFromName`

```text
MarkNetPropertyDirtyFromName(Object: UObject *, PropertyName: FName, LifetimeCondition: ELifetimeCondition) -> bool
```

Mark a particular net property of an UObject as dirty (for networking), thus it will be take into consideration in next replication

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | UObject to be marked dirty |
| `PropertyName` | `FName` | Name of the particular net property to be marked dirty |
| `LifetimeCondition` | `ELifetimeCondition` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetKeyValue`

```text
GetKeyValue(Pair: FString &, Key: FString &, Value: FString &) -> void
```

Break up a key=value pair into its key and value.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pair` | `FString &` | The string containing a pair to split apart. |
| `Key` | `FString &` | (out) Key portion of Pair. If no = in string will be the same as Pair. |
| `Value` | `FString &` | (out) Value portion of Pair. If no = in string will be empty. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ParseOption`

```text
ParseOption(Options: FString, Key: FString &) -> FString
```

Find an option in the options string and return it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Options` | `FString` | The string containing the options. |
| `Key` | `FString &` | The key to find the value of in Options. |

**Returns**

| Type | Description |
|---|---|
| `FString` | The value associated with Key if Key found in Options string. |

### `HasOption`

```text
HasOption(Options: FString, InKey: FString &) -> bool
```

Returns whether a key exists in an options string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Options` | `FString` | The string containing the options. |
| `InKey` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether Key was found in Options. |

### `GetIntOption`

```text
GetIntOption(Options: FString &, Key: FString &, DefaultValue: int32) -> int32
```

Find an option in the options string and return it as an integer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Options` | `FString &` | The string containing the options. |
| `Key` | `FString &` | The key to find the value of in Options. |
| `DefaultValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The value associated with Key as an integer if Key found in Options string, otherwise DefaultValue. |

### `HasLaunchOption`

```text
HasLaunchOption(OptionToCheck: FString &) -> bool
```

Checks the commandline to see if the desired option was specified on the commandline (e.g. -demobuild)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OptionToCheck` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the launch option was specified on the commandline, false otherwise |

### `GetDeviceQualityLevel`

```text
GetDeviceQualityLevel() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDeviceTCQualityGrade`

```text
GetDeviceTCQualityGrade() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDeviceMemoryLevel`

```text
GetDeviceMemoryLevel() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDeviceMemorySize`

```text
GetDeviceMemorySize() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `EnableObjArrayAutoResize`

```text
EnableObjArrayAutoResize(bEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConsoleIntVariable`

```text
SetConsoleIntVariable(Name: FString &, Value: int32) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FString &` | - |
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateComponentToWorld`

```text
UpdateComponentToWorld(ActorComponent: UActorComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorComponent` | `UActorComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsLongScreen`

```text
IsLongScreen(WorldContextObject: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsWinReleaseBuild`

```text
IsWinReleaseBuild() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RecordDSLaunchState`

```text
RecordDSLaunchState(state: int32) -> void
```

record ds launch state, collect for ds shutdown error report, add by czcheng

**Parameters**

| Name | Type | Description |
|---|---|---|
| `state` | `int32` | launch state, see details in EDSLaunchState |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecordDSShutdownErrorInfo`

```text
RecordDSShutdownErrorInfo(ErrorCode: int32, ErrMsg: FString &) -> void
```

record ds shutdown error info, collect for ds shutdown error report, add by czcheng

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ErrorCode` | `int32` | shutdown error code, see details in EDSShutdownErrorCode |
| `ErrMsg` | `FString &` | error message |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTagsDeveloperSettings.json -->

# UGameplayTagsDeveloperSettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DeveloperConfigName` | `FString` | Allows new tags to be saved into their own INI file. This is make merging easier for non technical developers by setting up their own ini file. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTagsList.json -->

# UGameplayTagsList

Base class for storing a list of gameplay tags as an ini list. This is used for both the central list and additional lists

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConfigFileName` | `FString` | Relative path to the ini file that is backing this list |
| `GameplayTagList` | `TArray < FGameplayTagTableRow >` | List of tags saved to this file |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTagsManager.json -->

# UGameplayTagsManager

Holds data about the tag dictionary, is in a singleton UObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TagSources` | `TArray < FGameplayTagSource >` | List of gameplay tag sources |
| `GameplayTagTables` | `TArray < UDataTable * >` | Holds all of the valid gameplay-related tags that can be applied to assets |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTagsSettings.json -->

# UGameplayTagsSettings

Class for importing GameplayTags directly from a config file.
 	FGameplayTagsEditorModule::StartupModule adds this class to the Project Settings menu to be edited.
 	Editing this in Project Settings will output changes to ConfigDefaultGameplayTags.ini.
 	
 	Primary advantages of this approach are:
 	-Adding new tags doesn't require checking out external and editing file (CSV or xls) then reimporting.
 	-New tags are mergeable since .ini are text and non exclusive checkout.
 	
 	To do:
 	-Better support could be added for adding new tags. We could match existing tags and autocomplete subtags as
 	the user types (e.g, autocomplete 'Damage.Physical' as the user is adding a 'Damage.Physical.Slash' tag).

## Inheritance

`UGameplayTagsList`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImportTagsFromConfig` | `bool` | If true, will import tags from ini files in the configtags folder |
| `WarnOnInvalidTags` | `bool` | If true, will give load warnings when reading invalid tags off disk |
| `InvalidTagCharacters` | `FString` | These characters cannot be used in gameplay tags, in addition to special ones like newline |
| `CategoryRemapping` | `TArray < FGameplayTagCategoryRemap >` | - |
| `FastReplication` | `bool` | If true, will replicate gameplay tags by index instead of name. For this to work, tags must be identical on client and server |
| `GameplayTagTableList` | `TArray < FSoftObjectPath >` | List of data tables to load tags from |
| `GameplayTagRedirects` | `TArray < FGameplayTagRedirect >` | List of active tag redirects |
| `CommonlyReplicatedTags` | `TArray < FName >` | List of tags most frequently replicated |
| `NumBitsForContainerSize` | `int32` | Numbers of bits to use for replicating container size, set this based on how large your containers tend to be |
| `NetIndexFirstBitSegment` | `int32` | The length in bits of the first segment when net serializing tags. We will serialize NetIndexFirstBitSegment + 1 bit to indicate "more", which is slower to replicate |
| `GameplayTagDontNeedFastReplicationList` | `TArray < FName >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask.json -->

# UGameplayTask

## Inheritance

`UObject` -> `IGameplayTaskOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceName` | `FName` | This name allows us to find the task later so that we can end it. |
| `ResourceOverlapPolicy` | `ETaskResourceOverlapPolicy` | - |
| `ChildTask` | `UGameplayTask *` | child task instance |

## Functions

### `ReadyForActivation`

```text
ReadyForActivation() -> void
```

Called to trigger the actual task once the delegates have been set up

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EndTask`

```text
EndTask() -> void
```

Called explicitly to end the task (usually by the task itself). Calls OnDestroy.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_ClaimResource.json -->

# UGameplayTask_ClaimResource

## Inheritance

`UGameplayTask`

## Functions

### `ClaimResource`

```text
ClaimResource(InTaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, ResourceClass: TSubclassOf < UGameplayTaskResource >, Priority: uint8, TaskInstanceName: FName) -> UGameplayTask_ClaimResource *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `ResourceClass` | `TSubclassOf < UGameplayTaskResource >` | - |
| `Priority` | `uint8` | - |
| `TaskInstanceName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_ClaimResource *` | - |

### `ClaimResources`

```text
ClaimResources(InTaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, ResourceClasses: TArray < TSubclassOf < UGameplayTaskResource > >, Priority: uint8, TaskInstanceName: FName) -> UGameplayTask_ClaimResource *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `ResourceClasses` | `TArray < TSubclassOf < UGameplayTaskResource > >` | - |
| `Priority` | `uint8` | - |
| `TaskInstanceName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_ClaimResource *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_SpawnActor.json -->

# UGameplayTask_SpawnActor

Convenience task for spawning actors (optionally limiting the spawning to the network authority). If not the net authority, we will not spawn 
 	and Success will not be called. The nice thing this adds is the ability to modify expose on spawn properties while also implicitly checking 
 	network role before spawning.
 
 	Though this task doesn't do much - games can implement similar tasks that carry out game specific rules. For example a 'SpawnProjectile'
 	task that limits the available classes to the games projectile class, and that does game specific stuff on spawn (for example, determining
 	firing position from a weapon attachment).
 	
 	Long term we can also use this task as a sync point. If the executing client could wait execution until the server creates and replicates the 
 	actor down to him. We could potentially also use this to do predictive actor spawning  reconciliation.

## Inheritance

`UGameplayTask`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClassToSpawn` | `TSubclassOf < AActor >` | - |

## Functions

### `SpawnActor`

```text
SpawnActor(TaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, SpawnLocation: FVector, SpawnRotation: FRotator, Class: TSubclassOf < AActor >, bSpawnOnlyOnAuthority: bool) -> UGameplayTask_SpawnActor *
```

Spawn new Actor on the network authority (server)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `SpawnLocation` | `FVector` | - |
| `SpawnRotation` | `FRotator` | - |
| `Class` | `TSubclassOf < AActor >` | - |
| `bSpawnOnlyOnAuthority` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_SpawnActor *` | - |

### `BeginSpawningActor`

```text
BeginSpawningActor(WorldContextObject: UObject *, SpawnedActor: AActor * &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SpawnedActor` | `AActor * &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FinishSpawningActor`

```text
FinishSpawningActor(WorldContextObject: UObject *, SpawnedActor: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SpawnedActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `Success`

```text
Success(SpawnedActor: AActor*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpawnedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DidNotSpawn`

```text
DidNotSpawn(SpawnedActor: AActor*) -> void
```

Called when we can't spawn: on clients or potentially on server if they fail to spawn (rare)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpawnedActor` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_TimeLimitedExecution.json -->

# UGameplayTask_TimeLimitedExecution

Adds time limit for running a child task
  - child task needs to be created with UGameplayTask_TimeLimitedExecution passed as TaskOwner 
  - activations are tied together and when either UGameplayTask_TimeLimitedExecution or child task is activated, other one starts as well
  - OnFinished and OnTimeExpired are mutually exclusive

## Inheritance

`UGameplayTask`

## Delegates

### `OnFinished`

```text
OnFinished() -> void
```

called when child task finishes execution before time runs out

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTimeExpired`

```text
OnTimeExpired() -> void
```

called when time runs out

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_WaitDelay.json -->

# UGameplayTask_WaitDelay

## Inheritance

`UGameplayTask`

## Functions

### `TaskWaitDelay`

```text
TaskWaitDelay(TaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, Time: float, Priority: uint8) -> UGameplayTask_WaitDelay *
```

Wait specified time. This is functionally the same as a standard Delay node.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `Time` | `float` | - |
| `Priority` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_WaitDelay *` | - |

## Delegates

### `OnFinish`

```text
OnFinish() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTaskResource.json -->

# UGameplayTaskResource

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ManualResourceID` | `int32` | Overrides AutoResourceID. -1 means auto ID will be applied |
| `AutoResourceID` | `int8` | - |
| `bManuallySetID` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameplayTasksComponent.json -->

# UGameplayTasksComponent

The core ActorComponent for interfacing with the GameplayAbilities System

## Inheritance

`UActorComponent` -> `IGameplayTaskOwnerInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SimulatedTasks` | `TArray < UGameplayTask * >` | Tasks that run on simulated proxies |
| `AutonomousTasks` | `TArray < UGameplayTask * >` | - |
| `TaskPriorityQueue` | `TArray < UGameplayTask * >` | - |
| `TickingTasks` | `TArray < UGameplayTask * >` | Array of currently active UGameplayTask that require ticking |
| `KnownTasks` | `TArray < UGameplayTask * >` | All known tasks (processed by this component) referenced for GC |

## Functions

### `OnRep_SimulatedTasks`

```text
OnRep_SimulatedTasks() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_AutonomousTasks`

```text
OnRep_AutonomousTasks() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_RunGameplayTask`

```text
K2_RunGameplayTask(TaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, Task: UGameplayTask *, Priority: uint8, AdditionalRequiredResources: TArray < TSubclassOf < UGameplayTaskResource > >, AdditionalClaimedResources: TArray < TSubclassOf < UGameplayTaskResource > >) -> EGameplayTaskRunResult
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `Task` | `UGameplayTask *` | - |
| `Priority` | `uint8` | - |
| `AdditionalRequiredResources` | `TArray < TSubclassOf < UGameplayTaskResource > >` | - |
| `AdditionalClaimedResources` | `TArray < TSubclassOf < UGameplayTaskResource > >` | - |

**Returns**

| Type | Description |
|---|---|
| `EGameplayTaskRunResult` | - |

## Delegates

### `OnClaimedResourcesChange`

```text
OnClaimedResourcesChange(NewlyClaimed: FGameplayResourceSet, FreshlyReleased: FGameplayResourceSet) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewlyClaimed` | `FGameplayResourceSet` | - |
| `FreshlyReleased` | `FGameplayResourceSet` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameSessionSettings.json -->

# UGameSessionSettings

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxSpectators` | `int32` | Maximum number of spectators allowed by this server. |
| `MaxPlayers` | `int32` | Maximum number of players allowed by this server. |
| `bRequiresPushToTalk` | `uint32` | Is voice enabled always or via a push to talk key binding. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameUserSettings.json -->

# UGameUserSettings

Stores user settings for a game (for example graphics and sound settings), with the ability to save and load to and from a file.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseVSync` | `bool` | Whether to use VSync or not. (public to allow UI to connect to it) |
| `ResolutionSizeX` | `uint32` | Game screen resolution width, in pixels. |
| `ResolutionSizeY` | `uint32` | Game screen resolution height, in pixels. |
| `LastUserConfirmedResolutionSizeX` | `uint32` | Game screen resolution width, in pixels. |
| `LastUserConfirmedResolutionSizeY` | `uint32` | Game screen resolution height, in pixels. |
| `IsBorderless` | `bool` | Is game window borderless added by windzjliu |
| `BorderlessMode` | `int32` | - |
| `WindowPosX` | `int32` | Window PosX |
| `WindowPosY` | `int32` | Window PosY |
| `FullscreenMode` | `int32` | Game window fullscreen mode<br>	 	0 = Fullscreen<br>	 	1 = Windowed fullscreen<br>	 	2 = Windowed |
| `LastConfirmedFullscreenMode` | `int32` | Last user confirmed fullscreen mode setting. |
| `PreferredFullscreenMode` | `int32` | Fullscreen mode to use when toggling between windowed and fullscreen. Same values as r.FullScreenMode. |
| `Version` | `uint32` | All settings will be wiped and set to default if the serialized version differs from UE_GAMEUSERSETTINGS_VERSION. |
| `AudioQualityLevel` | `int32` | - |
| `FrameRateLimit` | `float` | Frame rate cap |
| `DesiredScreenWidth` | `int32` | Desired screen width used to calculate the resolution scale when user changes display mode |
| `bUseDesiredScreenHeight` | `bool` | If true, the desired screen height will be used to scale the render resolution automatically. |
| `DesiredScreenHeight` | `int32` | Desired screen height used to calculate the resolution scale when user changes display mode |
| `LastRecommendedScreenWidth` | `float` | Result of the last benchmark; calculated resolution to use. |
| `LastRecommendedScreenHeight` | `float` | Result of the last benchmark; calculated resolution to use. |
| `LastCPUBenchmarkResult` | `float` | Result of the last benchmark (CPU); -1 if there has not been a benchmark run |
| `LastGPUBenchmarkResult` | `float` | Result of the last benchmark (GPU); -1 if there has not been a benchmark run |
| `LastCPUBenchmarkSteps` | `TArray < float >` | Result of each individual sub-section of the last CPU benchmark; empty if there has not been a benchmark run |
| `LastGPUBenchmarkSteps` | `TArray < float >` | Result of each individual sub-section of the last GPU benchmark; empty if there has not been a benchmark run |
| `LastGPUBenchmarkMultiplier` | `float` | Multiplier used against the last GPU benchmark |
| `bUseHDRDisplayOutput` | `bool` | HDR |
| `HDRDisplayOutputNits` | `int32` | HDR |

## Functions

### `ApplySettings`

```text
ApplySettings(bCheckForCommandLineOverrides: bool) -> void
```

Applies all current user settings to the game and saves to permanent storage (e.g. file), optionally checking for command line overrides.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bCheckForCommandLineOverrides` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyNonResolutionSettings`

```text
ApplyNonResolutionSettings() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyResolutionSettings`

```text
ApplyResolutionSettings(bCheckForCommandLineOverrides: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bCheckForCommandLineOverrides` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScreenResolution`

```text
GetScreenResolution() -> FIntPoint
```

Returns the user setting for game screen resolution, in pixels.

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | - |

### `GetLastConfirmedScreenResolution`

```text
GetLastConfirmedScreenResolution() -> FIntPoint
```

Returns the last confirmed user setting for game screen resolution, in pixels.

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | - |

### `GetDesktopResolution`

```text
GetDesktopResolution() -> FIntPoint
```

Returns user's desktop resolution, in pixels.

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | - |

### `SetScreenResolution`

```text
SetScreenResolution(Resolution: FIntPoint) -> void
```

Sets the user setting for game screen resolution, in pixels.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Resolution` | `FIntPoint` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIsBorderless`

```text
GetIsBorderless() -> bool
```

IsBorderless getter and setter added by windzjliu

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIsBorderless`

```text
SetIsBorderless(InIsBorderless: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsBorderless` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBorderlessMode`

```text
GetBorderlessMode() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetBorderlessMode`

```text
SetBorderlessMode(InBorderlessMode: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBorderlessMode` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFullscreenMode`

```text
GetFullscreenMode() -> EWindowMode :: Type
```

Returns the user setting for game window fullscreen mode.

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | - |

### `GetLastConfirmedFullscreenMode`

```text
GetLastConfirmedFullscreenMode() -> EWindowMode :: Type
```

Returns the last confirmed user setting for game window fullscreen mode.

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | - |

### `SetFullscreenMode`

```text
SetFullscreenMode(InFullscreenMode: EWindowMode :: Type) -> void
```

Sets the user setting for the game window fullscreen mode. See UGameUserSettings::FullscreenMode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFullscreenMode` | `EWindowMode :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPreferredFullscreenMode`

```text
GetPreferredFullscreenMode() -> EWindowMode :: Type
```

Returns the user setting for game window fullscreen mode.

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | - |

### `SetVSyncEnabled`

```text
SetVSyncEnabled(bEnable: bool) -> void
```

Sets the user setting for vsync. See UGameUserSettings::bUseVSync.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVSyncEnabled`

```text
IsVSyncEnabled() -> bool
```

Returns the user setting for vsync.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsScreenResolutionDirty`

```text
IsScreenResolutionDirty() -> bool
```

Checks if the Screen Resolution user setting is different from current

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsFullscreenModeDirty`

```text
IsFullscreenModeDirty() -> bool
```

Checks if the FullscreenMode user setting is different from current

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsVSyncDirty`

```text
IsVSyncDirty() -> bool
```

Checks if the vsync user setting is different from current system setting

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ConfirmVideoMode`

```text
ConfirmVideoMode() -> void
```

Mark current video mode settings (fullscreenmoderesolution) as being confirmed by the user

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertVideoMode`

```text
RevertVideoMode() -> void
```

Revert video mode (fullscreenmoderesolution) back to the last user confirmed values

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBenchmarkFallbackValues`

```text
SetBenchmarkFallbackValues() -> void
```

Set scalability settings to sensible fallback values, for use when the benchmark fails or potentially causes a crash

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAudioQualityLevel`

```text
SetAudioQualityLevel(QualityLevel: int32) -> void
```

Sets the user's audio quality level setting

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityLevel` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAudioQualityLevel`

```text
GetAudioQualityLevel() -> int32
```

Returns the user's audio quality level setting

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetFrameRateLimit`

```text
SetFrameRateLimit(NewLimit: float) -> void
```

Sets the user's frame rate limit (0 will disable frame rate limiting)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLimit` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFrameRateLimit`

```text
GetFrameRateLimit() -> float
```

Gets the user's frame rate limit (0 indiciates the frame rate limit is disabled)

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetOverallScalabilityLevel`

```text
SetOverallScalabilityLevel(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOverallScalabilityLevel`

```text
GetOverallScalabilityLevel() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetResolutionScaleInformation`

```text
GetResolutionScaleInformation(CurrentScaleNormalized: float &, CurrentScaleValue: int32 &, MinScaleValue: int32 &, MaxScaleValue: int32 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentScaleNormalized` | `float &` | - |
| `CurrentScaleValue` | `int32 &` | - |
| `MinScaleValue` | `int32 &` | - |
| `MaxScaleValue` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetResolutionScaleInformationEx`

```text
GetResolutionScaleInformationEx(CurrentScaleNormalized: float &, CurrentScaleValue: float &, MinScaleValue: float &, MaxScaleValue: float &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentScaleNormalized` | `float &` | - |
| `CurrentScaleValue` | `float &` | - |
| `MinScaleValue` | `float &` | - |
| `MaxScaleValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResolutionScaleValue`

```text
SetResolutionScaleValue(NewScaleValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScaleValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResolutionScaleValueEx`

```text
SetResolutionScaleValueEx(NewScaleValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScaleValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResolutionScaleNormalized`

```text
SetResolutionScaleNormalized(NewScaleNormalized: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScaleNormalized` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetViewDistanceQuality`

```text
SetViewDistanceQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewDistanceQuality`

```text
GetViewDistanceQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetShadowQuality`

```text
SetShadowQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetShadowQuality`

```text
GetShadowQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetAntiAliasingQuality`

```text
SetAntiAliasingQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAntiAliasingQuality`

```text
GetAntiAliasingQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetTextureQuality`

```text
SetTextureQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTextureQuality`

```text
GetTextureQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetVisualEffectQuality`

```text
SetVisualEffectQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetVisualEffectQuality`

```text
GetVisualEffectQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetPostProcessingQuality`

```text
SetPostProcessingQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPostProcessingQuality`

```text
GetPostProcessingQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetFoliageQuality`

```text
SetFoliageQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFoliageQuality`

```text
GetFoliageQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsDirty`

```text
IsDirty() -> bool
```

Checks if any user settings is different from current

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ValidateSettings`

```text
ValidateSettings() -> void
```

Validates and resets bad user settings to default. Deletes stale user settings file if necessary.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LoadSettings`

```text
LoadSettings(bForceReload: bool) -> void
```

Loads the user settings from persistent storage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bForceReload` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SaveSettings`

```text
SaveSettings() -> void
```

Save the user settings to persistent storage (automatically happens as part of ApplySettings)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetToCurrentSettings`

```text
ResetToCurrentSettings() -> void
```

This function resets all settings to the current system settings

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetToDefaults`

```text
SetToDefaults() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDefaultResolutionScale`

```text
GetDefaultResolutionScale() -> float
```

Gets the desired resolution quality based on DesiredScreenWidthHeight and the current screen resolution

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRecommendedResolutionScale`

```text
GetRecommendedResolutionScale() -> float
```

Gets the recommended resolution quality based on LastRecommendedScreenWidthHeight and the current screen resolution

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetDefaultResolution`

```text
GetDefaultResolution() -> FIntPoint
```

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | The default resolution when no resolution is set |

### `GetDefaultWindowPosition`

```text
GetDefaultWindowPosition() -> FIntPoint
```

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | The default window position when no position is set |

### `GetDefaultWindowMode`

```text
GetDefaultWindowMode() -> EWindowMode :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | The default window mode when no mode is set |

### `GetGameUserSettings`

```text
GetGameUserSettings() -> UGameUserSettings *
```

Returns the game local machine settings (resolution, windowing mode, scalability settings, etc...)

**Returns**

| Type | Description |
|---|---|
| `UGameUserSettings *` | - |

### `RunHardwareBenchmark`

```text
RunHardwareBenchmark(WorkScale: int32, CPUMultiplier: float, GPUMultiplier: float) -> void
```

Runs the hardware benchmark and populates ScalabilityQuality as well as the last benchmark results config members, but does not apply the settings it determines. Designed to be called in conjunction with ApplyHardwareBenchmarkResults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorkScale` | `int32` | - |
| `CPUMultiplier` | `float` | - |
| `GPUMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyHardwareBenchmarkResults`

```text
ApplyHardwareBenchmarkResults() -> void
```

Applies the settings stored in ScalabilityQuality and saves settings

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SupportsHDRDisplayOutput`

```text
SupportsHDRDisplayOutput() -> bool
```

Whether the curently running system supports HDR display output

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EnableHDRDisplayOutput`

```text
EnableHDRDisplayOutput(bEnable: bool, DisplayNits: int32) -> void
```

Enables or disables HDR display output. Can be called again to change the desired nit level

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `DisplayNits` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentHDRDisplayNits`

```text
GetCurrentHDRDisplayNits() -> int32
```

Returns 0 if HDR isn't supported or is turned off

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsHDREnabled`

```text
IsHDREnabled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnGameUserSettingsUINeedsUpdate`

```text
OnGameUserSettingsUINeedsUpdate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGameViewportClient.json -->

# UGameViewportClient

A game viewport (FViewport) is a high-level abstract interface for the
  platform specific rendering, audio, and input subsystems.
  GameViewportClient is the engine's interface to a game viewport.
  Exactly one GameViewportClient is created for each instance of the game.  The
  only case (so far) where you might have a single instance of Engine, but
  multiple instances of the game (and thus multiple GameViewportClients) is when
  you have more than one PIE window running.
 
  Responsibilities:
  propagating input events to the global interactions list
 
  @see UGameViewportClient

## Inheritance

`UScriptViewportClient` -> `FExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ViewportConsole` | `UConsole *` | The viewport's console.   Might be null on consoles |
| `DebugProperties` | `TArray < struct FDebugDisplayProperty >` | @todo document |
| `World` | `UWorld *` | The relative world context for this viewport |
| `GameInstance` | `UGameInstance *` | - |

## Functions

### `SSSwapControllers`

```text
SSSwapControllers() -> void
```

Rotates controller ids among gameplayers, useful for testing splitscreen with only one controller.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowTitleSafeArea`

```text
ShowTitleSafeArea() -> void
```

Exec for toggling the display of the title safe area

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetConsoleTarget`

```text
SetConsoleTarget(PlayerIndex: int32) -> void
```

Sets the player which console commands will be executed in the context of.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGarbageCollectionSettings.json -->

# UGarbageCollectionSettings

Implements the settings for garbage collection.

## Inheritance

`UDeveloperSettings`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TimeBetweenPurgingPendingKillObjects` | `float` | - |
| `FlushStreamingOnGC` | `uint32` | - |
| `AllowParallelGC` | `uint32` | - |
| `IncrementalBeginDestroyEnabled` | `uint32` | - |
| `CreateGCClusters` | `uint32` | - |
| `ForbidCDOBeInCluster` | `uint32` | - |
| `MergeGCClusters` | `uint32` | - |
| `ActorClusteringEnabled` | `uint32` | - |
| `BlueprintClusteringEnabled` | `uint32` | - |
| `UseDisregardForGCOnDedicatedServers` | `uint32` | - |
| `NumRetriesBeforeForcingGC` | `int32` | - |
| `MinActorNumForActorCluster` | `int32` | - |
| `MaxObjectsNotConsideredByGC` | `int32` | - |
| `SizeOfPermanentObjectPool` | `int32` | - |
| `MaxObjectsInGame` | `int32` | - |
| `MaxObjectsInEditor` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGC_Backpack_Item_UIBP.json -->

# UGC_Backpack_Item_UIBP

背包格子控件

@class UGC_Backpack_Item_UIBP_C:UUserWidget
@field CanvasPanel_Lock UCanvasPanel
@field CanvasPanel_CommonItem UCanvasPanel
@field CanvasPanel_New UCanvasPanel
@field UGCCommonDragDropItem UUGCCommonDragDropItem_C
@field HorizontalBox_Unlock UHorizontalBox
@field Text_UnlockCurrencyNum UTextBlock
@field TextBlock_Num UTextBlock
@field Image_Currency UImage

## Functions

### `LoadCommonItemWidget`

```text
LoadCommonItemWidget()
```

异步加载CommonItem控件（通过UGCBackpackSystemV2外部接口）

### `ShowSelected`

```text
ShowSelected(bSelect: boolean)
```

格子显示选中状态

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSelect` | `boolean` | 是否选中 |

### `UpdateItemData`

```text
UpdateItemData(ItemDefineID: ItemDefineID, Count: number, AdditionData: table)
```

更新格子数据(!!!)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemDefineID` | `ItemDefineID` | 物品DefineID |
| `Count` | `number` | 数量 |
| `AdditionData` | `table` | 控件额外数据, 选中数据/拖拽数据都会包含 |

### `UpdateDragData`

```text
UpdateDragData(DragType: string, DragDirectionMode: EDragDropDirectionMode, DragClickCallback: function, DragStartCallback: function, DragCancelCallback: function)
```

更新格子拖拽数据(!!!)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DragType` | `string` | 拖拽类型，用于区分不同的拖拽处理 |
| `DragDirectionMode` | `EDragDropDirectionMode` | 默认自由拖拽，若处于滚动列表中，需与滚动方向相反设置 |
| `DragClickCallback` | `function` | 拖拽点击回调 |
| `DragStartCallback` | `function` | 拖拽开始回调 |
| `DragCancelCallback` | `function` | 拖拽取消回调 |

### `UpdateItemState`

```text
UpdateItemState(State: EBackpackItemState)
```

更新格子解锁状态

**Parameters**

| Name | Type | Description |
|---|---|---|
| `State` | `EBackpackItemState` | 格子状态, 默认为Unlock |

### `SetCustomUIList`

```text
SetCustomUIList(SoftWidgetPaths: FSoftClassPath[], PostCallback: function)
```

设置格子叠加UI

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftWidgetPaths` | `FSoftClassPath[]` | 叠加UI路径列表 |
| `PostCallback` | `function` | 叠加UI加载完成回调 {UISlot:挂点Slot, CustomUI:叠加控件} |

### `SetUnlockInfo`

```text
SetUnlockInfo(bShow: boolean, CoinID: number, CostNum: number)
```

显示解锁信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShow` | `boolean` | 是否显示解锁信息 |
| `CoinID` | `number` | 代币物品ID |
| `CostNum` | `number` | 解锁所需代币数量 |

### `GetUIData`

```text
GetUIData() -> table
```

控件的UI数据

**Returns**

| Type | Description |
|---|---|
| `table` | UI数据 |

### `SetIsNewItem`

```text
SetIsNewItem(bNew: boolean)
```

显示 新 标记

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNew` | `boolean` | 是否显示 新 标记 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/UGC_SecondaryConfirmation_UIBP.json -->

# UGC_SecondaryConfirmation_UIBP

二次确认面板

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGC_SecondaryConfirmation_UIBP.ConfirmationOperationDelegate` | `-` | 生效范围：客户端<br>二次确认面板操作通知，触发后会清空绑定的回调<br>@param Value boolean @true为确认，false为取消 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCAchievementSystem.json -->

# UGCAchievementSystem

徽章专用接口库

## Functions

### `AddAchievementProgress`

```text
AddAchievementProgress(PlayerKey: number, AchievementID: number, Count: number)
```

累积徽章进度
计数为覆盖累计，单场内多次调用不会累加计数，需自行计算累计总数单次调用
详细使用流程参考wiki (https://developer.gp.qq.com/wiki/#/lvzhou_huizhang.html)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家PlayerKey |
| `AchievementID` | `number` | 徽章ID |
| `Count` | `number` | 徽章计数 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCActivitySystem.json -->

# UGCActivitySystem

活动系统库（需要启用活动GamePart）

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCActivitySystem.OnActivityInfoReadyDelegate` | `-` | 活动信息准备好时触发的委托<br>生效范围：客户端&&服务器 |
| `UGCActivitySystem.OnUpdateValidActivityIDsDelegate` | `-` | 更新有效活动时触发的委托<br>活动系统会按照每个活动配置的生效周期来定期更新有效活动<br>生效范围：客户端&&服务器 |

## Functions

### `IsActivityInfoReady`

```text
IsActivityInfoReady() -> bool
```

活动信息是否已准备好
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `bool` | 活动信息是否已准备好 |

### `GetAllActivityInfos`

```text
GetAllActivityInfos() -> UGCActivityInfo[]
```

获取所有活动的信息
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `UGCActivityInfo[]` | 所有活动信息 |

### `GetActivityInfo`

```text
GetActivityInfo(ActivityID: int) -> UGCActivityInfo
```

获取指定活动ID的活动信息
生效范围：客户端&&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActivityID` | `int` | 活动ID |

**Returns**

| Type | Description |
|---|---|
| `UGCActivityInfo` | 活动信息 |

### `GetValidActivityIDs`

```text
GetValidActivityIDs() -> int[]
```

获取所有有效的活动ID
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `int[]` | - |

### `GetNearestPeriodIndex`

```text
GetNearestPeriodIndex(ActivityID: int) -> int
```

获取指定活动距当前时间最近的生效周期序号，
如果已经没有符合条件的开启周期，则返回最后一个生效周期的序号
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActivityID` | `int` | 活动ID |

**Returns**

| Type | Description |
|---|---|
| `int` | 活动开启周期序号, 0表示永久时间，-1表示活动不存在或未开启 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCActorComponentUtility.json -->

# UGCActorComponentUtility

Actor接口库

## Functions

### `SpawnActor`

```text
SpawnActor(WorldContextObject: UObject, ActorClass: UClass, Location: Vector, Rotation: Rotator, Scale3D: Vector, Owner: Actor) -> Actor
```

在游戏世界中生成指定类型的 Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `ActorClass` | `UClass` | 要生成的 Actor 类型，需通过 UGCObjectUtility.LoadClass 加载类引用 |
| `Location` | `Vector` | 生成位置坐标，推荐使用 {X=1,Y=1,Z=1} 构造 |
| `Rotation` | `Rotator` | 生成旋转角度，推荐使用 {X=0,Y=0,Z=0} 构造 |
| `Scale3D` | `Vector` | 可生成缩放比例，推荐使用 {X=1,Y=1,Z=1} 构造，默认值: Vector(0,0,0)，建议使用Vector(1,1,1)保持原始比例 |
| `Owner` | `Actor` | 新生成 Actor 的所属对象 |

**Returns**

| Type | Description |
|---|---|
| `Actor` | 新生成的 Actor 实例 |

### `DestroyActor`

```text
DestroyActor(InActor: AActor)
```

销毁Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

### `ToString`

```text
ToString(InActor: AActor) -> string
```

获取Actor的ToString
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `string` | ToString |

### `GetOwner`

```text
GetOwner(InActor: AActor) -> AActor
```

获取Actor的Owner
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Owner |

### `SetOwner`

```text
SetOwner(InActor: AActor, InOwner: AActor)
```

设置Actor的Owner
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InOwner` | `AActor` | Owner |

### `GetUltimateOwnerActor`

```text
GetUltimateOwnerActor(InActor: AActor) -> AActor
```

获取技能，武器，Buff等持有者acotr
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Owner |

### `GetUltimateController`

```text
GetUltimateController(InActor: AActor) -> AActor
```

获取技能，武器，Buff等持有者的Controller
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Owner |

### `AttachToActor`

```text
AttachToActor(InActor: AActor, InAttachTo: AActor, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, InSocketName: string)
```

附着到Actor上
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InAttachTo` | `AActor` | 需要附着到的Actor |
| `LocationRule` | `EAttachmentRule` | 附着位置规则 |
| `RotationRule` | `EAttachmentRule` | 附着旋转规则 |
| `ScaleRule` | `EAttachmentRule` | 附着缩放规则 |
| `InSocketName` | `string` | 需要附着到的SocketName |

### `AttachToComponent`

```text
AttachToComponent(InActor: AActor, InAttachTo: USceneComponent, LocationRule: EAttachmentRule, RotationRule: EAttachmentRule, ScaleRule: EAttachmentRule, InSocketName: string, bWeldSimulatedBodies: boolean)
```

附着到Component上
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InAttachTo` | `USceneComponent` | 需要附着到的Actor |
| `LocationRule` | `EAttachmentRule` | 附着位置规则 |
| `RotationRule` | `EAttachmentRule` | 附着旋转规则 |
| `ScaleRule` | `EAttachmentRule` | 附着缩放规则 |
| `InSocketName` | `string` | 需要附着到的SocketName |
| `bWeldSimulatedBodies` | `boolean` | 是否保持相对位置不变/是否焊接为模拟刚体 |

### `DetachFromParent`

```text
DetachFromParent(InComponent: USceneComponent, bMaintainWorldPosition: boolean, bCallModify: boolean)
```

将Component从父Actor上拆离
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `USceneComponent` | Actor |
| `bMaintainWorldPosition` | `boolean` | 是否保持位置不变 |
| `bCallModify` | `boolean` | 是否调用Modify |

### `GetRootComponent`

```text
GetRootComponent(InActor: AActor) -> USceneComponent
```

获取根组件
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `USceneComponent` | 根组件 |

### `GetComponentsByOwner`

```text
GetComponentsByOwner(InActor: AActor) -> UActorComponent[]
```

获取Actor上的所有Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent[]` | Actor上的所有Component |

### `GetComponentsByClass`

```text
GetComponentsByClass(InActor: AActor, InComonentClass: UClass) -> UActorComponent[]
```

获取Actor上指定类的Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InComonentClass` | `UClass` | 指定Component的Class |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent[]` | Actor上特定类型的Components |

### `GetComponentsByTag`

```text
GetComponentsByTag(InActor: AActor, InComonentClass: UClass, Tag: string) -> UActorComponent[]
```

获取Actor上指定Tag的Component
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InComonentClass` | `UClass` | ComponentClass |
| `Tag` | `string` | Tag |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent[]` | Components |

### `GetAllActorsOfClass`

```text
GetAllActorsOfClass(WorldContextObject: UObject, ActorClass: UClass) -> AActor[]
```

获取指定Class在场景里的所有Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | WorldContextObject |
| `ActorClass` | `UClass` | ActorClass |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | Actor列表 |

### `GetAllActorsWithTag`

```text
GetAllActorsWithTag(WorldContextObject: UObject, Tag: string) -> AActor[]
```

获取指定Tag在场景里的所有Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | WorldContextObject |
| `Tag` | `string` | Tag |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | Actor列表 |

### `GetActorTransform`

```text
GetActorTransform(InActor: AActor) -> FTransform
```

获取Actor的Transform
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | Transform |

### `GetSceneComponentWorldTransform`

```text
GetSceneComponentWorldTransform(InSceneComponent: USceneComponent) -> FTransform
```

获取场景组件的世界Transform
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSceneComponent` | `USceneComponent` | 场景组件 |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | Transform |

### `SetActorTransform`

```text
SetActorTransform(InActor: AActor, InTransform: FTransform)
```

设置Actor的Transform
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InTransform` | `FTransform` | Transform |

### `HasAuthority`

```text
HasAuthority(InActor: AActor) -> boolean
```

判断是否为权威端
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前端是否为权威端 |

### `CreateAndRegisterComponent`

```text
CreateAndRegisterComponent(InComponentClass: UClass, InOuter: UObject, InComponentName: string)
```

创建并注册组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponentClass` | `UClass` | 要创建组件对应的Class |
| `InOuter` | `UObject` | Outer |
| `InComponentName` | `string` | 要创建组件对应的Class对应的ObjectName |

### `DestroyComponent`

```text
DestroyComponent(InActor: AActor, InComponent: UActorComponent)
```

销毁组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | Actor |
| `InComponent` | `UActorComponent` | 要销毁的组件 |

### `GetOverlappingActorsWithPrimitiveComponent`

```text
GetOverlappingActorsWithPrimitiveComponent(InPrimitiveComponent: UPrimitiveComponent, Transform: FTransform, ObjectTypes: ESceneQueryType[], ActorClassFilter: UClass, ActorsToIgnore: AActor[]) -> AActor[]
```

获取与PrimitiveComponent重叠的Actor
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPrimitiveComponent` | `UPrimitiveComponent` | 组件 |
| `Transform` | `FTransform` | 组件的Transform |
| `ObjectTypes` | `ESceneQueryType[]` | 对象类型列表 |
| `ActorClassFilter` | `UClass` | 要检测的Actor类型（默认值：nil为全部类型的Actor） |
| `ActorsToIgnore` | `AActor[]` | 需要忽略的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 与目标Actor重叠的Actor列表 |

### `GetActorByActorInstancePath`

```text
GetActorByActorInstancePath(InstancePath: string) -> AActor
```

在运行时通过Actor实例路径获取Actor，对关卡编辑器实例列表里任意Actor右键，选择GetActorInstancePath即可获取路径
生效范围：客户端&服务器
路径格式：PackageName.ObjectPath，例如：UGCmap.test_8

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstancePath` | `string` | 实例路径 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | Actor实例 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCAirAttachSystem.json -->

# UGCAirAttachSystem

轰炸区接口库

## Functions

### `GenerateBombingArea`

```text
GenerateBombingArea(ConfigID: number, Location: FVector) -> number
```

生成轰炸区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 轰炸配置 ID |
| `Location` | `FVector` | 轰炸中心坐标（系统会自动通过射线检测将炸弹位置修正到地面高度） |

**Returns**

| Type | Description |
|---|---|
| `number` | 是否成功生成轰炸区, 实例ID |

### `StopBombingArea`

```text
StopBombingArea(InstanceID: number) -> bool
```

停止轰炸区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 轰炸实例 ID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功停止轰炸区 |

### `ModifyBombingAreaConfig`

```text
ModifyBombingAreaConfig(ConfigID: number, ParameterType: string, NewValue: number) -> bool
```

修改轰炸区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 轰炸配置 ID |
| `ParameterType` | `string` | 参数类型（如："AttackAreaRadius", "EscapeTime", "AttackLastingTime"等） |
| `NewValue` | `number` | 新的参数值 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功修改轰炸配置 |

### `GetAllConfigBombingArea`

```text
GetAllConfigBombingArea() -> UGCAirAttackConfig>
```

查看当前全部轰炸区
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UGCAirAttackConfig>` | 所有轰炸实例ID和对应的轰炸参数 |

### `GetSpecifyBombingAreaList`

```text
GetSpecifyBombingAreaList(InstanceID: number) -> UGCAirAttackConfig
```

查看指定轰炸区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 轰炸实例 ID |

**Returns**

| Type | Description |
|---|---|
| `UGCAirAttackConfig` | 指定实例的轰炸参数 |

### `GetAirAttackManager`

```text
GetAirAttackManager() -> UGCAirAttackManager
```

获取轰炸区管理器
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UGCAirAttackManager` | 轰炸区管理器实例，失败时返回nil |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCAirAttackManager.json -->

# UGCAirAttackManager

UGC轰炸区全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCAirAttackManager.SuccessfullyGeneratedBombing` | `-` | 轰炸区生成成功事件<br>当轰炸区域成功创建并准备开始预警时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @轰炸实例唯一标识符<br>@param CenterLocation FVector @轰炸中心位置坐标 |
| `UGCAirAttackManager.SuccessfullyStopBombing` | `-` | 轰炸区停止成功事件<br>当轰炸区域被成功停止（主动停止或异常结束）时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @被停止的轰炸实例唯一标识符 |
| `UGCAirAttackManager.NormalEndBombing` | `-` | 轰炸正常结束事件<br>当轰炸区域按计划完成所有炸弹投放后正常结束时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @结束的轰炸实例唯一标识符<br>@param TotalBombsDropped number @实际投放的炸弹总数 |
| `UGCAirAttackManager.SuccessfullyStartBombing` | `-` | 轰炸正式开始事件<br>当轰炸预警结束后，开始正式投放炸弹时触发<br>生效范围：服务器&客户端<br>@param InstanceID number @开始轰炸的实例唯一标识符 |
| `UGCAirAttackManager.AffectedBombingPlayers` | `-` | 玩家受影响事件<br>当炸弹爆炸并对范围内玩家造成伤害时触发<br>生效范围：服务器&客户端<br>@param BombLocation FVector @炸弹爆炸位置坐标<br>@param AffectedPlayerKeys number[] @受到影响的玩家PlayerKey数组 |
| `UGCAirAttackManager.__BombingPromiseFutures` | `-` | - |
| `UGCAirAttackManager.__WarningTimers` | `-` | - |
| `UGCAirAttackManager.__AirAttackMarks` | `-` | - |
| `UGCAirAttackManager.__MarkGraphIDs` | `-` | - |

## Functions

### `ExecuteAirAttack`

```text
ExecuteAirAttack(ConfigInput: number|UGCAirAttackConfig, CenterLocation: FVector|nil) -> number
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigInput` | `number\|UGCAirAttackConfig` | 空袭配置索引或配置对象 |
| `CenterLocation` | `FVector\|nil` | 轰炸中心位置，nil时使用原点（系统会自动通过射线检测将炸弹位置修正到地面高度） |

**Returns**

| Type | Description |
|---|---|
| `number` | 空袭实例唯一标识符 |

### `AbortAirAttack`

```text
AbortAirAttack(InstanceID: number)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 要终止的空袭实例ID，nil时终止所有空袭 |

### `Multicast_ExecuteAirAttack`

```text
Multicast_ExecuteAirAttack(BroadcastData: table)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BroadcastData` | `table` | 广播数据 {InstanceID, Seed, CenterLocation, GeneratedBy} |

### `Multicast_AbortAirAttack`

```text
Multicast_AbortAirAttack(InstanceID: number)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 要终止的空袭实例ID，nil时终止所有空袭 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCAirDropManagerSystem.json -->

# UGCAirDropManagerSystem

空投系统接口库

## Functions

### `GenerateAirDrop`

```text
GenerateAirDrop(ID: number, DroppingLocation: FVector, DroppingSpeed: number) -> int32
```

生成指定ID空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `number` | 空投配置ID |
| `DroppingLocation` | `FVector` | 掉落位置 结构Vector={X=0,Y=0,Z=0} |
| `DroppingSpeed` | `number` | 掉落速度 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 是否生成成功, 实例ID |

### `GetAllAirDropConfigs`

```text
GetAllAirDropConfigs(ID: number) -> OneAirDrop[]
```

获得所有空投配置
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `number` | 空投配置ID |

**Returns**

| Type | Description |
|---|---|
| `OneAirDrop[]` | 空投配置 |

### `DestroyAirDrop`

```text
DestroyAirDrop(InsID: number) -> boolean
```

销毁指定实例ID空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InsID` | `number` | 指定实例ID的空投 0.1s 后销毁 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否销毁成功 |

### `GetAirDropItemList`

```text
GetAirDropItemList(InsID: number) -> FPickUpItemData[]
```

获取指定实例ID空投的物品列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InsID` | `number` | 空投实例InsID |

**Returns**

| Type | Description |
|---|---|
| `FPickUpItemData[]` | 空投的物品列表 |

### `GetAllAirDropInstanceIDs`

```text
GetAllAirDropInstanceIDs() -> int32[]
```

获取当前场景内所有的实例ID
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `int32[]` | 空投实例ID列表 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCAnnouncementSystem.json -->

# UGCAnnouncementSystem

UGC公告系统

## Functions

### `GetLatestAnnouncements`

```text
GetLatestAnnouncements() -> PromiseFuture
```

发起异步请求获取最新的公告列表（最新的5个公告）
参考用法：
```lua
local PF = UGCAnnouncementSystem.GetLatestAnnouncements()
PF:Then(function (PromiseFuture) local Announcements = PromiseFuture:Get() end)
PF:Else(function (PromiseFuture) print("[UGCAnnouncementSystem.GetLatestAnnouncements] Failed, timeout") end)
```
Announcements结构为Lua数组
```
Announcements = {{Title:string, Content:string, EffectiveTime:number, bTop:boolean}, ...}
```
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 如果上一次请求未完成，则返回上一次请求的 PromiseFuture，否则返回新的 PromiseFuture |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCAsyncUtility.json -->

# UGCAsyncUtility

异步工具类

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCAsyncUtility.CoroutineManager` | `-` | - |
| `UGCAsyncUtility.AsyncErrorType` | `-` | - |

## Functions

### `CreatePromiseFuture`

```text
CreatePromiseFuture(Prerequisite: UGCPromiseFuture, ...: any) -> UGCPromiseFuture
```

创建一个新的 PromiseFuture 实例
 - 创建实例: 使用 PromiseFuture.New() 创建新的 PromiseFuture 实例。
 - 设置回调: 使用 Then 和 Else 方法设置成功和失败的回调函数。
 - 执行逻辑: 使用 Set 方法定义 PromiseFuture 的执行逻辑，可以在其中使用 Yield 暂停执行。
 - 前置条件: 可以将其他 PromiseFuture 实例作为前置条件，确保在执行当前 PromiseFuture 之前，所有前置条件都已完成。
 - 自动恢复: 可以设置自动恢复功能，监控对象的状态并在需要时自动恢复执行。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Prerequisite` | `UGCPromiseFuture` | 可选的前置条件 PromiseFuture 实例 |
| `...` | `any` | 其他可选的前置条件 |

**Returns**

| Type | Description |
|---|---|
| `UGCPromiseFuture` | 新创建的 PromiseFuture 实例 |

### `NewSequenceList`

```text
NewSequenceList() -> UGCAsyncSequenceHandle
```

新建一个保序列表，并返回ListHandle用于操作

**Returns**

| Type | Description |
|---|---|
| `UGCAsyncSequenceHandle` | 返回的ListHandle |

### `InsertItemIntoSequenceList`

```text
InsertItemIntoSequenceList(ListHandle: UGCAsyncSequenceHandle, ParamIndex: number, InConditionFunction: any, InConditionTable: table, InFunction: function@, InFunctionTable: table, ...: any)
```

往List里添加变量和函数。激活后时序逻辑为：轮询变量是否为空或者函数是否返回true，当变量不为空的时候，执行对应的函数，所以每次Insert一组变量和函数，就相当于添加一个时序逻辑。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListHandle` | `UGCAsyncSequenceHandle` | 保序列表的索引 |
| `ParamIndex` | `number` | 参数插入保序列表的位置，如果是0，则是插入到列表的尾部 |
| `InConditionFunction` | `any` | 可执行的Function或变量 |
| `InConditionTable` | `table` | 轮询变量或函数所在的Table |
| `InFunction` | `function@` | 当条件为true时执行的函数 |
| `InFunctionTable` | `table` | 当条件为true时执行函数的Table |
| `...` | `any` | 可变参数，当条件为true时执行的函数参数 |

### `ActivateSequenceList`

```text
ActivateSequenceList(ListHandle: UGCAsyncSequenceHandle, Interval: number, Timeout: number)
```

激活保序列表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ListHandle` | `UGCAsyncSequenceHandle` | 保序列表的索引 |
| `Interval` | `number` | 自动恢复的间隔，单位为秒 |
| `Timeout` | `number` | 自动恢复的超时时间，单位为秒 |

### `AsyncLoadSomething`

```text
AsyncLoadSomething(AsyncFun: function, ParamTables: UGCAsyncSequenceParamTable[], OnCompleteCallback: function) -> table
```

支持并行初始化的通用有序异步加载器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AsyncFun` | `function` | 需要调用的异步函数（格式：func(LoadPath, CallBack, CallBack_Self)） |
| `ParamTables` | `UGCAsyncSequenceParamTable[]` | 参数表数组 |
| `OnCompleteCallback` | `function` | 最终回调(loadedObjects) |

**Returns**

| Type | Description |
|---|---|
| `table` | loadedObjects |

### `AsyncCall`

```text
AsyncCall(CallFunction: function, Callback: function, CheckFunction: function, Opts: table) -> PromiseFuture
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CallFunction` | `function` | 调用函数 |
| `Callback` | `function` | 回调函数 |
| `CheckFunction` | `function` | 检查函数 |
| `Opts` | `table` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | - |

### `AsyncIfThen`

```text
AsyncIfThen(IfFunction: function, ThenFunction: function, Opts: table)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IfFunction` | `function` | 条件函数，返回 true 时执行 ThenFunction |
| `ThenFunction` | `function` | 条件满足时执行的函数 |
| `Opts` | `table` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

### `AsyncIfThenElse`

```text
AsyncIfThenElse(IfFunction: function, ThenFunction: function, ElseFunction: function, Opts: table)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IfFunction` | `function` | 条件函数，返回 true 时执行 ThenFunction，超时/取消时执行 ElseFunction |
| `ThenFunction` | `function` | 条件满足时执行的函数 |
| `ElseFunction` | `function` | 超时或取消时执行的函数 |
| `Opts` | `table` | 可选参数 { Watched=UObject, Interval=number, Timeout=number } |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCAttributeSystem.json -->

# UGCAttributeSystem

属性系统接口库

## Functions

### `GetGameAttributeValue`

```text
GetGameAttributeValue(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举) -> number
```

获取指定属性数值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Returns**

| Type | Description |
|---|---|
| `number` | 目标数值 |

### `SetGameAttributeValue`

```text
SetGameAttributeValue(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, Value: number)
```

设置指定属性数值（自动同步到客户端）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `Value` | `number` | 操作数值 |

### `GetGameAttributeValueMax`

```text
GetGameAttributeValueMax(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举) -> number
```

获取指定属性数值的最大值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Returns**

| Type | Description |
|---|---|
| `number` | 目标数值 |

### `GetGameAttributeValueMin`

```text
GetGameAttributeValueMin(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举) -> number
```

获取指定属性数值的最小值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |

**Returns**

| Type | Description |
|---|---|
| `number` | 目标数值 |

### `AddGameAttributeValue`

```text
AddGameAttributeValue(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, Value: number)
```

服务端添加指定属性数值（自动同步到客户端）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `Value` | `number` | 操作数值 |

### `AddGameAttributeOperation`

```text
AddGameAttributeOperation(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, OperateType: EAttrOperator, Value: number) -> string
```

对指定属性添加数值修改操作
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `OperateType` | `EAttrOperator` | 操作类型 |
| `Value` | `number` | 操作数值 |

**Returns**

| Type | Description |
|---|---|
| `string` | 操作完成的唯一ID |

### `RemoveGameAttributeOperation`

```text
RemoveGameAttributeOperation(AttributeOwner: AActor, OperateUniqueID: string)
```

对指定属性移除特定的数值修改操作
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `OperateUniqueID` | `string` | 操作属性时返回的唯一ID |

### `AddGameAttributeChangedDelegate`

```text
AddGameAttributeChangedDelegate(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, CallbackFunction: function) -> Delegate
```

注册指定属性变化时的回调函数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `CallbackFunction` | `function` | 此属性变化时的回调函数 函数形式: function(AttributeOwner, AttrName, CurValue) end |

**Returns**

| Type | Description |
|---|---|
| `Delegate` | 属性变化的代理 |

### `RemoveGameAttributeChangedDelegate`

```text
RemoveGameAttributeChangedDelegate(AttributeOwner: AActor, AttributeType: UGCNativeGameAttributeType | UGCCustomGameAttributeType @操作属性的枚举, ChangedDelegate: Delegate)
```

清除指定属性变化时的回调函数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttributeOwner` | `AActor` | 操作属性的对象 （如玩家，枪械等，暂不支持带属性组件的普通Actor） |
| `AttributeType` | `UGCNativeGameAttributeType \| UGCCustomGameAttributeType @操作属性的枚举` | 操作属性的枚举 |
| `ChangedDelegate` | `Delegate` | 注册回调函数时返回的代理 |

### `GetSourceObjectFromContext`

```text
GetSourceObjectFromContext(Context: FGameMagnitudeContext) -> UObject
```

获取伤害事件上下文中的原对象
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `UObject` | 原对象 |

### `GetVictimFromContext`

```text
GetVictimFromContext(Context: FGameMagnitudeContext) -> AActor
```

获取伤害事件上下文中的受害者
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 受害者 |

### `GetCauserFromContext`

```text
GetCauserFromContext(Context: FGameMagnitudeContext) -> AActor
```

获取伤害事件上下文中的攻击者
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 攻击者(如玩家，怪物, 枪械等) |

### `GetInstigatorFromContext`

```text
GetInstigatorFromContext(Context: FGameMagnitudeContext) -> AController
```

获取伤害事件上下文中的攻击者Controller
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AController` | 攻击者Controller(如玩家PlayerController，怪物AIController, 枪械所属角色的Controller等) |

### `GetSourceMagnitudeFromContext`

```text
GetSourceMagnitudeFromContext(Context: FGameMagnitudeContext) -> number
```

获取伤害事件上下文中的原伤害数值
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `number` | 伤害数值 |

### `GetDamageTypeFromContext`

```text
GetDamageTypeFromContext(Context: FGameMagnitudeContext) -> ERestrictedDamageType
```

获取伤害事件上下文中的伤害类型
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `ERestrictedDamageType` | 伤害类型 |

### `GetDamageTagsFromContext`

```text
GetDamageTagsFromContext(Context: FGameMagnitudeContext) -> FName[]
```

获取伤害事件上下文中的伤害Tags
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `FName[]` | 伤害Tags |

### `GetRecoverTagsFromContext`

```text
GetRecoverTagsFromContext(Context: FGameMagnitudeContext) -> FName[]
```

获取治疗事件上下文中的治疗Tags
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 治疗事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `FName[]` | 伤害Tags |

### `GetRecoveredActorFromContext`

```text
GetRecoveredActorFromContext(Context: FGameMagnitudeContext) -> AActor
```

获取治疗上下文中的被治疗者
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 治疗事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 被治疗者 |

### `GetDamagePositionTypeFromContext`

```text
GetDamagePositionTypeFromContext(Context: FGameMagnitudeContext) -> EAvatarDamagePosition
```

获取伤害事件上下文中的伤害部位类型
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `EAvatarDamagePosition` | 伤害部位类型 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCBackPackSystem.json -->

# UGCBackPackSystem

背包系统接口库

## Functions

### `GetBackpackComponent`

```text
GetBackpackComponent(PlayerPawn: PlayerPawn) -> UBackpackComponent
```

获取背包组件(客户端仅能获取到自己的）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `UBackpackComponent` | 背包组件 |

### `AddItem`

```text
AddItem(PlayerPawn: PlayerPawn, ItemID: number, Count: number) -> boolean
```

添加道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |
| `Count` | `number` | 数量 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DropItem`

```text
DropItem(PlayerPawn: PlayerPawn, ItemID: number, Count: number, IsDestroy: boolean) -> boolean
```

掉落道具（入参为ItemID，不关心具体哪个道具）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |
| `Count` | `number` | 数量 |
| `IsDestroy` | `boolean` | 是否直接销毁，不掉落地面 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `UseItem`

```text
UseItem(PlayerPawn: PlayerPawn, ItemID: number) -> boolean
```

使用道具（入参为ItemID，不关心具体哪个道具）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DisuseItem`

```text
DisuseItem(PlayerPawn: PlayerPawn, ItemID: number) -> boolean
```

停止使用物品（入参为ItemID，默认选择同ID第一个，仅对物资编辑器生成的绷带，饮料类物资生效）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DropItemByInstanceID`

```text
DropItemByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number, Count: number, IsDestroy: boolean) -> boolean
```

根据InstanceID（物品实例ID）掉落道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |
| `Count` | `number` | 数量 |
| `IsDestroy` | `boolean` | 是否直接销毁，不掉落地面 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `UseItemByInstanceID`

```text
UseItemByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number) -> boolean
```

根据InstanceID（物品实例ID）使用道具
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DisuseItemByInstanceID`

```text
DisuseItemByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number) -> boolean
```

根据InstanceID（物品实例ID）停止使用道具（仅对物资编辑器生成的绷带，饮料类物资生效）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetItemCount`

```text
GetItemCount(PlayerPawn: PlayerPawn, ItemID: number) -> number
```

获取道具数量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包内物品数量 |

### `GetAllItemData`

```text
GetAllItemData(PlayerPawn: PlayerPawn) -> @LuaTable<ItemData>,
```

获取背包里所有道具数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `@LuaTable,` | ItemData结构：ItemID,InstanceID,Count,Type,SubType,IsAvatar |

### `GetAllItemDataByItemID`

```text
GetAllItemDataByItemID(PlayerPawn: PlayerPawn, ItemID: number) -> table
```

获取ItemData列表
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `table` | LuaTable |

### `GetItemDataByInstanceID`

```text
GetItemDataByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number) -> FBattleItemData
```

根据InstanceID（物品实例ID）获取ItemData
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | 物品实例ID（唯一） |

**Returns**

| Type | Description |
|---|---|
| `FBattleItemData` | 战斗物品数据 |

### `GetCapacity`

```text
GetCapacity(PlayerPawn: PlayerPawn) -> number
```

获取背包剩余容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 剩余容量 |

### `GetMaxCapacity`

```text
GetMaxCapacity(PlayerPawn: PlayerPawn) -> number
```

获取背包最大剩余容量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大剩余容量 |

### `HasItemBySubType`

```text
HasItemBySubType(PlayerPawn: PlayerPawn, ItemSubType: number) -> boolean
```

是否拥有某类物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `ItemSubType` | `number` | 道具字类型 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetWeaponsInBackpack`

```text
GetWeaponsInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包中的武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | FBattleItemData |

### `GetWeaponAttachmentsInBackpack`

```text
GetWeaponAttachmentsInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包中的武器配件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | FBattleItemData |

### `GetArmorInBackpack`

```text
GetArmorInBackpack(PlayerPawn: PlayerPawn) -> FBattleItemData
```

获取当前防弹衣
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `FBattleItemData` | 物品数据 |

### `GetHelmetInBackpack`

```text
GetHelmetInBackpack(PlayerPawn: PlayerPawn) -> FBattleItemData
```

获取当前头盔
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `FBattleItemData` | 物品数据 |

### `GetConsumablesInBackpack`

```text
GetConsumablesInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包中的所有消耗品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | FBattleItemData |

### `IsAttachItemType`

```text
IsAttachItemType(ItemID: number) -> boolean
```

通过传入物品ID判断是否拥有某类物品，例：可传入AKM的物品ID，判断是否拥有枪械
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `IsGunItemType`

```text
IsGunItemType(ItemID: number) -> boolean
```

传入物品ID判断是否为枪械
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetPickupWrapperClassPath`

```text
GetPickupWrapperClassPath(ItemID: number) -> string
```

获取PickupWrapperClass路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `string` | - |

### `GetAllAttachmentDefineIDInBackpack`

```text
GetAllAttachmentDefineIDInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包内所有枪械配件DefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | AttachmentDefineID列表 LuaTable |

### `GetAllUnEquipedAttachmentDefineIDInBackpack`

```text
GetAllUnEquipedAttachmentDefineIDInBackpack(PlayerPawn: PlayerPawn) -> table
```

获取背包内所有未装备的枪械配件DefineID
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `table` | AttachmentDefineID列表 LuaTable |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCBackpackSystemV2.json -->

# UGCBackpackSystemV2

UGC V2背包系统接口库

需启用及配合新背包系统使用，具体参见 https://developer.gp.qq.com/wikieditor/#/catalog/20104

## Functions

### `GetBackpackComponentV2`

```text
GetBackpackComponentV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> @UGC
```

获取背包组件(客户端仅能获取到自己的）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `@UGC` | V2背包组件 |

### `GetBackpackUIComponentV2`

```text
GetBackpackUIComponentV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> @UGC
```

获取背包UI组件(客户端）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `@UGC` | V2背包UI组件 |

### `GetPlayerControllerByBackpackComponent`

```text
GetPlayerControllerByBackpackComponent(BackpackComponent: BackpackComponentV2) -> PlayerController
```

通过背包组件获取 PlayerController
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BackpackComponent` | `BackpackComponentV2` | UGC V2背包组件 |

**Returns**

| Type | Description |
|---|---|
| `PlayerController` | 玩家控制器 |

### `GetCharacterByBackpackComponent`

```text
GetCharacterByBackpackComponent(BackpackComponent: BackpackComponentV2) -> PlayerPawn
```

通过背包组件获取角色
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BackpackComponent` | `BackpackComponentV2` | UGC V2背包组件 |

**Returns**

| Type | Description |
|---|---|
| `PlayerPawn` | 玩家角色 |

### `GetPlayerStateByBackpackComponent`

```text
GetPlayerStateByBackpackComponent(BackpackComponent: BackpackComponentV2) -> PlayerState
```

通过背包组件获取 PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BackpackComponent` | `BackpackComponentV2` | UGC V2背包组件 |

**Returns**

| Type | Description |
|---|---|
| `PlayerState` | 玩家状态 |

### `VerifyItemDefineIDInBackpack`

```text
VerifyItemDefineIDInBackpack(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID) -> boolean
```

验证ItemDefineID是否合法
防止外挂非法篡改ItemDefineID的数据
请注意，空的ItemDefineID是合法的

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否合法 |

### `AddItemV2`

```text
AddItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number, Count: number, PresetIdx: number) -> ItemDefineID[]
```

凭空添加物品
生效范围：服务器

使用 ItemID（配置ID）创建物品。创建的物品会自动尝试合并到已有堆叠上。堆叠时，如果超过最大堆叠数，将进行分堆。
函数返回会返回成功添加的物品数量，和所有新创建的分堆的实例ID（只有产生新的分堆，才会返回实例ID）。
如果有多个已有的的分堆，将会尽量尝试将所有分堆都填充到最大堆叠数，才开辟新的分堆。
新物品不会合并到拥有实例化数据的物品分堆。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |
| `Count` | `number` | 数量 |
| `PresetIdx` | `number` | 槽位预设索引 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 已成功添加的物品数量，成功添加的物品实例列表 |

### `CheckInitPersistCompleted`

```text
CheckInitPersistCompleted(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> boolean
```

检查初始化持久化完成
生效范围：服务器 & 客户端

检查初始化持久化完成

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否初始化持久化完成 |

### `AddItemByDefineIDV2`

```text
AddItemByDefineIDV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, DefineID: ItemDefineID, Count: number, AllowMerge: boolean) -> number
```

指定 ItemDefineID(实例ID) 添加物品
生效范围：服务器

这个是高级版的添加物品接口，简单需求建议使用“UGCBackpackSystemV2.AddItemV2”。
由于 ItemDefineID 需要保证唯一，因此需要使用全新的 ItemDefineID 创建物品（UGCItemSystemV2.GetItemDefineID）。
如果使用另一物品的 ItemDefineID 创建物品，将导致 ID 混乱。
接口最多创建一个新堆叠，此堆叠的实例ID即函数传入的实例ID。如果此堆叠无法容纳所有需要创建的物品数量，将有一部分物品创建失败。
接受的实例ID可以提前塞入实例化数据。
此功能可以用于创建一些随机属性的装备，然后添加进入背包（当然也可以发挥创意，实现其它趣味功能）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `DefineID` | `ItemDefineID` | 物品 DefineID |
| `Count` | `number` | 数量 |
| `AllowMerge` | `boolean` | 是否允许合并到已有堆叠(默认true) |

**Returns**

| Type | Description |
|---|---|
| `number` | 已成功添加的物品数量 |

### `AddAndEquipItemV2`

```text
AddAndEquipItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, DefineID: ItemDefineID) -> EItemAddAndEquipResultV2
```

添加并装备物品
生效范围：服务器

通过 ItemDefineID 添加物品到背包并装备到合适的槽位。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `DefineID` | `ItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `EItemAddAndEquipResultV2` | 添加装备返回结果枚举 |

### `RemoveItemV2`

```text
RemoveItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number, Count: number) -> number
```

指定ItemID(配置ID)移除物品
不生成可拾取物
生效范围：服务器&客户端

移除时背包将只关注数量，不关注具体是哪个实例。一般适用于不同实例物品都等价的情况。
由于是由服务器实际执行移除操作，客户端调用后无法立刻获得实际移除的物品数量。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品 ID |
| `Count` | `number` | 数量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 服务器:实际移除的物品数量 \| 客户端:返回 0 |

### `RemoveItemByDefineIDV2`

```text
RemoveItemByDefineIDV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID, Count: number) -> number
```

移除指定物品实例
不生成可拾取物
生效范围：服务器&客户端

只会移除指定的物品实例，不会波及到其它物品实例。
由于是由服务器实际执行移除操作，客户端调用后无法立刻获得实际移除的物品数量。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |
| `Count` | `number` | 数量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 服务器:实际移除的物品数量 \| 客户端:返回 0 |

### `DropItemV2`

```text
DropItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number, Count: number) -> number
```

指定ItemID(配置ID)丢弃物品
生成可拾取物
生效范围：服务器&客户端

丢弃时背包将只关注数量，不关注具体是哪个实例。一般适用于不同实例物品都等价的情况。
由于是由服务器实际执行丢弃操作，客户端调用后无法立刻获得实际丢弃的物品数量。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品 ID |
| `Count` | `number` | 数量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 服务器:实际丢弃的物品数量 \| 客户端:返回 0 |

### `DropItemByDefineIDV2`

```text
DropItemByDefineIDV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID, Count: number) -> number
```

丢弃指定物品实例
生成可拾取物
生效范围：服务器&客户端

只会丢弃指定的物品实例，不会波及到其它物品实例。
丢弃后生成的可拾取物（PickupWrapper）对应的实例ID与丢弃时指定的实例ID并不相同。
可拾取物将获得一个全新的实例ID，新实例ID依然具有原始实例物品的所有实例化数据。
由于是由服务器实际执行丢弃操作，客户端调用后无法立刻获得实际丢弃的物品数量。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |
| `Count` | `number` | 数量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 服务器:实际丢弃的物品数量 \| 客户端:返回 0 |

### `TrySortOutItemV2`

```text
TrySortOutItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器)
```

尝试整理物品
尝试将背包中的物品整理整齐(将可堆叠的物品尽量堆叠起来)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

### `CanUseItemV2`

```text
CanUseItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID) -> boolean
```

背包内的物品是否可以使用
生效范围：服务器&客户端

默认情况下，返回值等同于物编中物品的"是否可使用"配置
若在背包组件上重写了CanUseItemV2，将调用重写后的函数并返回

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 物品是否可以使用 |

### `CanRemoveItemV2`

```text
CanRemoveItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID, Count: number) -> number
```

背包内的物品是否可以移除
生效范围：服务器&客户端

默认情况下，若物编中物品"是否可移除"配置为true，要移除多少就返回多少，否则返回0
若在背包组件上重写了CanRemoveItemV2，将调用重写后的函数并返回

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |
| `Count` | `number` | 要移除的数量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品可移除的数量 |

### `CanDropItemV2`

```text
CanDropItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID, Count: number) -> number
```

背包内的物品是否可以丢弃
生效范围：服务器&客户端

默认情况下，若物编中物品"是否可丢弃"配置为true，要移除多少就返回多少，否则返回0
若在背包组件上重写了CanDropItemV2，将调用重写后的函数并返回

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |
| `Count` | `number` | 要丢弃的数量 |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品可丢弃数量 |

### `UseItemV2`

```text
UseItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID) -> boolean
```

使用指定物品
生效范围：服务器&客户端

只会使用指定的物品实例，不会波及到其它物品实例。
由于是由服务器实际执行使用操作，客户端调用后无法立刻获得实际使用物品的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 服务器:是否使用成功 \| 客户端:不管成功失败都返回 true |

### `DisuseItemV2`

```text
DisuseItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID)
```

取消使用指定物品
与 UseItem 对应，用于清理状态
永远成功，没有失败条件
支持多次调用，不产生额外副作用，移除物品时自动调用清理
生效范围：服务器&客户端

在和平的设计中，物品没有维护"使用中"的状态，因此 Disuse 和 Use 并非是完全对称的概念（和平经典背包与V2背包都遵循这个规则）。物品 Disuse 主要是用于物品清理状态。
由于是由服务器实际执行取消使用操作，客户端调用后无法立刻获得实际取消使用物品的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品DefineID |

### `GetItemCountV2`

```text
GetItemCountV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number) -> number
```

获取物品数量
如果有多个实例，将获取它们的总数量
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包内物品数量 |

### `GetItemCountByDefineIDV2`

```text
GetItemCountByDefineIDV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID) -> number
```

获取物品实例数量
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包内物品实例数量 |

### `GetItemDefineIDsByIDV2`

```text
GetItemDefineIDsByIDV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number) -> ItemDefineID[]
```

通过物品 ID，获取所有此 ID 物品实例
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 满足条件的物品实例 DefineID |

### `GetItemDefineIDsByTagV2`

```text
GetItemDefineIDsByTagV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemTag: string) -> ItemDefineID[]
```

通过物品 Tag，获取所有含此 Tag 物品实例
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemTag` | `string` | 物品Tag |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 满足条件的物品实例 DefineID |

### `GetAllItemDefineIDsV2`

```text
GetAllItemDefineIDsV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> ItemDefineID[]
```

获取所有物品实例
客户端数据可能稍微滞后
生效范围：服务器&客户端

只会获得V2背包支持的物品类型，一般为玩法功能性物品（武器、配件、弹药、药品、装备等）。
经典背包中的部分特殊物品不在此列（服装、皮肤、表情等）。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 背包内所有物品实例 DefineID |

### `GetEquipSlots`

```text
GetEquipSlots(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> FName[]
```

获取所有装备槽位名称
返回装备槽位的顺序与V2背包组件配置顺序一致。
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `FName[]` | 背包所有装备槽位名称 |

### `GetSlotDisplayName`

```text
GetSlotDisplayName(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, SlotName: string) -> string
```

获取槽位中文名
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `SlotName` | `string` | 槽位名称 |

**Returns**

| Type | Description |
|---|---|
| `string` | 槽位中文名 |

### `ItemCanEquipToSlot`

```text
ItemCanEquipToSlot(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number, SlotName: string) -> boolean
```

物品是否能装在槽位上(根据配置信息判断)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |
| `SlotName` | `string` | 槽位名称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true:可以装备 false:不可以装备 |

### `GetEquippedItemBySlotName`

```text
GetEquippedItemBySlotName(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, SlotName: string) -> ItemDefineID
```

获取指定装备槽位所装备的物品
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `SlotName` | `string` | 槽位名称 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID` | 槽位所装备的物品 |

### `GetItemEquippingSlot`

```text
GetItemEquippingSlot(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, DefineID: ItemDefineID) -> string
```

获取指定物品在背包上装备的槽位
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `DefineID` | `ItemDefineID` | 物品实例 DefineID |

**Returns**

| Type | Description |
|---|---|
| `string` | 物品在背包上装备的槽位。若为空字符串，则物品未装备在背包槽位上。 |

### `EquipItemV2`

```text
EquipItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, SlotName: string, DefineID: ItemDefineID) -> boolean
```

将物品装在指定槽位
生效范围：服务器&客户端

如果此物品已经装备在某个槽位上，将不再能够再次装备。
只有从部分模板中创建的物品拥有装备功能。
如果槽位上配置了类型约束，那将只有对应类型的物品能够装备。
如果对应槽位已经装备了其它物品，会触发卸下装备，然后再将指定物品装备到此槽位。
一般物品都会占用背包格子容量，但装备后的物品不再占用背包容量。
由于是由服务器实际执行装备操作，客户端调用后无法立刻获得实际装备的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `SlotName` | `string` | 槽位名称 |
| `DefineID` | `ItemDefineID` | 物品实例 DefineID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 服务器:是否装备成功 \| 客户端:不管成功失败都返回 true |

### `UnEquipItemV2`

```text
UnEquipItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, SlotName: string) -> boolean
```

将指定槽位的物品卸下
生效范围：服务器&客户端

一般物品都会占用背包格子容量，但装备后的物品不再占用背包容量（参考容量限制功能 ）。
一般情况下如果背包容量已满，卸下装备将会失败。
由于是由服务器实际执行卸下装备操作，客户端调用后无法立刻获得实际卸下装备的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `SlotName` | `string` | 槽位名称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 服务器:是否卸下成功 \| 客户端:不管成功失败都返回 true |

### `EquipItemToAnySlotV2`

```text
EquipItemToAnySlotV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, DefineID: ItemDefineID) -> boolean
```

将物品装在任意槽位
生效范围：服务器&客户端

功能类似 EquipItemV2，但无需指定槽位。
它将会尽量找到一个可装备的空槽位去尝试装备。
如果所有可装备的槽位都非空，它会尝试向一个非空槽位装备。此时此槽位的原物品，将被卸下。
由于是由服务器实际执行装备操作，客户端调用后无法立刻获得实际装备的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `DefineID` | `ItemDefineID` | 物品实例 DefineID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 服务器:是否装备成功 \| 客户端:不管成功失败都返回 true |

### `CheckCanEquipItemToAnySlotV2`

```text
CheckCanEquipItemToAnySlotV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number) -> boolean
```

检查物品能否装在任意槽位(背包槽位、装备槽位)
生效范围：服务器&客户端

支持递归检查：不仅检查能否装备到背包槽位、能否作为配件装备到已装备物品上，
还会递归地检查能否作为配件装备到当前已装备物品的子配件上。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否存在至少一个可装备的槽位（含已被占据但可替换的槽位） |

### `GetAllEquipableSlotsForItemV2`

```text
GetAllEquipableSlotsForItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number) -> table[]
```

获取物品所有可装备槽位的占用信息
生效范围：服务器&客户端

遍历所有背包槽位与已装备物品（含其所有子配件，递归），收集可装备 ItemID 的槽位信息。
返回的列表包含：
  - 空槽位（OccupiedItem 为空，IsOccupied=false）
  - 已被占据但可被替换的槽位（OccupiedItem 为已装备的物品 DefineID，IsOccupied=true）

每条记录包含：
  - SlotName       string         槽位名称
  - ParentDefineID ItemDefineID   父物品 DefineID（装到背包槽位时为空 DefineID）
  - ItemDefineID   ItemDefineID   当前占据该槽位的物品 DefineID（无则为空 DefineID）
  - IsOccupied     boolean        是否已被占据

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `table[]` | 可装备槽位信息列表 |

### `GetOccupiedSlotItemsForItemV2`

```text
GetOccupiedSlotItemsForItemV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number) -> table[]
```

获取物品可装备槽位中已被占据的物品信息列表
生效范围：服务器&客户端

在 GetAllEquipableSlotsForItemV2 的基础上，仅返回那些"槽位被占用"的项。
这通常用于：当玩家试图装备一个新物品时，提示玩家"装备此物品将替换以下物品"。

每条记录包含：
  - SlotName       string         被占用的槽位名称
  - ParentDefineID ItemDefineID   父物品 DefineID（装到背包槽位时为空 DefineID）
  - ItemDefineID   ItemDefineID   当前占据该槽位的物品 DefineID

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `table[]` | 被占用槽位的占用物品信息列表 |

### `SwapEquipSlotV2`

```text
SwapEquipSlotV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, SlotNameA: string, SlotNameB: string) -> boolean
```

交换两个槽位的装备(若其中一个槽位为空,其意义变为将一个槽位的装备移至另一槽位)
生效范围：服务器&客户端

交换功能的效果，并不完全与分别卸下再重新装备相同。
一方面，卸下时可能受背包容量限制。
另一方面，装备和卸下将触发物品Handle上对应的事件（OnEquip、OnUnEquip）。
但交换装备时不触发它们，而是对交换槽位的物品Handle分别触发 OnSwapEquipSlot 。
由于是由服务器实际执行交换操作，客户端调用后无法立刻获得实际交换的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `SlotNameA` | `string` | 槽位名称A |
| `SlotNameB` | `string` | 槽位名称B |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 服务器:是否交换成功 \| 客户端:不管成功失败都返回 true |

### `AttachEquipmentToTargetItem`

```text
AttachEquipmentToTargetItem(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, Equipment: ItemDefineID, TargetItem: ItemDefineID, SlotName: string) -> boolean
```

将物品A附加到另一个物品B的槽位上
要求物品A和物品B都在背包中
生效范围：服务器&客户端

当某物品A附加到一个已装备在背包槽位上的物品B时，物品A也视为进入装备状态，触发物品Handle的OnEquip事件。
当某物品A附加到另一物品B后，物品B装备到了背包槽位上。此时A会随B一起，进入装备状态，触发物品Handle的OnEquip事件。
由于是由服务器实际执行附加操作，客户端调用后无法立刻获得实际附加的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `Equipment` | `ItemDefineID` | 物品A |
| `TargetItem` | `ItemDefineID` | 物品B |
| `SlotName` | `string` | 物品B上的目标槽位 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 服务器:是否附加成功 \| 客户端:不管成功失败都返回 true |

### `DetachEquipmentToTargetItem`

```text
DetachEquipmentToTargetItem(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, TargetItem: ItemDefineID, SlotName: string) -> boolean
```

解除附加在物品B槽位上的物品A
生效范围：服务器&客户端

当某物品A附加到一个已装备在背包槽位上的物品B时，物品A也视为进入装备状态。此时若A解除对B的附加，将取消A的装备状态，触发物品Handle的OnUnEquip事件。
由于是由服务器实际执行附加操作，客户端调用后无法立刻获得实际附加的结果。且在服务器执行完毕并将结果同步到客户端之前，客户端本地数据不会立刻改变。

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `TargetItem` | `ItemDefineID` | 物品B |
| `SlotName` | `string` | 物品B上的目标槽位 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 服务器:是否解除附加成功 \| 客户端:不管成功失败都返回 true |

### `GetWarehouseItemCountByDefineID`

```text
GetWarehouseItemCountByDefineID(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID) -> number
```

获取仓库物品实例数量
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 物品实例 DefineID |

**Returns**

| Type | Description |
|---|---|
| `number` | 仓库内物品实例数量 |

### `GetWarehouseItemCount`

```text
GetWarehouseItemCount(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number) -> number
```

获取仓库物品数量
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 仓库内物品数量 |

### `GetAllWarehouseItemDefineIDs`

```text
GetAllWarehouseItemDefineIDs(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> ItemDefineID[]
```

获取仓库内所有物品实例
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 仓库内所有物品实例 DefineID |

### `PutInWarehouse`

```text
PutInWarehouse(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID, PutOnCount: number) -> FUGCItemTransferResult
```

将背包物品放入仓库
请注意，实例ID将被转换，真正进入仓库的实例ID和传入的实例ID有所不同
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 放入的物品实例ID |
| `PutOnCount` | `number` | 放入的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `FUGCItemTransferResult` | 物品转移结果 |

### `TakeOutWarehouse`

```text
TakeOutWarehouse(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: ItemDefineID, TakeOutCount: number) -> FUGCItemTransferResult
```

将物品从仓库取出
请注意，实例ID将被转换，真正回到背包的实例ID和传入的实例ID有所不同
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `ItemDefineID` | 取出的物品实例ID |
| `TakeOutCount` | `number` | 取出的物品数量 |

**Returns**

| Type | Description |
|---|---|
| `FUGCItemTransferResult` | 物品转移结果 |

### `TrySortOutWarehouseItem`

```text
TrySortOutWarehouseItem(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器)
```

尝试整理仓库物品
尝试将仓库中的物品整理整齐
整理过程中会将可堆叠的物品尽量堆叠起来
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

### `GetCellItemCount`

```text
GetCellItemCount(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> number
```

获取物品占据背包格子数
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品占据背包格子数 |

### `GetCellCapacity`

```text
GetCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> number
```

获取解锁背包格子容量
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包格子容量 |

### `GetMaxCellCapacity`

```text
GetMaxCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> number
```

获取背包格子容量上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 背包格子容量上限 |

### `AddCellCapacity`

```text
AddCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, AddCount: number) -> boolean
```

增加解锁背包格子容量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `AddCount` | `number` | 要增加的容量数 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否增加成功 |

### `AddMaxCellCapacity`

```text
AddMaxCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, AddCount: number) -> boolean
```

增加背包格子容量上限(同时增加解锁格子数)
生效范围：服务器

背包物品同款功能，扩充额外的容量
扩充的容量不会持久化(与背包扩容不同)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `AddCount` | `number` | 要增加的容量数 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否增加成功 |

### `RemoveMaxCellCapacity`

```text
RemoveMaxCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, RemoveCount: number) -> boolean
```

减少背包格子容量上限(同时减少解锁格子数)
生效范围：服务器

背包物品同款功能，减掉扩充的额外容量
减扩的容量不会持久化(与背包扩容不同)
使用此接口后，如果有持久化物品，跨对局后可能因为新对局中容量不足而导致物品超限(超限后默认将自动丢弃超限物品)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `RemoveCount` | `number` | 要减少的容量数 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否减少成功 |

### `GetWarehouseCellCapacity`

```text
GetWarehouseCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> number
```

获取解锁仓库格子容量
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 仓库格子容量 |

### `GetWarehouseMaxCellCapacity`

```text
GetWarehouseMaxCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> number
```

获取仓库格子容量上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 仓库格子容量上限 |

### `AddWarehouseCellCapacity`

```text
AddWarehouseCellCapacity(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, AddCount: number) -> boolean
```

增加仓库格子容量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `AddCount` | `number` | 要增加的容量数 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否增加成功 |

### `GetAllCellItemDefineIDsV2`

```text
GetAllCellItemDefineIDsV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> ItemDefineID[]
```

获取所有占背包格子的物品实例
Attach 附加到其它物品上的物品，或装备在背包上的物品，不占用背包格子。
货币类型不占用背包格子。
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 所有占背包格子的物品 DefineID |

### `GetAllCellWarehouseItemDefineIDsV2`

```text
GetAllCellWarehouseItemDefineIDsV2(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> ItemDefineID[]
```

获取所有占仓库格子的物品实例
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `ItemDefineID[]` | 所有占仓库格子的物品 DefineID |

### `IsCellCapacityFull`

```text
IsCellCapacityFull(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> boolean
```

背包格子是否已满
客户端数据可能稍微滞后
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 背包格子是否已满 |

### `GetCurrencyIDList`

```text
GetCurrencyIDList(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器) -> int[]
```

获取货币类型的物品ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

**Returns**

| Type | Description |
|---|---|
| `int[]` | 所有货币物品ID |

### `IsCurrency`

```text
IsCurrency(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemID: number) -> boolean
```

物品是否为货币
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemID` | `number` | 物品ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 物品是否为货币 |

### `OpenBackpackPanelStyle`

```text
OpenBackpackPanelStyle(Style: number, Mode: number)
```

打开背包主界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Style` | `number` | [0:全屏背包, 1:半屏背包, nil:读默认配置] |
| `Mode` | `number` | [1:背包 + 装备 2:背包 + 仓库 3:背包 + 仓库 + 装备 nil:读默认配置] |

### `OpenBackpackPanel`

```text
OpenBackpackPanel(Mode: number)
```

打开背包主界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mode` | `number` | 1:背包 + 装备 2:背包 + 仓库 3:背包 + 仓库 + 装备 [4-6]同1-3，形式为半屏背包 |

### `CloseBackpackPanel`

```text
CloseBackpackPanel()
```

关闭背包主界面
生效范围：客户端

### `DisableItemNewFlag`

```text
DisableItemNewFlag(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, bForever: boolean)
```

失效物品新标记, 会触发背包Update事件
生效范围：客户端 & 服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `bForever` | `boolean` | true:始终无效，影响后续新物品 false:仅无效当前背包物品 |

### `RemoveItemNewFlag`

```text
RemoveItemNewFlag(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: FItemDefineID)
```

移除某个物品的新标记，会触发背包Update事件
生效范围：客户端 & 服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `FItemDefineID` | 物品DefineID |

### `EnableItemNewFlag`

```text
EnableItemNewFlag(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器)
```

激活物品新标记
生效范围：客户端 & 服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |

### `GetItemIsNew`

```text
GetItemIsNew(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, ItemDefineID: FItemDefineID)
```

查询物品新标记
生效范围：客户端 & 服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `ItemDefineID` | `FItemDefineID` | 物品DefineID |

### `SetEquipSlotEnable`

```text
SetEquipSlotEnable(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, SlotName: string)
```

启用背包槽位
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `SlotName` | `string` | 槽位名称 |

### `GetEquipSlotEnable`

```text
GetEquipSlotEnable(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, SlotName: string) -> boolean
```

获取背包槽位启用状态
生效范围：服务端&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `SlotName` | `string` | 槽位名称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 槽位是否启用 |

### `GetCustomUIWidget`

```text
GetCustomUIWidget(Player: PlayerPawn | PlayerController @玩家角色或者玩家控制器, Type: ECustomUIType, DefineID: ItemDefineID) -> UserWidget
```

获取指定类型的自定义控件（打开过背包才会添加自定义控件）
生效范围：客户端
注意，背包UI在物品变更后延时刷新，不要在添加物品后 立即获取格子自定义控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `PlayerPawn \| PlayerController @玩家角色或者玩家控制器` | 玩家角色或者玩家控制器 |
| `Type` | `ECustomUIType` | 自定义控件种类 |
| `DefineID` | `ItemDefineID` | 查询具体实例的格子自定义UI |

**Returns**

| Type | Description |
|---|---|
| `UserWidget` | 自定义控件 \| UserWidget[] @自定义控件数组 |

### `SetBackpackButtonVisible`

```text
SetBackpackButtonVisible(Visible: boolean)
```

显隐背包按钮
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Visible` | `boolean` | 是否可见 |

### `SetItemListPanelVisible`

```text
SetItemListPanelVisible(InVisibility: ESlateVisibility)
```

设置背包物品列表面板的显隐
生效范围：客户端，仅背包打开时生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | 目标可见性 |

### `SetEquipmentPanelVisible`

```text
SetEquipmentPanelVisible(InVisibility: ESlateVisibility)
```

设置装备栏面板的显隐
生效范围：客户端，仅背包打开时生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | 目标可见性 |

### `SetWarehousePanelVisible`

```text
SetWarehousePanelVisible(InVisibility: ESlateVisibility)
```

设置仓库面板的显隐
生效范围：客户端，仅背包打开时生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | 目标可见性 |

### `SetBackpackSubPanelsVisible`

```text
SetBackpackSubPanelsVisible(InVisibility: ESlateVisibility)
```

一次性设置所有子面板的显隐（统一使用同一个 Visibility）
生效范围：客户端，仅背包打开时生效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | 所有子面板的目标可见性 |

### `GetItemListPanelVisible`

```text
GetItemListPanelVisible() -> ESlateVisibility
```

获取背包物品列表面板的显隐状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | 面板的 Visibility 值 |

### `GetEquipmentPanelVisible`

```text
GetEquipmentPanelVisible() -> ESlateVisibility
```

获取装备栏面板的显隐状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | 面板的 Visibility 值 |

### `GetWarehousePanelVisible`

```text
GetWarehousePanelVisible() -> ESlateVisibility
```

获取仓库面板的显隐状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | 面板的 Visibility 值 |

### `GetUISelectItemChangeDelegate`

```text
GetUISelectItemChangeDelegate() -> Delegate
```

获取背包UI选中态变化委托
生效范围：客户端
背包控件的选中数据 SelectData:
背包格子：table {ItemDefineID:物品DefineID, DataType:string, ItemIdx:格子位置索引, WeakWidget:控件弱引用,通过WeakWidget:Get()获取控件}
其他控件(装备、武器、槽位): table {ItemDefineID:物品DefineID, DataType:string, WeakWidget:控件弱引用}
可以通过DataType判断点击了哪个区域的UI控件，背包内核UI对应的DataType定义在EItemDataTypeStrs

**Returns**

| Type | Description |
|---|---|
| `Delegate` | 选中变化委托 {table:控件选中数据, boolean:是否选中} |

### `CreateCommonItemWidget`

```text
CreateCommonItemWidget(CanvasPanel: UCanvasPanel, Callback: function)
```

异步创建CommonItem格子控件并挂到指定容器
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CanvasPanel` | `UCanvasPanel` | 挂载容器 |
| `Callback` | `function` | 创建完成回调，参数为创建好的CommonItem控件（可能为nil） |

### `GetBackpackDragDropWidget`

```text
GetBackpackDragDropWidget(PlayerController: PlayerController)
```

获取背包UI的拖拽控件
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |

### `SetDefaultShowSettings`

```text
SetDefaultShowSettings(PanelType: ESubPanelType, Visibility: ESlateVisibility)
```

修改背包UI子面板的默认显隐设置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PanelType` | `ESubPanelType` | 子面板类型（Backpack/Equippment/Warehouse） |
| `Visibility` | `ESlateVisibility` | 目标 Visibility 值（如 ESlateVisibility.SelfHitTestInvisible / ESlateVisibility.Collapsed） |

### `GetDetailsWidgetCustomPathByItemID`

```text
GetDetailsWidgetCustomPathByItemID(PlayerController: PlayerController, ItemID: number) -> string[]
```

获取物品详情面板的自定义叠加控件路径列表
开放化控件通过此接口获取自定义详情控件路径，避免直接引用 BackpackManager
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 |
| `ItemID` | `number` | 物品配置ID |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 自定义控件蓝图路径列表，未配置时返回空表 |

### `FindItemInTable`

```text
FindItemInTable()
```

生效范围：客户端

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCBuffSystem.json -->

# UGCBuffSystem

【废弃】Buff 系统接口库

## Functions

### `GetBuffSystemComponent`

```text
GetBuffSystemComponent(PlayerPawn: PlayerPawn) -> BuffSystemComponent
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色。所有的接口里的 PlayerPawn 都可以扩展成任意的 Actor，只要这个 Actor 有一个名字叫 BuffSystemComponent 的 Buff 组件即可。 |

**Returns**

| Type | Description |
|---|---|
| `BuffSystemComponent` | USTBaseBuffSystemComponent |

### `AddBuff`

```text
AddBuff(PlayerPawn: PlayerPawn, BuffName: string, LayerCount: number, BuffCauser: Controller, CauserActor: Actor) -> number
```

【废弃】请使用 UGCPersistEffectSystem
为玩家添加 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色。所有的接口里的 PlayerPawn 都可以扩展成任意的 Actor，只要这个 Actor 有一个名字叫 BuffSystemComponent 的 Buff 组件即可。 |
| `BuffName` | `string` | Buff 名 |
| `LayerCount` | `number` | 层数 |
| `BuffCauser` | `Controller` | 施加 Buff 的玩家或 AI 的控制器 |
| `CauserActor` | `Actor` | 施加 Buff 的 Actor，比如说 PlayerPawn、燃烧瓶 Actor 等等 |

**Returns**

| Type | Description |
|---|---|
| `number` | Buff 唯一 ID |

### `RemoveBuff`

```text
RemoveBuff(PlayerPawn: PlayerPawn, BuffName: string, LayerCount: number)
```

【废弃】请使用 UGCPersistEffectSystem
为玩家移除 Buff,本帧内不即时移除
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |
| `LayerCount` | `number` | 层数 |

### `RemoveBuffByInstanceID`

```text
RemoveBuffByInstanceID(PlayerPawn: PlayerPawn, InstanceID: number, LayerCount: number)
```

【废弃】请使用 UGCPersistEffectSystem
使用唯一 ID 移除 Buff，本帧内不即时移除
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `InstanceID` | `number` | Buff 唯一 ID |
| `LayerCount` | `number` | 层数 |

### `HasBuff`

```text
HasBuff(PlayerPawn: PlayerPawn, BuffName: string) -> boolean
```

【废弃】请使用 UGCPersistEffectSystem
是否存在该 Buff
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否存在 Buff |

### `GetCurLayer`

```text
GetCurLayer(PlayerPawn: PlayerPawn, BuffName: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 当前层数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `number` | 层数 |

### `GetMaxLayer`

```text
GetMaxLayer(PlayerPawn: PlayerPawn, BuffName: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 最大层数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大层数 |

### `GetLeftTime`

```text
GetLeftTime(PlayerPawn: PlayerPawn, BuffName: string) -> number
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 剩余持续时间
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `BuffName` | `string` | Buff 名 |

**Returns**

| Type | Description |
|---|---|
| `number` | 剩余持续时间 |

### `GetBuffCauserActor`

```text
GetBuffCauserActor(PlayerPawn: PlayerPawn, InstanceID: number) -> Actor
```

【废弃】请使用 UGCPersistEffectSystem
获取 Buff 的施加者
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | Buff |
| `InstanceID` | `number` | Buff 唯一 ID |

**Returns**

| Type | Description |
|---|---|
| `Actor` | Buff 施加者（弱引用，需使用 Actor:Get() 获取实际对象） |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%A7%92%E8%89%B2%E7%B3%BB%E7%BB%9F/UGCCameraManagerSystem.json -->

# UGCCameraManagerSystem

相机管理器系统接口库

## Functions

### `GetInVehicleFPPViewPitchLimitMin`

```text
GetInVehicleFPPViewPitchLimitMin() -> @Pitch
```

获得第一人称视角下在载具内的 Pitch 视角限制（最小值）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `@Pitch` | 视角限制（最小值） |

### `SetInVehicleFPPViewPitchLimitMin`

```text
SetInVehicleFPPViewPitchLimitMin(PitchLimit: number)
```

设置第一人称视角下在载具内的 Pitch 视角限制（最小值）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PitchLimit` | `number` | Pitch 视角限制（最小值） |

### `GetInVehicleFPPViewYawLimit`

```text
GetInVehicleFPPViewYawLimit() -> @Yaw
```

获得第一人称视角下在载具内的 Yaw 视角限制
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `@Yaw` | 视角限制 |

### `SetInVehicleFPPViewYawLimit`

```text
SetInVehicleFPPViewYawLimit(YawLimit: number)
```

设置第一人称视角下在载具内的 Yaw 视角限制
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YawLimit` | `number` | Yaw 视角限制 |

### `GetInVehicleNarrowSeatGrenadesYawLimit`

```text
GetInVehicleNarrowSeatGrenadesYawLimit() -> @Yaw
```

获得在载具内的狭窄座位手雷投掷 Yaw 视角限制
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `@Yaw` | 视角限制 |

### `SetInVehicleNarrowSeatGrenadesYawLimit`

```text
SetInVehicleNarrowSeatGrenadesYawLimit(YawLimit: number)
```

设置在载具内的狭窄座位手雷投掷 Yaw 视角限制
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `YawLimit` | `number` | Yaw 视角限制 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCCampSystem.json -->

# UGCCampSystem

阵营接口库

## Functions

### `AddCamp`

```text
AddCamp(InCampName: string) -> number
```

增加阵营
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCampName` | `string` | 阵营名称 |

**Returns**

| Type | Description |
|---|---|
| `number` | 通过CampName创建的阵营ID，CampName与CampID都是阵营唯一标识符 |

### `SetCampForActor`

```text
SetCampForActor(InActor: AActor, InCampID: number)
```

设置非玩家Actor所属阵营，例如设置怪物的阵营
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | AActor |
| `InCampID` | `number` | 阵营ID |

### `SetCampForTeam`

```text
SetCampForTeam(InTeamID: number, InCampID: number) -> boolean
```

设置队伍所属阵营
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTeamID` | `number` | 队伍ID |
| `InCampID` | `number` | 阵营ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 设置队伍所属阵营是否成功 |

### `GetCampIDByActor`

```text
GetCampIDByActor(InActor: AActor) -> number
```

通过非玩家Actor获取阵营ID，获取失败的时候返回-1
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | AActor |

**Returns**

| Type | Description |
|---|---|
| `number` | 阵营ID |

### `GetCampNameByActor`

```text
GetCampNameByActor(InActor: AActor) -> string
```

通过非玩家Actor获取阵营名称，获取失败的时候返回空字符串
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor` | AActor |

**Returns**

| Type | Description |
|---|---|
| `string` | 阵营名称 |

### `GetCampIDByTeamID`

```text
GetCampIDByTeamID(InTeamID: number) -> number
```

通过队伍ID获取阵营ID，获取失败的时候返回-1
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTeamID` | `number` | 队伍ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 阵营ID |

### `GetCampNameByTeamID`

```text
GetCampNameByTeamID(InTeamID: number) -> string
```

通过队伍ID获取阵营名称，获取失败的时候返回空字符串
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTeamID` | `number` | 队伍ID |

**Returns**

| Type | Description |
|---|---|
| `string` | 阵营名称 |

### `SetDefaultCampRelation`

```text
SetDefaultCampRelation(InCampRelation: ECampRelation)
```

设置默认阵营关系
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCampRelation` | `ECampRelation` | 阵营关系,1:友好,2:中立,3:敌对 |

### `SetCampRelation`

```text
SetCampRelation(InCampA_ID: number, InCampB_ID: number, InCampRelation: ECampRelation)
```

设置两个阵营之间的阵营关系
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCampA_ID` | `number` | 阵营A ID |
| `InCampB_ID` | `number` | 阵营B ID |
| `InCampRelation` | `ECampRelation` | 阵营关系,0:友好,1:中立,2:敌对 |

### `GetCampRelation`

```text
GetCampRelation(InCampA_ID: number, InCampB_ID: number) -> ECampRelation
```

获取两个阵营之间的阵营关系，获取失败默认返回中立
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCampA_ID` | `number` | 阵营A ID |
| `InCampB_ID` | `number` | 阵营B ID |

**Returns**

| Type | Description |
|---|---|
| `ECampRelation` | 阵营关系,1:友好,2:中立,3:敌对 |

### `GetCampRelationWithActor`

```text
GetCampRelationWithActor(InActorA: AActor, InActorB: AActor) -> ECampRelation
```

获取两个Actor之间的阵营关系，获取失败默认返回中立
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActorA` | `AActor` | AActor |
| `InActorB` | `AActor` | AActor |

**Returns**

| Type | Description |
|---|---|
| `ECampRelation` | 阵营关系,1:友好,2:中立,3:敌对 |

### `SetCampDefaultSpawnMethod`

```text
SetCampDefaultSpawnMethod(InCampID: number, SpawnPointSelectionMethod: EUGCCampSpawnPointSelectionMethod, SpawnMethodInfo: FVector|uint8, PlayerStartInfo: boolean)
```

设置阵营出生方式
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCampID` | `number` | 阵营ID |
| `SpawnPointSelectionMethod` | `EUGCCampSpawnPointSelectionMethod` | 阵营出生方式 |
| `SpawnMethodInfo` | `FVector\|uint8` | 指定PlayerStartID或者世界坐标 |
| `PlayerStartInfo` | `boolean` | 是否随机出生点ID |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCCharAvatarShowcaseActor.json -->

# UGCCharAvatarShowcaseActor

复制玩家角色Avatar的Actor

## Functions

### `ClientShowAvatar`

```text
ClientShowAvatar(PlayerUID: number)
```

显示PlayerUID的Avatar
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerUID` | `number` | 玩家的 PlayerUID |

### `ServerShowAvatar`

```text
ServerShowAvatar(PlayerUID: number)
```

显示PlayerUID的Avatar
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerUID` | `number` | 玩家的 PlayerUID |

### `PlayAnim`

```text
PlayAnim(NewAnimToPlay: UAnimationAsset, bLooping: boolean)
```

播放动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAnimToPlay` | `UAnimationAsset` | 动画资源 |
| `bLooping` | `boolean` | 是否循环播放 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCCircleManagerSystem.json -->

# UGCCircleManagerSystem

信号圈系统接口库

## Functions

### `GetBlueCircleCenter`

```text
GetBlueCircleCenter() -> Vector2D
```

获取当前蓝圈中心
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `Vector2D` | 蓝圈中心 {X，Y} |

### `GetWhiteCircleCenter`

```text
GetWhiteCircleCenter() -> Vector2D
```

获取当前白圈中心
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `Vector2D` | 白圈中心 {X，Y} |

### `GetBlueCircleRadius`

```text
GetBlueCircleRadius() -> number
```

获取当前蓝圈半径
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 半径 |

### `GetWhiteCircleRadius`

```text
GetWhiteCircleRadius() -> number
```

获取当前白圈半径
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 半径 |

### `GetCurrentCircleIndex`

```text
GetCurrentCircleIndex() -> number
```

获得当前运行到的信号圈序号
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `number` | 信号圈序号 缩圈结束时，返回最后一个信号圈序号 |

### `GetAllCircleConfig`

```text
GetAllCircleConfig() -> FCirCleCfg[]
```

获得所有信号圈配置
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `FCirCleCfg[]` | 所有信号圈配置 |

### `GetCurrentConfigCircle`

```text
GetCurrentConfigCircle() -> FCirCleCfg
```

获取当前信号圈配置
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `FCirCleCfg` | 当前信号圈配置 |

### `GetNextConfigCircle`

```text
GetNextConfigCircle() -> FCirCleCfg
```

获取下一信号圈配置
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `FCirCleCfg` | 下一信号圈配置 |

### `TogglePoisonCircle`

```text
TogglePoisonCircle() -> boolean
```

开启或者关闭信号圈（关闭状态则开启，开启状态则关闭）
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | 调用后状态为开启或者关闭 |

### `StartCircle`

```text
StartCircle()
```

启用信号圈
生效范围：服务器

### `StopCircle`

```text
StopCircle()
```

关闭信号圈
生效范围：服务器

### `PauseCircle`

```text
PauseCircle()
```

暂停信号圈
生效范围：服务器

### `ResumeCircle`

```text
ResumeCircle()
```

恢复暂停信号圈
生效范围：服务器

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/UGCCommoditySystem.json -->

# UGCCommoditySystem

商业化库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCCommoditySystemImplementation.UseUGCCommodityResultDelegate` | `-` | - |
| `UGCCommoditySystem.BuyUGCCommodityResultDelegate` | `-` | 玩家购买商品后广播<br>生效范围：服务器&客户端 |
| `UGCCommoditySystem.CompensateUGCCommodityDelegate` | `-` | 补偿玩家商品后广播<br>生效范围：服务器&客户端<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityID number @物品ID<br>@param Count number @物品数量<br>@param ProductID number @商品ID |
| `UGCCommoditySystem.CompensateUGCCommodityBatchDelegate` | `-` | 补偿玩家商品后批量广播<br>生效范围：服务器<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityList table @补偿列表 |
| `UGCCommoditySystem.UseRedemptionCodeResultDelegate` | `-` | 玩家使用兑换码后逐个物品广播<br>生效范围：服务器&客户端<br>@param Result EUseRedemptionCodeResult @使用兑换码结果<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityID number @物品ID<br>@param Count number @物品数量<br>@param ProductID number @商品ID |
| `UGCCommoditySystem.UseRedemptionCodeBatchResultDelegate` | `-` | 玩家使用兑换码后批量广播<br>生效范围：服务器<br>@param Result EUseRedemptionCodeResult @使用兑换码结果<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityList table @兑换列表 |
| `UGCCommoditySystem.BuyUGCCommodityResultBetweenGamesDelegate` | `-` | 如果本次游戏对局的商品数据跟上一局结算时的物品数据有差异，那么服务端会在 PlayerController:Server_OnUGCCommodityPlayerDataReady() 之前广播此 Delegate<br>可以在PlayerController:ReceiveBeginPlay() 里监听这个 Delegate<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityID number @物品ID<br>@param Count number @物品数量<br>生效范围：服务器 |
| `UGCCommoditySystem.UseUGCCommodityResultDelegate` | `-` | 物品使用时广播<br>生效范围：服务器&客户端 |
| `UGCCommoditySystem.UGCProductsChangedDelegate` | `-` | 在商品列表发生变化时广播<br>生效范围：服务器&客户端 |
| `UGCCommoditySystem.UGCCommodityPlayerDataChangedDelegate` | `-` | 在UGCCommoditySystem.GetAllPlayerUGCCommodityList() 和 UGCCommoditySystem.GetUGCCommodityList()返回值发生改变时广播<br>生效范围：服务器&客户端 |
| `UGCCommoditySystem.BuyUGCCommodityBatchResultDelegate` | `-` | 批量购买结果广播<br>生效范围：服务器&客户端<br>@param bSuccess boolean @是否成功<br>@param PlayerKey number @玩家PlayerKey<br>@param UID number @玩家UID<br>@param CommodityList table @购买结果列表 {{CommodityID=, Count=}, ...}<br>@param Context string @上下文 |

## Functions

### `GetTicket`

```text
GetTicket(PlayerKey: number) -> number
```

获取玩家货币(绿洲币/灰度币)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家PlayerKey，服务器调用必传 |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家货币 |

### `GetActiveCoin`

```text
GetActiveCoin(PlayerKey: number) -> number
```

获取启元币
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家PlayerKey，服务器调用必传 |

**Returns**

| Type | Description |
|---|---|
| `number` | 启元币 |

### `BuyUGCCommodity`

```text
BuyUGCCommodity(BuyCommodityCMD: string, Name: string, Icon: string, Desc: string, Count: number, Cost: number) -> PromiseFuture
```

购买绿洲商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuyCommodityCMD` | `string` | 购买协议，参考：EUGCCommodityCommandType |
| `Name` | `string` | 物品的名称 |
| `Icon` | `string` | 物品图标 |
| `Desc` | `string` | 物品的描述 |
| `Count` | `number` | 单次购买的数量 |
| `Cost` | `number` | 单个物品的价格 Cost 必须传入 UGCCommoditySystem.GetSellingPriceAfterDiscount 的返回值 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 二次确认弹窗界面对象实例的 PromiseFuture 对象 |

### `BuyUGCPrivilegeCommodity`

```text
BuyUGCPrivilegeCommodity(BuyCommodityCMD: string, Name: string, Icon: string, Desc: string, Count: number, Cost: number) -> PromiseFuture
```

购买绿洲特权商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuyCommodityCMD` | `string` | 购买协议，参考：EUGCCommodityCommandType |
| `Name` | `string` | 物品的名称 |
| `Icon` | `string` | 物品图标 |
| `Desc` | `string` | 物品的描述 |
| `Count` | `number` | 单次购买的数量 |
| `Cost` | `number` | 单个物品的价格 Cost 必须传入 UGCCommoditySystem.GetSellingPriceAfterDiscount 的返回值 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 二次确认弹窗界面对象实例的 PromiseFuture 对象 |

### `BuyUGCCommodity2`

```text
BuyUGCCommodity2(ProductID: number, Icon: string, Desc: string, Count: number) -> PromiseFuture
```

购买绿洲商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品 ID |
| `Icon` | `string` | 物品图标 |
| `Desc` | `string` | 物品的描述 |
| `Count` | `number` | 单次购买的数量 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 二次确认弹窗界面对象实例的 PromiseFuture 对象 |

### `BuyUGCPrivilegeCommodity2`

```text
BuyUGCPrivilegeCommodity2(ProductID: number, Icon: string, Desc: string, Count: number) -> PromiseFuture
```

购买绿洲特权商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品 ID |
| `Icon` | `string` | 物品图标 |
| `Desc` | `string` | 物品的描述 |
| `Count` | `number` | 单次购买的数量 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 二次确认弹窗界面对象实例的 PromiseFuture 对象 |

### `BuyUGCCommodityBatch`

```text
BuyUGCCommodityBatch(BuyList: table) -> PromiseFuture
```

批量购买绿洲商品
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuyList` | `table` | 购买列表 {{ProductID=number, Count=number, bCheckPrivilege=boolean}, ...} |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 二次确认弹窗界面对象实例的 PromiseFuture 对象 |

### `UseUGCCommodity`

```text
UseUGCCommodity(UseCommodityCMD: string, CommodityID: number, Name: string, Icon: string, Desc: string, Count: number, bShowDialog: boolean) -> PromiseFuture
```

使用绿洲物品
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UseCommodityCMD` | `string` | 使用协议，参考：EUGCCommodityCommandType |
| `CommodityID` | `number` | 物品ID |
| `Name` | `string` | 物品的名称 |
| `Icon` | `string` | 物品图标 |
| `Desc` | `string` | 物品的描述 |
| `Count` | `number` | 单次消耗的数量 |
| `bShowDialog` | `boolean` | 是否二次确认 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | bShowDialog 为 true 的情况下，返回二次确认弹窗界面对象实例的 PromiseFuture 对象 |

### `UseUGCCommodity2`

```text
UseUGCCommodity2(PlayerController: PlayerController, ObjectID: number, Icon: string, Desc: string, Count: number, bShowDialog: boolean) -> PromiseFuture
```

使用绿洲物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `PlayerController` | 玩家控制器 在 DS 端调用的话 PlayerController 必须传，客户端可传 nil，否则调用无效 |
| `ObjectID` | `number` | 物品ID |
| `Icon` | `string` | 物品图标，填 nil 则使用 UGCObject.ItemSmallIcon（UGCObject 表格中的 ItemSmallIcon（小icon） 字段） |
| `Desc` | `string` | 物品的描述，填 nil 则使用 UGCObject.ItemDesc（UGCObject 表格中的 ItemDesc（物品描述） 字段） |
| `Count` | `number` | 单次消耗的数量 |
| `bShowDialog` | `boolean` | bShowDialog 在 DS 忽略 |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | bShowDialog 为 true 的情况下，返回二次确认弹窗界面对象实例的 PromiseFuture 对象(仅客户端调用) |

### `RegBuyCMD`

```text
RegBuyCMD(BuyCommodityCMD: string, ProductID: number, Count: number)
```

注册商品购买协议
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuyCommodityCMD` | `string` | 购买协议，参考：EUGCCommodityCommandType |
| `ProductID` | `number` | 商品的ID |
| `Count` | `number` | 单次购买的数量 |

### `RegUseCMD`

```text
RegUseCMD(UseCommodityCMD: string, CommodityID: number, Count: number)
```

注册使用物品协议
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UseCommodityCMD` | `string` | 使用商品协议，参考：EUGCCommodityCommandType |
| `CommodityID` | `number` | 物品的ID |
| `Count` | `number` | 单次消耗的数量 |

### `UseRedemptionCode`

```text
UseRedemptionCode(UID: number, RedemptionCode: string)
```

使用兑换码
PIE下调用该接口默认兑换成功，触发兑换结果 {ItemID=1001, Count=1, ProductID=900001}
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家的UID |
| `RedemptionCode` | `string` | 兑换码 |

### `GetAllPlayerUGCCommodityList`

```text
GetAllPlayerUGCCommodityList() -> table
```

获取所有玩家的物品数据
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `table` | 战斗服务器中所有玩家的物品数据列表 |

### `GetUGCCommodityList`

```text
GetUGCCommodityList(PlayerKey: number) -> table
```

获取主控端物品数据
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家PlayerKey，服务器调用必传 |

**Returns**

| Type | Description |
|---|---|
| `table` | 客户端所属玩家的物品数据列表 |

### `GetAllPlayerUGCProductList`

```text
GetAllPlayerUGCProductList() -> table
```

获取所有玩家的绿洲商品限购数据
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `table` | 战斗服务器中所有玩家的商品限购数据列表 |

### `GetUGCProductList`

```text
GetUGCProductList() -> table
```

获取所有玩家的绿洲商品限购数据
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `table` | 主控端玩家的商品限购数据列表 |

### `ClearCommodity`

```text
ClearCommodity()
```

清空所有已购买物品
生效范围：客户端

### `GetSellingPriceAfterDiscount`

```text
GetSellingPriceAfterDiscount(BuyCommodityCMDOrProductID: string|int) -> number
```

获取折扣后商品价格 
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuyCommodityCMDOrProductID` | `string\|int` | 购买商品协议 或者 商品ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 如果参数无效返回 nil 如果存在折扣返回折扣后的商品售价，否则返回商品表配置的售卖价格（SellingPrice） |

### `OpenRedeemPage`

```text
OpenRedeemPage()
```

打开兑换码页面
生效范围：客户端

### `ShowRechargeEntryUI`

```text
ShowRechargeEntryUI() -> PromiseFuture
```

显示绿洲币充值界面
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 绿洲币充值界面对象实例的PromiseFuture对象 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCCommonDragDropItem.json -->

# UGCCommonDragDropItem

拖拽控件

## Functions

### `SetDragWidget`

```text
SetDragWidget(Widget: UUserWidget|Class, bCreate: boolean)
```

设置拖拽时的控件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UUserWidget\|Class` | 拖拽时的控件实例 或 类 |
| `bCreate` | `boolean` | 是否创建控件，传入Class则创建控件实例 |

### `SetDragDirectionMode`

```text
SetDragDirectionMode(DirectionMode: EDragDirectionMode)
```

设置拖拽方向模式

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DirectionMode` | `EDragDirectionMode` | 拖拽方向模式 |

### `SetDragDropMode`

```text
SetDragDropMode(DragDropMode: EDragDropMode)
```

设置拖拽模式

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DragDropMode` | `EDragDropMode` | 拖拽模式 |

### `RegisterDragDropData`

```text
RegisterDragDropData(DragDropData: table, DragDropMode: EDragDropMode, InDragWidgetClass: FSoftClassPath|string)
```

注册拖拽(入口), 仅执行一次有效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DragDropData` | `table` | 拖拽数据，在拖拽响应事件中传递 |
| `DragDropMode` | `EDragDropMode` | 拖拽模式 |
| `InDragWidgetClass` | `FSoftClassPath\|string` | 可选，自定义拖拽控件类 |

### `SetData`

```text
SetData(Data: table)
```

设置拖拽数据

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `table` | 拖拽数据 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCCommonUISystem.json -->

# UGCCommonUISystem

UI通用响应库

## Functions

### `AddDragSuccess`

```text
AddDragSuccess(InFunc: function, Context: table)
```

拖拽成功添加监听
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFunc` | `function` | 回调函数 |
| `Context` | `table` | 函数上下文 |

### `RemoveDragSuccess`

```text
RemoveDragSuccess(InFunc: function, Context: table)
```

拖拽成功移除监听
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFunc` | `function` | 回调函数 |
| `Context` | `table` | 函数上下文 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCDebugSystem.json -->

# UGCDebugSystem

调试系统接口库

## Functions

### `PrintToScreen`

```text
PrintToScreen(InString: string, Color: FLinearColor, Duration: number)
```

屏幕左上角逐行打印字符串
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `string` | 要打印的字符串 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `FlushOnScreenDebugMessages`

```text
FlushOnScreenDebugMessages()
```

清除屏幕上持续时间未过的字符串
生效范围：客户端

### `DrawDebugLine`

```text
DrawDebugLine(LineStart: FVector, LineEnd: FVector, Color: FLinearColor, Duration: number)
```

绘制直线
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LineStart` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `LineEnd` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugPoint`

```text
DrawDebugPoint(Position: FVector, Size: number, Color: FLinearColor, Duration: number)
```

绘制点
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Size` | `number` | 点的大小 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugArrow`

```text
DrawDebugArrow(LineStart: FVector, LineEnd: FVector, Color: FLinearColor, Duration: number)
```

绘制箭头
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LineStart` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `LineEnd` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugCircle`

```text
DrawDebugCircle(Center: FVector, Radius: number, Color: FLinearColor, Duration: number, YAxis: FVector, ZAxis: FVector, bDrawAxis: boolean)
```

绘制圆
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Radius` | `number` | 圆的半径 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |
| `YAxis` | `FVector` | 椭圆半长轴方向向量，模长影响缩放; 缺省为{X=0,Y=1,Z=0}; 结构Vector={X=0,Y=0,Z=0} |
| `ZAxis` | `FVector` | 椭圆半短轴方向向量，模长影响缩放; 缺省为{X=0,Y=0,Z=1}; 结构Vector={X=0,Y=0,Z=0} |
| `bDrawAxis` | `boolean` | 缺省为0 |

### `DrawDebugCoordinateSystem`

```text
DrawDebugCoordinateSystem(AxisLoc: FVector, AxisRot: FRotator, Scale: number, Duration: number)
```

绘制坐标系
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisLoc` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `AxisRot` | `FRotator` | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| `Scale` | `number` | 坐标轴长度; 缺省为100 |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugBox`

```text
DrawDebugBox(Center: FVector, Extent: FVector, Rotation: FRotator, Color: FLinearColor, Duration: number)
```

绘制盒子
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Extent` | `FVector` | 表示盒子中心到各面的距离; 结构Vector={X=0,Y=0,Z=0} |
| `Rotation` | `FRotator` | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugSphere`

```text
DrawDebugSphere(Center: FVector, Radius: number, Color: FLinearColor, Duration: number)
```

绘制球体
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Radius` | `number` | 球的半径 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugCylinder`

```text
DrawDebugCylinder(Start: FVector, End: FVector, Radius: number, Color: FLinearColor, Duration: number)
```

绘制圆柱体
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Radius` | `number` | 底面半径 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugCapsule`

```text
DrawDebugCapsule(Center: FVector, HalfHeight: number, Radius: number, Rotation: FRotator, Color: FLinearColor, Duration: number)
```

绘制胶囊
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `HalfHeight` | `number` | 胶囊半高 |
| `Radius` | `number` | 截面圆半径 |
| `Rotation` | `FRotator` | 结构Rot={Pitch=0,Yaw=0,Roll=0}; |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugString`

```text
DrawDebugString(TextLocation: FVector, Text: string, TestBaseActor: AActor, Color: FLinearColor, Duration: number)
```

绘制文本
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextLocation` | `FVector` | 未绑定Actor时为世界坐标，绑定Actor时为相对Actor的坐标; 结构Vector={X=0,Y=0,Z=0} |
| `Text` | `string` | 显示的文本 |
| `TestBaseActor` | `AActor` | 绑定在哪个Actor上 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `FlushDebugStrings`

```text
FlushDebugStrings()
```

清空场景中持续时间未过的调试文本（不包括UI）
生效范围：客户端

### `FlushDebugLines`

```text
FlushDebugLines()
```

清空场景中持续时间未过的调试图形
生效范围：客户端

### `DrawDebugActorName`

```text
DrawDebugActorName(Actor: AActor, Offset: FVector, Color: FLinearColor, Duration: number)
```

绘制Actor名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标Actor |
| `Offset` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugActorMoveTrack`

```text
DrawDebugActorMoveTrack(Actor: AActor, Color: FLinearColor, Duration: number)
```

绘制Actor运动轨迹
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标Actor |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，此时运动轨迹将持续保留 |

### `DrawDebugDistance`

```text
DrawDebugDistance(Self: FVector, Target: FVector, Color: FLinearColor, Duration: number)
```

绘制Self到Target的连线和距离数值
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Self` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Target` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugTargetAimedAt`

```text
DrawDebugTargetAimedAt(Length: number, Duration: number)
```

绘制准心瞄准物体名称
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Length` | `number` | 生效距离，缺省为10000 |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugLineTraceSingle`

```text
DrawDebugLineTraceSingle(Start: FVector, End: FVector, Color: FLinearColor, Duration: number)
```

绘制射线与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugLineTraceMulti`

```text
DrawDebugLineTraceMulti(Start: FVector, End: FVector, Color: FLinearColor, Duration: number)
```

绘制射线与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugSphereTraceSingle`

```text
DrawDebugSphereTraceSingle(Start: FVector, End: FVector, Radius: number, Color: FLinearColor, Duration: number)
```

绘制沿射线运动的球体轨迹与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Radius` | `number` | 球体半径 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugSphereTraceMulti`

```text
DrawDebugSphereTraceMulti(Start: FVector, End: FVector, Radius: number, Color: FLinearColor, Duration: number)
```

绘制沿射线运动的球体轨迹与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Radius` | `number` | 球体半径 |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugBoxTraceSingle`

```text
DrawDebugBoxTraceSingle(Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, Duration: number)
```

绘制沿射线运动的方盒轨迹与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `HalfSize` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Orientation` | `FRotator` | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugBoxTraceMulti`

```text
DrawDebugBoxTraceMulti(Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, Duration: number)
```

绘制沿射线运动的方盒轨迹与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `HalfSize` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Orientation` | `FRotator` | 结构Rot={Pitch=0,Yaw=0,Roll=0} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugCapsuleTraceSingle`

```text
DrawDebugCapsuleTraceSingle(Start: FVector, End: FVector, Radius: number, HalfSize: FVector, Duration: number)
```

绘制沿射线运动的胶囊轨迹与第一处命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Radius` | `number` | 胶囊截面圆半径 |
| `HalfSize` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugCapsuleTraceMulti`

```text
DrawDebugCapsuleTraceMulti(Start: FVector, End: FVector, Radius: number, HalfSize: FVector, Duration: number)
```

绘制沿射线运动的胶囊轨迹与全部命中标记
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `End` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Radius` | `number` | 胶囊截面圆半径 |
| `HalfSize` | `FVector` | 结构Vector={X=0,Y=0,Z=0} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugActorCollision`

```text
DrawDebugActorCollision(Actor: AActor, Color: FLinearColor, Duration: number)
```

绘制碰撞盒
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标Actor |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

### `DrawDebugActorBounds`

```text
DrawDebugActorBounds(Actor: AActor, Color: FLinearColor, Duration: number)
```

绘制包围盒
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标Actor |
| `Color` | `FLinearColor` | 缺省为红色; 结构Color={A=1,B=1,G=1,R=1} |
| `Duration` | `number` | 缺省为0，即每帧调用一次，保持一帧时间 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCDelegateUtility.json -->

# UGCDelegateUtility

UGC 委托工具库

Lua 委托工具
- 使用 New() 创建委托
- 使用 Add(callable, obj) 绑定可调用对象
- 使用 Remove(callable, obj) 解绑可调用对象
- 使用 Broadcast(...) 触发委托

## Functions

### `CreateLuaDelegate`

```text
CreateLuaDelegate() -> @Lua
```

创建 Lua 委托（纯 Lua 实现）

**Returns**

| Type | Description |
|---|---|
| `@Lua` | 委托 |

### `CopyLuaDelegate`

```text
CopyLuaDelegate(Delegate: UGCLuaDelegate) -> UGCLuaDelegate
```

复制 Lua 委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `UGCLuaDelegate` | 被复制的 Lua 委托 |

**Returns**

| Type | Description |
|---|---|
| `UGCLuaDelegate` | 复制出来的新 Lua 委托 |

### `CreateUEDelegate`

```text
CreateUEDelegate(Outer: UObject) -> ULuaSingleDelegate
```

创建虚幻兼容单播委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject` | Outer 对象（GC 相关） |

**Returns**

| Type | Description |
|---|---|
| `ULuaSingleDelegate` | 虚幻兼容单播委托 |

### `DestroyUEDelegate`

```text
DestroyUEDelegate(UEDelegate: ULuaSingleDelegate)
```

销毁虚幻兼容单播委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UEDelegate` | `ULuaSingleDelegate` | 虚幻兼容单播委托 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCDropSystem.json -->

# UGCDropSystem

掉落系统接口库

## Functions

### `DropItems`

```text
DropItems(DropID: number) -> table
```

根据掉落信息进行物品掉落
根据权重掉落：每次掉落一个物品
根据概率掉落：每次根据物品表的物品数量掉落物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DropID` | `number` | 掉落ID |

**Returns**

| Type | Description |
|---|---|
| `table` | 掉落结果 {key-物品ID : value-物品数量} |

### `DropItemsByGroup`

```text
DropItemsByGroup(DropGroupID: number) -> table
```

根据掉落组信息进行物品掉落
掉落组配置参考掉落表格配置（DropGroup Table）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DropGroupID` | `number` | 掉落组ID |

**Returns**

| Type | Description |
|---|---|
| `table` | 掉落结果 {key-物品ID : value-物品数量} |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCEMPZoneManager.json -->

# UGCEMPZoneManager

电磁干扰区管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCEMPZoneManager.SuccessfullyGeneratedElectromagnetic` | `-` | param InstanceID number<br>@param CenterLocation FVector |
| `UGCEMPZoneManager.SuccessfullyStopElectromagnetic` | `-` | param InstanceID number |
| `UGCEMPZoneManager.NormalEndElectromagnetic` | `-` | param InstanceID number |
| `UGCEMPZoneManager.SuccessfullyStartElectromagnetic` | `-` | param InstanceID number |
| `UGCEMPZoneManager.AffectedElectromagneticPlayers` | `-` | param AffectedPlayerKeys number |
| `UGCEMPZoneManager.__EMPZoneMarkTypeID` | `-` | - |
| `UGCEMPZoneManager.__EMPZoneMarkInstIDs` | `-` | - |

## Functions

### `_ValidateAndClampConfig`

```text
_ValidateAndClampConfig(Config: UGCEMPZoneConfig) -> UGCEMPZoneConfig
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Config` | `UGCEMPZoneConfig` | - |

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneConfig` | - |

### `_GetInstanceDetailData`

```text
_GetInstanceDetailData(InstanceID: number) -> table|nil
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | - |

### `_GetConfigByIndex`

```text
_GetConfigByIndex(Index: number) -> table|nil
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | - |

### `_ModifyConfigByIndex`

```text
_ModifyConfigByIndex(Index: number, NewConfig: table) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | - |
| `NewConfig` | `table` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `_GetElectromagneticAreaConfigs`

```text
_GetElectromagneticAreaConfigs(InstanceID: number|nil) -> table|nil
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number\|nil` | - |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | - |

### `_ConvertToLuaConfigs`

```text
_ConvertToLuaConfigs(ElectromagneticInstances: table) -> table
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElectromagneticInstances` | `table` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `_GenerateNextInstanceID`

```text
_GenerateNextInstanceID() -> number
```

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `_MapLuaConfigToComponent`

```text
_MapLuaConfigToComponent(LuaConfig: UGCEMPZoneConfig) -> FEMPZoneCfg
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LuaConfig` | `UGCEMPZoneConfig` | - |

**Returns**

| Type | Description |
|---|---|
| `FEMPZoneCfg` | - |

### `_SyncCapsuleRadius`

```text
_SyncCapsuleRadius(EMPZoneActor: AEMPZoneActor, InstanceData: table) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EMPZoneActor` | `AEMPZoneActor` | - |
| `InstanceData` | `table` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `_WriteConfigToComponent`

```text
_WriteConfigToComponent(Comp: UEMPZoneControlComponent, ComponentConfig: FEMPZoneCfg) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Comp` | `UEMPZoneControlComponent` | - |
| `ComponentConfig` | `FEMPZoneCfg` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `CreateEMPZone`

```text
CreateEMPZone(ConfigID: string, CenterLocation: FVector)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `string` | - |
| `CenterLocation` | `FVector` | - |

### `_CreateEMPZoneActor`

```text
_CreateEMPZoneActor(InstanceID: number) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DestroyElectromagneticArea`

```text
DestroyElectromagneticArea(InstanceID: number) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `_DestroyAllElectromagneticAreas`

```text
_DestroyAllElectromagneticAreas() -> boolean
```

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `ModifyConfigElectromagneticArea`

```text
ModifyConfigElectromagneticArea(ConfigIndex: number, ParameterName: string, NewValue: any) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigIndex` | `number` | - |
| `ParameterName` | `string` | - |
| `NewValue` | `any` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetAllConfigElectromagneticArea`

```text
GetAllConfigElectromagneticArea() -> table
```

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetSpecifyElectromagneticAreaList`

```text
GetSpecifyElectromagneticAreaList(InstanceID: number) -> table
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `_NotifyClientHideMapMark`

```text
_NotifyClientHideMapMark(InstanceID: number)
```

当 EMPZone 销毁时隐藏小地图标记

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

### `Client_OnEMPZoneMapMarkShow`

```text
Client_OnEMPZoneMapMarkShow(InstanceID: number, LocX: number, LocY: number, LocZ: number, EffectRadius: number, ZoneState: number)
```

[Client RPC] 显示 EMPZone 小地图标记

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 实例ID |
| `LocX` | `number` | 位置X坐标 |
| `LocY` | `number` | 位置Y坐标 |
| `LocZ` | `number` | 位置Z坐标 |
| `EffectRadius` | `number` | 影响半径 |
| `ZoneState` | `number` | 区域状态 |

### `Client_OnEMPZoneMapMarkHide`

```text
Client_OnEMPZoneMapMarkHide(InstanceID: number)
```

[Client RPC] 隐藏 EMPZone 小地图标记

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 实例ID |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCEMPZoneSystem.json -->

# UGCEMPZoneSystem

电磁干扰区接口库

## Functions

### `GenerateElectromagneticArea`

```text
GenerateElectromagneticArea(ConfigID: number, Location: FVector) -> number
```

生成电磁干扰区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 电磁干扰区配置 ID |
| `Location` | `FVector` | 电磁干扰区中心坐标 |

**Returns**

| Type | Description |
|---|---|
| `number` | 是否成功生成电磁干扰区, 实例ID |

### `DestroyElectromagneticArea`

```text
DestroyElectromagneticArea(InstanceID: number) -> bool
```

取消电磁干扰区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 电磁干扰区实例 ID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功取消电磁干扰区 |

### `ModifyConfigElectromagneticArea`

```text
ModifyConfigElectromagneticArea(ConfigID: number, ParameterType: string, NewValue: number) -> bool
```

修改电磁干扰区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 电磁干扰区配置 ID |
| `ParameterType` | `string` | 参数类型 |
| `NewValue` | `number` | 新的参数值 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功修改电磁干扰区配置 |

### `GetAllConfigElectromagneticArea`

```text
GetAllConfigElectromagneticArea() -> UGCEMPZoneConfig>
```

查看当前全部电磁干扰区
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneConfig>` | 所有电磁干扰区实例ID和对应的电磁干扰区参数 |

### `GetSpecifyElectromagneticAreaList`

```text
GetSpecifyElectromagneticAreaList(InstanceID: number) -> UGCEMPZoneConfig
```

查看指定电磁干扰区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 电磁干扰区实例 ID |

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneConfig` | 指定实例的电磁干扰区参数 |

### `GetEMPZoneManager`

```text
GetEMPZoneManager() -> UGCEMPZoneManager
```

获取电磁干扰区管理器
获取电磁干扰区全局管理器实例，用于绑定电磁干扰区相关事件
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneManager` | 电磁干扰区管理器实例，失败时返回nil |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCEntityTypeSystem.json -->

# UGCEntityTypeSystem

实体类型查询系统接口库

## Functions

### `IsActorOfEntityType`

```text
IsActorOfEntityType(Actor: AActor, EntityTypeName: string) -> boolean
```

判断Actor是否属于指定的实体类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |
| `EntityTypeName` | `string` | 实体类型名称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否属于指定类型 |

### `GetActorEntityType`

```text
GetActorEntityType(Actor: AActor) -> string
```

获取Actor的实体类型（返回第一个匹配的）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |

**Returns**

| Type | Description |
|---|---|
| `string` | 实体类型名称，如果没有匹配则返回空字符串 |

### `GetActorEntityTypes`

```text
GetActorEntityTypes(Actor: AActor) -> string[]
```

获取Actor的所有匹配的实体类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |

**Returns**

| Type | Description |
|---|---|
| `string[]` | 实体类型名称数组 |

### `GetAllEntityTypeNames`

```text
GetAllEntityTypeNames() -> string[]
```

获取所有已配置的实体类型名称
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `string[]` | 所有实体类型名称数组 |

### `OverlapBoxByEntityType`

```text
OverlapBoxByEntityType(WorldContext: UObject, EntityTypeName: string, Location: FVector, HalfExtent: FVector, Rotation: FRotator) -> AActor[]
```

使用Box形状检测指定EntityType的Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeName` | `string` | 实体类型名称 |
| `Location` | `FVector` | 检测位置 |
| `HalfExtent` | `FVector` | Box的半尺寸（默认值：{X=50, Y=50, Z=50}） |
| `Rotation` | `FRotator` | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `OverlapSphereByEntityType`

```text
OverlapSphereByEntityType(WorldContext: UObject, EntityTypeName: string, Location: FVector, Radius: number) -> AActor[]
```

使用Sphere形状检测指定EntityType的Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeName` | `string` | 实体类型名称 |
| `Location` | `FVector` | 检测位置 |
| `Radius` | `number` | 球体半径（默认值：100） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `OverlapCapsuleByEntityType`

```text
OverlapCapsuleByEntityType(WorldContext: UObject, EntityTypeName: string, Location: FVector, Radius: number, HalfHeight: number, Rotation: FRotator) -> AActor[]
```

使用Capsule形状检测指定EntityType的Actor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeName` | `string` | 实体类型名称 |
| `Location` | `FVector` | 检测位置 |
| `Radius` | `number` | 胶囊体半径（默认值：100） |
| `HalfHeight` | `number` | 胶囊体半高（默认值：100） |
| `Rotation` | `FRotator` | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `IsActorOfClassType`

```text
IsActorOfClassType(Actor: AActor, ActorClassPath: string) -> boolean
```

检查Actor是否为指定的类类型
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |
| `ActorClassPath` | `string` | Actor类的路径 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为指定类型 |

### `IsActorOfAnyClassTypes`

```text
IsActorOfAnyClassTypes(Actor: AActor, ActorClassPaths: string[]) -> boolean
```

检查Actor是否为指定类类型数组中的任意一种
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |
| `ActorClassPaths` | `string[]` | Actor类路径数组 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为指定类型之一 |

### `IsActorOfEntityTypeByTag`

```text
IsActorOfEntityTypeByTag(Actor: AActor, EntityTypeTag: FGameplayTag) -> boolean
```

判断Actor是否属于指定的实体类型（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |
| `EntityTypeTag` | `FGameplayTag` | 实体类型GameplayTag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否属于指定类型 |

### `IsActorOfEntityTypeByTags`

```text
IsActorOfEntityTypeByTags(Actor: AActor, EntityTypeTags: FGameplayTagContainer) -> boolean
```

判断Actor是否属于指定的实体类型（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |
| `EntityTypeTags` | `FGameplayTagContainer` | 实体类型GameplayTag容器 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否属于指定类型之一 |

### `GetActorEntityTypeAsGameplayTag`

```text
GetActorEntityTypeAsGameplayTag(Actor: AActor) -> FGameplayTag
```

获取Actor的实体类型（返回GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTag` | 实体类型GameplayTag |

### `GetActorEntityTypesAsGameplayTagContainer`

```text
GetActorEntityTypesAsGameplayTagContainer(Actor: AActor) -> FGameplayTagContainer
```

获取Actor的所有匹配的实体类型（返回GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 要检查的Actor |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 实体类型GameplayTag容器 |

### `OverlapBoxByEntityTypeTag`

```text
OverlapBoxByEntityTypeTag(WorldContext: UObject, EntityTypeTag: FGameplayTag, Location: FVector, HalfExtent: FVector, Rotation: FRotator) -> AActor[]
```

使用Box形状检测指定EntityType的Actor（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeTag` | `FGameplayTag` | 实体类型GameplayTag |
| `Location` | `FVector` | 检测位置 |
| `HalfExtent` | `FVector` | Box的半尺寸（默认值：{X=50, Y=50, Z=50}） |
| `Rotation` | `FRotator` | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `OverlapBoxByEntityTypeTags`

```text
OverlapBoxByEntityTypeTags(WorldContext: UObject, EntityTypeTags: FGameplayTagContainer, Location: FVector, HalfExtent: FVector, Rotation: FRotator) -> AActor[]
```

使用Box形状检测指定EntityType的Actor（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeTags` | `FGameplayTagContainer` | 实体类型GameplayTag容器 |
| `Location` | `FVector` | 检测位置 |
| `HalfExtent` | `FVector` | Box的半尺寸（默认值：{X=50, Y=50, Z=50}） |
| `Rotation` | `FRotator` | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `OverlapSphereByEntityTypeTag`

```text
OverlapSphereByEntityTypeTag(WorldContext: UObject, EntityTypeTag: FGameplayTag, Location: FVector, Radius: number) -> AActor[]
```

使用Sphere形状检测指定EntityType的Actor（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeTag` | `FGameplayTag` | 实体类型GameplayTag |
| `Location` | `FVector` | 检测位置 |
| `Radius` | `number` | 球体半径（默认值：100） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `OverlapSphereByEntityTypeTags`

```text
OverlapSphereByEntityTypeTags(WorldContext: UObject, EntityTypeTags: FGameplayTagContainer, Location: FVector, Radius: number) -> AActor[]
```

使用Sphere形状检测指定EntityType的Actor（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeTags` | `FGameplayTagContainer` | 实体类型GameplayTag容器 |
| `Location` | `FVector` | 检测位置 |
| `Radius` | `number` | 球体半径（默认值：100） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `OverlapCapsuleByEntityTypeTag`

```text
OverlapCapsuleByEntityTypeTag(WorldContext: UObject, EntityTypeTag: FGameplayTag, Location: FVector, Radius: number, HalfHeight: number, Rotation: FRotator) -> AActor[]
```

使用Capsule形状检测指定EntityType的Actor（使用GameplayTag）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeTag` | `FGameplayTag` | 实体类型GameplayTag |
| `Location` | `FVector` | 检测位置 |
| `Radius` | `number` | 胶囊体半径（默认值：100） |
| `HalfHeight` | `number` | 胶囊体半高（默认值：100） |
| `Rotation` | `FRotator` | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `OverlapCapsuleByEntityTypeTags`

```text
OverlapCapsuleByEntityTypeTags(WorldContext: UObject, EntityTypeTags: FGameplayTagContainer, Location: FVector, Radius: number, HalfHeight: number, Rotation: FRotator) -> AActor[]
```

使用Capsule形状检测指定EntityType的Actor（使用GameplayTagContainer）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContext` | `UObject` | 世界上下文对象 |
| `EntityTypeTags` | `FGameplayTagContainer` | 实体类型GameplayTag容器 |
| `Location` | `FVector` | 检测位置 |
| `Radius` | `number` | 胶囊体半径（默认值：100） |
| `HalfHeight` | `number` | 胶囊体半高（默认值：100） |
| `Rotation` | `FRotator` | 旋转角度（默认值：{Pitch=0, Yaw=0, Roll=0}） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 找到的Actor数组 |

### `GetAllEntityTypesAsGameplayTagContainer`

```text
GetAllEntityTypesAsGameplayTagContainer() -> FGameplayTagContainer
```

获取所有已配置的实体类型（返回GameplayTagContainer）
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 所有实体类型GameplayTag容器 |

### `ConvertEntityTypeNameToGameplayTag`

```text
ConvertEntityTypeNameToGameplayTag(EntityTypeName: string) -> FGameplayTag
```

将实体类型名称转换为GameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EntityTypeName` | `string` | 实体类型名称 |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTag` | 对应的GameplayTag |

### `ConvertGameplayTagToEntityTypeName`

```text
ConvertGameplayTagToEntityTypeName(EntityTypeTag: FGameplayTag) -> string
```

将GameplayTag转换为实体类型名称
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EntityTypeTag` | `FGameplayTag` | 实体类型GameplayTag |

**Returns**

| Type | Description |
|---|---|
| `string` | 对应的实体类型名称 |

### `SetConfigDataAssetPath`

```text
SetConfigDataAssetPath(ConfigDataAssetPath: string)
```

设置自定义配置DataAsset路径
如果不调用此函数，将使用默认路径
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigDataAssetPath` | `string` | 配置DataAsset的路径 |

### `ForceReloadConfig`

```text
ForceReloadConfig()
```

强制重新加载配置
配合SetConfigDataAssetPath使用，建议设置完路径后调用一次
生效范围：服务器&客户端

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCFakePlayerSystem.json -->

# UGCFakePlayerSystem

假人玩家系统

## Functions

### `SpawnFakePlayer`

```text
SpawnFakePlayer(AIPlayerKey: number, TeamID: number)
```

生成假人玩家， GameMode 中 DataManager，AIProbe 数据中配置 AIController
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AIPlayerKey` | `number` | AIPlayerKey，建议使用 UGCFakePlayerSystem.GetRandomAIPlayerKey 生成 |
| `TeamID` | `number` | 队伍 ID |

### `GetRandomAIPlayerKey`

```text
GetRandomAIPlayerKey() -> number
```

生成随机AIPlayerKey，用于UGCFakePlayerSystem.SpawnFakePlayer接口参数
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `number` | AIPlayerKey |

### `DestroyFakePlayer`

```text
DestroyFakePlayer(AIPlayerKey: number)
```

销毁假人玩家
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AIPlayerKey` | `number` | AIPlayerKey |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/UGCGamePartSystem.json -->

# UGCGamePartSystem

GamePart系统接口库

## Functions

### `GetGamePartConfig`

```text
GetGamePartConfig(GamePartName: string) -> UUGCGamePartConfig
```

获取指定GamePart的Config
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GamePartName` | `string` | GamePart名称 |

**Returns**

| Type | Description |
|---|---|
| `UUGCGamePartConfig` | 指定GamePart的Config |

### `GetGamePartGlobalActor`

```text
GetGamePartGlobalActor(GamePartName: string) -> AActor
```

获取指定GamePart的GlobalActor
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GamePartName` | `string` | GamePart名称 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 指定GamePart的GlobalActor |

### `GetGamePartPlayerComponent`

```text
GetGamePartPlayerComponent(GamePartName: string, PC: PlayerController, PlayerComponentName: string) -> UActorComponent
```

获取指定GamePart的指定玩家的指定PlayerComponent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GamePartName` | `string` | GamePart名称 |
| `PC` | `PlayerController` | 玩家控制器 |
| `PlayerComponentName` | `string` | PlayerComponent名称 |

**Returns**

| Type | Description |
|---|---|
| `UActorComponent` | 指定的PlayerComponent |

### `IsGamePartLoaded`

```text
IsGamePartLoaded(GamePartName: string) -> boolean
```

获取指定GamePart是否已加载

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GamePartName` | `string` | GamePart名称 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | GamePart是否已加载 |

### `GetAllLoadedGameParts`

```text
GetAllLoadedGameParts() -> string[]
```

获取所有已加载的GamePart

**Returns**

| Type | Description |
|---|---|
| `string[]` | 所有已加载的GamePart列表 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UGCGameplayTag.json -->

# UGCGameplayTag

UGCGameplayTag

## Functions

### `__tostring`

```text
__tostring() -> string
```

返回 UGCGamePlayTag 的字符串

**Returns**

| Type | Description |
|---|---|
| `string` | - |

### `IsValid`

```text
IsValid() -> boolean
```

检查当前这个 UGCGameplayTag 是否合法

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCGameplayTagSystem.json -->

# UGCGameplayTagSystem

GameplayTag接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCGameplayTagSystem.Tags.PawnState` | `-` | - |

## Functions

### `RequestGameplayTag`

```text
RequestGameplayTag(TagString: string) -> FGameplayTag
```

根据字符串获取FGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagString` | `string` | Tag的字符串 |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTag` | 是否为合法的Tag |

### `IsValidTag`

```text
IsValidTag(Tag: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查一个Tag是否合法
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为合法的Tag |

### `IsUGCGameplayTag`

```text
IsUGCGameplayTag(Tag: UGCGameplayTag) -> boolean
```

检查一个Tag是否是UGCGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Tag` | `UGCGameplayTag` | UGCGameplayTag的lua对象 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为UGCGameplayTag |

### `MatchesTag`

```text
MatchesTag(TagA: UGCGameplayTag|string|FGameplayTag, TagB: UGCGameplayTag|string|FGameplayTag, bExactMatch: boolean) -> boolean
```

检查TagA是否与TagB匹配
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagA` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| `TagB` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| `bExactMatch` | `boolean` | 是否精确匹配 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否匹配 |

### `EqualsTag`

```text
EqualsTag(TagA: UGCGameplayTag|string|FGameplayTag, TagB: UGCGameplayTag|string|FGameplayTag) -> boolean
```

检查TagA是否与TagB相等
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagA` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |
| `TagB` | `UGCGameplayTag\|string\|FGameplayTag` | Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否相等 |

### `CreateGameplayTagContainer`

```text
CreateGameplayTagContainer() -> FGameplayTagContainer
```

创建一个空的FFGameplayTagContainer
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 空的FGameplayTagContainer |

### `CreateGameplayTagContainerFromTag`

```text
CreateGameplayTagContainerFromTag(SingleTag: UGCGameplayTag|string|FGameplayTag) -> FGameplayTagContainer
```

创建一个包含指定FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SingleTag` | `UGCGameplayTag\|string\|FGameplayTag` | 传入FGameplayTagContainer中的FGameplayTag |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 包含传入FGameplayTag的GameplayTagContainer |

### `CreateGameplayTagContainerFromArray`

```text
CreateGameplayTagContainerFromArray(GameplayTags: FGameplayTag[]) -> FGameplayTagContainer
```

创建一个包含一组FGameplayTag的FGameplayTagContainer
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GameplayTags` | `FGameplayTag[]` | 传入FGameplayTagContainer中的FGameplayTags |

**Returns**

| Type | Description |
|---|---|
| `FGameplayTagContainer` | 包含传入FGameplayTags的GameplayTagContainer |

### `AddGameplayTagToContainer`

```text
AddGameplayTagToContainer(TagContainer: FGameplayTagContainer, Tag: FGameplayTag)
```

将单个FGameplayTag添加到传入的FGameplayTagContainer中
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer` | 要追加到的FGameplayTagContainer |
| `Tag` | `FGameplayTag` | 要添加到FGameplayTagContainer中的FGameplayTag |

### `RemoveGameplayTagFromContainer`

```text
RemoveGameplayTagFromContainer(TagContainer: FGameplayTagContainer, Tag: FGameplayTag) -> boolean
```

从传入的FGameplayTagContainer中移除单个FGameplayTag，若找到并移除则返回 true ，否则返回 false
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer` | 要从中移除的FGameplayTagContainer |
| `Tag` | `FGameplayTag` | 要从FGameplayTagContainer中移除的FGameplayTag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否成功移除 |

### `HasTag`

```text
HasTag(TagContainer: FGameplayTagContainer, Tag: FGameplayTag, bExactMatch: boolean) -> boolean
```

检查FGameplayTagContainer是否包含特定的FGameplayTag
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TagContainer` | `FGameplayTagContainer` | 要从中查找指定FGameplayTag的FGameplayTagContainer |
| `Tag` | `FGameplayTag` | 要从FGameplayTagContainer中检查的FGameplayTag |
| `bExactMatch` | `boolean` | 是否精确匹配 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否包含Tag |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCGameplayTaskSystem.json -->

# UGCGameplayTaskSystem

异步任务接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCGameplayTaskSystem.General` | `-` | class General @通用异步任务 |
| `UGCGameplayTaskSystem.General.SpawnActor` | `-` | class SpawnActor @通用异步任务：SpawnActor |
| `UGCGameplayTaskSystem.Player` | `-` | class Player @玩家异步任务 |
| `UGCGameplayTaskSystem.Player.AddCustomCameraData` | `-` | class AddCustomCameraData @玩家异步任务：添加自定义相机数据 |
| `UGCGameplayTaskSystem.Player.SetEyeRotationMode` | `-` | class SetEyeRotationMode @玩家异步任务：添加自定义相机数据 |
| `UGCGameplayTaskSystem.Player.RegisterDynamicState` | `-` | class RegisterDynamicState @玩家异步任务：注册一组状态互斥 |
| `UGCGameplayTaskSystem.General.SelectLocationFromMap` | `-` | class SelectLocationFromMap @通用异步任务：从小地图上获得一个选点 |
| `UGCGameplayTaskSystem.Player.SwitchWeapon` | `-` | class SwitchWeapon @玩家异步任务：切换武器 |
| `UGCGameplayTaskSystem.PlayerPawn` | `-` | class PlayerPawn @角色异步任务 |
| `UGCGameplayTaskSystem.PlayerPawn.TeleportPawn` | `-` | class TeleportPawn @角色异步任务：传送角色 |
| `UGCGameplayTaskSystem.PlayerPawn.Sprint` | `-` | class TeleportPawn @角色异步任务：角色冲刺 |
| `UGCGameplayTaskSystem.PlayerPawn.SetMaterial` | `-` | class SetMaterial @角色异步任务：角色换材质 |
| `UGCGameplayTaskSystem.PlayerPawn.HitBack` | `-` | class SetMaterial @角色异步任务：击退 |
| `UGCGameplayTaskSystem.PlayerPawn.AttachToCharacterScoket` | `-` | class Character @角色异步任务 |
| `UGCGameplayTaskSystem.PlayerPawn.ReplaceAnim` | `-` | class Character @角色异步任务: 替换动画 |
| `UGCGameplayTaskSystem.GenericCharacter` | `-` | class GenericCharacter @GenericCharacter异步任务 |
| `UGCGameplayTaskSystem.GenericCharacter.ReplaceAnim` | `-` | class ReplaceAnim @GenericCharacter异步任务：替换动画 |
| `UGCGameplayTaskSystem.Weapon` | `-` | class Weapon @武器异步任务 |
| `UGCGameplayTaskSystem.Weapon.AutoAim` | `-` | class AutoAim @武器异步任务：自动瞄准 |
| `UGCGameplayTaskSystem.Weapon.LaunchProjectile` | `-` | class LaunchProjectile @武器异步任务：发射抛体 |

## Language

`lua`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UGCGameSettingSystem.json -->

# UGCGameSettingSystem

游戏配置通用接口库

## Functions

### `GetDeviceLevel`

```text
GetDeviceLevel() -> number
```

获取设备水平（0=低端机，1=中端机，2=高端机）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `number` | 设备水平级别 |

### `GetRenderQualitySetting`

```text
GetRenderQualitySetting() -> ERenderQuality
```

获取渲染水平设置（画面品质）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ERenderQuality` | 渲染水平枚举值 |

### `GetRenderStyleSetting`

```text
GetRenderStyleSetting() -> ERenderStyle
```

获取渲染风格设置（画面风格）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `ERenderStyle` | 渲染风格枚举值 |

### `AllowSoftwareOcclusion`

```text
AllowSoftwareOcclusion(bEnabled: boolean)
```

是否开启软件遮挡剔除（默认开启）。2D 类游戏建议关闭，否则在手机上层次相近（接近重叠）的物体处，可能会出现（黑屏）闪烁
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `boolean` | 是否开启 |

## Language

`lua`

