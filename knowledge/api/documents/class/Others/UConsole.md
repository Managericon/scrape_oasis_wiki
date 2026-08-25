---
id: "api:class:UConsole"
title: "UConsole"
source: "https://developer.gp.qq.com/api/class/detail/Others/UConsole.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UConsole

A basic command line console that accepts most commands.

## Inheritance

`UObject` -> `FOutputDevice`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConsoleTargetPlayer` | `ULocalPlayer *` | The player which the next console command should be executed in the context of.  If nullptr, execute in the viewport. |
| `DefaultTexture_Black` | `UTexture2D *` | - |
| `DefaultTexture_White` | `UTexture2D *` | - |
| `HistoryBuffer` | `TArray < FString >` | Holds the history buffer, order is old to new |

## Language

`cpp`
