---
id: "api:class:UAISense"
title: "UAISense"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAISense.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAISense

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefaultExpirationAge` | `float` | age past which stimulus of this sense are "forgotten" |
| `NotifyType` | `EAISenseNotifyType` | - |
| `bWantsNewPawnNotification` | `uint32` | whether this sense is interested in getting notified about new Pawns being spawned <br>	 	this can be used for example for automated sense sources registration |
| `bAutoRegisterAllPawnsAsSources` | `uint32` | If true all newly spawned pawns will get auto registered as source for this sense. |
| `PerceptionSystemInstance` | `UAIPerceptionSystem *` | - |

## Language

`cpp`
