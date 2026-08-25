---
id: "api:class:UBlueprintMapLibrary"
title: "UBlueprintMapLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBlueprintMapLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBlueprintMapLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Map_Add`

```text
Map_Add(TargetMap: TMap < int32 , int32 > &, Key: int32 &, Value: int32 &) -> void
```

Adds a key and value to the map. If something already uses the provided key it will be overwritten with the new value.
	  After calling Key is guaranteed to be associated with Value until a subsequent mutation of the Map.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to add the key and value to |
| `Key` | `int32 &` | The key that will be used to look the value up |
| `Value` | `int32 &` | The value to be retrieved later |

**Returns**

| Type | Description |
|---|---|
| `void` | True if a Value was added, or False if the Key was already present and has been overwritten |

### `Map_Remove`

```text
Map_Remove(TargetMap: TMap < int32 , int32 > &, Key: int32 &) -> bool
```

Removes a key and its associated value from the map.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to remove the key and its associated value from |
| `Key` | `int32 &` | The key that will be used to look the value up |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was removed (False indicates nothing in the map uses the provided key) |

### `Map_Find`

```text
Map_Find(TargetMap: TMap < int32 , int32 > &, Key: int32 &, Value: int32 &) -> bool
```

Finds the value associated with the provided Key

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to perform the lookup on |
| `Key` | `int32 &` | The key that will be used to look the value up |
| `Value` | `int32 &` | The value associated with the key, default constructed if key was not found |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was found (False indicates nothing in the map uses the provided key) |

### `Map_Contains`

```text
Map_Contains(TargetMap: TMap < int32 , int32 > &, Key: int32 &) -> bool
```

Checks whether key is in a provided Map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to perform the lookup on |
| `Key` | `int32 &` | The key that will be used to lookup |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was found (False indicates nothing in the map uses the provided key) |

### `Map_Keys`

```text
Map_Keys(TargetMap: TMap < int32 , int32 > &, Keys: TArray < int32 > &) -> void
```

Outputs an array of all keys present in the map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to get the list of keys from |
| `Keys` | `TArray < int32 > &` | All keys present in the map |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Map_Values`

```text
Map_Values(TargetMap: TMap < int32 , int32 > &, Values: TArray < int32 > &) -> void
```

Outputs an array of all values present in the map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to get the list of values from |
| `Values` | `TArray < int32 > &` | All values present in the map |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Map_Length`

```text
Map_Length(TargetMap: TMap < int32 , int32 > &) -> int32
```

Determines the number of entries in a provided Map

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map in question |

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of entries in the map |

### `Map_Clear`

```text
Map_Clear(TargetMap: TMap < int32 , int32 > &) -> void
```

Clears a map of all entries, resetting it to empty

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetMap` | `TMap < int32 , int32 > &` | The map to clear |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMapPropertyByName`

```text
SetMapPropertyByName(Object: UObject *, PropertyName: FName, Value: TMap < int32 , int32 > &) -> void
```

Not exposed to users. Supports setting a map property on an object by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TMap < int32 , int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
