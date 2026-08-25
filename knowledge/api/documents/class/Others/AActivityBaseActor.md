---
id: "api:class:AActivityBaseActor"
title: "AActivityBaseActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/AActivityBaseActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AActivityBaseActor

可实现可交互物基础功能的Actor

## Inheritance

`AUAERegionActor` -> `IOwnBlackboardInterface` -> `IPlayerLogicInterface` -> `IRelativeMoveMgrInterface` -> `IDamageableInterface` -> `IActivityStateInterface` -> `IGameplayTaskOwnerInterface` -> `INetContainerterface` -> `IClientConditionInerterface` -> `IObjectPoolInterface` -> `IInteractorInterface` -> `IUnifiedInteractionInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OnActivityActorChangeState` | `FActivityChangeState` | 状态变化事件委托<br>	 @param LeaveState 离开的状态 名<br>	 @param EnterState 进入的状态名 |

## Functions

### `GetCurrentStateName`

```text
GetCurrentStateName() -> SHADOWTRACKEREXTRA_API FName
```

生效范围：SC
	  获取当前状态名

**Returns**

| Type | Description |
|---|---|
| `SHADOWTRACKEREXTRA_API FName` | 当前状态名 |

### `GetCurrentStateTime`

```text
GetCurrentStateTime() -> float
```

生效范围：SC
	  获取进入当前状态后所经过的时间

**Returns**

| Type | Description |
|---|---|
| `float` | 当前状态经过的时间 |

### `JumpToState`

```text
JumpToState(StateName: FName, EnterTime: float, bPause: bool) -> void
```

生效范围：S
	  跳转到指定状态

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | 要跳转的状态名 |
| `EnterTime` | `float` | 进入状态的时间 |
| `bPause` | `bool` | 是否暂停 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Pause`

```text
Pause() -> void
```

生效范围：S
	  暂停当前状态的sequence的播放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Resume`

```text
Resume() -> void
```

生效范围：S
	  恢复当前状态的sequence的播放

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CheckCurrentStateIsEntry`

```text
CheckCurrentStateIsEntry() -> bool
```

生效范围：SC
	  检查当前状态是否为状态机的入口状态

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否为入口状态 |

### `GetCurrentSequnceIsEnd`

```text
GetCurrentSequnceIsEnd() -> bool
```

生效范围：SC
	  检查当前sequence是否播放完毕

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否播放完毕 |

## Events

### `OnEnterState_BP`

```text
OnEnterState_BP(StateName: FName) -> void
```

进入某个状态触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StateName` | `FName` | 状态名 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerAttachedToThisActor_BP`

```text
OnPlayerAttachedToThisActor_BP(Player: ASTExtraCharacter *) -> void
```

当角色Attach到这个Actor时触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter *` | Attach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerBeforeAttachedToThisActor_BP`

```text
OnPlayerBeforeAttachedToThisActor_BP(Player: ASTExtraCharacter *) -> void
```

当角色Attach到这个Actor前触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter *` | Attach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerDettachedToThisActor_BP`

```text
OnPlayerDettachedToThisActor_BP(Player: ASTExtraCharacter *) -> void
```

当角色从Actor上Detach时触发

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter *` | Detach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPlayerAttachedDelegate`

```text
OnPlayerAttachedDelegate(Player: ASTExtraCharacter*) -> void
```

角色Attach事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter*` | Attach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlayerDettachedDelegate`

```text
OnPlayerDettachedDelegate(Player: ASTExtraCharacter*) -> void
```

角色Detach事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Player` | `ASTExtraCharacter*` | Detach的角色 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
