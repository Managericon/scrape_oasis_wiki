---
id: "api:class:UGameplayTask_ClaimResource"
title: "UGameplayTask_ClaimResource"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayTask_ClaimResource.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayTask_ClaimResource

## Inheritance

`UGameplayTask`

## Functions

### `ClaimResource`

```text
ClaimResource(InTaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, ResourceClass: TSubclassOf < UGameplayTaskResource >, Priority: uint8, TaskInstanceName: FName) -> UGameplayTask_ClaimResource *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `ResourceClass` | `TSubclassOf < UGameplayTaskResource >` | - |
| `Priority` | `uint8` | - |
| `TaskInstanceName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_ClaimResource *` | - |

### `ClaimResources`

```text
ClaimResources(InTaskOwner: TScriptInterface < IGameplayTaskOwnerInterface >, ResourceClasses: TArray < TSubclassOf < UGameplayTaskResource > >, Priority: uint8, TaskInstanceName: FName) -> UGameplayTask_ClaimResource *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTaskOwner` | `TScriptInterface < IGameplayTaskOwnerInterface >` | - |
| `ResourceClasses` | `TArray < TSubclassOf < UGameplayTaskResource > >` | - |
| `Priority` | `uint8` | - |
| `TaskInstanceName` | `FName` | - |

**Returns**

| Type | Description |
|---|---|
| `UGameplayTask_ClaimResource *` | - |

## Language

`cpp`
