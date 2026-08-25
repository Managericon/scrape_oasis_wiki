---
id: "api:cppstruct:FEditorImportExportTestDefinition"
title: "FEditorImportExportTestDefinition"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FEditorImportExportTestDefinition.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FEditorImportExportTestDefinition

Holds settings for the asset import  export automation test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImportFilePath` | `FFilePath` | The file to import <br>	UPROPERTY(config, EditAnywhere, Category = Automation, meta = (FilePathFilter = "")) |
| `ExportFileExtension` | `FString` | The file extension to use when exporting |
| `bSkipExport` | `bool` | If true, the export step will be skipped |
| `FactorySettings` | `TArray < FImportFactorySettingValues >` | Settings for the import factory |
