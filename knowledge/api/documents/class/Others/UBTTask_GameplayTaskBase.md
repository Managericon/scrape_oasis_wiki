---
id: "api:class:UBTTask_GameplayTaskBase"
title: "UBTTask_GameplayTaskBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTTask_GameplayTaskBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTTask_GameplayTaskBase

Base class for managing gameplay tasks
  Since AITask doesn't have any kind of successfailed results, default implemenation will only return EBTNode::Succeeded
 
  In your ExecuteTask:
  - use NewBTAITask() helper to create task
  - initialize task with values if needed
  - use StartGameplayTask() helper to execute and get node result

## Inheritance

`UBTTaskNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bWaitForGameplayTask` | `uint32` | if set, behavior tree task will wait until gameplay tasks finishes |

## Language

`cpp`
