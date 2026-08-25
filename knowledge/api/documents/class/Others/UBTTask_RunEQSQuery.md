---
id: "api:class:UBTTask_RunEQSQuery"
title: "UBTTask_RunEQSQuery"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunEQSQuery.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTTask_RunEQSQuery

Run Environment Query System Query task node.
  Runs the specified environment query when executed.

## Inheritance

`UBTTask_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `QueryTemplate` | `UEnvQuery *` | query to run |
| `QueryParams` | `TArray < FEnvNamedValue >` | optional parameters for query |
| `QueryConfig` | `TArray < FAIDynamicParam >` | - |
| `RunMode` | `TEnumAsByte < EEnvQueryRunMode :: Type >` | determines which item will be stored (All = only first matching) |
| `EQSQueryBlackboardKey` | `FBlackboardKeySelector` | blackboard key storing an EQS query template |
| `bUseBBKey` | `bool` | - |
| `EQSRequest` | `FEQSParametrizedQueryExecutionRequest` | - |

## Language

`cpp`
