---
id: "api:class:UGameEngine"
title: "UGameEngine"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameEngine.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameEngine

Engine that manages core systems that enable a game.

## Inheritance

`UEngine`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxDeltaTime` | `float` | Maximium delta time the engine uses to populate FApp::DeltaTime. If 0, unbound. |
| `ServerFlushLogInterval` | `float` | Maximium time (in seconds) between the flushes of the logs on the server (best effort). If 0, this will happen every tick. |
| `GameInstance` | `UGameInstance *` | - |

## Language

`cpp`
