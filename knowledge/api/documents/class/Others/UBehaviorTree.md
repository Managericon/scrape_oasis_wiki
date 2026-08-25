---
id: "api:class:UBehaviorTree"
title: "UBehaviorTree"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBehaviorTree.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBehaviorTree

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RootNode` | `UBTCompositeNode *` | root node of loaded tree |
| `BlackboardAsset` | `UBlackboardData *` | blackboard asset for this tree |
| `RootDecorators` | `TArray < UBTDecorator * >` | root level decorators, used by subtrees |
| `RootDecoratorOps` | `TArray < FBTDecoratorLogic >` | logic operators for root level decorators, used by subtrees |

## Language

`cpp`
