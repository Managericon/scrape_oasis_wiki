---
id: "api:class:UVisualLoggerKismetLibrary"
title: "UVisualLoggerKismetLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UVisualLoggerKismetLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UVisualLoggerKismetLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `LogText`

```text
LogText(WorldContextObject: UObject *, Text: FString, LogCategory: FName) -> void
```

Logs simple text string with Visual Logger - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Text` | `FString` | - |
| `LogCategory` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LogLocation`

```text
LogLocation(WorldContextObject: UObject *, Location: FVector, Text: FString, ObjectColor: FLinearColor, Radius: float, LogCategory: FName) -> void
```

Logs location as sphere with given radius - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Location` | `FVector` | - |
| `Text` | `FString` | - |
| `ObjectColor` | `FLinearColor` | - |
| `Radius` | `float` | - |
| `LogCategory` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LogBox`

```text
LogBox(WorldContextObject: UObject *, BoxShape: FBox, Text: FString, ObjectColor: FLinearColor, LogCategory: FName) -> void
```

Logs box shape - recording for Visual Logs has to be enabled to record this data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `BoxShape` | `FBox` | - |
| `Text` | `FString` | - |
| `ObjectColor` | `FLinearColor` | - |
| `LogCategory` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
