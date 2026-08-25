---
id: "api:class:UBlueprintSetLibrary"
title: "UBlueprintSetLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBlueprintSetLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBlueprintSetLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Set_Add`

```text
Set_Add(TargetSet: TSet < int32 > &, NewItem: int32 &) -> void
```

Adds item to set. Output value indicates whether the item was successfully added, meaning an 
	  output of False indicates the item was already in the Set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to add item to |
| `NewItem` | `int32 &` | The item to add to the set |

**Returns**

| Type | Description |
|---|---|
| `void` | True if NewItem was added to the set (False indicates an equivalent item was present) |

### `Set_AddItems`

```text
Set_AddItems(TargetSet: TSet < int32 > &, NewItems: TArray < int32 > &) -> void
```

Adds all elements from an Array to a Set

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to search for the item |
| `NewItems` | `TArray < int32 > &` | The items to add to the set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Remove`

```text
Set_Remove(TargetSet: TSet < int32 > &, Item: int32 &) -> bool
```

Remove item from set. Output value indicates if something was actually removed. False
	  indicates no equivalent item was found.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to remove from |
| `Item` | `int32 &` | The item to remove from the set |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if an item was removed (False indicates no equivalent item was present) |

### `Set_RemoveItems`

```text
Set_RemoveItems(TargetSet: TSet < int32 > &, Items: TArray < int32 > &) -> void
```

Removes all elements in an Array from a set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to remove from |
| `Items` | `TArray < int32 > &` | The items to remove from the set |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_ToArray`

```text
Set_ToArray(A: TSet < int32 > &, Result: TArray < int32 > &) -> void
```

Outputs an Array containing copies of the entries of a Set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | Set |
| `Result` | `TArray < int32 > &` | Array |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Clear`

```text
Set_Clear(TargetSet: TSet < int32 > &) -> void
```

Clear a set, removes all content.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to clear |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Length`

```text
Set_Length(TargetSet: TSet < int32 > &) -> int32
```

Get the number of items in a set.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to get the length of |

**Returns**

| Type | Description |
|---|---|
| `int32` | The length of the set |

### `Set_Contains`

```text
Set_Contains(TargetSet: TSet < int32 > &, ItemToFind: int32 &) -> bool
```

Returns true if the set contains the given item.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetSet` | `TSet < int32 > &` | The set to search for the item |
| `ItemToFind` | `int32 &` | The item to look for |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the item was found within the set |

### `Set_Intersection`

```text
Set_Intersection(A: TSet < int32 > &, B: TSet < int32 > &, Result: TSet < int32 > &) -> void
```

Assigns Result to the intersection of Set A and Set B. That is, Result will contain
	  all elements that are in both Set A and Set B. To intersect with the empty set use
	  Clear.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | One set to intersect |
| `B` | `TSet < int32 > &` | Another set to intersect |
| `Result` | `TSet < int32 > &` | Set to store results in |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Union`

```text
Set_Union(A: TSet < int32 > &, B: TSet < int32 > &, Result: TSet < int32 > &) -> void
```

Assigns Result to the union of two sets, A and B. That is, Result will contain
	  all elements that are in Set A and in addition all elements in Set B. Note that 
	  a Set is a collection of unique elements, so duplicates will be eliminated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | One set to union |
| `B` | `TSet < int32 > &` | Another set to union |
| `Result` | `TSet < int32 > &` | Set to store results in |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Set_Difference`

```text
Set_Difference(A: TSet < int32 > &, B: TSet < int32 > &, Result: TSet < int32 > &) -> void
```

Assigns Result to the relative difference of two sets, A and B. That is, Result will 
	  contain  all elements that are in Set A but are not found in Set B. Note that the 
	  difference between two sets  is not commutative. The Set whose elements you wish to 
	  preserve should be the first (top) parameter. Also called the relative complement.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `TSet < int32 > &` | Starting set |
| `B` | `TSet < int32 > &` | Set of elements to remove from set A |
| `Result` | `TSet < int32 > &` | Set containing all elements in A that are not found in B |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSetPropertyByName`

```text
SetSetPropertyByName(Object: UObject *, PropertyName: FName, Value: TSet < int32 > &) -> void
```

Not exposed to users. Supports setting a set property on an object by name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Object` | `UObject *` | - |
| `PropertyName` | `FName` | - |
| `Value` | `TSet < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
