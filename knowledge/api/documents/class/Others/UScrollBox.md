---
id: "api:class:UScrollBox"
title: "UScrollBox"
source: "https://developer.gp.qq.com/api/class/detail/Others/UScrollBox.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UScrollBox

An arbitrary scrollable collection of widgets.  Great for presenting 10-100 widgets in a list.  Doesn't support virtualization.

## Inheritance

`UPanelWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetStyle` | `FScrollBoxStyle` | The style |
| `WidgetBarStyle` | `FScrollBarStyle` | The bar style |
| `OverscrollLooseness` | `float` | Overscroll Looseness |
| `Style_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `BarStyle_DEPRECATED` | `USlateWidgetStyleAsset *` | - |
| `Orientation` | `TEnumAsByte < EOrientation >` | The orientation of the scrolling and stacking in the box. |
| `ScrollBarVisibility` | `ESlateVisibility` | Visibility |
| `ConsumeMouseWheel` | `EConsumeMouseWheel` | Enable to always consume mouse wheel event, even when scrolling is not possible |
| `ScrollbarThickness` | `FVector2D` | - |
| `AlwaysShowScrollbar` | `bool` | - |
| `AllowOverscroll` | `bool` | Disable to stop scrollbars from activating inertial overscrolling |
| `NavigationDestination` | `EDescendantScrollDestination` | - |
| `NavigationScrollPadding` | `float` | The amount of padding to ensure exists between the item being navigated to, at the edge of the<br>	  scrollbox.  Use this if you want to ensure there's a preview of the next item the user could scroll to. |
| `bAllowRightClickDragScrolling` | `bool` | Option to disable right-click-drag scrolling |
| `bScrollEnabled` | `bool` | 启用滑动 |
| `bScrollDisableHandled` | `bool` | 启用滑动 |
| `bPreciseScroll` | `bool` | 启用精准滑动 |
| `bDisableDragListScroll` | `bool` | 依旧可以通过拖拽bar或者鼠标滚轮滑动, 仅PC版生效 |
| `bScrollFocus` | `bool` | 滑动时获得焦点 |

## Functions

### `SetOrientation`

```text
SetOrientation(NewOrientation: EOrientation) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOrientation` | `EOrientation` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollBarVisibility`

```text
SetScrollBarVisibility(NewScrollBarVisibility: ESlateVisibility) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScrollBarVisibility` | `ESlateVisibility` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollbarThickness`

```text
SetScrollbarThickness(NewScrollbarThickness: FVector2D &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScrollbarThickness` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAlwaysShowScrollbar`

```text
SetAlwaysShowScrollbar(NewAlwaysShowScrollbar: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAlwaysShowScrollbar` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAllowOverscroll`

```text
SetAllowOverscroll(NewAllowOverscroll: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAllowOverscroll` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCacheOverscrollOffset`

```text
GetCacheOverscrollOffset() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetOverscrollLooseness`

```text
SetOverscrollLooseness(v: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `v` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollEnabled`

```text
SetScrollEnabled(InScrollEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollDisableHandled`

```text
SetScrollDisableHandled(InScrollDisableHandled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollDisableHandled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollPrecise`

```text
SetScrollPrecise(InScrollPrecise: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollPrecise` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetScrollFocus`

```text
SetScrollFocus(InScrollFocus: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InScrollFocus` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDragListScrollEnabled`

```text
SetDragListScrollEnabled(InDragListScrollEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDragListScrollEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsReachEnd`

```text
IsReachEnd() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsLargerThanContentSize`

```text
IsLargerThanContentSize() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetScrollOffset`

```text
SetScrollOffset(NewScrollOffset: float) -> void
```

Updates the scroll offset of the scrollbox.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScrollOffset` | `float` | is in Slate Units. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScrollOffset`

```text
GetScrollOffset() -> float
```

Gets the scroll offset of the scrollbox in Slate Units.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `ScrollToStart`

```text
ScrollToStart() -> void
```

Scrolls the ScrollBox to the top instantly

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScrollToEnd`

```text
ScrollToEnd() -> void
```

Scrolls the ScrollBox to the bottom instantly during the next layout pass.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopScroll`

```text
StopScroll() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ScrollWidgetIntoView`

```text
ScrollWidgetIntoView(WidgetToFind: UWidget *, AnimateScroll: bool, ScrollDestination: EDescendantScrollDestination) -> void
```

Scrolls the ScrollBox to the widget during the next layout pass.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WidgetToFind` | `UWidget *` | - |
| `AnimateScroll` | `bool` | - |
| `ScrollDestination` | `EDescendantScrollDestination` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnUserScrolled`

```text
OnUserScrolled(CurrentOffset: float) -> void
```

Called when the scroll has changed

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnUserScrolledUnused`

```text
OnUserScrolledUnused(CurrentOffset: float) -> void
```

Called when the scroll has changed,the value is mouse movement in another direction -zhenzhai

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentOffset` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTouchFinish`

```text
OnTouchFinish() -> void
```

Called when the touch has end

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
