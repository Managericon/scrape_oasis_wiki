---
id: "api:class:UBaseMediaSource"
title: "UBaseMediaSource"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBaseMediaSource.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBaseMediaSource

Base class for concrete media sources.

## Inheritance

`UMediaSource`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerName` | `FName` | Name of the desired native media player (Empty = find one automatically). |
| `PlatformPlayerNames` | `TMap < FString , FName >` | Override native media player plug-ins per platform (Empty = find one automatically). |

## Language

`cpp`
