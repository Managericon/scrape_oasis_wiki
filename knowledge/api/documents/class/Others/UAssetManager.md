---
id: "api:class:UAssetManager"
title: "UAssetManager"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAssetManager.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAssetManager

A singleton UObject that is responsible for loading and unloading PrimaryAssets, and maintaining game-specific asset references
  Games should override this class and change the class reference

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ObjectReferenceList` | `TArray < UObject * >` | List of UObjects that are being kept from being GCd, derived from the asset type map. Arrays are currently more efficient than Sets |
| `bIsGlobalAsyncScanEnvironment` | `bool` | True if we are running a build that is already scanning assets globally so we can perhaps avoid scanning paths synchronously |
| `bShouldGuessTypeAndName` | `bool` | True if PrimaryAssetTypeName will be implied for loading assets that don't have it saved on disk. Won't work for all projects |
| `bShouldUseSynchronousLoad` | `bool` | True if we should always use synchronous loads, this speeds up cooking |
| `bIsLoadingFromPakFiles` | `bool` | True if we are loading from pak files |
| `bShouldAcquireMissingChunksOnLoad` | `bool` | True if the chunk install interface should be queries before loading assets |
| `bOnlyCookProductionAssets` | `bool` | If true, DevelopmentCook assets will error when they are cooked |
| `bIsBulkScanning` | `bool` | True if we are currently in bulk scanning mode |
| `bIsPrimaryAssetDirectoryCurrent` | `bool` | True if asset data is current, if false it will need to rescan before PIE |
| `bIsManagementDatabaseCurrent` | `bool` | True if the asset management database is up to date |
| `bUpdateManagementDatabaseAfterScan` | `bool` | True if the asset management database should be updated after scan completes |
| `bIncludeOnlyOnDiskAssets` | `bool` | True if only on-disk assets should be searched by the asset registry |
| `NumberOfSpawnedNotifications` | `int32` | Number of notifications seen in this update |

## Language

`cpp`
