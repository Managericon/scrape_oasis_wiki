---
id: "api:class:UKismetSystemLibrary"
title: "UKismetSystemLibrary"
source: "https://developer.gp.qq.com/api/class/detail/%E5%BC%95%E6%93%8E/%E5%B8%B8%E7%94%A8%E5%85%A8%E5%B1%80%E7%B1%BB/UKismetSystemLibrary.json"
category: "API Wiki/class/引擎/常用全局类"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetSystemLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `StackTrace`

```text
StackTrace() -> void
```

Prints a stack trace to the log, so you can see how a blueprint got to this node

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsValid`

```text
IsValid(Object: UObject *) -> bool
```

对象是否可用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true可用，false不可用 |

### `IsRecycled`

```text
IsRecycled(Object: UObject *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValidClass`

```text
IsValidClass(Class: UClass *) -> bool
```

类型是否可用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Class` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true可用，false不可用 |

### `GetObjectName`

```text
GetObjectName(Object: UObject *) -> FString
```

获取对象名称

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | 对象实际名称 |

### `GetPathName`

```text
GetPathName(Object: UObject *) -> FString
```

获取对象路径

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | 对象完整路径 |

### `GetDisplayName`

```text
GetDisplayName(Object: UObject *) -> FString
```

获取对象展示名称

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | 对象展示名称 |

### `GetClassDisplayName`

```text
GetClassDisplayName(Class: UClass *) -> FString
```

获取类展示名称

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Class` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | 类展示名称 |

### `StripObjectClass`

```text
StripObjectClass(PathName: FString &, bAssertOnBadPath: bool) -> FString
```

If there is an object class, strips it off.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PathName` | `FString &` | - |
| `bAssertOnBadPath` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetEngineVersion`

```text
GetEngineVersion() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetGameName`

```text
GetGameName() -> FString
```

Get the name of the current game

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetGameBundleId`

```text
GetGameBundleId() -> FString
```

Retrieves the game's platform-specific bundle identifier or package name of the game

**Returns**

| Type | Description |
|---|---|
| `FString` | The game's bundle identifier or package name. |

### `GetPlatformUserName`

```text
GetPlatformUserName() -> FString
```

Get the current user name from the OS

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `DoesImplementInterface`

```text
DoesImplementInterface(TestObject: UObject *, Interface: TSubclassOf < UInterface >) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TestObject` | `UObject *` | - |
| `Interface` | `TSubclassOf < UInterface >` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetGameTimeInSeconds`

```text
GetGameTimeInSeconds(WorldContextObject: UObject *) -> float
```

Get the current game time, in seconds. This stops when the game is paused and is affected by slomo.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | World context |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsServer`

```text
IsServer(WorldContextObject: UObject *) -> bool
```

Returns whether the world this object is in is the host or not

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsDedicatedServer`

```text
IsDedicatedServer(WorldContextObject: UObject *) -> bool
```

Returns whether this is running on a dedicated server

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsStandalone`

```text
IsStandalone(WorldContextObject: UObject *) -> bool
```

Returns whether this game instance is stand alone (no networking).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsPackagedForDistribution`

```text
IsPackagedForDistribution() -> bool
```

Returns whether this is a build that is packaged for distribution

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetUniqueDeviceId`

```text
GetUniqueDeviceId() -> FString
```

Returns the platform specific unique device id

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetDeviceId`

```text
GetDeviceId() -> FString
```

Returns the platform specific unique device id

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_InterfaceToObject`

```text
Conv_InterfaceToObject(Interface: FScriptInterface &) -> UObject *
```

Converts an interfance into an object

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Interface` | `FScriptInterface &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `MakeSoftObjectPath`

```text
MakeSoftObjectPath(PathString: FString &) -> FSoftObjectPath
```

将路径字符串转换为SoftObjectPath

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PathString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | SoftObjectPath |

### `BreakSoftObjectPath`

```text
BreakSoftObjectPath(InSoftObjectPath: FSoftObjectPath, PathString: FString &) -> void
```

将SoftObjectPath转换为路径字符串

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSoftObjectPath` | `FSoftObjectPath` | - |
| `PathString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | PathString |

### `BreakSoftClassPath`

```text
BreakSoftClassPath(InSoftClassPath: FSoftClassPath, PathString: FString &) -> void
```

将SoftClassPath转换为路径字符串

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSoftClassPath` | `FSoftClassPath` | - |
| `PathString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | PathString |

### `IsValidSoftObjectReference`

```text
IsValidSoftObjectReference(SoftObjectReference: TSoftObjectPtr < UObject > &) -> bool
```

SoftObjectPath是否有效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftObjectReference` | `TSoftObjectPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true为有效 |

### `Conv_SoftObjectReferenceToString`

```text
Conv_SoftObjectReferenceToString(SoftObjectReference: TSoftObjectPtr < UObject > &) -> FString
```

Converts a Soft Object Reference to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftObjectReference` | `TSoftObjectPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `EqualEqual_SoftObjectReference`

```text
EqualEqual_SoftObjectReference(A: TSoftObjectPtr < UObject > &, B: TSoftObjectPtr < UObject > &) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSoftObjectPtr < UObject > &` | - |
| `B` | `TSoftObjectPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_SoftObjectReference`

```text
NotEqual_SoftObjectReference(A: TSoftObjectPtr < UObject > &, B: TSoftObjectPtr < UObject > &) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSoftObjectPtr < UObject > &` | - |
| `B` | `TSoftObjectPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValidSoftClassReference`

```text
IsValidSoftClassReference(SoftClassReference: TSoftClassPtr < UObject > &) -> bool
```

Returns true if the Soft Class Reference is not null

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftClassReference` | `TSoftClassPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Conv_SoftClassReferenceToString`

```text
Conv_SoftClassReferenceToString(SoftClassReference: TSoftClassPtr < UObject > &) -> FString
```

Converts a Soft Class Reference to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftClassReference` | `TSoftClassPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `EqualEqual_SoftClassReference`

```text
EqualEqual_SoftClassReference(A: TSoftClassPtr < UObject > &, B: TSoftClassPtr < UObject > &) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSoftClassPtr < UObject > &` | - |
| `B` | `TSoftClassPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_SoftClassReference`

```text
NotEqual_SoftClassReference(A: TSoftClassPtr < UObject > &, B: TSoftClassPtr < UObject > &) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSoftClassPtr < UObject > &` | - |
| `B` | `TSoftClassPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Conv_SoftObjectReferenceToObject`

```text
Conv_SoftObjectReferenceToObject(SoftObject: TSoftObjectPtr < UObject > &) -> UObject *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftObject` | `TSoftObjectPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `Conv_SoftClassReferenceToClass`

```text
Conv_SoftClassReferenceToClass(SoftClass: TSoftClassPtr < UObject > &) -> TSubclassOf < UObject >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftClass` | `TSoftClassPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `TSubclassOf < UObject >` | - |

### `Conv_ObjectToSoftObjectReference`

```text
Conv_ObjectToSoftObjectReference(Object: UObject *) -> TSoftObjectPtr < UObject >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `TSoftObjectPtr < UObject >` | - |

### `Conv_ClassToSoftClassReference`

```text
Conv_ClassToSoftClassReference(Class: TSubclassOf < UObject > &) -> TSoftClassPtr < UObject >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Class` | `TSubclassOf < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `TSoftClassPtr < UObject >` | - |

### `LoadAssetClass`

```text
LoadAssetClass(WorldContextObject: UObject *, AssetClass: TSoftClassPtr < UObject >, OnLoaded: FOnAssetClassLoaded, LatentInfo: FLatentActionInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `AssetClass` | `TSoftClassPtr < UObject >` | - |
| `OnLoaded` | `FOnAssetClassLoaded` | - |
| `LatentInfo` | `FLatentActionInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeLiteralInt`

```text
MakeLiteralInt(Value: int32) -> int32
```

Creates a literal integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | value to set the integer to |

**Returns**

| Type | Description |
|---|---|
| `int32` | The literal integer |

### `LoadAsset`

```text
LoadAsset(WorldContextObject: UObject *, Asset: TSoftObjectPtr < UObject >, OnLoaded: FOnAssetLoaded, LatentInfo: FLatentActionInfo) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Asset` | `TSoftObjectPtr < UObject >` | - |
| `OnLoaded` | `FOnAssetLoaded` | - |
| `LatentInfo` | `FLatentActionInfo` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeLiteralInt64`

```text
MakeLiteralInt64(Value: int64) -> int64
```

Creates a literal integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int64` | value to set the integer to |

**Returns**

| Type | Description |
|---|---|
| `int64` | The literal integer |

### `MakeLiteralFloat`

```text
MakeLiteralFloat(Value: float) -> float
```

Creates a literal float

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | value to set the float to |

**Returns**

| Type | Description |
|---|---|
| `float` | The literal float |

### `MakeLiteralBool`

```text
MakeLiteralBool(Value: bool) -> bool
```

Creates a literal bool

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `bool` | value to set the bool to |

**Returns**

| Type | Description |
|---|---|
| `bool` | The literal bool |

### `MakeLiteralName`

```text
MakeLiteralName(Value: FName) -> FName
```

Creates a literal name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FName` | value to set the name to |

**Returns**

| Type | Description |
|---|---|
| `FName` | The literal name |

### `MakeLiteralByte`

```text
MakeLiteralByte(Value: uint8) -> uint8
```

Creates a literal byte

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `uint8` | value to set the byte to |

**Returns**

| Type | Description |
|---|---|
| `uint8` | The literal byte |

### `MakeLiteralString`

```text
MakeLiteralString(Value: FString &) -> FString
```

Creates a literal string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FString &` | value to set the string to |

**Returns**

| Type | Description |
|---|---|
| `FString` | The literal string |

### `MakeLiteralText`

```text
MakeLiteralText(Value: FText) -> FText
```

Creates a literal FText

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `FText` | value to set the FText to |

**Returns**

| Type | Description |
|---|---|
| `FText` | The literal FText |

### `PrintString`

```text
PrintString(WorldContextObject: UObject *, InString: FString &, bPrintToScreen: bool, bPrintToLog: bool, TextColor: FLinearColor, Duration: float) -> void
```

Prints a string to the log, and optionally, to the screen
	  If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InString` | `FString &` | The string to log out |
| `bPrintToScreen` | `bool` | Whether or not to print the output to the screen |
| `bPrintToLog` | `bool` | Whether or not to print the output to the log |
| `TextColor` | `FLinearColor` | Whether or not to print the output to the console |
| `Duration` | `float` | The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PrintText`

```text
PrintText(WorldContextObject: UObject *, InText: FText, bPrintToScreen: bool, bPrintToLog: bool, TextColor: FLinearColor, Duration: float) -> void
```

Prints text to the log, and optionally, to the screen
	  If Print To Log is true, it will be visible in the Output Log window.  Otherwise it will be logged only as 'Verbose', so it generally won't show up.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InText` | `FText` | The text to log out |
| `bPrintToScreen` | `bool` | Whether or not to print the output to the screen |
| `bPrintToLog` | `bool` | Whether or not to print the output to the log |
| `TextColor` | `FLinearColor` | Whether or not to print the output to the console |
| `Duration` | `float` | The display duration (if Print to Screen is True). Using negative number will result in loading the duration time from the config. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PrintWarning`

```text
PrintWarning(InString: FString &) -> void
```

Prints a warning string to the log and the screen. Meant to be used as a way to inform the user that they misused the node.
	 
	  WARNING!! Don't change the signature of this function without fixing up all nodes using it in the compiler

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | The string to log out |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWindowTitle`

```text
SetWindowTitle(Title: FText &) -> void
```

Sets the game window title

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Title` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ExecuteConsoleCommand`

```text
ExecuteConsoleCommand(WorldContextObject: UObject *, Command: FString &, SpecificPlayer: APlayerController *, bDisableCheck: bool) -> void
```

Executes a console command, optionally on a specific controller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Command` | `FString &` | Command to send to the console |
| `SpecificPlayer` | `APlayerController *` | If specified, the console command will be routed through the specified player |
| `bDisableCheck` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ExecuteConsoleCommandDisableCheck`

```text
ExecuteConsoleCommandDisableCheck(WorldContextObject: UObject *, Command: FString &, SpecificPlayer: APlayerController *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Command` | `FString &` | - |
| `SpecificPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetConsoleVariableFloatValue`

```text
GetConsoleVariableFloatValue(VariableName: FString &) -> float
```

Attempts to retrieve the value of the specified float console variable, if it exists.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VariableName` | `FString &` | Name of the console variable to find. |

**Returns**

| Type | Description |
|---|---|
| `float` | The value if found, 0 otherwise. |

### `GetConsoleVariableIntValue`

```text
GetConsoleVariableIntValue(VariableName: FString &) -> int32
```

Attempts to retrieve the value of the specified integer console variable, if it exists.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VariableName` | `FString &` | Name of the console variable to find. |

**Returns**

| Type | Description |
|---|---|
| `int32` | The value if found, 0 otherwise. |

### `GetConsoleVariableBoolValue`

```text
GetConsoleVariableBoolValue(VariableName: FString &) -> bool
```

Evaluates, if it exists, whether the specified integer console variable has a non-zero value (true) or not (false).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VariableName` | `FString &` | Name of the console variable to find. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if found and has a non-zero value, false otherwise. |

### `QuitGame`

```text
QuitGame(WorldContextObject: UObject *, SpecificPlayer: APlayerController *, QuitPreference: TEnumAsByte < EQuitPreference :: Type >) -> void
```

Exit the current game

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SpecificPlayer` | `APlayerController *` | The specific player to quit the game. If not specified, player 0 will quit. |
| `QuitPreference` | `TEnumAsByte < EQuitPreference :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Delay`

```text
Delay(WorldContextObject: UObject *, Duration: float, LatentInfo: FLatentActionInfo) -> void
```

Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Duration` | `float` | length of delay (in seconds). |
| `LatentInfo` | `FLatentActionInfo` | The latent action. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DelayUntilNextTick`

```text
DelayUntilNextTick(WorldContextObject: UObject *, LatentInfo: FLatentActionInfo) -> void
```

Perform a latent action with a delay of one tick.  Calling again while it is counting down will be ignored.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `LatentInfo` | `FLatentActionInfo` | The latent action. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DelayReplacePreDuration`

```text
DelayReplacePreDuration(WorldContextObject: UObject *, Duration: float, IsReplacePreDuration: bool, LatentInfo: FLatentActionInfo) -> void
```

Perform a latent action with a delay (specified in seconds).  Calling again while it is counting down will be ignored.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Duration` | `float` | length of delay (in seconds). |
| `IsReplacePreDuration` | `bool` | replace previous action Duration |
| `LatentInfo` | `FLatentActionInfo` | The latent action. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RetriggerableDelay`

```text
RetriggerableDelay(WorldContextObject: UObject *, Duration: float, LatentInfo: FLatentActionInfo) -> void
```

Perform a latent action with a retriggerable delay (specified in seconds).  Calling again while it is counting down will reset the countdown to Duration.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Duration` | `float` | length of delay (in seconds). |
| `LatentInfo` | `FLatentActionInfo` | The latent action. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MoveComponentTo`

```text
MoveComponentTo(Component: USceneComponent *, TargetRelativeLocation: FVector, TargetRelativeRotation: FRotator, bEaseOut: bool, bEaseIn: bool, OverTime: float, bForceShortestRotationPath: bool, MoveAction: TEnumAsByte < EMoveComponentAction :: Type >, LatentInfo: FLatentActionInfo) -> void
```

Interpolate a component to the specified relative location and rotation over the course of OverTime seconds.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent *` | Component to interpolate |
| `TargetRelativeLocation` | `FVector` | Relative target location |
| `TargetRelativeRotation` | `FRotator` | Relative target rotation |
| `bEaseOut` | `bool` | if true we will ease out (ie end slowly) during interpolation |
| `bEaseIn` | `bool` | if true we will ease in (ie start slowly) during interpolation |
| `OverTime` | `float` | duration of interpolation |
| `bForceShortestRotationPath` | `bool` | if true we will always use the shortest path for rotation |
| `MoveAction` | `TEnumAsByte < EMoveComponentAction :: Type >` | required movement behavior @see EMoveComponentAction |
| `LatentInfo` | `FLatentActionInfo` | The latent action |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_SetTimerDelegate`

```text
K2_SetTimerDelegate(Delegate: FTimerDynamicDelegate, Time: float, bLooping: bool) -> FTimerHandle
```

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |
| `Time` | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| `bLooping` | `bool` | True to keep executing the delegate every Time seconds, false to execute delegate only once. |

**Returns**

| Type | Description |
|---|---|
| `FTimerHandle` | The timer handle to pass to other timer functions to manipulate this timer. |

### `K2_SetTimerForNextTickDelegate`

```text
K2_SetTimerForNextTickDelegate(Delegate: FTimerDynamicDelegate) -> void
```

Set a timer to execute a delegate next tick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | The timer handle to pass to other timer functions to manipulate this timer. |

### `K2_SetTimerTickDelegate`

```text
K2_SetTimerTickDelegate(Delegate: FTimerDynamicParamDelegate, Time: float, InExeFirst: bool) -> FTimerHandle
```

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicParamDelegate` | - |
| `Time` | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| `InExeFirst` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimerHandle` | The timer handle to pass to other timer functions to manipulate this timer. |

### `K2_SetTimerDelegateForLua`

```text
K2_SetTimerDelegateForLua(Delegate: FTimerDynamicDelegate, Object: UObject *, Time: float, bLooping: bool) -> FTimerHandle
```

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `Time` | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| `bLooping` | `bool` | True to keep executing the delegate every Time seconds, false to execute delegate only once. |

**Returns**

| Type | Description |
|---|---|
| `FTimerHandle` | The timer handle to pass to other timer functions to manipulate this timer. |

### `K2_ClearTimerDelegate`

```text
K2_ClearTimerDelegate(Delegate: FTimerDynamicDelegate) -> void
```

Clears a set timer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_PauseTimerDelegate`

```text
K2_PauseTimerDelegate(Delegate: FTimerDynamicDelegate) -> void
```

Pauses a set timer at its current elapsed time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_UnPauseTimerDelegate`

```text
K2_UnPauseTimerDelegate(Delegate: FTimerDynamicDelegate) -> void
```

Resumes a paused timer from its current elapsed time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_IsTimerActiveDelegate`

```text
K2_IsTimerActiveDelegate(Delegate: FTimerDynamicDelegate) -> bool
```

Returns true if a timer exists and is active for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists and is active. |

### `K2_IsTimerPausedDelegate`

```text
K2_IsTimerPausedDelegate(Delegate: FTimerDynamicDelegate) -> bool
```

Returns true if a timer exists and is paused for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists and is paused. |

### `K2_TimerExistsDelegate`

```text
K2_TimerExistsDelegate(Delegate: FTimerDynamicDelegate) -> bool
```

Returns true is a timer for the given delegate exists, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists. |

### `K2_GetTimerElapsedTimeDelegate`

```text
K2_GetTimerElapsedTimeDelegate(Delegate: FTimerDynamicDelegate) -> float
```

Returns elapsed time for the given delegate (time since current countdown iteration began).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | How long has elapsed since the current iteration of the timer began. |

### `K2_GetTimerRemainingTimeDelegate`

```text
K2_GetTimerRemainingTimeDelegate(Delegate: FTimerDynamicDelegate) -> float
```

Returns time until the timer will next execute its delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delegate` | `FTimerDynamicDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | How long is remaining in the current iteration of the timer. |

### `K2_IsValidTimerHandle`

```text
K2_IsValidTimerHandle(Handle: FTimerHandle) -> bool
```

Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTimerHandle` | The handle of the timer to check validity of. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the timer handle is valid. |

### `K2_InvalidateTimerHandle`

```text
K2_InvalidateTimerHandle(Handle: FTimerHandle &) -> FTimerHandle
```

Returns whether the timer handle is valid. This does not indicate that there is an active timer that this handle references, but rather that it once referenced a valid timer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTimerHandle &` | The handle of the timer to check validity of. |

**Returns**

| Type | Description |
|---|---|
| `FTimerHandle` | Return the invalidated timer handle for convenience. |

### `K2_ClearTimerHandle`

```text
K2_ClearTimerHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> void
```

Clears a set timer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle of the timer to clear. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_ClearAndInvalidateTimerHandle`

```text
K2_ClearAndInvalidateTimerHandle(WorldContextObject: UObject *, Handle: FTimerHandle &) -> void
```

Clears a set timer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle &` | The handle of the timer to clear. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_PauseTimerHandle`

```text
K2_PauseTimerHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> void
```

Pauses a set timer at its current elapsed time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle of the timer to pause. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_UnPauseTimerHandle`

```text
K2_UnPauseTimerHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> void
```

Resumes a paused timer from its current elapsed time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle of the timer to unpause. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_IsTimerActiveHandle`

```text
K2_IsTimerActiveHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> bool
```

Returns true if a timer exists and is active for the given handle, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle of the timer to check whether it is active. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists and is active. |

### `K2_IsTimerPausedHandle`

```text
K2_IsTimerPausedHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> bool
```

Returns true if a timer exists and is paused for the given handle, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle of the timer to check whether it is paused. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists and is paused. |

### `K2_TimerExistsHandle`

```text
K2_TimerExistsHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> bool
```

Returns true is a timer for the given handle exists, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle to check whether it exists. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists. |

### `K2_GetTimerElapsedTimeHandle`

```text
K2_GetTimerElapsedTimeHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> float
```

Returns elapsed time for the given handle (time since current countdown iteration began).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle of the timer to get the elapsed time of. |

**Returns**

| Type | Description |
|---|---|
| `float` | How long has elapsed since the current iteration of the timer began. |

### `K2_GetTimerRemainingTimeHandle`

```text
K2_GetTimerRemainingTimeHandle(WorldContextObject: UObject *, Handle: FTimerHandle) -> float
```

Returns time until the timer will next execute its handle.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Handle` | `FTimerHandle` | The handle of the timer to time remaining of. |

**Returns**

| Type | Description |
|---|---|
| `float` | How long is remaining in the current iteration of the timer. |

### `K2_SetTimer`

```text
K2_SetTimer(Object: UObject *, FunctionName: FString, Time: float, bLooping: bool) -> FTimerHandle
```

Set a timer to execute delegate. Setting an existing timer will reset that timer with updated parameters.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |
| `Time` | `float` | How long to wait before executing the delegate, in seconds. Setting a timer to <= 0 seconds will clear it if it is set. |
| `bLooping` | `bool` | true to keep executing the delegate every Time seconds, false to execute delegate only once. |

**Returns**

| Type | Description |
|---|---|
| `FTimerHandle` | The timer handle to pass to other timer functions to manipulate this timer. |

### `K2_SetTimerForNextTick`

```text
K2_SetTimerForNextTick(Object: UObject *, FunctionName: FString) -> void
```

Set a timer to execute a delegate on the next tick.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `void` | The timer handle to pass to other timer functions to manipulate this timer. |

### `K2_ClearTimer`

```text
K2_ClearTimer(Object: UObject *, FunctionName: FString) -> void
```

Clears a set timer.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_PauseTimer`

```text
K2_PauseTimer(Object: UObject *, FunctionName: FString) -> void
```

Pauses a set timer at its current elapsed time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_UnPauseTimer`

```text
K2_UnPauseTimer(Object: UObject *, FunctionName: FString) -> void
```

Resumes a paused timer from its current elapsed time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `K2_IsTimerActive`

```text
K2_IsTimerActive(Object: UObject *, FunctionName: FString) -> bool
```

Returns true if a timer exists and is active for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists and is active. |

### `K2_TimerExists`

```text
K2_TimerExists(Object: UObject *, FunctionName: FString) -> bool
```

Returns true is a timer for the given delegate exists, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists. |

### `K2_IsTimerPaused`

```text
K2_IsTimerPaused(Object: UObject *, FunctionName: FString) -> bool
```

Returns true if a timer exists and is paused for the given delegate, false otherwise.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the timer exists and is paused. |

### `K2_GetTimerElapsedTime`

```text
K2_GetTimerElapsedTime(Object: UObject *, FunctionName: FString) -> float
```

Returns elapsed time for the given delegate (time since current countdown iteration began).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `float` | How long has elapsed since the current iteration of the timer began. |

### `K2_GetTimerRemainingTime`

```text
K2_GetTimerRemainingTime(Object: UObject *, FunctionName: FString) -> float
```

Returns time until the timer will next execute its delegate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | Object that implements the delegate function. Defaults to self (this blueprint) |
| `FunctionName` | `FString` | Delegate function name. Can be a K2 function or a Custom Event. |

**Returns**

| Type | Description |
|---|---|
| `float` | How long is remaining in the current iteration of the timer. |

### `SetIntPropertyByName`

```text
SetIntPropertyByName(Object: UObject *, PropertyName: FName, Value: int32) -> void
```

Set an int32 property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInt64PropertyByName`

```text
SetInt64PropertyByName(Object: UObject *, PropertyName: FName, Value: int64) -> void
```

Set an int64 property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUInt64PropertyByName`

```text
SetUInt64PropertyByName(Object: UObject *, PropertyName: FName, Value: uint64) -> void
```

Set an uint64 property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBytePropertyByName`

```text
SetBytePropertyByName(Object: UObject *, PropertyName: FName, Value: uint8) -> void
```

Set an uint8 or enum property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatPropertyByName`

```text
SetFloatPropertyByName(Object: UObject *, PropertyName: FName, Value: float) -> void
```

Set a float property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBoolPropertyByName`

```text
SetBoolPropertyByName(Object: UObject *, PropertyName: FName, Value: bool) -> void
```

Set a bool property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetObjectPropertyByName`

```text
SetObjectPropertyByName(Object: UObject *, PropertyName: FName, Value: UObject *) -> void
```

Set an OBJECT property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetClassPropertyByName`

```text
SetClassPropertyByName(Object: UObject *, PropertyName: FName, Value: TSubclassOf < UObject >) -> void
```

Set a CLASS property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TSubclassOf < UObject >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetInterfacePropertyByName`

```text
SetInterfacePropertyByName(Object: UObject *, PropertyName: FName, Value: FScriptInterface &) -> void
```

Set an INTERFACE property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FScriptInterface &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNamePropertyByName`

```text
SetNamePropertyByName(Object: UObject *, PropertyName: FName, Value: FName &) -> void
```

Set a NAME property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSoftObjectPropertyByName`

```text
SetSoftObjectPropertyByName(Object: UObject *, PropertyName: FName, Value: TSoftObjectPtr < UObject > &) -> void
```

Set a SOFTOBJECT property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TSoftObjectPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSoftClassPropertyByName`

```text
SetSoftClassPropertyByName(Object: UObject *, PropertyName: FName, Value: TSoftClassPtr < UObject > &) -> void
```

Set a SOFTCLASS property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TSoftClassPtr < UObject > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStringPropertyByName`

```text
SetStringPropertyByName(Object: UObject *, PropertyName: FName, Value: FString &) -> void
```

Set a STRING property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTextPropertyByName`

```text
SetTextPropertyByName(Object: UObject *, PropertyName: FName, Value: FText &) -> void
```

Set a TEXT property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorPropertyByName`

```text
SetVectorPropertyByName(Object: UObject *, PropertyName: FName, Value: FVector &) -> void
```

Set a VECTOR property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRotatorPropertyByName`

```text
SetRotatorPropertyByName(Object: UObject *, PropertyName: FName, Value: FRotator &) -> void
```

Set a ROTATOR property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FRotator &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLinearColorPropertyByName`

```text
SetLinearColorPropertyByName(Object: UObject *, PropertyName: FName, Value: FLinearColor &) -> void
```

Set a LINEAR COLOR property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTransformPropertyByName`

```text
SetTransformPropertyByName(Object: UObject *, PropertyName: FName, Value: FTransform &) -> void
```

Set a TRANSFORM property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCollisionProfileNameProperty`

```text
SetCollisionProfileNameProperty(Object: UObject *, PropertyName: FName, Value: FCollisionProfileName &) -> void
```

Set a CollisionProfileName property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FCollisionProfileName &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetStructurePropertyByName`

```text
SetStructurePropertyByName(Object: UObject *, PropertyName: FName, Value: FGenericStruct &) -> void
```

Set a custom structure property by name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `FGenericStruct &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SphereOverlapActors`

```text
SphereOverlapActors(WorldContextObject: UObject *, SpherePos: FVector, SphereRadius: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ActorClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutActors: TArray < AActor * > &) -> bool
```

返回一组跟指定球体范围发生重叠的Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `SpherePos` | `FVector` | 球心位置 |
| `SphereRadius` | `float` | 球体半径 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ActorClassFilter` | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutActors` | `TArray < AActor * > &` | 输出的产生碰撞的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `SphereOverlapComponents`

```text
SphereOverlapComponents(WorldContextObject: UObject *, SpherePos: FVector, SphereRadius: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ComponentClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutComponents: TArray < UPrimitiveComponent * > &) -> bool
```

返回一组跟指定球体范围发生重叠的Component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `SpherePos` | `FVector` | 球心位置 |
| `SphereRadius` | `float` | 球体半径 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ComponentClassFilter` | `UClass *` | 组件类型过滤，只检测指定类型的组件 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutComponents` | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `BoxOverlapAnyTest`

```text
BoxOverlapAnyTest(WorldContextObject: UObject *, BoxPos: FVector, Rotator: FRotator, BoxExtent: FVector, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ActorClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &) -> bool
```

检测指定Box范围是否发生重叠

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `BoxPos` | `FVector` | Box中心位置 |
| `Rotator` | `FRotator` | Box旋转量 |
| `BoxExtent` | `FVector` | Box范围 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ActorClassFilter` | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `BoxOverlapActors`

```text
BoxOverlapActors(WorldContextObject: UObject *, BoxPos: FVector, BoxRotation: FRotator, BoxExtent: FVector, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ActorClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutActors: TArray < AActor * > &) -> bool
```

返回一组跟指定Box范围发生重叠的Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `BoxPos` | `FVector` | Box中心位置 |
| `BoxRotation` | `FRotator` | - |
| `BoxExtent` | `FVector` | Box范围 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ActorClassFilter` | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutActors` | `TArray < AActor * > &` | 输出的产生碰撞的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `BoxOverlapOBBActors`

```text
BoxOverlapOBBActors(WorldContextObject: UObject *, BoxPos: FVector &, BoxRot: FRotator &, BoxExtent: FVector &, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ActorClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutActors: TArray < AActor * > &) -> bool
```

Returns an array of actors that overlap the given axis-aligned box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BoxPos` | `FVector &` | Center of box. |
| `BoxRot` | `FRotator &` | Rotator of box. |
| `BoxExtent` | `FVector &` | Extents of box. |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | - |
| `ActorClassFilter` | `UClass *` | - |
| `ActorsToIgnore` | `TArray < AActor * > &` | Ignore these actors in the list |
| `OutActors` | `TArray < AActor * > &` | Returned array of actors. Unsorted. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `BoxOverlapComponents`

```text
BoxOverlapComponents(WorldContextObject: UObject *, BoxPos: FVector, BoxRotation: FRotator, Extent: FVector, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ComponentClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutComponents: TArray < UPrimitiveComponent * > &) -> bool
```

返回一组跟指定Box范围发生重叠的Component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `BoxPos` | `FVector` | Box中心位置 |
| `BoxRotation` | `FRotator` | - |
| `Extent` | `FVector` | - |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ComponentClassFilter` | `UClass *` | - |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutComponents` | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `BoxOverlapOBBComponents`

```text
BoxOverlapOBBComponents(WorldContextObject: UObject *, BoxPos: FVector &, BoxRot: FRotator &, Extent: FVector &, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ComponentClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutComponents: TArray < UPrimitiveComponent * > &) -> bool
```

Returns an array of components that overlap the given axis-aligned box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BoxPos` | `FVector &` | Center of box. |
| `BoxRot` | `FRotator &` | Rotator of box. |
| `Extent` | `FVector &` | - |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | - |
| `ComponentClassFilter` | `UClass *` | - |
| `ActorsToIgnore` | `TArray < AActor * > &` | Ignore these actors in the list |
| `OutComponents` | `TArray < UPrimitiveComponent * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `CapsuleOverlapActors`

```text
CapsuleOverlapActors(WorldContextObject: UObject *, CapsulePos: FVector, Radius: float, HalfHeight: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ActorClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutActors: TArray < AActor * > &) -> bool
```

返回一组跟指定胶囊体范围发生重叠的Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `CapsulePos` | `FVector` | 胶囊体中心位置 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半高 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ActorClassFilter` | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutActors` | `TArray < AActor * > &` | Returned array of actors. Unsorted. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `CapsuleOverlapComponents`

```text
CapsuleOverlapComponents(WorldContextObject: UObject *, CapsulePos: FVector, Radius: float, HalfHeight: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ComponentClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutComponents: TArray < UPrimitiveComponent * > &) -> bool
```

返回一组跟指定胶囊体范围发生重叠的Component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | world上下文对象 |
| `CapsulePos` | `FVector` | 胶囊体中心位置 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半高 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ComponentClassFilter` | `UClass *` | - |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutComponents` | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `ComponentOverlapActors`

```text
ComponentOverlapActors(Component: UPrimitiveComponent *, ComponentTransform: FTransform &, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ActorClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutActors: TArray < AActor * > &) -> bool
```

返回一组跟指定Component发生重叠的Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | Component对象 |
| `ComponentTransform` | `FTransform &` | Component的Transform |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ActorClassFilter` | `UClass *` | 对象类型过滤，只检测指定类型的Actor |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutActors` | `TArray < AActor * > &` | 输出的产生碰撞的Actor列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `ComponentOverlapComponents`

```text
ComponentOverlapComponents(Component: UPrimitiveComponent *, ComponentTransform: FTransform &, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, ComponentClassFilter: UClass *, ActorsToIgnore: TArray < AActor * > &, OutComponents: TArray < UPrimitiveComponent * > &) -> bool
```

返回一组跟指定Component发生重叠的Component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `UPrimitiveComponent *` | Component对象 |
| `ComponentTransform` | `FTransform &` | Component的Transform |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 将结果限制为仅静态或仅动态的选项 |
| `ComponentClassFilter` | `UClass *` | - |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `OutComponents` | `TArray < UPrimitiveComponent * > &` | 输出的产生碰撞的组件列表 |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if there was an overlap that passed the filters, false otherwise. |

### `LineTraceSingle`

```text
LineTraceSingle(WorldContextObject: UObject *, Start: FVector, End: FVector, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟射线碰撞的物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `LineTraceSingleByCollisionChannel`

```text
LineTraceSingleByCollisionChannel(WorldContextObject: UObject *, Start: FVector, End: FVector, CollisionChannel: ECollisionChannel, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | - |
| `End` | `FVector` | - |
| `CollisionChannel` | `ECollisionChannel` | - |
| `bTraceComplex` | `bool` | - |
| `ActorsToIgnore` | `TArray < AActor * > &` | - |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | - |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LineTraceMulti`

```text
LineTraceMulti(WorldContextObject: UObject *, Start: FVector, End: FVector, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟射线碰撞的物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `SphereTraceSingle`

```text
SphereTraceSingle(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 球体半径 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `SphereTraceMulti`

```text
SphereTraceMulti(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 球体半径 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `BoxTraceSingle`

```text
BoxTraceSingle(WorldContextObject: UObject *, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `BoxTraceMulti`

```text
BoxTraceMulti(WorldContextObject: UObject *, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `CapsuleTraceSingle`

```text
CapsuleTraceSingle(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, HalfHeight: float, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半长高度 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `CapsuleTraceMulti`

```text
CapsuleTraceMulti(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, HalfHeight: float, TraceChannel: ETraceTypeQuery, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半长高度 |
| `TraceChannel` | `ETraceTypeQuery` | 轨迹检测通道 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `LineTraceSingleForObjects`

```text
LineTraceSingleForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟射线碰撞的物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `LineTraceSingleByObjectType`

```text
LineTraceSingleByObjectType(WorldContextObject: UObject *, Start: FVector, End: FVector, ObjectTypes: TArray < TEnumAsByte < ECollisionChannel > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | - |
| `End` | `FVector` | - |
| `ObjectTypes` | `TArray < TEnumAsByte < ECollisionChannel > > &` | - |
| `bTraceComplex` | `bool` | - |
| `ActorsToIgnore` | `TArray < AActor * > &` | - |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | - |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LineTraceMultiForObjects`

```text
LineTraceMultiForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟射线碰撞的物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `SphereTraceSingleForObjects`

```text
SphereTraceSingleForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 球体半径 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `SphereTraceMultiForObjects`

```text
SphereTraceMultiForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 球体半径 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `BoxTraceSingleForObjects`

```text
BoxTraceSingleForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `BoxTraceMultiForObjects`

```text
BoxTraceMultiForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `CapsuleTraceSingleForObjects`

```text
CapsuleTraceSingleForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, HalfHeight: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半长高度 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `CapsuleTraceMultiForObjects`

```text
CapsuleTraceMultiForObjects(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, HalfHeight: float, ObjectTypes: TArray < TEnumAsByte < EObjectTypeQuery > > &, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半长高度 |
| `ObjectTypes` | `TArray < TEnumAsByte < EObjectTypeQuery > > &` | 对象类型列表 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `LineTraceSingleByProfile`

```text
LineTraceSingleByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟射线碰撞的物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `LineTraceMultiByProfile`

```text
LineTraceMultiByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟射线碰撞的物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `SphereTraceSingleByProfile`

```text
SphereTraceSingleByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟球体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 球体半径 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `SphereTraceMultiByProfile`

```text
SphereTraceMultiByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 球体半径 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `BoxTraceSingleByProfile`

```text
BoxTraceSingleByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟Box沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `BoxTraceMultiByProfile`

```text
BoxTraceMultiByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `CapsuleTraceSingleByProfile`

```text
CapsuleTraceSingleByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, HalfHeight: float, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHit: FHitResult &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回第一个跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半长高度 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHit` | `FHitResult &` | 输出的HitResult |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a hit, false otherwise. |

### `CapsuleTraceMultiByProfile`

```text
CapsuleTraceMultiByProfile(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, HalfHeight: float, ProfileName: FName, bTraceComplex: bool, ActorsToIgnore: TArray < AActor * > &, DrawDebugType: EDrawDebugTrace :: Type, OutHits: TArray < FHitResult > &, bIgnoreSelf: bool, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: float) -> bool
```

返回所有跟胶囊体沿射线移动扫过区域碰撞物体的碰撞信息，按照指定碰撞预设查询

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `float` | 胶囊体半径 |
| `HalfHeight` | `float` | 胶囊体半长高度 |
| `ProfileName` | `FName` | 预设名称 |
| `bTraceComplex` | `bool` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `TArray < AActor * > &` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace :: Type` | - |
| `OutHits` | `TArray < FHitResult > &` | 输出的HitResult列表 |
| `bIgnoreSelf` | `bool` | - |
| `TraceColor` | `FLinearColor` | - |
| `TraceHitColor` | `FLinearColor` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if there was a blocking hit, false otherwise. |

### `GetActorListFromComponentList`

```text
GetActorListFromComponentList(ComponentList: TArray < UPrimitiveComponent * > &, ActorClassFilter: UClass *, OutActorList: TArray < AActor * > &) -> void
```

Returns an array of unique actors represented by the given list of components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ComponentList` | `TArray < UPrimitiveComponent * > &` | List of components. |
| `ActorClassFilter` | `UClass *` | - |
| `OutActorList` | `TArray < AActor * > &` | Start of line segment. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PrintToScreen`

```text
PrintToScreen(InString: FString &, TextColor: FLinearColor, TextScale: FVector2D, Duration: float, bIsUGC: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |
| `TextColor` | `FLinearColor` | - |
| `TextScale` | `FVector2D` | - |
| `Duration` | `float` | - |
| `bIsUGC` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushOnScreenDebugMessages`

```text
FlushOnScreenDebugMessages() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugLine`

```text
DrawDebugLine(WorldContextObject: UObject *, LineStart: FVector, LineEnd: FVector, LineColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draw a debug line

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `LineStart` | `FVector` | - |
| `LineEnd` | `FVector` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugCircle`

```text
DrawDebugCircle(WorldContextObject: UObject *, Center: FVector, Radius: float, NumSegments: int32, LineColor: FLinearColor, Duration: float, Thickness: float, YAxis: FVector, ZAxis: FVector, bDrawAxis: bool) -> void
```

Draw a debug circle!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Center` | `FVector` | - |
| `Radius` | `float` | - |
| `NumSegments` | `int32` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |
| `YAxis` | `FVector` | - |
| `ZAxis` | `FVector` | - |
| `bDrawAxis` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugPoint`

```text
DrawDebugPoint(WorldContextObject: UObject *, Position: FVector, Size: float, PointColor: FLinearColor, Duration: float) -> void
```

Draw a debug point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Position` | `FVector` | - |
| `Size` | `float` | - |
| `PointColor` | `FLinearColor` | - |
| `Duration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugArrow`

```text
DrawDebugArrow(WorldContextObject: UObject *, LineStart: FVector, LineEnd: FVector, ArrowSize: float, LineColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draw directional arrow, pointing from LineStart to LineEnd.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `LineStart` | `FVector` | - |
| `LineEnd` | `FVector` | - |
| `ArrowSize` | `float` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugBox`

```text
DrawDebugBox(WorldContextObject: UObject *, Center: FVector, Extent: FVector, LineColor: FLinearColor, Rotation: FRotator, Duration: float, Thickness: float) -> void
```

Draw a debug box

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Center` | `FVector` | - |
| `Extent` | `FVector` | - |
| `LineColor` | `FLinearColor` | - |
| `Rotation` | `FRotator` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugCoordinateSystem`

```text
DrawDebugCoordinateSystem(WorldContextObject: UObject *, AxisLoc: FVector, AxisRot: FRotator, Scale: float, Duration: float, Thickness: float) -> void
```

Draw a debug coordinate system.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `AxisLoc` | `FVector` | - |
| `AxisRot` | `FRotator` | - |
| `Scale` | `float` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugSphere`

```text
DrawDebugSphere(WorldContextObject: UObject *, Center: FVector, Radius: float, Segments: int32, LineColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draw a debug sphere

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Center` | `FVector` | - |
| `Radius` | `float` | - |
| `Segments` | `int32` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugCylinder`

```text
DrawDebugCylinder(WorldContextObject: UObject *, Start: FVector, End: FVector, Radius: float, Segments: int32, LineColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draw a debug cylinder

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Start` | `FVector` | - |
| `End` | `FVector` | - |
| `Radius` | `float` | - |
| `Segments` | `int32` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugCone`

```text
DrawDebugCone(WorldContextObject: UObject *, Origin: FVector, Direction: FVector, Length: float, AngleWidth: float, AngleHeight: float, NumSides: int32, LineColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draw a debug cone

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector` | - |
| `Direction` | `FVector` | - |
| `Length` | `float` | - |
| `AngleWidth` | `float` | - |
| `AngleHeight` | `float` | - |
| `NumSides` | `int32` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugConeInDegrees`

```text
DrawDebugConeInDegrees(WorldContextObject: UObject *, Origin: FVector, Direction: FVector, Length: float, AngleWidth: float, AngleHeight: float, NumSides: int32, LineColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draw a debug cone
	  Angles are specified in degrees

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Origin` | `FVector` | - |
| `Direction` | `FVector` | - |
| `Length` | `float` | - |
| `AngleWidth` | `float` | - |
| `AngleHeight` | `float` | - |
| `NumSides` | `int32` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugCapsule`

```text
DrawDebugCapsule(WorldContextObject: UObject *, Center: FVector, HalfHeight: float, Radius: float, Rotation: FRotator, LineColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draw a debug capsule

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Center` | `FVector` | - |
| `HalfHeight` | `float` | - |
| `Radius` | `float` | - |
| `Rotation` | `FRotator` | - |
| `LineColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugString`

```text
DrawDebugString(WorldContextObject: UObject *, TextLocation: FVector, Text: FString &, TestBaseActor: AActor *, TextColor: FLinearColor, Duration: float) -> void
```

Draw a debug string at a 3d world location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextLocation` | `FVector` | - |
| `Text` | `FString &` | - |
| `TestBaseActor` | `AActor *` | - |
| `TextColor` | `FLinearColor` | - |
| `Duration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugPlane`

```text
DrawDebugPlane(WorldContextObject: UObject *, PlaneCoordinates: FPlane &, Location: FVector, Size: float, PlaneColor: FLinearColor, Duration: float) -> void
```

Draws a debug plane.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PlaneCoordinates` | `FPlane &` | - |
| `Location` | `FVector` | - |
| `Size` | `float` | - |
| `PlaneColor` | `FLinearColor` | - |
| `Duration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushPersistentDebugLines`

```text
FlushPersistentDebugLines(WorldContextObject: UObject *) -> void
```

Flush all persistent debug lines and shapes.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FlushDebugStrings`

```text
FlushDebugStrings(WorldContextObject: UObject *) -> void
```

Removes all debug strings.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugFrustum`

```text
DrawDebugFrustum(WorldContextObject: UObject *, FrustumTransform: FTransform &, FrustumColor: FLinearColor, Duration: float, Thickness: float) -> void
```

Draws a debug frustum.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `FrustumTransform` | `FTransform &` | - |
| `FrustumColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugCamera`

```text
DrawDebugCamera(CameraActor: ACameraActor *, CameraColor: FLinearColor, Duration: float) -> void
```

Draw a debug camera shape.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CameraActor` | `ACameraActor *` | - |
| `CameraColor` | `FLinearColor` | - |
| `Duration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugFloatHistoryTransform`

```text
DrawDebugFloatHistoryTransform(WorldContextObject: UObject *, FloatHistory: FDebugFloatHistory &, DrawTransform: FTransform &, DrawSize: FVector2D, DrawColor: FLinearColor, Duration: float) -> void
```

Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawTransform for the position in the world.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `FloatHistory` | `FDebugFloatHistory &` | - |
| `DrawTransform` | `FTransform &` | - |
| `DrawSize` | `FVector2D` | - |
| `DrawColor` | `FLinearColor` | - |
| `Duration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugFloatHistoryLocation`

```text
DrawDebugFloatHistoryLocation(WorldContextObject: UObject *, FloatHistory: FDebugFloatHistory &, DrawLocation: FVector, DrawSize: FVector2D, DrawColor: FLinearColor, Duration: float) -> void
```

Draws a 2D Histogram of size 'DrawSize' based FDebugFloatHistory struct, using DrawLocation for the location in the world, rotation will face camera of first player.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `FloatHistory` | `FDebugFloatHistory &` | - |
| `DrawLocation` | `FVector` | - |
| `DrawSize` | `FVector2D` | - |
| `DrawColor` | `FLinearColor` | - |
| `Duration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddFloatHistorySample`

```text
AddFloatHistorySample(Value: float, FloatHistory: FDebugFloatHistory &) -> FDebugFloatHistory
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `FloatHistory` | `FDebugFloatHistory &` | - |

**Returns**

| Type | Description |
|---|---|
| `FDebugFloatHistory` | - |

### `DrawDebugActorName`

```text
DrawDebugActorName(Actor: AActor *, Offset: FVector, LinearColor: FLinearColor, Duration: float) -> void
```

绘制Actor名称

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `Offset` | `FVector` | - |
| `LinearColor` | `FLinearColor` | - |
| `Duration` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugActorMoveTrack`

```text
DrawDebugActorMoveTrack(Actor: AActor *, LinearColor: FLinearColor, Duration: float, Thickness: float) -> void
```

绘制Actor运动轨迹

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `LinearColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugDistance`

```text
DrawDebugDistance(WorldContextObject: UObject *, Self: FVector, Target: FVector, LinearColor: FLinearColor, Duration: float, Thickness: float) -> void
```

绘制Self到Tartget的连线与距离

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Self` | `FVector` | - |
| `Target` | `FVector` | - |
| `LinearColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugTargetAimedAt`

```text
DrawDebugTargetAimedAt(WorldContextObject: UObject *, Length: float, DrawTime: float) -> void
```

绘制准心瞄准物体名称

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Length` | `float` | - |
| `DrawTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugActorCollision`

```text
DrawDebugActorCollision(Actor: AActor *, LinearColor: FLinearColor, Duration: float, Thickness: float) -> void
```

绘制碰撞盒

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `LinearColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DrawDebugActorBounds`

```text
DrawDebugActorBounds(Actor: AActor *, LinearColor: FLinearColor, Duration: float, Thickness: float) -> void
```

绘制Actor的包围盒

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `LinearColor` | `FLinearColor` | - |
| `Duration` | `float` | - |
| `Thickness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateCopyForUndoBuffer`

```text
CreateCopyForUndoBuffer(ObjectToModify: UObject *) -> void
```

Mark as modified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectToModify` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetComponentBounds`

```text
GetComponentBounds(Component: USceneComponent *, Origin: FVector &, BoxExtent: FVector &, SphereRadius: float &) -> void
```

Get bounds

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Component` | `USceneComponent *` | - |
| `Origin` | `FVector &` | - |
| `BoxExtent` | `FVector &` | - |
| `SphereRadius` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActorBounds`

```text
GetActorBounds(Actor: AActor *, Origin: FVector &, BoxExtent: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor *` | - |
| `Origin` | `FVector &` | - |
| `BoxExtent` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetRenderingDetailMode`

```text
GetRenderingDetailMode() -> int32
```

Get the clamped state of r.DetailMode, see console variable help (allows for scalability, cannot be used in construction scripts)
	  0: low, show only object with DetailMode low or higher
	  1: medium, show all object with DetailMode medium or higher
	  2: high, show all objects

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetRenderingMaterialQualityLevel`

```text
GetRenderingMaterialQualityLevel() -> int32
```

Get the clamped state of r.MaterialQualityLevel, see console variable help (allows for scalability, cannot be used in construction scripts)
	  0: low
	  1: high
	  2: medium
	  3: ultimatehigh

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetSupportedFullscreenResolutions`

```text
GetSupportedFullscreenResolutions(Resolutions: TArray < FIntPoint > &) -> bool
```

Gets the list of support fullscreen resolutions.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Resolutions` | `TArray < FIntPoint > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if successfully queried the device for available resolutions. |

### `GetConvenientWindowedResolutions`

```text
GetConvenientWindowedResolutions(Resolutions: TArray < FIntPoint > &) -> bool
```

Gets the list of windowed resolutions which are convenient for the current primary display size.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Resolutions` | `TArray < FIntPoint > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if successfully queried the device for available resolutions. |

### `GetMinYResolutionForUI`

```text
GetMinYResolutionForUI() -> int32
```

Gets the smallest Y resolution we want to support in the UI, clamped within reasons

**Returns**

| Type | Description |
|---|---|
| `int32` | value in pixels |

### `GetMinYResolutionFor3DView`

```text
GetMinYResolutionFor3DView() -> int32
```

Gets the smallest Y resolution we want to support in the 3D view, clamped within reasons

**Returns**

| Type | Description |
|---|---|
| `int32` | value in pixels |

### `LaunchURL`

```text
LaunchURL(URL: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanLaunchURL`

```text
CanLaunchURL(URL: FString &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `URL` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `CollectGarbage`

```text
CollectGarbage(bFullPurge: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bFullPurge` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTimeSinceLastPendingKillPurge`

```text
GetTimeSinceLastPendingKillPurge() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `ShowAdBanner`

```text
ShowAdBanner(AdIdIndex: int32, bShowOnBottomOfScreen: bool) -> void
```

Will show an ad banner (iAd on iOS, or AdMob on Android) on the top or bottom of screen, on top of the GL view (doesn't resize the view)
	  (iOS and Android only)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AdIdIndex` | `int32` | The index of the ID to select for the ad to show |
| `bShowOnBottomOfScreen` | `bool` | If true, the iAd will be shown at the bottom of the screen, top otherwise |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAdIDCount`

```text
GetAdIDCount() -> int32
```

Retrieves the total number of Ad IDs that can be selected between

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `HideAdBanner`

```text
HideAdBanner() -> void
```

Hides the ad banner (iAd on iOS, or AdMob on Android). Will force close the ad if it's open
	  (iOS and Android only)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceCloseAdBanner`

```text
ForceCloseAdBanner() -> void
```

Forces closed any displayed ad. Can lead to loss of revenue
	  (iOS and Android only)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LoadInterstitialAd`

```text
LoadInterstitialAd(AdIdIndex: int32) -> void
```

Will load a fullscreen interstitial AdMob ad. Call this before using ShowInterstitialAd
	 (Android only)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AdIdIndex` | `int32` | The index of the ID to select for the ad to show |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsInterstitialAdAvailable`

```text
IsInterstitialAdAvailable() -> bool
```

Returns true if the requested interstitial ad is loaded and ready
	 (Android only)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsInterstitialAdRequested`

```text
IsInterstitialAdRequested() -> bool
```

Returns true if the requested interstitial ad has been successfully requested (false if load request fails)
	 (Android only)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ShowInterstitialAd`

```text
ShowInterstitialAd() -> void
```

Shows the loaded interstitial ad (loaded with LoadInterstitialAd)
	 (Android only)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowPlatformSpecificLeaderboardScreen`

```text
ShowPlatformSpecificLeaderboardScreen(CategoryName: FString &) -> void
```

Displays the built-in leaderboard GUI (iOS and Android only; this function may be renamed or moved in a future release)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CategoryName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowPlatformSpecificAchievementsScreen`

```text
ShowPlatformSpecificAchievementsScreen(SpecificPlayer: APlayerController *) -> void
```

Displays the built-in achievements GUI (iOS and Android only; this function may be renamed or moved in a future release)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpecificPlayer` | `APlayerController *` | Specific player's achievements to show. May not be supported on all platforms. If null, defaults to the player with ControllerId 0 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsLoggedIn`

```text
IsLoggedIn(SpecificPlayer: APlayerController *) -> bool
```

Returns whether the player is logged in to the currently active online subsystem.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpecificPlayer` | `APlayerController *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ControlScreensaver`

```text
ControlScreensaver(bAllowScreenSaver: bool) -> void
```

Allows or inhibits screensaver

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bAllowScreenSaver` | `bool` | If false, don't allow screensaver if possible, otherwise allow default behavior |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumeButtonsHandledBySystem`

```text
SetVolumeButtonsHandledBySystem(bEnabled: bool) -> void
```

Allows or inhibits system default handling of volume up and volume down buttons (Android only)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `bool` | If true, allow Android to handle volume up and down events |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetVolumeButtonsHandledBySystem`

```text
GetVolumeButtonsHandledBySystem() -> bool
```

Returns true if system default handling of volume up and volume down buttons enabled (Android only)

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ResetGamepadAssignments`

```text
ResetGamepadAssignments() -> void
```

Resets the gamepad to player controller id assignments (Android only)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetGamepadAssignmentToController`

```text
ResetGamepadAssignmentToController(ControllerId: int32) -> void
```

Resets the gamepad assignment to player controller id (Android only)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControllerId` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsControllerAssignedToGamepad`

```text
IsControllerAssignedToGamepad(ControllerId: int32) -> bool
```

Returns true if controller id assigned to a gamepad (Android only)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControllerId` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetSuppressViewportTransitionMessage`

```text
SetSuppressViewportTransitionMessage(WorldContextObject: UObject *, bState: bool) -> void
```

Sets the state of the transition message rendered by the viewport. (The blue text displayed when the game is paused and so forth.)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | World context |
| `bState` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPreferredLanguages`

```text
GetPreferredLanguages() -> TArray < FString >
```

Returns an array of the user's preferred languages in order of preference

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | An array of language IDs ordered from most preferred to least |

### `GetDefaultLanguage`

```text
GetDefaultLanguage() -> FString
```

Get the default language (for localization) used by this platform

**Returns**

| Type | Description |
|---|---|
| `FString` | The language as an IETF language tag (eg, "zh-Hans-CN") |

### `GetDefaultLocale`

```text
GetDefaultLocale() -> FString
```

Get the default locale (for internationalization) used by this platform

**Returns**

| Type | Description |
|---|---|
| `FString` | The locale as an IETF language tag (eg, "zh-Hans-CN") |

### `GetLocalCurrencyCode`

```text
GetLocalCurrencyCode() -> FString
```

Returns the currency code associated with the device's locale

**Returns**

| Type | Description |
|---|---|
| `FString` | the currency code associated with the device's locale |

### `GetLocalCurrencySymbol`

```text
GetLocalCurrencySymbol() -> FString
```

Returns the currency symbol associated with the device's locale

**Returns**

| Type | Description |
|---|---|
| `FString` | the currency symbol associated with the device's locale |

### `RegisterForRemoteNotifications`

```text
RegisterForRemoteNotifications() -> void
```

Requests permission to send remote notifications to the user's device.
	  (Android and iOS only)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnregisterForRemoteNotifications`

```text
UnregisterForRemoteNotifications() -> void
```

Requests Requests unregistering from receiving remote notifications to the user's device.
	 (Android only)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetUserActivity`

```text
SetUserActivity(UserActivity: FUserActivity &) -> void
```

Tells the engine what the user is doing for debug, analytics, etc.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UserActivity` | `FUserActivity &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCommandLine`

```text
GetCommandLine() -> FString
```

Returns the command line that the process was launched with.

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetObjectFromPrimaryAssetId`

```text
GetObjectFromPrimaryAssetId(PrimaryAssetId: FPrimaryAssetId) -> UObject *
```

Returns the Object associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `GetClassFromPrimaryAssetId`

```text
GetClassFromPrimaryAssetId(PrimaryAssetId: FPrimaryAssetId) -> TSubclassOf < UObject >
```

Returns the Blueprint Class associated with a Primary Asset Id, this will only return a valid object if it is in memory, it will not load it

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `TSubclassOf < UObject >` | - |

### `GetSoftObjectReferenceFromPrimaryAssetId`

```text
GetSoftObjectReferenceFromPrimaryAssetId(PrimaryAssetId: FPrimaryAssetId) -> TSoftObjectPtr < UObject >
```

Returns the Object Id associated with a Primary Asset Id, this works even if the asset is not loaded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `TSoftObjectPtr < UObject >` | - |

### `GetSoftClassReferenceFromPrimaryAssetId`

```text
GetSoftClassReferenceFromPrimaryAssetId(PrimaryAssetId: FPrimaryAssetId) -> TSoftClassPtr < UObject >
```

Returns the Blueprint Class Id associated with a Primary Asset Id, this works even if the asset is not loaded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `TSoftClassPtr < UObject >` | - |

### `GetPrimaryAssetIdFromObject`

```text
GetPrimaryAssetIdFromObject(Object: UObject *) -> FPrimaryAssetId
```

Returns the Primary Asset Id for an Object, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FPrimaryAssetId` | - |

### `GetPrimaryAssetIdFromClass`

```text
GetPrimaryAssetIdFromClass(Class: TSubclassOf < UObject >) -> FPrimaryAssetId
```

Returns the Primary Asset Id for a Class, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Class` | `TSubclassOf < UObject >` | - |

**Returns**

| Type | Description |
|---|---|
| `FPrimaryAssetId` | - |

### `GetPrimaryAssetIdFromSoftObjectReference`

```text
GetPrimaryAssetIdFromSoftObjectReference(SoftObjectReference: TSoftObjectPtr < UObject >) -> FPrimaryAssetId
```

Returns the Primary Asset Id for a Soft Object Reference, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftObjectReference` | `TSoftObjectPtr < UObject >` | - |

**Returns**

| Type | Description |
|---|---|
| `FPrimaryAssetId` | - |

### `GetPrimaryAssetIdFromSoftClassReference`

```text
GetPrimaryAssetIdFromSoftClassReference(SoftClassReference: TSoftClassPtr < UObject >) -> FPrimaryAssetId
```

Returns the Primary Asset Id for a Soft Class Reference, this can return an invalid one if not registered

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SoftClassReference` | `TSoftClassPtr < UObject >` | - |

**Returns**

| Type | Description |
|---|---|
| `FPrimaryAssetId` | - |

### `GetPrimaryAssetIdList`

```text
GetPrimaryAssetIdList(PrimaryAssetType: FPrimaryAssetType, OutPrimaryAssetIdList: TArray < FPrimaryAssetId > &) -> void
```

Returns list of PrimaryAssetIds for a PrimaryAssetType

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetType` | `FPrimaryAssetType` | - |
| `OutPrimaryAssetIdList` | `TArray < FPrimaryAssetId > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsValidPrimaryAssetId`

```text
IsValidPrimaryAssetId(PrimaryAssetId: FPrimaryAssetId) -> bool
```

Returns true if the Primary Asset Id is valid

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Conv_PrimaryAssetIdToString`

```text
Conv_PrimaryAssetIdToString(PrimaryAssetId: FPrimaryAssetId) -> FString
```

Converts a Primary Asset Id to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `EqualEqual_PrimaryAssetId`

```text
EqualEqual_PrimaryAssetId(A: FPrimaryAssetId, B: FPrimaryAssetId) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FPrimaryAssetId` | - |
| `B` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_PrimaryAssetId`

```text
NotEqual_PrimaryAssetId(A: FPrimaryAssetId, B: FPrimaryAssetId) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FPrimaryAssetId` | - |
| `B` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValidPrimaryAssetType`

```text
IsValidPrimaryAssetType(PrimaryAssetType: FPrimaryAssetType) -> bool
```

Returns list of Primary Asset Ids for a PrimaryAssetType

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetType` | `FPrimaryAssetType` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Conv_PrimaryAssetTypeToString`

```text
Conv_PrimaryAssetTypeToString(PrimaryAssetType: FPrimaryAssetType) -> FString
```

Converts a Primary Asset Type to a string. The other direction is not provided because it cannot be validated

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetType` | `FPrimaryAssetType` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `EqualEqual_PrimaryAssetType`

```text
EqualEqual_PrimaryAssetType(A: FPrimaryAssetType, B: FPrimaryAssetType) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FPrimaryAssetType` | - |
| `B` | `FPrimaryAssetType` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_PrimaryAssetType`

```text
NotEqual_PrimaryAssetType(A: FPrimaryAssetType, B: FPrimaryAssetType) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FPrimaryAssetType` | - |
| `B` | `FPrimaryAssetType` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UnloadPrimaryAsset`

```text
UnloadPrimaryAsset(PrimaryAssetId: FPrimaryAssetId) -> void
```

Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnloadPrimaryAssetList`

```text
UnloadPrimaryAssetList(PrimaryAssetIdList: TArray < FPrimaryAssetId > &) -> void
```

Unloads a primary asset, which allows it to be garbage collected if nothing else is referencing it

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetIdList` | `TArray < FPrimaryAssetId > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentBundleState`

```text
GetCurrentBundleState(PrimaryAssetId: FPrimaryAssetId, bForceCurrentState: bool, OutBundles: TArray < FName > &) -> bool
```

Returns the list of loaded bundles for a given Primary Asset. This will return false if the asset is not loaded at all.
	  If ForceCurrentState is true it will return the current state even if a load is in process

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PrimaryAssetId` | `FPrimaryAssetId` | - |
| `bForceCurrentState` | `bool` | - |
| `OutBundles` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetPrimaryAssetsWithBundleState`

```text
GetPrimaryAssetsWithBundleState(RequiredBundles: TArray < FName > &, ExcludedBundles: TArray < FName > &, ValidTypes: TArray < FPrimaryAssetType > &, bForceCurrentState: bool, OutPrimaryAssetIdList: TArray < FPrimaryAssetId > &) -> void
```

Returns the list of assets that are in a given bundle state. Required Bundles must be specified
	  If ExcludedBundles is not empty, it will not return any assets in those bundle states
	  If ValidTypes is not empty, it will only return assets of those types
	  If ForceCurrentState is true it will use the current state even if a load is in process

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RequiredBundles` | `TArray < FName > &` | - |
| `ExcludedBundles` | `TArray < FName > &` | - |
| `ValidTypes` | `TArray < FPrimaryAssetType > &` | - |
| `bForceCurrentState` | `bool` | - |
| `OutPrimaryAssetIdList` | `TArray < FPrimaryAssetId > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddResMapping`

```text
AddResMapping(InPackageNameRemap: TMap < FName , FName > &) -> void
```

Functions for Asset Redirect

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPackageNameRemap` | `TMap < FName , FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddResPathMapping`

```text
AddResPathMapping(InPackagePathRemap: TMap < FString , FString > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPackagePathRemap` | `TMap < FString , FString > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddResARMapping`

```text
AddResARMapping(InARPaths: TSet < FString > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InARPaths` | `TSet < FString > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IterateAddResARMapping`

```text
IterateAddResARMapping(InARRoot: FString &, InARPaths: TSet < FString > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InARRoot` | `FString &` | - |
| `InARPaths` | `TSet < FString > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IterateRemoveResARMapping`

```text
IterateRemoveResARMapping(InARRoot: FString &, InARPaths: TSet < FString > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InARRoot` | `FString &` | - |
| `InARPaths` | `TSet < FString > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsResARMapping`

```text
IsResARMapping(InARPath: FString &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InARPath` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveResMapping`

```text
RemoveResMapping(PathKeys: TArray < FString > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PathKeys` | `TArray < FString > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EmptyResMapping`

```text
EmptyResMapping() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddBlackResMapping`

```text
AddBlackResMapping(InPackageNames: TSet < FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPackageNames` | `TSet < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveBlackResMapping`

```text
RemoveBlackResMapping(InPackageNames: TSet < FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPackageNames` | `TSet < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EmptyBlackResMapping`

```text
EmptyBlackResMapping() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BindPackageNameResolver`

```text
BindPackageNameResolver() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UnBindPackageNameResolver`

```text
UnBindPackageNameResolver() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsPackageNameResolverBinded`

```text
IsPackageNameResolverBinded() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsARPathActivated`

```text
IsARPathActivated(InARPath: FString &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InARPath` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOriginalPath`

```text
GetOriginalPath(Path: FName &, OriginalPath: FName &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Path` | `FName &` | - |
| `OriginalPath` | `FName &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDelegateResolvedPackagePath`

```text
GetDelegateResolvedPackagePath(InSourcePackagePath: FString &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSourcePackagePath` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`
