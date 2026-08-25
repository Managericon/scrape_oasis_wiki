---
id: "api:class:APlayerStart"
title: "APlayerStart"
source: "https://developer.gp.qq.com/api/class/detail/Others/APlayerStart.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# APlayerStart

This class indicates a location where a player can spawn when the game begins

## Inheritance

`ANavigationObjectBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PlayerStartTag` | `FName` | ~ To take more control over PlayerStart selection, you can override the virtual AGameModeBase::FindPlayerStart and AGameModeBase::ChoosePlayerStart functions. <br>	 Used when searching for which playerstart to use. |
| `ArrowComponent` | `UArrowComponent *` | Arrow component to indicate forward direction of start |

## Language

`cpp`
