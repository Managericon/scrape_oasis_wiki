---
id: "api:class:USoundNodeLooping"
title: "USoundNodeLooping"
source: "https://developer.gp.qq.com/api/class/detail/Others/USoundNodeLooping.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USoundNodeLooping

Defines how a sound loops; either indefinitely, or for a set number of times.
  Note: The Looping node should only be used for logical or procedural looping such as introducing a delay.
  These sounds will not be played seamlessly. If you want a sound to loop seamlessly and indefinitely,
  use the Looping flag on the Wave Player node for that sound.

## Inheritance

`USoundNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LoopCount` | `int32` | The amount of times to loop |
| `bLoopIndefinitely` | `uint32` | If enabled, the node will continue to loop indefinitely regardless of the Loop Count value. |

## Language

`cpp`
