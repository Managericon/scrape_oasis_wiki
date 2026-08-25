---
id: "api:class:UGameplayDataCollectHelperBase"
title: "UGameplayDataCollectHelperBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameplayDataCollectHelperBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameplayDataCollectHelperBase

## Inheritance

`UObject`

## Functions

### `GMPEvent_SkillUseDelay`

```text
GMPEvent_SkillUseDelay(SkillUID: int32, bRealUsed: bool) -> void
```

老技能释放延迟时间（客户端点击到实际释放的时间差）

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillUID` | `int32` | - |
| `bRealUsed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GMPEvent_SkillUseFaildRate`

```text
GMPEvent_SkillUseFaildRate(SkillUID: int32, bUseFailed: bool) -> void
```

老技能释放失败率

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkillUID` | `int32` | - |
| `bUseFailed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
