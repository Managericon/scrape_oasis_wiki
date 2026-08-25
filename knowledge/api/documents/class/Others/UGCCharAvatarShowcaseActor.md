---
id: "api:class:UGCCharAvatarShowcaseActor"
title: "UGCCharAvatarShowcaseActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCCharAvatarShowcaseActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCCharAvatarShowcaseActor

复制玩家角色Avatar的Actor

## Functions

### `ClientShowAvatar`

```text
ClientShowAvatar(PlayerUID: number)
```

显示PlayerUID的Avatar
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerUID` | `number` | 玩家的 PlayerUID |

### `ServerShowAvatar`

```text
ServerShowAvatar(PlayerUID: number)
```

显示PlayerUID的Avatar
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerUID` | `number` | 玩家的 PlayerUID |

### `PlayAnim`

```text
PlayAnim(NewAnimToPlay: UAnimationAsset, bLooping: boolean)
```

播放动画
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAnimToPlay` | `UAnimationAsset` | 动画资源 |
| `bLooping` | `boolean` | 是否循环播放 |

## Language

`lua`
