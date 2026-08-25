---
id: "api:class:UEnvQueryGenerator_BlueprintBase"
title: "UEnvQueryGenerator_BlueprintBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryGenerator_BlueprintBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryGenerator_BlueprintBase

## Inheritance

`UEnvQueryGenerator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GeneratorsActionDescription` | `FText` | A short description of what test does, like "Generate pawn named Joe" |
| `Context` | `TSubclassOf < UEnvQueryContext >` | context |
| `GeneratedItemType` | `TSubclassOf < UEnvQueryItemType >` | @todo this should show up only in the generator's BP, but <br>	 	due to the way EQS editor is generating widgets it's there as well<br>	 	It's a bug and we'll fix it |

## Functions

### `DoItemGeneration`

```text
DoItemGeneration(ContextLocations: TArray < FVector > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ContextLocations` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddGeneratedVector`

```text
AddGeneratedVector(GeneratedVector: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GeneratedVector` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddGeneratedActor`

```text
AddGeneratedActor(GeneratedActor: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GeneratedActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetQuerier`

```text
GetQuerier() -> UObject *
```

**Returns**

| Type | Description |
|---|---|
| `UObject *` | - |

## Language

`cpp`
