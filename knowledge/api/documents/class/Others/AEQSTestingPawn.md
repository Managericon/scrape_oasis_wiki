---
id: "api:class:AEQSTestingPawn"
title: "AEQSTestingPawn"
source: "https://developer.gp.qq.com/api/class/detail/Others/AEQSTestingPawn.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AEQSTestingPawn

this class is abstract even though it's perfectly functional on its own.
 	The reason is to stop it from showing as valid player pawn type when configuring 
 	project's game mode.

## Inheritance

`ACharacter` -> `IEQSQueryResultSourceInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryTemplate` | `UEnvQuery *` | - |
| `QueryParams` | `TArray < FEnvNamedValue >` | optional parameters for query |
| `QueryConfig` | `TArray < FAIDynamicParam >` | - |
| `TimeLimitPerStep` | `float` | - |
| `StepToDebugDraw` | `int32` | - |
| `HighlightMode` | `EEnvQueryHightlightMode` | - |
| `bDrawLabels` | `uint32` | - |
| `bDrawFailedItems` | `uint32` | - |
| `bReRunQueryOnlyOnFinishedMove` | `uint32` | - |
| `bShouldBeVisibleInGame` | `uint32` | - |
| `bTickDuringGame` | `uint32` | - |
| `QueryingMode` | `TEnumAsByte < EEnvQueryRunMode :: Type >` | - |
| `EdRenderComp` | `UEQSRenderingComponent *` | Editor Preview |

## Language

`cpp`
