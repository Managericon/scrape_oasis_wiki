---
id: "api:class:ASTExtraShootWeapon"
title: "ASTExtraShootWeapon"
source: "https://developer.gp.qq.com/api/class/detail/Others/ASTExtraShootWeapon.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASTExtraShootWeapon

射击武器类

## Inheritance

`ASTExtraWeapon`

## Delegates

### `OnShootWeaponAutoReloadDel`

```text
OnShootWeaponAutoReloadDel() -> void
```

Delegate
	  生效范围C
	  自动换弹事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCurBulletChange`

```text
OnCurBulletChange() -> void
```

Delegate
	  生效范围SC
	  弹药数量变化事件。注：手动修改会触发开火消耗子弹不触发

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnCurBarrelBulletChangeDelegate`

```text
OnCurBarrelBulletChangeDelegate() -> void
```

Delegate
	  生效范围C
	  膛内弹药数量变化代理

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStartFireDelegate`

```text
OnStartFireDelegate() -> void
```

Delegate
	  生效范围SC
	  开火事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnStopFireDelegate`

```text
OnStopFireDelegate() -> void
```

Delegate
	  生效范围SC
	  停火事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponShootDelegate`

```text
OnWeaponShootDelegate() -> void
```

Delegate
	  生效范围C
	  射击事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponReloadStartDelegate`

```text
OnWeaponReloadStartDelegate() -> void
```

Delegate
	  生效范围SC
	  开始换弹事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponReloadEndDelegage`

```text
OnWeaponReloadEndDelegage() -> void
```

Delegate
	  生效范围SC
	  结束换弹事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponEquipDelegate`

```text
OnWeaponEquipDelegate() -> void
```

Delegate
	  生效范围SC
	  武器装备事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponUnEquipDelegate`

```text
OnWeaponUnEquipDelegate() -> void
```

Delegate
	  生效范围SC
	  武器卸载事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLeftLastBulletWhenReloadOneByOneDelegate`

```text
OnLeftLastBulletWhenReloadOneByOneDelegate(RemainNum: int32) -> void
```

Delegate
	  生效范围SC
	  最后一发换弹通知事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RemainNum` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletHitDelegate`

```text
OnBulletHitDelegate(InHitActor: AActor*, ImpactPosDistanceToWeapon: float, Player: APawn*) -> void
```

Delegate
	  生效范围S
	  射击武器命中事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InHitActor` | `AActor*` | - |
| `ImpactPosDistanceToWeapon` | `float` | - |
| `Player` | `APawn*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnShootIntervalModeChangeDelegate`

```text
OnShootIntervalModeChangeDelegate() -> void
```

Delegate
	  生效范围SC
	  改变射速模式事件（指的是改变了武器拥有的射速模式）

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnChangeAmmoDelegate`

```text
OnChangeAmmoDelegate(AmmoDefineID: FItemDefineID) -> void
```

Delegate
	  生效范围SC
	  切换武器弹药种类事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AmmoDefineID` | `FItemDefineID` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnClipAmmoDataChangeDelegate`

```text
OnClipAmmoDataChangeDelegate() -> void
```

Delegate
	  生效范围SC
	  武器弹夹内弹药数据发生变化事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnExplosionProjectileBulletExplodeDelegate`

```text
OnExplosionProjectileBulletExplodeDelegate(Bullet: AActor*) -> void
```

Delegate
	  生效范围SC
	  炮弹爆炸事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnScopeIn`

```text
OnScopeIn() -> void
```

Delegate
	  生效范围C
	  开镜事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnScopeOut`

```text
OnScopeOut() -> void
```

Delegate
	  生效范围C
	  关镜事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMaxBulletChange`

```text
OnMaxBulletChange() -> void
```

Delegate
	  生效范围SC
	  最大弹药数量变化事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletPreShootDelegate`

```text
OnBulletPreShootDelegate(Bullet: ASTExtraShootWeaponBulletBase*) -> void
```

Delegate
	  生效范围C
	  子弹射出预处理事件，带有子弹参数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `ASTExtraShootWeaponBulletBase*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletBeforeShootDelegate`

```text
OnBulletBeforeShootDelegate(Bullet: ASTExtraShootWeaponBulletBase*) -> void
```

Delegate
	  生效范围C
	  子弹射出事件，带有子弹参数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `ASTExtraShootWeaponBulletBase*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnBulletPostShootDelegate`

```text
OnBulletPostShootDelegate(Bullet: ASTExtraShootWeaponBulletBase*) -> void
```

Delegate
	  生效范围C
	  子弹射出后理事件，带有子弹参数

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Bullet` | `ASTExtraShootWeaponBulletBase*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
