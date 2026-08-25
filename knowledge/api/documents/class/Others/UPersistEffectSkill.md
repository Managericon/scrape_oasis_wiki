---
id: "api:class:UPersistEffectSkill"
title: "UPersistEffectSkill"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPersistEffectSkill.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPersistEffectSkill

技能实体

## Inheritance

`UPersistEffectWithState` -> `ISkillObjectInterface` -> `IPESkillTaskTrackConditionFilterInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PESkillSlot` | `FGameplayTag` | 技能槽位Tag |
| `ApplyTagGroup` | `FGameplayTagGroups` | Tag的配置组，包含该技能与各个Tag的互斥关系 |
| `CustomActivateConditions` | `FPESkillConditionContainer` | 技能激活自定义条件 |
| `ConsumeTime` | `EPESkillConsumeTimeType` | CD能量和消耗扣除时机 |
| `SkillCD` | `FPESkillCDWapper` | 技能CD |
| `CostConsume` | `FPESkillConsume` | 技能消耗 |
| `UIInfo` | `FPESkillUIInfo` | 技能外显信息 |
| `SkillGroup` | `FGameplayTag` | 技能组，同组互斥，不能同时激活同组的技能，如果填空的话则没有任何互斥关系 |
| `bDefaultEnable` | `bool` | 默认是否可用，如果配置了false，则需要调用enable才能激活技能 |

## Functions

### `EnableSkill`

```text
EnableSkill() -> void
```

生效范围：S
	  使技能可用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DisableSkill`

```text
DisableSkill() -> void
```

生效范围：S
	  使技能不可用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsSkillEnable`

```text
IsSkillEnable() -> bool
```

生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否可用 |

### `DeActivateSkill`

```text
DeActivateSkill(Reason: EPESkillDeActivateReason) -> void
```

生效范围：SC
	  取消技能释放

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EPESkillDeActivateReason` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanActivateSkill`

```text
CanActivateSkill() -> bool
```

生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否可用 |

### `ActivateSkill`

```text
ActivateSkill() -> void
```

生效范围：SC
	  释放技能

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActivating`

```text
IsActivating() -> bool
```

生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否正在激活 |

### `CheckCDReady`

```text
CheckCDReady() -> bool
```

生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能CD是否已准备好 |

### `CheckCostReady`

```text
CheckCostReady() -> bool
```

生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能需要的消耗是否已准备好 |

### `ConsumeCD`

```text
ConsumeCD() -> bool
```

生效范围：服务器
	  消耗CD

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功消耗 |

### `ConsumeCost`

```text
ConsumeCost() -> bool
```

生效范围：服务器
	  消耗道具

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功消耗 |

### `GetRemainingCDTime`

```text
GetRemainingCDTime() -> float
```

生效范围：服务器&客户端
	  获取CD剩余时间

**Returns**

| Type | Description |
|---|---|
| `float` | 剩余时间 |

### `GetCDRecoveryTime`

```text
GetCDRecoveryTime() -> float
```

生效范围：服务器&客户端
	  获取CD恢复时间

**Returns**

| Type | Description |
|---|---|
| `float` | 剩余时间 |

### `SetCDRecoveryTime`

```text
SetCDRecoveryTime(CDRecoveryTime: float) -> void
```

生效范围：服务器
	  设置CD恢复时间

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CDRecoveryTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCDRecoverRate`

```text
GetCDRecoverRate() -> float
```

生效范围：服务器&客户端
	  获取CD恢复速率

**Returns**

| Type | Description |
|---|---|
| `float` | CD恢复速率 |

### `SetCDRecoverRate`

```text
SetCDRecoverRate(Rate: float) -> void
```

生效范围：服务器
	  设置CD恢复速率

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | CD恢复速率 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChargeCDEnergy`

```text
ChargeCDEnergy(ChargeRate: float) -> void
```

生效范围：服务器
	  恢复CD比例，1代表完全恢复一层CD，大于1代表恢复多层，不超过层数上限

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChargeRate` | `float` | 恢复的层数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ChargeCDTime`

```text
ChargeCDTime(ChargeTime: float) -> void
```

生效范围：服务器
	  恢复CD固定时间，不超过层数上限

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChargeTime` | `float` | 恢复的时间，单位秒 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RefreshCD`

```text
RefreshCD() -> void
```

生效范围：服务器
	  刷新技能CD

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCDMaxLayer`

```text
SetCDMaxLayer(InMaxLayer: int) -> void
```

生效范围：服务器
	  设置CD最大层数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaxLayer` | `int` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OverwriteSkillUIInfo`

```text
OverwriteSkillUIInfo(SkillName: FName, SkillDetail: FString, SkillIconPath: FString) -> void
```

