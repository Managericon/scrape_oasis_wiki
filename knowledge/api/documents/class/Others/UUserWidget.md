---
id: "api:class:UUserWidget"
title: "UUserWidget"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUserWidget.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUserWidget

The user widget is extensible by users through the WidgetBlueprint.

## Inheritance

`UWidget` -> `INamedSlotInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ColorAndOpacity` | `FLinearColor` | The color and opacity of this widget.  Tints all child widgets. |
| `ColorAndOpacityDelegate` | `FGetLinearColor` | - |
| `ForegroundColor` | `FSlateColor` | The foreground color of the widget, this is inherited by sub widgets.  Any color property<br>	  that is marked as inherit will use this color. |
| `ForegroundColorDelegate` | `FGetSlateColor` | - |
| `Padding` | `FMargin` | The padding area around the content. |
| `ActiveSequencePlayers` | `TArray < UUMGSequencePlayer * >` | All the sequence players currently playing |
| `StoppedSequencePlayers` | `TArray < UUMGSequencePlayer * >` | List of sequence players to cache and clean up when safe |
| `NamedSlotBindings` | `TArray < FNamedSlotBinding >` | Stores the widgets being assigned to named slots |
| `WidgetTree` | `UWidgetTree *` | The widget tree contained inside this user widget initialized by the blueprint |
| `bOptimiseAnimation` | `bool` | - |
| `bNoBubbleUpEvent` | `bool` | - |
| `Priority` | `int32` | - |
| `bSupportsKeyboardFocus_DEPRECATED` | `uint8` | - |
| `bIsFocusable` | `uint8` | Setting this flag to true, allows this widget to accept focus when clicked, or when navigated to. |
| `bStopAction` | `uint8` | - |
| `CanDisableDrag` | `uint8` | - |
| `bCanEverTick` | `uint8` | If a widget doesn't ever need to tick the blueprint, setting this to false is an optimization. |
| `bCanEverPaint` | `uint8` | If a widget doesn't ever need to do custom painting in the blueprint, setting this to false is an optimization. |
| `bCookedWidgetTree` | `uint8` | If this user widget was created using a cooked widget tree.  If that's true, we want to skip a lot of the normal<br>	  initialization logic for widgets, because these widgets have already been initialized. |
| `WidgetSkinProxy` | `UObject *` | UPROPERTY(EditAnywhere, BlueprintReadOnly, Category = "WidgetSkin") |
| `InputComponent` | `UInputComponent *` | - |
| `AnimationCallbacks` | `TArray < FAnimationEventBinding >` | - |

## Functions

### `AddToViewport`

```text
AddToViewport(ZOrder: int32) -> void
```

Adds it to the game's viewport and fills the entire screen, unless SetDesiredSizeInViewport is called
	  to explicitly set the size.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZOrder` | `int32` | The higher the number, the more on top this widget will be. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddToPlayerScreen`

```text
AddToPlayerScreen(ZOrder: int32) -> bool
```

Adds the widget to the game's viewport in a section dedicated to the player.  This is valuable in a split screen
	  game where you need to only show a widget over a player's portion of the viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ZOrder` | `int32` | The higher the number, the more on top this widget will be. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveFromViewport`

```text
RemoveFromViewport() -> void
```

Removes the widget from the viewport.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetZOrderOfViewportWidget`

```text
GetZOrderOfViewportWidget() -> int
```

Get Z-order of Viewport Widget, added by fourthchen

**Returns**

| Type | Description |
|---|---|
| `int` | - |

### `SetPositionInViewport`

```text
SetPositionInViewport(Position: FVector2D, bRemoveDPIScale: bool) -> void
```

Sets the widgets position in the viewport.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Position` | `FVector2D` | The 2D position to set the widget to in the viewport. |
| `bRemoveDPIScale` | `bool` | If you've already calculated inverse DPI, set this to false. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDesiredSizeInViewport`

