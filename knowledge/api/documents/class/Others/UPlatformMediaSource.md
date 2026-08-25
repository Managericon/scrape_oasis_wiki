---
id: "api:class:UPlatformMediaSource"
title: "UPlatformMediaSource"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPlatformMediaSource.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPlatformMediaSource

A media source that selects other media sources based on target platform.
 
  Use this asset to override media sources on a per-platform basis.

## Inheritance

`UMediaSource`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | Default media source.<br>	 <br>	  This media source will be used if no source was specified for a target platform. |
| `PlatformMediaSources` | `TMap < FString , UMediaSource * >` | Media sources per platform. |

## Language

`cpp`
