---
id: "api:class:UBTDecorator_ConeCheck"
title: "UBTDecorator_ConeCheck"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_ConeCheck.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_ConeCheck

Cone check decorator node.
  A decorator node that bases its condition on a cone check, using Blackboard entries to form the parameters of the check.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConeHalfAngle` | `float` | Angle between cone direction and code cone edge, or a half of the total cone angle |
| `ConeOrigin` | `FBlackboardKeySelector` | blackboard key selector |
| `ConeDirection` | `FBlackboardKeySelector` | "None" means "use ConeOrigin's direction" |
| `Observed` | `FBlackboardKeySelector` | blackboard key selector |

## Language

`cpp`
