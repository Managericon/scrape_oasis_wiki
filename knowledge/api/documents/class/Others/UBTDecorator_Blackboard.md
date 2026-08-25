---
id: "api:class:UBTDecorator_Blackboard"
title: "UBTDecorator_Blackboard"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_Blackboard.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_Blackboard

Blackboard decorator node.
  A decorator node that bases its condition on a Blackboard key.

## Inheritance

`UBTDecorator_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IntValue` | `int32` | value for arithmetic operations |
| `FloatValue` | `float` | value for arithmetic operations |
| `StringValue` | `FString` | value for string operations |
| `CachedDescription` | `FString` | cached description |
| `OperationType` | `uint8` | operation type |
| `NotifyObserver` | `TEnumAsByte < EBTBlackboardRestart :: Type >` | when observer can try to request abort? |

## Language

`cpp`
