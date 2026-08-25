---
id: "api:class:AUniversalProjectileBase"
title: "AUniversalProjectileBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/AUniversalProjectileBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUniversalProjectileBase

通用抛体

## Inheritance

`AUniversalProjectileCore`

## Functions

### `ReceiveCustomFilter`

```text
ReceiveCustomFilter(InActor: AActor *) -> bool
```

自定义的过滤器接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ReceivePlayExplosionEffectToAllTarget`

```text
ReceivePlayExplosionEffectToAllTarget(FoundTargets: TArray < FHitResult > &) -> void
```

自定义爆炸范围内筛选过后所有碰撞结果接口
	 生效范围：S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FoundTargets` | `TArray < FHitResult > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceivePlayExplosionEffect`

```text
ReceivePlayExplosionEffect(ExplosionTarget: FHitResult &) -> void
```

自定义爆炸范围内筛选过后碰撞接口
	 生效范围：S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ExplosionTarget` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveBeginExplodeTimer`

```text
ReceiveBeginExplodeTimer() -> void
```

爆炸开始计时的额外接口（如果有延时爆炸）
	 生效范围：S

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveEndExplodeTimer`

```text
ReceiveEndExplodeTimer() -> void
```

爆炸停止计时的额外接口（如果有延时爆炸）
	 生效范围：S

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
