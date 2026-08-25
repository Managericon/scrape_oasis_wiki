---
id: "api:class:UKismetTextLibrary"
title: "UKismetTextLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetTextLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
