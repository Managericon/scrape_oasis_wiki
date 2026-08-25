---
id: "api:class:UAssetRegistryHelpers"
title: "UAssetRegistryHelpers"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAssetRegistryHelpers.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAssetRegistryHelpers

## Inheritance

`UObject`

## Functions

### `GetAssetRegistry`

```text
GetAssetRegistry() -> TScriptInterface < IAssetRegistry >
```

**Returns**

| Type | Description |
|---|---|
| `TScriptInterface < IAssetRegistry >` | - |

### `CreateAssetData`

```text
CreateAssetData(InAsset: UObject *, bAllowBlueprintClass: bool) -> FAssetData
```

Creates asset data from a UObject.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAsset` | `UObject *` | The asset to create asset data for |
| `bAllowBlueprintClass` | `bool` | By default trying to create asset data for a blueprint class will create one for the UBlueprint instead |

**Returns**

| Type | Description |
|---|---|
| `FAssetData` | - |

### `IsValid`

```text
IsValid(InAssetData: FAssetData &) -> bool
```

Checks to see if this AssetData refers to an asset or is NULL

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsUAsset`

```text
IsUAsset(InAssetData: FAssetData &) -> bool
```

Returns true if this asset was found in a UAsset file

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsRedirector`

```text
IsRedirector(InAssetData: FAssetData &) -> bool
```

Returns true if the this asset is a redirector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetFullName`

```text
GetFullName(InAssetData: FAssetData &) -> FString
```

Returns the full name for the asset in the form: Class ObjectPath

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `ToSoftObjectPath`

```text
ToSoftObjectPath(InAssetData: FAssetData &) -> FSoftObjectPath
```

Convert to a SoftObjectPath for loading

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `FSoftObjectPath` | - |

### `GetClass`

```text
GetClass(InAssetData: FAssetData &) -> UClass *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetAsset`

```text
GetAsset(InAssetData: FAssetData &) -> UObject *
```

Returns the asset UObject if it is loaded or loads the asset if it is unloaded then returns the result

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `IsAssetLoaded`

```text
IsAssetLoaded(InAssetData: FAssetData &) -> bool
```

Returns true if the asset is loaded

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetExportTextName`

```text
GetExportTextName(InAssetData: FAssetData &) -> FString
```

Returns the name for the asset in the form: Class'ObjectPath'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetTagValue < FName >`

```text
GetTagValue < FName >(InAssetData: FAssetData &, InTagName: FName &, OutTagValue: FString &) -> bool
```

Gets the value associated with the given tag as a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAssetData` | `FAssetData &` | - |
| `InTagName` | `FName &` | - |
| `OutTagValue` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetFilterTagsAndValues`

```text
SetFilterTagsAndValues(InFilter: FARFilter &, InTagsAndValues: TArray < FTagAndValue > &) -> FARFilter
```

Populates the FARFilters tags and values map with the passed in tags and values

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFilter` | `FARFilter &` | - |
| `InTagsAndValues` | `TArray < FTagAndValue > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FARFilter` | - |

## Language

`cpp`
