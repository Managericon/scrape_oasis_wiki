---
id: "api:class:RankingListManager"
title: "RankingListManager"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/RankingListManager.json"
category: "API Wiki/class/和平全局接口/商业化与功能模板"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# RankingListManager

UGC排行榜系统全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RankingListManager.ShowRankDataChangeDelegate` | `-` | 生效范围：客户端<br>排行榜数据变更回调<br>@param RankID number @榜单ID<br>@param RankingCycles number @榜单周期 |
| `RankingListManager.PlayerRankDataChangeDelegate` | `-` | 生效范围：客户端<br>玩家排名数据变更回调<br>@param RankID number @榜单ID<br>@param RankingCycles number @榜单周期<br>@param UID number @玩家UID |
| `RankingListManager.ProfileDataChangeDelegate` | `-` | 生效范围：客户端<br>玩家信息数据变更回调<br>@param RankID number @榜单ID |
| `RankingListManager.ClaimRankListAwardDelegate` | `-` | 生效范围：客户端&服务端<br>领取奖励回调<br>@param RankID number @榜单ID<br>@param Result boolean @领奖是否成功<br>@param UID number @玩家UID |

## Functions

### `UpdateScore`

```text
UpdateScore(PlayerController: BP_UGCPlayerController_C, UID: number, RankID: number, Score: number, IsIncremental: boolean)
```

更新排行榜分数
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `UID` | `number` | 玩家UID |
| `RankID` | `number` | 排行榜ID |
| `Score` | `number` | 更新分数 |
| `IsIncremental` | `boolean` | 是否增量更新 |

### `GetProfileData`

```text
GetProfileData(RankID: number, UID: number) -> RankListProfileData
```

获取玩家信息，使用前需要调用对应榜单的GetRankListData接口
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `RankListProfileData` | - |

### `ClaimRankListAward`

```text
ClaimRankListAward(PlayerController: BP_UGCPlayerController_C, RankID: number)
```

领取排行榜奖励
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `RankID` | `number` | 排行榜ID |

### `CanClaimRankListAward`

```text
CanClaimRankListAward(PlayerController: BP_UGCPlayerController_C, RankID: number) -> UGCRankListAwardState
```

判断是否可以领取奖励
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `BP_UGCPlayerController_C` | 玩家控制器 |
| `RankID` | `number` | 排行榜ID |

**Returns**

| Type | Description |
|---|---|
| `UGCRankListAwardState` | - |

### `GetPlayerRankData`

```text
GetPlayerRankData(UID: number, RankID: number, RankingCycles: number) -> PlayerRankData
```

获取当前DS内玩家排行榜数据(调用后如果当前缓存数据的获取时间超过RequestInterval或者榜单跨越了结算时间, DS会向后台重新请求一次，刷新缓存数据，但当次调用的返回结果还是旧缓存数据)
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家UID |
| `RankID` | `number` | 排行榜ID |
| `RankingCycles` | `number` | 排行榜周期，0为当期，1为上期 |

**Returns**

| Type | Description |
|---|---|
| `PlayerRankData` | 玩家排行榜数据 |

### `GetRankListData`

```text
GetRankListData(RankID: number, RankingCycles: number) -> RankListData>,
```

获取排行榜数据(调用后如果当前缓存数据的获取时间超过RequestInterval或者榜单跨越了结算时间, DS会向后台重新请求一次，刷新缓存数据，但当次调用的返回结果还是旧缓存数据)
生效范围：客户端&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |
| `RankingCycles` | `number` | 排行榜周期，0为当期，1为上期 |

**Returns**

| Type | Description |
|---|---|
| `RankListData>,` | boolean |

### `GetShowRankData`

```text
GetShowRankData() -> table
```

获取全部排行榜数据
生效范围：客户端&服务端

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `OpenReportUI`

```text
OpenReportUI(UID: number, PlayerName: string, RankID: number, ShowUID: boolean)
```

打开举报界面
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 举报玩家UID |
| `PlayerName` | `string` | 举报玩家姓名 |
| `RankID` | `number` | 排行榜ID |
| `ShowUID` | `boolean` | 是否显示UID |

## Language

`lua`
