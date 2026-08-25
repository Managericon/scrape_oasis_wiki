---
id: "api:class:UDataTableFunctionLibrary"
title: "UDataTableFunctionLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDataTableFunctionLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDataTableFunctionLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `EvaluateCurveTableRow`

```text
EvaluateCurveTableRow(CurveTable: UCurveTable *, RowName: FName, InXY: float, OutResult: TEnumAsByte < EEvaluateCurveTableResult :: Type > &, OutXY: float &, ContextString: FString &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurveTable` | `UCurveTable *` | - |
| `RowName` | `FName` | - |
| `InXY` | `float` | - |
| `OutResult` | `TEnumAsByte < EEvaluateCurveTableResult :: Type > &` | - |
| `OutXY` | `float &` | - |
| `ContextString` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDataTableRowNames`

```text
GetDataTableRowNames(Table: UDataTable *, OutRowNames: TArray < FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Table` | `UDataTable *` | - |
| `OutRowNames` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDataTableRowFromName`

```text
GetDataTableRowFromName(Table: UDataTable *, RowName: FName, OutRow: FTableRowBase &) -> bool
```

Get a Row from a DataTable given a RowName

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Table` | `UDataTable *` | - |
| `RowName` | `FName` | - |
| `OutRow` | `FTableRowBase &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FillDataTableFromCSVString`

```text
FillDataTableFromCSVString(DataTable: UDataTable *, CSVString: FString &) -> bool
```

Empty and fill a Data Table from CSV string.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DataTable` | `UDataTable *` | - |
| `CSVString` | `FString &` | The Data that representing the contents of a CSV file. |

**Returns**

| Type | Description |
|---|---|
| `bool` | True if the operation succeeds, check the log for errors if it didn't succeed. |

## Language

`cpp`
