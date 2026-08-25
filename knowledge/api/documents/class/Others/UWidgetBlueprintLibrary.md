---
id: "api:class:UWidgetBlueprintLibrary"
title: "UWidgetBlueprintLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetBlueprintLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetBlueprintLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Create`

```text
Create(WorldContextObject: UObject *, WidgetType: TSubclassOf < UUserWidget >, OwningPlayer: APlayerController *) -> UUserWidget *
```

Creates a widget

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `WidgetType` | `TSubclassOf < UUserWidget >` | - |
| `OwningPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | - |

### `CreateDragDropOperation`

```text
CreateDragDropOperation(OperationClass: TSubclassOf < UDragDropOperation >) -> UDragDropOperation *
```

Creates a new drag and drop operation that can be returned from a drag begin to inform the UI what i
	  being dragged and dropped and what it looks like.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OperationClass` | `TSubclassOf < UDragDropOperation >` | - |

**Returns**

| Type | Description |
|---|---|
| `UDragDropOperation *` | - |

### `SetInputMode_UIOnly`

```text
SetInputMode_UIOnly(Target: APlayerController *, InWidgetToFocus: UWidget *, bLockMouseToViewport: bool) -> void
```

Setup an input mode that allows only the UI to respond to user input.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `bLockMouseToViewport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_UIOnlyEx`

```text
SetInputMode_UIOnlyEx(Target: APlayerController *, InWidgetToFocus: UWidget *, InMouseLockMode: EMouseLockMode) -> void
```

Setup an input mode that allows only the UI to respond to user input.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `InMouseLockMode` | `EMouseLockMode` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_GameAndUI`

```text
SetInputMode_GameAndUI(Target: APlayerController *, InWidgetToFocus: UWidget *, bLockMouseToViewport: bool, bHideCursorDuringCapture: bool) -> void
```

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `bLockMouseToViewport` | `bool` | - |
| `bHideCursorDuringCapture` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_GameAndUIEx`

```text
SetInputMode_GameAndUIEx(Target: APlayerController *, InWidgetToFocus: UWidget *, InMouseLockMode: EMouseLockMode, bHideCursorDuringCapture: bool) -> void
```

Setup an input mode that allows only the UI to respond to user input, and if the UI doesn't handle it player input  player controller gets a chance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |
| `InWidgetToFocus` | `UWidget *` | - |
| `InMouseLockMode` | `EMouseLockMode` | - |
| `bHideCursorDuringCapture` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInputMode_GameOnly`

```text
SetInputMode_GameOnly(Target: APlayerController *) -> void
```

Setup an input mode that allows only player input  player controller to respond to user input.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFocusToGameViewport`

```text
SetFocusToGameViewport() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawBox`

```text
DrawBox(Context: FPaintContext &, Position: FVector2D, Size: FVector2D, Brush: USlateBrushAsset *, Tint: FLinearColor) -> void
```

Draws a box

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `Position` | `FVector2D` | - |
| `Size` | `FVector2D` | - |
| `Brush` | `USlateBrushAsset *` | - |
| `Tint` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawLine`

```text
DrawLine(Context: FPaintContext &, PositionA: FVector2D, PositionB: FVector2D, Tint: FLinearColor, bAntiAlias: bool) -> void
```

Draws a line.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `PositionA` | `FVector2D` | Starting position of the line in local space. |
| `PositionB` | `FVector2D` | Ending position of the line in local space. |
| `Tint` | `FLinearColor` | Color to render the line. |
| `bAntiAlias` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawLines`

```text
DrawLines(Context: FPaintContext &, Points: TArray < FVector2D > &, Tint: FLinearColor, bAntiAlias: bool) -> void
```

Draws several line segments.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `Points` | `TArray < FVector2D > &` | Line pairs, each line needs to be 2 separate points in the array. |
| `Tint` | `FLinearColor` | Color to render the line. |
| `bAntiAlias` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawText`

```text
DrawText(Context: FPaintContext &, InString: FString &, Position: FVector2D, Tint: FLinearColor) -> void
```

Draws text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `InString` | `FString &` | The string to draw. |
| `Position` | `FVector2D` | The starting position where the text is drawn in local space. |
| `Tint` | `FLinearColor` | Color to render the line. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawTextFormatted`

```text
DrawTextFormatted(Context: FPaintContext &, Text: FText &, Position: FVector2D, Font: UFont *, FontSize: int32, FontTypeFace: FName, Tint: FLinearColor) -> void
```

Draws text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FPaintContext &` | - |
| `Text` | `FText &` | The string to draw. |
| `Position` | `FVector2D` | The starting position where the text is drawn in local space. |
| `Font` | `UFont *` | - |
| `FontSize` | `int32` | - |
| `FontTypeFace` | `FName` | - |
| `Tint` | `FLinearColor` | Color to render the line. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Handled`

```text
Handled() -> FEventReply
```

The event reply to use when you choose to handle an event.  This will prevent the event 
	  from continuing to bubble up  down the widget hierarchy.

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `Unhandled`

