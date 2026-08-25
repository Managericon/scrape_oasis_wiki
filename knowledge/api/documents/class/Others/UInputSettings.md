---
id: "api:class:UInputSettings"
title: "UInputSettings"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInputSettings.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInputSettings

Project wide settings for input handling

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisConfig` | `TArray < struct FInputAxisConfigEntry >` | Properties of Axis controls |
| `bAltEnterTogglesFullscreen` | `uint32` | - |
| `bF11TogglesFullscreen` | `uint32` | - |
| `bUseMouseForTouch` | `uint32` | - |
| `bEnableMouseSmoothing` | `uint32` | - |
| `bEnableFOVScaling` | `uint32` | - |
| `FOVScale` | `float` | - |
| `DoubleClickTime` | `float` | If a key is pressed twice in this amount of time it is considered a "double click" |
| `bCaptureMouseOnLaunch` | `bool` | Controls if the viewport will capture the mouse on Launch of the application |
| `DefaultViewportMouseCaptureMode` | `EMouseCaptureMode` | The default mouse capture mode for the game viewport |
| `bDefaultViewportMouseLock_DEPRECATED` | `bool` | The default mouse lock state when the viewport acquires capture |
| `DefaultViewportMouseLockMode` | `EMouseLockMode` | The default mouse lock state behavior when the viewport acquires capture |
| `ActionMappings` | `TArray < struct FInputActionKeyMapping >` | List of Action Mappings |
| `AxisMappings` | `TArray < struct FInputAxisKeyMapping >` | List of Axis Mappings |
| `bAlwaysShowTouchInterface` | `bool` | Should the touch input interface be shown always, or only when the platform has a touch screen? |
| `bShowConsoleOnFourFingerTap` | `bool` | Whether or not to show the console on 4 finger tap, on mobile platforms |
| `DefaultTouchInterface` | `FSoftObjectPath` | The default on-screen touch input interface for the game (can be null to disable the onscreen interface) |
| `ConsoleKey_DEPRECATED` | `FKey` | The key which opens the console. |
| `ConsoleKeys` | `TArray < FKey >` | The keys which open the console. |

## Functions

### `GetInputSettings`

```text
GetInputSettings() -> UInputSettings *
```

Returns the game local input settings (action mappings, axis mappings, etc...)

**Returns**

| Type | Description |
|---|---|
| `UInputSettings *` | - |

### `AddActionMapping`

```text
AddActionMapping(KeyMapping: FInputActionKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically add an action mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputActionKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActionMappingByName`

```text
GetActionMappingByName(InActionName: FName, OutMappings: TArray < FInputActionKeyMapping > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActionName` | `FName` | - |
| `OutMappings` | `TArray < FInputActionKeyMapping > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveActionMapping`

```text
RemoveActionMapping(KeyMapping: FInputActionKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically remove an action mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputActionKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddAxisMapping`

```text
AddAxisMapping(KeyMapping: FInputAxisKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically add an axis mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputAxisKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAxisMappingByName`

```text
GetAxisMappingByName(InAxisName: FName, OutMappings: TArray < FInputAxisKeyMapping > &) -> void
```

Retrieve all axis mappings by a certain name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAxisName` | `FName` | - |
| `OutMappings` | `TArray < FInputAxisKeyMapping > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveAxisMapping`

```text
RemoveAxisMapping(KeyMapping: FInputAxisKeyMapping &, bForceRebuildKeymaps: bool) -> void
```

Programmatically remove an axis mapping to the project defaults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `KeyMapping` | `FInputAxisKeyMapping &` | - |
| `bForceRebuildKeymaps` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SaveKeyMappings`

```text
SaveKeyMappings() -> void
```

Flush the current mapping values to the config file

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActionNames`

```text
GetActionNames(ActionNames: TArray < FName > &) -> void
```

Populate a list of all defined action names

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActionNames` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAxisNames`

```text
GetAxisNames(AxisNames: TArray < FName > &) -> void
```

Populate a list of all defined axis names

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisNames` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceRebuildKeymaps`

```text
ForceRebuildKeymaps() -> void
```

When changes are made to the default mappings, push those changes out to PlayerInput key maps

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplySettings`

```text
ApplySettings() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetToDefaultEditorSettings`

```text
ResetToDefaultEditorSettings() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SaveToConfig`

```text
SaveToConfig() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetActionMappings`

```text
GetActionMappings() -> TArray < struct FInputActionKeyMapping >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < struct FInputActionKeyMapping >` | - |

### `GetAxisMappings`

```text
GetAxisMappings() -> TArray < struct FInputAxisKeyMapping >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < struct FInputAxisKeyMapping >` | - |

## Language

`cpp`
