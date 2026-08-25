---
id: "api:class:UPlayerInput"
title: "UPlayerInput"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPlayerInput.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPlayerInput

end: 单条记录，滑屏轨迹中的一个点 

  Object within PlayerController that processes player input.
  Only exists on the client in network games.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableKeyInput` | `bool` | - |
| `InputTouchCacheDataList` | `TArray < FInputTouchCacheData >` | - |
| `DebugExecBindings` | `TArray < struct FKeyBind >` | Generic bindings of keys to Exec()-compatible strings for development purposes only |
| `InvertedAxis` | `TArray < FName >` | List of Axis Mappings that have been inverted |

## Functions

### `SetMouseSensitivity`

```text
SetMouseSensitivity(Sensitivity: float) -> void
```

Exec function to change the mouse sensitivity

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Sensitivity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBind`

```text
SetBind(BindName: FName, Command: FString &) -> void
```

Exec function to add a debug exec command

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindName` | `FName` | - |
| `Command` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvertAxisKey`

```text
InvertAxisKey(AxisKey: FKey) -> void
```

Exec function to invert an axis key

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisKey` | `FKey` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InvertAxis`

```text
InvertAxis(AxisName: FName) -> void
```

Exec function to invert an axis mapping

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AxisName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearSmoothing`

```text
ClearSmoothing() -> void
```

Exec function to reset mouse smoothing values

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
