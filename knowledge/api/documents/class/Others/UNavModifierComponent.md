---
id: "api:class:UNavModifierComponent"
title: "UNavModifierComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UNavModifierComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UNavModifierComponent

## Inheritance

`UNavRelevantComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AreaClass` | `TSubclassOf < UNavArea >` | - |
| `FailsafeExtent` | `FVector` | box extent used ONLY when owning actor doesn't have collision component |

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
