---
id: "api:class:UGCSceneQueryUtility"
title: "UGCSceneQueryUtility"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCSceneQueryUtility.json"
category: "API Wiki/class/和平全局接口/工具库"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCSceneQueryUtility

环境查询工具库

## Functions

### `QueryByLineSingle`

```text
QueryByLineSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用射线执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果，是否找到 |

### `QueryByLineMulti`

```text
QueryByLineMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用射线执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryBySphereSingle`

```text
QueryBySphereSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用球体执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 球体半径（默认值：100） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果数组，是否找到 |

### `QueryBySphereMulti`

```text
QueryBySphereMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用球体执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 球体半径（默认值：100） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryByBoxSingle`

```text
QueryByBoxSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, HalfSize: FVector, Orientation: FRotator, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用盒子执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `HalfSize` | `FVector` | 各轴到盒子中心的距离（默认值：X = 25, Y = 25, Z = 25） |
| `Orientation` | `FRotator` | 盒子朝向（默认值：Pitch = 0, Yaw = 0, Roll = 0） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果数组，是否找到 |

### `QueryByBoxMulti`

```text
QueryByBoxMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, HalfSize: FVector, Orientation: FRotator, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用盒子执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线起点 |
| `End` | `FVector` | 射线终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `HalfSize` | `FVector` | 各轴到盒子中心的距离（默认值：X = 25, Y = 25, Z = 25） |
| `Orientation` | `FRotator` | 盒子朝向（默认值：Pitch = 0, Yaw = 0, Roll = 0） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryByCapsuleSingle`

```text
QueryByCapsuleSingle(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, HalfHeight: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult
```

使用胶囊执行一次环境查询（单个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 胶囊起点 |
| `End` | `FVector` | 胶囊终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 胶囊半径（默认值：100） |
| `HalfHeight` | `number` | 胶囊高度（默认值：50） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult` | 查询结果数组，是否找到 |

### `QueryByCapsuleMulti`

```text
QueryByCapsuleMulti(WorldContextObject: UObject, Start: FVector, End: FVector, QueryType: ESceneQueryType, Radius: number, HalfHeight: number, ActorsToIgnore: AActor[], IgnoreSelf: boolean) -> FHitResult[]
```

使用胶囊执行一次环境查询（多个目标）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 胶囊起点 |
| `End` | `FVector` | 胶囊终点 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 胶囊半径（默认值：100） |
| `HalfHeight` | `number` | 胶囊高度（默认值：50） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `IgnoreSelf` | `boolean` | 是否忽略自身（默认值：true） |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 查询结果数组，是否找到 |

### `QueryOverlapActorsBySphere`

```text
QueryOverlapActorsBySphere(WorldContextObject: UObject, Position: FVector, QueryType: ESceneQueryType, Radius: number, ActorsToIgnore: AActor[], ActorClassFilter: UClass, OutActors: AActor[]) -> AActor[]
```

使用球体检测重叠的Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Position` | `FVector` | 球体中心位置 |
| `QueryType` | `ESceneQueryType` | 环境查询类型 |
| `Radius` | `number` | 球体半径（默认值：100） |
| `ActorsToIgnore` | `AActor[]` | 忽略的 Actor 列表（默认值：空） |
| `ActorClassFilter` | `UClass` | Actor类型过滤器（默认值：nil） |
| `OutActors` | `AActor[]` | 输出的Actor数组（如果为nil则创建新数组） |

**Returns**

| Type | Description |
|---|---|
| `AActor[]` | 是否找到重叠的Actor，重叠的Actor数组 |

### `QueryByBoxMultiForObjects`

```text
QueryByBoxMultiForObjects(WorldContextObject: UObject, Start: FVector, End: FVector, HalfSize: FVector, Orientation: FRotator, ObjectTypes: EObjectTypeQuery[], bTraceComplex: boolean, ActorsToIgnore: AActor[], DrawDebugType: EDrawDebugTrace, OutHits: FHitResult[], bIgnoreSelf: boolean, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: number) -> FHitResult[]
```

返回所有跟Box沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `HalfSize` | `FVector` | Box边的半长尺寸 |
| `Orientation` | `FRotator` | Box的朝向 |
| `ObjectTypes` | `EObjectTypeQuery[]` | 要检测的对象类型数组 |
| `bTraceComplex` | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `AActor[]` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace` | 绘制调试类型 |
| `OutHits` | `FHitResult[]` | 存储所有碰撞结果 |
| `bIgnoreSelf` | `boolean` | 是否忽略自身 |
| `TraceColor` | `FLinearColor` | 未命中时的调试线颜色 |
| `TraceHitColor` | `FLinearColor` | 命中时的调试线颜色 |
| `DrawTime` | `number` | 绘制时间 |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 是否检测到碰撞，碰撞结果数组 |

### `QueryOverlapActorsBySphereWithFinder`

```text
QueryOverlapActorsBySphereWithFinder(WorldContextObject: UObject, Finder: AActor, Origin: FVector, Radius: number, Channel: ECollisionChannel) -> FHitResult[]
```

在指定位置和半径的球体范围内检测所有重叠的Actor对象

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Finder` | `AActor` | 检测发起者，不被检测 |
| `Origin` | `FVector` | 球体中心位置 |
| `Radius` | `number` | 球体半径 |
| `Channel` | `ECollisionChannel` | 碰撞通道，默认为ECollisionChannel.ECC_WorldDynamic |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 碰撞结果数组 |

### `QueryBlocksByChannel`

```text
QueryBlocksByChannel(WorldContextObject: UObject, Start: FVector, End: FVector, OutHits: FHitResult[], IgnoreActors: AActor[], TraceChannels: ECollisionChannel[]) -> FHitResult[]
```

检测从起点到终点之间所有阻挡物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `OutHits` | `FHitResult[]` | 存储所有碰撞结果 |
| `IgnoreActors` | `AActor[]` | 需要忽略的Actor列表 |
| `TraceChannels` | `ECollisionChannel[]` | 需要检测的碰撞通道数组 |

**Returns**

| Type | Description |
|---|---|
| `FHitResult[]` | 是否检测到碰撞，碰撞结果数组 |

### `QueryBySphereMultiForObjects`

```text
QueryBySphereMultiForObjects(WorldContextObject: UObject, Start: FVector, End: FVector, Radius: number, ObjectTypes: EObjectTypeQuery[], bTraceComplex: boolean, ActorsToIgnore: AActor[], DrawDebugType: EDrawDebugTrace, OutHits: FHitResult[], bIgnoreSelf: boolean, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: number) -> boolean
```

返回所有跟球体沿射线移动扫过区域碰撞物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `Radius` | `number` | 扫描球体的半径 |
| `ObjectTypes` | `EObjectTypeQuery[]` | 对象类型列表 |
| `bTraceComplex` | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `AActor[]` | 要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace` | 调试模式 |
| `OutHits` | `FHitResult[]` | 碰撞结果列表，按从起点到终点的检测顺序排序。如果存在阻挡性碰撞，它将是列表中的最后一个碰撞结果 |
| `bIgnoreSelf` | `boolean` | 是否忽略自身 |
| `TraceColor` | `FLinearColor` | 未命中时的调试线颜色 |
| `TraceHitColor` | `FLinearColor` | 命中时的调试线颜色 |
| `DrawTime` | `number` | 调试线的持续时间 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 如果发生碰撞返回true，否则返回false |

### `QueryByLineMultiForObjects`

```text
QueryByLineMultiForObjects(WorldContextObject: UObject, Start: FVector, End: FVector, ObjectTypes: EObjectTypeQuery[], bTraceComplex: boolean, ActorsToIgnore: AActor[], DrawDebugType: EDrawDebugTrace, OutHits: FHitResult[], bIgnoreSelf: boolean, TraceColor: FLinearColor, TraceHitColor: FLinearColor, DrawTime: number) -> boolean
```

返回所有跟射线碰撞的物体的碰撞信息，只查询指定对象类型

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | world上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `ObjectTypes` | `EObjectTypeQuery[]` | 对象类型列表 |
| `bTraceComplex` | `boolean` | true为复杂碰撞检测，false为简单碰撞检测 |
| `ActorsToIgnore` | `AActor[]` | 需要忽略的Actor列表 |
| `DrawDebugType` | `EDrawDebugTrace` | 调试模式 |
| `OutHits` | `FHitResult[]` | 输出的HitResult列表 |
| `bIgnoreSelf` | `boolean` | 是否忽略自身 |
| `TraceColor` | `FLinearColor` | 未命中时的调试线颜色 |
| `TraceHitColor` | `FLinearColor` | 命中时的调试线颜色 |
| `DrawTime` | `number` | 调试线的持续时间 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true为检测到碰撞，false为未检测到碰撞 |

### `QueryByLineWithChannel`

```text
QueryByLineWithChannel(OutHit: FHitResult, ContextObject: UObject, Start: FVector, End: FVector, IgnoreActors: AActor[], TraceChannel: ECollisionChannel) -> boolean
```

返回指定通道的射线碰撞的物体的碰撞信息

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutHit` | `FHitResult` | 输出的HitResult |
| `ContextObject` | `UObject` | world上下文对象 |
| `Start` | `FVector` | 射线检测起点 |
| `End` | `FVector` | 射线检测终点 |
| `IgnoreActors` | `AActor[]` | 需要忽略的Actor列表 |
| `TraceChannel` | `ECollisionChannel` | 碰撞通道 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true为检测到碰撞，false为未检测到碰撞 |

### `FindPositionToHoldCapsule`

```text
FindPositionToHoldCapsule(WorldContextObject: UObject, SourceLocation: FVector, CapsuleRotation: FRotator, CapsuleRadius: float, CapsuleHalfHeight: float, IgnoreActors: AActor[], DetectObjectTypes: EObjectTypeQuery[], Iterations: int, bNearestLocation: bool) -> boolean, FVector
```

获取一个目标位置附近能容纳胶囊体的坐标，以目标位置为中心，八方向向外迭代寻找位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | World上下文 |
| `SourceLocation` | `FVector` | 目标位置 |
| `CapsuleRotation` | `FRotator` | 胶囊体的旋转 |
| `CapsuleRadius` | `float` | 胶囊体半径 |
| `CapsuleHalfHeight` | `float` | 胶囊体半高 |
| `IgnoreActors` | `AActor[]` | 需要忽略的Actor列表 |
| `DetectObjectTypes` | `EObjectTypeQuery[]` | 检测的对象类型列表 |
| `Iterations` | `int` | 检测迭代次数 |
| `bNearestLocation` | `bool` | 是否返回最近的位置 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否找到合适的位置 |
| `FVector` | 找到的坐标 |

## Language

`lua`
