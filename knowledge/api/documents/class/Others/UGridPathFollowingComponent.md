---
id: "api:class:UGridPathFollowingComponent"
title: "UGridPathFollowingComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGridPathFollowingComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGridPathFollowingComponent

Path following augmented with local navigation grids
 
   Keeps track of nearby grids and use them instead of navigation path when agent is inside.
   Once outside grid, regular path following is resumed.
 
   This allows creating dynamic navigation obstacles with fully static navigation (e.g. static navmesh),
   as long as they are minor modifications for path. Not recommended for blocking off entire corridors.
 
   Does not replace proper avoidance for dynamic obstacles!

## Inheritance

`UPathFollowingComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `GridManager` | `UNavLocalGridManager *` | - |

## Language

`cpp`
