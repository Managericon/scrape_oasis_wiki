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

### `GetFriendRankData`

```text
GetFriendRankData(RankID: number)
```

获取好友榜数据（好友榜只有当期）
生效范围：客户端
调用后触发客户端直连大厅请求刷新好友分数，当次调用直接从本地缓存取数并排序后返回（可能为空）
大厅数据到来后会写入FriendScoreData并广播ShowRankDataChangeDelegate

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |

### `RequestFriendUGCLevel`

```text
RequestFriendUGCLevel(FriendUIDList: table<number, number> @好友UID列表, OnComplete: fun(FilteredUIDList:table<number, number>) @全部profile获取完成后的回调，返回过滤后的UID列表)
```

异步获取好友绿洲等级(ugc_level)，profile数据存入ProfileDataList与排行榜数据复用
通过ProfileMgr.GetProfileList批量获取（每批50个），profile返回数据中包含ugc_level字段
全部批次回调完成后，剔除ugc_level<=1的好友，将剩余UID通过OnComplete回调返回
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FriendUIDList` | `table @好友UID列表` | 好友UID列表 |
| `OnComplete` | `fun(FilteredUIDList:table) @全部profile获取完成后的回调，返回过滤后的UID列表` | 全部profile获取完成后的回调，返回过滤后的UID列表 |

### `IsFriendRankEnabled`

```text
IsFriendRankEnabled(RankID: number) -> boolean
```

判断指定榜单的好友榜是否开启

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 榜单ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 好友榜是否开启 |

### `GetFriendScore`

```text
GetFriendScore(RankID: number, UID: number) -> number|nil
```

从本地数据中获取指定UID在指定榜单的分数
优先从FriendScoreData.ScoreMap取，其次从ShowPlayerRankData取，最后从ShowRankData取
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |
| `UID` | `number` | 玩家UID |

**Returns**

| Type | Description |
|---|---|
| `number\|nil` | 分数，nil表示未获取到 |

### `BuildFriendRankList`

```text
BuildFriendRankList(RankID: number) -> {UID:number,
```

从本地FriendScoreData中，按好友列表过滤并排序，返回好友榜列表
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |

**Returns**

| Type | Description |
|---|---|
| `{UID:number,` | Score:number}> |

### `GetSelfFriendRankData`

```text
GetSelfFriendRankData(RankID: number) -> Score:number}
```

获取当前客户端玩家在好友榜中的排名和分数
从BuildFriendRankList的排序结果中查找当前客户端玩家的排名
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RankID` | `number` | 排行榜ID |

**Returns**

| Type | Description |
|---|---|
| `Score:number}` | 排名(从1开始)，分数(无数据时为0) |

### `RequestFriendRankScores`

```text
RequestFriendRankScores(FriendUIDList: table<number, number> @好友UID列表, RankID: number)
```

客户端直接向大厅发送好友分数查询协议（分批，每批最多100个）
使用cbdata透传{TotalBatch=, BatchIdx=}标记批次，响应中据此判断是否全部请求完毕
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FriendUIDList` | `table @好友UID列表` | 好友UID列表 |
| `RankID` | `number` | 子榜ID |

### `OnFriendRankScoresRsp`

```text
OnFriendRankScoresRsp()
```

客户端收到大厅返回的好友分数查询响应
rsp参数：res, uids, sub_rank, rank_scores, cbdata
cbdata透传{TotalBatch=, BatchIdx=}，用于判断是否全部批次请求完毕
生效范围：客户端

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
