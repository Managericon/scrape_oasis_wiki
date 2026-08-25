---
id: "api:class:UGameplayTagsList"
title: "UGameplayTagsList"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayTagsList.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayTagsList

Base class for storing a list of gameplay tags as an ini list. This is used for both the central list and additional lists

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConfigFileName` | `FString` | Relative path to the ini file that is backing this list |
| `GameplayTagList` | `TArray < FGameplayTagTableRow >` | List of tags saved to this file |

## Language

`cpp`
