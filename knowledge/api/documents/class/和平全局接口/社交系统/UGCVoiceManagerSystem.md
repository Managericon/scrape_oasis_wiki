---
id: "api:class:UGCVoiceManagerSystem"
title: "UGCVoiceManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCVoiceManagerSystem.json"
category: "API Wiki/class/和平全局接口/社交系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCVoiceManagerSystem

语音系统接口库

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCVoiceManagerSystem.VoiceMode` | `-` | - |
| `UGCVoiceManagerSystem.VoiceChannel` | `-` | - |
| `UGCVoiceManagerSystem.MicStateChangedEventID` | `-` | - |
| `UGCVoiceManagerSystem._MicMode` | `-` | - |

## Functions

### `GetGVoiceInterface`

```text
GetGVoiceInterface() -> UGVoiceInterface
```

获取 Voice 组件
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `UGVoiceInterface` | 对应语音管理类的指针 |

### `GetPlayerMemberID`

```text
GetPlayerMemberID(PlayerKey: number) -> number
```

获取玩家的语音房间 MemberID
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 角色的 PlayerKey |

**Returns**

| Type | Description |
|---|---|
| `number` | 角色语音房间的 MemberID |

### `JoinVoiceRoom`

```text
JoinVoiceRoom(RoomKey: string)
```

加入语音房间
RoomKey 为语音房间唯一标识，可由自己进行拼接
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RoomKey` | `string` | 语音房间 Key |

### `QuitVoiceRoom`

```text
QuitVoiceRoom()
```

退出 UGC 语音房间
生效范围：客户端

### `GetVoiceRoomKey`

```text
GetVoiceRoomKey() -> string
```

获取当前房间 RoomKey
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `string` | 语音房间 Key |

### `SetGlobalVoiceRadius`

```text
SetGlobalVoiceRadius(Radius: number)
```

设置全局语音生效范围
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Radius` | `number` | 全局语音半径（单位：cm） |

### `SetVoiceRoomSoundEnable`

```text
SetVoiceRoomSoundEnable(IsEnable: boolean)
```

开启/关闭语音房间喇叭
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭喇叭 |

### `SetVoiceRoomMicrophoneEnable`

```text
SetVoiceRoomMicrophoneEnable(IsEnable: boolean)
```

开启/关闭语音房间麦克风
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭麦克风 |

### `SetGlobalVoiceSoundEnable`

```text
SetGlobalVoiceSoundEnable(IsEnable: boolean)
```

开启/关闭全局语音喇叭
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭喇叭 |

### `SeGlobalVoiceMicrophoneEnable`

```text
SeGlobalVoiceMicrophoneEnable(IsEnable: boolean)
```

开启/关闭 全局语音麦克风
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsEnable` | `boolean` | 开启或者关闭麦克风 |

### `SetVoiceRoomPlayerMuteState`

```text
SetVoiceRoomPlayerMuteState(MemberID: number, IsMute: boolean)
```

设置语音房间指定玩家语音屏蔽（静音）状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MemberID` | `number` | 当前房间要被屏蔽的玩家的 UID |
| `IsMute` | `boolean` | 是否屏蔽 |

### `SetGlobalVoicePlayerMuteState`

```text
SetGlobalVoicePlayerMuteState(MemberID: number, IsMute: boolean)
```

设置全局房间指定玩家语音屏蔽（静音）状态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MemberID` | `number` | 当前房间要被屏蔽的玩家的 MemberID |
| `IsMute` | `boolean` | 是否屏蔽 |

### `IsVoiceRoomSoundEnable`

```text
IsVoiceRoomSoundEnable() -> boolean
```

获得语音房间声音（喇叭）开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间喇叭状态 |

### `IsVoiceRoomMicrophoneEnable`

```text
IsVoiceRoomMicrophoneEnable() -> boolean
```

获得语音房间麦克风开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间麦克风状态 |

### `IsGlobalVoiceSoundEnable`

```text
IsGlobalVoiceSoundEnable() -> boolean
```

获得全局语音声音（喇叭）开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间喇叭状态 |

