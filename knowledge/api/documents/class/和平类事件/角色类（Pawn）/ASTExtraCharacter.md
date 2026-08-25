---
id: "api:class:ASTExtraCharacter"
title: "ASTExtraCharacter"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%A7%92%E8%89%B2%E7%B1%BB%EF%BC%88Pawn%EF%BC%89/ASTExtraCharacter.json"
category: "API Wiki/class/和平类事件/角色类（Pawn）"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASTExtraCharacter

角色类

## Inheritance

`AUAECharacter` -> `IUAESkillInterface` -> `ISTBaseBuffCarrierInterface` -> `IDamageableInterface` -> `IWeaponOwnerInterface` -> `IWeaponOwnerProxyFactory` -> `IAttrModifyInterface` -> `IItemGenerateInterface` -> `IObjectPoolInterface` -> `IActorHiddenInterface` -> `ILaserSeekAndLockOwnerInterface` -> `IBulletHitInterface` -> `IGameAttributeCarrierInterface` -> `IPickerEffectInterface` -> `ICustomMovementInterface` -> `IGenericCharacterInterface` -> `ITargetFilterInfoProviderInterface` -> `IStateAbilityInterface` -> `IOwnershipChainInterface` -> `IFieldApplyInterface` -> `ICharacterTypeInterface`

## Events

### `UGC_GetDamageNumberConfigIndex`

```text
UGC_GetDamageNumberConfigIndex(Damage: float, bHeadShot: bool, EventInstigator: AController *, DamageCauser: AActor *, DamageTypeID: int32) -> int32
```

获取伤害数字配置索引
	  生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 伤害数值 |
| `bHeadShot` | `bool` | 是否爆头 |
| `EventInstigator` | `AController *` | 伤害来源Controller |
| `DamageCauser` | `AActor *` | 伤害来源物体 |
| `DamageTypeID` | `int32` | 伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `UGC_PreTakeDamageEvent`

```text
UGC_PreTakeDamageEvent(Damage: float, EventInstigator: AController *, DamageEvent: FDamageEvent, DamageCauser: AActor *) -> float
```

受到伤害前，返回值可以修改伤害值
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 当前伤害值， |
| `EventInstigator` | `AController *` | - |
| `DamageEvent` | `FDamageEvent` | 伤害类型 |
| `DamageCauser` | `AActor *` | 把该角色淘汰的玩家 |

**Returns**

| Type | Description |
|---|---|
| `float` | 修改后伤害值 |

## Delegates

### `UGC_OnHPChangedDelegate`

```text
UGC_OnHPChangedDelegate(HP: float, HPChanged: float) -> void
```

Delegate
	 生效范围SC
	 怪物血量变化

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HP` | `float` | 当前血量 |
| `HPChanged` | `float` | 血量变化值 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnTakeDamageDelegate`

```text
UGC_OnTakeDamageDelegate(Damage: float, EventInstigator: AController*, DamageEvent: FDamageEvent, DamageCauser: AActor*) -> void
```

Delegate
	 生效范围S
	 受到伤害后

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 当前伤害值， |
| `EventInstigator` | `AController*` | - |
| `DamageEvent` | `FDamageEvent` | 伤害类型 |
| `DamageCauser` | `AActor*` | 把该角色淘汰的玩家 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
