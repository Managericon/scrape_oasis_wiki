---
id: "api:class:ULevelStreaming"
title: "ULevelStreaming"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULevelStreaming.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULevelStreaming

Abstract base class of container object encapsulating data required for streaming and providing 
  interface for when a level should be streamed in and out of memory.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PackageName_DEPRECATED` | `FName` | Deprecated name of the package containing the level to load. Use GetWorldAsset() or GetWorldAssetPackageFName() instead. |
| `WorldAsset` | `TSoftObjectPtr < UWorld >` | The reference to the world containing the level to load |
| `PackageNameToLoad` | `FName` | If this isn't Name_None, then we load from this package on disk to the new package named PackageName |
| `LODPackageNames` | `TArray < FName >` | LOD versions of this level |
| `LevelTransform` | `FTransform` | Transform applied to actors after loading. |
| `bShouldBeVisibleInEditor` | `uint32` | Whether this level should be visible in the Editor |
| `bLocked` | `uint32` | Whether this level is locked; that is, its actors are read-only. |
| `bShouldBeLoaded` | `uint32` | Whether the level should be loaded |
| `bShouldBeVisible` | `uint32` | Whether the level should be visible if it is loaded |
| `bIsStatic` | `uint32` | Whether this level only contains static actors that aren't affected by gameplay or replication.<br>	  If true, the engine can make certain optimizations and will add this level to the StaticLevels collection. |
| `bShouldBlockOnLoad` | `uint32` | Whether we want to force a blocking load |
| `LevelLODIndex` | `int32` | Requested LOD. Non LOD sub-levels have Index = -1 |
| `bDisableDistanceStreaming` | `uint32` | Whether this level streaming object should be ignored by world composition distance streaming, <br>	   so streaming state can be controlled by other systems (ex: in blueprints) |
| `bDrawOnLevelStatusMap` | `uint32` | If true, will be drawn on the 'level streaming status' map (STAT LEVELMAP console command) |
| `DrawColor_DEPRECATED` | `FColor` | Deprecated level color used for visualization. |
| `LevelColor` | `FLinearColor` | The level color used for visualization. (Show -> Advanced -> Level Coloration) |
| `EditorStreamingVolumes` | `TArray < ALevelStreamingVolume * >` | The level streaming volumes bound to this level. |
| `MinTimeBetweenVolumeUnloadRequests` | `float` | Cooldown time in seconds between volume-based unload requests.  Used in preventing spurious unload requests. |
| `Keywords` | `TArray < FString >` | List of keywords to filter on in the level browser |
| `LoadedLevel` | `ULevel *` | Pointer to Level object if currently loaded streamed in. |
| `PendingUnloadLevel` | `ULevel *` | Pointer to a Level object that was previously active and was replaced with a new LoadedLevel (for LOD switching) |
| `UnloadingLevels` | `TArray < ULevel * >` | Array to save unloading levels. |
| `LevelStreamingInfo` | `FLevelLoadConditionInfo` | - |
| `FolderPath` | `FName` | The folder path for this level within the world browser. This is only available in editor builds. <br>		A NONE path indicates that it exists at the root. It is '' separated. |

## Functions

### `GetWorldAssetPackageFName`

```text
GetWorldAssetPackageFName() -> ENGINE_API FName
```

Gets the package name for the world asset referred to by this level streaming as an FName

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FName` | - |

### `GetLoadedLevel`

```text
GetLoadedLevel() -> ENGINE_API class ULevel *
```

Gets a pointer to the LoadedLevel value

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API class ULevel *` | - |

### `IsLevelVisible`

```text
IsLevelVisible() -> ENGINE_API bool
```

Returns whether streaming level is visible

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `IsLevelLoaded`

```text
IsLevelLoaded() -> ENGINE_API bool
```

Returns whether streaming level is loaded

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `IsStreamingStatePending`

```text
IsStreamingStatePending() -> ENGINE_API bool
```

Returns whether level has streaming state change pending

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API bool` | - |

### `CreateInstance`

```text
CreateInstance(UniqueInstanceName: FString) -> ULevelStreaming *
```

Creates a new instance of this streaming level with a provided unique instance name

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UniqueInstanceName` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `ULevelStreaming *` | - |

### `GetLevelScriptActor`

```text
GetLevelScriptActor() -> ENGINE_API ALevelScriptActor *
```

Returns the Level Script Actor of the level if the level is loaded and valid

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API ALevelScriptActor *` | - |

## Delegates

### `OnLevelLoaded`

```text
OnLevelLoaded() -> void
```

Called when level is streamed in

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLevelUnloaded`

```text
OnLevelUnloaded() -> void
```

Called when level is streamed out

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLevelShown`

```text
OnLevelShown() -> void
```

Called when level is added to the world

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLevelHidden`

```text
OnLevelHidden() -> void
```

Called when level is removed from the world

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
