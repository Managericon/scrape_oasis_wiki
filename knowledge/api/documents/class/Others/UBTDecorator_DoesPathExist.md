---
id: "api:class:UBTDecorator_DoesPathExist"
title: "UBTDecorator_DoesPathExist"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_DoesPathExist.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_DoesPathExist

Cooldown decorator node.
  A decorator node that bases its condition on whether a path exists between two points from the Blackboard.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BlackboardKeyA` | `FBlackboardKeySelector` | blackboard key selector |
| `BlackboardKeyB` | `FBlackboardKeySelector` | blackboard key selector |
| `bUseSelf` | `uint32` | - |
| `PathQueryType` | `TEnumAsByte < EPathExistanceQueryType :: Type >` | - |
| `FilterClass` | `TSubclassOf < UNavigationQueryFilter >` | "None" will result in default filter being used |

## Language

`cpp`
