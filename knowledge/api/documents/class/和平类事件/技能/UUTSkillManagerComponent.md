---
id: "api:class:UUTSkillManagerComponent"
title: "UUTSkillManagerComponent"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E6%8A%80%E8%83%BD/UUTSkillManagerComponent.json"
category: "API Wiki/class/和平类事件/技能"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUTSkillManagerComponent

技能组件

## Inheritance

`UActorComponent` -> `IUTSkillInstanceNodeContainerInterface` -> `IObjectPoolInterface`

## Delegates

### `UGC_SkillActiveDelegate`

```text
UGC_SkillActiveDelegate(SkillPath: FString) -> void
```

技能激活
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_SkillStartDelegate`

```text
UGC_SkillStartDelegate(SkillPath: FString) -> void
```

技能开始
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_SkillEndDelegate`

```text
UGC_SkillEndDelegate(SkillPath: FString) -> void
```

技能结束
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_SkillCDDelegate`

```text
UGC_SkillCDDelegate(SkillPath: FString) -> void
```

技能进入冷却
	   生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillPath` | `FString` | 技能路径 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
