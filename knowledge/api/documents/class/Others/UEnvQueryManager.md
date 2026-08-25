---
id: "api:class:UEnvQueryManager"
title: "UEnvQueryManager"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryManager.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryManager

## Inheritance

`UObject` -> `FTickableGameObject` -> `FSelfRegisteringExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InstanceCache` | `TArray < FEnvQueryInstanceCache >` | cache of instances |
| `LocalContexts` | `TArray < UEnvQueryContext * >` | local cache of context objects for managing BP based objects |
| `GCShieldedWrappers` | `TArray < UEnvQueryInstanceBlueprintWrapper * >` | - |
| `MaxAllowedTestingTime` | `float` | how long are we allowed to test per update, in seconds. |
| `bTestQueriesUsingBreadth` | `bool` | whether we update EQS queries based on:<br>	    or test an entire query before moving to the next one (depth). |
| `QueryCountWarningThreshold` | `int32` | if greater than zero, we will warn once when the number of queries is greater than or equal to this number, and log the queries out |
| `QueryCountWarningInterval` | `double` | how often (in seconds) we will warn about the number of queries (allows us to catch multiple occurrences in a session) |

## Functions

### `RunEQSQuery`

```text
RunEQSQuery(WorldContextObject: UObject *, QueryTemplate: UEnvQuery *, Querier: UObject *, RunMode: TEnumAsByte < EEnvQueryRunMode :: Type >, WrapperClass: TSubclassOf < UEnvQueryInstanceBlueprintWrapper >) -> UEnvQueryInstanceBlueprintWrapper *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `QueryTemplate` | `UEnvQuery *` | - |
| `Querier` | `UObject *` | - |
| `RunMode` | `TEnumAsByte < EEnvQueryRunMode :: Type >` | - |
| `WrapperClass` | `TSubclassOf < UEnvQueryInstanceBlueprintWrapper >` | - |

**Returns**

| Type | Description |
|---|---|
| `UEnvQueryInstanceBlueprintWrapper *` | - |

## Language

`cpp`
