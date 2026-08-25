---
id: "api:class:UGCTeamSystem"
title: "UGCTeamSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCTeamSystem.json"
category: "API Wiki/class/和平全局接口/社交系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCTeamSystem

队伍系统接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCTeamSystem.NotifyInviteToJoinLobbyTeamDelegate` | `-` | 通知被邀请加入大厅队伍<br>生效范围：客户端<br>@param InviteToJoinLobbyTeamToken table @邀请到大厅队伍的 Token。InviteToJoinLobbyTeamToken.InviterUID int @邀请者 UID |
| `UGCTeamSystem.NotifyRequestToJoinLobbyTeamDelegate` | `-` | 通知请求加入大厅队伍<br>生效范围：客户端<br>@param RequestToJoinLobbyTeamToken table @请求加入大厅队伍的 Token。RequestToJoinLobbyTeamToken.TeamID int @队伍 ID |

## Functions

### `GetTeamComponent`

```text
GetTeamComponent() -> TeamModeComponent
```

【废弃】获取队伍组件
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `TeamModeComponent` | 队伍组件 |

### `ChangePlayerTeamID`

```text
ChangePlayerTeamID(PlayerKey: number, TeamID: number)
```

改变玩家 TeamID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |
| `TeamID` | `number` | 队伍 ID |

### `GetUIDsByTeamID`

```text
GetUIDsByTeamID(TeamID: number) -> @UID
```

根据TeamID获取对应队伍里所有的玩家UID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@UID` | 列表 |

### `GetPlayerKeysByTeamID`

```text
GetPlayerKeysByTeamID(TeamID: number, bReturnAsLuaTable: boolean) -> @PlayerKey
```

根据TeamID获取对应队伍里所有的玩家PlayerKey，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |
| `bReturnAsLuaTable` | `boolean` | 是否以LuaTable返回 |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `GetAIPlayerKeysByTeamID`

```text
GetAIPlayerKeysByTeamID(TeamID: number) -> @PlayerKey
```

根据 TeamID 获取对应队伍里所有的假人玩家 AIPlayerKey，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `GetPlayerControllersByTeamID`

```text
GetPlayerControllersByTeamID(TeamID: number) -> @PlayerController
```

根据TeamID获取对应队伍里所有的玩家PlayerController
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerController` | 列表 |

### `GetPlayerPawnsByTeamID`

```text
GetPlayerPawnsByTeamID(TeamID: number) -> @PlayerPawn
```

根据TeamID获取对应队伍里所有的玩家PlayerPawn
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerPawn` | 列表 |

### `GetPlayerStatesByTeamID`

```text
GetPlayerStatesByTeamID(TeamID: number) -> @PlayerState
```

根据TeamID获取对应队伍里所有的玩家PlayerState
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `@PlayerState` | 列表 |

### `GetLobbyTeamUIDsByUID`

```text
GetLobbyTeamUIDsByUID(UID: number) -> number[]
```

【废弃】请使用 UGCTeamSystem.GetLobbyTeammateUIDsByUID
根据玩家的UID获取其大厅里组队的成员 UID 列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家 UID 列表 |

### `GetLobbyTeammateUIDsByUID`

```text
GetLobbyTeammateUIDsByUID(UID: number) -> number[]
```

根据玩家的UID获取其大厅里组队的成员 UID 列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家 UID 列表 |

### `GetDynamicLobbyTeammateUIDsByUID`

```text
GetDynamicLobbyTeammateUIDsByUID(UID: number) -> number[]
```

根据玩家的UID获取其大厅里组队的成员 UID 列表。跟 UGCTeamSystem.GetLobbyTeammateUIDsByUID 不同的是，此接口会返回动态组队（UGCTeamSystem.InviteToJoinLobbyTeam、UGCTeamSystem.RequestToJoinLobbyTeam）的成员 UID 列表，而 UGCTeamSystem.GetLobbyTeammateUIDsByUID 以及其他接口只会返回从大厅进入战斗对局那一刻的该玩家在大厅组队的成员 UID 列表。
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `UID` | `number` | 玩家 UID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家 UID 列表 |

### `GetLobbyTeamKeysByPlayerKey`

```text
GetLobbyTeamKeysByPlayerKey(PlayerKey: number) -> @PlayerKey
```

【废弃】请使用 UGCTeamSystem.GetLobbyTeammatePlayerKeysByPlayerKey
根据玩家的 PlayerKey 获取其大厅里组队的成员 PlayerKey 列表，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `GetLobbyTeammatePlayerKeysByPlayerKey`

```text
GetLobbyTeammatePlayerKeysByPlayerKey(PlayerKey: number) -> @PlayerKey
```

根据玩家的 PlayerKey 获取其大厅里组队的成员 PlayerKey 列表，PlayerKey需要客户端连上DS后，才会被初始化，若在客户端连上DS前调用该接口，返回的PlayerKey列表不准确
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `@PlayerKey` | 列表 |

### `InviteToJoinLobbyTeam`

```text
InviteToJoinLobbyTeam(InviteeUID: number)
```

邀请玩家加入（我的）大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InviteeUID` | `number` | 被邀请玩家 UID |

### `RespondToInvitingToJoinLobbyTeam`

```text
RespondToInvitingToJoinLobbyTeam(ResponseOfBeingInvitedToJoinLobby: EResponseOfBeingInvitedToJoinLobby, InviteToJoinLobbyTeamToken: table)
```

响应加入大厅队伍的邀请
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResponseOfBeingInvitedToJoinLobby` | `EResponseOfBeingInvitedToJoinLobby` | 被邀请加入大厅队伍的响应类型：EResponseOfBeingInvitedToJoinLobby |
| `InviteToJoinLobbyTeamToken` | `table` | 邀请到大厅队伍的 Token |

