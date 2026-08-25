---
id: "api:class:UNavRelevantComponent"
title: "UNavRelevantComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UNavRelevantComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UNavRelevantComponent

## Inheritance

`UActorComponent` -> `INavRelevantInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAttachToOwnersRoot` | `uint32` | attach navigation data to entry for owner's root component (depends on its relevancy) |
| `CachedNavParent` | `UObject *` | - |

## Functions

### `SetNavigationRelevancy`

```text
SetNavigationRelevancy(bRelevant: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bRelevant` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
