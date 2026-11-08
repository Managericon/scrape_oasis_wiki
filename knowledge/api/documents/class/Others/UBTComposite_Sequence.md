---
id: "api:class:UBTComposite_Sequence"
title: "UBTComposite_Sequence"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTComposite_Sequence.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTComposite_Sequence

Sequence composite node.
  Sequence Nodes execute their children from left to right, and will stop executing its children when one of their children fails.
  If a child fails, then the Sequence fails. If all the Sequence's children succeed, then the Sequence succeeds.

## Inheritance

`UBTCompositeNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bRunChildrenInSameFrame` | `uint8` | if set, instant (non-latent) child tasks of this sequence are run within the same frame<br>	   instead of being deferred to the next tick. Latent tasks (InProgress) break the chain. |

## Language

`cpp`
