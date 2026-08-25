---
id: "api:class:UBTDecorator_KeepInCone"
title: "UBTDecorator_KeepInCone"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_KeepInCone.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_KeepInCone

Cooldown decorator node.
  A decorator node that bases its condition on whether the observed position is still inside a cone. The cone's direction is calculated when the node first becomes relevant.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConeHalfAngle` | `float` | max allowed time for execution of underlying node |
| `ConeOrigin` | `FBlackboardKeySelector` | blackboard key selector |
| `Observed` | `FBlackboardKeySelector` | blackboard key selector |
| `bUseSelfAsOrigin` | `uint32` | - |
| `bUseSelfAsObserved` | `uint32` | - |

## Language

`cpp`
