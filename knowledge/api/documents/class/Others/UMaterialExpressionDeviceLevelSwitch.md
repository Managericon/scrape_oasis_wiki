---
id: "api:class:UMaterialExpressionDeviceLevelSwitch"
title: "UMaterialExpressionDeviceLevelSwitch"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMaterialExpressionDeviceLevelSwitch.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMaterialExpressionDeviceLevelSwitch

## Inheritance

`UMaterialExpression`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Default` | `FExpressionInput` | Default input (must be connected). Same as Low. Used when DEVICE_LEVEL_HIGH is 0. |
| `Low` | `FExpressionInput` | Low device input (optional). If connected, overrides Default. Used when DEVICE_LEVEL_HIGH is 0. |
| `High` | `FExpressionInput` | High device input (optional). Used when DEVICE_LEVEL_HIGH is 1. Connecting this enables DeviceLevel shader variants. |

## Language

`cpp`
