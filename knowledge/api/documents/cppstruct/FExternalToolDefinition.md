---
id: "api:cppstruct:FExternalToolDefinition"
title: "FExternalToolDefinition"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FExternalToolDefinition.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FExternalToolDefinition

Structure for defining an external tool

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ToolName` | `FString` | The name of the tool  test. |
| `ExecutablePath` | `FFilePath` | The executable to run. <br>	UPROPERTY(config, EditAnywhere, Category=ExternalTools, meta=(FilePathFilter = "")) |
| `CommandLineOptions` | `FString` | The command line options to pass to the executable. |
| `WorkingDirectory` | `FDirectoryPath` | The working directory for the new process. |
| `ScriptExtension` | `FString` | If set, look for scripts with this extension. |
| `ScriptDirectory` | `FDirectoryPath` | If the ScriptExtension is set, look here for the script files. |
