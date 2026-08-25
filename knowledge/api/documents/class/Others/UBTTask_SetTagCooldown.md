---
id: "api:class:UBTTask_SetTagCooldown"
title: "UBTTask_SetTagCooldown"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTTask_SetTagCooldown.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTTask_SetTagCooldown

Cooldown task node.
  Sets a cooldown tag value.  Use with cooldown tag decorators to prevent behavior tree execution.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | Gameplay tag that will be used for the cooldown. |
| `bAddToExistingDuration` | `bool` | True if we are adding to any existing duration, false if we are setting the duration (potentially invalidating an existing end time). |
| `CooldownDuration` | `float` | Value we will add or set to the Cooldown tag when this task runs. |

## Language

`cpp`
