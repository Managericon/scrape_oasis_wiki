---
id: "api:cppstruct:FEditorImportWorkflowDefinition"
title: "FEditorImportWorkflowDefinition"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FEditorImportWorkflowDefinition.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FEditorImportWorkflowDefinition

Holds settings for the asset import workflow test

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ImportFilePath` | `FFilePath` | The file to import <br>	UPROPERTY(config, EditAnywhere, Category = Automation, meta = (FilePathFilter = "")) |
| `FactorySettings` | `TArray < FImportFactorySettingValues >` | Settings for the import factory |
