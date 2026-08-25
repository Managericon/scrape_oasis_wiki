---
id: "api:class:UGCGenericCharacterSystem"
title: "UGCGenericCharacterSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCGenericCharacterSystem.json"
category: "API Wiki/class/和平全局接口/怪物系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCGenericCharacterSystem

怪物系统接口库

## Functions

### `KillGenericCharacter`

```text
KillGenericCharacter(GenericCharacter: AUGCGenericCharacter)
```

强制杀死怪物
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `IsAlive`

```text
IsAlive(GenericCharacter: AUGCGenericCharacter) -> boolean
```

小怪是否存活
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 小怪是否存活 |

### `IsGenericCharacter`

```text
IsGenericCharacter(Target: AActor) -> boolean
```

目标是否为小怪
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Target` | `AActor` | 目标 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否为小怪 |

### `GetHealth`

```text
GetHealth(GenericCharacter: AUGCGenericCharacter) -> number
```

获取小怪血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量 |

### `GetHealthMax`

```text
GetHealthMax(GenericCharacter: AUGCGenericCharacter) -> number
```

获取小怪血量上限
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量上限 |

### `SetHealth`

```text
SetHealth(GenericCharacter: AUGCGenericCharacter, Health: number)
```

设置小怪血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Health` | `number` | 血量 |

### `SetHealthMax`

```text
SetHealthMax(GenericCharacter: AUGCGenericCharacter, HealthMax: number)
```

设置小怪血量上限
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `HealthMax` | `number` | 血量上限 |

### `EnableMovement`

```text
EnableMovement(GenericCharacter: AUGCGenericCharacter)
```

启动移动能力
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `DisableMovement`

```text
DisableMovement(GenericCharacter: AUGCGenericCharacter)
```

关闭移动能力
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `SetAvoidanceGroup`

```text
SetAvoidanceGroup(GenericCharacter: AUGCGenericCharacter, AvoidanceGroup: EGenericAvoidanceGroup)
```

设置避障组
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `AvoidanceGroup` | `EGenericAvoidanceGroup` | 避障组 |

### `MoveTo`

```text
MoveTo(GenericCharacter: AUGCGenericCharacter, InDestination: FVector, InStopRadius: number)
```

移动到目标位置(注意不要和行为树移动冲突)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InDestination` | `FVector` | 目的地 |
| `InStopRadius` | `number` | 停止距离 |

### `StopMove`

```text
StopMove(GenericCharacter: AUGCGenericCharacter)
```

停止移动(注意不要和行为树移动冲突)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

### `GetCurrentVelocity`

```text
GetCurrentVelocity(GenericCharacter: AUGCGenericCharacter) -> FVector
```

获取当前怪物动量
生效范围：服务器/客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 当前动量 |

### `SetMaxSpeed`

```text
SetMaxSpeed(GenericCharacter: AUGCGenericCharacter, InSpeed: number, Reason: number)
```

设置最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InSpeed` | `number` | 速度 |
| `Reason` | `number` | 原因 |

### `GetMaxSpeed`

```text
GetMaxSpeed(GenericCharacter: AUGCGenericCharacter) -> number
```

获取最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 最大移动速度 |

### `GetDefaultMaxSpeed`

```text
GetDefaultMaxSpeed(GenericCharacter: AUGCGenericCharacter) -> number
```

获取默认最大移动速度
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 默认最大移动速度 |

### `GetTargetEnemy`

```text
GetTargetEnemy(GenericCharacter: AUGCGenericCharacter) -> AActor
```

获取当前仇恨目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 当前仇恨对象 |

### `RunBehavior`

```text
RunBehavior(GenericCharacter: AUGCGenericCharacter, BehaviorTreePath: string)
```

运行指定行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `BehaviorTreePath` | `string` | 行为树路径 |

### `StopBehavior`

```text
StopBehavior(GenericCharacter: AUGCGenericCharacter, Reason: string)
```

停止当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Reason` | `string` | 原因 |

### `OverrideBehaviorTreeSetting`

```text
OverrideBehaviorTreeSetting(GenericCharacter: AUGCGenericCharacter, InBehaviorTreeSetting: FBehaviorTreeReflectSetting)
```

覆盖行为树设置并重新启动行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InBehaviorTreeSetting` | `FBehaviorTreeReflectSetting` | 新的行为树设置 |

### `GetBehaviorTreeSetting`

```text
GetBehaviorTreeSetting(GenericCharacter: AUGCGenericCharacter) -> FBehaviorTreeReflectSetting
```

获取当前行为树设置
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |

**Returns**

| Type | Description |
|---|---|
| `FBehaviorTreeReflectSetting` | - |

### `PauseBehavior`

```text
PauseBehavior(GenericCharacter: AUGCGenericCharacter, Reason: string)
```

暂停当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Reason` | `string` | 原因 |

### `ResumeBehavior`

```text
ResumeBehavior(GenericCharacter: AUGCGenericCharacter, Reason: string)
```

继续当前行为树
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Reason` | `string` | 原因 |

