---
id: "api:class:UWidget"
title: "UWidget"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidget.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidget

This is the base class for all wrapped Slate controls that are exposed to UObjects.

## Inheritance

`UVisual`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Slot` | `UPanelSlot *` | The parent slot of the UWidget.  Allows us to easily inline edit the layout controlling this widget. |
| `CachedPanel_ForGC` | `UPanelWidget *` | - |
| `ToolTipText` | `FText` | Tooltip text to show when the user hovers over the widget with the mouse |
| `ToolTipWidget` | `UWidget *` | Tooltip widget to show when the user hovers over the widget with the mouse |
| `IgnorePixelSnapping` | `bool` | - |
| `RelatedStyleWidgetName` | `FName` | - |
| `RelatedStyleWidget` | `TWeakObjectPtr < UWidget >` | - |
| `RenderTransform` | `FWidgetTransform` | The render transform of the widget allows for arbitrary 2D transforms to be applied to the widget. |
| `RenderTransformPivot` | `FVector2D` | The render transform pivot controls the location about which transforms are applied.<br>	  This value is a normalized coordinate about which things like rotations will occur. |
| `bIsVariable` | `uint8` | Allows controls to be exposed as variables in a blueprint.  Not all controls need to be exposed<br>	  as variables, so this allows only the most useful ones to end up being exposed. |
| `bCreatedByConstructionScript` | `uint8` | Flag if the Widget was created from a blueprint |
| `bIsEnabled` | `uint8` | Sets whether this widget can be modified interactively by the user |
| `bOverride_Cursor` | `uint8` | - |
| `bIsVolatile` | `uint8` | Engine modify End<br>	<br>	<br>	  If true prevents the widget or its child's geometry or layout information from being cached.  If this widget<br>	  changes every frame, but you want it to still be in an invalidation panel you should make it as volatile<br>	  instead of invalidating it every frame, which would prevent the invalidation panel from actually<br>	  ever caching anything. |
| `bWriteSceneZBuffer` | `uint8` | - |
| `UsedLayerPolicy` | `uint8` | DrawLayer's policy, 0: default, 1: prevent increasing layer to force batch |
| `PreservedLayerNum` | `uint8` | - |
| `FixedLayerPolicy` | `uint8` | DrawLayer's policy, 0: default, 1: Fixed layer to force batch |
| `FixedLayerNum` | `uint8` | - |
| `IngoreRectMove` | `uint8` | - |
| `CareRectMove` | `uint8` | - |
| `Cursor` | `TEnumAsByte < EMouseCursor :: Type >` | The cursor to show when the mouse is over the widget |
| `Clipping` | `EWidgetClipping` | Controls how the clipping behavior of this widget.  Normally content that overflows the<br>	  bounds of the widget continues rendering.  Enabling clipping prevents that overflowing content<br>	  from being seen.<br>	 <br>	  NOTE: Elements in different clipping spaces can not be batched together, and so there is a<br>	  performance cost to clipping.  Do not enable clipping unless a panel actually needs to prevent<br>	  content from showing up outside its bounds. |
| `Visibility` | `ESlateVisibility` | The visibility of the widget |
| `RenderOpacity` | `float` | The opacity of the widget |
| `Navigation` | `UWidgetNavigation *` | The navigation object for this widget is optionally created if the user has configured custom<br>	  navigation rules for this widget in the widget designer.  Those rules determine how navigation transitions<br>	  can occur between widgets. |
| `bCatchVisibilityChangedEvent` | `bool` | True if you want to enable auto destroy user widget stragegy |
| `NativeBindings` | `TArray < UPropertyBinding * >` | Native property bindings. |
| `AreaTypeFlags` | `int32` | - |
| `ZValue` | `int32` | - |
| `bLogTraceVisibilityChange` | `uint8` | Engine modify Start |
| `bHiddenInDesigner` | `uint8` | Stores the design time flag setting if the widget is hidden inside the designer |
| `bExpandedInDesigner` | `uint8` | Stores the design time flag setting if the widget is expanded inside the designer |
| `bLockedInDesigner` | `uint8` | Stores the design time flag setting if the widget is locked inside the designer |
| `DesignerFlags` | `TEnumAsByte < EWidgetDesignFlags :: Type >` | Any flags used by the designer at edit time. |
| `DisplayLabel` | `FString` | The friendly name for this widget displayed in the designer and BP graph. |
| `bStyleHidding` | `bool` | - |
| `bStyleRemove` | `bool` | - |
| `bStyleInsertInvBox` | `bool` | - |
| `bStyleInsertRetainerBox` | `bool` | - |

## Functions

### `SetRenderTransform`

```text
SetRenderTransform(InTransform: FWidgetTransform) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTransform` | `FWidgetTransform` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderScale`

