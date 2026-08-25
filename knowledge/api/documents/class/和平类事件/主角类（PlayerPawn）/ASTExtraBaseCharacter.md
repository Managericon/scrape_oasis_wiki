---
id: "api:class:ASTExtraBaseCharacter"
title: "ASTExtraBaseCharacter"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E4%B8%BB%E8%A7%92%E7%B1%BB%EF%BC%88PlayerPawn%EF%BC%89/ASTExtraBaseCharacter.json"
category: "API Wiki/class/和平类事件/主角类（PlayerPawn）"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASTExtraBaseCharacter

主角类（PlayerPawn）

## Inheritance

`ASTExtraCharacter` -> `ISTExtraInputInterface` -> `IPickupProxyFactory` -> `ISTExtraBaseCharacter_UGCEventInterface` -> `IGISPlayerInterface` -> `IGenericAbilityCarrierInterface` -> `IItemSkillV2RecevierInterface` -> `IInteractorInterface` -> `IDamageNumberInterface` -> `IMeleeAttackOwnerInterface`

## Functions

### `DSTeleportToLocationOrRotation`

```text
DSTeleportToLocationOrRotation(location: FVector, rotation: FRotator, setLoc: bool, setRot: bool, ResetVelocity: bool, bRecordTeleportInfo: bool) -> void
```

生效范围：服务器
	  传送主角，只有服务器上调用生效，客户端调用无效

**Parameters**

| Name | Type | Description |
|---|---|---|
| `location` | `FVector` | 位置 |
| `rotation` | `FRotator` | 旋转 |
| `setLoc` | `bool` | 是否修改位置 |
| `setRot` | `bool` | 是否修改旋转 |
| `ResetVelocity` | `bool` | 是否重置速度 |
| `bRecordTeleportInfo` | `bool` | 是否记录传送时间用于射击校验，如无特殊需求保持默认配置 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Events

### `UGC_WeaponShootBulletEvent`

```text
UGC_WeaponShootBulletEvent(ShootWeapon: ASTExtraShootWeapon *, Bullet: ASTExtraShootWeaponBulletBase *) -> void
```

发射子弹事件
	 生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShootWeapon` | `ASTExtraShootWeapon *` | 射击武器 |
| `Bullet` | `ASTExtraShootWeaponBulletBase *` | 子弹 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponBulletHitEvent`

```text
UGC_WeaponBulletHitEvent(ShootWeapon: ASTExtraShootWeapon *, Bullet: ASTExtraShootWeaponBulletBase *, HitInfo: FHitResult) -> void
```

子弹命中事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ShootWeapon` | `ASTExtraShootWeapon *` | 射击武器 |
| `Bullet` | `ASTExtraShootWeaponBulletBase *` | 子弹 |
| `HitInfo` | `FHitResult` | 命中信息 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ChangeCurrentUsingWeaponEvent`

```text
UGC_ChangeCurrentUsingWeaponEvent(UsingWeaponSlot: ESurviveWeaponPropSlot, LastSlot: ESurviveWeaponPropSlot) -> void
```

当前武器变化事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UsingWeaponSlot` | `ESurviveWeaponPropSlot` | 当前武器插槽 |
| `LastSlot` | `ESurviveWeaponPropSlot` | 上次武器插槽 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_EquipWeaponEvent`

```text
UGC_EquipWeaponEvent(Slot: ESurviveWeaponPropSlot) -> void
```

装备武器事件，仅装备在身上，非当前手持武器
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Slot` | `ESurviveWeaponPropSlot` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponStartFireEvent`

```text
UGC_WeaponStartFireEvent(isAuto: ESTEWeaponShootType :: type) -> void
```

开火调用事件，仅在按下开火时调用一次
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `isAuto` | `ESTEWeaponShootType :: type` | 是否自动开火 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponStopFireEvent`

```text
UGC_WeaponStopFireEvent() -> void
```

停火调用事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_WeaponSwitchEvent`

```text
UGC_WeaponSwitchEvent() -> void
```

切换武器事件
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ReloadStartEvent`

```text
UGC_ReloadStartEvent() -> void
```

开始换弹事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_ReloadEndEvent`

```text
UGC_ReloadEndEvent() -> void
```

换弹结束事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OpenScopeEvent`

```text
UGC_OpenScopeEvent() -> void
```

开镜事件
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_CloseScopeEvent`

```text
UGC_CloseScopeEvent() -> void
```

开镜结束事件
	 生效范围C

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_EnterPawnStateEvent`

```text
UGC_EnterPawnStateEvent(PawnState: EPawnState) -> void
```

进入某个PawnState事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PawnState` | `EPawnState` | 进入的PawnState |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_LeavePawnStateEvent`

```text
UGC_LeavePawnStateEvent(PawnState: EPawnState) -> void
```

离开某个PawnState事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PawnState` | `EPawnState` | 离开的PawnState |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerPickUpEvent`

```text
UGC_PlayerPickUpEvent() -> void
```

玩家拾取事件
	 生效范围SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PlayerDeadEvent`

```text
UGC_PlayerDeadEvent(Killer: AController *, DamageType: EDamageType :: DamageType) -> void
```

玩家死亡事件
	 生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Killer` | `AController *` | 把该角色淘汰的玩家 |
| `DamageType` | `EDamageType :: DamageType` | 伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_TakeDamageOverrideEvent`

```text
UGC_TakeDamageOverrideEvent(Damage: float, DamageType: EDamageType :: DamageType, EventInstigator: AController *, DamageCauser: AActor *, Hit: FHitResult) -> float
```

重载伤害事件，返回值为修改后的伤害
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Damage` | `float` | 伤害类型 |
| `DamageType` | `EDamageType :: DamageType` | 造成伤害的玩家 |
| `EventInstigator` | `AController *` | 造成伤害的玩家 |
| `DamageCauser` | `AActor *` | 把该角色淘汰的玩家 |
| `Hit` | `FHitResult` | 伤害命中信息 |

**Returns**

| Type | Description |
|---|---|
| `float` | 修改后伤害值 |

## Language

`cpp`
