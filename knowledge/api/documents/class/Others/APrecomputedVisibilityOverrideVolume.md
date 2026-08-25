---
id: "api:class:APrecomputedVisibilityOverrideVolume"
title: "APrecomputedVisibilityOverrideVolume"
source: "https://developer.gp.qq.com/api/class/detail/Others/APrecomputedVisibilityOverrideVolume.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# APrecomputedVisibilityOverrideVolume

## Inheritance

`AVolume`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OverrideVisibleActors` | `TArray < AActor * >` | Array of actors that will always be considered visible by Precomputed Visibility when viewed from inside this volume. |
| `OverrideInvisibleActors` | `TArray < AActor * >` | Array of actors that will always be considered invisible by Precomputed Visibility when viewed from inside this volume. |
| `OverrideInvisibleLevels` | `TArray < FName >` | Array of level names whose actors will always be considered invisible by Precomputed Visibility when viewed from inside this volume. |

## Language

`cpp`
