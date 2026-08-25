---
id: "api:class:UDemoNetDriver"
title: "UDemoNetDriver"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDemoNetDriver.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDemoNetDriver

Simulated network driver for recording and playing back game sessions.

## Inheritance

`UNetDriver`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RollbackNetStartupActors` | `TMap < FString , FRollbackNetStartupActorInfo >` | Net startup actors that need to be rolled back during scrubbing by being destroyed and re-spawned <br>	  NOTE - DeletedNetStartupActors will take precedence here, and destroy the actor instead |
| `CheckpointSaveMaxMSPerFrame` | `float` | Maximum time allowed each frame to spend on saving a checkpoint. If 0, it will save the checkpoint in a single frame, regardless of how long it takes.<br>	  See also demo.CheckpointSaveMaxMSPerFrameOverride. |
| `bIsLocalReplay` | `bool` | - |
| `GameInstance` | `UGameInstance *` | - |

## Language

`cpp`
