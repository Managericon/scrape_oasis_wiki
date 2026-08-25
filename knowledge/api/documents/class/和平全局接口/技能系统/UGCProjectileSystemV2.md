---
id: "api:class:UGCProjectileSystemV2"
title: "UGCProjectileSystemV2"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCProjectileSystemV2.json"
category: "API Wiki/class/和平全局接口/技能系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCProjectileSystemV2

技能抛体系统接口库

## Functions

### `CreateProjectile`

```text
CreateProjectile(ProjectileClass: UClass, Owner: AActor, Location: FVector, Direction: FVector, Speed: number, GravityScale: number, DamageValue: number, DamageType: FRestrictedDamageTypeData) -> APESkillProjectileBase
```

发射技能抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProjectileClass` | `UClass` | 抛体类型 |
| `Owner` | `AActor` | 新生成抛体的所属对象 |
| `Location` | `FVector` | 生成坐标 |
| `Direction` | `FVector` | 初始方向 |
| `Speed` | `number` | 初始速度 |
| `GravityScale` | `number` | 初始重力系数 |
| `DamageValue` | `number` | 抛体的伤害值 |
| `DamageType` | `FRestrictedDamageTypeData` | 抛体的伤害类型 |

**Returns**

| Type | Description |
|---|---|
| `APESkillProjectileBase` | 抛体实例 |

### `CreateProjectileSimple`

```text
CreateProjectileSimple(ProjectileClass: UClass, Owner: AActor, Location: FVector, Direction: FVector, Speed: number, GravityScale: number, Target: number) -> APESkillProjectileBase
```

发射技能抛体（不传递伤害）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProjectileClass` | `UClass` | 抛体类型 |
| `Owner` | `AActor` | 新生成抛体的所属对象 |
| `Location` | `FVector` | 生成坐标 |
| `Direction` | `FVector` | 初始方向 |
| `Speed` | `number` | 初始速度 |
| `GravityScale` | `number` | 初始重力系数 |
| `Target` | `number` | 抛体的伤害值 |

**Returns**

| Type | Description |
|---|---|
| `APESkillProjectileBase` | 抛体实例 |

### `SetDirection`

```text
SetDirection(Projectile: APESkillProjectileBase, NewDirection: FVector)
```

设置抛体速度方向
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewDirection` | `FVector` | 新方向 |

### `SetSpeed`

```text
SetSpeed(Projectile: APESkillProjectileBase, NewSpeed: number)
```

设置抛体速度大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewSpeed` | `number` | 新速度 |

### `SetGravityScale`

```text
SetGravityScale(Projectile: APESkillProjectileBase, NewGravityScale: number)
```

设置抛体重力系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewGravityScale` | `number` | 新重力系数 |

### `SetDamage`

```text
SetDamage(Projectile: APESkillProjectileBase, NewDamage: number)
```

设置抛体伤害，会覆盖所有的伤害值，伤害方式会调整为常量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewDamage` | `number` | 伤害值 |

### `SetTarget`

```text
SetTarget(Projectile: APESkillProjectileBase, NewTarget: APawn)
```

设置抛体目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |
| `NewTarget` | `APawn` | 新的目标单位 |

### `GetProjectileMovementComponent`

```text
GetProjectileMovementComponent(Projectile: APESkillProjectileBase) -> UProjectileMovementComponent
```

获取抛体移动组件
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `UProjectileMovementComponent` | 抛体组件类 |

### `GetDirection`

```text
GetDirection(Projectile: APESkillProjectileBase) -> FVector
```

获取抛体速度方向
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `FVector` | 当前速度方向 |

### `GetSpeed`

```text
GetSpeed(Projectile: APESkillProjectileBase) -> number
```

获取抛体速度大小
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `number` | 新速度 |

### `GetGravityScale`

```text
GetGravityScale(Projectile: APESkillProjectileBase) -> number
```

获取抛体重力系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `number` | 新重力系数 |

### `GetTarget`

```text
GetTarget(Projectile: APESkillProjectileBase) -> APawn
```

获取抛体目标
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APESkillProjectileBase` | 抛体实例 |

**Returns**

| Type | Description |
|---|---|
| `APawn` | 新的目标单位 |

### `GetProjectileListByGroupKey`

```text
GetProjectileListByGroupKey(TargetActor: APESkillProjectileBase, GroupKey: string) -> APESkillProjectileBase[]
```

获取抛体组中的抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetActor` | `APESkillProjectileBase` | 发射抛体的角色 |
| `GroupKey` | `string` | 抛体组Key |

**Returns**

| Type | Description |
|---|---|
| `APESkillProjectileBase[]` | 抛体组中的抛体 |

## Language

`lua`
