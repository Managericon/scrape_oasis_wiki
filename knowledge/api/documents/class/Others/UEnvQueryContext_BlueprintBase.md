---
id: "api:class:UEnvQueryContext_BlueprintBase"
title: "UEnvQueryContext_BlueprintBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEnvQueryContext_BlueprintBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEnvQueryContext_BlueprintBase

## Inheritance

`UEnvQueryContext`

## Functions

### `ProvideSingleActor`

```text
ProvideSingleActor(QuerierObject: UObject *, QuerierActor: AActor *, ResultingActor: AActor * &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingActor` | `AActor * &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProvideSingleLocation`

```text
ProvideSingleLocation(QuerierObject: UObject *, QuerierActor: AActor *, ResultingLocation: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingLocation` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProvideActorsSet`

```text
ProvideActorsSet(QuerierObject: UObject *, QuerierActor: AActor *, ResultingActorsSet: TArray < AActor * > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingActorsSet` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ProvideLocationsSet`

```text
ProvideLocationsSet(QuerierObject: UObject *, QuerierActor: AActor *, ResultingLocationSet: TArray < FVector > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QuerierObject` | `UObject *` | - |
| `QuerierActor` | `AActor *` | - |
| `ResultingLocationSet` | `TArray < FVector > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
