---
id: "api:class:UKismetMathLibrary"
title: "UKismetMathLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetMathLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
