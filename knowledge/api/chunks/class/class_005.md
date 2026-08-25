---
id: "api-chunk:class:5"
title: "Oasis API class chunk 5"
source: "https://developer.gp.qq.com/api/"
category: "API Wiki/class"
kind: "api_chunk"
---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetMathLibrary.json -->

# UKismetMathLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `RandomBool`

```text
RandomBool() -> bool
```

Returns a uniformly distributed random bool

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RandomBoolWithWeight`

```text
RandomBoolWithWeight(Weight: float) -> bool
```

Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
	 		Weight = .6 return value = True 60% of the time

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weight` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RandomBoolWithWeightFromStream`

```text
RandomBoolWithWeightFromStream(Weight: float, RandomStream: FRandomStream &) -> bool
```

Get a random chance with the specified weight. Range of weight is 0.0 - 1.0 E.g.,
			Weight = .6 return value = True 60% of the time

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weight` | `float` | - |
| `RandomStream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Not_PreBool`

```text
Not_PreBool(A: bool) -> bool
```

Returns the logical complement of the Boolean value (NOT A)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_BoolBool`

```text
EqualEqual_BoolBool(A: bool, B: bool) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |
| `B` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_BoolBool`

```text
NotEqual_BoolBool(A: bool, B: bool) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |
| `B` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BooleanAND`

```text
BooleanAND(A: bool, B: bool) -> bool
```

Returns the logical AND of two values (A AND B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |
| `B` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BooleanNAND`

```text
BooleanNAND(A: bool, B: bool) -> bool
```

