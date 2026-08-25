---
id: "api:class:UGCProjectileSystem"
title: "UGCProjectileSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%8A%80%E8%83%BD%E7%B3%BB%E7%BB%9F/UGCProjectileSystem.json"
category: "API Wiki/class/和平全局接口/技能系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCProjectileSystem

抛体系统接口库

## Functions

### `SpawnProjectile`

```text
SpawnProjectile(ProjectileSpawnInfo: ProjectileSpawnInfo) -> APVEProjectileBase
```

生成抛体
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProjectileSpawnInfo` | `ProjectileSpawnInfo` | 抛体生成参数 |

**Returns**

| Type | Description |
|---|---|
| `APVEProjectileBase` | 抛体对象实例 |

### `GetDestroyAfterHit`

```text
GetDestroyAfterHit(Projectile: APVEProjectileBase) -> boolean
```

获取抛体命中之后是否销毁
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否命中后销毁 |

### `SetDestroyAfterHit`

```text
SetDestroyAfterHit(Projectile: APVEProjectileBase, bNewDestroyAfterHit: boolean)
```

设置抛体命中之后是否销毁
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |
| `bNewDestroyAfterHit` | `boolean` | 是否销毁 |

### `GetPMComp`

```text
GetPMComp(Projectile: APVEProjectileBase) -> boolean
```

获取抛体运动组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 抛体运动组件 |

### `SetMoveAfterImpactWithNoLost`

```text
SetMoveAfterImpactWithNoLost(Projectile: APVEProjectileBase, bNeedUpdateImmide: boolean)
```

设置抛体命中之后是否继续移动
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |
| `bNeedUpdateImmide` | `boolean` | 是否更新组件速度 |

### `GetLastUpdateCompBeforeStop`

```text
GetLastUpdateCompBeforeStop(Projectile: APVEProjectileBase) -> boolean
```

停止前最后更新的组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Projectile` | `APVEProjectileBase` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 最后更新的组件 |

## Language

`lua`
