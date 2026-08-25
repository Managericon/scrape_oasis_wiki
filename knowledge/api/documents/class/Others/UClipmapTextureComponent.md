---
id: "api:class:UClipmapTextureComponent"
title: "UClipmapTextureComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UClipmapTextureComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UClipmapTextureComponent

Component used to place a URuntimeVirtualTexture in the world.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ClipmapTexture` | `UClipmapTexture *` | - |
| `bUseForCDLODMatID` | `bool` | - |
| `BoundsSourceActor` | `AActor *` | Actor to copy the bounds from to set up the transform. |
| `MipToDis` | `TMap < int32 , float >` | - |
| `ClipmapInfo` | `FVector4` | - |

## Functions

### `SetTransformToBounds`

```text
SetTransformToBounds() -> void
```

Set this component transform to include the BoundsSourceActor bounds. Called by our UI details customization.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshClipmapInfo`

```text
RefreshClipmapInfo() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
