---
id: "api:class:UBTDecorator_Loop"
title: "UBTDecorator_Loop"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTDecorator_Loop.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTDecorator_Loop

Loop decorator node.
  A decorator node that bases its condition on whether its loop counter has been exceeded.

## Inheritance

`UBTDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NumLoops` | `int32` | number of executions |
| `bInfiniteLoop` | `bool` | infinite loop |
| `InfiniteLoopTimeoutTime` | `float` | timeout (when looping infinitely, when we finish a loop we will check whether we have spent this time looping, if we have we will stop looping). A negative value means loop forever. |

## Language

`cpp`
