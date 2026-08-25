---
id: "api:class:UKismetNodeHelperLibrary"
title: "UKismetNodeHelperLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetNodeHelperLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UKismetNodeHelperLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `BitIsMarked`

```text
BitIsMarked(Data: int32, Index: int32) -> bool
```

Returns whether the bit at index "Index" is set or not in the data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32` | - The integer containing the bits that are being tested against |
| `Index` | `int32` | - The bit index into the Data that we are inquiring |

**Returns**

| Type | Description |
|---|---|
| `bool` | - Whether the bit at index "Index" is set or not |

### `MarkBit`

```text
MarkBit(Data: int32 &, Index: int32) -> void
```

Sets the bit at index "Index" in the data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32 &` | - The integer containing the bits that are being set |
| `Index` | `int32` | - The bit index into the Data that we are setting |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearBit`

```text
ClearBit(Data: int32 &, Index: int32) -> void
```

Clears the bit at index "Index" in the data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32 &` | - The integer containing the bits that are being cleared |
| `Index` | `int32` | - The bit index into the Data that we are clearing |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearAllBits`

```text
ClearAllBits(Data: int32 &) -> void
```

Clears all of the bit in the data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32 &` | - The integer containing the bits that are being cleared |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HasUnmarkedBit`

```text
HasUnmarkedBit(Data: int32, NumBits: int32) -> bool
```

Returns whether there exists an unmarked bit in the data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32` | - The data being tested against |
| `NumBits` | `int32` | - The logical number of bits we want to track |

**Returns**

| Type | Description |
|---|---|
| `bool` | - Whether there is a bit not marked in the data |

### `HasMarkedBit`

```text
HasMarkedBit(Data: int32, NumBits: int32) -> bool
```

Returns whether there exists a marked bit in the data

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32` | - The data being tested against |
| `NumBits` | `int32` | - The logical number of bits we want to track |

**Returns**

| Type | Description |
|---|---|
| `bool` | - Whether there is a bit marked in the data |

### `GetUnmarkedBit`

```text
GetUnmarkedBit(Data: int32, StartIdx: int32, NumBits: int32, bRandom: bool) -> int32
```

Gets an already unmarked bit and returns the bit index selected

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32` | - The integer containing the bits that are being set |
| `StartIdx` | `int32` | - The index to start with when determining the selection' |
| `NumBits` | `int32` | - The logical number of bits we want to track |
| `bRandom` | `bool` | - Whether to select a random index or not |

**Returns**

| Type | Description |
|---|---|
| `int32` | - The index that was selected (returns INDEX_NONE if there was no unmarked bits to choose from) |

### `GetRandomUnmarkedBit`

```text
GetRandomUnmarkedBit(Data: int32, StartIdx: int32, NumBits: int32) -> int32
```

Gets a random not already marked bit and returns the bit index selected

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32` | - The integer containing the bits that are being set |
| `StartIdx` | `int32` | - |
| `NumBits` | `int32` | - The logical number of bits we want to track |

**Returns**

| Type | Description |
|---|---|
| `int32` | - The index that was selected (returns INDEX_NONE if there was no unmarked bits to choose from) |

### `GetFirstUnmarkedBit`

```text
GetFirstUnmarkedBit(Data: int32, StartIdx: int32, NumBits: int32) -> int32
```

Gets the first index not already marked starting from a specific index and returns the bit index selected

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Data` | `int32` | - The integer containing the bits that are being set |
| `StartIdx` | `int32` | - The index to start looking for an available index from |
| `NumBits` | `int32` | - The logical number of bits we want to track |

**Returns**

| Type | Description |
|---|---|
| `int32` | - The index that was selected (returns INDEX_NONE if there was no unmarked bits to choose from) |

### `GetEnumeratorName`

```text
GetEnumeratorName(Enum: UEnum *, EnumeratorValue: uint8) -> FName
```

Gets enumerator name.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - Enumeration |
| `EnumeratorValue` | `uint8` | - Value of searched enumeration |

**Returns**

| Type | Description |
|---|---|
| `FName` | - name of the searched enumerator, or NAME_None |

### `GetEnumeratorUserFriendlyName`

```text
GetEnumeratorUserFriendlyName(Enum: UEnum *, EnumeratorValue: uint8) -> FString
```

Gets enumerator name as FString. Use DeisplayName when possible.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - Enumeration |
| `EnumeratorValue` | `uint8` | - Value of searched enumeration |

**Returns**

| Type | Description |
|---|---|
| `FString` | - name of the searched enumerator, or NAME_None |

### `GetValidValue`

```text
GetValidValue(Enum: UEnum *, EnumeratorValue: uint8) -> uint8
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - Enumeration |
| `EnumeratorValue` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - if EnumeratorIndex is valid return EnumeratorIndex, otherwise return MAX value of Enum |

### `GetEnumeratorValueFromIndex`

```text
GetEnumeratorValueFromIndex(Enum: UEnum *, EnumeratorIndex: uint8) -> uint8
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - Enumeration |
| `EnumeratorIndex` | `uint8` | - Input index |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - The value of the enumerator, or INDEX_NONE |

## Language

`cpp`