生效范围：服务器&客户端
	  更改UI信息，但双端不同步

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillName` | `FName` | 技能名字 |
| `SkillDetail` | `FString` | 技能描述 |
| `SkillIconPath` | `FString` | 技能图标路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSkillName`

```text
GetSkillName() -> FName
```

生效范围：服务器&客户端
	  获取技能名字

**Returns**

| Type | Description |
|---|---|
| `FName` | 技能名字 |

### `GetSkillDetail`

```text
GetSkillDetail() -> FString
```

生效范围：服务器&客户端
	  获取技能描述

**Returns**

| Type | Description |
|---|---|
| `FString` | 技能描述 |

### `GetSkillIconPath`

```text
GetSkillIconPath() -> FString
```

生效范围：服务器&客户端
	  获取技能图标路径

**Returns**

| Type | Description |
|---|---|
| `FString` | 技能图标路径 |

### `SetShowTipsEnable`

```text
SetShowTipsEnable(bEnable: bool) -> void
```

生效范围：服务器
	  设置是否开启技能激活检查失败显示Tips

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | 是否开启提示 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlayActivateFailedSoundEnable`

```text
SetPlayActivateFailedSoundEnable(bEnable: bool) -> void
```

生效范围：服务器
	  设置是否开启技能激活检查失败播放提示音

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | 是否开启提示 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectTargetActor`

```text
GetSelectTargetActor(SelectType: EPESkillSelectTarget) -> TArray < AActor * >
```

获取技能目标角色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SelectType` | `EPESkillSelectTarget` | 选择类型 |

**Returns**

| Type | Description |
|---|---|
| `TArray < AActor * >` | 技能目标角色 |

### `SetSelectTargetActor`

```text
SetSelectTargetActor(Actors: TArray < AActor * > &) -> void
```

设置技能目标角色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actors` | `TArray < AActor * > &` | Actor数组 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectTargetOneActor`

```text
SetSelectTargetOneActor(pActor: AActor *) -> void
```

设置技能目标角色

**Parameters**

| Name | Type | Description |
|---|---|---|
| `pActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectDirection`

```text
SetSelectDirection(Direction: FVector &) -> void
```

设置技能方向

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Direction` | `FVector &` | 方向 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectDirection`

```text
GetSelectDirection() -> FVector
```

获取技能方向

**Returns**

| Type | Description |
|---|---|
| `FVector` | 技能方向 |

### `GetSelectTransform`

```text
GetSelectTransform() -> const FTransform &
```

获取技能目标位置

**Returns**

| Type | Description |
|---|---|
| `const FTransform &` | 技能目标位置 |

### `SetSelectTransform`

```text
SetSelectTransform(Transform: FTransform &) -> void
```

设置技能目标位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transform` | `FTransform &` | 技能目标位置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSelectTransforms`

```text
SetSelectTransforms(Transforms: TArray < FTransform > &) -> void
```

设置技能多目标位置

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Transforms` | `TArray < FTransform > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSelectTransforms`

```text
GetSelectTransforms() -> const TArray < FTransform > &
```

获取技能多目标位置

**Returns**

| Type | Description |
|---|---|
| `const TArray < FTransform > &` | - |

### `ClearSelectTransforms`

```text
ClearSelectTransforms() -> void
```

清除技能目标位置

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `OnEnableSkill_BP`

```text
OnEnableSkill_BP() -> bool
```

生效范围：服务器
	  技能可用通知

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnDisableSkill_BP`

```text
OnDisableSkill_BP() -> bool
```

生效范围：服务器
	  技能不可用通知

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnActivateSkill_BP`

```text
OnActivateSkill_BP() -> bool
```

生效范围：服务器
	  技能被触发

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `OnDeActivateSkill_BP`

```text
OnDeActivateSkill_BP(Reason: EPESkillDeActivateReason) -> void
```

生效范围：服务器
	  技能结束

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EPESkillDeActivateReason` | 结束原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanActivateSkill_BP`

```text
CanActivateSkill_BP() -> bool
```

生效范围：服务器&客户端
	  技能是否可用

**Returns**

| Type | Description |
|---|---|
| `bool` | 技能是否可释放 |

### `OnCDStateChange_BP`

```text
OnCDStateChange_BP(bIsCD: bool) -> void
```

生效范围：服务器&客户端
	  技能CD状态改变

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsCD` | `bool` | 技能是否CD中 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnUIInfoChange`

```text
OnUIInfoChange() -> void
```

Event
	  生效范围：客户端
	  技能的UI信息改变事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CDStateChangeHandle`

```text
CDStateChangeHandle(IsTrue: bool) -> void
```

Event
	  生效范围：服务器&客户端
	  客户端同步技能CD状态变化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsTrue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
