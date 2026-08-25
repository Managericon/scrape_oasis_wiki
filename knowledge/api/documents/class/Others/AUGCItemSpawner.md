---
id: "api:class:AUGCItemSpawner"
title: "AUGCItemSpawner"
source: "https://developer.gp.qq.com/api/class/detail/Others/AUGCItemSpawner.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUGCItemSpawner

物资刷新系统：物资刷新器

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemConfig` | `FUGCItemSpawnerItemConfig` | 配置刷出的物资类别和数量 |
| `bNeedSpawnerManager` | `bool` | 物资刷新点是否能独立运作，还是依赖于物资刷新管理器 |
| `bLoopSpawn` | `bool` | 独立运作模式时，物资被拾取后是否会自动生成 |
| `SpawnCD` | `float` | 开启循环生成后，物资被拾取后间隔重新刷新 |
| `bTraceGround` | `bool` | 物资是否一定刷新在地面上 |
| `bRandomRotator` | `bool` | 物资方向是否随机 |
| `StartRadius` | `int32` | 物资刷新位置到刷新点的最小距离 |
| `EndRadius` | `int32` | 物资刷新位置到刷新点的最大距离 |

## Functions

### `SpawnItem`

```text
SpawnItem(ItemID: int32, ItemCount: int32) -> AActor *
```

生效范围 服务器
	  刷物资

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ItemID` | `int32` | 物资ID |
| `ItemCount` | `int32` | 物资数量 |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | 刷出的物资 |

### `SetItemConfig`

```text
SetItemConfig(InItemConfig: FUGCItemSpawnerItemConfig) -> void
```

生效范围 服务器
	  修改物资刷新配置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InItemConfig` | `FUGCItemSpawnerItemConfig` | 新的物资刷新配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CleanItems`

```text
CleanItems() -> void
```

生效范围 服务器
	  清除刷出的物资

**Returns**

| Type | Description |
|---|---|
| `void` | 刷出的物资 |

## Events

### `OnItemsSpawn`

```text
OnItemsSpawn(Items: TArray < AActor * > &) -> void
```

生效范围 服务器
	  物资刷出事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Items` | `TArray < AActor * > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAllItemsArePick`

```text
OnAllItemsArePick() -> void
```

生效范围 服务器
	  所有物资都被拾取

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CustomSpawnItem`

```text
CustomSpawnItem(CustomParam: TMap < FString , FString > &) -> TArray < AActor * >
```

生效范围 服务器
	  覆写该事件来自定义物资刷出流程

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CustomParam` | `TMap < FString , FString > &` | 自定义参数列表 |

**Returns**

| Type | Description |
|---|---|
| `TArray < AActor * >` | - |

## Language

`cpp`
