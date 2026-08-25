---
id: "api:class:ANavModifierVolume"
title: "ANavModifierVolume"
source: "https://developer.gp.qq.com/api/class/detail/Others/ANavModifierVolume.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ANavModifierVolume

Allows applying selected AreaClass to navmesh, using Volume's shape

## Inheritance

`AVolume` -> `INavRelevantInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AreaClass` | `TSubclassOf < UNavArea >` | - |

## Functions

### `SetAreaClass`

```text
SetAreaClass(NewAreaClass: TSubclassOf < UNavArea >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAreaClass` | `TSubclassOf < UNavArea >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
