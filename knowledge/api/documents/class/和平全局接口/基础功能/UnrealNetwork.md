---
id: "api:class:UnrealNetwork"
title: "UnrealNetwork"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%9F%BA%E7%A1%80%E5%8A%9F%E8%83%BD/UnrealNetwork.json"
category: "API Wiki/class/和平全局接口/基础功能"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UnrealNetwork

虚幻网络库

## Functions

### `RepLazyProperty`

```text
RepLazyProperty(TargetObject: AActor | UActorComponent @属性所在的Actor或Component, PropertyName: string)
```

对声明为复制的Lazy属性执行复制

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetObject` | `AActor \| UActorComponent @属性所在的Actor或Component` | 属性所在的Actor或Component |
| `PropertyName` | `string` | 属性名或路径 |

### `CallUnrealRPC`

```text
CallUnrealRPC(TargetPlayerController: APlayerController, TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送可靠单播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetPlayerController` | `APlayerController` | 目标玩家 |
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

### `CallUnrealRPC_Unreliable`

```text
CallUnrealRPC_Unreliable(TargetPlayerController: APlayerController, TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送不可靠单播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetPlayerController` | `APlayerController` | 目标玩家 |
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

### `CallUnrealRPC_Multicast`

```text
CallUnrealRPC_Multicast(TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送可靠广播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

### `CallUnrealRPC_Multicast_Unreliable`

```text
CallUnrealRPC_Multicast_Unreliable(TargetObject: AActor | UActorComponent @目标Actor或Component, FunctionName: string)
```

发送不可靠广播RPC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TargetObject` | `AActor \| UActorComponent @目标Actor或Component` | 目标Actor或Component |
| `FunctionName` | `string` | RPC函数名 |

## Language

`lua`