```text
SetDesiredSizeInViewport(Size: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Size` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOffsetsInViewport`

```text
SetOffsetsInViewport(Margin: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Margin` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnchorsInViewport`

```text
SetAnchorsInViewport(Anchors: FAnchors) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Anchors` | `FAnchors` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAlignmentInViewport`

```text
SetAlignmentInViewport(Alignment: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Alignment` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAnchorsInViewport`

```text
GetAnchorsInViewport() -> FAnchors
```

**Returns**

| Type | Description |
|---|---|
| `FAnchors` | - |

### `GetAlignmentInViewport`

```text
GetAlignmentInViewport() -> FVector2D
```

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `GetIsVisible`

```text
GetIsVisible() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsInViewport`

```text
IsInViewport() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the widget was added to the viewport using AddToViewport. |

### `GetOwningLocalPlayer`

```text
GetOwningLocalPlayer() -> ULocalPlayer *
```

Gets the local player associated with this UI.

**Returns**

| Type | Description |
|---|---|
| `ULocalPlayer *` | The owning local player. |

### `SetOwningLocalPlayer`

```text
SetOwningLocalPlayer(LocalPlayer: ULocalPlayer *) -> void
```

Sets the player associated with this UI via LocalPlayer reference.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalPlayer` | `ULocalPlayer *` | The local player you want to be the conceptual owner of this UI. |

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

### `SetOwningPlayer`

```text
SetOwningPlayer(LocalPlayerController: APlayerController *) -> void
```

Sets the local player associated with this UI via PlayerController reference.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LocalPlayerController` | `APlayerController *` | The PlayerController of the local player you want to be the conceptual owner of this UI. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOwningPlayerPawn`

```text
GetOwningPlayerPawn() -> APawn *
```

Gets the player pawn associated with this UI.

**Returns**

| Type | Description |
|---|---|
| `APawn *` | Gets the owning player pawn that's owned by the player controller assigned to this widget. |

### `PreConstruct`

```text
PreConstruct(IsDesignTime: bool) -> void
```

Called by both the game and the editor.  Allows users to run initial setup for their widgets to better preview
	  the setup in the designer and since generally that same setup code is required at runtime, it's called there
	  as well.
	 
	  WARNING
	  This is intended purely for cosmetic updates using locally owned data, you can not safely access any game related
	  state, if you call something that doesn't expect to be run at editor time, you may crash the editor.
	 
	  In the event you save the asset with blueprint code that causes a crash on evaluation.  You can turn off
	  PreConstruct evaluation in the Widget Designer settings in the Editor Preferences.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsDesignTime` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Construct`

```text
Construct() -> void
```

Called after the underlying slate widget is constructed.  Depending on how the slate object is used
	  this event may be called multiple times due to adding and removing from the hierarchy.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ConstructForLua`

```text
ConstructForLua() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Destruct`

```text
Destruct() -> void
```

Called when a widget is no longer referenced causing the slate resource to destroyed.  Just like
	  Construct this event can be called multiple times.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Tick`

```text
Tick(MyGeometry: FGeometry, InDeltaTime: float) -> void
```

Ticks this widget.  Override in derived classes, but always call the parent implementation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The space allotted for this widget |
| `InDeltaTime` | `float` | Real time passed since last tick |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPaint`

```text
OnPaint(Context: FPaintContext &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInteractable`

```text
IsInteractable() -> bool
```

Gets a value indicating if the widget is interactive.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnFocusReceived`

```text
OnFocusReceived(MyGeometry: FGeometry, InFocusEvent: FFocusEvent) -> FEventReply
```

Called when keyboard focus is given to this widget.  This event does not bubble.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnFocusLost`

```text
OnFocusLost(InFocusEvent: FFocusEvent) -> void
```

Called when this widget loses focus.  This event does not bubble.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAddedToFocusPath`

```text
OnAddedToFocusPath(InFocusEvent: FFocusEvent) -> void
```

If focus is gained on on this widget or on a child widget and this widget is added
	  to the focus path, and wasn't previously part of it, this event is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRemovedFromFocusPath`

```text
OnRemovedFromFocusPath(InFocusEvent: FFocusEvent) -> void
```

If focus is lost on on this widget or on a child widget and this widget is
	  no longer part of the focus path.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFocusEvent` | `FFocusEvent` | FocusEvent |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnKeyChar`

```text
OnKeyChar(MyGeometry: FGeometry, InCharacterEvent: FCharacterEvent) -> FEventReply
```

Called after a character is entered while this widget has focus

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InCharacterEvent` | `FCharacterEvent` | Character event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnPreviewKeyDown`

```text
OnPreviewKeyDown(MyGeometry: FGeometry, InKeyEvent: FKeyEvent) -> FEventReply
```

Called after a key (keyboard, controller, ...) is pressed when this widget or a child of this widget has focus
	  If a widget handles this event, OnKeyDown will not be passed to the focused widget.
	 
	  This event is primarily to allow parent widgets to consume an event before a child widget processes
	  it and it should be used only when there is no better design alternative.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InKeyEvent` | `FKeyEvent` | Key event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnKeyDown`

```text
OnKeyDown(MyGeometry: FGeometry, InKeyEvent: FKeyEvent) -> FEventReply
```

Called after a key (keyboard, controller, ...) is pressed when this widget has focus (this event bubbles if not handled)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InKeyEvent` | `FKeyEvent` | Key event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnKeyUp`

```text
OnKeyUp(MyGeometry: FGeometry, InKeyEvent: FKeyEvent) -> FEventReply
```

Called after a key (keyboard, controller, ...) is released when this widget has focus

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InKeyEvent` | `FKeyEvent` | Key event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnAnalogValueChanged`

```text
OnAnalogValueChanged(MyGeometry: FGeometry, InAnalogInputEvent: FAnalogInputEvent) -> FEventReply
```

Called when an analog value changes on a button that supports analog

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `InAnalogInputEvent` | `FAnalogInputEvent` | Analog Event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnMouseButtonDown`

```text
OnMouseButtonDown(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

The system calls this method to notify the widget that a mouse button was pressed within it. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnPreviewMouseButtonDown`

```text
OnPreviewMouseButtonDown(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

Just like OnMouseButtonDown, but tunnels instead of bubbling.
	  If this even is handled, OnMouseButtonDown will not be sent.
	  
	  Use this event sparingly as preview events generally make UIs more
	  difficult to reason about.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnMouseButtonUp`

```text
OnMouseButtonUp(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

The system calls this method to notify the widget that a mouse button was release within it. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnMouseMove`

```text
OnMouseMove(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

The system calls this method to notify the widget that a mouse moved within it. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Whether the event was handled along with possible requests for the system to take action. |

### `OnMouseEnter`

```text
OnMouseEnter(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> void
```

The system will use this event to notify a widget that the cursor has entered it. This event is NOT bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The Geometry of the widget receiving the event |
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseLeave`

```text
OnMouseLeave(MouseEvent: FPointerEvent &) -> void
```

The system will use this event to notify a widget that the cursor has left it. This event is NOT bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MouseEvent` | `FPointerEvent &` | Information about the input event |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMouseWheel`

```text
OnMouseWheel(MyGeometry: FGeometry, MouseEvent: FPointerEvent &) -> FEventReply
```

Called when the mouse wheel is spun. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `MouseEvent` | `FPointerEvent &` | Mouse event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnMouseButtonDoubleClick`

```text
OnMouseButtonDoubleClick(InMyGeometry: FGeometry, InMouseEvent: FPointerEvent &) -> FEventReply
```

Called when a mouse button is double clicked.  Override this in derived classes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMyGeometry` | `FGeometry` | Widget geometry |
| `InMouseEvent` | `FPointerEvent &` | Mouse button event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnDragDetected`

```text
OnDragDetected(MyGeometry: FGeometry, PointerEvent: FPointerEvent &, Operation: UDragDropOperation * &) -> void
```

Called when Slate detects that a widget started to be dragged.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | - |
| `PointerEvent` | `FPointerEvent &` | MouseMove that triggered the drag |
| `Operation` | `UDragDropOperation * &` | The drag operation that was detected. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragCancelled`

```text
OnDragCancelled(PointerEvent: FPointerEvent &, Operation: UDragDropOperation *) -> void
```

Called when the user cancels the drag operation, typically when they simply release the mouse button after
	  beginning a drag operation, but failing to complete the drag.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent &` | Last mouse event from when the drag was canceled. |
| `Operation` | `UDragDropOperation *` | The drag operation that was canceled. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragEnter`

```text
OnDragEnter(MyGeometry: FGeometry, PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> void
```

Called during drag and drop when the drag enters the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag entered the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation that entered the widget. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragLeave`

```text
OnDragLeave(PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> void
```

Called during drag and drop when the drag leaves the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag left the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation that entered the widget. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDragOver`

```text
OnDragOver(MyGeometry: FGeometry, PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> bool
```

Called during drag and drop when the the mouse is being dragged over a widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag occurred over the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation over the widget. |

**Returns**

| Type | Description |
|---|---|
| `bool` | 'true' to indicate that you handled the drag over operation.  Returning 'false' will cause the operation to continue to bubble up. |

### `OnDrop`

```text
OnDrop(MyGeometry: FGeometry, PointerEvent: FPointerEvent, Operation: UDragDropOperation *) -> bool
```

Called when the user is dropping something onto a widget.  Ends the drag and drop operation, even if no widget handles this.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `PointerEvent` | `FPointerEvent` | The mouse event from when the drag occurred over the widget. |
| `Operation` | `UDragDropOperation *` | The drag operation over the widget. |

**Returns**

| Type | Description |
|---|---|
| `bool` | 'true' to indicate you handled the drop operation. |

### `OnTouchGesture`

```text
OnTouchGesture(MyGeometry: FGeometry, GestureEvent: FPointerEvent &) -> FEventReply
```

Called when the user performs a gesture on trackpad. This event is bubbled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `GestureEvent` | `FPointerEvent &` | gesture event |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | Returns whether the event was handled, along with other possible actions |

### `OnTouchStarted`

```text
OnTouchStarted(MyGeometry: FGeometry, InTouchEvent: FPointerEvent &) -> FEventReply
```

Called when a touchpad touch is started (finger down)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InTouchEvent` | `FPointerEvent &` | The touch event generated |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnTouchMoved`

```text
OnTouchMoved(MyGeometry: FGeometry, InTouchEvent: FPointerEvent &) -> FEventReply
```

Called when a touchpad touch is moved  (finger moved)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InTouchEvent` | `FPointerEvent &` | The touch event generated |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnTouchEnded`

```text
OnTouchEnded(MyGeometry: FGeometry, InTouchEvent: FPointerEvent &) -> FEventReply
```

Called when a touchpad touch is ended (finger lifted)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InTouchEvent` | `FPointerEvent &` | The touch event generated |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnMotionDetected`

```text
OnMotionDetected(MyGeometry: FGeometry, InMotionEvent: FMotionEvent) -> FEventReply
```

Called when motion is detected (controller or device)
	  e.g. Someone tilts or shakes their controller.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MyGeometry` | `FGeometry` | The geometry of the widget receiving the event. |
| `InMotionEvent` | `FMotionEvent` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `OnMouseCaptureLost`

```text
OnMouseCaptureLost() -> void
```

Called when mouse capture is lost if it was owned by this widget.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllChildrenOfType`

```text
GetAllChildrenOfType(Type: FString, Children: TArray < UWidget * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Type` | `FString` | - |
| `Children` | `TArray < UWidget * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTypedChildrenOfWidget`

```text
GetTypedChildrenOfWidget(Parent: UWidget *, Type: FString, Children: TArray < UWidget * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Parent` | `UWidget *` | - |
| `Type` | `FString` | - |
| `Children` | `TArray < UWidget * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationStarted`

```text
BindToAnimationStarted(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Bind an animation started delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationStarted`

```text
UnbindFromAnimationStarted(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Unbind an animation started delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationStarted`

```text
UnbindAllFromAnimationStarted(Animation: UWidgetAnimation *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationFinished`

```text
BindToAnimationFinished(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Bind an animation finished delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindFromAnimationFinished`

```text
UnbindFromAnimationFinished(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent) -> void
```

Unbind an animation finished delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnbindAllFromAnimationFinished`

```text
UnbindAllFromAnimationFinished(Animation: UWidgetAnimation *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindToAnimationEvent`

```text
BindToAnimationEvent(Animation: UWidgetAnimation *, Delegate: FWidgetAnimationDynamicEvent, AnimationEvent: EWidgetAnimationEvent, UserTag: FName) -> void
```

Allows binding to a specific animation's event.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation to listen for starting or finishing. |
| `Delegate` | `FWidgetAnimationDynamicEvent` | the delegate to call when the animation's state changes |
| `AnimationEvent` | `EWidgetAnimationEvent` | the event to watch for. |
| `UserTag` | `FName` | Scopes the delegate to only be called when the animation completes with a specific tag set on it when it was played. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimationStarted`

```text
OnAnimationStarted(Animation: UWidgetAnimation *) -> void
```

Called when an animation is started.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | the animation that started |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimationFinished`

```text
OnAnimationFinished(Animation: UWidgetAnimation *) -> void
```

Called when an animation has either played all the way through or is stopped

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Animation` | `UWidgetAnimation *` | The animation that has finished playing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorAndOpacity`

```text
SetColorAndOpacity(InColorAndOpacity: FLinearColor) -> void
```

Sets the tint of the widget, this affects all child widgets.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColorAndOpacity` | `FLinearColor` | The tint to apply to all child widgets. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetForegroundColor`

```text
SetForegroundColor(InForegroundColor: FSlateColor) -> void
```

Sets the foreground color of the widget, this is inherited by sub widgets.  Any color property 
	  that is marked as inherit will use this color.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InForegroundColor` | `FSlateColor` | The foreground color. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPadding`

```text
SetPadding(InPadding: FMargin) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPadding` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayAnimation`

```text
PlayAnimation(InAnimation: UWidgetAnimation *, StartAtTime: float, NumLoopsToPlay: int32, PlayMode: EUMGSequencePlayMode :: Type, PlaybackSpeed: float) -> void
```

Plays an animation in this widget a specified number of times

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to play |
| `StartAtTime` | `float` | The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation. |
| `NumLoopsToPlay` | `int32` | The number of times to loop this animation (0 to loop indefinitely) |
| `PlayMode` | `EUMGSequencePlayMode :: Type` | Specifies the playback mode |
| `PlaybackSpeed` | `float` | The speed at which the animation should play |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PlayAnimationTo`

```text
PlayAnimationTo(InAnimation: UWidgetAnimation *, StartAtTime: float, EndAtTime: float, NumLoopsToPlay: int32, PlayMode: EUMGSequencePlayMode :: Type, PlaybackSpeed: float) -> void
```

Plays an animation in this widget a specified number of times stoping at a specified time

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to play |
| `StartAtTime` | `float` | The time in the animation from which to start playing, relative to the start position. For looped animations, this will only affect the first playback of the animation. |
| `EndAtTime` | `float` | The absolute time in the animation where to stop, this is only considered in the last loop. |
| `NumLoopsToPlay` | `int32` | The number of times to loop this animation (0 to loop indefinitely) |
| `PlayMode` | `EUMGSequencePlayMode :: Type` | Specifies the playback mode |
| `PlaybackSpeed` | `float` | The speed at which the animation should play |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAnimation`

```text
StopAnimation(InAnimation: UWidgetAnimation *) -> void
```

Stops an already running animation in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpAnimation`

```text
JumpAnimation(InAnimation: UWidgetAnimation *, JumpAtTime: float) -> void
```

Stop and jump to the specified time in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to jump |
| `JumpAtTime` | `float` | specified time |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseAnimation`

```text
PauseAnimation(InAnimation: UWidgetAnimation *) -> float
```

Pauses an already running animation in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | the time point the animation was at when it was paused, relative to its start position.  Use this as the StartAtTime when you trigger PlayAnimation. |

### `GetAnimationCurrentTime`

```text
GetAnimationCurrentTime(InAnimation: UWidgetAnimation *) -> float
```

Gets the current time of the animation in this widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | the current time of the animation. |

### `IsAnimationPlaying`

```text
IsAnimationPlaying(InAnimation: UWidgetAnimation *) -> bool
```

Gets whether an animation is currently playing on this widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation to check the playback status of |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the animation is currently playing |

### `IsAnyAnimationPlaying`

```text
IsAnyAnimationPlaying() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | True if any animation is currently playing |

### `SetNumLoopsToPlay`

```text
SetNumLoopsToPlay(InAnimation: UWidgetAnimation *, NumLoopsToPlay: int32) -> void
```

Changes the number of loops to play given a playing animation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation that is already playing |
| `NumLoopsToPlay` | `int32` | The number of loops to play. (0 to loop indefinitely) |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaybackSpeed`

```text
SetPlaybackSpeed(InAnimation: UWidgetAnimation *, PlaybackSpeed: float) -> void
```

Changes the playback rate of a playing animation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The animation that is already playing |
| `PlaybackSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReverseAnimation`

```text
ReverseAnimation(InAnimation: UWidgetAnimation *) -> void
```

If an animation is playing, this function will reverse the playback.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The playing animation that we want to reverse |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsAnimationPlayingForward`

```text
IsAnimationPlayingForward(InAnimation: UWidgetAnimation *) -> bool
```

returns true if the animation is currently playing forward, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnimation` | `UWidgetAnimation *` | The playing animation that we want to know about |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `PlaySound`

```text
PlaySound(SoundToPlay: USoundBase *) -> void
```

Plays a sound through the UI

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoundToPlay` | `USoundBase *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetWidgetFromName`

```text
GetWidgetFromName(Name: FName &) -> UWidget *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | The uobject widget corresponding to a given name |

### `GetVariableWidgetFromName`

```text
GetVariableWidgetFromName(Name: FName &) -> UWidget *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Name` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `UWidget *` | - |

### `IsPlayingAnimation`

```text
IsPlayingAnimation() -> bool
```

Are we currently playing any animations?

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NewWidgetObjectBP`

```text
NewWidgetObjectBP(Outer: UObject *, UserWidgetClass: UClass *) -> UUserWidget *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject *` | - |
| `UserWidgetClass` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | - |

### `GetCacheLayerId`

```text
GetCacheLayerId() -> int32
```

return CacheLayerId only windows

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `ListenForInputAction`

```text
ListenForInputAction(ActionName: FName, EventType: TEnumAsByte < EInputEvent >, bConsume: bool, Callback: FOnInputAction) -> void
```

Listens for a particular Player Input Action by name.  This requires that those actions are being executed, and
	  that we're not currently in UI-Only Input Mode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName` | - |
| `EventType` | `TEnumAsByte < EInputEvent >` | - |
| `bConsume` | `bool` | - |
| `Callback` | `FOnInputAction` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopListeningForInputAction`

```text
StopListeningForInputAction(ActionName: FName, EventType: TEnumAsByte < EInputEvent >) -> void
```

Removes the binding for a particular action's callback.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName` | - |
| `EventType` | `TEnumAsByte < EInputEvent >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopListeningForAllInputActions`

```text
StopListeningForAllInputActions() -> void
```

Stops listening to all input actions, and unregisters the input component with the player controller.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RegisterInputComponent`

```text
RegisterInputComponent() -> void
```

ListenForInputAction will automatically Register an Input Component with the player input system.
	  If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
	  UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterInputComponent`

```text
UnregisterInputComponent() -> void
```

StopListeningForAllInputActions will automatically Register an Input Component with the player input system.
	  If you however, want to Pause and Resume, listening for a set of actions, the best way is to use
	  UnregisterInputComponent to pause, and RegisterInputComponent to resume listening.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsListeningForInputAction`

```text
IsListeningForInputAction(ActionName: FName) -> bool
```

Checks if the action has a registered callback with the input component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetInputActionPriority`

```text
SetInputActionPriority(NewPriority: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewPriority` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputActionBlocking`

```text
SetInputActionBlocking(bShouldBlock: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShouldBlock` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
