---
id: "api:class:UGCAchievementSystem"
title: "UGCAchievementSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCAchievementSystem.json"
category: "API Wiki/class/和平全局接口/玩法规则"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCAchievementSystem

徽章专用接口库

## Functions

### `AddAchievementProgress`

```text
AddAchievementProgress(PlayerKey: number, AchievementID: number, Count: number)
```

累积徽章进度
计数为覆盖累计，单场内多次调用不会累加计数，需自行计算累计总数单次调用
详细使用流程参考wiki (https://developer.gp.qq.com/wiki/#/lvzhou_huizhang.html)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家PlayerKey |
| `AchievementID` | `number` | 徽章ID |
| `Count` | `number` | 徽章计数 |

## Language

`lua`
