---
id: "api:class:UGCRankSystem"
title: "UGCRankSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCRankSystem.json"
category: "API Wiki/class/和平全局接口/玩法规则"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCRankSystem

段位专用接口库

## Functions

### `GetUGCRank`

```text
GetUGCRank(PlayerKey: number) -> number
```

查询段位分
调用 UGCRankSystem.AddRankProgress 后，会获取到新段位分
例：开局 2000 积分，中途调用 UGCRankSystem.AddRankProgress 增加 100 积分，再调用 UGCRankSystem.GetUGCRank 则得到 2100 积分
详细使用流程参考 wiki (https://developer.gp.qq.com/wiki/#/lvzhou_duanwei.html)
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 段位分 |

### `AddRankProgress`

```text
AddRankProgress(PlayerKey: number, Count: number)
```

修改段位分
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |
| `Count` | `number` | 段位分变化值 |

### `GetUGCGameSeasonId`

```text
GetUGCGameSeasonId() -> number
```

查询当前玩法段位赛 ID
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `number` | 游戏赛季 ID |

## Language

`lua`