```text
SetRenderScale(Scale: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Scale` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderShear`

```text
SetRenderShear(Shear: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Shear` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderAngle`

```text
SetRenderAngle(Angle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Angle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderTranslation`

```text
SetRenderTranslation(Translation: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Translation` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRenderTransformPivot`

```text
SetRenderTransformPivot(Pivot: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Pivot` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIsEnabled`

```text
GetIsEnabled() -> bool
```

Gets the current enabled status of the widget

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIsEnabled`

```text
SetIsEnabled(bInIsEnabled: bool) -> void
```

Sets the current enabled status of the widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInIsEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetToolTipText`

```text
SetToolTipText(InToolTipText: FText &) -> void
```

Sets the tooltip text for the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InToolTipText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetToolTip`

```text
SetToolTip(Widget: UWidget *) -> void
```

Sets a custom widget as the tooltip of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCursor`

```text
SetCursor(InCursor: EMouseCursor :: Type) -> void
```

Sets the cursor to show over the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCursor` | `EMouseCursor :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetCursor`

```text
ResetCursor() -> void
```

Resets the cursor to use on the widget, removing any customization for it.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVisible`

```text
IsVisible() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget is Visible, HitTestInvisible or SelfHitTestInvisible. |

### `GetVisibility`

```text
GetVisibility() -> ESlateVisibility
```

Gets the current visibility of the widget.

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `GetUVisibility`

```text
GetUVisibility() -> ESlateVisibility
```

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `SetLocalVisibility`

```text
SetLocalVisibility(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLocalVisibilityWithoutPCUIStyle`

```text
SetLocalVisibilityWithoutPCUIStyle(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPCVisibility`

```text
GetPCVisibility() -> ESlateVisibility
```

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `IsPCVisible`

```text
IsPCVisible() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetVisibility`

```text
SetVisibility(InVisibility: ESlateVisibility) -> void
```

Sets the visibility of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVisibility` | `ESlateVisibility` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAdvancedCollapsed`

```text
SetAdvancedCollapsed(IsAdvancedCollapsed: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsAdvancedCollapsed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetRenderOpacity`

```text
GetRenderOpacity() -> float
```

Gets the current visibility of the widget.

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetRenderOpacity`

```text
SetRenderOpacity(InOpacity: float) -> void
```

Sets the visibility of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOpacity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetClipping`

```text
GetClipping() -> EWidgetClipping
```

Gets the clipping state of this widget.

**Returns**

| Type | Description |
|---|---|
| `EWidgetClipping` | - |

### `SetClipping`

```text
SetClipping(InClipping: EWidgetClipping) -> void
```

Sets the clipping state of this widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClipping` | `EWidgetClipping` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceVolatile`

```text
ForceVolatile(bForce: bool) -> void
```

Sets the forced volatility of the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bForce` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVolatile`

```text
IsVolatile() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsHovered`

```text
IsHovered() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget is currently being hovered by a pointer device |

### `SetWriteSceneZBuffer`

```text
SetWriteSceneZBuffer(bInWriteSceneZBuffer: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInWriteSceneZBuffer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasKeyboardFocus`

```text
HasKeyboardFocus() -> bool
```

Checks to see if this widget currently has the keyboard focus

**Returns**

| Type | Description |
|---|---|
| `bool` | True if this widget has keyboard focus |

### `HasMouseCapture`

```text
HasMouseCapture() -> bool
```

Checks to see if this widget is the current mouse captor

**Returns**

| Type | Description |
|---|---|
| `bool` | True if this widget has captured the mouse |

### `SetKeyboardFocus`

```text
SetKeyboardFocus() -> void
```

Sets the focus to this widget.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasUserFocus`

```text
HasUserFocus(PlayerController: APlayerController *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this widget is focused by a specific user. |

### `HasAnyUserFocus`

```text
HasAnyUserFocus() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this widget is focused by any user. |

### `HasFocusedDescendants`

```text
HasFocusedDescendants() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if any descendant widget is focused by any user. |

### `HasUserFocusedDescendants`

```text
HasUserFocusedDescendants(PlayerController: APlayerController *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if any descendant widget is focused by a specific user. |

### `SetUserFocus`

```text
SetUserFocus(PlayerController: APlayerController *) -> void
```

Sets the focus to this widget for a specific user

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceLayoutPrepass`

```text
ForceLayoutPrepass() -> void
```

Forces a pre-pass.  A pre-pass caches the desired size of the widget hierarchy owned by this widget.
	  One pre-pass is already happens for every widget before Tick occurs.  You only need to perform another
	  pre-pass if you are adding child widgets this frame and want them to immediately be visible this frame.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvalidateLayoutAndVolatility`

```text
InvalidateLayoutAndVolatility() -> void
```

Invalidates the widget from the view of a layout caching widget that may own this widget.
	  will force the owning widget to redraw and cache children on the next paint pass.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDesiredSize`

```text
GetDesiredSize() -> FVector2D
```

Gets the widgets desired size.
	  NOTE: The underlying Slate widget must exist and be valid, also at least one pre-pass must
	        have occurred before this value will be of any use.

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | The widget's desired size |

### `SetAllNavigationRules`

```text
SetAllNavigationRules(Rule: EUINavigationRule, WidgetToFocus: FName) -> void
```

Sets the widget navigation rules for all directions. This can only be called on widgets that are in a widget tree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rule` | `EUINavigationRule` | The rule to use when navigation is taking place |
| `WidgetToFocus` | `FName` | When using the Explicit rule, focus on this widget |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNavigationRule`

```text
SetNavigationRule(Direction: EUINavigation, Rule: EUINavigationRule, WidgetToFocus: FName) -> void
```

Sets the widget navigation rules for a specific direction. This can only be called on widgets that are in a widget tree.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Direction` | `EUINavigation` | - |
| `Rule` | `EUINavigationRule` | The rule to use when navigation is taking place |
| `WidgetToFocus` | `FName` | When using the Explicit rule, focus on this widget |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetParent`

```text
GetParent() -> UPanelWidget *
```

Gets the parent widget

**Returns**

| Type | Description |
|---|---|
| `UPanelWidget *` | - |

### `RemoveFromParent`

```text
RemoveFromParent() -> void
```

Removes the widget from its parent widget.  If this widget was added to the player's screen or the viewport
	  it will also be removed from those containers.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCachedGeometry`

```text
GetCachedGeometry() -> const FGeometry &
```

Gets the last geometry used to Tick the widget.  This data may not exist yet if this call happens prior to
	  the widget having been tickedpainted, or it may be out of date, or a frame behind.
	 
	  We recommend not to use this data unless there's no other way to solve your problem.  Normally in Slate we
	  try and handle these issues by making a dependent widget part of the hierarchy, as to avoid frame behind
	  or what are referred to as hysteresis problems, both caused by depending on geometry from the previous frame
	  being used to advise how to layout a dependent object the current frame.

**Returns**

| Type | Description |
|---|---|
| `const FGeometry &` | - |

### `GetCachedAllottedGeometry`

```text
GetCachedAllottedGeometry() -> const FGeometry &
```

**Returns**

| Type | Description |
|---|---|
| `const FGeometry &` | - |

### `SetIgnorePixelSnapping`

```text
SetIgnorePixelSnapping(Ignore: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Ignore` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwningPlayer`

```text
GetOwningPlayer() -> APlayerController *
```

Gets the player controller associated with this UI.

**Returns**

| Type | Description |
|---|---|
| `APlayerController *` | The player controller that owns the UI. |

### `AddAdvancedCollapsedCount`

```text
AddAdvancedCollapsedCount(Num: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Num` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SubAdvancedCollapsedCount`

```text
SubAdvancedCollapsedCount(Num: uint8) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Num` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAdvancedCollapsedCount`

```text
GetAdvancedCollapsedCount() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetWidgetOutlineName`

```text
GetWidgetOutlineName() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `IsCachedWidgetValid`

```text
IsCachedWidgetValid() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `bIsEnabledDelegate`

```text
bIsEnabledDelegate() -> bool
```

A bindable delegate for bIsEnabled

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ToolTipTextDelegate`

```text
ToolTipTextDelegate() -> FText
```

A bindable delegate for ToolTipText

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `ToolTipWidgetDelegate`

```text
ToolTipWidgetDelegate() -> UWidget*
```

A bindable delegate for ToolTipWidget

**Returns**

| Type | Description |
|---|---|
| `UWidget*` | - |

### `VisibilityDelegate`

```text
VisibilityDelegate() -> ESlateVisibility
```

A bindable delegate for Visibility

**Returns**

| Type | Description |
|---|---|
| `ESlateVisibility` | - |

### `IgnorePixelSnappingDelegate`

```text
IgnorePixelSnappingDelegate() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnWidgetVisibilityChanged`

```text
OnWidgetVisibilityChanged(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWidgetSlateVisibilityChanged`

```text
OnWidgetSlateVisibilityChanged(OldVisibility: ESlateVisibility, NewVisibility: ESlateVisibility, Widget: UWidget*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldVisibility` | `ESlateVisibility` | - |
| `NewVisibility` | `ESlateVisibility` | - |
| `Widget` | `UWidget*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWidgetIsEnabledSet`

```text
OnWidgetIsEnabledSet(bIsEnabled: bool, Widget: UWidget*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsEnabled` | `bool` | - |
| `Widget` | `UWidget*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
