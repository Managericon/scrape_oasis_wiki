---
id: "api:class:UKismetStringLibrary"
title: "UKismetStringLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetStringLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
