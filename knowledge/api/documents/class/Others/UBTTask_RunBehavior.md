---
id: "api:class:UBTTask_RunBehavior"
title: "UBTTask_RunBehavior"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunBehavior.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTTask_RunBehavior

RunBehavior task allows pushing subtrees on execution stack.
  Subtree asset can't be changed in runtime! 
 
  This limitation is caused by support for subtree's root level decorators,
  which are injected into parent tree, and structure of running tree
  cannot be modified in runtime (see: BTNode: ExecutionIndex, MemoryOffset)
 
  Use RunBehaviorDynamic task for subtrees that need to be changed in runtime.

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BehaviorAsset` | `UBehaviorTree *` | behavior to run |

## Language

`cpp`
