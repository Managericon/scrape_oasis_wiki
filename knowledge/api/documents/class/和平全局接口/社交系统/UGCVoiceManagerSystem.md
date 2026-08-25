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

## Language

`lua`
