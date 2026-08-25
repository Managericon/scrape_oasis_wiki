---
id: "api:class:UBTDecorator_CheckGameplayTagsOnActor"
title: "UBTDecorator_CheckGameplayTagsOnActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_CheckGameplayTagsOnActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_CheckGameplayTagsOnActor

GameplayTag decorator node.
  A decorator node that bases its condition on whether the specified Actor (in the blackboard) has a Gameplay Tag or
  Tags specified.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ActorToCheck` | `FBlackboardKeySelector` | - |
| `TagsToMatch` | `EGameplayContainerMatchType` | - |
| `GameplayTags` | `FGameplayTagContainer` | - |
| `CachedDescription` | `FString` | cached description |

## Language

`cpp`
