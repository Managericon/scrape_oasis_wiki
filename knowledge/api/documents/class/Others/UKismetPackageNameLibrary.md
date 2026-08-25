---
id: "api:class:UKismetPackageNameLibrary"
title: "UKismetPackageNameLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetPackageNameLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetPackageNameLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IsValidLongPackageName`

```text
IsValidLongPackageName(InLongPackageName: FString &, bIncludeReadOnlyRoots: bool, OutReason: FText &) -> bool
```

Helper function for converting short to long script package name (InputCore -> ScriptInputCore)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLongPackageName` | `FString &` | Long Package Name |
| `bIncludeReadOnlyRoots` | `bool` | If true, will include roots that you should not save to. (Temp, Script) |
| `OutReason` | `FText &` | When returning false, this will provide a description of what was wrong with the name. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if a valid long package name |

### `IsValidObjectPath`

```text
IsValidObjectPath(InObjectPath: FString &, OutReason: FText &) -> bool
```

Returns true if the path starts with a valid root (i.e. Game, Engine, etc) and contains no illegal characters.
	  This validates that the packagename is valid, and also makes sure the object after package name is also correct.
	  This will return false if passed a path starting with Classname'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObjectPath` | `FString &` | The object path to test |
| `OutReason` | `FText &` | When returning false, this will provide a description of what was wrong with the name. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if a valid object path |

### `DoesPackageExist`

```text
DoesPackageExist(LongPackageName: FString &, Guid: FGuid &, OutFilename: FString &) -> bool
```

Checks if the given string is a long package name or not.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LongPackageName` | `FString &` | Package name. |
| `Guid` | `FGuid &` | - |
| `OutFilename` | `FString &` | Package filename on disk. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the specified package name points to an existing package, false otherwise. |

## Language

`cpp`