### `PlayAnimMontage`

```text
PlayAnimMontage(GenericCharacter: AUGCGenericCharacter, AnimMontage: UAnimMontage, InPlayRate: number)
```

播放蒙太奇动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `AnimMontage` | `UAnimMontage` | 蒙太奇动画 |
| `InPlayRate` | `number` | 播放速率 |

### `PlayAnimMontageByTag`

```text
PlayAnimMontageByTag(GenericCharacter: AUGCGenericCharacter, AnimGameplayTag: FGameplayTag, InPlayRate: number)
```

通过Tag播放蒙太奇动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `AnimGameplayTag` | `FGameplayTag` | 蒙太奇动画Tag |
| `InPlayRate` | `number` | 播放速率 |

### `AddOverrideAnimAsset`

```text
AddOverrideAnimAsset(GenericCharacter: AUGCGenericCharacter, Data: FGenericCharacterAnimOverrideData, BlendTime: number)
```

覆盖指定Tag的动画资源
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Data` | `FGenericCharacterAnimOverrideData` | 覆写数据 |
| `BlendTime` | `number` | 混合时间 |

### `RemoveOverrideAnimAsset`

```text
RemoveOverrideAnimAsset(GenericCharacter: AUGCGenericCharacter, Data: FGenericCharacterAnimOverrideData, BlendTime: number)
```

移除覆盖指定Tag的动画资源
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `Data` | `FGenericCharacterAnimOverrideData` | 覆写数据 |
| `BlendTime` | `number` | 混合时间 |

### `IsEnableLogicPart`

```text
IsEnableLogicPart(GenericCharacter: AUGCGenericCharacter, InLogicPartTag: FGameplayTag) -> boolean
```

是否启用LogicPart
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GenericCharacter` | `AUGCGenericCharacter` | 怪物 |
| `InLogicPartTag` | `FGameplayTag` | LogicPart Tag |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否启用 |

### `SpawnGenericCharacter`

```text
SpawnGenericCharacter(WorldContextObject: UObject, GenericCharacterClass: UClass, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GenericCharacterClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `SpawnGenericCharacterByGroup`

```text
SpawnGenericCharacterByGroup(WorldContextObject: UObject, GroupID: number, Location: FVector, Rotation: FRotator) -> AActor
```

在目标位置根据怪物组表中的ID刷一个怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪的位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |

**Returns**

| Type | Description |
|---|---|
| `AActor` | 刷出的怪物 |

### `RangeSpawnGenericCharacters`

```text
RangeSpawnGenericCharacters(WorldContextObject: UObject, GenericCharacterClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GenericCharacterClass` | `UClass` | 怪物的类 |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnGenericCharactersByGroup`

```text
RangeSpawnGenericCharactersByGroup(WorldContextObject: UObject, GroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, Count: number) -> table
```

在指定位置的圆形范围中寻找合适的地面刷出指定数量的怪，怪物类型由怪物组表ID指定
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GroupID` | `number` | 怪物组表中的ID |
| `Location` | `FVector` | 刷怪范围的中心位置 |
| `Rotation` | `FRotator` | 刷出怪物的朝向 |
| `Range` | `number` | 刷怪圆形范围的半径 |
| `HeightRange` | `number` | 怪物刷出位置与中心位置的最大高度差 |
| `Count` | `number` | 刷出怪物的数量 |

**Returns**

| Type | Description |
|---|---|
| `table` | 刷出怪物的列表 |

### `RangeSpawnGenericCharactersOnTime`

```text
RangeSpawnGenericCharactersOnTime(WorldContextObject: UObject, GenericCharacterClass: UClass, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每隔一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GenericCharacterClass` | `UClass` | 怪物类 |
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

### `RangeSpawnGenericCharactersByGroupOnTime`

```text
RangeSpawnGenericCharactersByGroupOnTime(WorldContextObject: UObject, GroupID: number, Location: FVector, Rotation: FRotator, Range: number, HeightRange: number, MinSpawnCountPerLoop: number, MaxSpawnCountPerLoop: number, LoopTimes: number, IntervalMinTime: number, IntervalMaxTime: number, FirstDelayTime: number, Callback: function, CallbackSelf: table)
```

在指定位置的圆形范围中每个一定时间寻找合适的地面刷出一定数量的怪
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject` | 世界上下文对象 |
| `GroupID` | `number` | 怪物组表中的ID |
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

### `GetPartTypeSockets`

```text
GetPartTypeSockets(Character: ACharacter) -> UPartTypeSocket[]
```

获取角色骨骼里所有的PartTypeSocket
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ACharacter` | 角色 |

**Returns**

| Type | Description |
|---|---|
| `UPartTypeSocket[]` | PartTypeSocket列表 |

### `GetBlackboard`

```text
GetBlackboard(Actor: AActor) -> UBlackboardComponent
```

获取Actor的BlackboardComponent
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | Actor |

**Returns**

| Type | Description |
|---|---|
| `UBlackboardComponent` | BlackboardComponent |

## Language

`lua`
