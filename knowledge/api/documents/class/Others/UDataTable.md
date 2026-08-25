---
id: "api:class:UDataTable"
title: "UDataTable"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDataTable.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDataTable

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RowStruct` | `UScriptStruct *` | Structure to use for each row of the table, must inherit from FTableRowBase |
| `RowNameToCategoryMap` | `TMap < FName , FName >` | - |
| `CategoryMap` | `TMap < FName , int32 >` | - |
| `AssetImportData` | `UAssetImportData *` | - |
| `ImportPath_DEPRECATED` | `FString` | The filename imported to create this object. Relative to this object's package, BaseDir() or absolute |
| `RowStructName` | `FName` | The name of the RowStruct we were using when we were last saved |
| `IgnoreEmptyRowError` | `bool` | 是否忽略空数据错误,added by fourthchen |

## Language

`cpp`
