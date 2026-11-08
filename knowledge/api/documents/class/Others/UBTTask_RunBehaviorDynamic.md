---
id: "api:class:UBTTask_RunBehaviorDynamic"
title: "UBTTask_RunBehaviorDynamic"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTTask_RunBehaviorDynamic.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTTask_RunBehaviorDynamic

RunBehaviorDynamic task allows pushing subtrees on execution stack.
  Subtree asset can be assigned at runtime with SetDynamicSubtree function of BehaviorTreeComponent.
 
  Does NOT support subtree's root level decorators!

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InjectionTag` | `FGameplayTag` | Gameplay tag that will identify this task for subtree injection |
| `DefaultBehaviorAsset` | `UBehaviorTree *` | default behavior to run |
| `BehaviorAsset` | `UBehaviorTree *` | current subtree |
| `bRunSubtreeInSameFrame` | `uint8` | if set, this task acts as an instant node: pushing the subtree no longer breaks the parent<br>	   composite's same-frame chain, so the subtree can start within the same frame.<br>	   Needs the parent composite to opt in via bRunChildrenInSameFrame.<br>	   Only affects this node; the subtree's own children are governed by the subtree's composites. |

## Language

`cpp`
