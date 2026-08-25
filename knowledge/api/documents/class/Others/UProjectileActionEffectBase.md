---
id: "api:class:UProjectileActionEffectBase"
title: "UProjectileActionEffectBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UProjectileActionEffectBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UProjectileActionEffectBase

抛体动作基类

## Inheritance

`UProjectileEffectBase`

## Events

### `ApplyActionEffect`

```text
ApplyActionEffect(TargetData: FPESkillTargetData &) -> void
```

执行动作
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetData` | `FPESkillTargetData &` | 条件触发时的数据 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `InitBP`

```text
InitBP(InOwnerActor: AActor *) -> void
```

动作初始化接口
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOwnerActor` | `AActor *` | 抛体 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyParamsBP`

```text
ApplyParamsBP(Params: FProjectileParams &) -> void
```

动作发射时调用的参数
	 生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Params` | `FProjectileParams &` | 发射参数 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
