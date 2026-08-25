---
id: "api:class:UAnimationAsset"
title: "UAnimationAsset"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimationAsset.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimationAsset

## Inheritance

`UObject` -> `IInterface_AssetUserData`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AnimAssetUID` | `int32` | - |
| `Skeleton` | `USkeleton *` | Pointer to the Skeleton this asset can be played on . |
| `MetaData` | `TArray < UAnimMetaData * >` | Meta data that can be saved with the asset <br>	  <br>	  You can query by GetMetaData function |
| `AssetUserData` | `TArray < UAssetUserData * >` | Array of user data stored with the asset |
| `bUseBoneRetarget` | `bool` | - |

## Language

`cpp`
