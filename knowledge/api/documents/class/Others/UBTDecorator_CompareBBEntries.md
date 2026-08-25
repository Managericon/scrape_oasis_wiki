---
id: "api:class:UBTDecorator_CompareBBEntries"
title: "UBTDecorator_CompareBBEntries"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_CompareBBEntries.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_CompareBBEntries

Blackboard comparison decorator node.
  A decorator node that bases its condition on a comparison between two Blackboard keys.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Operator` | `TEnumAsByte < EBlackBoardEntryComparison :: Type >` | operation type |
| `BlackboardKeyA` | `FBlackboardKeySelector` | blackboard key selector |
| `BlackboardKeyB` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`
