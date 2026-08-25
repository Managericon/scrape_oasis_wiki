---
id: "api:class:UGCSoundManagerSystem"
title: "UGCSoundManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%A4%BE%E4%BA%A4%E7%B3%BB%E7%BB%9F/UGCSoundManagerSystem.json"
category: "API Wiki/class/和平全局接口/社交系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCSoundManagerSystem

语音系统接口库

## Functions

### `PlaySound2D`

```text
PlaySound2D(AKEvent: UAkAudioEvent) -> number
```

播放 2D 音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `PlaySoundAtLocation`

```text
PlaySoundAtLocation(AKEvent: UAkAudioEvent, Location: Vector, Orientation: Rotator) -> number
```

在指定位置播放音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取），需要导入音效时选 3D |
| `Location` | `Vector` | 位置 |
| `Orientation` | `Rotator` | 旋转 可使用 Rotator.New(Roll,Pitch,Yaw) 创建,结构 {Roll=Roll, Pitch=Pitch, Yaw=Yaw} |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `PlaySoundAttachActor`

```text
PlaySoundAttachActor(AKEvent: UAkAudioEvent, AttachedActor: Actor, StopWhenAttachedToDestroyed: boolean) -> number
```

依附于 Actor 播放音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |
| `StopWhenAttachedToDestroyed` | `boolean` | 依附的 Actor 销毁时是否停止音效播放 |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `StopAllSound`

```text
StopAllSound()
```

停止全部音效
生效范围：客户端

### `StopSoundByActor`

```text
StopSoundByActor(Actor: Actor)
```

停止指定 Actor 上的所有音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `Actor` | 指定的Actor |

### `StopSoundByID`

```text
StopSoundByID(ID: number)
```

停止指定 ID 的音效
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `number` | 音效 ID |

### `PlaySoundWithVolumePitch`

```text
PlaySoundWithVolumePitch(AKEvent: UAkAudioEvent, AttachedActor: Actor, Volume: number, Pitch: number, StopWhenAttachedToDestroyed: boolean) -> number
```

在以指定音量音高的方式播放音效，如果播放的是同一个音效，必须在上次播放完成再开始下一个播放，音效资源必须在最新的UGC编辑器上制作生成的
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |
| `Volume` | `number` | 范围为-12到12的值 如果不想调整该参数就传一个范围以外的值 |
| `Pitch` | `number` | 范围为-2400到2400的值 如果不想调整该参数就传一个范围以外的值 |
| `StopWhenAttachedToDestroyed` | `boolean` | 依附的 Actor 销毁时是否停止音效播放 |

**Returns**

| Type | Description |
|---|---|
| `number` | 音效 ID |

### `PlaySoundWithRange`

```text
PlaySoundWithRange(AKEvent: UAkAudioEvent, AttachedActor: Actor, StartTime: number, EndTime: number, ID: number)
```

播放指定时间范围的音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |
| `StartTime` | `number` | 开始时间 |
| `EndTime` | `number` | 结束时间 |
| `ID` | `number` | 音效 ID |

### `PlaySoundWithLoop`

```text
PlaySoundWithLoop(AKEvent: UAkAudioEvent, AttachedActor: Actor)
```

播放循环音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |

### `PlaySoundWith2D`

```text
PlaySoundWith2D(AKEvent: UAkAudioEvent, AttachedActor: Actor)
```

播放2D音频
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AKEvent` | `UAkAudioEvent` | 音效资源（通过 UE.LoadObject(SoundPath) 获取） |
| `AttachedActor` | `Actor` | 依附的 Actor |

## Language

`lua`
