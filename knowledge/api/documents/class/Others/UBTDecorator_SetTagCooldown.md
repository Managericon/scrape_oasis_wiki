---
id: "api:class:UBTDecorator_SetTagCooldown"
title: "UBTDecorator_SetTagCooldown"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_SetTagCooldown.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_SetTagCooldown

Set tag cooldown decorator node.
  A decorator node that sets a gameplay tag cooldown.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | Gameplay tag that will be used for the cooldown. |
| `CooldownDuration` | `float` | Value we will add or set to the Cooldown tag when this task runs. |
| `bAddToExistingDuration` | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |

## Language

`cpp`
