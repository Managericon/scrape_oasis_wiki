---
id: "api:class:UBTComposite_Selector"
title: "UBTComposite_Selector"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTComposite_Selector.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTComposite_Selector

Selector composite node.
  Selector Nodes execute their children from left to right, and will stop executing its children when one of their children succeeds.
  If a Selector's child succeeds, the Selector succeeds. If all the Selector's children fail, the Selector fails.

## Inheritance

`UBTCompositeNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bRunChildrenInSameFrame` | `uint8` | if set, instant (non-latent) child tasks of this selector are run within the same frame<br>	   instead of being deferred to the next tick. Latent tasks (InProgress) break the chain. |

## Language

`cpp`