```text
Unhandled() -> FEventReply
```

The event reply to use when you choose not to handle an event.

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `CaptureMouse`

```text
CaptureMouse(Reply: FEventReply &, CapturingWidget: UWidget *) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `CapturingWidget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `ReleaseMouseCapture`

```text
ReleaseMouseCapture(Reply: FEventReply &) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `LockMouse`

```text
LockMouse(Reply: FEventReply &, CapturingWidget: UWidget *) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `CapturingWidget` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `UnlockMouse`

```text
UnlockMouse(Reply: FEventReply &) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `SetUserFocus`

```text
SetUserFocus(Reply: FEventReply &, FocusWidget: UWidget *, bInAllUsers: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `FocusWidget` | `UWidget *` | - |
| `bInAllUsers` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `CaptureJoystick`

```text
CaptureJoystick(Reply: FEventReply &, CapturingWidget: UWidget *, bInAllJoysticks: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `CapturingWidget` | `UWidget *` | - |
| `bInAllJoysticks` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `ClearUserFocus`

```text
ClearUserFocus(Reply: FEventReply &, bInAllUsers: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `bInAllUsers` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `ReleaseJoystickCapture`

```text
ReleaseJoystickCapture(Reply: FEventReply &, bInAllJoysticks: bool) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `bInAllJoysticks` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `SetMousePosition`

```text
SetMousePosition(Reply: FEventReply &, NewMousePosition: FVector2D) -> FEventReply
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `NewMousePosition` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `DetectDrag`

```text
DetectDrag(Reply: FEventReply &, WidgetDetectingDrag: UWidget *, DragKey: FKey) -> FEventReply
```

Ask Slate to detect if a user starts dragging in this widget later.  Slate internally tracks the movement
	  and if it surpasses the drag threshold, Slate will send an OnDragDetected event to the widget.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |
| `WidgetDetectingDrag` | `UWidget *` | Detect dragging in this widget |
| `DragKey` | `FKey` | This button should be pressed to detect the drag |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `DetectDragIfPressed`

```text
DetectDragIfPressed(PointerEvent: FPointerEvent &, WidgetDetectingDrag: UWidget *, DragKey: FKey) -> FEventReply
```

Given the pointer event, emit the DetectDrag reply if the provided key was pressed.
	  If the DragKey is a touch key, that will also automatically work.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PointerEvent` | `FPointerEvent &` | The pointer device event coming in. |
| `WidgetDetectingDrag` | `UWidget *` | Detect dragging in this widget. |
| `DragKey` | `FKey` | This button should be pressed to detect the drag, won't emit the DetectDrag FEventReply unless this is pressed. |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `EndDragDrop`

```text
EndDragDrop(Reply: FEventReply &) -> FEventReply
```

An event should return FReply::Handled().EndDragDrop() to request that the current dragdrop operation be terminated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reply` | `FEventReply &` | - |

**Returns**

| Type | Description |
|---|---|
| `FEventReply` | - |

### `IsDragDropping`

```text
IsDragDropping() -> bool
```

Returns true if a dragdrop event is occurring that a widget can handle.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDragDroppingContent`

```text
GetDragDroppingContent() -> UDragDropOperation *
```

Returns the drag and drop operation that is currently occurring if any, otherwise nothing.

**Returns**

| Type | Description |
|---|---|
| `UDragDropOperation *` | - |

### `CancelDragDrop`

```text
CancelDragDrop() -> void
```

Cancels any current drag drop operation.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeBrushFromAsset`

```text
MakeBrushFromAsset(BrushAsset: USlateBrushAsset *) -> FSlateBrush
```

Creates a Slate Brush from a Slate Brush Asset

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BrushAsset` | `USlateBrushAsset *` | - |

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush using the asset's brush. |

### `MakeBrushFromTexture`

```text
MakeBrushFromTexture(Texture: UTexture2D *, Width: int32, Height: int32) -> FSlateBrush
```

Creates a Slate Brush from a Texture2D

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - |
| `Width` | `int32` | When less than or equal to zero, the Width of the brush will default to the Width of the Texture |
| `Height` | `int32` | When less than or equal to zero, the Height of the brush will default to the Height of the Texture |

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush using the texture. |

### `MakeBrushFromMaterial`

```text
MakeBrushFromMaterial(Material: UMaterialInterface *, Width: int32, Height: int32) -> FSlateBrush
```

Creates a Slate Brush from a Material.  Materials don't have an implicit size, so providing a widget and height
	  is required to hint slate with how large the image wants to be by default.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush using the material. |

### `GetBrushResource`

```text
GetBrushResource(Brush: FSlateBrush &) -> UObject *
```

Gets the resource object on a brush.  This could be a UTexture2D or a UMaterialInterface.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetBrushResourceConst`

```text
GetBrushResourceConst(Brush: FSlateBrush &) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetBrushResourceAsTexture2D`

```text
GetBrushResourceAsTexture2D(Brush: FSlateBrush &) -> UTexture2D *
```

Gets the brush resource as a texture 2D.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UTexture2D *` | - |

### `GetBrushResourceAsMaterial`

```text
GetBrushResourceAsMaterial(Brush: FSlateBrush &) -> UMaterialInterface *
```

Gets the brush resource as a material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `SetBrushResourceToTexture`

```text
SetBrushResourceToTexture(Brush: FSlateBrush &, Texture: UTexture2D *) -> void
```

Sets the resource on a brush to be a UTexture2D.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |
| `Texture` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrushResourceToMaterial`

```text
SetBrushResourceToMaterial(Brush: FSlateBrush &, Material: UMaterialInterface *) -> void
```

Sets the resource on a brush to be a Material.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `NoResourceBrush`

```text
NoResourceBrush() -> FSlateBrush
```

Creates a Slate Brush that wont draw anything, the "Null Brush".

**Returns**

| Type | Description |
|---|---|
| `FSlateBrush` | A new slate brush that wont draw anything. |

### `GetDynamicMaterial`

```text
GetDynamicMaterial(Brush: FSlateBrush &) -> UMaterialInstanceDynamic *
```

Gets the material that allows changes to parameters at runtime.  The brush must already have a material assigned to it, 
	  if it does it will automatically be converted to a MID.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Brush` | `FSlateBrush &` | - |

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | A material that supports dynamic input from the game. |

### `DismissAllMenus`

```text
DismissAllMenus() -> void
```

Closes any popup menu

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllWidgetsOfClass`

```text
GetAllWidgetsOfClass(WorldContextObject: UObject *, FoundWidgets: TArray < UUserWidget * > &, WidgetClass: TSubclassOf < UUserWidget >, TopLevelOnly: bool) -> void
```

Find all widgets of a certain class.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `FoundWidgets` | `TArray < UUserWidget * > &` | The widgets that were found matching the filter. |
| `WidgetClass` | `TSubclassOf < UUserWidget >` | The widget class to filter by. |
| `TopLevelOnly` | `bool` | Only the widgets that are direct children of the viewport will be returned. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAllWidgetsWithInterface`

```text
GetAllWidgetsWithInterface(WorldContextObject: UObject *, Interface: TSubclassOf < UInterface >, FoundWidgets: TArray < UUserWidget * > &, TopLevelOnly: bool) -> void
```

Find all widgets in the world with the specified interface.
	 This is a slow operation, use with caution e.g. do not use every frame.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Interface` | `TSubclassOf < UInterface >` | The interface to find. Must be specified or result array will be empty. |
| `FoundWidgets` | `TArray < UUserWidget * > &` | Output array of widgets that implement the specified interface. |
| `TopLevelOnly` | `bool` | Only the widgets that are direct children of the viewport will be returned. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInputEventFromKeyEvent`

```text
GetInputEventFromKeyEvent(Event: FKeyEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FKeyEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetKeyEventFromAnalogInputEvent`

```text
GetKeyEventFromAnalogInputEvent(Event: FAnalogInputEvent &) -> FKeyEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FAnalogInputEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FKeyEvent` | - |

### `GetInputEventFromCharacterEvent`

```text
GetInputEventFromCharacterEvent(Event: FCharacterEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FCharacterEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetInputEventFromPointerEvent`

```text
GetInputEventFromPointerEvent(Event: FPointerEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FPointerEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetInputEventFromNavigationEvent`

```text
GetInputEventFromNavigationEvent(Event: FNavigationEvent &) -> FInputEvent
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `FNavigationEvent &` | - |

**Returns**

| Type | Description |
|---|---|
| `FInputEvent` | - |

### `GetSafeZonePadding`

```text
GetSafeZonePadding(WorldContextObject: UObject *, SafePadding: FVector2D &, SafePaddingScale: FVector2D &, SpillOverPadding: FVector2D &) -> void
```

Gets the amount of padding that needs to be added when accounting for the safe zone on TVs.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SafePadding` | `FVector2D &` | - |
| `SafePaddingScale` | `FVector2D &` | - |
| `SpillOverPadding` | `FVector2D &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetHardwareCursor`

```text
SetHardwareCursor(WorldContextObject: UObject *, CursorShape: EMouseCursor :: Type, CursorName: FName, HotSpot: FVector2D) -> bool
```

Loads or sets a hardware cursor from the content directory in the game.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `CursorShape` | `EMouseCursor :: Type` | - |
| `CursorName` | `FName` | - |
| `HotSpot` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ApplyUserWidgetSkin`

```text
ApplyUserWidgetSkin(UserWidget: UUserWidget *, SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >, bAsyncLoad: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UserWidget` | `UUserWidget *` | - |
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |
| `bAsyncLoad` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertUserWidgetSkin`

```text
RevertUserWidgetSkin(UserWidget: UUserWidget *, SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UserWidget` | `UUserWidget *` | - |
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
