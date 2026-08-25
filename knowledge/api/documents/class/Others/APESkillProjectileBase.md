---
id: "api:class:APESkillProjectileBase"
title: "APESkillProjectileBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/APESkillProjectileBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# APESkillProjectileBase

通用抛体V2

## Inheritance

`AUniversalProjectileCore`

## Events

### `ReceiveOnImpactBP`

```text
ReceiveOnImpactBP(ImpactResult: FHitResult &, TargetData: FPESkillTargetData &) -> void
```

碰撞时处理Action前的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `TargetData` | `FPESkillTargetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `PostReceiveOnImpactBP`

```text
PostReceiveOnImpactBP(ImpactResult: FHitResult &, TargetData: FPESkillTargetData &) -> void
```

碰撞处理Action结束后的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImpactResult` | `FHitResult &` | - |
| `TargetData` | `FPESkillTargetData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveStoppedBP`

```text
ReceiveStoppedBP(LastHitResult: FHitResult &) -> void
```

完全停止后的额外接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LastHitResult` | `FHitResult &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SearchTargetActorByPriorityBP`

```text
SearchTargetActorByPriorityBP(InActors: TArray < AActor * > &, CurrentTarget: AActor *) -> AActor *
```

弹射轨迹的自定义优先级算法
	 生效范围：S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActors` | `TArray < AActor * > &` | 传入的Actor数组 |
| `CurrentTarget` | `AActor *` | 当前碰撞对象 |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | AActor 最后返回的结果对象 |

## Language

`cpp`
