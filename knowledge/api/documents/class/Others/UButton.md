---
id: "api:class:UButton"
title: "UButton"
source: "https://developer.gp.qq.com/api/class/detail/Others/UButton.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UButton

The button is a click-able primitive widget to enable basic interaction, you
  can place any other widget inside a button to make a more complex and
  interesting click-able element in your UI.
 
   Single Child
   Clickable

## Inheritance

`UContentWidget` -> `IWidgetSkinInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | The template style asset, used to seed the mutable instance of the style. |
| `WidgetStyle` | `FButtonStyle` | The button style used at runtime |
| `ColorAndOpacity` | `FLinearColor` | The color multiplier for the button content |
| `BackgroundColor` | `FLinearColor` | The color multiplier for the button background |
| `ClickMethod` | `TEnumAsByte < EButtonClickMethod :: Type >` | The type of mouse action required by the user to trigger the buttons 'Click' |
| `TouchMethod` | `TEnumAsByte < EButtonTouchMethod :: Type >` | The type of touch action required by the user to trigger the buttons 'Click' |
| `ListenEscMethod` | `TEnumAsByte < EListenEscMethod :: Type >` | 通过命名识别关闭按钮，识别忽略大小写下划线，推荐命名(Button_Close,NewButton_Close...) |
| `ListenActions` | `TArray < FButtonListenAction >` | 通过监听Action，来统一模拟按键点击，扩展Esc模拟点击功能 |
| `IsTipsBgBtn` | `bool` | 是否为Tips背景按钮 |
| `IsFocusable` | `bool` | Sometimes a button should only be mouse-clickable and never keyboard focusable. |
| `IsPassMouseEvent` | `bool` | - |
| `IsImgAlphaBtn` | `bool` | - |
| `bUseCustomSettings` | `bool` | - |
| `CustomHitAreaTexture` | `UTexture2D *` | - |
| `CustomHitAreaAlpha` | `int` | - |
| `bIsShowHover` | `bool` | - |
| `bIsLayerPlus` | `bool` | - |
| `OnMouseButtonDownEvent` | `FOnPointerEvent` | - |
| `OnMouseButtonUpEvent` | `FOnPointerEvent` | - |
| `OnMouseMoveEvent` | `FOnPointerEvent` | - |
| `InputActionBindings` | `FButtonInputActionBindingsStruct` | - |
| `EscRespondSetting` | `FEscRespondSetting` | - |
| `IsThisFrameClicked` | `bool` | - |

## Functions

### `SetStyle`

```text
SetStyle(InStyle: FButtonStyle &) -> void
```

Sets the color multiplier for the button background

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InStyle` | `FButtonStyle &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FLinearColor) -> void
```

Sets the color multiplier for the button content

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBackgroundColor`

```text
SetBackgroundColor(InBackgroundColor: FLinearColor) -> void
```

Sets the color multiplier for the button background

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBackgroundColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPressed`

```text
IsPressed() -> bool
```

Returns true if the user is actively pressing the button.  Do not use this for detecting 'Clicks', use the OnClicked event instead.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the user is actively pressing the button otherwise false. |

### `Release`

```text
Release() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClickMethod`

```text
SetClickMethod(InClickMethod: EButtonClickMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClickMethod` | `EButtonClickMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTouchMethod`

```text
SetTouchMethod(InTouchMethod: EButtonTouchMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTouchMethod` | `EButtonTouchMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetReleasedReason`

```text
GetReleasedReason() -> uint8
```

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `SetListenEscMethod`

```text
SetListenEscMethod(InListenEscMethod: EListenEscMethod :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InListenEscMethod` | `EListenEscMethod :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetListenEscMethod`

```text
GetListenEscMethod() -> EListenEscMethod :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EListenEscMethod :: Type` | - |

### `SetShowHover`

```text
SetShowHover(InShowHover: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InShowHover` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddListenAction`

```text
AddListenAction(InActionName: FName, InType: EButtonListenActionEvent :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActionName` | `FName` | - |
| `InType` | `EButtonListenActionEvent :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveListenAction`

```text
RemoveListenAction(InActionName: FName) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActionName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearListenActions`

```text
ClearListenActions() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCacheLayerId`

```text
GetCacheLayerId() -> int32
```

return CacheLayerId only windows

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RespondEscape`

```text
RespondEscape() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetButtonsFromAction`

```text
GetButtonsFromAction(OutButtons: TArray < UButton * > &, InAction: FName) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutButtons` | `TArray < UButton * > &` | - |
| `InAction` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearInvalidForListenActions`

```text
ClearInvalidForListenActions() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetButtonsFromTipsBg`

```text
GetButtonsFromTipsBg() -> TArray < UButton * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UButton * >` | - |

### `SetButtonClickedGlobalEvent`

```text
SetButtonClickedGlobalEvent(InEvent: FOnButtonClickedGlobalEvent) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InEvent` | `FOnButtonClickedGlobalEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearButtonClickedGlobalEvent`

```text
ClearButtonClickedGlobalEvent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsFocusable`

```text
SetIsFocusable(InFocusable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnClicked`

```text
OnClicked() -> void
```

Called when the button is clicked

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPressed`

```text
OnPressed() -> void
```

Called when the button is pressed

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReleased`

```text
OnReleased() -> void
```

Called when the button is released

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnHovered`

```text
OnHovered() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUnhovered`

```text
OnUnhovered() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPressedParam`

```text
OnPressedParam(MyGeometry: FGeometry, MouseEvent: const FPointerEvent&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `MouseEvent` | `const FPointerEvent&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReleasedParam`

```text
OnReleasedParam(MyGeometry: FGeometry, MouseEvent: const FPointerEvent&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `MouseEvent` | `const FPointerEvent&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnReplayRecordNotify`

```text
OnReplayRecordNotify(EventIndex: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