Returns the logical NAND of two values (A AND B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |
| `B` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BooleanOR`

```text
BooleanOR(A: bool, B: bool) -> bool
```

Returns the logical OR of two values (A OR B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |
| `B` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BooleanXOR`

```text
BooleanXOR(A: bool, B: bool) -> bool
```

Returns the logical eXclusive OR of two values (A XOR B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |
| `B` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `BooleanNOR`

```text
BooleanNOR(A: bool, B: bool) -> bool
```

Returns the logical Not OR of two values (A NOR B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `bool` | - |
| `B` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Multiply_ByteByte`

```text
Multiply_ByteByte(A: uint8, B: uint8) -> uint8
```

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "Byte  Byte", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Byte")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `Divide_ByteByte`

```text
Divide_ByteByte(A: uint8, B: uint8) -> uint8
```

Division (A  B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `Percent_ByteByte`

```text
Percent_ByteByte(A: uint8, B: uint8) -> uint8
```

Modulo (A % B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `Add_ByteByte`

```text
Add_ByteByte(A: uint8, B: uint8) -> uint8
```

Addition (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `Subtract_ByteByte`

```text
Subtract_ByteByte(A: uint8, B: uint8) -> uint8
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `BMin`

```text
BMin(A: uint8, B: uint8) -> uint8
```

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `BMax`

```text
BMax(A: uint8, B: uint8) -> uint8
```

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `Less_ByteByte`

```text
Less_ByteByte(A: uint8, B: uint8) -> bool
```

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Greater_ByteByte`

```text
Greater_ByteByte(A: uint8, B: uint8) -> bool
```

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LessEqual_ByteByte`

```text
LessEqual_ByteByte(A: uint8, B: uint8) -> bool
```

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GreaterEqual_ByteByte`

```text
GreaterEqual_ByteByte(A: uint8, B: uint8) -> bool
```

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_ByteByte`

```text
EqualEqual_ByteByte(A: uint8, B: uint8) -> bool
```

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_ByteByte`

```text
NotEqual_ByteByte(A: uint8, B: uint8) -> bool
```

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint8` | - |
| `B` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Multiply_IntInt`

```text
Multiply_IntInt(A: int32, B: int32) -> int32
```

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "integer  integer", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Integer")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Divide_IntInt`

```text
Divide_IntInt(A: int32, B: int32) -> int32
```

Division (A  B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Percent_IntInt`

```text
Percent_IntInt(A: int32, B: int32) -> int32
```

Modulo (A % B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Add_IntInt`

```text
Add_IntInt(A: int32, B: int32) -> int32
```

Addition (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Subtract_IntInt`

```text
Subtract_IntInt(A: int32, B: int32) -> int32
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Less_IntInt`

```text
Less_IntInt(A: int32, B: int32) -> bool
```

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Greater_IntInt`

```text
Greater_IntInt(A: int32, B: int32) -> bool
```

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LessEqual_IntInt`

```text
LessEqual_IntInt(A: int32, B: int32) -> bool
```

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GreaterEqual_IntInt`

```text
GreaterEqual_IntInt(A: int32, B: int32) -> bool
```

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_IntInt`

```text
EqualEqual_IntInt(A: int32, B: int32) -> bool
```

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_IntInt`

```text
NotEqual_IntInt(A: int32, B: int32) -> bool
```

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `InRange_IntInt`

```text
InRange_IntInt(Value: int32, Min: int32, Max: int32, InclusiveMin: bool, InclusiveMax: bool) -> bool
```

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |
| `Min` | `int32` | - |
| `Max` | `int32` | - |
| `InclusiveMin` | `bool` | - |
| `InclusiveMax` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `And_IntInt`

```text
And_IntInt(A: int32, B: int32) -> int32
```

Bitwise AND (A & B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Xor_IntInt`

```text
Xor_IntInt(A: int32, B: int32) -> int32
```

Bitwise XOR (A ^ B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Or_IntInt`

```text
Or_IntInt(A: int32, B: int32) -> int32
```

Bitwise OR (A | B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Not_Int`

```text
Not_Int(A: int32) -> int32
```

Bitwise NOT (~A)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `LeftShift_Int`

```text
LeftShift_Int(A: int32, N: int32) -> int32
```

Bitwise LeftShift (A << N)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `N` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RightShift_Int`

```text
RightShift_Int(A: int32, N: int32) -> int32
```

Bitwise RightShift (A >> N)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `N` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `LeftShift_Int64`

```text
LeftShift_Int64(A: int64, N: int32) -> int64
```

Bitwise LeftShift (A << N)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `N` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `RightShift_Int64`

```text
RightShift_Int64(A: int64, N: int32) -> int64
```

Bitwise RightShift (A >> N)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `N` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `SignOfInteger`

```text
SignOfInteger(A: int32) -> int32
```

Sign (integer, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RandomInteger`

```text
RandomInteger(A: int32) -> int32
```

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RandomIntegerInRange`

```text
RandomIntegerInRange(Min: int32, Max: int32) -> int32
```

Return a random integer between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `int32` | - |
| `Max` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Min`

```text
Min(A: int32, B: int32) -> int32
```

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Max`

```text
Max(A: int32, B: int32) -> int32
```

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Clamp`

```text
Clamp(V: int32, A: int32, B: int32) -> int32
```

Returns Value clamped to be between A and B (inclusive)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `int32` | - |
| `A` | `int32` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Abs_Int`

```text
Abs_Int(A: int32) -> int32
```

Returns the absolute (positive) value of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Multiply_Int64Int64`

```text
Multiply_Int64Int64(A: int64, B: int64) -> int64
```

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "integer64  integer64", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Integer64")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Divide_Int64Int64`

```text
Divide_Int64Int64(A: int64, B: int64) -> int64
```

Division (A  B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Add_Int64Int64`

```text
Add_Int64Int64(A: int64, B: int64) -> int64
```

Addition (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Subtract_Int64Int64`

```text
Subtract_Int64Int64(A: int64, B: int64) -> int64
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Less_Int64Int64`

```text
Less_Int64Int64(A: int64, B: int64) -> bool
```

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Greater_Int64Int64`

```text
Greater_Int64Int64(A: int64, B: int64) -> bool
```

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LessEqual_Int64Int64`

```text
LessEqual_Int64Int64(A: int64, B: int64) -> bool
```

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GreaterEqual_Int64Int64`

```text
GreaterEqual_Int64Int64(A: int64, B: int64) -> bool
```

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_Int64Int64`

```text
EqualEqual_Int64Int64(A: int64, B: int64) -> bool
```

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_Int64Int64`

```text
NotEqual_Int64Int64(A: int64, B: int64) -> bool
```

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `InRange_Int64Int64`

```text
InRange_Int64Int64(Value: int64, Min: int64, Max: int64, InclusiveMin: bool, InclusiveMax: bool) -> bool
```

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int64` | - |
| `Min` | `int64` | - |
| `Max` | `int64` | - |
| `InclusiveMin` | `bool` | - |
| `InclusiveMax` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `And_Int64Int64`

```text
And_Int64Int64(A: int64, B: int64) -> int64
```

Bitwise AND (A & B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Xor_Int64Int64`

```text
Xor_Int64Int64(A: int64, B: int64) -> int64
```

Bitwise XOR (A ^ B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Or_Int64Int64`

```text
Or_Int64Int64(A: int64, B: int64) -> int64
```

Bitwise OR (A | B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Not_Int64`

```text
Not_Int64(A: int64) -> int64
```

Bitwise NOT (~A)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `SignOfInteger64`

```text
SignOfInteger64(A: int64) -> int64
```

Sign (integer64, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `RandomInteger64`

```text
RandomInteger64(A: int64) -> int64
```

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `RandomInteger64InRange`

```text
RandomInteger64InRange(Min: int64, Max: int64) -> int64
```

Return a random integer64 between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `int64` | - |
| `Max` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `MinInt64`

```text
MinInt64(A: int64, B: int64) -> int64
```

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `MaxInt64`

```text
MaxInt64(A: int64, B: int64) -> int64
```

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `ClampInt64`

```text
ClampInt64(V: int64, A: int64, B: int64) -> int64
```

Returns Value clamped to be between A and B (inclusive)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `int64` | - |
| `A` | `int64` | - |
| `B` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Abs_Int64`

```text
Abs_Int64(A: int64) -> int64
```

Returns the absolute (positive) value of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Multiply_UInt64UInt64`

```text
Multiply_UInt64UInt64(A: uint64, B: uint64) -> uint64
```

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta = (DisplayName = "uinteger64  uinteger64", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category = "Math|Integer64")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `Divide_UInt64UInt64`

```text
Divide_UInt64UInt64(A: uint64, B: uint64) -> uint64
```

Division (A  B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `Add_UInt64UInt64`

```text
Add_UInt64UInt64(A: uint64, B: uint64) -> uint64
```

Addition (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `Subtract_UInt64UInt64`

```text
Subtract_UInt64UInt64(A: uint64, B: uint64) -> uint64
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `Less_UInt64UInt64`

```text
Less_UInt64UInt64(A: uint64, B: uint64) -> bool
```

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Greater_UInt64UInt64`

```text
Greater_UInt64UInt64(A: uint64, B: uint64) -> bool
```

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LessEqual_UInt64UInt64`

```text
LessEqual_UInt64UInt64(A: uint64, B: uint64) -> bool
```

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GreaterEqual_UInt64UInt64`

```text
GreaterEqual_UInt64UInt64(A: uint64, B: uint64) -> bool
```

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_UInt64UInt64`

```text
EqualEqual_UInt64UInt64(A: uint64, B: uint64) -> bool
```

Returns true if A is equal to B (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_UInt64UInt64`

```text
NotEqual_UInt64UInt64(A: uint64, B: uint64) -> bool
```

Returns true if A is not equal to B (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `InRange_UInt64UInt64`

```text
InRange_UInt64UInt64(Value: uint64, Min: uint64, Max: uint64, InclusiveMin: bool, InclusiveMax: bool) -> bool
```

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `uint64` | - |
| `Min` | `uint64` | - |
| `Max` | `uint64` | - |
| `InclusiveMin` | `bool` | - |
| `InclusiveMax` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `And_UInt64UInt64`

```text
And_UInt64UInt64(A: uint64, B: uint64) -> uint64
```

Bitwise AND (A & B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `Xor_UInt64UInt64`

```text
Xor_UInt64UInt64(A: uint64, B: uint64) -> uint64
```

Bitwise XOR (A ^ B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `Or_UInt64UInt64`

```text
Or_UInt64UInt64(A: uint64, B: uint64) -> uint64
```

Bitwise OR (A | B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `Not_UInt64`

```text
Not_UInt64(A: uint64) -> uint64
```

Bitwise NOT (~A)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `RandomUInteger64`

```text
RandomUInteger64(A: uint64) -> uint64
```

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `RandomUInteger64InRange`

```text
RandomUInteger64InRange(Min: uint64, Max: uint64) -> uint64
```

Return a random integer64 between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `uint64` | - |
| `Max` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `MinUInt64`

```text
MinUInt64(A: uint64, B: uint64) -> uint64
```

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `MaxUInt64`

```text
MaxUInt64(A: uint64, B: uint64) -> uint64
```

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `ClampUInt64`

```text
ClampUInt64(V: uint64, A: uint64, B: uint64) -> uint64
```

Returns Value clamped to be between A and B (inclusive)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `uint64` | - |
| `A` | `uint64` | - |
| `B` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `uint64` | - |

### `MultiplyMultiply_FloatFloat`

```text
MultiplyMultiply_FloatFloat(Base: float, Exp: float) -> float
```

Power (Base to the Exp-th power)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Base` | `float` | - |
| `Exp` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Multiply_FloatFloat`

```text
Multiply_FloatFloat(A: float, B: float) -> float
```

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "float  float", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Float")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Multiply_IntFloat`

```text
Multiply_IntFloat(A: int32, B: float) -> float
```

Multiplication (A  B) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "int  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Float")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Divide_FloatFloat`

```text
Divide_FloatFloat(A: float, B: float) -> float
```

Division (A  B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Percent_FloatFloat`

```text
Percent_FloatFloat(A: float, B: float) -> float
```

Modulo (A % B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Fraction`

```text
Fraction(A: float) -> float
```

Returns the fractional part of a float.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Add_FloatFloat`

```text
Add_FloatFloat(A: float, B: float) -> float
```

Addition (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Subtract_FloatFloat`

```text
Subtract_FloatFloat(A: float, B: float) -> float
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Less_FloatFloat`

```text
Less_FloatFloat(A: float, B: float) -> bool
```

Returns true if A is Less than B (A < B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Greater_FloatFloat`

```text
Greater_FloatFloat(A: float, B: float) -> bool
```

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LessEqual_FloatFloat`

```text
LessEqual_FloatFloat(A: float, B: float) -> bool
```

Returns true if A is Less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GreaterEqual_FloatFloat`

```text
GreaterEqual_FloatFloat(A: float, B: float) -> bool
```

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_FloatFloat`

```text
EqualEqual_FloatFloat(A: float, B: float) -> bool
```

Returns true if A is exactly equal to B (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NearlyEqual_FloatFloat`

```text
NearlyEqual_FloatFloat(A: float, B: float, ErrorTolerance: float) -> bool
```

Returns true if A is nearly equal to B (|A - B| < ErrorTolerance)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |
| `ErrorTolerance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_FloatFloat`

```text
NotEqual_FloatFloat(A: float, B: float) -> bool
```

Returns true if A does not equal B (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `InRange_FloatFloat`

```text
InRange_FloatFloat(Value: float, Min: float, Max: float, InclusiveMin: bool, InclusiveMax: bool) -> bool
```

Returns true if value is between Min and Max (V >= Min && V <= Max)
	  If InclusiveMin is true, value needs to be equal or larger than Min, else it needs to be larger
	  If InclusiveMax is true, value needs to be smaller or equal than Max, else it needs to be smaller

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `Min` | `float` | - |
| `Max` | `float` | - |
| `InclusiveMin` | `bool` | - |
| `InclusiveMax` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Hypotenuse`

```text
Hypotenuse(Width: float, Height: float) -> float
```

Returns the hypotenuse of a right-angled triangle given the width and height.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Width` | `float` | - |
| `Height` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GridSnap_Float`

```text
GridSnap_Float(Location: float, GridSize: float) -> float
```

Snaps a value to the nearest grid multiple. E.g.,
	 		Location = 5.1, GridSize = 10.0 : return value = 10.0
	  If GridSize is 0 Location is returned
	  if GridSize is very small precision issues may occur.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `float` | - |
| `GridSize` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Abs`

```text
Abs(A: float) -> float
```

Returns the absolute (positive) value of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Sin`

```text
Sin(A: float) -> float
```

Returns the sine of A (expects Radians)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Asin`

```text
Asin(A: float) -> float
```

Returns the inverse sine (arcsin) of A (result is in Radians)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Cos`

```text
Cos(A: float) -> float
```

Returns the cosine of A (expects Radians)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Acos`

```text
Acos(A: float) -> float
```

Returns the inverse cosine (arccos) of A (result is in Radians)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Tan`

```text
Tan(A: float) -> float
```

Returns the tan of A (expects Radians)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Atan`

```text
Atan(A: float) -> float
```

Returns the inverse tan (atan) (result is in Radians)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Atan2`

```text
Atan2(A: float, B: float) -> float
```

Returns the inverse tan (atan2) of AB (result is in Radians)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Exp`

```text
Exp(A: float) -> float
```

Returns exponential(e) to the power A (e^A)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Log`

```text
Log(A: float, Base: float) -> float
```

Returns log of A base B (if B^R == A, returns R)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `Base` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Loge`

```text
Loge(A: float) -> float
```

Returns natural log of A (if e^R == A, returns R)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Sqrt`

```text
Sqrt(A: float) -> float
```

Returns square root of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Square`

```text
Square(A: float) -> float
```

Returns square of A (AA)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `RandomFloat`

```text
RandomFloat() -> float
```

Returns a random float between 0 and 1

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `RandomFloatInRange`

```text
RandomFloatInRange(Min: float, Max: float) -> float
```

Generate a random number between Min and Max

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `float` | - |
| `Max` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPI`

```text
GetPI() -> float
```

Returns the value of PI

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTAU`

```text
GetTAU() -> float
```

Returns the value of TAU (= 2  PI)

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegreesToRadians`

```text
DegreesToRadians(A: float) -> float
```

Returns radians value based on the input degrees

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `RadiansToDegrees`

```text
RadiansToDegrees(A: float) -> float
```

Returns degrees value based on the input radians

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegSin`

```text
DegSin(A: float) -> float
```

Returns the sin of A (expects Degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegAsin`

```text
DegAsin(A: float) -> float
```

Returns the inverse sin (arcsin) of A (result is in Degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegCos`

```text
DegCos(A: float) -> float
```

Returns the cos of A (expects Degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegAcos`

```text
DegAcos(A: float) -> float
```

Returns the inverse cos (arccos) of A (result is in Degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegTan`

```text
DegTan(A: float) -> float
```

Returns the tan of A (expects Degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegAtan`

```text
DegAtan(A: float) -> float
```

Returns the inverse tan (atan) (result is in Degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `DegAtan2`

```text
DegAtan2(A: float, B: float) -> float
```

Returns the inverse tan (atan2) of AB (result is in Degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `ClampAngle`

```text
ClampAngle(AngleDegrees: float, MinAngleDegrees: float, MaxAngleDegrees: float) -> float
```

Clamps an arbitrary angle to be between the given angles.  Will clamp to nearest boundary.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AngleDegrees` | `float` | - |
| `MinAngleDegrees` | `float` | "from" angle that defines the beginning of the range of valid angles (sweeping clockwise) |
| `MaxAngleDegrees` | `float` | "to" angle that defines the end of the range of valid angles |

**Returns**

| Type | Description |
|---|---|
| `float` | Returns clamped angle in the range -180..180. |

### `FMin`

```text
FMin(A: float, B: float) -> float
```

Returns the minimum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FMax`

```text
FMax(A: float, B: float) -> float
```

Returns the maximum value of A and B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FClamp`

```text
FClamp(V: float, A: float, B: float) -> float
```

Returns Value clamped between A and B (inclusive)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `float` | - |
| `A` | `float` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `MaxOfIntArray`

```text
MaxOfIntArray(IntArray: TArray < int32 > &, IndexOfMaxValue: int32 &, MaxValue: int32 &) -> void
```

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IntArray` | `TArray < int32 > &` | - |
| `IndexOfMaxValue` | `int32 &` | - |
| `MaxValue` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MinOfIntArray`

```text
MinOfIntArray(IntArray: TArray < int32 > &, IndexOfMinValue: int32 &, MinValue: int32 &) -> void
```

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IntArray` | `TArray < int32 > &` | - |
| `IndexOfMinValue` | `int32 &` | - |
| `MinValue` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MaxOfFloatArray`

```text
MaxOfFloatArray(FloatArray: TArray < float > &, IndexOfMaxValue: int32 &, MaxValue: float &) -> void
```

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FloatArray` | `TArray < float > &` | - |
| `IndexOfMaxValue` | `int32 &` | - |
| `MaxValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MinOfFloatArray`

```text
MinOfFloatArray(FloatArray: TArray < float > &, IndexOfMinValue: int32 &, MinValue: float &) -> void
```

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FloatArray` | `TArray < float > &` | - |
| `IndexOfMinValue` | `int32 &` | - |
| `MinValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MaxOfByteArray`

```text
MaxOfByteArray(ByteArray: TArray < uint8 > &, IndexOfMaxValue: int32 &, MaxValue: uint8 &) -> void
```

Returns max of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ByteArray` | `TArray < uint8 > &` | - |
| `IndexOfMaxValue` | `int32 &` | - |
| `MaxValue` | `uint8 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MinOfByteArray`

```text
MinOfByteArray(ByteArray: TArray < uint8 > &, IndexOfMinValue: int32 &, MinValue: uint8 &) -> void
```

Returns min of all array entries and the index at which it was found. Returns value of 0 and index of -1 if the supplied array is empty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ByteArray` | `TArray < uint8 > &` | - |
| `IndexOfMinValue` | `int32 &` | - |
| `MinValue` | `uint8 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Lerp`

```text
Lerp(A: float, B: float, V: float) -> float
```

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |
| `V` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `InverseLerp`

```text
InverseLerp(A: float, B: float, Value: float) -> float
```

Returns the fraction (alpha) of the range B-A that corresponds to Value, e.g.,
		inputs A = 0, B = 8, Value = 3 : outputs Return Value = 38, indicating Value is 38 from A to B 
		inputs A = 8, B = 0, Value = 3 : outputs Return Value = 58, indicating Value is 58 from A to B
	 Named InverseLerp because Lerp( A, B, InverseLerp(A, B, Value) ) == Value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | The "from" value this float could be, usually but not necessarily a minimum. Returned as 0. |
| `B` | `float` | The "to" value this float could be, usually but not necessarily a maximum. Returned as 1. |
| `Value` | `float` | A value intended to be normalized relative to B-A |

**Returns**

| Type | Description |
|---|---|
| `float` | A normalized alpha value considering A and B. |

### `Ease`

```text
Ease(A: float, B: float, Alpha: float, EasingFunc: TEnumAsByte < EEasingFunc :: Type >, BlendExp: float, Steps: int32) -> float
```

Easeing  between A and B using a specified easing function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |
| `Alpha` | `float` | - |
| `EasingFunc` | `TEnumAsByte < EEasingFunc :: Type >` | - |
| `BlendExp` | `float` | - |
| `Steps` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Round`

```text
Round(A: float) -> int32
```

Rounds A to the nearest integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `FFloor`

```text
FFloor(A: float) -> int32
```

Rounds A to the largest previous integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `FTrunc`

```text
FTrunc(A: float) -> int32
```

Rounds A to an integer with truncation towards zero.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `FTruncVector`

```text
FTruncVector(InVector: FVector &) -> FIntVector
```

Rounds A to an integer with truncation towards zero for each element in a vector.  (e.g. -1.7 truncated to -1, 2.8 truncated to 2)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVector` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FIntVector` | - |

### `FCeil`

```text
FCeil(A: float) -> int32
```

Rounds A to the smallest following integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `FMod`

```text
FMod(Dividend: float, Divisor: float, Remainder: float &) -> int32
```

Returns the number of times Divisor will go into Dividend (i.e., Dividend divided by Divisor), as well as the remainder

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Dividend` | `float` | - |
| `Divisor` | `float` | - |
| `Remainder` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SignOfFloat`

```text
SignOfFloat(A: float) -> float
```

Sign (float, returns -1 if A < 0, 0 if A is zero, and +1 if A > 0)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `NormalizeToRange`

```text
NormalizeToRange(Value: float, RangeMin: float, RangeMax: float) -> float
```

Returns Value normalized to the given range.  (e.g. 20 normalized to the range 10->50 would result in 0.25)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `RangeMin` | `float` | - |
| `RangeMax` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `MapRangeUnclamped`

```text
MapRangeUnclamped(Value: float, InRangeA: float, InRangeB: float, OutRangeA: float, OutRangeB: float) -> float
```

Returns Value mapped from one range into another.  (e.g. 20 normalized from the range 10->50 to 20->40 would result in 25)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `InRangeA` | `float` | - |
| `InRangeB` | `float` | - |
| `OutRangeA` | `float` | - |
| `OutRangeB` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `MapRangeClamped`

```text
MapRangeClamped(Value: float, InRangeA: float, InRangeB: float, OutRangeA: float, OutRangeB: float) -> float
```

Returns Value mapped from one range into another where the Value is clamped to the Input Range.  (e.g. 0.5 normalized from the range 0->1 to 0->50 would result in 25)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `InRangeA` | `float` | - |
| `InRangeB` | `float` | - |
| `OutRangeA` | `float` | - |
| `OutRangeB` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `MultiplyByPi`

```text
MultiplyByPi(Value: float) -> float
```

Multiplies the input value by pi. 
	UFUNCTION(BlueprintPure, meta=(Keywords = " multiply"), Category="Math|Float")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FInterpEaseInOut`

```text
FInterpEaseInOut(A: float, B: float, Alpha: float, Exponent: float) -> float
```

Interpolate between A and B, applying an ease inout function.  Exp controls the degree of the curve.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |
| `Alpha` | `float` | - |
| `Exponent` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `MakePulsatingValue`

```text
MakePulsatingValue(InCurrentTime: float, InPulsesPerSecond: float, InPhase: float) -> float
```

Simple function to create a pulsating scalar value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCurrentTime` | `float` | Current absolute time |
| `InPulsesPerSecond` | `float` | How many full pulses per second? |
| `InPhase` | `float` | Optional phase amount, between 0.0 and 1.0 (to synchronize pulses) |

**Returns**

| Type | Description |
|---|---|
| `float` | Pulsating value (0.0-1.0) |

### `FixedTurn`

```text
FixedTurn(InCurrent: float, InDesired: float, InDeltaRate: float) -> float
```

Returns a new rotation component value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InCurrent` | `float` | is the current rotation value |
| `InDesired` | `float` | is the desired rotation value |
| `InDeltaRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | a new rotation component value clamped in the range (-360,360) |

### `Multiply_VectorFloat`

```text
Multiply_VectorFloat(A: FVector, B: float) -> FVector
```

Scales Vector A by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Multiply_VectorInt`

```text
Multiply_VectorInt(A: FVector, B: int32) -> FVector
```

Scales Vector A by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  int", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Multiply_VectorVector`

```text
Multiply_VectorVector(A: FVector, B: FVector) -> FVector
```

UFUNCTION(BlueprintPure, meta=(DisplayName = "vector  vector", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category="Math|Vector")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Divide_VectorFloat`

```text
Divide_VectorFloat(A: FVector, B: float) -> FVector
```

Vector divide by a float

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Divide_VectorInt`

```text
Divide_VectorInt(A: FVector, B: int32) -> FVector
```

Vector divide by an integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Divide_VectorVector`

```text
Divide_VectorVector(A: FVector, B: FVector) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Add_VectorVector`

```text
Add_VectorVector(A: FVector, B: FVector) -> FVector
```

Vector addition

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Add_VectorFloat`

```text
Add_VectorFloat(A: FVector, B: float) -> FVector
```

Adds a float to each component of a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Add_VectorInt`

```text
Add_VectorInt(A: FVector, B: int32) -> FVector
```

Adds an integer to each component of a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Subtract_VectorVector`

```text
Subtract_VectorVector(A: FVector, B: FVector) -> FVector
```

Vector subtraction

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Subtract_VectorFloat`

```text
Subtract_VectorFloat(A: FVector, B: float) -> FVector
```

Subtracts a float from each component of a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Subtract_VectorInt`

```text
Subtract_VectorInt(A: FVector, B: int32) -> FVector
```

Subtracts an integer from each component of a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `LessLess_VectorRotator`

```text
LessLess_VectorRotator(A: FVector, B: FRotator) -> FVector
```

Returns result of vector A rotated by the inverse of Rotator B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GreaterGreater_VectorRotator`

```text
GreaterGreater_VectorRotator(A: FVector, B: FRotator) -> FVector
```

Returns result of vector A rotated by Rotator B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RotateAngleAxis`

```text
RotateAngleAxis(InVect: FVector, AngleDeg: float, Axis: FVector) -> FVector
```

Returns result of vector A rotated by AngleDeg around Axis

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVect` | `FVector` | - |
| `AngleDeg` | `float` | - |
| `Axis` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `EqualEqual_VectorVector`

```text
EqualEqual_VectorVector(A: FVector, B: FVector, ErrorTolerance: float) -> bool
```

Returns true if vector A is equal to vector B (A == B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |
| `ErrorTolerance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_VectorVector`

```text
NotEqual_VectorVector(A: FVector, B: FVector, ErrorTolerance: float) -> bool
```

Returns true if vector A is not equal to vector B (A != B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |
| `ErrorTolerance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Dot_VectorVector`

```text
Dot_VectorVector(A: FVector, B: FVector) -> float
```

Returns the dot product of two 3d vectors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Cross_VectorVector`

```text
Cross_VectorVector(A: FVector, B: FVector) -> FVector
```

Returns the cross product of two 3d vectors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `DotProduct2D`

```text
DotProduct2D(A: FVector2D, B: FVector2D) -> float
```

Returns the dot product of two 2d vectors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `CrossProduct2D`

```text
CrossProduct2D(A: FVector2D, B: FVector2D) -> float
```

Returns the cross product of two 2d vectors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `VSize`

```text
VSize(A: FVector) -> float
```

Returns the length of the FVector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `VSize2D`

```text
VSize2D(A: FVector2D) -> float
```

Returns the length of a 2d FVector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `VSizeSquared`

```text
VSizeSquared(A: FVector) -> float
```

Returns the squared length of the FVector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `VSize2DSquared`

```text
VSize2DSquared(A: FVector2D) -> float
```

Returns the squared length of a 2d FVector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Normal`

```text
Normal(A: FVector) -> FVector
```

Returns a unit normal version of the FVector A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Normal2D`

```text
Normal2D(A: FVector2D) -> FVector2D
```

Returns a unit normal version of the vector2d A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `VLerp`

```text
VLerp(A: FVector, B: FVector, V: float) -> FVector
```

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |
| `V` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `VEase`

```text
VEase(A: FVector, B: FVector, Alpha: float, EasingFunc: TEnumAsByte < EEasingFunc :: Type >, BlendExp: float, Steps: int32) -> FVector
```

Easeing  between A and B using a specified easing function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |
| `Alpha` | `float` | - |
| `EasingFunc` | `TEnumAsByte < EEasingFunc :: Type >` | - |
| `BlendExp` | `float` | - |
| `Steps` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `VContainsNan`

```text
VContainsNan(A: FVector) -> bool
```

Returns true if the vector contains NAN

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RandomUnitVector`

```text
RandomUnitVector() -> FVector
```

Returns a random vector with length of 1

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomPointInBoundingBox`

```text
RandomPointInBoundingBox(Origin: FVector &, BoxExtent: FVector &) -> FVector
```

Returns a random point within the specified bounding box

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Origin` | `FVector &` | - |
| `BoxExtent` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomUnitVectorInConeInRadians`

```text
RandomUnitVectorInConeInRadians(ConeDir: FVector, ConeHalfAngleInRadians: float) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector` | The base "center" direction of the cone. |
| `ConeHalfAngleInRadians` | `float` | The half-angle of the cone (from ConeDir to edge), in radians. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomUnitVectorInConeInDegrees`

```text
RandomUnitVectorInConeInDegrees(ConeDir: FVector, ConeHalfAngleInDegrees: float) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector` | The base "center" direction of the cone. |
| `ConeHalfAngleInDegrees` | `float` | The half-angle of the cone (from ConeDir to edge), in degrees. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomUnitVectorInEllipticalConeInRadians`

```text
RandomUnitVectorInEllipticalConeInRadians(ConeDir: FVector, MaxYawInRadians: float, MaxPitchInRadians: float) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector` | - |
| `MaxYawInRadians` | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in radians. |
| `MaxPitchInRadians` | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in radians. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomUnitVectorInEllipticalConeInDegrees`

```text
RandomUnitVectorInEllipticalConeInDegrees(ConeDir: FVector, MaxYawInDegrees: float, MaxPitchInDegrees: float) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector` | - |
| `MaxYawInDegrees` | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in degrees. |
| `MaxPitchInDegrees` | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in degrees. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `MirrorVectorByNormal`

```text
MirrorVectorByNormal(A: FVector, B: FVector) -> FVector
```

Mirrors a vector by a normal

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ProjectVectorOnToVector`

```text
ProjectVectorOnToVector(V: FVector, Target: FVector) -> FVector
```

Projects one vector (V) onto another (Target) and returns the projected vector.
	 If Target is nearly zero in length, returns the zero vector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | Vector to project. |
| `Target` | `FVector` | Vector on which we are projecting. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | V projected on to Target. |

### `GetReflectionVector`

```text
GetReflectionVector(Direction: FVector, SurfaceNormal: FVector) -> FVector
```

Given a direction vector and a surface normal, returns the vector reflected across the surface normal.
	  Produces a result like shining a laser at a mirror!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Direction` | `FVector` | Direction vector the ray is coming from. |
| `SurfaceNormal` | `FVector` | A normal of the surface the ray should be reflected on. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Reflected vector. |

### `FindNearestPointsOnLineSegments`

```text
FindNearestPointsOnLineSegments(Segment1Start: FVector, Segment1End: FVector, Segment2Start: FVector, Segment2End: FVector, Segment1Point: FVector &, Segment2Point: FVector &) -> void
```

Find closest points between 2 segments.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Segment1Start` | `FVector` | Start of the 1st segment. |
| `Segment1End` | `FVector` | End of the 1st segment. |
| `Segment2Start` | `FVector` | Start of the 2nd segment. |
| `Segment2End` | `FVector` | End of the 2nd segment. |
| `Segment1Point` | `FVector &` | Closest point on segment 1 to segment 2. |
| `Segment2Point` | `FVector &` | Closest point on segment 2 to segment 1. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FindClosestPointOnSegment`

```text
FindClosestPointOnSegment(Point: FVector, SegmentStart: FVector, SegmentEnd: FVector) -> FVector
```

Find the closest point on a segment to a given point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point for which we find the closest point on the segment. |
| `SegmentStart` | `FVector` | Start of the segment. |
| `SegmentEnd` | `FVector` | End of the segment. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | The closest point on the segment to the given point. |

### `FindClosestPointOnLine`

```text
FindClosestPointOnLine(Point: FVector, LineOrigin: FVector, LineDirection: FVector) -> FVector
```

Find the closest point on an infinite line to a given point.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point for which we find the closest point on the line. |
| `LineOrigin` | `FVector` | Point of reference on the line. |
| `LineDirection` | `FVector` | Direction of the line. Not required to be normalized. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | The closest point on the line to the given point. |

### `GetPointDistanceToSegment`

```text
GetPointDistanceToSegment(Point: FVector, SegmentStart: FVector, SegmentEnd: FVector) -> float
```

Find the distance from a point to the closest point on a segment.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point for which we find the distance to the closest point on the segment. |
| `SegmentStart` | `FVector` | Start of the segment. |
| `SegmentEnd` | `FVector` | End of the segment. |

**Returns**

| Type | Description |
|---|---|
| `float` | The distance from the given point to the closest point on the segment. |

### `GetPointDistanceToLine`

```text
GetPointDistanceToLine(Point: FVector, LineOrigin: FVector, LineDirection: FVector) -> float
```

Find the distance from a point to the closest point on an infinite line.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point for which we find the distance to the closest point on the line. |
| `LineOrigin` | `FVector` | Point of reference on the line. |
| `LineDirection` | `FVector` | Direction of the line. Not required to be normalized. |

**Returns**

| Type | Description |
|---|---|
| `float` | The distance from the given point to the closest point on the line. |

### `ProjectPointOnToPlane`

```text
ProjectPointOnToPlane(Point: FVector, PlaneBase: FVector, PlaneNormal: FVector) -> FVector
```

Projects a point onto a plane defined by a point on the plane and a plane normal.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point to project onto the plane. |
| `PlaneBase` | `FVector` | A point on the plane. |
| `PlaneNormal` | `FVector` | Normal of the plane. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Point projected onto the plane. |

### `ProjectVectorOnToPlane`

```text
ProjectVectorOnToPlane(V: FVector, PlaneNormal: FVector) -> FVector
```

Projects a vector onto a plane defined by a normalized vector (PlaneNormal).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `V` | `FVector` | Vector to project onto the plane. |
| `PlaneNormal` | `FVector` | Normal of the plane. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | Vector projected onto the plane. |

### `NegateVector`

```text
NegateVector(A: FVector) -> FVector
```

Negate a vector.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ClampVectorSize`

```text
ClampVectorSize(A: FVector, Min: float, Max: float) -> FVector
```

Clamp the vector size between a min and max length

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `Min` | `float` | - |
| `Max` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetMinElement`

```text
GetMinElement(A: FVector) -> float
```

Find the minimum element (X, Y or Z) of a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetMaxElement`

```text
GetMaxElement(A: FVector) -> float
```

Find the maximum element (X, Y or Z) of a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetVectorArrayAverage`

```text
GetVectorArrayAverage(Vectors: TArray < FVector > &) -> FVector
```

Find the average of an array of vectors

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vectors` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetDirectionUnitVector`

```text
GetDirectionUnitVector(From: FVector, To: FVector) -> FVector
```

Find the unit direction vector from one position to another.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `From` | `FVector` | - |
| `To` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `EqualEqual_RotatorRotator`

```text
EqualEqual_RotatorRotator(A: FRotator, B: FRotator, ErrorTolerance: float) -> bool
```

Returns true if rotator A is equal to rotator B (A == B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `FRotator` | - |
| `ErrorTolerance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_RotatorRotator`

```text
NotEqual_RotatorRotator(A: FRotator, B: FRotator, ErrorTolerance: float) -> bool
```

Returns true if rotator A is not equal to rotator B (A != B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `FRotator` | - |
| `ErrorTolerance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Multiply_RotatorFloat`

```text
Multiply_RotatorFloat(A: FRotator, B: float) -> FRotator
```

Returns rotator representing rotator A scaled by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "ScaleRotator", CompactNodeTitle = "", Keywords = " multiply rotate rotation"), Category="Math|Rotator")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `Multiply_RotatorInt`

```text
Multiply_RotatorInt(A: FRotator, B: int32) -> FRotator
```

Returns rotator representing rotator A scaled by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "ScaleRotator (int)", CompactNodeTitle = "", Keywords = " multiply rotate rotation"), Category="Math|Rotator")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `ComposeRotators`

```text
ComposeRotators(A: FRotator, B: FRotator) -> FRotator
```

Combine 2 rotations to give you the resulting rotation of first applying A, then B.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `NegateRotator`

```text
NegateRotator(A: FRotator) -> FRotator
```

Negate a rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `NormalRotator`

```text
NormalRotator(A: FRotator) -> FRotator
```

Negate a rotator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `GetAxes`

```text
GetAxes(A: FRotator, X: FVector &, Y: FVector &, Z: FVector &) -> void
```

Get the reference frame direction vectors (axes) described by this rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `X` | `FVector &` | - |
| `Y` | `FVector &` | - |
| `Z` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RandomRotator`

```text
RandomRotator(bRoll: bool) -> FRotator
```

Generates a random rotation, with optional random roll.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bRoll` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `RLerp`

```text
RLerp(A: FRotator, B: FRotator, Alpha: float, bShortestPath: bool) -> FRotator
```

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `FRotator` | - |
| `Alpha` | `float` | - |
| `bShortestPath` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `REase`

```text
REase(A: FRotator, B: FRotator, Alpha: float, bShortestPath: bool, EasingFunc: TEnumAsByte < EEasingFunc :: Type >, BlendExp: float, Steps: int32) -> FRotator
```

Easeing  between A and B using a specified easing function

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `FRotator` | - |
| `Alpha` | `float` | - |
| `bShortestPath` | `bool` | - |
| `EasingFunc` | `TEnumAsByte < EEasingFunc :: Type >` | - |
| `BlendExp` | `float` | - |
| `Steps` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `RContainsNan`

```text
RContainsNan(A: FRotator) -> bool
```

Returns true if the rotation contains NAN

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NormalizedDeltaRotator`

```text
NormalizedDeltaRotator(A: FRotator, B: FRotator) -> FRotator
```

Normalized A-B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `RotatorFromAxisAndAngle`

```text
RotatorFromAxisAndAngle(Axis: FVector, Angle: float) -> FRotator
```

Create a rotation from an axis and and angle (in degrees)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Axis` | `FVector` | - |
| `Angle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `ClampAxis`

```text
ClampAxis(Angle: float) -> float
```

Clamps an angle to the range of [0, 360].

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Angle` | `float` | The angle to clamp. |

**Returns**

| Type | Description |
|---|---|
| `float` | The clamped angle. |

### `NormalizeAxis`

```text
NormalizeAxis(Angle: float) -> float
```

Clamps an angle to the range of [-180, 180].

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Angle` | `float` | The Angle to clamp. |

**Returns**

| Type | Description |
|---|---|
| `float` | The clamped angle. |

### `LinearColorLerp`

```text
LinearColorLerp(A: FLinearColor, B: FLinearColor, Alpha: float) -> FLinearColor
```

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FLinearColor` | - |
| `B` | `FLinearColor` | - |
| `Alpha` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `LinearColorLerpUsingHSV`

```text
LinearColorLerpUsingHSV(A: FLinearColor, B: FLinearColor, Alpha: float) -> FLinearColor
```

Linearly interpolates between two colors by the specified Alpha amount (100% of A when Alpha=0 and 100% of B when Alpha=1).  The interpolation is performed in HSV color space taking the shortest path to the new color's hue.  This can give better results than a normal lerp, but is much more expensive.  The incoming colors are in RGB space, and the output color will be RGB.  The alpha value will also be interpolated.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FLinearColor` | The color and alpha to interpolate from as linear RGBA |
| `B` | `FLinearColor` | The color and alpha to interpolate to as linear RGBA |
| `Alpha` | `float` | Scalar interpolation amount (usually between 0.0 and 1.0 inclusive) |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | The interpolated color in linear RGB space along with the interpolated alpha value |

### `Multiply_LinearColorLinearColor`

```text
Multiply_LinearColorLinearColor(A: FLinearColor, B: FLinearColor) -> FLinearColor
```

Element-wise multiplication of two linear colors (RR, GG, BB, AA) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "LinearColor  (LinearColor)", CompactNodeTitle = ""), Category="Math|Color")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FLinearColor` | - |
| `B` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `Multiply_LinearColorFloat`

```text
Multiply_LinearColorFloat(A: FLinearColor, B: float) -> FLinearColor
```

Element-wise multiplication of a linear color by a float (FR, FG, FB, FA) 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "LinearColor  Float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Color")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FLinearColor` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `MakePlaneFromPointAndNormal`

```text
MakePlaneFromPointAndNormal(Point: FVector, Normal: FVector) -> FPlane
```

Creates a plane with a facing direction of Normal at the given Point

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | A point on the plane |
| `Normal` | `FVector` | The Normal of the plane at Point |

**Returns**

| Type | Description |
|---|---|
| `FPlane` | Plane instance |

### `MakeDateTime`

```text
MakeDateTime(Year: int32, Month: int32, Day: int32, Hour: int32, Minute: int32, Second: int32, Millisecond: int32) -> FDateTime
```

Makes a DateTime struct

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Year` | `int32` | - |
| `Month` | `int32` | - |
| `Day` | `int32` | - |
| `Hour` | `int32` | - |
| `Minute` | `int32` | - |
| `Second` | `int32` | - |
| `Millisecond` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `MakeDateTimeFromString`

```text
MakeDateTimeFromString(InString: FString &) -> FDateTime
```

Makes a DateTime struct

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `BreakDateTime`

```text
BreakDateTime(InDateTime: FDateTime, Year: int32 &, Month: int32 &, Day: int32 &, Hour: int32 &, Minute: int32 &, Second: int32 &, Millisecond: int32 &) -> void
```

Breaks a DateTime into its components

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDateTime` | `FDateTime` | - |
| `Year` | `int32 &` | - |
| `Month` | `int32 &` | - |
| `Day` | `int32 &` | - |
| `Hour` | `int32 &` | - |
| `Minute` | `int32 &` | - |
| `Second` | `int32 &` | - |
| `Millisecond` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Add_DateTimeTimespan`

```text
Add_DateTimeTimespan(A: FDateTime, B: FTimespan) -> FDateTime
```

Addition (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `Subtract_DateTimeTimespan`

```text
Subtract_DateTimeTimespan(A: FDateTime, B: FTimespan) -> FDateTime
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `Subtract_DateTimeDateTime`

```text
Subtract_DateTimeDateTime(A: FDateTime, B: FDateTime) -> FTimespan
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `EqualEqual_DateTimeDateTime`

```text
EqualEqual_DateTimeDateTime(A: FDateTime, B: FDateTime) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_DateTimeDateTime`

```text
NotEqual_DateTimeDateTime(A: FDateTime, B: FDateTime) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Greater_DateTimeDateTime`

```text
Greater_DateTimeDateTime(A: FDateTime, B: FDateTime) -> bool
```

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GreaterEqual_DateTimeDateTime`

```text
GreaterEqual_DateTimeDateTime(A: FDateTime, B: FDateTime) -> bool
```

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Less_DateTimeDateTime`

```text
Less_DateTimeDateTime(A: FDateTime, B: FDateTime) -> bool
```

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LessEqual_DateTimeDateTime`

```text
LessEqual_DateTimeDateTime(A: FDateTime, B: FDateTime) -> bool
```

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |
| `B` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDate`

```text
GetDate(A: FDateTime) -> FDateTime
```

Returns the date component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `GetDay`

```text
GetDay(A: FDateTime) -> int32
```

Returns the day component of A (1 to 31)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDayOfYear`

```text
GetDayOfYear(A: FDateTime) -> int32
```

Returns the day of year of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetHour`

```text
GetHour(A: FDateTime) -> int32
```

Returns the hour component of A (24h format)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetHour12`

```text
GetHour12(A: FDateTime) -> int32
```

Returns the hour component of A (12h format)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetMillisecond`

```text
GetMillisecond(A: FDateTime) -> int32
```

Returns the millisecond component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetMinute`

```text
GetMinute(A: FDateTime) -> int32
```

Returns the minute component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetMonth`

```text
GetMonth(A: FDateTime) -> int32
```

Returns the month component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetSecond`

```text
GetSecond(A: FDateTime) -> int32
```

Returns the second component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetTimeOfDay`

```text
GetTimeOfDay(A: FDateTime) -> FTimespan
```

Returns the time elapsed since midnight of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `GetYear`

```text
GetYear(A: FDateTime) -> int32
```

Returns the year component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsAfternoon`

```text
IsAfternoon(A: FDateTime) -> bool
```

Returns whether A's time is in the afternoon

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsMorning`

```text
IsMorning(A: FDateTime) -> bool
```

Returns whether A's time is in the morning

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DaysInMonth`

```text
DaysInMonth(Year: int32, Month: int32) -> int32
```

Returns the number of days in the given year and month

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Year` | `int32` | - |
| `Month` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `DaysInYear`

```text
DaysInYear(Year: int32) -> int32
```

Returns the number of days in the given year

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Year` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsLeapYear`

```text
IsLeapYear(Year: int32) -> bool
```

Returns whether given year is a leap year

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Year` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DateTimeMaxValue`

```text
DateTimeMaxValue() -> FDateTime
```

Returns the maximum date and time value

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `DateTimeMinValue`

```text
DateTimeMinValue() -> FDateTime
```

Returns the minimum date and time value

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `Now`

```text
Now() -> FDateTime
```

Returns the local date and time on this computer

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `Today`

```text
Today() -> FDateTime
```

Returns the local date on this computer

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `UtcNow`

```text
UtcNow() -> FDateTime
```

Returns the UTC date and time on this computer

**Returns**

| Type | Description |
|---|---|
| `FDateTime` | - |

### `DateTimeFromIsoString`

```text
DateTimeFromIsoString(IsoString: FString, Result: FDateTime &) -> bool
```

Converts a date string in ISO-8601 format to a DateTime object

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsoString` | `FString` | - |
| `Result` | `FDateTime &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `DateTimeFromString`

```text
DateTimeFromString(DateTimeString: FString, Result: FDateTime &) -> bool
```

Converts a date string to a DateTime object

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DateTimeString` | `FString` | - |
| `Result` | `FDateTime &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `MakeTimespan`

```text
MakeTimespan(Days: int32, Hours: int32, Minutes: int32, Seconds: int32, Milliseconds: int32) -> FTimespan
```

Makes a Timespan struct

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Days` | `int32` | - |
| `Hours` | `int32` | - |
| `Minutes` | `int32` | - |
| `Seconds` | `int32` | - |
| `Milliseconds` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `MakeTimespan2`

```text
MakeTimespan2(Days: int32, Hours: int32, Minutes: int32, Seconds: int32, FractionNano: int32) -> FTimespan
```

Makes a Timespan struct

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Days` | `int32` | - |
| `Hours` | `int32` | - |
| `Minutes` | `int32` | - |
| `Seconds` | `int32` | - |
| `FractionNano` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `BreakTimespan`

```text
BreakTimespan(InTimespan: FTimespan, Days: int32 &, Hours: int32 &, Minutes: int32 &, Seconds: int32 &, Milliseconds: int32 &) -> void
```

Breaks a Timespan into its components

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTimespan` | `FTimespan` | - |
| `Days` | `int32 &` | - |
| `Hours` | `int32 &` | - |
| `Minutes` | `int32 &` | - |
| `Seconds` | `int32 &` | - |
| `Milliseconds` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BreakTimespan2`

```text
BreakTimespan2(InTimespan: FTimespan, Days: int32 &, Hours: int32 &, Minutes: int32 &, Seconds: int32 &, FractionNano: int32 &) -> void
```

Breaks a Timespan into its components

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTimespan` | `FTimespan` | - |
| `Days` | `int32 &` | - |
| `Hours` | `int32 &` | - |
| `Minutes` | `int32 &` | - |
| `Seconds` | `int32 &` | - |
| `FractionNano` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Add_TimespanTimespan`

```text
Add_TimespanTimespan(A: FTimespan, B: FTimespan) -> FTimespan
```

Addition (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `Subtract_TimespanTimespan`

```text
Subtract_TimespanTimespan(A: FTimespan, B: FTimespan) -> FTimespan
```

Subtraction (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `Multiply_TimespanFloat`

```text
Multiply_TimespanFloat(A: FTimespan, Scalar: float) -> FTimespan
```

Scalar multiplication (A  s) 
	UFUNCTION(BlueprintPure, meta=(DisplayName="Timespan  float", CompactNodeTitle="", Keywords=" multiply"), Category="Math|Timespan")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `Scalar` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `Divide_TimespanFloat`

```text
Divide_TimespanFloat(A: FTimespan, Scalar: float) -> FTimespan
```

Scalar division (A  s) 
	UFUNCTION(BlueprintPure, meta=(DisplayName="Timespan  float", CompactNodeTitle="", Keywords=" divide"), Category="Math|Timespan")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `Scalar` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `EqualEqual_TimespanTimespan`

```text
EqualEqual_TimespanTimespan(A: FTimespan, B: FTimespan) -> bool
```

Returns true if the values are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_TimespanTimespan`

```text
NotEqual_TimespanTimespan(A: FTimespan, B: FTimespan) -> bool
```

Returns true if the values are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Greater_TimespanTimespan`

```text
Greater_TimespanTimespan(A: FTimespan, B: FTimespan) -> bool
```

Returns true if A is greater than B (A > B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GreaterEqual_TimespanTimespan`

```text
GreaterEqual_TimespanTimespan(A: FTimespan, B: FTimespan) -> bool
```

Returns true if A is greater than or equal to B (A >= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Less_TimespanTimespan`

```text
Less_TimespanTimespan(A: FTimespan, B: FTimespan) -> bool
```

Returns true if A is less than B (A < B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `LessEqual_TimespanTimespan`

```text
LessEqual_TimespanTimespan(A: FTimespan, B: FTimespan) -> bool
```

Returns true if A is less than or equal to B (A <= B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDays`

```text
GetDays(A: FTimespan) -> int32
```

Returns the days component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetDuration`

```text
GetDuration(A: FTimespan) -> FTimespan
```

Returns the absolute value of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `GetHours`

```text
GetHours(A: FTimespan) -> int32
```

Returns the hours component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetMilliseconds`

```text
GetMilliseconds(A: FTimespan) -> int32
```

Returns the milliseconds component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetMinutes`

```text
GetMinutes(A: FTimespan) -> int32
```

Returns the minutes component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetSeconds`

```text
GetSeconds(A: FTimespan) -> int32
```

Returns the seconds component of A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetTotalDays`

```text
GetTotalDays(A: FTimespan) -> float
```

Returns the total number of days in A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTotalHours`

```text
GetTotalHours(A: FTimespan) -> float
```

Returns the total number of hours in A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTotalMilliseconds`

```text
GetTotalMilliseconds(A: FTimespan) -> float
```

Returns the total number of milliseconds in A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTotalMinutes`

```text
GetTotalMinutes(A: FTimespan) -> float
```

Returns the total number of minutes in A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetTotalSeconds`

```text
GetTotalSeconds(A: FTimespan) -> float
```

Returns the total number of seconds in A

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `FromDays`

```text
FromDays(Days: float) -> FTimespan
```

Returns a time span that represents the specified number of days

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Days` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `FromHours`

```text
FromHours(Hours: float) -> FTimespan
```

Returns a time span that represents the specified number of hours

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hours` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `FromMilliseconds`

```text
FromMilliseconds(Milliseconds: float) -> FTimespan
```

Returns a time span that represents the specified number of milliseconds

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Milliseconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `FromMinutes`

```text
FromMinutes(Minutes: float) -> FTimespan
```

Returns a time span that represents the specified number of minutes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Minutes` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `FromSeconds`

```text
FromSeconds(Seconds: float) -> FTimespan
```

Returns a time span that represents the specified number of seconds

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Seconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `TimespanMaxValue`

```text
TimespanMaxValue() -> FTimespan
```

Returns the maximum time span value

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `TimespanMinValue`

```text
TimespanMinValue() -> FTimespan
```

Returns the minimum time span value

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `TimespanRatio`

```text
TimespanRatio(A: FTimespan, B: FTimespan) -> float
```

Returns the ratio between two time spans (A  B), handles zero values

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTimespan` | - |
| `B` | `FTimespan` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `TimespanZeroValue`

```text
TimespanZeroValue() -> FTimespan
```

Returns a zero time span value

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | - |

### `TimespanFromString`

```text
TimespanFromString(TimespanString: FString, Result: FTimespan &) -> bool
```

Converts a time span string to a Timespan object

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TimespanString` | `FString` | - |
| `Result` | `FTimespan &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Conv_ByteToFloat`

```text
Conv_ByteToFloat(InByte: uint8) -> float
```

Converts a byte to a float

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InByte` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Conv_IntToFloat`

```text
Conv_IntToFloat(InInt: int32) -> float
```

Converts an integer to a float

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Conv_IntToInt64`

```text
Conv_IntToInt64(InInt: int32) -> int64
```

Converts an integer to a 64 bit integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Conv_Int64ToInt`

```text
Conv_Int64ToInt(InInt: int64) -> int32
```

Converts an 64 bit integer to a 32 bit integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Conv_IntToByte`

```text
Conv_IntToByte(InInt: int32) -> uint8
```

Converts an integer to a byte (if the integer is too large, returns the low 8 bits)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `Conv_IntToIntVector`

```text
Conv_IntToIntVector(InInt: int32) -> FIntVector
```

Converts an integer to an IntVector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FIntVector` | - |

### `Conv_IntToBool`

```text
Conv_IntToBool(InInt: int32) -> bool
```

Converts a int to a bool

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Conv_BoolToInt`

```text
Conv_BoolToInt(InBool: bool) -> int32
```

Converts a bool to an int

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Conv_BoolToFloat`

```text
Conv_BoolToFloat(InBool: bool) -> float
```

Converts a bool to a float (0.0f or 1.0f)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Conv_BoolToByte`

```text
Conv_BoolToByte(InBool: bool) -> uint8
```

Converts a bool to a byte

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `uint8` | - |

### `Conv_ByteToInt`

```text
Conv_ByteToInt(InByte: uint8) -> int32
```

Converts a byte to an integer

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InByte` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Conv_VectorToLinearColor`

```text
Conv_VectorToLinearColor(InVec: FVector) -> FLinearColor
```

Converts a vector to LinearColor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `Conv_LinearColorToVector`

```text
Conv_LinearColorToVector(InLinearColor: FLinearColor) -> FVector
```

Converts a LinearColor to a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLinearColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Conv_ColorToLinearColor`

```text
Conv_ColorToLinearColor(InColor: FColor) -> FLinearColor
```

Converts a color to LinearColor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `Conv_LinearColorToColor`

```text
Conv_LinearColorToColor(InLinearColor: FLinearColor) -> FColor
```

Converts a LinearColor to a color

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLinearColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `FColor` | - |

### `Conv_VectorToTransform`

```text
Conv_VectorToTransform(InTranslation: FVector) -> FTransform
```

Convert a vector to a transform. Uses vector as location

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTranslation` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `Conv_VectorToVector2D`

```text
Conv_VectorToVector2D(InVec: FVector) -> FVector2D
```

Convert a Vector to a Vector2D

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Conv_Vector2DToVector`

```text
Conv_Vector2DToVector(InVec2D: FVector2D, Z: float) -> FVector
```

Convert a Vector2D to a Vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec2D` | `FVector2D` | - |
| `Z` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Conv_IntVectorToVector`

```text
Conv_IntVectorToVector(InIntVector: FIntVector &) -> FVector
```

Convert an IntVector to a vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIntVector` | `FIntVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Conv_FloatToVector`

```text
Conv_FloatToVector(InFloat: float) -> FVector
```

Convert a float into a vector, where each element is that float

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFloat` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `Conv_FloatToLinearColor`

```text
Conv_FloatToLinearColor(InFloat: float) -> FLinearColor
```

Convert a float into a LinearColor, where each element is that float

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFloat` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `MakeBox`

```text
MakeBox(Min: FVector, Max: FVector) -> FBox
```

Makes an FBox from Min and Max and sets IsValid to true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `FVector` | - |
| `Max` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FBox` | - |

### `MakeBox2D`

```text
MakeBox2D(Min: FVector2D, Max: FVector2D) -> FBox2D
```

Makes an FBox2D from Min and Max and sets IsValid to true

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `FVector2D` | - |
| `Max` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FBox2D` | - |

### `MakeVector`

```text
MakeVector(X: float, Y: float, Z: float) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `float` | - |
| `Y` | `float` | - |
| `Z` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `BreakVector`

```text
BreakVector(InVec: FVector, X: float &, Y: float &, Z: float &) -> void
```

Breaks a vector apart into X, Y, Z

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector` | - |
| `X` | `float &` | - |
| `Y` | `float &` | - |
| `Z` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeVector2D`

```text
MakeVector2D(X: float, Y: float) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `float` | - |
| `Y` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `BreakVector2D`

```text
BreakVector2D(InVec: FVector2D, X: float &, Y: float &) -> void
```

Breaks a 2D vector apart into X, Y.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector2D` | - |
| `X` | `float &` | - |
| `Y` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetForwardVector`

```text
GetForwardVector(InRot: FRotator) -> FVector
```

Rotate the world forward vector by the given rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetRightVector`

```text
GetRightVector(InRot: FRotator) -> FVector
```

Rotate the world right vector by the given rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetUpVector`

```text
GetUpVector(InRot: FRotator) -> FVector
```

Rotate the world up vector by the given rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `CreateVectorFromYawPitch`

```text
CreateVectorFromYawPitch(Yaw: float, Pitch: float, Length: float) -> FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Yaw` | `float` | - |
| `Pitch` | `float` | - |
| `Length` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `GetYawPitchFromVector`

```text
GetYawPitchFromVector(InVec: FVector, Yaw: float &, Pitch: float &) -> void
```

Breaks a vector apart into Yaw, Pitch rotation values given in degrees. (non-clamped)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector` | - |
| `Yaw` | `float &` | - |
| `Pitch` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAzimuthAndElevation`

```text
GetAzimuthAndElevation(InDirection: FVector, ReferenceFrame: FTransform &, Azimuth: float &, Elevation: float &) -> void
```

Breaks a direction vector apart into Azimuth (Yaw) and Elevation (Pitch) rotation values given in degrees. (non-clamped)
	 Relative to the provided reference frame (an Actor's WorldTransform for example)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDirection` | `FVector` | - |
| `ReferenceFrame` | `FTransform &` | - |
| `Azimuth` | `float &` | - |
| `Elevation` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeRotator`

```text
MakeRotator(Roll: float, Pitch: float, Yaw: float) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Roll` | `float` | - |
| `Pitch` | `float` | - |
| `Yaw` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `FindLookAtRotation`

```text
FindLookAtRotation(Start: FVector &, Target: FVector &) -> FRotator
```

Find a rotation for an object at Start location to point at Target location.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector &` | - |
| `Target` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromX`

```text
MakeRotFromX(X: FVector &) -> FRotator
```

Builds a rotator given only a XAxis. Y and Z are unspecified but will be orthonormal. XAxis need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromY`

```text
MakeRotFromY(Y: FVector &) -> FRotator
```

Builds a rotation matrix given only a YAxis. X and Z are unspecified but will be orthonormal. YAxis need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Y` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromZ`

```text
MakeRotFromZ(Z: FVector &) -> FRotator
```

Builds a rotation matrix given only a ZAxis. X and Y are unspecified but will be orthonormal. ZAxis need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Z` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromXY`

```text
MakeRotFromXY(X: FVector &, Y: FVector &) -> FRotator
```

Builds a matrix with given X and Y axes. X will remain fixed, Y may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `FVector &` | - |
| `Y` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromXZ`

```text
MakeRotFromXZ(X: FVector &, Z: FVector &) -> FRotator
```

Builds a matrix with given X and Z axes. X will remain fixed, Z may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `X` | `FVector &` | - |
| `Z` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromYX`

```text
MakeRotFromYX(Y: FVector &, X: FVector &) -> FRotator
```

Builds a matrix with given Y and X axes. Y will remain fixed, X may be changed minimally to enforce orthogonality. Z will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Y` | `FVector &` | - |
| `X` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromYZ`

```text
MakeRotFromYZ(Y: FVector &, Z: FVector &) -> FRotator
```

Builds a matrix with given Y and Z axes. Y will remain fixed, Z may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Y` | `FVector &` | - |
| `Z` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromZX`

```text
MakeRotFromZX(Z: FVector &, X: FVector &) -> FRotator
```

Builds a matrix with given Z and X axes. Z will remain fixed, X may be changed minimally to enforce orthogonality. Y will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Z` | `FVector &` | - |
| `X` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `MakeRotFromZY`

```text
MakeRotFromZY(Z: FVector &, Y: FVector &) -> FRotator
```

Builds a matrix with given Z and Y axes. Z will remain fixed, Y may be changed minimally to enforce orthogonality. X will be computed. Inputs need not be normalized.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Z` | `FVector &` | - |
| `Y` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `BreakRotator`

```text
BreakRotator(InRot: FRotator, Roll: float &, Pitch: float &, Yaw: float &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | - |
| `Roll` | `float &` | - |
| `Pitch` | `float &` | - |
| `Yaw` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BreakRotIntoAxes`

```text
BreakRotIntoAxes(InRot: FRotator &, X: FVector &, Y: FVector &, Z: FVector &) -> void
```

Breaks apart a rotator into its component axes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator &` | - |
| `X` | `FVector &` | - |
| `Y` | `FVector &` | - |
| `Z` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeTransform`

```text
MakeTransform(Translation: FVector, Rotation: FRotator, Scale: FVector) -> FTransform
```

Make a transform from location, rotation and scale

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Translation` | `FVector` | - |
| `Rotation` | `FRotator` | - |
| `Scale` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `BreakTransform`

```text
BreakTransform(InTransform: FTransform &, Translation: FVector &, Rotation: FRotator &, Scale: FVector &) -> void
```

Breaks apart a transform into location, rotation and scale

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTransform` | `FTransform &` | - |
| `Translation` | `FVector &` | - |
| `Rotation` | `FRotator &` | - |
| `Scale` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeRandomStream`

```text
MakeRandomStream(InitialSeed: int32) -> FRandomStream
```

Makes a SRand-based random number generator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InitialSeed` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FRandomStream` | - |

### `BreakRandomStream`

```text
BreakRandomStream(InRandomStream: FRandomStream &, InitialSeed: int32 &) -> void
```

Breaks apart a random number generator

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRandomStream` | `FRandomStream &` | - |
| `InitialSeed` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `MakeColor`

```text
MakeColor(R: float, G: float, B: float, A: float) -> FLinearColor
```

Make a color from individual color components (RGB space)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `R` | `float` | - |
| `G` | `float` | - |
| `B` | `float` | - |
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `BreakColor`

```text
BreakColor(InColor: FLinearColor, R: float &, G: float &, B: float &, A: float &) -> void
```

Breaks apart a color into individual RGB components (as well as alpha)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FLinearColor` | - |
| `R` | `float &` | - |
| `G` | `float &` | - |
| `B` | `float &` | - |
| `A` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HSVToRGB`

```text
HSVToRGB(H: float, S: float, V: float, A: float) -> FLinearColor
```

Make a color from individual color components (HSV space)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `H` | `float` | - |
| `S` | `float` | - |
| `V` | `float` | - |
| `A` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `RGBToHSV`

```text
RGBToHSV(InColor: FLinearColor, H: float &, S: float &, V: float &, A: float &) -> void
```

Breaks apart a color into individual HSV components (as well as alpha)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FLinearColor` | - |
| `H` | `float &` | - |
| `S` | `float &` | - |
| `V` | `float &` | - |
| `A` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HSVToRGB_Vector`

```text
HSVToRGB_Vector(HSV: FLinearColor, RGB: FLinearColor &) -> void
```

Converts a HSV linear color (where H is in R, S is in G, and V is in B) to RGB

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HSV` | `FLinearColor` | - |
| `RGB` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RGBToHSV_Vector`

```text
RGBToHSV_Vector(RGB: FLinearColor, HSV: FLinearColor &) -> void
```

Converts a RGB linear color to HSV (where H is in R, S is in G, and V is in B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RGB` | `FLinearColor` | - |
| `HSV` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HexToRGB_Vector`

```text
HexToRGB_Vector(HexString: FString, bSRGB: bool) -> FLinearColor
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HexString` | `FString` | - |
| `bSRGB` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `RGB_VectorToHex`

```text
RGB_VectorToHex(RGB: FLinearColor, bSRGB: bool) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RGB` | `FLinearColor` | - |
| `bSRGB` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `SelectString`

```text
SelectString(A: FString &, B: FString &, bSelectA: bool) -> FString
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FString &` | - |
| `B` | `FString &` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `SelectInt`

```text
SelectInt(A: int32, B: int32, bSelectA: bool) -> int32
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `int32` | - |
| `B` | `int32` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SelectFloat`

```text
SelectFloat(A: float, B: float, bSelectA: bool) -> float
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `float` | - |
| `B` | `float` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SelectVector`

```text
SelectVector(A: FVector, B: FVector, bSelectA: bool) -> FVector
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector` | - |
| `B` | `FVector` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SelectRotator`

```text
SelectRotator(A: FRotator, B: FRotator, bSelectA: bool) -> FRotator
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FRotator` | - |
| `B` | `FRotator` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SelectColor`

```text
SelectColor(A: FLinearColor, B: FLinearColor, bSelectA: bool) -> FLinearColor
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FLinearColor` | - |
| `B` | `FLinearColor` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SelectTransform`

```text
SelectTransform(A: FTransform &, B: FTransform &, bSelectA: bool) -> FTransform
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTransform &` | - |
| `B` | `FTransform &` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `SelectObject`

```text
SelectObject(A: UObject *, B: UObject *, bSelectA: bool) -> UObject *
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `UObject *` | - |
| `B` | `UObject *` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

### `SelectClass`

```text
SelectClass(A: UClass *, B: UClass *, bSelectA: bool) -> UClass *
```

If bPickA is true, A is returned, otherwise B is

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `UClass *` | - |
| `B` | `UClass *` | - |
| `bSelectA` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `MakeRotationFromAxes`

```text
MakeRotationFromAxes(Forward: FVector, Right: FVector, Up: FVector) -> FRotator
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Forward` | `FVector` | - |
| `Right` | `FVector` | - |
| `Up` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `Conv_VectorToRotator`

```text
Conv_VectorToRotator(InVec: FVector) -> FRotator
```

Create a rotator which orients X along the supplied direction vector

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `Conv_RotatorToVector`

```text
Conv_RotatorToVector(InRot: FRotator) -> FVector
```

Get the X direction vector after this rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `EqualEqual_ObjectObject`

```text
EqualEqual_ObjectObject(A: UObject *, B: UObject *) -> bool
```

Returns true if A and B are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `UObject *` | - |
| `B` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_ObjectObject`

```text
NotEqual_ObjectObject(A: UObject *, B: UObject *) -> bool
```

Returns true if A and B are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `UObject *` | - |
| `B` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_ClassClass`

```text
EqualEqual_ClassClass(A: UClass *, B: UClass *) -> bool
```

Returns true if A and B are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `UClass *` | - |
| `B` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_ClassClass`

```text
NotEqual_ClassClass(A: UClass *, B: UClass *) -> bool
```

Returns true if A and B are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `UClass *` | - |
| `B` | `UClass *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClassIsChildOf`

```text
ClassIsChildOf(TestClass: TSubclassOf < UObject >, ParentClass: TSubclassOf < UObject >) -> bool
```

Determine if a class is a child of another class.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TestClass` | `TSubclassOf < UObject >` | - |
| `ParentClass` | `TSubclassOf < UObject >` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if TestClass == ParentClass, or if TestClass is a child of ParentClass; false otherwise, or if either |

### `EqualEqual_NameName`

```text
EqualEqual_NameName(A: FName, B: FName) -> bool
```

Returns true if A and B are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FName` | - |
| `B` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_NameName`

```text
NotEqual_NameName(A: FName, B: FName) -> bool
```

Returns true if A and B are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FName` | - |
| `B` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TransformLocation`

```text
TransformLocation(T: FTransform &, Location: FVector) -> FVector
```

Transform a position by the supplied transform.
	 	For example, if T was an object's transform, this would transform a position from local space to world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform &` | - |
| `Location` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `TransformDirection`

```text
TransformDirection(T: FTransform &, Direction: FVector) -> FVector
```

Transform a direction vector by the supplied transform - will not change its length. 
	 	For example, if T was an object's transform, this would transform a direction from local space to world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform &` | - |
| `Direction` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `TransformRotation`

```text
TransformRotation(T: FTransform &, Rotation: FRotator) -> FRotator
```

Transform a rotator by the supplied transform. 
	 	For example, if T was an object's transform, this would transform a rotation from local space to world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform &` | - |
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `InverseTransformLocation`

```text
InverseTransformLocation(T: FTransform &, Location: FVector) -> FVector
```

Transform a position by the inverse of the supplied transform.
	 	For example, if T was an object's transform, this would transform a position from world space to local space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform &` | - |
| `Location` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `InverseTransformDirection`

```text
InverseTransformDirection(T: FTransform &, Direction: FVector) -> FVector
```

Transform a direction vector by the inverse of the supplied transform - will not change its length.
	 	For example, if T was an object's transform, this would transform a direction from world space to local space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform &` | - |
| `Direction` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `InverseTransformRotation`

```text
InverseTransformRotation(T: FTransform &, Rotation: FRotator) -> FRotator
```

Transform a rotator by the inverse of the supplied transform. 
	 	For example, if T was an object's transform, this would transform a rotation from world space to local space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform &` | - |
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `ComposeTransforms`

```text
ComposeTransforms(A: FTransform &, B: FTransform &) -> FTransform
```

Compose two transforms in order: A  B.
	 
	  Order matters when composing transforms:
	  A  B will yield a transform that logically first applies A then B to any subsequent transformation.
	 
	  Example: LocalToWorld = ComposeTransforms(DeltaRotation, LocalToWorld) will change rotation in local space by DeltaRotation.
	  Example: LocalToWorld = ComposeTransforms(LocalToWorld, DeltaRotation) will change rotation in world space by DeltaRotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTransform &` | - |
| `B` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | New transform: A  B |

### `ConvertTransformToRelative`

```text
ConvertTransformToRelative(Transform: FTransform &, ParentTransform: FTransform &) -> FTransform
```

Returns the given transform, converted to be relative to the given ParentTransform.
	 
	  Example: AToB = ConvertTransformToRelative(AToWorld, BToWorld) to compute A relative to B.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform &` | The transform you wish to convert |
| `ParentTransform` | `FTransform &` | The transform the conversion is relative to (in the same space as Transform) |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | The new relative transform |

### `InvertTransform`

```text
InvertTransform(T: FTransform &) -> FTransform
```

Returns the inverse of the given transform T.
	  
	  Example: Given a LocalToWorld transform, WorldToLocal will be returned.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `T` | `FTransform &` | The transform you wish to invert |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | The inverse of T. |

### `TLerp`

```text
TLerp(A: FTransform &, B: FTransform &, Alpha: float, InterpMode: TEnumAsByte < ELerpInterpolationMode :: Type >) -> FTransform
```

Linearly interpolates between A and B based on Alpha (100% of A when Alpha=0 and 100% of B when Alpha=1).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTransform &` | - |
| `B` | `FTransform &` | - |
| `Alpha` | `float` | - |
| `InterpMode` | `TEnumAsByte < ELerpInterpolationMode :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `TEase`

```text
TEase(A: FTransform &, B: FTransform &, Alpha: float, EasingFunc: TEnumAsByte < EEasingFunc :: Type >, BlendExp: float, Steps: int32) -> FTransform
```

Ease between A and B using a specified easing function.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTransform &` | - |
| `B` | `FTransform &` | - |
| `Alpha` | `float` | - |
| `EasingFunc` | `TEnumAsByte < EEasingFunc :: Type >` | - |
| `BlendExp` | `float` | - |
| `Steps` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `TInterpTo`

```text
TInterpTo(Current: FTransform &, Target: FTransform &, DeltaTime: float, InterpSpeed: float) -> FTransform
```

Tries to reach a target transform.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FTransform &` | - |
| `Target` | `FTransform &` | - |
| `DeltaTime` | `float` | - |
| `InterpSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FTransform` | - |

### `EqualEqual_TransformTransform`

```text
EqualEqual_TransformTransform(A: FTransform &, B: FTransform &) -> bool
```

Returns true if transform A is equal to transform B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTransform &` | - |
| `B` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NearlyEqual_TransformTransform`

```text
NearlyEqual_TransformTransform(A: FTransform &, B: FTransform &, LocationTolerance: float, RotationTolerance: float, Scale3DTolerance: float) -> bool
```

Returns true if transform A is nearly equal to B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FTransform &` | - |
| `B` | `FTransform &` | - |
| `LocationTolerance` | `float` | How close position of transforms need to be to be considered equal |
| `RotationTolerance` | `float` | How close rotations of transforms need to be to be considered equal |
| `Scale3DTolerance` | `float` | How close scale of transforms need to be to be considered equal |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Add_Vector2DVector2D`

```text
Add_Vector2DVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

Returns addition of Vector A and Vector B (A + B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Subtract_Vector2DVector2D`

```text
Subtract_Vector2DVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

Returns subtraction of Vector B from Vector A (A - B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Multiply_Vector2DFloat`

```text
Multiply_Vector2DFloat(A: FVector2D, B: float) -> FVector2D
```

Returns Vector A scaled by B 
	UFUNCTION(BlueprintPure, meta=(DisplayName = "vector2d  float", CompactNodeTitle = "", Keywords = " multiply"), Category="Math|Vector2D")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Multiply_Vector2DVector2D`

```text
Multiply_Vector2DVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

UFUNCTION(BlueprintPure, meta = (DisplayName = "vector2d  vector2d", CompactNodeTitle = "", Keywords = " multiply", CommutativeAssociativeBinaryOperator = "true"), Category = "Math|Vector2D")

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Divide_Vector2DFloat`

```text
Divide_Vector2DFloat(A: FVector2D, B: float) -> FVector2D
```

Returns Vector A divided by B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Divide_Vector2DVector2D`

```text
Divide_Vector2DVector2D(A: FVector2D, B: FVector2D) -> FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Add_Vector2DFloat`

```text
Add_Vector2DFloat(A: FVector2D, B: float) -> FVector2D
```

Returns Vector A added by B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `Subtract_Vector2DFloat`

```text
Subtract_Vector2DFloat(A: FVector2D, B: float) -> FVector2D
```

Returns Vector A subtracted by B

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `EqualEqual_Vector2DVector2D`

```text
EqualEqual_Vector2DVector2D(A: FVector2D, B: FVector2D, ErrorTolerance: float) -> bool
```

Returns true if vector2D A is equal to vector2D B (A == B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |
| `ErrorTolerance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_Vector2DVector2D`

```text
NotEqual_Vector2DVector2D(A: FVector2D, B: FVector2D, ErrorTolerance: float) -> bool
```

Returns true if vector2D A is not equal to vector2D B (A != B) within a specified error tolerance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FVector2D` | - |
| `B` | `FVector2D` | - |
| `ErrorTolerance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FInterpTo`

```text
FInterpTo(Current: float, Target: float, DeltaTime: float, InterpSpeed: float) -> float
```

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `float` | Actual position |
| `Target` | `float` | Target position |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `float` | New interpolated position |

### `FInterpTo_Constant`

```text
FInterpTo_Constant(Current: float, Target: float, DeltaTime: float, InterpSpeed: float) -> float
```

Tries to reach Target at a constant rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `float` | Actual position |
| `Target` | `float` | Target position |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `float` | New interpolated position |

### `VInterpTo`

```text
VInterpTo(Current: FVector, Target: FVector, DeltaTime: float, InterpSpeed: float) -> FVector
```

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector` | Actual position |
| `Target` | `FVector` | Target position |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `FVector` | New interpolated position |

### `VInterpTo_Constant`

```text
VInterpTo_Constant(Current: FVector, Target: FVector, DeltaTime: float, InterpSpeed: float) -> FVector
```

Tries to reach Target at a constant rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector` | Actual position |
| `Target` | `FVector` | Target position |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `FVector` | New interpolated position |

### `Vector2DInterpTo`

```text
Vector2DInterpTo(Current: FVector2D, Target: FVector2D, DeltaTime: float, InterpSpeed: float) -> FVector2D
```

Tries to reach Target based on distance from Current position, giving a nice smooth feeling when tracking a position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector2D` | Actual position |
| `Target` | `FVector2D` | Target position |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | New interpolated position |

### `Vector2DInterpTo_Constant`

```text
Vector2DInterpTo_Constant(Current: FVector2D, Target: FVector2D, DeltaTime: float, InterpSpeed: float) -> FVector2D
```

Tries to reach Target at a constant rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector2D` | Actual position |
| `Target` | `FVector2D` | Target position |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | New interpolated position |

### `RInterpTo`

```text
RInterpTo(Current: FRotator, Target: FRotator, DeltaTime: float, InterpSpeed: float) -> FRotator
```

Tries to reach Target rotation based on Current rotation, giving a nice smooth feeling when rotating to Target rotation.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FRotator` | Actual rotation |
| `Target` | `FRotator` | Target rotation |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | New interpolated position |

### `RInterpTo_Constant`

```text
RInterpTo_Constant(Current: FRotator, Target: FRotator, DeltaTime: float, InterpSpeed: float) -> FRotator
```

Tries to reach Target rotation at a constant rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FRotator` | Actual rotation |
| `Target` | `FRotator` | Target rotation |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | New interpolated position |

### `CInterpTo`

```text
CInterpTo(Current: FLinearColor, Target: FLinearColor, DeltaTime: float, InterpSpeed: float) -> FLinearColor
```

Interpolates towards a varying target color smoothly.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FLinearColor` | Current Color |
| `Target` | `FLinearColor` | Target Color |
| `DeltaTime` | `float` | Time since last tick |
| `InterpSpeed` | `float` | Interpolation speed |

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | New interpolated Color |

### `FloatSpringInterp`

```text
FloatSpringInterp(Current: float, Target: float, SpringState: FFloatSpringState &, Stiffness: float, CriticalDampingFactor: float, DeltaTime: float, Mass: float) -> float
```

Uses a simple spring model to interpolate a float from Current to Target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `float` | Current value |
| `Target` | `float` | Target value |
| `SpringState` | `FFloatSpringState &` | Data related to spring model (velocity, error, etc..) - Create a unique variable per spring |
| `Stiffness` | `float` | How stiff the spring model is (more stiffness means more oscillation around the target value) |
| `CriticalDampingFactor` | `float` | How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation) |
| `DeltaTime` | `float` | - |
| `Mass` | `float` | Multiplier that acts like mass on a spring |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `VectorSpringInterp`

```text
VectorSpringInterp(Current: FVector, Target: FVector, SpringState: FVectorSpringState &, Stiffness: float, CriticalDampingFactor: float, DeltaTime: float, Mass: float) -> FVector
```

Uses a simple spring model to interpolate a vector from Current to Target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Current` | `FVector` | Current value |
| `Target` | `FVector` | Target value |
| `SpringState` | `FVectorSpringState &` | Data related to spring model (velocity, error, etc..) - Create a unique variable per spring |
| `Stiffness` | `float` | How stiff the spring model is (more stiffness means more oscillation around the target value) |
| `CriticalDampingFactor` | `float` | How much damping to apply to the spring (0 means no damping, 1 means critically damped which means no oscillation) |
| `DeltaTime` | `float` | - |
| `Mass` | `float` | Multiplier that acts like mass on a spring |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `ResetFloatSpringState`

```text
ResetFloatSpringState(SpringState: FFloatSpringState &) -> void
```

Resets the state of a given spring

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpringState` | `FFloatSpringState &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetVectorSpringState`

```text
ResetVectorSpringState(SpringState: FVectorSpringState &) -> void
```

Resets the state of a given spring

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SpringState` | `FVectorSpringState &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RandomIntegerFromStream`

```text
RandomIntegerFromStream(Max: int32, Stream: FRandomStream &) -> int32
```

Returns a uniformly distributed random number between 0 and Max - 1

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Max` | `int32` | - |
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RandomIntegerInRangeFromStream`

```text
RandomIntegerInRangeFromStream(Min: int32, Max: int32, Stream: FRandomStream &) -> int32
```

Return a random integer between Min and Max (>= Min and <= Max)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `int32` | - |
| `Max` | `int32` | - |
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `RandomBoolFromStream`

```text
RandomBoolFromStream(Stream: FRandomStream &) -> bool
```

Returns a random bool

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RandomFloatFromStream`

```text
RandomFloatFromStream(Stream: FRandomStream &) -> float
```

Returns a random float between 0 and 1

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `RandomFloatInRangeFromStream`

```text
RandomFloatInRangeFromStream(Min: float, Max: float, Stream: FRandomStream &) -> float
```

Generate a random number between Min and Max

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Min` | `float` | - |
| `Max` | `float` | - |
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `RandomUnitVectorFromStream`

```text
RandomUnitVectorFromStream(Stream: FRandomStream &) -> FVector
```

Returns a random vector with length of 1.0

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomRotatorFromStream`

```text
RandomRotatorFromStream(bRoll: bool, Stream: FRandomStream &) -> FRotator
```

Create a random rotation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bRoll` | `bool` | - |
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `ResetRandomStream`

```text
ResetRandomStream(Stream: FRandomStream &) -> void
```

Reset a random stream

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SeedRandomStream`

```text
SeedRandomStream(Stream: FRandomStream &) -> void
```

Create a new random seed for a random stream

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Stream` | `FRandomStream &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRandomStreamSeed`

```text
SetRandomStreamSeed(Stream: FRandomStream &, NewSeed: int32) -> void
```

Set the seed of a random stream to a specific number

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Stream` | `FRandomStream &` | - |
| `NewSeed` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RandomUnitVectorInConeInRadiansFromStream`

```text
RandomUnitVectorInConeInRadiansFromStream(ConeDir: FVector &, ConeHalfAngleInRadians: float, Stream: FRandomStream &) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector &` | The base "center" direction of the cone. |
| `ConeHalfAngleInRadians` | `float` | The half-angle of the cone (from ConeDir to edge), in radians. |
| `Stream` | `FRandomStream &` | The random stream from which to obtain the vector. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomUnitVectorInConeInDegreesFromStream`

```text
RandomUnitVectorInConeInDegreesFromStream(ConeDir: FVector &, ConeHalfAngleInDegrees: float, Stream: FRandomStream &) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector &` | The base "center" direction of the cone. |
| `ConeHalfAngleInDegrees` | `float` | The half-angle of the cone (from ConeDir to edge), in degrees. |
| `Stream` | `FRandomStream &` | The random stream from which to obtain the vector. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomUnitVectorInEllipticalConeInRadiansFromStream`

```text
RandomUnitVectorInEllipticalConeInRadiansFromStream(ConeDir: FVector &, MaxYawInRadians: float, MaxPitchInRadians: float, Stream: FRandomStream &) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector &` | - |
| `MaxYawInRadians` | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in radians. |
| `MaxPitchInRadians` | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in radians. |
| `Stream` | `FRandomStream &` | The random stream from which to obtain the vector. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `RandomUnitVectorInEllipticalConeInDegreesFromStream`

```text
RandomUnitVectorInEllipticalConeInDegreesFromStream(ConeDir: FVector &, MaxYawInDegrees: float, MaxPitchInDegrees: float, Stream: FRandomStream &) -> FVector
```

Returns a random vector with length of 1, within the specified cone, with uniform random distribution.
	 The shape of the cone can be modified according to the yaw and pitch angles.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConeDir` | `FVector &` | - |
| `MaxYawInDegrees` | `float` | The yaw angle of the cone (from ConeDir to horizontal edge), in degrees. |
| `MaxPitchInDegrees` | `float` | The pitch angle of the cone (from ConeDir to vertical edge), in degrees. |
| `Stream` | `FRandomStream &` | The random stream from which to obtain the vector. |

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `MinimumAreaRectangle`

```text
MinimumAreaRectangle(WorldContextObject: UObject *, InVerts: TArray < FVector > &, SampleSurfaceNormal: FVector &, OutRectCenter: FVector &, OutRectRotation: FRotator &, OutSideLengthX: float &, OutSideLengthY: float &, bDebugDraw: bool) -> void
```

Finds the minimum area rectangle that encloses all of the points in InVerts

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `InVerts` | `TArray < FVector > &` | - Points to enclose in the rectangle |
| `SampleSurfaceNormal` | `FVector &` | - |
| `OutRectCenter` | `FVector &` | - |
| `OutRectRotation` | `FRotator &` | - |
| `OutSideLengthX` | `float &` | - |
| `OutSideLengthY` | `float &` | - |
| `bDebugDraw` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PointsAreCoplanar`

```text
PointsAreCoplanar(Points: TArray < FVector > &, Tolerance: float) -> bool
```

Determines whether a given set of points are coplanar, with a tolerance. Any three points or less are always coplanar.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Points` | `TArray < FVector > &` | - The set of points to determine coplanarity for. |
| `Tolerance` | `float` | - Larger numbers means more variance is allowed. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the points are relatively coplanar, based on the tolerance |

### `IsPointInBox`

```text
IsPointInBox(Point: FVector, BoxOrigin: FVector, BoxExtent: FVector) -> bool
```

Determines whether the given point is in a box. Includes points on the box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point to test |
| `BoxOrigin` | `FVector` | Origin of the box |
| `BoxExtent` | `FVector` | Extents of the box (distance in each axis from origin) |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the point is in the box. |

### `IsPointInBoxWithTransform`

```text
IsPointInBoxWithTransform(Point: FVector, BoxWorldTransform: FTransform &, BoxExtent: FVector) -> bool
```

Determines whether a given point is in a box with a given transform. Includes points on the box.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Point` | `FVector` | Point to test |
| `BoxWorldTransform` | `FTransform &` | Component-to-World transform of the box. |
| `BoxExtent` | `FVector` | Extents of the box (distance in each axis from origin), in component space. |

**Returns**

| Type | Description |
|---|---|
| `bool` | Whether the point is in the box. |

### `LinePlaneIntersection`

```text
LinePlaneIntersection(LineStart: FVector &, LineEnd: FVector &, APlane: FPlane &, T: float &, Intersection: FVector &) -> bool
```

Computes the intersection point between a line and a plane.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LineStart` | `FVector &` | - |
| `LineEnd` | `FVector &` | - |
| `APlane` | `FPlane &` | - |
| `T` | `float &` | - The t of the intersection between the line and the plane |
| `Intersection` | `FVector &` | - The point of intersection between the line and the plane |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the intersection test was successful. |

### `LinePlaneIntersection_OriginNormal`

```text
LinePlaneIntersection_OriginNormal(LineStart: FVector &, LineEnd: FVector &, PlaneOrigin: FVector, PlaneNormal: FVector, T: float &, Intersection: FVector &) -> bool
```

Computes the intersection point between a line and a plane.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LineStart` | `FVector &` | - |
| `LineEnd` | `FVector &` | - |
| `PlaneOrigin` | `FVector` | - |
| `PlaneNormal` | `FVector` | - |
| `T` | `float &` | - The t of the intersection between the line and the plane |
| `Intersection` | `FVector &` | - The point of intersection between the line and the plane |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the intersection test was successful. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetMetaDataLibrary.json -->

# UKismetMetaDataLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `HasMetaData`

```text
HasMetaData(Field: UField *, Key: FName, NameIndex: int32) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Field` | `UField *` | - |
| `Key` | `FName` | - |
| `NameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetMetaData`

```text
GetMetaData(Field: UField *, Key: FName, NameIndex: int32) -> const FString &
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Field` | `UField *` | - |
| `Key` | `FName` | - |
| `NameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `const FString &` | - |

### `GetEnum`

```text
GetEnum(EnumProperty: UEnumProperty *) -> UEnum *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EnumProperty` | `UEnumProperty *` | - |

**Returns**

| Type | Description |
|---|---|
| `UEnum *` | - |

### `GetEnumFromByte`

```text
GetEnumFromByte(ByteProperty: UByteProperty *) -> UEnum *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ByteProperty` | `UByteProperty *` | - |

**Returns**

| Type | Description |
|---|---|
| `UEnum *` | - |

### `GetNumOfEnum`

```text
GetNumOfEnum(Enum: UEnum *) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetEnumName`

```text
GetEnumName(Enum: UEnum *, NameIndex: int32) -> FName
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - |
| `NameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `GetEnumValue`

```text
GetEnumValue(Enum: UEnum *, NameIndex: int32) -> int64
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - |
| `NameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `GetEnumIndexByValue`

```text
GetEnumIndexByValue(Enum: UEnum *, Value: int64) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Enum` | `UEnum *` | - |
| `Value` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetScriptStructOfStructProperty`

```text
GetScriptStructOfStructProperty(StructProperty: UStructProperty *) -> UScriptStruct *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StructProperty` | `UStructProperty *` | - |

**Returns**

| Type | Description |
|---|---|
| `UScriptStruct *` | - |

### `GetClassOfObjectPropertyBase`

```text
GetClassOfObjectPropertyBase(ObjectPropertyBase: UObjectPropertyBase *) -> UClass *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectPropertyBase` | `UObjectPropertyBase *` | - |

**Returns**

| Type | Description |
|---|---|
| `UClass *` | - |

### `GetObjectsWithOuter`

```text
GetObjectsWithOuter(Outer: UObject *, bIncludeNestedObjects: bool, ExclusionFlags: int32, ExclusionInternalFlags: int32) -> TArray < UObject * >
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Outer` | `UObject *` | - |
| `bIncludeNestedObjects` | `bool` | - |
| `ExclusionFlags` | `int32` | - |
| `ExclusionInternalFlags` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < UObject * >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetNodeHelperLibrary.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetPackageNameLibrary.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetRenderingLibrary.json -->

# UKismetRenderingLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `ClearRenderTarget2D`

```text
ClearRenderTarget2D(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, ClearColor: FLinearColor) -> ENGINE_API void
```

Clears the specified render target with the given ClearColor.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `ClearColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `CreateRenderTarget2D`

```text
CreateRenderTarget2D(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

### `CreateRenderTarget2DExt`

```text
CreateRenderTarget2DExt(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat, ClearColor: FLinearColor &) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |
| `ClearColor` | `FLinearColor &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

### `CreateRenderTarget2DWithFilter`

```text
CreateRenderTarget2DWithFilter(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat, Filter: TextureFilter) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |
| `Filter` | `TextureFilter` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

### `ReleaseRenderTarget2D`

```text
ReleaseRenderTarget2D(TextureRenderTarget: UTextureRenderTarget2D *) -> ENGINE_API void
```

Manually releases GPU resources of a render target. This is useful for blueprint creating a lot of render target that would
	  normally be released too late by the garbage collector that can be problematic on platforms that have tight GPU memory constrains.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `DrawMaterialToRenderTarget`

```text
DrawMaterialToRenderTarget(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, Material: UMaterialInterface *) -> ENGINE_API void
```

Renders a quad with the material applied to the specified render target.   
	  This sets the render target even if it is already set, which is an expensive operation. 
	  Use BeginDrawCanvasToRenderTarget  EndDrawCanvasToRenderTarget instead if rendering multiple primitives to the same render target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `Material` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `RenderTargetCreateStaticTexture2DEditorOnly`

```text
RenderTargetCreateStaticTexture2DEditorOnly(RenderTarget: UTextureRenderTarget2D *, Name: FString, CompressionSettings: TextureCompressionSettings, MipSettings: TextureMipGenSettings) -> ENGINE_API UTexture2D *
```

Creates a new Static Texture from a Render Target 2D. Render Target Must be power of two and use four channels.
	 Only works in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RenderTarget` | `UTextureRenderTarget2D *` | - |
| `Name` | `FString` | - |
| `CompressionSettings` | `TextureCompressionSettings` | - |
| `MipSettings` | `TextureMipGenSettings` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTexture2D *` | - |

### `ConvertRenderTargetToTexture2DEditorOnly`

```text
ConvertRenderTargetToTexture2DEditorOnly(WorldContextObject: UObject *, RenderTarget: UTextureRenderTarget2D *, Texture: UTexture2D *) -> ENGINE_API void
```

Copies the contents of a render target to a UTexture2D
	  Only works in the editor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `RenderTarget` | `UTextureRenderTarget2D *` | - |
| `Texture` | `UTexture2D *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ExportRenderTarget`

```text
ExportRenderTarget(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, FilePath: FString &, FileName: FString &) -> ENGINE_API void
```

Exports a render target as a HDR or PNG image onto the disk (depending on the format of the render target)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `FilePath` | `FString &` | - |
| `FileName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ExportTexture2D`

```text
ExportTexture2D(WorldContextObject: UObject *, Texture: UTexture2D *, FilePath: FString &, FileName: FString &) -> ENGINE_API void
```

Exports a Texture2D as a HDR image onto the disk.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Texture` | `UTexture2D *` | - |
| `FilePath` | `FString &` | - |
| `FileName` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `BeginDrawCanvasToRenderTarget`

```text
BeginDrawCanvasToRenderTarget(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, Canvas: UCanvas * &, Size: FVector2D &, Context: FDrawToRenderTargetContext &) -> ENGINE_API void
```

Returns a Canvas object that can be used to draw to the specified render target.
	  Canvas has functions like DrawMaterial with size parameters that can be used to draw to a specific area of a render target.
	  Be sure to call EndDrawCanvasToRenderTarget to complete the rendering!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `Canvas` | `UCanvas * &` | - |
| `Size` | `FVector2D &` | - |
| `Context` | `FDrawToRenderTargetContext &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `EndDrawCanvasToRenderTarget`

```text
EndDrawCanvasToRenderTarget(WorldContextObject: UObject *, Context: FDrawToRenderTargetContext &) -> ENGINE_API void
```

Must be paired with a BeginDrawCanvasToRenderTarget to complete rendering to a render target.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Context` | `FDrawToRenderTargetContext &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `MakeSkinWeightInfo`

```text
MakeSkinWeightInfo(Bone0: int32, Weight0: uint8, Bone1: int32, Weight1: uint8, Bone2: int32, Weight2: uint8, Bone3: int32, Weight3: uint8) -> ENGINE_API FSkelMeshSkinWeightInfo
```

Create FSkelMeshSkinWeightInfo

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bone0` | `int32` | - |
| `Weight0` | `uint8` | - |
| `Bone1` | `int32` | - |
| `Weight1` | `uint8` | - |
| `Bone2` | `int32` | - |
| `Weight2` | `uint8` | - |
| `Bone3` | `int32` | - |
| `Weight3` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FSkelMeshSkinWeightInfo` | - |

### `BreakSkinWeightInfo`

```text
BreakSkinWeightInfo(InWeight: FSkelMeshSkinWeightInfo, Bone0: int32 &, Weight0: uint8 &, Bone1: int32 &, Weight1: uint8 &, Bone2: int32 &, Weight2: uint8 &, Bone3: int32 &, Weight3: uint8 &) -> ENGINE_API void
```

Break FSkelMeshSkinWeightInfo

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InWeight` | `FSkelMeshSkinWeightInfo` | - |
| `Bone0` | `int32 &` | - |
| `Weight0` | `uint8 &` | - |
| `Bone1` | `int32 &` | - |
| `Weight1` | `uint8 &` | - |
| `Bone2` | `int32 &` | - |
| `Weight2` | `uint8 &` | - |
| `Bone3` | `int32 &` | - |
| `Weight3` | `uint8 &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ReadRenderTargetRawPixel`

```text
ReadRenderTargetRawPixel(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, X: int32, Y: int32) -> ENGINE_API FLinearColor
```

Incredibly inefficient and slow operation! Read a value as-is from a render target using integer pixel coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `X` | `int32` | - |
| `Y` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FLinearColor` | - |

### `ReadRenderTargetRawUV`

```text
ReadRenderTargetRawUV(WorldContextObject: UObject *, TextureRenderTarget: UTextureRenderTarget2D *, U: float, V: float) -> ENGINE_API FLinearColor
```

Incredibly inefficient and slow operation! Read a value as-is color from a render target using UV [0,1]x[0,1] coordinates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `TextureRenderTarget` | `UTextureRenderTarget2D *` | - |
| `U` | `float` | - |
| `V` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FLinearColor` | - |

### `NeedsToSwitchVerticalAxis`

```text
NeedsToSwitchVerticalAxis() -> ENGINE_API bool
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `SetCastInsetShadowForAllAttachments`

```text
SetCastInsetShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, bCastInsetShadow: bool, bLightAttachmentsAsGroup: bool) -> ENGINE_API void
```

Set the inset shadow casting state of the given component and all its child attachments.
	 	Also choose if all attachments should be grouped for the inset shadow rendering. If enabled, one depth target will be shared for all attachments.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `bCastInsetShadow` | `bool` | - |
| `bLightAttachmentsAsGroup` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetupFPPShadowForAllAttachments`

```text
SetupFPPShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `SetupTPPShadowForAllAttachments`

```text
SetupTPPShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ResetShadowForAllAttachments`

```text
ResetShadowForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `RecordForAllAttachments`

```text
RecordForAllAttachments(WorldContextObject: UObject *, PrimitiveComponent: UPrimitiveComponent *, ChangeRecords: TArray < FFppTppShadowChangeRecord > &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PrimitiveComponent` | `UPrimitiveComponent *` | - |
| `ChangeRecords` | `TArray < FFppTppShadowChangeRecord > &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `GetScalabilityQualityLevels`

```text
GetScalabilityQualityLevels() -> ENGINE_API FScalabilityQuality
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FScalabilityQuality` | - |

### `ApplyMaxScalabilityQualityLevels`

```text
ApplyMaxScalabilityQualityLevels() -> ENGINE_API void
```

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `ApplyScalabilityQualityLevels`

```text
ApplyScalabilityQualityLevels(QualityLevels: FScalabilityQuality &) -> ENGINE_API void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityLevels` | `FScalabilityQuality &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

### `CreateRenderTarget2D`

```text
CreateRenderTarget2D(WorldContextObject: UObject *, Width: int32, Height: int32, Format: ETextureRenderTargetFormat, bAutoGenerateMipmap: bool) -> ENGINE_API UTextureRenderTarget2D *
```

Creates a new render target and initializes it to the specified dimensions

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `Width` | `int32` | - |
| `Height` | `int32` | - |
| `Format` | `ETextureRenderTargetFormat` | - |
| `bAutoGenerateMipmap` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API UTextureRenderTarget2D *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetStringLibrary.json -->

# UKismetStringLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Conv_FloatToString`

```text
Conv_FloatToString(InFloat: float) -> FString
```

Converts a float value to a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFloat` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_IntToString`

```text
Conv_IntToString(InInt: int32) -> FString
```

Converts an integer value to a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_Int64ToString`

```text
Conv_Int64ToString(InInt64: int64) -> FString
```

Converts an integer64 value to a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InInt64` | `int64` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_UInt64ToString`

```text
Conv_UInt64ToString(InUInt64: uint64) -> FString
```

Converts an uinteger64 value to a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InUInt64` | `uint64` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_ByteToString`

```text
Conv_ByteToString(InByte: uint8) -> FString
```

Converts a byte value to a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InByte` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_BoolToString`

```text
Conv_BoolToString(InBool: bool) -> FString
```

Converts a boolean value to a string, either 'true' or 'false'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_VectorToString`

```text
Conv_VectorToString(InVec: FVector) -> FString
```

Converts a vector value to a string, in the form 'X= Y= Z='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_IntVectorToString`

```text
Conv_IntVectorToString(InIntVec: FIntVector) -> FString
```

Converts an IntVector value to a string, in the form 'X= Y= Z='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIntVec` | `FIntVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_Vector2dToString`

```text
Conv_Vector2dToString(InVec: FVector2D) -> FString
```

Converts a vector2d value to a string, in the form 'X= Y='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_RotatorToString`

```text
Conv_RotatorToString(InRot: FRotator) -> FString
```

Converts a rotator value to a string, in the form 'P= Y= R='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_TransformToString`

```text
Conv_TransformToString(InTrans: FTransform &) -> FString
```

Converts a transform value to a string, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTrans` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_ObjectToString`

```text
Conv_ObjectToString(InObj: UObject *) -> FString
```

Converts a UObject value to a string by calling the object's GetName method

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObj` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_ColorToString`

```text
Conv_ColorToString(InColor: FLinearColor) -> FString
```

Converts a linear color value to a string, in the form '(R=,G=,B=,A=)'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_DateTimeToString`

```text
Conv_DateTimeToString(InDateTime: FDateTime) -> FString
```

Converts a date time value to a string, in the form '%Y.%m.%d-%H.%M.%S'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDateTime` | `FDateTime` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_NameToString`

```text
Conv_NameToString(InName: FName) -> FString
```

Converts a name value to a string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_StringToName`

```text
Conv_StringToName(InString: FString &) -> FName
```

Converts a string to a name value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FName` | - |

### `Conv_StringToInt`

```text
Conv_StringToInt(InString: FString &) -> int32
```

Converts a string to a int value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `Conv_StringToInt64`

```text
Conv_StringToInt64(InString: FString &) -> int64
```

Converts a string to a int64 value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `int64` | - |

### `Conv_StringToFloat`

```text
Conv_StringToFloat(InString: FString &) -> float
```

Converts a string to a float value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `Conv_StringToVector`

```text
Conv_StringToVector(InString: FString &, OutConvertedVector: FVector &, OutIsValid: bool &) -> void
```

Convert String Back To Vector. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |
| `OutConvertedVector` | `FVector &` | - |
| `OutIsValid` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Conv_StringToVector2D`

```text
Conv_StringToVector2D(InString: FString &, OutConvertedVector2D: FVector2D &, OutIsValid: bool &) -> void
```

Convert String Back To Vector2D. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |
| `OutConvertedVector2D` | `FVector2D &` | - |
| `OutIsValid` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Conv_StringToRotator`

```text
Conv_StringToRotator(InString: FString &, OutConvertedRotator: FRotator &, OutIsValid: bool &) -> void
```

Convert String Back To Rotator. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |
| `OutConvertedRotator` | `FRotator &` | - |
| `OutIsValid` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Conv_StringToColor`

```text
Conv_StringToColor(InString: FString &, OutConvertedColor: FLinearColor &, OutIsValid: bool &) -> void
```

Convert String Back To Color. IsValid indicates whether or not the string could be successfully converted.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |
| `OutConvertedColor` | `FLinearColor &` | - |
| `OutIsValid` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `BuildString_Float`

```text
BuildString_Float(AppendTo: FString &, Prefix: FString &, InFloat: float, Suffix: FString &) -> FString
```

Converts a float->string, create a new string in the form AppendTo+Prefix+InFloat+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InFloat` | `float` | - The float value to convert |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Int`

```text
BuildString_Int(AppendTo: FString &, Prefix: FString &, InInt: int32, Suffix: FString &) -> FString
```

Converts a int->string, creating a new string in the form AppendTo+Prefix+InInt+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InInt` | `int32` | - The int value to convert |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Int64`

```text
BuildString_Int64(AppendTo: FString &, Prefix: FString &, InInt64: int64, Suffix: FString &) -> FString
```

Converts a int->string, creating a new string in the form AppendTo+Prefix+InInt+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InInt64` | `int64` | - |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Bool`

```text
BuildString_Bool(AppendTo: FString &, Prefix: FString &, InBool: bool, Suffix: FString &) -> FString
```

Converts a boolean->string, creating a new string in the form AppendTo+Prefix+InBool+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InBool` | `bool` | - The bool value to convert. Will add "true" or "false" to the conversion string |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Vector`

```text
BuildString_Vector(AppendTo: FString &, Prefix: FString &, InVector: FVector, Suffix: FString &) -> FString
```

Converts a vector->string, creating a new string in the form AppendTo+Prefix+InVector+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InVector` | `FVector` | - The vector value to convert. Uses the standard FVector::ToString conversion |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_IntVector`

```text
BuildString_IntVector(AppendTo: FString &, Prefix: FString &, InIntVector: FIntVector, Suffix: FString &) -> FString
```

Converts an IntVector->string, creating a new string in the form AppendTo+Prefix+InIntVector+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InIntVector` | `FIntVector` | - The intVector value to convert. Uses the standard FVector::ToString conversion |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Vector2d`

```text
BuildString_Vector2d(AppendTo: FString &, Prefix: FString &, InVector2d: FVector2D, Suffix: FString &) -> FString
```

Converts a vector2d->string, creating a new string in the form AppendTo+Prefix+InVector2d+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InVector2d` | `FVector2D` | - The vector2d value to convert. Uses the standard FVector2D::ToString conversion |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Rotator`

```text
BuildString_Rotator(AppendTo: FString &, Prefix: FString &, InRot: FRotator, Suffix: FString &) -> FString
```

Converts a rotator->string, creating a new string in the form AppendTo+Prefix+InRot+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InRot` | `FRotator` | - The rotator value to convert. Uses the standard ToString conversion |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Object`

```text
BuildString_Object(AppendTo: FString &, Prefix: FString &, InObj: UObject *, Suffix: FString &) -> FString
```

Converts a object->string, creating a new string in the form AppendTo+Prefix+object name+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InObj` | `UObject *` | - The object to convert. Will insert the name of the object into the conversion string |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Color`

```text
BuildString_Color(AppendTo: FString &, Prefix: FString &, InColor: FLinearColor, Suffix: FString &) -> FString
```

Converts a color->string, creating a new string in the form AppendTo+Prefix+InColor+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InColor` | `FLinearColor` | - The linear color value to convert. Uses the standard ToString conversion |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `BuildString_Name`

```text
BuildString_Name(AppendTo: FString &, Prefix: FString &, InName: FName, Suffix: FString &) -> FString
```

Converts a color->string, creating a new string in the form AppendTo+Prefix+InName+Suffix

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AppendTo` | `FString &` | - An existing string to use as the start of the conversion string |
| `Prefix` | `FString &` | - A string to use as a prefix, after the AppendTo string |
| `InName` | `FName` | - The name value to convert |
| `Suffix` | `FString &` | - A suffix to append to the end of the conversion string |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string built from the passed parameters |

### `Concat_StrStr`

```text
Concat_StrStr(A: FString &, B: FString &) -> FString
```

Concatenates two strings together to make a new string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FString &` | - The original string |
| `B` | `FString &` | - The string to append to A |

**Returns**

| Type | Description |
|---|---|
| `FString` | A new string which is the concatenation of A+B |

### `EqualEqual_StrStr`

```text
EqualEqual_StrStr(A: FString &, B: FString &) -> bool
```

Test if the input strings are equal (A == B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FString &` | - The string to compare against |
| `B` | `FString &` | - The string to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the strings are equal, false otherwise |

### `EqualEqual_StriStri`

```text
EqualEqual_StriStri(A: FString &, B: FString &) -> bool
```

Test if the input strings are equal (A == B), ignoring case

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FString &` | - The string to compare against |
| `B` | `FString &` | - The string to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the strings are equal, false otherwise |

### `NotEqual_StrStr`

```text
NotEqual_StrStr(A: FString &, B: FString &) -> bool
```

Test if the input string are not equal (A != B)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FString &` | - The string to compare against |
| `B` | `FString &` | - The string to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns true if the input strings are not equal, false if they are equal |

### `NotEqual_StriStri`

```text
NotEqual_StriStri(A: FString &, B: FString &) -> bool
```

Test if the input string are not equal (A != B), ignoring case differences

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FString &` | - The string to compare against |
| `B` | `FString &` | - The string to compare |

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns true if the input strings are not equal, false if they are equal |

### `Len`

```text
Len(S: FString &) -> int32
```

Returns the number of characters in the string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `S` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of chars in the string |

### `GetSubstring`

```text
GetSubstring(SourceString: FString &, StartIndex: int32, Length: int32) -> FString
```

Returns a substring from the string starting at the specified position

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - The string to get the substring from |
| `StartIndex` | `int32` | - The location in SourceString to use as the start of the substring |
| `Length` | `int32` | The length of the requested substring |

**Returns**

| Type | Description |
|---|---|
| `FString` | The requested substring |

### `FindSubstring`

```text
FindSubstring(SearchIn: FString &, Substring: FString &, bUseCase: bool, bSearchFromEnd: bool, StartPosition: int32) -> int32
```

Finds the starting index of a substring in the a specified string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SearchIn` | `FString &` | The string to search within |
| `Substring` | `FString &` | The string to look for in the SearchIn string |
| `bUseCase` | `bool` | Whether or not to be case-sensitive |
| `bSearchFromEnd` | `bool` | Whether or not to start the search from the end of the string instead of the beginning |
| `StartPosition` | `int32` | The position to start the search from |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index (starting from 0 if bSearchFromEnd is false) of the first occurence of the substring |

### `Contains`

```text
Contains(SearchIn: FString &, Substring: FString &, bUseCase: bool, bSearchFromEnd: bool) -> bool
```

Returns whether this string contains the specified substring.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SearchIn` | `FString &` | - |
| `Substring` | `FString &` | - |
| `bUseCase` | `bool` | - |
| `bSearchFromEnd` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | Returns whether the string contains the substring |

### `GetCharacterAsNumber`

```text
GetCharacterAsNumber(SourceString: FString &, Index: int32) -> int32
```

Gets a single character from the string (as an integer)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - The string to convert |
| `Index` | `int32` | - Location of the character whose value is required |

**Returns**

| Type | Description |
|---|---|
| `int32` | The integer value of the character or 0 if index is out of range |

### `ParseIntoArray`

```text
ParseIntoArray(SourceString: FString &, Delimiter: FString &, CullEmptyStrings: bool) -> TArray < FString >
```

Gets an array of strings from a source string divided up by a separator and empty strings can optionally be culled.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - The string to chop up |
| `Delimiter` | `FString &` | - The string to delimit on |
| `CullEmptyStrings` | `bool` | = true - Cull (true) empty strings or add them to the array (false) |

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | The array of string that have been separated |

### `JoinStringArray`

```text
JoinStringArray(SourceArray: TArray < FString > &, Separator: FString &) -> FString
```

Concatenates an array of strings into a single string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceArray` | `TArray < FString > &` | - The array of strings to concatenate. |
| `Separator` | `FString &` | - The string used to separate each element. |

**Returns**

| Type | Description |
|---|---|
| `FString` | The final, joined, separated string. |

### `GetCharacterArrayFromString`

```text
GetCharacterArrayFromString(SourceString: FString &) -> TArray < FString >
```

Returns an array that contains one entry for each character in SourceString

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | The string to break apart into characters |

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | An array containing one entry for each character in SourceString |

### `ToUpper`

```text
ToUpper(SourceString: FString &) -> FString
```

Returns a string converted to Upper case

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | The string to convert |

**Returns**

| Type | Description |
|---|---|
| `FString` | The string in upper case |

### `ToLower`

```text
ToLower(SourceString: FString &) -> FString
```

Returns a string converted to Lower case

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | The string to convert |

**Returns**

| Type | Description |
|---|---|
| `FString` | The string in lower case |

### `LeftPad`

```text
LeftPad(SourceString: FString &, ChCount: int32) -> FString
```

Pad the left of this string for a specified number of characters

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | The string to pad |
| `ChCount` | `int32` | Amount of padding required |

**Returns**

| Type | Description |
|---|---|
| `FString` | The padded string |

### `RightPad`

```text
RightPad(SourceString: FString &, ChCount: int32) -> FString
```

Pad the right of this string for a specified number of characters

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | The string to pad |
| `ChCount` | `int32` | Amount of padding required |

**Returns**

| Type | Description |
|---|---|
| `FString` | The padded string |

### `IsNumeric`

```text
IsNumeric(SourceString: FString &) -> bool
```

Checks if a string contains only numeric characters

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | The string to check |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the string only contains numeric characters |

### `StartsWith`

```text
StartsWith(SourceString: FString &, InPrefix: FString &, SearchCase: ESearchCase :: Type) -> bool
```

Test whether this string starts with given string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `InPrefix` | `FString &` | - |
| `SearchCase` | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this string begins with specified text, false otherwise |

### `EndsWith`

```text
EndsWith(SourceString: FString &, InSuffix: FString &, SearchCase: ESearchCase :: Type) -> bool
```

Test whether this string ends with given string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `InSuffix` | `FString &` | - |
| `SearchCase` | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this string ends with specified text, false otherwise |

### `MatchesWildcard`

```text
MatchesWildcard(SourceString: FString &, Wildcard: FString &, SearchCase: ESearchCase :: Type) -> bool
```

Searches this string for a given wild card

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `Wildcard` | `FString &` | ?-type wildcard |
| `SearchCase` | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if this string matches the ?-type wildcard given. |

### `Trim`

```text
Trim(SourceString: FString &) -> FString
```

Removes whitespace characters from the front of this string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `TrimTrailing`

```text
TrimTrailing(SourceString: FString &) -> FString
```

Removes trailing whitespace characters

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `CullArray`

```text
CullArray(SourceString: FString &, InArray: TArray < FString > &) -> int32
```

Takes an array of strings and removes any zero length entries.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `InArray` | `TArray < FString > &` | The array to cull |

**Returns**

| Type | Description |
|---|---|
| `int32` | The number of elements left in InArray |

### `Reverse`

```text
Reverse(SourceString: FString &) -> FString
```

Returns a copy of this string, with the characters in reverse order

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Replace`

```text
Replace(SourceString: FString &, From: FString &, To: FString &, SearchCase: ESearchCase :: Type) -> FString
```

Replace all occurrences of a substring in this string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `From` | `FString &` | substring to replace |
| `To` | `FString &` | substring to replace From with |
| `SearchCase` | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Returns**

| Type | Description |
|---|---|
| `FString` | a copy of this string with the replacement made |

### `ReplaceInline`

```text
ReplaceInline(SourceString: FString &, SearchText: FString &, ReplacementText: FString &, SearchCase: ESearchCase :: Type) -> int32
```

Replace all occurrences of SearchText with ReplacementText in this string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `SearchText` | `FString &` | the text that should be removed from this string |
| `ReplacementText` | `FString &` | the text to insert in its place |
| `SearchCase` | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |

**Returns**

| Type | Description |
|---|---|
| `int32` | the number of occurrences of SearchText that were replaced. |

### `Split`

```text
Split(SourceString: FString &, InStr: FString &, LeftS: FString &, RightS: FString &, SearchCase: ESearchCase :: Type, SearchDir: ESearchDir :: Type) -> bool
```

Splits this string at given string position case sensitive.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `InStr` | `FString &` | The string to search and split at |
| `LeftS` | `FString &` | out the string to the left of InStr, not updated if return is false |
| `RightS` | `FString &` | out the string to the right of InStr, not updated if return is false |
| `SearchCase` | `ESearchCase :: Type` | Indicates whether the search is case sensitive or not ( defaults to ESearchCase::IgnoreCase ) |
| `SearchDir` | `ESearchDir :: Type` | Indicates whether the search starts at the begining or at the end ( defaults to ESearchDir::FromStart ) |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if string is split, otherwise false |

### `Left`

```text
Left(SourceString: FString &, Count: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `Count` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the left most given number of characters |

### `LeftChop`

```text
LeftChop(SourceString: FString &, Count: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `Count` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the left most characters from the string chopping the given number of characters from the end |

### `Right`

```text
Right(SourceString: FString &, Count: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `Count` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the string to the right of the specified location, counting back from the right (end of the word). |

### `RightChop`

```text
RightChop(SourceString: FString &, Count: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `Count` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the string to the right of the specified location, counting forward from the left (from the beginning of the word). |

### `Mid`

```text
Mid(SourceString: FString &, Start: int32, Count: int32) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SourceString` | `FString &` | - |
| `Start` | `int32` | - |
| `Count` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | the substring from Start position for Count characters. |

### `TimeSecondsToString`

```text
TimeSecondsToString(InSeconds: float) -> FString
```

Convert a number of seconds into minutes:seconds.milliseconds format string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `TimeSecondsToStringSec`

```text
TimeSecondsToStringSec(InSeconds: float) -> FString
```

Convert a number of seconds into minutes:seconds

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSeconds` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetStringTableLibrary.json -->

# UKismetStringTableLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `IsRegisteredTableId`

```text
IsRegisteredTableId(TableId: FName) -> bool
```

Returns true if the given table ID corresponds to a registered string table.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsRegisteredTableEntry`

```text
IsRegisteredTableEntry(TableId: FName, Key: FString &) -> bool
```

Returns true if the given table ID corresponds to a registered string table, and that table has.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |
| `Key` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetTableNamespace`

```text
GetTableNamespace(TableId: FName) -> FString
```

Returns the namespace of the given string table.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetTableEntrySourceString`

```text
GetTableEntrySourceString(TableId: FName, Key: FString &) -> FString
```

Returns the source string of the given string table entry (or an empty string).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |
| `Key` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetTableEntryMetaData`

```text
GetTableEntryMetaData(TableId: FName, Key: FString &, MetaDataId: FName) -> FString
```

Returns the specified meta-data of the given string table entry (or an empty string).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |
| `Key` | `FString &` | - |
| `MetaDataId` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `GetRegisteredStringTables`

```text
GetRegisteredStringTables() -> TArray < FName >
```

Returns an array of all registered string table IDs

**Returns**

| Type | Description |
|---|---|
| `TArray < FName >` | - |

### `GetKeysFromStringTable`

```text
GetKeysFromStringTable(TableId: FName) -> TArray < FString >
```

Returns an array of all keys within the given string table

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < FString >` | - |

### `GetMetaDataIdsFromStringTableEntry`

```text
GetMetaDataIdsFromStringTableEntry(TableId: FName, Key: FString &) -> TArray < FName >
```

Returns an array of all meta-data IDs within the given string table entry

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |
| `Key` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < FName >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/%E5%BC%95%E6%93%8E/%E5%B8%B8%E7%94%A8%E5%85%A8%E5%B1%80%E7%B1%BB/UKismetSystemLibrary.json -->

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


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UKismetTextLibrary.json -->

# UKismetTextLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `Conv_VectorToText`

```text
Conv_VectorToText(InVec: FVector) -> FText
```

Converts a vector value to localized formatted text, in the form 'X= Y= Z='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_Vector2dToText`

```text
Conv_Vector2dToText(InVec: FVector2D) -> FText
```

Converts a vector2d value to localized formatted text, in the form 'X= Y='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVec` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_RotatorToText`

```text
Conv_RotatorToText(InRot: FRotator) -> FText
```

Converts a rotator value to localized formatted text, in the form 'P= Y= R='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRot` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_TransformToText`

```text
Conv_TransformToText(InTrans: FTransform &) -> FText
```

Converts a transform value to localized formatted text, in the form 'Translation: X= Y= Z= Rotation: P= Y= R= Scale: X= Y= Z='

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTrans` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_ObjectToText`

```text
Conv_ObjectToText(InObj: UObject *) -> FText
```

Converts a UObject value to culture invariant text by calling the object's GetName method

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InObj` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_ColorToText`

```text
Conv_ColorToText(InColor: FLinearColor) -> FText
```

Converts a linear color value to localized formatted text, in the form '(R=,G=,B=,A=)'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_TextToString`

```text
Conv_TextToString(InText: FText &) -> FString
```

Converts localizable text to the string

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `Conv_StringToText`

```text
Conv_StringToText(InString: FString &) -> FText
```

Converts string to culture invariant text. Use Format or Make Literal Text to create localizable text

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_NameToText`

```text
Conv_NameToText(InName: FName) -> FText
```

Converts Name to culture invariant text

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `TextIsEmpty`

```text
TextIsEmpty(InText: FText &) -> bool
```

Returns true if text is empty.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TextIsTransient`

```text
TextIsTransient(InText: FText &) -> bool
```

Returns true if text is transient.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TextIsCultureInvariant`

```text
TextIsCultureInvariant(InText: FText &) -> bool
```

Returns true if text is culture invariant.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TextToLower`

```text
TextToLower(InText: FText &) -> FText
```

Transforms the text to lowercase in a culture correct way.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `TextToUpper`

```text
TextToUpper(InText: FText &) -> FText
```

Transforms the text to uppercase in a culture correct way.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `TextTrimPreceding`

```text
TextTrimPreceding(InText: FText &) -> FText
```

Removes whitespace characters from the front of the text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `TextTrimTrailing`

```text
TextTrimTrailing(InText: FText &) -> FText
```

Removes trailing whitespace characters.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `TextTrimPrecedingAndTrailing`

```text
TextTrimPrecedingAndTrailing(InText: FText &) -> FText
```

Removes whitespace characters from the front and end of the text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `GetEmptyText`

```text
GetEmptyText() -> FText
```

Returns an empty piece of text.

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `FindTextInLocalizationTable`

```text
FindTextInLocalizationTable(Namespace: FString &, Key: FString &, OutText: FText &) -> bool
```

Attempts to find existing Text using the representation found in the loc tables for the specified namespace and key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Namespace` | `FString &` | - |
| `Key` | `FString &` | - |
| `OutText` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_TextText`

```text
EqualEqual_TextText(A: FText &, B: FText &) -> bool
```

Returns true if A and B are linguistically equal (A == B).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FText &` | - |
| `B` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EqualEqual_IgnoreCase_TextText`

```text
EqualEqual_IgnoreCase_TextText(A: FText &, B: FText &) -> bool
```

Returns true if A and B are linguistically equal (A == B), ignoring case.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FText &` | - |
| `B` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_TextText`

```text
NotEqual_TextText(A: FText &, B: FText &) -> bool
```

Returns true if A and B are linguistically not equal (A != B).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FText &` | - |
| `B` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `NotEqual_IgnoreCase_TextText`

```text
NotEqual_IgnoreCase_TextText(A: FText &, B: FText &) -> bool
```

Returns true if A and B are linguistically not equal (A != B), ignoring case.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `A` | `FText &` | - |
| `B` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Conv_BoolToText`

```text
Conv_BoolToText(InBool: bool) -> FText
```

Converts a boolean value to formatted text, either 'true' or 'false'

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBool` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_ByteToText`

```text
Conv_ByteToText(Value: uint8) -> FText
```

Converts a byte value to formatted text

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `uint8` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_IntToText`

```text
Conv_IntToText(Value: int32, bUseGrouping: bool, MinimumIntegralDigits: int32, MaximumIntegralDigits: int32) -> FText
```

Converts a passed in integer to text based on formatting options

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |
| `bUseGrouping` | `bool` | - |
| `MinimumIntegralDigits` | `int32` | - |
| `MaximumIntegralDigits` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Conv_FloatToText`

```text
Conv_FloatToText(Value: float, RoundingMode: TEnumAsByte < ERoundingMode >, bUseGrouping: bool, MinimumIntegralDigits: int32, MaximumIntegralDigits: int32, MinimumFractionalDigits: int32, MaximumFractionalDigits: int32) -> FText
```

Converts a passed in float to text based on formatting options

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `RoundingMode` | `TEnumAsByte < ERoundingMode >` | - |
| `bUseGrouping` | `bool` | - |
| `MinimumIntegralDigits` | `int32` | - |
| `MaximumIntegralDigits` | `int32` | - |
| `MinimumFractionalDigits` | `int32` | - |
| `MaximumFractionalDigits` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsCurrencyBase`

```text
AsCurrencyBase(BaseValue: int32, CurrencyCode: FString &) -> FText
```

Generate an FText that represents the passed number as currency in the current culture. BaseVal is specified in the smallest fractional value of the currency and will be converted for formatting according to the selected culture. Keep in mind the CurrencyCode is completely independent of the culture it's displayed in (and they do not imply one another). For example: FText::AsCurrencyBase(650, TEXT("EUR")); would return an FText of "6.50" in most English cultures (en_USen_UK) and "6,50" in Spanish (es_ES) (where  is U+20AC)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BaseValue` | `int32` | - |
| `CurrencyCode` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsCurrency_Integer`

```text
AsCurrency_Integer(Value: int32, RoundingMode: TEnumAsByte < ERoundingMode >, bUseGrouping: bool, MinimumIntegralDigits: int32, MaximumIntegralDigits: int32, MinimumFractionalDigits: int32, MaximumFractionalDigits: int32, CurrencyCode: FString &) -> FText
```

Converts a passed in integer to a text formatted as a currency

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |
| `RoundingMode` | `TEnumAsByte < ERoundingMode >` | - |
| `bUseGrouping` | `bool` | - |
| `MinimumIntegralDigits` | `int32` | - |
| `MaximumIntegralDigits` | `int32` | - |
| `MinimumFractionalDigits` | `int32` | - |
| `MaximumFractionalDigits` | `int32` | - |
| `CurrencyCode` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsCurrency_Float`

```text
AsCurrency_Float(Value: float, RoundingMode: TEnumAsByte < ERoundingMode >, bUseGrouping: bool, MinimumIntegralDigits: int32, MaximumIntegralDigits: int32, MinimumFractionalDigits: int32, MaximumFractionalDigits: int32, CurrencyCode: FString &) -> FText
```

Converts a passed in float to a text formatted as a currency

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `RoundingMode` | `TEnumAsByte < ERoundingMode >` | - |
| `bUseGrouping` | `bool` | - |
| `MinimumIntegralDigits` | `int32` | - |
| `MaximumIntegralDigits` | `int32` | - |
| `MinimumFractionalDigits` | `int32` | - |
| `MaximumFractionalDigits` | `int32` | - |
| `CurrencyCode` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsPercent_Float`

```text
AsPercent_Float(Value: float, RoundingMode: TEnumAsByte < ERoundingMode >, bUseGrouping: bool, MinimumIntegralDigits: int32, MaximumIntegralDigits: int32, MinimumFractionalDigits: int32, MaximumFractionalDigits: int32) -> FText
```

Converts a passed in float to a text, formatted as a percent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `float` | - |
| `RoundingMode` | `TEnumAsByte < ERoundingMode >` | - |
| `bUseGrouping` | `bool` | - |
| `MinimumIntegralDigits` | `int32` | - |
| `MaximumIntegralDigits` | `int32` | - |
| `MinimumFractionalDigits` | `int32` | - |
| `MaximumFractionalDigits` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsDate_DateTime`

```text
AsDate_DateTime(InDateTime: FDateTime &) -> FText
```

Converts a passed in date & time to a text, formatted as a date using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDateTime` | `FDateTime &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsTimeZoneDate_DateTime`

```text
AsTimeZoneDate_DateTime(InDateTime: FDateTime &, InTimeZone: FString &) -> FText
```

Converts a passed in date & time to a text, formatted as a date using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDateTime` | `FDateTime &` | - |
| `InTimeZone` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsDateTime_DateTime`

```text
AsDateTime_DateTime(In: FDateTime &) -> FText
```

Converts a passed in date & time to a text, formatted as a date & time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `In` | `FDateTime &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsTimeZoneDateTime_DateTime`

```text
AsTimeZoneDateTime_DateTime(InDateTime: FDateTime &, InTimeZone: FString &) -> FText
```

Converts a passed in date & time to a text, formatted as a date & time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDateTime` | `FDateTime &` | - |
| `InTimeZone` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsTime_DateTime`

```text
AsTime_DateTime(In: FDateTime &) -> FText
```

Converts a passed in date & time to a text, formatted as a time using an invariant timezone. This will use the given date & time as-is, so it's assumed to already be in the correct timezone.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `In` | `FDateTime &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsTimeZoneTime_DateTime`

```text
AsTimeZoneTime_DateTime(InDateTime: FDateTime &, InTimeZone: FString &) -> FText
```

Converts a passed in date & time to a text, formatted as a time using the given timezone (default is the local timezone). This will convert the given date & time from UTC to the given timezone (taking into account DST).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDateTime` | `FDateTime &` | - |
| `InTimeZone` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `AsTimespan_Timespan`

```text
AsTimespan_Timespan(InTimespan: FTimespan &) -> FText
```

Converts a passed in time span to a text, formatted as a time span

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTimespan` | `FTimespan &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `Format`

```text
Format(InPattern: FText, InArgs: TArray < FFormatArgumentData >) -> FText
```

Used for formatting text using the FText::Format function and utilized by the UK2Node_FormatText

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPattern` | `FText` | - |
| `InArgs` | `TArray < FFormatArgumentData >` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

### `TextIsFromStringTable`

```text
TextIsFromStringTable(Text: FText &) -> bool
```

Returns true if the given text is referencing a string table.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `FText &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `TextFromStringTable`

```text
TextFromStringTable(TableId: FName, Key: FString &) -> FText
```

Attempts to create a text instance from a string table ID and key.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TableId` | `FName` | - |
| `Key` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `FText` | The found text, or a dummy text if the entry could not be found. |

### `StringTableIdAndKeyFromText`

```text
StringTableIdAndKeyFromText(Text: FText, OutTableId: FName &, OutKey: FString &) -> bool
```

Attempts to find the String Table ID and key used by the given text.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Text` | `FText` | - |
| `OutTableId` | `FName &` | - |
| `OutKey` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the String Table ID and key were found, false otherwise. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeAOTextureDataAsset.json -->

# ULandscapeAOTextureDataAsset

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DataSize` | `uint32` | Platform Data where don't support texture sampling in vertex buffer |
| `LandscapeAOPlatformData` | `TArray < uint8 >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeBiomesInfoObject.json -->

# ULandscapeBiomesInfoObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BiomesName` | `FName` | - |
| `LayerCount` | `int32` | - |
| `MaterialIdLayers` | `TArray < ULandscapeMaterialIdLayerInfoObject * >` | 0-255 MaterialID layers |
| `DiffuseTextureArray` | `UTexture2DArray *` | - |
| `NormalTextureArray` | `UTexture2DArray *` | - |
| `bTextureArrayDirty` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeComponent.json -->

# ULandscapeComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SectionBaseX` | `int32` | X offset from global components grid origin (in quads) |
| `SectionBaseY` | `int32` | Y offset from global components grid origin (in quads) |
| `ComponentSizeQuads` | `int32` | Total number of quads for this component, has to be >0 |
| `SubsectionSizeQuads` | `int32` | Number of quads for a subsection of the component. SubsectionSizeQuads+1 must be a power of two. |
| `NumSubsections` | `int32` | Number of subsections in X or Y axis |
| `OverrideMaterial` | `UMaterialInterface *` | - |
| `OverrideHoleMaterial` | `UMaterialInterface *` | - |
| `OverrideMaterial_ForPC` | `UMaterialInterface *` | - |
| `OverrideHoleMaterial_ForPC` | `UMaterialInterface *` | - |
| `bShouldSerializationGrassWeightDataForPC` | `bool` | - |
| `OverrideOtherMaterials` | `TMap < FName , UMaterialInterface * >` | - |
| `OverridePhyxMaterial` | `FOverridePhyxMaterial` | - |
| `bOverrideGrassTypes` | `uint8` | - |
| `GrassTypes` | `TArray < ULandscapeGrassType * >` | - |
| `bOverrideGrassTypes_ForPC` | `uint8` | - |
| `GrassTypes_ForPC` | `TArray < ULandscapeGrassType * >` | - |
| `MaterialInstances` | `TArray < UMaterialInstanceConstant * >` | - |
| `OtherMaterialInstances` | `TMap < FName , UMaterialInstanceConstant * >` | - |
| `WeightmapLayerAllocations` | `TArray < FWeightmapLayerAllocationInfo >` | List of layers, and the weightmap and channel they are stored |
| `WeightmapTextures` | `TArray < UTexture2D * >` | Weightmap texture reference |
| `SplatmapTextures` | `TArray < UTexture2D * >` | Helper to getset splatmap data, hold reference to splatmap textures |
| `SplatmapLayerAllocations` | `TArray < FSplatmapLayerAllocationInfo >` | - |
| `bUseMaterialId` | `bool` | Cached value of bUseMaterialId, should be equal to bUseMaterialId in ALandscape |
| `SplatmapG8Texture` | `UTexture2D *` | - |
| `SplatmapG16Texture` | `UTexture2D *` | - |
| `MaterialInstances_ForPC` | `TArray < UMaterialInstanceConstant * >` | - |
| `WeightmapTextures_ForPC` | `TArray < UTexture2D * >` | Weightmap texture reference |
| `VisibilityLayerChannel` | `int32` | Visibility layer channel in weightmap |
| `XYOffsetmapTexture` | `UTexture2D *` | XYOffsetmap texture reference |
| `WeightmapScaleBias` | `FVector4` | UV offset to component's weightmap data from component local coordinates |
| `WeightmapSubsectionOffset` | `float` | U or V offset into the weightmap for the first subsection, in texture UV space |
| `HeightmapScaleBias` | `FVector4` | UV offset to Heightmap data from component local coordinates |
| `HeightmapTexture` | `UTexture2D *` | Heightmap texture reference |
| `MultiVisibilityTextureData` | `TMap < FString , FVisibilityData >` | - |
| `VisibleVisibilityLayer` | `FString` | - |
| `CachedLocalBox` | `FBox` | Cached local-space bounding box, created at heightmap update time |
| `CollisionComponent` | `TLazyObjectPtr < ULandscapeHeightfieldCollisionComponent >` | Reference to associated collision component |
| `SplatmapScaleBias` | `FVector4` | UV offset to component's splatmap data from component local coordinates |
| `FarLandDiffuseTexture` | `UTexture2D *` | - |
| `FarLandNormalTexture` | `UTexture2D *` | - |
| `MapBuildDataId` | `FGuid` | Uniquely identifies this component's built map data. |
| `IrrelevantLights_DEPRECATED` | `TArray < FGuid >` | Legacy irrelevant lights |
| `CollisionMipLevel` | `int32` | Heightfield mipmap used to generate collision |
| `SimpleCollisionMipLevel` | `int32` | Heightfield mipmap used to generate simple collision |
| `NegativeZBoundsExtension` | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the negative Z axis, positive value increases bound size |
| `PositiveZBoundsExtension` | `float` | Allows overriding the landscape bounds. This is useful if you distort the landscape with world-position-offset, for example<br>	   Extension value in the positive Z axis, positive value increases bound size |
| `StaticLightingResolution` | `float` | StaticLightingResolution overriding per component, default value 0 means no overriding |
| `ForcedLOD` | `int32` | Forced LOD level to use when rendering |
| `LODBias` | `int32` | LOD level Bias to use when rendering |
| `MobileVertexHoleMaxLOD` | `int32` | The max lod level that allow landscape component to use vertex hole. If the lod level greater than this limitation, all vertex hole on landscape will vanish |
| `LODDeltaVertex` | `TArray < float >` | Subsection's Delta Vertex for fixing LOD level |
| `MaxDeltaVertex` | `float` | - |
| `StateId` | `FGuid` | - |
| `BakedTextureMaterialGuid` | `FGuid` | The Material Guid that used when baking, to detect material recompilations |
| `GIBakedBaseColorTexture` | `UTexture2D *` | Pre-baked Base Color texture for use by distance field GI |
| `FSOCOccluder` | `UFlakeOccluder *` | - |
| `MobileBlendableLayerMask` | `uint8` | For ES2 |
| `MobileMaterialInterface` | `UMaterialInterface *` | Material interface used for ES2. Serialized only when cooking or loading cooked builds. |
| `MatIDFallbackMaterialInterface` | `UMaterialInterface *` | - |
| `OtherMobileMaterialInterfaces` | `TMap < FName , UMaterialInterface * >` | - |
| `MobileWeightmapTextures` | `TArray < UTexture2D * >` | Generated weightnormal map texture used for ES2. Serialized only when cooking or loading cooked builds. |
| `MobileWeightNormalmapTexture` | `UTexture2D *` | - |
| `bMobileMultiLayers` | `uint32` | - |
| `CachedHeightData` | `TArray < uint16 >` | - |
| `CachedHaltonBaseIndex` | `TArray < bool >` | - |
| `CachedAddHaltonBaseIndexList` | `TArray < int32 >` | - |
| `bHasROCData` | `bool` | Has ROCData？ |
| `DeformHeightmap` | `UTexture2D *` | - |
| `UsedOtherMaterialName` | `FName` | - |

## Functions

### `GenerateSplatmapG16AndG8`

```text
GenerateSplatmapG16AndG8() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeGrassType.json -->

# ULandscapeGrassType

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GrassVarieties` | `TArray < FGrassVariety >` | - |
| `GrassMesh_DEPRECATED` | `UStaticMesh *` | - |
| `GrassDensity_DEPRECATED` | `float` | - |
| `PlacementJitter_DEPRECATED` | `float` | - |
| `StartCullDistance_DEPRECATED` | `int32` | - |
| `EndCullDistance_DEPRECATED` | `int32` | - |
| `RandomRotation_DEPRECATED` | `bool` | - |
| `AlignToSurface_DEPRECATED` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeHeightfieldCollisionComponent.json -->

# ULandscapeHeightfieldCollisionComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ComponentLayerInfos` | `TArray < ULandscapeLayerInfoObject * >` | List of layers painted on this component. Matches the WeightmapLayerAllocations array in the LandscapeComponent. |
| `SectionBaseX` | `int32` | Offset of component in landscape quads |
| `SectionBaseY` | `int32` | - |
| `CollisionSizeQuads` | `int32` | Size of component in collision quads |
| `CollisionScale` | `float` | Collision scale: (ComponentSizeQuads)  (CollisionSizeQuads) |
| `SimpleCollisionSizeQuads` | `int32` | Size of component's "simple collision" in collision quads |
| `CollisionQuadFlags` | `TArray < uint8 >` | The flags for each collision quad. See ECollisionQuadFlags. |
| `HeightfieldGuid` | `FGuid` | Guid used to share PhysX heightfield objects in the editor |
| `CachedLocalBox` | `FBox` | Cached local-space bounding box, created at heightmap update time |
| `RenderComponent` | `TLazyObjectPtr < ULandscapeComponent >` | Reference to render component |
| `bUseLandscapeDeform` | `bool` | - |
| `CookedPhysicalMaterials` | `TArray < UPhysicalMaterial * >` | This is a list of physical materials that is actually used by a cooked HeightField |
| `RCRLandscapeMapList` | `TArray < FString >` | - |
| `RCRCommunicatorClassName` | `FSoftClassPath` | - |
| `RCRCommunicator` | `URCRCommunicator *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeInfo.json -->

# ULandscapeInfo

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LandscapeActor` | `TLazyObjectPtr < ALandscape >` | - |
| `LandscapeGuid` | `FGuid` | - |
| `ComponentSizeQuads` | `int32` | - |
| `SubsectionSizeQuads` | `int32` | - |
| `ComponentNumSubsections` | `int32` | - |
| `DrawScale` | `FVector` | - |
| `Proxies` | `TSet < ALandscapeStreamingProxy * >` | - |
| `Layers` | `TArray < FLandscapeInfoLayerSettings >` | - |
| `RChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `GChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `BChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `AChannelLayer` | `TWeakObjectPtr < ULandscapeLayerInfoObject >` | - |
| `RChannelCustomWeight` | `int32` | - |
| `GChannelCustomWeight` | `int32` | - |
| `BChannelCustomWeight` | `int32` | - |
| `AChannelCustomWeight` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeLayerInfoObject.json -->

# ULandscapeLayerInfoObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerName` | `FName` | - |
| `PhysMaterial` | `UPhysicalMaterial *` | - |
| `Hardness` | `float` | - |
| `LayerUsageDebugColor` | `FLinearColor` | The color to use for layer usage debug |
| `bNoWeightBlend` | `uint32` | - |
| `IsReferencedFromLoadedData` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeMaterialIdLayerInfoObject.json -->

# ULandscapeMaterialIdLayerInfoObject

## Inheritance

`ULandscapeLayerInfoObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BiomesOwner` | `ULandscapeBiomesInfoObject *` | Owner Biomes of this LayerInfoObject. Do not modify this Owner unless necessary. |
| `DisplayName` | `FName` | - |
| `LayerIndex` | `int32` | Layer index of this layer info object, can be re-ordered. |
| `DiffuseTexture` | `UTexture2D *` | Diffuse Texture |
| `NormalmapTexture` | `UTexture2D *` | Normalmap Texture |
| `TextureRotation` | `float` | Rotation (in degree) applied when sampling diffusenormal texture |
| `TextureTiling` | `FVector2D` | Scaling applied when sampling diffusenormal texture |
| `TextureTilingFar` | `FVector2D` | - |
| `TextureTilingFarScale` | `FVector2D` | - |
| `TextureFarUVParam` | `FVector2D` | - |
| `HeightBlendThresholdSoftness` | `float` | ThresholdSoftness adjusts how sharp the edges of the height blend will be. The greater the value is, the softer the edge would be. |
| `HeightContrast` | `float` | HeightContrast adjust sampled height value's contrast. |
| `DeltaForceHeightBlendSharpness` | `float` | - |
| `DisplacementLocalBias` | `float` | Convert displacement from texture space to world space, unit is meter. |
| `DisplacementIntensity` | `float` | Scalar applied to displacement, applied after LocalBias is applied. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeMaterialInstanceConstant.json -->

# ULandscapeMaterialInstanceConstant

## Inheritance

`UMaterialInstanceConstant`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bIsLayerThumbnail` | `uint32` | - |
| `bDisableTessellation` | `uint32` | - |
| `bNotForceOverridenBaseProperties` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeMeshCollisionComponent.json -->

# ULandscapeMeshCollisionComponent

## Inheritance

`ULandscapeHeightfieldCollisionComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MeshGuid` | `FGuid` | Guid used to share PhysX heightfield objects in the editor |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeMeshProxyComponent.json -->

# ULandscapeMeshProxyComponent

## Inheritance

`UStaticMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LandscapeGuid` | `FGuid` | The landscape this proxy was generated for |
| `ProxyComponentBases` | `TArray < FIntPoint >` | The components this proxy was generated for |
| `ProxyLOD` | `int8` | LOD level proxy was generated for |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeSplineControlPoint.json -->

# ULandscapeSplineControlPoint

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Location` | `FVector` | Location in Landscape-space |
| `Rotation` | `FRotator` | Rotation of tangent vector at this point (in landscape-space) |
| `Width` | `float` | Width of the spline at this point. |
| `SideFalloff` | `float` | Falloff at the sides of the spline at this point. |
| `EndFalloff` | `float` | Falloff at the startend of the spline (if this point is a start or end point, otherwise ignored). |
| `ConnectedSegments` | `TArray < FLandscapeSplineConnection >` | - |
| `Points` | `TArray < FLandscapeSplineInterpPoint >` | Spline points |
| `Bounds` | `FBox` | Bounds of points |
| `LocalMeshComponent` | `UControlPointMeshComponent *` | Control point mesh |
| `SegmentMeshOffset` | `float` | Vertical offset of the spline segment mesh. Useful for a river's surface, among other things. |
| `LayerName` | `FName` | Name of blend layer to paint when applying spline to landscape<br>	  If "none", no layer is painted |
| `bRaiseTerrain` | `uint32` | If the spline is above the terrain, whether to raise the terrain up to the level of the spline when applying it to the landscape. |
| `bLowerTerrain` | `uint32` | If the spline is below the terrain, whether to lower the terrain down to the level of the spline when applying it to the landscape. |
| `Mesh` | `UStaticMesh *` | Mesh to use on the control point |
| `MaterialOverrides` | `TArray < UMaterialInterface * >` | Overrides mesh's materials |
| `MeshScale` | `FVector` | Scale of the control point mesh |
| `bEnableCollision` | `uint32` | Whether to enable collision for the Control Point Mesh. |
| `bCastShadow` | `uint32` | Whether the Control Point Mesh should cast a shadow. |
| `LDMaxDrawDistance` | `float` | Max draw distance for the mesh used on this control point |
| `TranslucencySortPriority` | `int32` | Translucent objects with a lower sort priority draw behind objects with a higher priority.<br>	  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.<br>	 <br>	  Ignored if the object is not translucent.  The default priority is zero.<br>	  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly. |
| `bPlaceSplineMeshesInStreamingLevels` | `uint32` | Whether control point mesh should be placed in landscape proxy streaming level (true) or the spline's level (false) |
| `bRenderToTerrainVirtualTexture` | `uint8` | This spline will be rendered to terrain VT if true |
| `TerrainRVTRenderSortPriority` | `int32` | Objects with a lower sort priority draw behind objects with a higher priority.<br>	  Objects with the same priority are rendered from back-to-front based on their bounds origin. |
| `bHiddenInGame` | `bool` | - |
| `bSelected` | `uint32` | - |
| `bNavDirty` | `uint32` | - |
| `ForeignWorld` | `TSoftObjectPtr < UWorld >` | World reference for if mesh component is stored in another streaming level |
| `ModificationKey` | `FGuid` | Key for tracking whether this segment has been modified relative to the mesh component stored in another streaming level |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeSplinesComponent.json -->

# ULandscapeSplinesComponent

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ControlPoints` | `TArray < ULandscapeSplineControlPoint * >` | - |
| `Segments` | `TArray < ULandscapeSplineSegment * >` | - |
| `CookedForeignMeshComponents` | `TArray < UMeshComponent * >` | - |
| `SplineResolution` | `float` | Resolution of the spline, in distance per point |
| `SplineColor` | `FColor` | Color to use to draw the splines |
| `ControlPointSprite` | `UTexture2D *` | Sprite used to draw control points |
| `SplineEditorMesh` | `UStaticMesh *` | Mesh used to draw splines that have no mesh |
| `bShowSplineEditorMesh` | `uint32` | Whether we are in-editor and showing spline editor meshes |
| `ForeignWorldSplineDataMap` | `TMap < TSoftObjectPtr < UWorld > , FForeignWorldSplineData >` | - |
| `bOverrideSplineMeshLightmapType` | `uint8` | Whether to override the lightmap type for all spline mesh components. |
| `SplineMeshLightmapType` | `TEnumAsByte < ELightmapType >` | Controls the type of lightmap used for all spline mesh components. Only used if bOverrideSplineMeshLightmapType is true. |
| `bOverrideSplineMeshLightmapRes` | `uint8` | Whether to override the lightmap resolution for all spline mesh components. |
| `OverriddenSplineMeshLightmapRes` | `int32` | Light map resolution to use on all spline mesh components, used if bOverrideSplineMeshLightmapRes is true. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULandscapeSplineSegment.json -->

# ULandscapeSplineSegment

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Connections` | `FLandscapeSplineSegmentConnection` | - |
| `SplineInfo` | `FInterpCurveVector` | Actual data for spline. |
| `Points` | `TArray < FLandscapeSplineInterpPoint >` | Spline points |
| `Bounds` | `FBox` | Bounds of points |
| `LocalMeshComponents` | `TArray < USplineMeshComponent * >` | Spline meshes |
| `LayerName` | `FName` | Name of blend layer to paint when applying spline to landscape<br>	  If "none", no layer is painted |
| `bRaiseTerrain` | `uint32` | If the spline is above the terrain, whether to raise the terrain up to the level of the spline when applying it to the landscape. |
| `bLowerTerrain` | `uint32` | If the spline is below the terrain, whether to lower the terrain down to the level of the spline when applying it to the landscape. |
| `SplineMeshes` | `TArray < FLandscapeSplineMeshEntry >` | Spline meshes from this list are used in random order along the spline. |
| `bEnableCollision` | `uint32` | Whether to generate collision for the Spline Meshes. |
| `bCastShadow` | `uint32` | Whether the Spline Meshes should cast a shadow. |
| `RandomSeed` | `int32` | Random seed used for choosing which order to use spline meshes. Ignored if only one mesh is set. |
| `LDMaxDrawDistance` | `float` | Max draw distance for all the mesh pieces used in this spline |
| `TranslucencySortPriority` | `int32` | Translucent objects with a lower sort priority draw behind objects with a higher priority.<br>	  Translucent objects with the same priority are rendered from back-to-front based on their bounds origin.<br>	 <br>	  Ignored if the object is not translucent.  The default priority is zero.<br>	  Warning: This should never be set to a non-default value unless you know what you are doing, as it will prevent the renderer from sorting correctly. |
| `bPlaceSplineMeshesInStreamingLevels` | `uint32` | Whether spline meshes should be placed in landscape proxy streaming levels (true) or the spline's level (false) |
| `bRenderToTerrainVirtualTexture` | `uint8` | This spline will be rendered to terrain VT if true |
| `TerrainRVTRenderSortPriority` | `int32` | Objects with a lower sort priority draw behind objects with a higher priority.<br>	  Objects with the same priority are rendered from back-to-front based on their bounds origin. |
| `bHiddenInGame` | `bool` | - |
| `bSelected` | `uint32` | - |
| `bNavDirty` | `uint32` | - |
| `ForeignWorlds` | `TArray < TSoftObjectPtr < UWorld > >` | World references for mesh components stored in other streaming levels |
| `ModificationKey` | `FGuid` | Key for tracking whether this segment has been modified relative to the mesh components stored in other streaming levels |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULayer.json -->

# ULayer

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerName` | `FName` | The display name of the layer |
| `bIsVisible` | `uint32` | Whether actors associated with the layer are visible in the viewport |
| `ActorStats` | `TArray < FLayerActorStats >` | Basic stats regarding the number of Actors and their types currently assigned to the Layer |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevel.json -->

# ULevel

A Level is a collection of Actors (lights, volumes, mesh instances etc.).
  Multiple Levels can be loaded and unloaded into the World to create a streaming experience.
 
  @see UActor

## Inheritance

`UObject` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OwningWorld` | `UWorld *` | The World that has this level in its Levels array.<br>	  This is not the same as GetOuter(), because GetOuter() for a streaming level is a vestigial world that is not used.<br>	  It should not be accessed during BeginDestroy(), just like any other UObject references, since GC may occur in any order. |
| `Model` | `UModel *` | BSP UModel. |
| `ModelComponents` | `TArray < UModelComponent * >` | BSP Model components used for rendering. |
| `ActorCluster` | `ULevelActorContainer *` | - |
| `NumTextureStreamingUnbuiltComponents` | `int32` | Num of components missing valid texture streaming data. Updated in map check. |
| `NumTextureStreamingDirtyResources` | `int32` | Num of resources that have changed since the last texture streaming build. Updated in map check. |
| `LevelScriptActor` | `ALevelScriptActor *` | The level scripting actor, created by instantiating the class from LevelScriptBlueprint.  This handles all level scripting |
| `NavListStart` | `ANavigationObjectBase *` | Start and end of the navigation list for this level, used for quickly fixing up<br>	  when streaming this level inout. @TODO DEPRECATED - DELETE |
| `NavListEnd` | `ANavigationObjectBase *` | - |
| `NavDataChunks` | `TArray < UNavigationDataChunk * >` | Navigation related data that can be stored per level |
| `LightmapTotalSize` | `float` | Total number of KB used for lightmap textures in the level. |
| `ShadowmapTotalSize` | `float` | Total number of KB used for shadowmap textures in the level. |
| `StaticNavigableGeometry` | `TArray < FVector >` | threes of triangle vertices - AABB filtering friendly. Stored if there's a runtime need to rebuild navigation that accepts BSPs<br>	 	as well - it's a lot easier this way than retrieve this data at runtime |
| `StreamingTextureGuids` | `TArray < FGuid >` | The Guid of each texture refered by FStreamingTextureBuildInfo::TextureLevelIndex |
| `LevelVolumeProbeGIBakedStreamingData` | `ULevelVolumeProbeGIBakedStreamingData *` | - |
| `PVSHandlerHash` | `FString` | - |
| `PrecomputedVisibilityDataRegistry` | `UPrecomputedVisibilityDataRegistry *` | - |
| `bIsLightingScenario` | `bool` | Whether the level is a lighting scenario.  Lighting is built separately for each lighting scenario level with all other scenario levels hidden.<br>	  Only one lighting scenario level should be visible at a time for correct rendering, and lightmaps from that level will be used on the rest of the world.<br>	  Note: When a lighting scenario level is present, lightmaps for all streaming levels are placed in the scenario's _BuildData package.<br>	 		This means that lightmaps for those streaming levels will not be streamed with them. |
| `LevelBuildDataId` | `FGuid` | Identifies map build data specific to this level, eg lighting volume samples. |
| `LightBuildLevelOffset` | `FIntVector` | Level offset at time when lighting was built |
| `bTextureStreamingRotationChanged` | `uint8` | Whether a level transform rotation was applied since the texture streaming builds. Invalidates the precomputed streaming bounds. |
| `bIsVisible` | `uint8` | Whether the level is currently visible associated with the world |
| `bLocked` | `uint8` | Whether this level is locked; that is, its actors are read-only<br>	 	Used by WorldBrowser to lock a level when corresponding ULevelStreaming does not exist |
| `bPVSDirty` | `uint8` | - |
| `WorldSettings` | `AWorldSettings *` | - |
| `MapBuildData` | `UMapBuildDataRegistry *` | Registry for data from the map build.  This is stored in a separate package from the level to speed up saving  autosaving.<br>	  ReleaseRenderingResources must be called before changing what is referenced, to update the rendering thread state. |
| `RCRCommunicatorClassName` | `FSoftClassPath` | - |
| `RCRCommunicator` | `URCRCommunicator *` | - |
| `MeshRefCounter` | `TMap < UStaticMesh * , int32 >` | - |
| `Level_RCR` | `ULevel_RCR *` | - |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `LevelScriptBlueprint` | `ULevelScriptBlueprint *` | Reference to the blueprint for level scripting |
| `TextureStreamingResourceGuids` | `TArray < FGuid >` | The Guid list of all materials and meshes Guid used in the last texture streaming build. Used to know if the streaming data needs rebuild. Only used for the persistent level. |
| `LevelSimplification` | `FLevelSimplificationDetails` | Level simplification settings for each LOD |
| `PlatformLevelSimplification` | `TArray < FLevelSimplificationDetails >` | - |
| `LevelColor` | `FLinearColor` | The level color used for visualization. (Show -> Advanced -> Level Coloration)<br>	  Used only in world composition mode |
| `CurrentTieredMapBuildData` | `UMapBuildDataRegistry *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelActorContainer.json -->

# ULevelActorContainer

Root object for all level actors

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Actors` | `TArray < AActor * >` | Array of actors in a level |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelBlocksFoliageDataContainer.json -->

# ULevelBlocksFoliageDataContainer

植被

## Inheritance

`ULevelBlocksDataContainer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LevelFoliageLocations` | `TMap < FName , FFoliageTypeLocation >` | - |
| `TreesFlyLevel` | `FStringAssetReference` | - |
| `TreesFlyLevelName` | `FName` | - |
| `SurroundingTreesLevels` | `TSet < FName >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelCapture.json -->

# ULevelCapture

## Inheritance

`UMovieSceneCapture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoStartCapture` | `bool` | Specifies whether the capture should start immediately, or whether it will be invoked externally (through StartMovieCaptureStopMovieCapture exec commands) |
| `PrerequisiteActorId` | `FGuid` | Copy of the ID from PrerequisiteActor. Required because JSON serialization exports the path of the object, rather that its GUID |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelScriptBlueprint.json -->

# ULevelScriptBlueprint

A level blueprint is a specialized type of blueprint. It is used to house
  global, level-wide logic. In a level blueprint, you can operate on specific 
  level-actor instances through blueprint's node-based interface. UE3 users 
  should be familiar with this concept, as it is very similar to Kismet.
 
  @see UBlueprint
  @see ALevelScriptActor

## Inheritance

`UBlueprint`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FriendlyName` | `FString` | The friendly name to use for UI |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequence.json -->

# ULevelSequence

Movie scene animation for Actors.

## Inheritance

`UMovieSceneSequence`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MovieScene` | `UMovieScene *` | Pointer to the movie scene that controls this animation. |
| `ObjectReferences` | `FLevelSequenceObjectReferenceMap` | Legacy object references - should be read-only. Not deprecated because they need to still be saved |
| `BindingReferences` | `FLevelSequenceBindingReferences` | References to bound objects. |
| `PossessedObjects_DEPRECATED` | `TMap < FString , FLevelSequenceObject >` | Deprecated property housing old possessed object bindings |
| `DirectorClass` | `UClass *` | The class that is used to spawn this level sequence's director instance.<br>	  Director instances are allocated on-demand one per sequence during evaluation and are used by event tracks for triggering events. |
| `DirectorBlueprint` | `UBlueprint *` | A pointer to the director blueprint that generates this sequence's DirectorClass. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequenceBurnIn.json -->

# ULevelSequenceBurnIn

Base class for level sequence burn ins

## Inheritance

`UUserWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FrameInformation` | `FLevelSequencePlayerSnapshot` | Snapshot of frame information. |
| `LevelSequenceActor` | `ALevelSequenceActor *` | The actor to get our burn in frames from |

## Functions

### `SetSettings`

```text
SetSettings(InSettings: UObject *) -> void
```

Called when this burn in is receiving its settings

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSettings` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSettingsClass`

```text
GetSettingsClass() -> TSubclassOf < ULevelSequenceBurnInInitSettings >
```

Get the settings class to use for this burn in

**Returns**

| Type | Description |
|---|---|
| `TSubclassOf < ULevelSequenceBurnInInitSettings >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequenceBurnInOptions.json -->

# ULevelSequenceBurnInOptions

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseBurnIn` | `bool` | - |
| `BurnInClass` | `FSoftClassPath` | - |
| `Settings` | `ULevelSequenceBurnInInitSettings *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequenceDirector.json -->

# ULevelSequenceDirector

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Player` | `ULevelSequencePlayer *` | Pointer to the player that's playing back this director's sequence |

## Functions

### `OnCreated`

```text
OnCreated() -> void
```

Called when this director is created

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelSequencePlayer.json -->

# ULevelSequencePlayer

ULevelSequencePlayer is used to actually "play" an level sequence asset at runtime.
 
  This class keeps track of playback state and provides functions for manipulating
  an level sequence while its playing.

## Inheritance

`UMovieSceneSequencePlayer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AdditionalEventReceivers` | `TArray < UObject * >` | Array of additional event receivers |

## Functions

### `CreateLevelSequencePlayer`

```text
CreateLevelSequencePlayer(WorldContextObject: UObject *, LevelSequence: ULevelSequence *, Settings: FMovieSceneSequencePlaybackSettings, OutActor: ALevelSequenceActor * &) -> ULevelSequencePlayer *
```

Create a new level sequence player.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | Context object from which to retrieve a UWorld. |
| `LevelSequence` | `ULevelSequence *` | The level sequence to play. |
| `Settings` | `FMovieSceneSequencePlaybackSettings` | The desired playback settings |
| `OutActor` | `ALevelSequenceActor * &` | The level sequence actor created to play this sequence. |

**Returns**

| Type | Description |
|---|---|
| `ULevelSequencePlayer *` | - |

### `GetEventReceivers`

```text
GetEventReceivers() -> TArray < UObject * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UObject * >` | - |

## Delegates

### `OnCameraCut`

```text
OnCameraCut(CameraComponent: UCameraComponent*) -> void
```

Event triggered when there is a camera cut

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CameraComponent` | `UCameraComponent*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelStreaming.json -->

# ULevelStreaming

Abstract base class of container object encapsulating data required for streaming and providing 
  interface for when a level should be streamed in and out of memory.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PackageName_DEPRECATED` | `FName` | Deprecated name of the package containing the level to load. Use GetWorldAsset() or GetWorldAssetPackageFName() instead. |
| `WorldAsset` | `TSoftObjectPtr < UWorld >` | The reference to the world containing the level to load |
| `PackageNameToLoad` | `FName` | If this isn't Name_None, then we load from this package on disk to the new package named PackageName |
| `LODPackageNames` | `TArray < FName >` | LOD versions of this level |
| `LevelTransform` | `FTransform` | Transform applied to actors after loading. |
| `bShouldBeVisibleInEditor` | `uint32` | Whether this level should be visible in the Editor |
| `bLocked` | `uint32` | Whether this level is locked; that is, its actors are read-only. |
| `bShouldBeLoaded` | `uint32` | Whether the level should be loaded |
| `bShouldBeVisible` | `uint32` | Whether the level should be visible if it is loaded |
| `bIsStatic` | `uint32` | Whether this level only contains static actors that aren't affected by gameplay or replication.<br>	  If true, the engine can make certain optimizations and will add this level to the StaticLevels collection. |
| `bShouldBlockOnLoad` | `uint32` | Whether we want to force a blocking load |
| `LevelLODIndex` | `int32` | Requested LOD. Non LOD sub-levels have Index = -1 |
| `bDisableDistanceStreaming` | `uint32` | Whether this level streaming object should be ignored by world composition distance streaming, <br>	   so streaming state can be controlled by other systems (ex: in blueprints) |
| `bDrawOnLevelStatusMap` | `uint32` | If true, will be drawn on the 'level streaming status' map (STAT LEVELMAP console command) |
| `DrawColor_DEPRECATED` | `FColor` | Deprecated level color used for visualization. |
| `LevelColor` | `FLinearColor` | The level color used for visualization. (Show -> Advanced -> Level Coloration) |
| `EditorStreamingVolumes` | `TArray < ALevelStreamingVolume * >` | The level streaming volumes bound to this level. |
| `MinTimeBetweenVolumeUnloadRequests` | `float` | Cooldown time in seconds between volume-based unload requests.  Used in preventing spurious unload requests. |
| `Keywords` | `TArray < FString >` | List of keywords to filter on in the level browser |
| `LoadedLevel` | `ULevel *` | Pointer to Level object if currently loaded streamed in. |
| `PendingUnloadLevel` | `ULevel *` | Pointer to a Level object that was previously active and was replaced with a new LoadedLevel (for LOD switching) |
| `UnloadingLevels` | `TArray < ULevel * >` | Array to save unloading levels. |
| `LevelStreamingInfo` | `FLevelLoadConditionInfo` | - |
| `FolderPath` | `FName` | The folder path for this level within the world browser. This is only available in editor builds. <br>		A NONE path indicates that it exists at the root. It is '' separated. |

## Functions

### `GetWorldAssetPackageFName`

```text
GetWorldAssetPackageFName() -> ENGINE_API FName
```

Gets the package name for the world asset referred to by this level streaming as an FName

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FName` | - |

### `GetLoadedLevel`

```text
GetLoadedLevel() -> ENGINE_API class ULevel *
```

Gets a pointer to the LoadedLevel value

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API class ULevel *` | - |

### `IsLevelVisible`

```text
IsLevelVisible() -> ENGINE_API bool
```

Returns whether streaming level is visible

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `IsLevelLoaded`

```text
IsLevelLoaded() -> ENGINE_API bool
```

Returns whether streaming level is loaded

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `IsStreamingStatePending`

```text
IsStreamingStatePending() -> ENGINE_API bool
```

Returns whether level has streaming state change pending

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `CreateInstance`

```text
CreateInstance(UniqueInstanceName: FString) -> ULevelStreaming *
```

Creates a new instance of this streaming level with a provided unique instance name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UniqueInstanceName` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `ULevelStreaming *` | - |

### `GetLevelScriptActor`

```text
GetLevelScriptActor() -> ENGINE_API ALevelScriptActor *
```

Returns the Level Script Actor of the level if the level is loaded and valid

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API ALevelScriptActor *` | - |

## Delegates

### `OnLevelLoaded`

```text
OnLevelLoaded() -> void
```

Called when level is streamed in

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLevelUnloaded`

```text
OnLevelUnloaded() -> void
```

Called when level is streamed out

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLevelShown`

```text
OnLevelShown() -> void
```

Called when level is added to the world

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLevelHidden`

```text
OnLevelHidden() -> void
```

Called when level is removed from the world

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULevelStreamingKismet.json -->

# ULevelStreamingKismet

## Inheritance

`ULevelStreaming`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bInitiallyLoaded` | `uint32` | Whether the level should be loaded at startup |
| `bInitiallyVisible` | `uint32` | Whether the level should be visible at startup if it is loaded |

## Functions

### `LoadLevelInstance`

```text
LoadLevelInstance(WorldContextObject: UObject *, LevelName: FString &, Location: FVector &, Rotation: FRotator &, bOutSuccess: bool &) -> ENGINE_API ULevelStreamingKismet *
```

Stream in a level with a specific location and rotation. You can create multiple instances of the same level!
 	
 	 The level to be loaded does not have to be in the persistent map's Levels list, however to ensure that the .umap does get
 	 packaged, please be sure to include the .umap in your Packaging Settings:
 	
 	   Project Settings -> Packaging -> List of Maps to Include in a Packaged Build (you may have to show advanced or type in filter)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `LevelName` | `FString &` | - Level package name, ex: GameMapsMyMapName, specifying short name like MyMapName will force very slow search on disk |
| `Location` | `FVector &` | - World space location where the level should be spawned |
| `Rotation` | `FRotator &` | - World space rotation for rotating the entire level |
| `bOutSuccess` | `bool &` | - Whether operation was successful (map was found and added to the sub-levels list) |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API ULevelStreamingKismet *` | Streaming level object for a level instance |

### `CreateLevelInstanceWithLevelName`

```text
CreateLevelInstanceWithLevelName(WorldContextObject: UObject *, LevelName: FString &, UniqueName: FString &, Trans: FTransform &, bOutSuccess: bool &) -> ENGINE_API ULevelStreamingKismet *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `LevelName` | `FString &` | - |
| `UniqueName` | `FString &` | - |
| `Trans` | `FTransform &` | - |
| `bOutSuccess` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API ULevelStreamingKismet *` | - |

### `CreateLevelInstanceWithLevel`

```text
CreateLevelInstanceWithLevel(OriStreamingLevel: ULevelStreaming *, UniqueName: FString &, Trans: FTransform &, bOutSuccess: bool &) -> ENGINE_API ULevelStreamingKismet *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OriStreamingLevel` | `ULevelStreaming *` | - |
| `UniqueName` | `FString &` | - |
| `Trans` | `FTransform &` | - |
| `bOutSuccess` | `bool &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API ULevelStreamingKismet *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULightComponent.json -->

# ULightComponent

## Inheritance

`ULightComponentBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Temperature` | `float` | Color temperature in Kelvin of the blackbody illuminant.<br>	 White (D65) is 6500K. |
| `MaxDrawDistance` | `float` | - |
| `MaxDistanceFadeRange` | `float` | - |
| `bUseTemperature` | `uint32` | false: use white (D65) as illuminant. |
| `ShadowMapChannel_DEPRECATED` | `int32` | Legacy shadowmap channel from the lighting build, now stored in FLightComponentMapBuildData. |
| `MinRoughness` | `float` | Min roughness effective for this light. Used for softening specular highlights. |
| `SpecularScale` | `float` | Multiplier on specular highlights. Use only with great care! Any value besides 1 is not physical!<br>	 Can be used to artistically remove highlights mimicking polarizing filters or photo touch up. |
| `bLocalLightDisableDiffuse` | `uint32` | Local light disable diffuse |
| `ShadowResolutionScale` | `float` | Scales the resolution of shadowmaps used to shadow this light.  By default shadowmap resolution is chosen based on screen size of the caster. <br>	  Note: shadowmap resolution is still clamped by 'r.Shadow.MaxResolution' |
| `LightPriority` | `int32` | Light priority for mobile light grid |
| `ShadowBias` | `float` | Controls how accurate self shadowing of whole scene shadows from this light are.  <br>	  At 0, shadows will start at the their caster surface, but there will be many self shadowing artifacts.<br>	  larger values, shadows will start further from their caster, and there won't be self shadowing artifacts but object might appear to fly.<br>	  around 0.5 seems to be a good tradeoff. This also affects the soft transition of shadows |
| `ShadowSharpen` | `float` | Amount to sharpen shadow filtering |
| `ContactShadowLength` | `float` | Length of screen space ray trace for sharp contact shadows. Zero is disabled. |
| `InverseSquaredFalloff_DEPRECATED` | `uint32` | - |
| `bCacheStaticShadows` | `uint32` | - |
| `CastTranslucentShadows` | `uint32` | Whether the light is allowed to cast dynamic shadows from translucency. |
| `bCastShadowsFromCinematicObjectsOnly` | `uint32` | Whether the light should only cast shadows from components marked as bCastCinematicShadows. <br>	  This is useful for setting up cinematic Movable spotlights aimed at characters and avoiding the shadow depth rendering costs of the background.<br>	  Note: this only works with dynamic shadow maps, not with static shadowing or Ray Traced Distance Field shadows. |
| `bAffectDynamicIndirectLighting` | `uint32` | Whether the light should be injected into the Light Propagation Volume |
| `LightingChannels` | `FLightingChannels` | Channels that this light should affect.  <br>	  These channels only apply to opaque materials, direct lighting, and dynamic lighting and shadowing. |
| `LightFunctionMaterial` | `UMaterialInterface *` | The light function material to be applied to this light.<br>	  Note that only non-lightmapped lights (UseDirectLightMap=False) can have a light function. |
| `LightFunctionScale` | `FVector` | Scales the light function projection.  X and Y scale in the directions perpendicular to the light's direction, Z scales along the light direction. |
| `IESTexture` | `UTextureLightProfile *` | IES texture (light profiles from real world measured data) |
| `bUseIESBrightness` | `uint32` | true: take light brightness from IES profile, false: use the light brightness - the maximum light in one direction is used to define no masking. Use with InverseSquareFalloff. Will be disabled if a valid IES profile texture is not supplied. |
| `IESBrightnessScale` | `float` | Global scale for IES brightness contribution. Only available when "Use IES Brightness" is selected, and a valid IES profile texture is set |
| `LightFunctionFadeDistance` | `float` | Distance at which the light function should be completely faded to DisabledBrightness.  <br>	  This is useful for hiding aliasing from light functions applied in the distance. |
| `DisabledBrightness` | `float` | Brightness factor applied to the light when the light function is specified but disabled, for example in scene captures that use SceneCapView_LitNoShadows. <br>	  This should be set to the average brightness of the light function material's emissive input, which should be between 0 and 1. |
| `bEnableLightShaftBloom` | `uint32` | Whether to render light shaft bloom from this light. <br>	  For directional lights, the color around the light direction will be blurred radially and added back to the scene.<br>	  for point lights, the color on pixels closer than the light's SourceRadius will be blurred radially and added back to the scene. |
| `BloomScale` | `float` | Scales the additive color. |
| `BloomThreshold` | `float` | Scene color must be larger than this to create bloom in the light shafts. |
| `BloomTint` | `FColor` | Multiplies against scene color to create the bloom color. |
| `bUseRayTracedDistanceFieldShadows` | `bool` | Whether to use ray traced distance field area shadows.  The project setting bGenerateMeshDistanceFields must be enabled for this to have effect.<br>	  Distance field shadows support area lights so they create soft shadows with sharp contacts.  <br>	  They have less aliasing artifacts than standard shadowmaps, but inherit all the limitations of distance field representations (only uniform scale, no deformation).<br>	  These shadows have a low per-object cost (and don't depend on triangle count) so they are effective for distant shadows from a dynamic sun. |
| `RayStartOffsetDepthScale` | `float` | Controls how large of an offset ray traced shadows have from the receiving surface as the camera gets further away.  <br>	  This can be useful to hide self-shadowing artifacts from low resolution distance fields on huge static meshes. |

## Functions

### `SetIntensity`

```text
SetIntensity(NewIntensity: float) -> void
```

Set intensity of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIndirectLightingIntensity`

```text
SetIndirectLightingIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVolumetricScatteringIntensity`

```text
SetVolumetricScatteringIntensity(NewIntensity: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewIntensity` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightColor`

```text
SetLightColor(NewLightColor: FLinearColor, bSRGB: bool) -> void
```

Set color of the light

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightColor` | `FLinearColor` | - |
| `bSRGB` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTemperature`

```text
SetTemperature(NewTemperature: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTemperature` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionMaterial`

```text
SetLightFunctionMaterial(NewLightFunctionMaterial: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionScale`

```text
SetLightFunctionScale(NewLightFunctionScale: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionScale` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionFadeDistance`

```text
SetLightFunctionFadeDistance(NewLightFunctionFadeDistance: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionFadeDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionDisabledBrightness`

```text
SetLightFunctionDisabledBrightness(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAffectDynamicIndirectLighting`

```text
SetAffectDynamicIndirectLighting(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAffectTranslucentLighting`

```text
SetAffectTranslucentLighting(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnableLightShaftBloom`

```text
SetEnableLightShaftBloom(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBloomScale`

```text
SetBloomScale(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBloomThreshold`

```text
SetBloomThreshold(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBloomTint`

```text
SetBloomTint(NewValue: FColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `FColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIESTexture`

```text
SetIESTexture(NewValue: UTextureLightProfile *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `UTextureLightProfile *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetShadowBias`

```text
SetShadowBias(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ForceUpdateShadowState`

```text
ForceUpdateShadowState() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpecularScale`

```text
SetSpecularScale(NewValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLocalLightDisableDiffuse`

```text
SetLocalLightDisableDiffuse(NewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULightComponentBase.json -->

# ULightComponentBase

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightGuid` | `FGuid` | GUID used to associate a light component with precomputed shadowing information across levels.<br>	  The GUID changes whenever the light position changes. |
| `Brightness_DEPRECATED` | `float` | - |
| `Intensity` | `float` | Total energy that the light emits.  <br>	  For pointspot lights with inverse squared falloff, this is in units of lumens.  1700 lumens corresponds to a 100W lightbulb. <br>	  For other lights, this is just a brightness multiplier. |
| `LightColor` | `FColor` | Filter color of the light.<br>	  Note that this can change the light's effective intensity. |
| `bAffectsWorld` | `uint32` | Whether the light can affect the world, or whether it is disabled.<br>	  A disabled light will not contribute to the scene in any way.  This setting cannot be changed at runtime and unbuilds lighting when changed.<br>	  Setting this to false has the same effect as deleting the light, so it is useful for non-destructive experiments. |
| `CastShadows` | `uint32` | Whether the light should cast any shadows. |
| `CastStaticShadows` | `uint32` | Whether the light should cast shadows from static objects.  Also requires Cast Shadows to be set to True. |
| `CastDynamicShadows` | `uint32` | Whether the light should cast shadows from dynamic objects.  Also requires Cast Shadows to be set to True. |
| `bAffectTranslucentLighting` | `uint32` | Whether the light affects translucency or not.  Disabling this can save GPU time when there are many small lights. |
| `bCastVolumetricShadow` | `uint32` | Whether the light shadows volumetric fog.  Disabling this can save GPU time. |
| `RequiredDeviceLevel` | `int32` | - |
| `IndirectLightingIntensity` | `float` | Scales the indirect lighting contribution from this light. <br>	  A value of 0 disables any GI from this light. Default is 1. |
| `VolumetricScatteringIntensity` | `float` | Intensity of the volumetric scattering from this light.  This scales Intensity and LightColor. |

## Functions

### `SetCastShadows`

```text
SetCastShadows(bNewValue: bool) -> void
```

Sets whether this light casts shadows

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLightColor`

```text
GetLightColor() -> FLinearColor
```

Gets the light color as a linear color

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetCastVolumetricShadow`

```text
SetCastVolumetricShadow(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULightmappedSurfaceCollection.json -->

# ULightmappedSurfaceCollection

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceModel` | `UModel *` | The UModel these surfaces come from. |
| `Surfaces` | `TArray < int32 >` | An array of the surface indices grouped into a single static lighting mapping. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULightmassPortalComponent.json -->

# ULightmassPortalComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PreviewBox` | `UBoxComponent *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULightmassPrimitiveSettingsObject.json -->

# ULightmassPrimitiveSettingsObject

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightmassSettings` | `FLightmassPrimitiveSettings` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UListView.json -->

# UListView

Allows thousands of items to be displayed in a list.  Generates widgets dynamically for each item.

## Inheritance

`UTableViewBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemHeight` | `float` | The height of each widget |
| `Items` | `TArray < UObject * >` | The list of items to generate widgets for |
| `SelectionMode` | `TEnumAsByte < ESelectionMode :: Type >` | The selection method for the list |
| `OnGenerateRowEvent` | `FOnGenerateRowUObject` | Called when a widget needs to be generated |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULocalizedOverlays.json -->

# ULocalizedOverlays

Implements an asset that contains a set of Basic Overlays that will be displayed in accordance with
  the current locale, or a default set if an appropriate locale is not found

## Inheritance

`UOverlays`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultOverlays` | `UBasicOverlays *` | The overlays to use if no overlays are found for the current culture |
| `LocaleToOverlaysMap` | `TMap < FString , UBasicOverlays * >` | Maps a set of cultures to specific BasicOverlays assets.<br>	  Cultures are comprised of three hyphen-separated parts:<br>	 		A two-letter ISO 639-1 language code (e.g., "zh")<br>	 		An optional four-letter ISO 15924 script code (e.g., "Hans")<br>	 		An optional two-letter ISO 3166-1 country code  (e.g., "CN") |
| `AssetImportData` | `UAssetImportData *` | The import data used to make this overlays asset |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/ULocalPlayer.json -->

# ULocalPlayer

Each player that is active on the current client has a LocalPlayer. It stays active across maps
 	There may be several spawned in the case of splitscreencoop.
 	There may be 0 spawned on servers.

## Inheritance

`UPlayer`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ViewportClient` | `UGameViewportClient *` | The master viewport containing this player's view. |
| `AspectRatioAxisConstraint` | `TEnumAsByte < enum EAspectRatioAxisConstraint >` | How to constrain perspective viewport FOV |
| `PendingLevelPlayerControllerClass` | `TSubclassOf < APlayerController >` | The class of PlayerController to spawn for players logging in. |
| `bSentSplitJoin` | `uint32` | set when we've sent a split join request |
| `ControllerId` | `int32` | The controller ID which this player accepts input from. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UManagementRuleSetting.json -->

# UManagementRuleSetting

ManagementRule逻辑规则的.ini文件配置版本，减少结构体和容器嵌套，方便.ini配置和阅读

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `SetResult` | `EAssetSetManagerResult` | - |
| `CheckTargetDirectoriesSwitch` | `FManagementRuleSwitch` | - |
| `CheckTargetDirectories` | `TArray < FManagementRuleFStringCheck >` | - |
| `CheckTargetAssetsSwitch` | `FManagementRuleSwitch` | - |
| `CheckTargetAssets` | `TArray < FManagementRuleFNameCheck >` | - |
| `CheckTargetAssetClassSwitch` | `FManagementRuleSwitch` | - |
| `CheckTargetAssetClassTypes` | `TArray < FManagementRuleFNameCheck >` | - |
| `CheckSourcePackagesSwitch` | `FManagementRuleSwitch` | - |
| `CheckSourcePackages` | `TArray < FManagementRuleFNameCheck >` | - |
| `CheckSourcePackageClassSwitch` | `FManagementRuleSwitch` | - |
| `CheckSourcePackageClassTypes` | `TArray < FManagementRuleFNameCheck >` | - |
| `CheckTargetAssetTagSwitch` | `FManagementRuleSwitch` | - |
| `CheckTargetAssetTags` | `TArray < FManagementRuleFNameCheck >` | - |
| `bOnlySoftReferences` | `bool` | - |
| `CheckOrMask` | `uint8` | 对应FManagementRule::CheckOrMask，控制6个检查条件之间的或与非逻辑，见EManagementRuleCheckOrMask |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMapBuildDataRegistry.json -->

# UMapBuildDataRegistry

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LevelLightingQuality` | `TEnumAsByte < enum ELightingBuildQuality >` | The lighting quality the level was last built with |
| `LevelVolumeProbeGIBakedStreamingData` | `ULevelVolumeProbeGIBakedStreamingData *` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterial.json -->

# UMaterial

A Material is an asset which can be applied to a mesh to control the visual look of the scene.
  When light from the scene hits the surface, the shading model of the material is used to calculate how that light interacts with the surface.
 
  Warning: Creating new materials directly increases shader compile times!  Consider creating a Material Instance off of an existing material instead.

## Inheritance

`UMaterialInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PhysMaterial` | `UPhysicalMaterial *` | Physical material to use for this graphics material. Used for sounds, effects etc. |
| `DiffuseColor_DEPRECATED` | `FColorMaterialInput` | - |
| `SpecularColor_DEPRECATED` | `FColorMaterialInput` | - |
| `BaseColor` | `FColorMaterialInput` | - |
| `Metallic` | `FScalarMaterialInput` | - |
| `Specular` | `FScalarMaterialInput` | - |
| `Roughness` | `FScalarMaterialInput` | - |
| `Normal` | `FVectorMaterialInput` | - |
| `EmissiveColor` | `FColorMaterialInput` | - |
| `Opacity` | `FScalarMaterialInput` | - |
| `OpacityMask` | `FScalarMaterialInput` | - |
| `ReplaceMaterial` | `UMaterialInterface *` | - |
| `MaterialDomain` | `TEnumAsByte < enum EMaterialDomain >` | The domain that the material's attributes will be evaluated in.<br>	  Certain pieces of material functionality are only valid in certain domains, for example vertex normal is only valid on a surface. |
| `BlendMode` | `TEnumAsByte < enum EBlendMode >` | Determines how the material's color is blended with background colors. |
| `DecalBlendMode` | `TEnumAsByte < enum EDecalBlendMode >` | Defines how the GBuffer chanels are getting manipulated by a decal material pass. (only with MaterialDomain == MD_DeferredDecal) |
| `MaterialDecalResponse` | `TEnumAsByte < enum EMaterialDecalResponse >` | Defines how the material reacts on DBuffer decals (Affects look, performance and texturesample usage).<br>	  Non DBuffer Decals can be disabled on the primitive (e.g. static mesh) |
| `ShadingModel` | `TEnumAsByte < enum EMaterialShadingModel >` | Determines how inputs are combined to create the material's final color. |
| `bIncludeShaderCode` | `uint32` | - |
| `OpacityMaskClipValue` | `float` | If BlendMode is BLEND_Masked, the surface is not rendered where OpacityMask < OpacityMaskClipValue. |
| `bTranslucentVelocityRendering` | `uint32` | - |
| `TranslucentVelocityClipValue` | `float` | - |
| `VertexOffsetAlongNormal` | `float` | pixels offset along vertex normal, for outline drawing. |
| `bCastDynamicShadowAsMasked` | `uint32` | If true, translucent materials will cast dynamic shadows according to their opacity.<br>	 OpacityMaskClipValue is used as the threshold value. |
| `bCastDynamicShadowAsUnlit` | `uint32` | - |
| `OITBlendMode` | `TEnumAsByte < enum EOITBlendMode >` | - |
| `WorldPositionOffset` | `FVectorMaterialInput` | Adds to world position in the vertex shader. |
| `WorldDisplacement` | `FVectorMaterialInput` | Offset in world space applied to tessellated vertices. |
| `TessellationMultiplier` | `FScalarMaterialInput` | Multiplies the tessellation factors applied when a tessellation mode is set. |
| `SubsurfaceColor` | `FColorMaterialInput` | Inner material color, only used for ShadingModel=Subsurface |
| `ClearCoat` | `FScalarMaterialInput` | - |
| `ClearCoatRoughness` | `FScalarMaterialInput` | - |
| `AmbientOcclusion` | `FScalarMaterialInput` | output ambient occlusion to the GBuffer |
| `Refraction` | `FScalarMaterialInput` | output refraction index for translucent rendering<br>	  Air:1.0 Water:1.333 Ice:1.3 Glass:~1.6 Diamond:2.42 |
| `CustomizedUVs` | `FVector2MaterialInput` | These inputs are evaluated in the vertex shader and allow artists to do arbitrary vertex shader operations and access them in the pixel shader.<br>	  When unconnected or hidden they default to passing through the vertex UVs. |
| `MaterialAttributes` | `FMaterialAttributesInput` | - |
| `PixelDepthOffset` | `FScalarMaterialInput` | - |
| `CustomizedVertexColor` | `FVector4MaterialInput` | - |
| `PlanarReflectionOffsetScale` | `FVector4MaterialInput` | - |
| `VertexDepthOffset` | `FScalarMaterialInput` | - |
| `PixelDepthOffsetNegative` | `FScalarMaterialInput` | - |
| `bAllowGCCluster` | `uint32` | - |
| `bEnableSeparateTranslucency` | `uint32` | Indicates that the material should be rendered in the SeparateTranslucency Pass (not affected by DOF, requires bAllowSeparateTranslucency to be set in .ini). |
| `bTranslucencyRenderAfterSS` | `uint32` | Indicates that the material should be rendered after post process and super sampling, dedicate for reticle materials |
| `bEnableMobileSeparateTranslucency` | `uint32` | Indicates that the translucent material should not be affected by bloom or DOF. (Note: Depth testing is not available) |
| `bEnableMobileDownsampleSeparateTranslucency` | `uint32` | Indicates that the translucent material can be rendered on an off-screen render target at a low resolution) |
| `bEnableResponsiveAA` | `uint32` | Indicates that the material should be rendered using responsive anti-aliasing. Improves sharpness of small moving particles such as sparks.<br>	  Only use for small moving features because it will cause aliasing of the background. |
| `bScreenSpaceReflections` | `uint32` | SSR on translucency |
| `TwoSided` | `uint32` | Indicates that the material should be rendered without backface culling and the normal should be flipped for backfaces. |
| `DitheredLODTransition` | `uint32` | Whether meshes rendered with the material should support dithered LOD transitions. |
| `ForceOpaqueLevelPointIndirectLighting` | `uint32` | - |
| `DitherOpacityMask` | `uint32` | Dither opacity mask. When combined with Temporal AA this can be used as a form of limited translucency which supports all lighting features. |
| `bAllowNegativeEmissiveColor` | `uint32` | Whether the material should allow outputting negative emissive color values.  Only allowed on unlit materials. |
| `NumCustomizedUVs` | `int32` | Number of customized UV inputs to display.  Unconnected customized UV inputs will just pass through the vertex UVs. |
| `TranslucencyLightingMode` | `TEnumAsByte < enum ETranslucencyLightingMode >` | Sets the lighting mode that will be used on this material if it is translucent. |
| `TranslucencyDirectionalLightingIntensity` | `float` | Useful for artificially increasing the influence of the normal on the lighting result for translucency.<br>	  A value larger than 1 increases the influence of the normal, a value smaller than 1 makes the lighting more ambient. |
| `AllowTranslucentCustomDepthWrites` | `uint32` | Allows a translucenct material to be used with custom depth writing by compiling additional shaders. |
| `TranslucentShadowDensityScale` | `float` | Scale used to make translucent shadows more or less opaque than the material's actual opacity. |
| `TranslucentSelfShadowDensityScale` | `float` | Scale used to make translucent self-shadowing more or less opaque than the material's shadow on other objects.<br>	  This is only used when the object is casting a volumetric translucent shadow. |
| `TranslucentSelfShadowSecondDensityScale` | `float` | Used to make a second self shadow gradient, to add interesting shading in the shadow of the first. |
| `TranslucentSelfShadowSecondOpacity` | `float` | Controls the strength of the second self shadow gradient. |
| `TranslucentBackscatteringExponent` | `float` | Controls how diffuse the material's backscattering is when using the MSM_Subsurface shading model.<br>	  Larger exponents give a less diffuse look (smaller, brighter backscattering highlight).<br>	  This is only used when the object is casting a volumetric translucent shadow from a directional light. |
| `TranslucentMultipleScatteringExtinction` | `FLinearColor` | Colored extinction factor used to approximate multiple scattering in dense volumes.<br>	  This is only used when the object is casting a volumetric translucent shadow. |
| `TranslucentShadowStartOffset` | `float` | Local space distance to bias the translucent shadow.  Positive values move the shadow away from the light. |
| `bDisableDepthTest` | `uint32` | Whether to draw on top of opaque pixels even if behind them. This only has meaning for translucency. |
| `bGenerateSphericalParticleNormals` | `uint32` | Whether to generate spherical normals for particles that use this material. |
| `bTangentSpaceNormal` | `uint32` | Whether the material takes a tangent space normal or a world space normal as input.<br>	  (TangentSpace requires extra instructions but is often more convenient). |
| `bUseEmissiveForDynamicAreaLighting` | `uint32` | If enabled, the material's emissive colour is injected into the LightPropagationVolume |
| `bBlockGI` | `uint32` | If enabled, the material's opacity defines how much GI is blocked when using the LightPropagationVolume feature |
| `bUseSimpleGI` | `uint32` | If enabled, the material uses simplified and inaccurate GI color for efficiency |
| `bUsedAsSpecialEngineMaterial` | `uint32` | This is a special usage flag that allows a material to be assignable to any primitive type.<br>	  This is useful for materials used by code to implement certain viewmodes, for example the default material or lighting only material.<br>	  The cost is that nearly 20x more shaders will be compiled for the material than the average material, which will greatly increase shader compile time and memory usage.<br>	  This flag should only be enabled when absolutely necessary, and is purposefully not exposed to the UI to prevent abuse. |
| `bUsedWithSkeletalMesh` | `uint32` | Indicates that the material and its instances can be use with skeletal meshes.<br>	  This will result in the shaders required to support skeletal meshes being compiled which will increase shader compile time and memory usage. |
| `bUsedWithGFur` | `uint32` | Indicates that the material and its instances can be use with GFur.<br>	 This will result in the shaders required to support skeletal meshes being compiled which will increase shader compile time and memory usage. |
| `bUsedWithEditorCompositing` | `uint32` | Indicates that the material and its instances can be use with editor compositing<br>	  This will result in the shaders required to support editor compositing being compiled which will increase shader compile time and memory usage. |
| `bUsedWithParticleSprites` | `uint32` | Indicates that the material and its instances can be use with particle sprites<br>	  This will result in the shaders required to support particle sprites being compiled which will increase shader compile time and memory usage. |
| `bForceDisableSubUVCalculate` | `uint32` | - |
| `bUsedWithBeamTrails` | `uint32` | Indicates that the material and its instances can be use with beam trails<br>	  This will result in the shaders required to support beam trails being compiled which will increase shader compile time and memory usage. |
| `bUsedWithMeshParticles` | `uint32` | Indicates that the material and its instances can be use with mesh particles<br>	  This will result in the shaders required to support mesh particles being compiled which will increase shader compile time and memory usage. |
| `bUsedWithParticleBigWorldPrecision` | `uint32` | - |
| `bUsedWithNiagaraSprites` | `uint32` | Indicates that the material and its instances can be use with Niagara sprites (meshes and ribbons, respectively)<br>	 This will result in the shaders required to support Niagara sprites being compiled which will increase shader compile time and memory usage. |
| `bUsedWithNiagaraRibbons` | `uint32` | - |
| `bUsedWithNiagaraMeshParticles` | `uint32` | - |
| `bUsedWithIBL` | `uint32` | Indicates that the material and its instances can be use with reflection cube<br>	  This will result in the shaders required to support IBL being compiled which will increase shader compile time and memory usage. |
| `bUsedWithStaticLighting` | `uint32` | Indicates that the material and its instances can be use with static lighting<br>	  This will result in the shaders required to support static lighting being compiled which will increase shader compile time and memory usage. |
| `bUsedWithMorphTargets` | `uint32` | Indicates that the material and its instances can be use with morph targets<br>	  This will result in the shaders required to support morph targets being compiled which will increase shader compile time and memory usage. |
| `bUsedWithSplineMeshes` | `uint32` | Indicates that the material and its instances can be use with spline meshes<br>	  This will result in the shaders required to support spline meshes being compiled which will increase shader compile time and memory usage. |
| `bUsedWithQuantizedMeshes` | `uint32` | - |
| `bUsedWithInstancedStaticMeshes` | `uint32` | Indicates that the material and its instances can be use with instanced static meshes<br>	  This will result in the shaders required to support instanced static meshes being compiled which will increase shader compile time and memory usage. |
| `bUsedWithCustomInstancedStaticMeshes` | `uint32` | Indicates that the material and its instances can be use with custom instanced static meshes<br>	  This will result in the shaders required to support instanced static meshes being compiled which will increase shader compile time and memory usage. |
| `bUsedWithInstancedWidget` | `uint32` | - |
| `bUsedWithInstancedPDSurface` | `uint32` | - |
| `bUsesDistortion` | `uint32` | Indicates that the material and its instances can be use with distortion<br>	  This will result in the shaders required to support distortion being compiled which will increase shader compile time and memory usage. |
| `bUsedWithClothing` | `uint32` | Indicates that the material and its instances can be use with clothing<br>	  This will result in the shaders required to support clothing being compiled which will increase shader compile time and memory usage. |
| `bUsedWithUI_DEPRECATED` | `uint32` | Indicates that the material and its instances can be use with Slate UI and UMG<br>	  This will result in the shaders required to support UI materials being compiled which will increase shader compile time and memory usage. |
| `bUsedWithPPRBackgroud` | `uint32` | Indicates that the material would use for ppr background in deferred rendering. |
| `bUsedWithSurfelInjectColor` | `uint32` | Indicates that the material and its instances can be use with SurfelGI inject color<br>	  This will result in the shaders required to support SurfelGI inject color being compiled which will increase shader compile time and memory usage.<br>	  HACK by huiwenjiang. |
| `bUsedWithTranslucentGI` | `uint32` | [SurfelGI - brainfkli ADD]<br>	  Indicates that the material and its instances can be affected by GI in translucent blend mode. |
| `bUsedWithAtmosphericSkyBox` | `uint32` | Indicates that the material and its instances can be use with AtmosphericSkyBox<br>	  This will result in the shaders required to support AtmosphericSkyBox being compiled which will increase shader compile time and memory usage. |
| `bAutomaticallySetUsageInEditor` | `uint32` | Whether to automatically set usage flags based on what the material is applied to in the editor.<br>	  It can be useful to disable this on a base material with many instances, where adding another usage flag accidentally (eg bUsedWithSkeletalMeshes) can add a lot of shader permutations. |
| `bFullyRough` | `uint32` | Forces the material to be completely rough. Saves a number of instructions and one sampler. Note: Overrided by Lite Rough. |
| `bUsedWithLandscapeDeform` | `uint32` | Indicates that the material and its instances can be use with Landscape Deform<br>	  This will result in the shaders required to support LandscapeDeform being compiled which will increase shader compile time and memory usage. |
| `bUseFullPrecision` | `uint32` | Forces this material to use full (highp) precision in the pixel shader.<br>	 	This is slower than the default (mediump) but can be used to work around precision-related rendering errors.<br>	 	This setting has no effect on older mobile devices that do not support high precision.<br>	   Note: Overrided by Lite Rough. |
| `bForceMaterialFloat` | `uint32` | Forces this material's temporary variables to use full precision float in the pixel shader.<br>	  Keeps uniforms to use default precision. HACK by huiwen. |
| `bUseLightmapDirectionality` | `uint32` | Use lightmap directionality and per pixel normals. If disabled, lighting from lightmaps will be flat but cheaper. |
| `bUsedWithDynamicInstancing` | `uint32` | Indicates that the each material instance(of this material) can be dynamic instanced. |
| `bDynamicInstancingByUBO` | `uint32` | - |
| `bUsedWithRuntimeStaticBatchMultiParams` | `uint32` | - |
| `bNeedInstanceTransform` | `uint32` | - |
| `bUseSimplestShader` | `uint32` | - |
| `bBypassSystemMaterialQuality` | `uint32` | - |
| `bBypassMobilePointLight` | `uint32` | - |
| `bUseAsEarlyZ` | `uint32` | - |
| `bForceOutputLinearSpace` | `uint32` | - |
| `bUseAsDrawToRenderTarget` | `uint32` | - |
| `bRenderInTwoPass` | `uint32` | - |
| `bShadowUseTentFilter` | `uint32` | - |
| `bUseLightmap` | `uint32` | - |
| `bUseGPUVolumetricLightMap` | `uint32` | - |
| `bUsedGPUVLMVertexLighting` | `uint32` | - |
| `bUseVolumeProbeGIMobile` | `uint32` | - |
| `bUseVolumeProbeGIMobileWithAO` | `uint32` | - |
| `bShouldReceiveGridShadow` | `uint32` | - |
| `bEnableMicroShadow` | `uint32` | - |
| `MicroShadowIntensity` | `float` | - |
| `bUseIndirectLighting` | `uint32` | - |
| `bShadowOnEmissiveColor` | `uint32` | - |
| `bUsedGrassInstnaceColor` | `uint32` | - |
| `bUsedVertexPointLight` | `uint32` | - |
| `bUsedWithLandscapeShadow` | `uint32` | - |
| `bUseLandscapeMultiLayer` | `uint32` | - |
| `bUsedWithPhotonShadow` | `uint32` | #if WITH_PHOTON_SHADOW |
| `bUsedWithPhotonShadowPCSS` | `uint32` | - |
| `bUsedDynamicObjectVertexLighting` | `uint32` | - |
| `bUsedWithDynamicBatching` | `uint32` | Indicates that the material instance shared with same base mat can be batched |
| `bUsedWithDynamicMergeSkeletalMesh` | `uint32` | - |
| `bUsedWithDynamicInstancingES2Fixup` | `uint32` | - |
| `bUsedWithMatIDLandscape` | `uint32` | - |
| `ShadowOverride` | `TEnumAsByte < enum EMaterialShadowOverride >` | - |
| `SimpleVertexNormalSituation` | `TEnumAsByte < enum ESimpleVertexNormalSituation >` | - |
| `bZForceFar` | `uint32` | - |
| `bWettable` | `uint32` | - |
| `bUseLegacySpecular` | `uint32` | use Phong instead of GGX |
| `bCorrectBlendingColorInHDR` | `uint32` | - |
| `bGPUSkinForceUseBonesUniformBuffer` | `uint32` | - |
| `bUseAsTranslucentEarlyZ` | `uint32` | - |
| `bLiteRough` | `uint32` | Override: Fully Rough On、UseFullPrecision Off |
| `bUseSimpleSkyLight` | `uint32` | - |
| `bACESOff` | `uint32` | - |
| `bEmissionOff` | `uint32` | - |
| `bInstL2WOnlyTranslation` | `uint32` | Instancing only uses translation of LocalToWorld, exclusive of rotation and scale. |
| `bUseLiteFog` | `uint32` | - |
| `bUseChromaticAberration` | `uint32` | - |
| `bUsedWithFirstPerson` | `uint32` | - |
| `bUsedWithScope` | `uint32` | - |
| `bUsedWithMaterialDistFade` | `uint32` | - |
| `bUseHQForwardReflections` | `uint32` | Forward renderer: enables multiple parallax-corrected reflection captures that blend together.<br>	  Mobile renderer: blend between nearest 3 reflection captures, but reduces the number of samplers available to the material as two more samplers will be used for reflection cubemaps. |
| `bUsePlanarForwardReflections` | `uint32` | Enables planar reflection when using the forward renderer or mobile. Enabling this setting reduces the number of samplers available to the material as one more sampler will be used for the planar reflection. |
| `bApplyVertexFog` | `uint32` | When false, materials are not fogged in forward shading or mobile. Defaults to true. |
| `bNormalCurvatureToRoughness` | `uint32` | Reduce roughness based on screen space normal changes. |
| `D3D11TessellationMode` | `TEnumAsByte < enum EMaterialTessellationMode >` | The type of tessellation to apply to this object.  Note D3D11 required for anything except MTM_NoTessellation. |
| `bEnableCrackFreeDisplacement` | `uint32` | Prevents cracks in the surface of the mesh when using tessellation. |
| `bEnableAdaptiveTessellation` | `uint32` | Enables adaptive tessellation, which tries to maintain a uniform number of pixels per triangle. |
| `bUsedWithTexture2DArrayShaderVariant` | `uint32` | ENABLE_TEXTURE2D_ARRAY_SHADER_VARIANT<br>	 Enable Dynamic MaterialInstance use Texture 2D Array shader variant with Texture 2D material expression graph |
| `bSkipRSH` | `uint32` | Skip Runtime Static Batching (RSH) |
| `bSkipDynamicSwitchOp` | `uint32` | - |
| `bUsesDeviceLevelSwitch` | `uint32` | 缓存标记：材质是否使用了DeviceLevelSwitch节点且High输入已连接，在PostEditChangeProperty中自动更新 |
| `bForceUsesDeviceLevelSwitch` | `uint32` | 强制开启DeviceLevelSwitch：勾选后bUsesDeviceLevelSwitch将被强制设为true，即使材质中没有DeviceLevelSwitch节点 |
| `bDisableShadowWPO` | `uint32` | - |
| `bEnableGrassShadowScale` | `uint32` | - |
| `bForceDisableVertexNormal` | `uint32` | - |
| `MaxDisplacement` | `float` | - |
| `Wireframe` | `uint32` | Enables a wireframe view of the mesh the material is applied to. |
| `bOutputVelocityOnBasePass` | `uint32` | Skips outputting velocity during the base pass. |
| `bUnlitOutputAllMTOnBasePass` | `uint32` | Force unlit material output all MT during the base pass. |
| `ShadingRate` | `TEnumAsByte < EMaterialShadingRate >` | Select what shading rate to apply for platforms that have variable rate shading |
| `EditorX` | `int32` | - |
| `EditorY` | `int32` | - |
| `EditorPitch` | `int32` | - |
| `EditorYaw` | `int32` | - |
| `Expressions` | `TArray < UMaterialExpression * >` | Array of material expressions, excluding Comments.  Used by the material editor. |
| `MaterialFunctionInfos` | `TArray < FMaterialFunctionInfo >` | Array of all functions this material depends on. |
| `MaterialParameterCollectionInfos` | `TArray < FMaterialParameterCollectionInfo >` | Array of all parameter collections this material depends on. |
| `bCanMaskedBeAssumedOpaque` | `uint32` | true if this Material can be assumed Opaque when set to masked. |
| `bIsMasked_DEPRECATED` | `uint32` | true if Material is masked and uses custom opacity |
| `bIsPreviewMaterial` | `uint32` | true if Material is the preview material used in the material editor. |
| `bUseMaterialAttributes` | `uint32` | when true, the material attributes pin is used instead of the regular pins. |
| `bComputeFogPerPixel` | `uint32` | When true, translucent materials have fog computed for every pixel, which costs more but fixes artifacts due to low tessellation. |
| `bDisableDirectionalLighting` | `uint32` | When true, the directional lighting will be disabled |
| `bAllowDevelopmentShaderCompile` | `uint32` | If true the compilation environment will be changed to remove the global COMPILE_SHADERS_FOR_DEVELOPMENT flag. |
| `bIsMaterialEditorStatsMaterial` | `uint32` | true if this is a special material used for stats by the material editor. |
| `bUseLandscapeVertexAO` | `uint32` | - |
| `bAllowLandscapeVertexMorph` | `uint32` | - |
| `bUseLandscapeVertexHole` | `uint32` | - |
| `UsageFlagWarnings` | `uint32` | true if we have printed a warning about material usage for a given usage flag. |
| `BlendableLocation` | `TEnumAsByte < enum EBlendableLocation >` | Where the node is inserted in the (post processing) graph, only used if domain is PostProcess |
| `BlendablePriority` | `int32` | If multiple nodes with the same  type are inserted at the same point, this defined order and if they get combined, only used if domain is PostProcess |
| `BlendableOutputAlpha` | `bool` | If this is enabled, the blendable will output alpha |
| `RefractionMode` | `TEnumAsByte < enum ERefractionMode >` | Controls how the Refraction input is interpreted and how the refraction offset into scene color is computed for this material. |
| `RefractionDepthBias` | `float` | This is the refraction depth bias, larger values offset distortion to prevent closer objects from rendering into the distorted surface at acute viewing angles but increases the disconnect between surface and where the refraction starts. |
| `bOceanFoam` | `uint32` | - |
| `bEnableMeshClip` | `uint32` | - |
| `bEnableMeshDiscard` | `uint32` | - |
| `bEnableMeshArcPlaneClip` | `uint32` | - |
| `bIsEnhancedUImage` | `uint32` | - |
| `bSimplePointLight` | `uint32` | Enable this so the material will not calculate spot light shadows |
| `StateId` | `FGuid` | Guid that uniquely identifies this material.<br>	  Any changes to the state of the material that do not appear separately in the shadermap DDC keys must cause this guid to be regenerated!<br>	  For example, a modification to the Expressions array.<br>	  Code changes that cause the guid to be regenerated on load should be avoided, as that requires a resave of the content to stop recompiling every load. |
| `ExpressionTextureReferences` | `TArray < UTexture * >` | Cached texture references from all expressions in the material (including nested functions).<br>	  This is used to link uniform texture expressions which were stored in the DDC with the UTextures that they reference. |
| `EditorComments` | `TArray < UMaterialExpressionComment * >` | Array of comments associated with this material; viewed in the material editor. |
| `ParameterGroupData` | `TArray < FParameterGroupData >` | Controls where this parameter group is displayed in a material instance parameter list.  The lower the number the higher up in the parameter list. |
| `ReferencedTextureGuids` | `TArray < FGuid >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialBillboardComponent.json -->

# UMaterialBillboardComponent

A 2d material that will be rendered always facing the camera.

## Inheritance

`UPrimitiveComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Elements` | `TArray < FMaterialSpriteElement >` | Current array of material billboard elements |

## Functions

### `SetElements`

```text
SetElements(NewElements: TArray < FMaterialSpriteElement > &) -> void
```

Set all elements of this material billboard component

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewElements` | `TArray < FMaterialSpriteElement > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddElement`

```text
AddElement(Material: UMaterialInterface *, DistanceToOpacityCurve: UCurveFloat *, bSizeIsInScreenSpace: bool, BaseSizeX: float, BaseSizeY: float, DistanceToSizeCurve: UCurveFloat *) -> void
```

Adds an element to the sprite.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Material` | `UMaterialInterface *` | - |
| `DistanceToOpacityCurve` | `UCurveFloat *` | - |
| `bSizeIsInScreenSpace` | `bool` | - |
| `BaseSizeX` | `float` | - |
| `BaseSizeY` | `float` | - |
| `DistanceToSizeCurve` | `UCurveFloat *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpression.json -->

# UMaterialExpression

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Material` | `UMaterial *` | The material that this expression is currently being compiled in.  <br>	  This is not necessarily the object which owns this expression, for example a preview material compiling a material function's expressions. |
| `Function` | `UMaterialFunction *` | The material function that this expression is being used with, if any.<br>	  This will be NULL if the expression belongs to a function that is currently being edited, |
| `Desc` | `FString` | A description that level designers can add (shows in the material editor UI). |
| `BorderColor` | `FColor` | Color of the expression's border outline. |
| `bRealtimePreview` | `uint32` | Set to true by RecursiveUpdateRealtimePreview() if the expression's preview needs to be updated in realtime in the material editor. |
| `bNeedToUpdatePreview` | `uint32` | If true, we should update the preview next render. This is set when changing bRealtimePreview. |
| `bIsParameterExpression` | `uint32` | Indicates that this is a 'parameter' type of expression and should always be loaded (ie not cooked away) because we might want the default parameter. |
| `bCommentBubbleVisible` | `uint32` | If true, the comment bubble will be visible in the graph editor |
| `bShowOutputNameOnPin` | `uint32` | If true, use the output name as the label for the pin |
| `bShowMaskColorsOnPin` | `uint32` | If true, changes the pin color to match the output mask |
| `bHidePreviewWindow` | `uint32` | If true, do not render the preview window for the expression |
| `bCollapsed` | `uint32` | If true, show a collapsed version of the node |
| `bShaderInputData` | `uint32` | Whether the node represents an input to the shader or not.  Used to color the node's background. |
| `bShowInputs` | `uint32` | Whether to draw the expression's inputs. |
| `bShowOutputs` | `uint32` | Whether to draw the expression's outputs. |
| `Outputs` | `TArray < FExpressionOutput >` | The expression's outputs, which are set in default properties by derived classes. |
| `MaterialExpressionEditorX` | `int32` | - |
| `MaterialExpressionEditorY` | `int32` | - |
| `GraphNode` | `UEdGraphNode *` | Expression's Graph representation |
| `MaterialExpressionGuid` | `FGuid` | GUID to uniquely identify this node, to help the tutorials out |
| `MenuCategories` | `TArray < FText >` | Localized categories to sort this expression into... |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionAbs.json -->

# UMaterialExpressionAbs

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | Link to the input expression to be evaluated |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionAdd.json -->

# UMaterialExpressionAdd

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionAntialiasedTextureMask.json -->

# UMaterialExpressionAntialiasedTextureMask

## Inheritance

`UMaterialExpressionTextureSampleParameter2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Threshold` | `float` | - |
| `Channel` | `TEnumAsByte < enum ETextureColorChannel >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionAppendVector.json -->

# UMaterialExpressionAppendVector

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArccosine.json -->

# UMaterialExpressionArccosine

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArccosineFast.json -->

# UMaterialExpressionArccosineFast

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArcsine.json -->

# UMaterialExpressionArcsine

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArcsineFast.json -->

# UMaterialExpressionArcsineFast

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArctangent.json -->

# UMaterialExpressionArctangent

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArctangent2.json -->

# UMaterialExpressionArctangent2

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Y` | `FExpressionInput` | - |
| `X` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArctangent2Fast.json -->

# UMaterialExpressionArctangent2Fast

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Y` | `FExpressionInput` | - |
| `X` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionArctangentFast.json -->

# UMaterialExpressionArctangentFast

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionAtmosphericFogColor.json -->

# UMaterialExpressionAtmosphericFogColor

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WorldPosition` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionBentNormalCustomOutput.json -->

# UMaterialExpressionBentNormalCustomOutput

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionBlackBody.json -->

# UMaterialExpressionBlackBody

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Temp` | `FExpressionInput` | Temperature |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionBlendMaterialAttributes.json -->

# UMaterialExpressionBlendMaterialAttributes

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FMaterialAttributesInput` | - |
| `B` | `FMaterialAttributesInput` | - |
| `Alpha` | `FExpressionInput` | - |
| `PixelAttributeBlendType` | `TEnumAsByte < EMaterialAttributeBlend :: Type >` | - |
| `VertexAttributeBlendType` | `TEnumAsByte < EMaterialAttributeBlend :: Type >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionBreakMaterialAttributes.json -->

# UMaterialExpressionBreakMaterialAttributes

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialAttributes` | `FMaterialAttributesInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionBumpOffset.json -->

# UMaterialExpressionBumpOffset

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Coordinate` | `FExpressionInput` | - |
| `Height` | `FExpressionInput` | - |
| `HeightRatioInput` | `FExpressionInput` | - |
| `HeightRatio` | `float` | - |
| `ReferencePlane` | `float` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinate is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionCeil.json -->

# UMaterialExpressionCeil

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionChromaticAberrationCustomOutput.json -->

# UMaterialExpressionChromaticAberrationCustomOutput

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionClamp.json -->

# UMaterialExpressionClamp

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `Min` | `FExpressionInput` | - |
| `Max` | `FExpressionInput` | - |
| `ClampMode` | `TEnumAsByte < enum EClampMode >` | - |
| `MinDefault` | `float` | - |
| `MaxDefault` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionClearCoatNormalCustomOutput.json -->

# UMaterialExpressionClearCoatNormalCustomOutput

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionClipmapSample.json -->

# UMaterialExpressionClipmapSample

## Inheritance

`UMaterialExpressionTextureSampleParameter2D`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClipmapTexture` | `UClipmapTexture *` | - |
| `ParentClipmapTexture` | `UClipmapTexture *` | - |
| `bLerpWithNextMip` | `bool` | - |
| `FallBackValue` | `FLinearColor` | - |
| `bUseCustomUV` | `bool` | - |
| `bUseCalculateUVInVS` | `bool` | - |
| `CustomUVIndex` | `int32` | - |
| `NumParentInputs` | `int32` | Number of inputs from parent class |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionCollectionParameter.json -->

# UMaterialExpressionCollectionParameter

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Collection` | `UMaterialParameterCollection *` | The Parameter Collection to use. |
| `ParameterName` | `FName` | Name of the parameter being referenced. |
| `ParameterId` | `FGuid` | Id that is set from the name, and used to handle renaming of collection parameters. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionComment.json -->

# UMaterialExpressionComment

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SizeX` | `int32` | - |
| `SizeY` | `int32` | - |
| `Text` | `FString` | - |
| `CommentColor` | `FLinearColor` | Color to style comment with |
| `FontSize` | `int32` | Size of the text in the comment box |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionComponentMask.json -->

# UMaterialExpressionComponentMask

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `R` | `uint32` | - |
| `G` | `uint32` | - |
| `B` | `uint32` | - |
| `A` | `uint32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionConstant.json -->

# UMaterialExpressionConstant

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `R` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionConstant2Vector.json -->

# UMaterialExpressionConstant2Vector

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `R` | `float` | - |
| `G` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionConstant3Vector.json -->

# UMaterialExpressionConstant3Vector

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Constant` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionConstant4Vector.json -->

# UMaterialExpressionConstant4Vector

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Constant` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionConstantBiasScale.json -->

# UMaterialExpressionConstantBiasScale

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `Bias` | `float` | - |
| `Scale` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionCosine.json -->

# UMaterialExpressionCosine

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `Period` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionCrossProduct.json -->

# UMaterialExpressionCrossProduct

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionCurveAtlasRowParameter.json -->

# UMaterialExpressionCurveAtlasRowParameter

## Inheritance

`UMaterialExpressionScalarParameter`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Curve` | `UCurveLinearColor *` | - |
| `Atlas` | `UCurveLinearColorAtlas *` | - |
| `InputTime` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionCustom.json -->

# UMaterialExpressionCustom

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Code` | `FString` | - |
| `OutputType` | `TEnumAsByte < enum ECustomMaterialOutputType >` | - |
| `Description` | `FString` | - |
| `Inputs` | `TArray < struct FCustomInput >` | - |
| `AdditionalOutputs` | `TArray < struct FCustomOutput >` | - |
| `IncludeFilePaths` | `TArray < FString >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDDX.json -->

# UMaterialExpressionDDX

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FExpressionInput` | The value we want to compute ddxddy from |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDDY.json -->

# UMaterialExpressionDDY

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Value` | `FExpressionInput` | The value we want to compute ddxddy from |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDecalMipmapLevel.json -->

# UMaterialExpressionDecalMipmapLevel

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TextureSize` | `FExpressionInput` | The texture's size |
| `ConstWidth` | `float` | only used if TextureSize is not hooked up |
| `ConstHeight` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDepthFade.json -->

# UMaterialExpressionDepthFade

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InOpacity` | `FExpressionInput` | Input opacity which will be scaled by the result of the fade. |
| `FadeDistance` | `FExpressionInput` | World space distance over which the fade should take place. |
| `OpacityDefault` | `float` | Opacity which will be scaled by the result of the fade.  This is used when InOpacity is unconnected. |
| `FadeDistanceDefault` | `float` | World space distance over which the fade should take place.  This is used when FadeDistance is unconnected. |
| `bSupportFPR` | `bool` | - |
| `bClampSceneDepth` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDepthOfFieldFunction.json -->

# UMaterialExpressionDepthOfFieldFunction

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FunctionValue` | `TEnumAsByte < enum EDepthOfFieldFunctionValue >` | Determines the mapping place to use on the terrain. |
| `Depth` | `FExpressionInput` | usually nothing or PixelDepth |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDeriveNormalZ.json -->

# UMaterialExpressionDeriveNormalZ

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InXY` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDesaturation.json -->

# UMaterialExpressionDesaturation

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |
| `Fraction` | `FExpressionInput` | - |
| `LuminanceFactors` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDeviceLevelSwitch.json -->

# UMaterialExpressionDeviceLevelSwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Default` | `FExpressionInput` | Default input (must be connected). Same as Low. Used when DEVICE_LEVEL_HIGH is 0. |
| `Low` | `FExpressionInput` | Low device input (optional). If connected, overrides Default. Used when DEVICE_LEVEL_HIGH is 0. |
| `High` | `FExpressionInput` | High device input (optional). Used when DEVICE_LEVEL_HIGH is 1. Connecting this enables DeviceLevel shader variants. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDistance.json -->

# UMaterialExpressionDistance

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDistanceFieldGradient.json -->

# UMaterialExpressionDistanceFieldGradient

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDistanceToNearestSurface.json -->

# UMaterialExpressionDistanceToNearestSurface

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Position` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDivide.json -->

# UMaterialExpressionDivide

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDotProduct.json -->

# UMaterialExpressionDotProduct

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDynamicInstancingParameter.json -->

# UMaterialExpressionDynamicInstancingParameter

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | The names of the parameter. |
| `DefaultValue` | `FLinearColor` | - |
| `ParameterIndex` | `int32` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDynamicParameter.json -->

# UMaterialExpressionDynamicParameter

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParamNames` | `TArray < FString >` | The names of the parameters.<br>	 	These will show up in Cascade when editing a particle system<br>	 	that uses the material it is in... |
| `DefaultValue` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFeatureLevelSwitch.json -->

# UMaterialExpressionFeatureLevelSwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Default` | `FExpressionInput` | Default connection, used when a certain feature level doesn't have an override. |
| `Inputs` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFloor.json -->

# UMaterialExpressionFloor

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFmod.json -->

# UMaterialExpressionFmod

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFontSample.json -->

# UMaterialExpressionFontSample

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Font` | `UFont *` | font resource that will be sampled |
| `FontTexturePage` | `int32` | allow access to the various font pages |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFontSampleParameter.json -->

# UMaterialExpressionFontSampleParameter

## Inheritance

`UMaterialExpressionFontSample`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | name to be referenced when we want to find and set thsi parameter |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `Group` | `FName` | The name of the parameter Group to display in MaterialInstance Editor. Default is None group |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFrac.json -->

# UMaterialExpressionFrac

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Input` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFresnel.json -->

# UMaterialExpressionFresnel

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExponentIn` | `FExpressionInput` | - |
| `Exponent` | `float` | The exponent to pass into the pow() function |
| `BaseReflectFractionIn` | `FExpressionInput` | - |
| `BaseReflectFraction` | `float` | Specifies the fraction of specular reflection when the surfaces is viewed from straight on.<br>	  A value of 1 effectively disables Fresnel. |
| `Normal` | `FExpressionInput` | The normal to dot with the camera FVector |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFunctionInput.json -->

# UMaterialExpressionFunctionInput

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Preview` | `FExpressionInput` | Used for previewing when editing the function, or when bUsePreviewValueAsDefault is enabled. |
| `InputName` | `FString` | The input's name, which will be drawn on the connector in function call expressions that use this function. |
| `Description` | `FString` | The input's description, which will be used as a tooltip on the connector in function call expressions that use this function. |
| `Id` | `FGuid` | Id of this input, used to maintain references through name changes. |
| `InputType` | `TEnumAsByte < enum EFunctionInputType >` | Type of this input.  <br>	  Input code chunks will be cast to this type, and a compiler error will be emitted if the cast fails. |
| `PreviewValue` | `FVector4` | Value used to preview this input when editing the material function. |
| `bUsePreviewValueAsDefault` | `uint32` | Whether to use the preview value or texture as the default value for this input. |
| `SortPriority` | `int32` | Controls where the input is displayed relative to the other inputs. |
| `bCompilingFunctionPreview` | `uint32` | true when this expression is being compiled in a function preview, <br>	  false when this expression is being compiled into a material that uses the function.<br>	  Only valid in Compile() |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionFunctionOutput.json -->

# UMaterialExpressionFunctionOutput

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OutputName` | `FString` | The output's name, which will be drawn on the connector in function call expressions that use this function. |
| `Description` | `FString` | The output's description, which will be used as a tooltip on the connector in function call expressions that use this function. |
| `SortPriority` | `int32` | Controls where the output is displayed relative to the other outputs. |
| `A` | `FExpressionInput` | Stores the expression in the material function connected to this output. |
| `bLastPreviewed` | `uint32` | Whether this output was previewed the last time this function was edited. |
| `Id` | `FGuid` | Id of this input, used to maintain references through name changes. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionGetMaterialAttributes.json -->

# UMaterialExpressionGetMaterialAttributes

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialAttributes` | `FMaterialAttributesInput` | - |
| `AttributeGetTypes` | `TArray < FGuid >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionGIReplace.json -->

# UMaterialExpressionGIReplace

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Default` | `FExpressionInput` | Used for direct lighting computations e.g. real-time shaders |
| `StaticIndirect` | `FExpressionInput` | Used for baked indirect lighting e.g. Lightmass |
| `DynamicIndirect` | `FExpressionInput` | Used for dynamic indirect lighting e.g. Light Propagation Volumes |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionIBLSwitch.json -->

# UMaterialExpressionIBLSwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IBLOn` | `FExpressionInput` | - |
| `IBLOff` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionIf.json -->

# UMaterialExpressionIf

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `AGreaterThanB` | `FExpressionInput` | - |
| `AEqualsB` | `FExpressionInput` | - |
| `ALessThanB` | `FExpressionInput` | - |
| `EqualsThreshold` | `float` | - |
| `ConstB` | `float` | only used if B is not hooked up |
| `ConstAEqualsB_DEPRECATED` | `float` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeBlendTA.json -->

# UMaterialExpressionLandscapeBlendTA

## Inheritance

`UMaterialExpressionTerrainBlendBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UV` | `FExpressionInput` | - |
| `DiffuseTexture` | `FExpressionInput` | - |
| `NormalTexture` | `FExpressionInput` | - |
| `HeightTexture` | `FExpressionInput` | - |
| `RoughnessTexture` | `FExpressionInput` | - |
| `Layers` | `TArray < FTerrainLayerTA >` | - |
| `ConstCoordinate` | `uint32` | only used if Coordinates is not hooked up |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeCustomChannelSample.json -->

# UMaterialExpressionLandscapeCustomChannelSample

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `bColorChannel` | `bool` | - |
| `bNonLandscapeSample` | `bool` | - |
| `TextureIndex` | `int32` | - |
| `ChannelIndex` | `int32` | - |
| `WorldPosition` | `FExpressionInput` | Optional world position input to override the default world position. |
| `PreviewWeight` | `FLinearColor` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeFlattenCoords.json -->

# UMaterialExpressionLandscapeFlattenCoords

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UVScaleBias` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeFlattenTexture.json -->

# UMaterialExpressionLandscapeFlattenTexture

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Coordinates` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeGrassOutput.json -->

# UMaterialExpressionLandscapeGrassOutput

## Inheritance

`UMaterialExpressionCustomOutput`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GrassTypes` | `TArray < FGrassInput >` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeLayerBlend.json -->

# UMaterialExpressionLandscapeLayerBlend

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Layers` | `TArray < FLayerBlendInput >` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeLayerCoords.json -->

# UMaterialExpressionLandscapeLayerCoords

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MappingType` | `TEnumAsByte < enum ETerrainCoordMappingType >` | Determines the mapping place to use on the terrain. |
| `CustomUVType` | `TEnumAsByte < enum ELandscapeCustomizedCoordType >` | Determines the mapping place to use on the terrain. |
| `MappingScaleOverride` | `FExpressionInput` | - |
| `MappingScale` | `float` | Uniform scale to apply to the mapping. |
| `MappingRotation` | `float` | Rotation to apply to the mapping. |
| `MappingPanU` | `float` | Offset to apply to the mapping along U. |
| `MappingPanV` | `float` | Offset to apply to the mapping along V. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeLayerSample.json -->

# UMaterialExpressionLandscapeLayerSample

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `PreviewWeight` | `float` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeLayerSwitch.json -->

# UMaterialExpressionLandscapeLayerSwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayerUsed` | `FExpressionInput` | - |
| `LayerNotUsed` | `FExpressionInput` | - |
| `ParameterName` | `FName` | - |
| `PreviewUsed` | `uint32` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeLayerWeight.json -->

# UMaterialExpressionLandscapeLayerWeight

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Base` | `FExpressionInput` | - |
| `Layer` | `FExpressionInput` | - |
| `ParameterName` | `FName` | - |
| `PreviewWeight` | `float` | - |
| `ConstBase` | `FVector` | only used if Base is not hooked up |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeMaterialIdSample.json -->

# UMaterialExpressionLandscapeMaterialIdSample

## Inheritance

`UMaterialExpressionTextureSample`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DiffuseSamplerType` | `TEnumAsByte < enum EMaterialSamplerType >` | - |
| `NormalSamplerType` | `TEnumAsByte < enum EMaterialSamplerType >` | - |
| `bUseTextureTransform` | `bool` | If apply rotationscaling separately when sample diffusenormal texture array. |
| `bUseDeltaForceHeightBlend` | `bool` | - |
| `bUseLargeWeight` | `bool` | - |
| `LargeWeight` | `float` | - |
| `bSkipNormalLowQuality` | `bool` | - |
| `bUseFarUV` | `bool` | - |
| `DeltaForceHeightBlendFactorInput` | `FExpressionInput` | - |
| `FarUVFactorInput` | `FExpressionInput` | - |
| `bUseApplyNoiseLow` | `bool` | - |
| `bUseApplyNoiseHigh` | `bool` | - |
| `bUseApplyNoiseMedium` | `bool` | - |
| `bUseApplyNoiseUltimateHigh` | `bool` | - |
| `bUseOneTextureInsteadFar` | `bool` | - |
| `bHasHole` | `bool` | - |
| `bUseLayerDensity` | `bool` | - |
| `bDebugES2` | `bool` | - |
| `bDebugBlend4Pixels` | `bool` | - |
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `NumParentInputs` | `int32` | Number of inputs from parent class |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeMaterialIdWeight.json -->

# UMaterialExpressionLandscapeMaterialIdWeight

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TestMaterialId` | `FExpressionInput` | - |
| `LayerName` | `FName` | - |
| `ExpressionGUID` | `FGuid` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLandscapeVisibilityMask.json -->

# UMaterialExpressionLandscapeVisibilityMask

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ExpressionGUID` | `FGuid` | GUID that should be unique within the material, this is used for parameter renaming. |
| `bUseMaterialIdShading` | `bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLightmassReplace.json -->

# UMaterialExpressionLightmassReplace

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Realtime` | `FExpressionInput` | - |
| `Lightmass` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLinearInterpolate.json -->

# UMaterialExpressionLinearInterpolate

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `Alpha` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |
| `ConstAlpha` | `float` | only used if Alpha is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLogarithm10.json -->

# UMaterialExpressionLogarithm10

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `X` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionLogarithm2.json -->

# UMaterialExpressionLogarithm2

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `X` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionMakeMaterialAttributes.json -->

# UMaterialExpressionMakeMaterialAttributes

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BaseColor` | `FExpressionInput` | - |
| `Metallic` | `FExpressionInput` | - |
| `Specular` | `FExpressionInput` | - |
| `Roughness` | `FExpressionInput` | - |
| `EmissiveColor` | `FExpressionInput` | - |
| `Opacity` | `FExpressionInput` | - |
| `OpacityMask` | `FExpressionInput` | - |
| `Normal` | `FExpressionInput` | - |
| `WorldPositionOffset` | `FExpressionInput` | - |
| `WorldDisplacement` | `FExpressionInput` | - |
| `TessellationMultiplier` | `FExpressionInput` | - |
| `SubsurfaceColor` | `FExpressionInput` | - |
| `ClearCoat` | `FExpressionInput` | - |
| `ClearCoatRoughness` | `FExpressionInput` | - |
| `AmbientOcclusion` | `FExpressionInput` | - |
| `Refraction` | `FExpressionInput` | - |
| `CustomizedUVs` | `FExpressionInput` | - |
| `PixelDepthOffset` | `FExpressionInput` | - |
| `CustomizedVertexColor` | `FExpressionInput` | - |
| `PlanarReflectionOffsetScale` | `FExpressionInput` | - |
| `VertexDepthOffset` | `FExpressionInput` | - |
| `PixelDepthOffsetNegative` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionMaterialFunctionCall.json -->

# UMaterialExpressionMaterialFunctionCall

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaterialFunction` | `UMaterialFunction *` | The function to call. |
| `FunctionInputs` | `TArray < struct FFunctionExpressionInput >` | Array of all the function inputs that this function exposes. |
| `FunctionOutputs` | `TArray < struct FFunctionExpressionOutput >` | Array of all the function outputs that this function exposes. |

## Functions

### `SetMaterialFunction`

```text
SetMaterialFunction(NewMaterialFunction: UMaterialFunction *) -> ENGINE_API bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewMaterialFunction` | `UMaterialFunction *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionMaterialProxyReplace.json -->

# UMaterialExpressionMaterialProxyReplace

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Realtime` | `FExpressionInput` | - |
| `MaterialProxy` | `FExpressionInput` | - |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionMax.json -->

# UMaterialExpressionMax

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionMin.json -->

# UMaterialExpressionMin

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionMultiply.json -->

# UMaterialExpressionMultiply

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `A` | `FExpressionInput` | - |
| `B` | `FExpressionInput` | - |
| `ConstA` | `float` | only used if A is not hooked up |
| `ConstB` | `float` | only used if B is not hooked up |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionNamedRerouteDeclaration.json -->

# UMaterialExpressionNamedRerouteDeclaration

## Inheritance

`UMaterialExpressionRerouteBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | 此 Named Reroute 的显示名称 |
| `NodeColor` | `FLinearColor` | 节点标题颜色，Declaration 和所有 Usage 共享 |
| `VariableGuid` | `FGuid` | 全局唯一标识，用于 Usage 查找 Declaration，以及复制粘贴后重连 |
| `Input` | `FExpressionInput` | 输入引脚：接收上游数据 |

## Language

`cpp`


---

<!-- Source: https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionNamedRerouteUsage.json -->

# UMaterialExpressionNamedRerouteUsage

## Inheritance

`UMaterialExpressionRerouteBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Declaration` | `UMaterialExpressionNamedRerouteDeclaration *` | 指向对应的 Declaration 节点（运行时直接引用） |
| `DeclarationGuid` | `FGuid` | Declaration 的 GUID 副本，用于序列化后重连和复制粘贴修复 |

## Language

`cpp`

