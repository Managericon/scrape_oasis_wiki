---
id: "api:class:UKismetMetaDataLibrary"
title: "UKismetMetaDataLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetMetaDataLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
