---
id: "api:class:AUGCMobSpawnerManager"
title: "AUGCMobSpawnerManager"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/AUGCMobSpawnerManager.json"
category: "API Wiki/class/和平全局接口/怪物系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUGCMobSpawnerManager

刷怪系统：刷怪管理器

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `StartCondition` | `EUGCMobSpawnerManagerStartCondition` | 配置刷怪管理器的启动方式 |
| `EventName` | `FString` | 启动方式使用事件触发时，监听的GMP名 |
| `MaxSpawnPerFrame` | `int32` | 配置刷怪管理器每帧刷怪的上限 |
| `AliveMobsCheckDeltaTime` | `float` | 配置刷怪管理器检查当前怪物存活情况的间隔 |
| `SpawnWaves` | `TArray < FUGCSpawnWave >` | 配置刷怪的波次 |

## Functions

### `StartSpawnerManager`

```text
StartSpawnerManager() -> void
```

生效范围 服务器
	  启动刷怪管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetSpawnerManager`

```text
ResetSpawnerManager(bDeleteAllMobs: bool) -> void
```

生效范围 服务器
	  重置刷怪管理器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDeleteAllMobs` | `bool` | 是否清除所有刷出的怪物 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllMobs`

```text
CleanAllMobs(bDelete: bool) -> void
```

生效范围 服务器
	  清理对刷出怪物的引用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bDelete` | `bool` | 是否清除怪物 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PauseSpawnerManager`

```text
PauseSpawnerManager() -> void
```

生效范围 服务器
	  暂停刷怪管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResumeSpawnerManager`

```text
ResumeSpawnerManager() -> void
```

生效范围 服务器
	  恢复刷怪管理器

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSpawner`

```text
GetSpawner(WaveIndex: int32, SpawnerIndex: int32) -> AUGCMobSpawner *
```

生效范围 服务器
	  获取波次中特定编号的刷怪点

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | 波次编号 |
| `SpawnerIndex` | `int32` | 刷新点编号 |

**Returns**

| Type | Description |
|---|---|
| `AUGCMobSpawner *` | 怪物刷新点 |

### `GetCurrentWaveIndex`

```text
GetCurrentWaveIndex() -> int32
```

生效范围 服务器
	  获取当前波的波次编号

**Returns**

| Type | Description |
|---|---|
| `int32` | 当前波次编号 |

### `GetWaveSpawnerNum`

```text
GetWaveSpawnerNum(WaveIndex: int32) -> int32
```

生效范围 服务器
	  获取对应波次的刷新点数量

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | 刷新点数量 |

### `GetWaveNum`

```text
GetWaveNum() -> int32
```

生效范围 服务器
	  获取波次的数量

**Returns**

| Type | Description |
|---|---|
| `int32` | 波次数量 |

### `SetMobConfigOverrideForSpawner`

```text
SetMobConfigOverrideForSpawner(InMobConfig: FUGCMobSpawnerMobConfig, WaveIndex: int32, SpawnerIndex: int32) -> void
```

生效范围 服务器
	  修改特定波次中特定刷新点的怪物配置覆盖

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMobConfig` | `FUGCMobSpawnerMobConfig` | 新的怪物配置 |
| `WaveIndex` | `int32` | 波次编号 |
| `SpawnerIndex` | `int32` | 刷新点编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMobConfigOverrideForWave`

```text
SetMobConfigOverrideForWave(InMobConfig: FUGCMobSpawnerMobConfig, WaveIndex: int32) -> void
```

生效范围 服务器
	  修改特定波次中所有刷新点的怪物配置覆盖

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMobConfig` | `FUGCMobSpawnerMobConfig` | 新的怪物配置 |
| `WaveIndex` | `int32` | 波次编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMobConfigOverride`

```text
SetMobConfigOverride(InMobConfig: FUGCMobSpawnerMobConfig) -> void
```

生效范围 服务器
	  修改所有波次的怪物配置覆盖

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMobConfig` | `FUGCMobSpawnerMobConfig` | 新的怪物配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanAllMobConfigOverride`

```text
CleanAllMobConfigOverride() -> void
```

生效范围 服务器
	  清除管理器所有的怪物配置覆盖

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `JumpToWave`

```text
JumpToWave(WaveIndex: int32) -> void
```

生效范围 服务器
	  跳转到指定波次

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnMobSpawn`

```text
OnMobSpawn(Mob: AActor *) -> void
```

生效范围 服务器
	  怪物刷出事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mob` | `AActor *` | 刷出的怪物 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaveStart`

```text
OnWaveStart(WaveIndex: int32) -> void
```

生效范围 服务器
	  刷怪波次开始事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | 波次编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWaveEnd`

```text
OnWaveEnd(WaveIndex: int32) -> void
```

生效范围 服务器
	  刷怪波次结束事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WaveIndex` | `int32` | 波次编号 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllWaveEnd`

```text
OnAllWaveEnd() -> void
```

生效范围 服务器
	  所有波次结束事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllMobDie`

```text
OnAllMobDie() -> void
```

生效范围 服务器
	  所以波次怪物都已刷新并死亡事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
