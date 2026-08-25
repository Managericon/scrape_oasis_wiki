---
id: "api:class:AEliteProjectile"
title: "AEliteProjectile"
source: "https://developer.gp.qq.com/api/class/detail/Others/AEliteProjectile.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AEliteProjectile

投掷物

## Inheritance

`AActor` -> `IRegionObjectInterface`

## Functions

### `AddOnProjectileDestroyedHandler`

```text
AddOnProjectileDestroyedHandler(InDelegate: FSimpleProjectileDelegate) -> void
```

生效范围SC
	  添加销毁事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDelegate` | `FSimpleProjectileDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveOnProjectileDestroyedHandler`

```text
RemoveOnProjectileDestroyedHandler(InDelegate: FSimpleProjectileDelegate) -> void
```

生效范围SC
	  移除销毁事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InDelegate` | `FSimpleProjectileDelegate` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileExplodedEvent`

```text
ReceiveProjectileExplodedEvent(Impact: FHitResult &) -> void
```

生效范围SC
	  爆炸事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Impact` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileHit`

```text
ReceiveProjectileHit(Hit: FHitResult &) -> void
```

生效范围SC
	  击中事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Hit` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileBouncedEvent`

```text
ReceiveProjectileBouncedEvent(ImpactResult: FHitResult &, ImpactVelocity: FVector &) -> void
```

生效范围SC
	  弹射事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `ImpactVelocity` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveProjectileStoppedEvent`

```text
ReceiveProjectileStoppedEvent(HitResult: FHitResult &) -> void
```

生效范围SC
	  停止事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
