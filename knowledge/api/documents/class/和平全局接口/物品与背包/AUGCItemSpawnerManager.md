---
id: "api:class:AUGCItemSpawnerManager"
title: "AUGCItemSpawnerManager"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/AUGCItemSpawnerManager.json"
category: "API Wiki/class/和平全局接口/物品与背包"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUGCItemSpawnerManager

生成系统：物资生成管理器

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartCondition` | `EUGCItemSpawnerManagerStartCondition` | 管理器的启动方式 |
| `EventName` | `FString` | 启动方式选择事件触发时，监听的GMP事件名 |
| `ItemSpawners` | `TArray < FUGCItemSpawnerInfo >` | 配置刷新点 |
| `MaxWaveInternalTime` | `float` | 配置两次刷新之间的最大时间间隔 |
| `MinWaveInternalTime` | `float` | 配置两次刷新之间的最小时间间隔 |
| `MaxSpawnerNumPerWave` | `int32` | 配置同一时间有物资刷出的刷新点的最大数量 |
| `MinSpawnerNumPerWave` | `int32` | 配置同一时间有物资刷出的刷新点的最小数量 |
| `TotalSpawnWaveCount` | `int32` | 物资刷新的总轮数，设为-1则无限刷新 |
| `bOverrideItemConfig` | `bool` | 是否覆盖所有刷新点上的物资配置 |
| `ItemConfig` | `FUGCItemSpawnerItemConfig` | 配置所有刷新点上的物资配置 |

## Functions

### `StartSpawnerManager`

```text
StartSpawnerManager() -> void
```

生效范围 服务器
	  启动管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSpawnerManager`

```text
ResetSpawnerManager() -> void
```

生效范围 服务器
	  重置管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllItem`

```text
CleanAllItem() -> void
```

生效范围 服务器
	  清理刷出的物资

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseSpawnerManager`

```text
PauseSpawnerManager() -> void
```

生效范围 服务器
	  暂停物资刷新管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumeSpawnerManager`

```text
ResumeSpawnerManager() -> void
```

生效范围 服务器
	  恢复物资刷新管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetItemConfigOverrideForSpawner`

```text
SetItemConfigOverrideForSpawner(InItemConfig: FUGCItemSpawnerItemConfig, SpawnerIndex: int32) -> void
```

生效范围 服务器
	  修改特定刷新点的物资配置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemConfig` | `FUGCItemSpawnerItemConfig` | 新的物资刷新配置 |
| `SpawnerIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetItemConfigOverride`

```text
SetItemConfigOverride(InItemConfig: FUGCItemSpawnerItemConfig) -> void
```

生效范围 服务器
	  修改所有刷新点的物资配置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemConfig` | `FUGCItemSpawnerItemConfig` | 新的物资刷新配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllItemConfigOverride`

```text
CleanAllItemConfigOverride() -> void
```

生效范围 服务器
	  清除刷新点的物资配置设置，调用后将使用刷新点本身的配置

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnItemsSpawn`

```text
OnItemsSpawn(Items: TArray < AActor * > &) -> void
```

生效范围 服务器
	  物品刷新

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Items` | `TArray < AActor * > &` | 本轮刷新的物品 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
