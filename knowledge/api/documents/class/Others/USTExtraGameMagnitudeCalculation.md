---
id: "api:class:USTExtraGameMagnitudeCalculation"
title: "USTExtraGameMagnitudeCalculation"
source: "https://developer.gp.qq.com/api/class/detail/Others/USTExtraGameMagnitudeCalculation.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USTExtraGameMagnitudeCalculation

伤害公式

## Inheritance

`UGameMagnitudeCalculationBase` -> `ILocalCalculationVariableSupportInterface`

## Functions

### `IsHeadDamage`

```text
IsHeadDamage(Context: FGameMagnitudeContext &) -> bool
```

获取是否是爆头伤害

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Context` | `FGameMagnitudeContext &` | 公式的上下文对象 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否是爆头伤害 |

## Language

`cpp`
