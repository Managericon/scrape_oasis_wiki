---
id: "api:class:UBTDecorator_IsAtLocation"
title: "UBTDecorator_IsAtLocation"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_IsAtLocation.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_IsAtLocation

Is At Location decorator node.
  A decorator node that checks if AI controlled pawn is at given location.

## Inheritance

`UBTDecorator_BlackboardBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AcceptableRadius` | `float` | distance threshold to accept as being at location |
| `ParametrizedAcceptableRadius` | `FAIDataProviderFloatValue` | - |
| `GeometricDistanceType` | `FAIDistanceType` | - |
| `bUseParametrizedRadius` | `uint32` | - |
| `bUseNavAgentGoalLocation` | `uint32` | if moving to an actor and this actor is a nav agent, then we will move to their nav agent location |
| `bPathFindingBasedTest` | `uint32` | If true the result will be consistent with tests done while following paths.<br>	 	Set to false to use geometric distance as configured with DistanceType |

## Language

`cpp`