### `IsGlobalVoiceMicrophoneEnable`

```text
IsGlobalVoiceMicrophoneEnable() -> boolean
```

获得全局语音麦克风开关状态
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前房间麦克风状态 |

### `JoinGlobalVoiceRoom`

```text
JoinGlobalVoiceRoom(GlobalVoiceRoomId: number)
```

加入全局语音房间（依赖于全局语音房间的某个范围可听可说,区域语音，包厢等等）
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `GlobalVoiceRoomId` | `number` | 区域小房间的 index |

### `QuitGlobalVoiceRoom`

```text
QuitGlobalVoiceRoom()
```

退出全局语音房间（区域语音，包厢等等）
生效范围：客户端

### `CloseCivilVoiceDetect`

```text
CloseCivilVoiceDetect()
```

关闭文明语音检测和 lbs 小号限制
生效范围：客户端

### `GetNormalizedMicVolume`

```text
GetNormalizedMicVolume() -> integer
```

获取归一化麦克风音量（0-100）
通过 GetMicLevelDB 获取 dB 值，映射到 0-100 的归一化范围
映射公式: normalized = clamp(round((db + 96) / 96 * 100), 0, 100)
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `integer` | 归一化音量值 0-100 |

### `_ApplyMicChannel`

```text
_ApplyMicChannel()
```

内部：根据当前模式与频道，应用麦克风频道到 gvoice
Always 模式使用 Open*Micphone（自由发言），Push 模式使用 Open*Interphone（按键发言）

### `_ApplySpeakerChannel`

```text
_ApplySpeakerChannel()
```

内部：根据当前频道，应用扬声器频道到 gvoice

### `RefreshVoiceUI`

```text
RefreshVoiceUI()
```

刷新主界面语音图标显示
逻辑层调用切换麦克风或喇叭后调用，通知主界面刷新语音控件状态
生效范围：客户端

### `SetMicMode`

```text
SetMicMode(Mode: EVoiceMode)
```

设置说话模式（始终开启说话 / 按下说话），对应面板两个分区的切换
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Mode` | `EVoiceMode` | 说话模式（VoiceMode.Always 或 VoiceMode.Push） |

### `SetMicChannel`

```text
SetMicChannel(Channel: EVoiceChannel)
```

设置麦克风指向的频道（全部 / 队伍 / 组队），对应面板中对应控件呈选中态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Channel` | `EVoiceChannel` | 麦克风频道（VoiceChannel.All / Team / LobbyTeam） |

### `SetMicEnabled`

```text
SetMicEnabled(bEnabled: boolean)
```

开启/关闭麦克风；关闭时对应控件呈禁用图标，开启时恢复到之前选中项
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `boolean` | 是否开启麦克风 |

### `SetSpeakerChannel`

```text
SetSpeakerChannel(Channel: EVoiceChannel)
```

设置扬声器收听的频道（全部 / 队伍），对应控件呈选中态
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Channel` | `EVoiceChannel` | 扬声器频道（VoiceChannel.All / Team） |

### `SetSpeakerEnabled`

```text
SetSpeakerEnabled(bEnabled: boolean)
```

开启/关闭扬声器；关闭时对应控件呈禁用图标，开启时恢复到之前选中项
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnabled` | `boolean` | 是否开启扬声器 |

### `GetMicState`

```text
GetMicState() -> EVoiceMode, EVoiceChannel, boolean
```

获取当前麦克风状态（说话模式、麦克风指向频道、开关状态）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `EVoiceMode` | 当前说话模式 |
| `EVoiceChannel` | 当前麦克风指向频道 |
| `boolean` | 当前麦克风开关状态 |

### `GetSpeakerState`

```text
GetSpeakerState() -> EVoiceChannel, boolean
```

获取当前扬声器状态（收听频道、开关状态）
生效范围：客户端

**Returns**

| Type | Description |
|---|---|
| `EVoiceChannel` | 当前扬声器收听频道 |
| `boolean` | 当前扬声器开关状态 |

## Language

`lua`
