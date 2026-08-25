---
id: "api:class:AUGCMobCharacter"
title: "AUGCMobCharacter"
source: "https://developer.gp.qq.com/api/class/detail/Others/AUGCMobCharacter.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUGCMobCharacter

怪物角色类

## Inheritance

`ACharacter` -> `IObjectPoolInterface` -> `IDamageableInterface` -> `IAttrModifyInterface` -> `IGameAttributeCarrierInterface` -> `IRegionObjectInterface` -> `IBulletEffectInterface` -> `IBulletHitInterface` -> `IUGCCharacterAnimPlayInterfaceBase` -> `ICommonAIInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Health` | `float` | 当前生命值 |
| `HealthAddScale` | `float` | 加血速率 |
| `HealthMax` | `float` | 最大生命值 |
| `bInvincible` | `int` | 是否无敌 |
| `SkillCDRecoverRate` | `FGameAttributeProperty` | 技能急速，值越大技能冷却越快结束 |
| `IsShowDamageNum` | `bool` | 是否显示伤害数字 |
| `HealthBarWidget` | `UUGCCharacterPositionWidget *` | 血条的蓝图类 |
| `bIsShowHealthBar` | `bool` | 是否显示血条 |
| `ShowName` | `FName` | 血条上显示的名字 |
| `PlayBeHitedAnimTimeInterval` | `float` | 受击动画播放最小间隔，小于受击动画长度时无效 |
| `bNeedDestroyOnDeath` | `bool` | 是否启用尸体消失后延迟销毁 |
| `DisappearOnDeathLifeSpan` | `float` | 尸体消失后延迟多久销毁 |
| `DelayRemoveDeadBody` | `float` | 死亡后尸体存在时间 |
| `BornTime` | `float` | 出生状态持续时间 |
| `StunDuration` | `float` | 硬直状态持续时间 |
| `UGCGeneralMoveSpeedScale` | `float` | 移动速度倍率 |
| `AttackMeActorRemainTime` | `float` | 活动范围，处于活动范围外时索敌无效，仇恨随时间消失<br>	 <br>	 UGC<br>	  处于活动范围外时仇恨持续时间 |
| `SpawnLoc` | `FVector` | 出生地点 |
| `bOutOfActivityRange` | `bool` | 是否在活动范围外 |

## Functions

### `IsAlive`

```text
IsAlive() -> bool
```

是否存活

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsInvincible`

```text
IsInvincible() -> FORCEINLINE int
```

是否无敌

**Returns**

| Type | Description |
|---|---|
| `FORCEINLINE int` | - |

### `ForceDie`

```text
ForceDie() -> void
```

生效范围 服务器
	  强制杀死怪物

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentSpeed`

```text
GetCurrentSpeed() -> float
```

生效范围 服务器&客户端
	  获取当前速度值

**Returns**

| Type | Description |
|---|---|
| `float` | float 当前速度值 |

### `GetVelocity`

```text
GetVelocity() -> FVector
```

生效范围 服务器&客户端
	  获取当前速度向量

**Returns**

| Type | Description |
|---|---|
| `FVector` | FVector 当前速度向量 |

## Events

### `PreTakeDamageEvent`

```text
PreTakeDamageEvent(DamageCauser: AActor *, EventInstigator: AController *, Damage: float, DamageContext: FGameMagnitudeContext &) -> void
```

生效范围 服务器
	  小怪即将受到伤害前事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamageCauser` | `AActor *` | 伤害来源 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `Damage` | `float` | - |
| `DamageContext` | `FGameMagnitudeContext &` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PostTakeDamageEvent`

```text
PostTakeDamageEvent(DamageCauser: AActor *, EventInstigator: AController *, Damage: float, DamageContext: FGameMagnitudeContext &) -> void
```

生效范围 服务器
	  受到伤害后事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DamageCauser` | `AActor *` | 伤害来源 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `Damage` | `float` | - |
| `DamageContext` | `FGameMagnitudeContext &` | 伤害事件上下文 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PreOverrideDamageValue`

```text
PreOverrideDamageValue(Damage: float, DamageType: int32, EventInstigator: AController *, DamageCauser: AActor *, Hit: FHitResult &) -> float
```

生效范围 服务器
	  伤害值覆盖事件,在全局伤害公式前

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `int32` | 伤害类型 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `DamageCauser` | `AActor *` | 伤害来源 |
| `Hit` | `FHitResult &` | 命中信息 |

**Returns**

| Type | Description |
|---|---|
| `float` | 覆盖后的伤害值 |

### `PostOverrideDamageValue`

```text
PostOverrideDamageValue(Damage: float, DamageType: int32, EventInstigator: AController *, DamageCauser: AActor *, Hit: FHitResult &) -> float
```

生效范围 服务器
	  伤害值覆盖事件,在全局伤害公式后

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | - |
| `DamageType` | `int32` | 伤害类型 |
| `EventInstigator` | `AController *` | 伤害来源的Controller |
| `DamageCauser` | `AActor *` | 伤害来源 |
| `Hit` | `FHitResult &` | 命中信息 |

**Returns**

| Type | Description |
|---|---|
| `float` | 覆盖后的伤害值 |

### `MobPawnDeadEvent`

```text
MobPawnDeadEvent(Killer: AController *, DamageCauser: AActor *, KillingHitDamageType: EDamageType :: DamageType) -> void
```

生效范围 服务器&客户端
	  怪物死亡事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Killer` | `AController *` | 把该小怪杀死的角色的Controller |
| `DamageCauser` | `AActor *` | 杀死该小怪的角色 |
| `KillingHitDamageType` | `EDamageType :: DamageType` | 最后一击的伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StateChangeEvent`

```text
StateChangeEvent(OldState: EUGCMobState, NewState: EUGCMobState) -> void
```

生效范围 服务器&客户端
	  状态变化事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldState` | `EUGCMobState` | 变化前状态 |
| `NewState` | `EUGCMobState` | 变化后状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
