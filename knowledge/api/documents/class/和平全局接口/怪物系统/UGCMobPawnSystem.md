---
id: "api:class:UGCMobPawnSystem"
title: "UGCMobPawnSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCMobPawnSystem.json"
category: "API Wiki/class/和平全局接口/怪物系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCMobPawnSystem

怪物系统接口库

## Functions

### `SpawnMob`

```text
SpawnMob(WorldContextObject: UObject, MobClass: UClass, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `SpawnMobByMobGroup`

```text
SpawnMobByMobGroup(WorldContextObject: UObject, MobGroupID: number, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置根据怪物组表中的ID刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobGroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `RangeSpawnMobs`

```text
RangeSpawnMobs(WorldContextObject: UObject, MobClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnMobsByMobGroup`

```text
RangeSpawnMobsByMobGroup(WorldContextObject: UObject, MobGroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪，怪物类型由怪物组表ID指定
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobGroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnMobsOnTime`

```text
RangeSpawnMobsOnTime(WorldContextObject: UObject, MobClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每隔一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobClass` | `UClass` | 怪物类 |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `MinSpawnCountPerLoop` | `number` | 每次刷怪的最小数量 |
| `MaxSpawnCountPerLoop` | `number` | 每次刷怪的最大数量 |
| `LoopTimes` | `number` | 总的刷怪轮数 |
| `IntervalMinTime` | `number` | 刷怪轮次间的最小时间间隔 |
| `IntervalMaxTime` | `number` | 刷怪轮次间的最大时间间隔 |
| `FirstDelayTime` | `number` | 从接口调用到首次刷怪的延迟时间 |
| `Callback` | `function` | 回调函数 |
| `CallbackSelf` | `table` | 回调函数的调用主体，静态函数时留空 |

### `RangeSpawnMobsByMobGroupOnTime`

```text
RangeSpawnMobsByMobGroupOnTime(WorldContextObject: UObject, MobGroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每个一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `MobGroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `MinSpawnCountPerLoop` | `number` | 每次刷怪的最小数量 |
| `MaxSpawnCountPerLoop` | `number` | 每次刷怪的最大数量 |
| `LoopTimes` | `number` | 总的刷怪轮数 |
| `IntervalMinTime` | `number` | 刷怪轮次间的最小时间间隔 |
| `IntervalMaxTime` | `number` | 刷怪轮次间的最大时间间隔 |
| `FirstDelayTime` | `number` | 从接口调用到首次刷怪的延迟时间 |
| `Callback` | `function` | 回调函数 |
| `CallbackSelf` | `table` | 回调函数的调用主体，静态函数时留空 |

## Language

`lua`
