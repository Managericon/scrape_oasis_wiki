---
id: "api:class:UWorldComposition"
title: "UWorldComposition"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWorldComposition.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWorldComposition

WorldComposition represents world structure:
 	- Holds list of all level packages participating in this world and theirs base parameters (bounding boxes, offset from origin)
 	- Holds list of streaming level objects to stream in and out based on distance from current view point
   - Handles properly levels repositioning during level loading and saving

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Package2WorldTileExtraInfo` | `TMap < FName , FWorldTileExtraInfo >` | - |
| `LODStealConfigs` | `TArray < FLODStealConfig >` | - |
| `TilesStreaming` | `TArray < ULevelStreaming * >` | - |
| `TilesStreamingTimeThreshold` | `double` | - |
| `bLoadAllTilesDuringCinematic` | `bool` | - |
| `bRebaseOriginIn3DSpace` | `bool` | - |
| `RebaseOriginDistance` | `float` | - |
| `TileBoundsVerifyScale` | `float` | - |
| `bFlushPool` | `bool` | - |
| `ServerExcludedLevels` | `TArray < FString >` | - |
| `ClientExcludedLevels` | `TArray < FString >` | - |
| `UGCPIEMapBlackList` | `TArray < FString >` | - |
| `UGCWhiteListSubLevelPaths` | `TArray < FString >` | - |
| `DeviceExcludedLevels` | `TArray < FString >` | - |
| `DynamicSubLevelPaths` | `TArray < FString >` | - |
| `BlackLevelPaths` | `TArray < FString >` | - |
| `SpecifiedBuildingLevels` | `TArray < FString >` | - |
| `ClientLoadRadiusFactor` | `float` | - |

## Functions

### `CheckBisNeedSavedLevelToFileInServer`

```text
CheckBisNeedSavedLevelToFileInServer() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
