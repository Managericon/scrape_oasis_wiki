---
id: "api:class:UKismetStringTableLibrary"
title: "UKismetStringTableLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UKismetStringTableLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

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
