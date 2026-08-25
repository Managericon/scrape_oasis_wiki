---
id: "api:class:UBTDecorator_TagCooldown"
title: "UBTDecorator_TagCooldown"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_TagCooldown.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_TagCooldown

Cooldown decorator node.
  A decorator node that bases its condition on whether a cooldown timer based on a gameplay tag has expired.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | Gameplay tag that will be used for the cooldown. |
| `CooldownDuration` | `float` | Value we will add or set to the Cooldown tag when this node is deactivated. |
| `bAddToExistingDuration` | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |
| `bActivatesCooldown` | `bool` | Whether or not we are addingsetting to the cooldown tag's value when the decorator deactivates. |

## Language

`cpp`
