---
id: "api:class:UKismetArrayLibrary"
title: "UKismetArrayLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetArrayLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetArrayLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Array_Add`

```text
Array_Add(TargetArray: TArray < int32 > &, NewItem: int32 &) -> int32
```

Add item to array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to add item to |
| `NewItem` | `int32 &` | The item to add to the array |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the newly added item |

### `Array_AddUnique`

```text
Array_AddUnique(TargetArray: TArray < int32 > &, NewItem: int32 &) -> int32
```

Add item to array (unique)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to add item to |
| `NewItem` | `int32 &` | The item to add to the array |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the newly added item, or INDEX_NONE if the item is already present in the array |

### `Array_Shuffle`

```text
Array_Shuffle(TargetArray: TArray < int32 > &) -> void
```

Shuffle (randomize) the elements of an array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to shuffle |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Append`

```text
Array_Append(TargetArray: TArray < int32 > &, SourceArray: TArray < int32 > &) -> void
```

Append an array to another array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to add the source array to |
| `SourceArray` | `TArray < int32 > &` | The array to add to the target array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Insert`

```text
Array_Insert(TargetArray: TArray < int32 > &, NewItem: int32 &, Index: int32) -> void
```

Insert item at the given index into the array.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to insert into |
| `NewItem` | `int32 &` | The item to insert into the array |
| `Index` | `int32` | The index at which to insert the item into the array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Remove`

```text
Array_Remove(TargetArray: TArray < int32 > &, IndexToRemove: int32) -> void
```

Remove item at the given index from the array.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to remove from |
| `IndexToRemove` | `int32` | The index into the array to remove from |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_RemoveItem`

```text
Array_RemoveItem(TargetArray: TArray < int32 > &, Item: int32 &) -> bool
```

Remove all instances of item from array.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to remove from |
| `Item` | `int32 &` | The item to remove from the array |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if one or more items were removed |

### `Array_Clear`

```text
Array_Clear(TargetArray: TArray < int32 > &) -> void
```

Clear an array, removes all content

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to clear |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Resize`

```text
Array_Resize(TargetArray: TArray < int32 > &, Size: int32) -> void
```

Resize Array to specified size.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to resize |
| `Size` | `int32` | The new size of the array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Length`

```text
Array_Length(TargetArray: TArray < int32 > &) -> int32
```

Get the number of items in an array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to get the length of |

**Returns**

| Type | Description |
|---|---|
| `int32` | The length of the array |

### `Array_LastIndex`

```text
Array_LastIndex(TargetArray: TArray < int32 > &) -> int32
```

Get the last valid index into an array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to perform the operation on |

**Returns**

| Type | Description |
|---|---|
| `int32` | The last valid index of the array |

### `Array_Get`

```text
Array_Get(TargetArray: TArray < int32 > &, Index: int32, Item: int32 &) -> void
```

Given an array and an index, returns a copy of the item found at that index

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to get an item from |
| `Index` | `int32` | The index in the array to get an item from |
| `Item` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | A copy of the item stored at the index |

### `Array_Set`

```text
Array_Set(TargetArray: TArray < int32 > &, Index: int32, Item: int32 &, bSizeToFit: bool) -> void
```

Given an array and an index, assigns the item to that array element

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to perform the operation on |
| `Index` | `int32` | The index to assign the item to |
| `Item` | `int32 &` | The item to assign to the index of the array |
| `bSizeToFit` | `bool` | If true, the array will expand if Index is greater than the current size of the array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Swap`

```text
Array_Swap(TargetArray: TArray < int32 > &, FirstIndex: int32, SecondIndex: int32) -> void
```

Swaps the elements at the specified positions in the specified array
	 If the specified positions are equal, invoking this method leaves the array unchanged

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to perform the operation on |
| `FirstIndex` | `int32` | - |
| `SecondIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_Find`

```text
Array_Find(TargetArray: TArray < int32 > &, ItemToFind: int32 &) -> int32
```

Finds the index of the first instance of the item within the array

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to search for the item |
| `ItemToFind` | `int32 &` | The item to look for |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index the item was found at, or -1 if not found |

### `Array_Contains`

```text
Array_Contains(TargetArray: TArray < int32 > &, ItemToFind: int32 &) -> bool
```

Returns true if the array contains the given item

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | The array to search for the item |
| `ItemToFind` | `int32 &` | The item to look for |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the item was found within the array |

### `FilterArray`

```text
FilterArray(TargetArray: TArray < AActor * > &, FilterClass: TSubclassOf < AActor >, FilteredArray: TArray < AActor * > &) -> void
```

Filter an array based on a Class derived from Actor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < AActor * > &` | The array to filter from |
| `FilterClass` | `TSubclassOf < AActor >` | The Actor sub-class type that acts as the filter, only objects derived from it will be returned. |
| `FilteredArray` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | An array containing only those objects which are derived from the class specified. |

### `SetArrayPropertyByName`

```text
SetArrayPropertyByName(Object: UObject *, PropertyName: FName, Value: TArray < int32 > &) -> void
```

Not exposed to users. Supports setting an array property on an object by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Array_IsValidIndex`

```text
Array_IsValidIndex(TargetArray: TArray < int32 > &, IndexToTest: int32) -> bool
```

Tests if IndexToTest is valid, i.e. greater than or equal to zero, and less than the number of elements in TargetArray.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetArray` | `TArray < int32 > &` | Array to use for the IsValidIndex test |
| `IndexToTest` | `int32` | The Index, that we want to test for being valid |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the Index is Valid, i.e. greater than or equal to zero, and less than the number of elements in TargetArray. |

## Language

`cpp`
