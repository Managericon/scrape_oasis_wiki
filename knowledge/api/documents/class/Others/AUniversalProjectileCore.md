---
id: "api:class:AUniversalProjectileCore"
title: "AUniversalProjectileCore"
source: "https://developer.gp.qq.com/api/class/detail/Others/AUniversalProjectileCore.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AUniversalProjectileCore

通用抛体基类

## Inheritance

`AActor` -> `IObjectPoolInterface` -> `IOwnershipChainInterface`

## Events

### `ReceiveOnBounce`

```text
ReceiveOnBounce(ImpactResult: FHitResult &, ImpactVelocity: FVector &) -> void
```

弹跳时的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `ImpactVelocity` | `FVector &` | 碰撞速度 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveLaunchBullet`

```text
ReceiveLaunchBullet() -> void
```

发射时的额外接口
	 生效范围：S

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetTarget`

```text
SetTarget(TargetPawn: APawn *) -> void
```

修改Target的接口，能触发对应目标修改接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetPawn` | `APawn *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveOnProjectileDestroyed`

```text
ReceiveOnProjectileDestroyed() -> void
```

销毁时的额外接口
	 生效范围：SC

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnBulletHitDelegate`

```text
OnBulletHitDelegate(ImpactResult: const FHitResult&) -> void
```

Delegate
	  生效范围S
	  通用抛体命中事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `const FHitResult&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnLaunchBulletDelegate`

```text
OnLaunchBulletDelegate() -> void
```

Delegate
	  生效范围S
	  抛体发射事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
