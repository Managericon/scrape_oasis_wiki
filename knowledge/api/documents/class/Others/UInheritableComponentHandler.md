---
id: "api:class:UInheritableComponentHandler"
title: "UInheritableComponentHandler"
source: "https://developer.gp.qq.com/api/class/detail/Others/UInheritableComponentHandler.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UInheritableComponentHandler

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Records` | `TArray < FComponentOverrideRecord >` | All component records |
| `UnnecessaryComponents` | `TArray < UActorComponent * >` | List of components that were marked unnecessary, need to keep these around so it doesn't regenerate them when a child asks for one |

## Language

`cpp`