### `RequestToJoinLobbyTeam`

```text
RequestToJoinLobbyTeam(TeamMemberUID: number)
```

玩家请求加入大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamMemberUID` | `number` | 大厅队伍中的玩家 UID |

### `RespondToRequestingToJoinLobbyTeam`

```text
RespondToRequestingToJoinLobbyTeam(ResponseOfBeingRequestedToJoinLobby: EResponseOfBeingRequestedToJoinLobby, RequestToJoinLobbyTeamToken: table)
```

队长响应被加入大厅队伍的请求
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ResponseOfBeingRequestedToJoinLobby` | `EResponseOfBeingRequestedToJoinLobby` | 被请求加入大厅队伍的响应类型：EResponseOfBeingRequestedToJoinLobby |
| `RequestToJoinLobbyTeamToken` | `table` | 请求加入大厅队伍的 Token |

### `QuitLobbyTeam`

```text
QuitLobbyTeam()
```

玩家主动退出大厅队伍
生效范围：客户端

### `KickFromLobbyTeam`

```text
KickFromLobbyTeam(TargetUID: number)
```

队长将指定玩家踢出大厅队伍
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetUID` | `number` | 被踢玩家的 UID |

### `TransferLobbyTeamLeader`

```text
TransferLobbyTeamLeader(NewLeaderUID: number)
```

队长转让大厅队长身份给指定玩家
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLeaderUID` | `number` | 新队长的 UID |

### `GetTeamIDs`

```text
GetTeamIDs() -> @TeamID
```

获取所有队伍的 ID
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `@TeamID` | 列表 |

### `GetPlayerList`

```text
GetPlayerList(bWithOB?: boolean) -> number[]
```

获取所有玩家信息列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bWithOB?` | `boolean` | 是否包含 OB |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 玩家信息列表 |

### `GetTeamSizeByID`

```text
GetTeamSizeByID(TeamID: number) -> number
```

【废弃】请使用 UGCTeamSystem.GetTeamSizeByTeamID
获取队伍中的玩家数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家数量 |

### `GetTeamSizeByTeamID`

```text
GetTeamSizeByTeamID(TeamID: number) -> number
```

获取队伍中的玩家数量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 玩家数量 |

### `GetTeamLeaderKeyByTeamID`

```text
GetTeamLeaderKeyByTeamID(TeamID: number) -> number[]
```

通过队伍编号获取队长PlayerKey列表（每个在大厅点击开始游戏的玩家都会被设置为队长，例如四人匹配，队伍里只有一个队长，三人匹配，再随机匹配一个队友，三人里面点击开始游戏的是队长，随机匹配的那个队友也是队长，属于他自己那个小队的队长）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | 队伍 ID |

**Returns**

| Type | Description |
|---|---|
| `number[]` | 队长PlayerKey |

### `GetIsLeaderOrNotByPlayerKey`

```text
GetIsLeaderOrNotByPlayerKey(PlayerKey: number) -> boolean
```

通过玩家PlayerKey查询身份
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否是队长 |

### `GetAllTeammatePlayerState`

```text
GetAllTeammatePlayerState(bExcludeSelf: boolean) -> ASTExtraPlayerState[]
```

获取所有队友的的PlayerState
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bExcludeSelf` | `boolean` | 是否排除玩家自身 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState[]` | - |

### `GetTeammatePlayerStateByPlayerKey`

```text
GetTeammatePlayerStateByPlayerKey(PlayerKey: number) -> ASTExtraPlayerState
```

获取指定PlayerKey队友的的PlayerState
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState` | - |

### `IsTeamIDValid`

```text
IsTeamIDValid(TeamID: number) -> ASTExtraPlayerState
```

判断TeamID是否合法
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TeamID` | `number` | TeamID |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraPlayerState` | - |

### `GetTeamIDByPlayerKey`

```text
GetTeamIDByPlayerKey(PlayerKey: number) -> number
```

根据PlayerKey获取队伍ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 队伍 ID |

### `GetTeammateIndexByPlayerKey`

```text
GetTeammateIndexByPlayerKey(PlayerState: ASTExtraPlayerState, PlayerKey: number) -> number
```

根据PlayerKey获取队友ID(头顶标号)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | 玩家 PlayerState |
| `PlayerKey` | `number` | 玩家 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 队友 ID |

### `GetAllTeammateIndex`

```text
GetAllTeammateIndex(PlayerState: ASTExtraPlayerState) -> number>
```

获取所有队友的的队友ID(头顶标号)
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | 玩家 PlayerState |

**Returns**

| Type | Description |
|---|---|
| `number>` | 以PlayerKey为键，队友ID为值的表 |

### `GetPlayerKeyByTeammateIndex`

```text
GetPlayerKeyByTeammateIndex(PlayerState: ASTExtraPlayerState, TeammateIndex: number) -> number
```

根据队友ID(头顶标号)获取队友PlayerKey
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerState` | `ASTExtraPlayerState` | 玩家 PlayerState |
| `TeammateIndex` | `number` | 队友ID |

**Returns**

| Type | Description |
|---|---|
| `number` | 队友 PlayerKey |

## Language

`lua`
