---
id: "api:class:UGCTweenSystem"
title: "UGCTweenSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCTweenSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCTweenSystem

Tween 动画系统接口库

## Functions

### `MakeConfig`

```text
MakeConfig(Delay: number, RepeatCount: number, bYoyo: boolean, RepeatDelay: number) -> FUnrealTweenConfig
```

创建一个 Tween 配置表

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Delay` | `number` | 初始延迟（秒），默认 0 |
| `RepeatCount` | `number` | 重复次数（-1 无限，0 不重复），默认 1 |
| `bYoyo` | `boolean` | 是否往返，默认 false |
| `RepeatDelay` | `number` | 重复间隔（秒），默认 0 |

**Returns**

| Type | Description |
|---|---|
| `FUnrealTweenConfig` | - |

### `GetTweenSubsystem`

```text
GetTweenSubsystem() -> @Tween
```

获取 TweenSubsystem 实例
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `@Tween` | 子系统实例 |

### `TweenActorLocation`

```text
TweenActorLocation(Actor: AActor, TargetLocation: FVector, Duration: number, Easing: EEasingType, Config: FUnrealTweenConfig) -> FTweenHandle
```

移动 Actor 到目标位置
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `TargetLocation` | `FVector` | 目标位置 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenActorRotation`

```text
TweenActorRotation(Actor: AActor, TargetRotation: FRotator, Duration: number, Easing: EEasingType, bShortestPath: boolean, Config: FUnrealTweenConfig) -> FTweenHandle
```

旋转 Actor 到目标朝向
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Actor` | `AActor` | 目标 Actor |
| `TargetRotation` | `FRotator` | 目标旋转 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `bShortestPath` | `boolean` | 是否走最短路径旋转 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenFloatValue`

```text
TweenFloatValue(Start: number, End: number, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 float 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `number` | 起始值 |
| `End` | `number` | 目标值 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 float 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenVectorValue`

```text
TweenVectorValue(Start: FVector, End: FVector, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 FVector 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FVector` | 起始向量 |
| `End` | `FVector` | 目标向量 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FVector 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenRotatorValue`

```text
TweenRotatorValue(Start: FRotator, End: FRotator, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 FRotator 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FRotator` | 起始旋转 |
| `End` | `FRotator` | 目标旋转 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FRotator 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `TweenColorValue`

```text
TweenColorValue(Start: FLinearColor, End: FLinearColor, Duration: number, Easing: EEasingType, Callback: function, Config: FUnrealTweenConfig) -> FTweenHandle
```

对 FLinearColor 数值进行插值，每帧通过回调返回当前值
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Start` | `FLinearColor` | 起始颜色 |
| `End` | `FLinearColor` | 目标颜色 |
| `Duration` | `number` | 动画时长（秒） |
| `Easing` | `EEasingType` | 缓动类型（EEasingType 枚举） |
| `Callback` | `function` | 每帧回调，签名 function(Obj, Value)，Obj 为 WorldContext，Value 为当前 FLinearColor 值 |
| `Config` | `FUnrealTweenConfig` | 高级配置（可用 UGCTweenSystem.MakeConfig() 创建，不传则使用默认值） |

**Returns**

| Type | Description |
|---|---|
| `FTweenHandle` | 动画句柄，用于后续控制 |

### `ConfigureTween`

```text
ConfigureTween(Handle: FTweenHandle, Delay: number, RepeatCount: number, bYoyo: boolean, RepeatDelay: number)
```

配置已创建的 Tween 的高级属性（延迟/循环/Yoyo）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |
| `Delay` | `number` | 初始延迟（秒） |
| `RepeatCount` | `number` | 重复次数（-1 为无限循环，0 为不重复） |
| `bYoyo` | `boolean` | 是否往返播放（A->B->A） |
| `RepeatDelay` | `number` | 每次重复前的等待时间（秒），默认 0 |

### `ChainTween`

```text
ChainTween(Handle: FTweenHandle, NextHandle: FTweenHandle)
```

链式连接两个 Tween：Parent 完成后自动播放 Child
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 父动画句柄 |
| `NextHandle` | `FTweenHandle` | 子动画句柄（将在父动画完成后自动触发） |

### `PauseTween`

```text
PauseTween(Handle: FTweenHandle)
```

暂停 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

### `ResumeTween`

```text
ResumeTween(Handle: FTweenHandle)
```

恢复已暂停的 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

### `KillTween`

```text
KillTween(Handle: FTweenHandle)
```

停止并销毁 Tween 动画
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

### `IsTweenValid`

```text
IsTweenValid(Handle: FTweenHandle) -> boolean
```

判断 Tween 句柄是否有效（动画是否仍在运行）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 句柄是否有效 |

### `BindCompletedDelegate`

```text
BindCompletedDelegate(Handle: FTweenHandle, Callback: function)
```

绑定 Tween 完成回调
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Handle` | `FTweenHandle` | 动画句柄 |
| `Callback` | `function` | 完成回调，签名 function(Obj, Handle)，Obj 为 WorldContext，Handle 为动画句柄 |

## Language

`lua`
