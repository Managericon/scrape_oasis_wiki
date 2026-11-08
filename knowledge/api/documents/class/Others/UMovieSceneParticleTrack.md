---
id: "api:class:UMovieSceneParticleTrack"
title: "UMovieSceneParticleTrack"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneParticleTrack.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneParticleTrack

Handles triggering of particle emitters

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bEnableLoopRetrigger` | `bool` | 是否启用范围式触发策略（新实现）。<br>	  默认关闭（false），走原始触发逻辑（老实现）。<br>	  需要同时 CVar Seq.EnableParticleLoopRetrigger 开启时才生效。 |
| `ParticleSections` | `TArray < UMovieSceneSection * >` | List of all particle sections. |

## Language

`cpp`
