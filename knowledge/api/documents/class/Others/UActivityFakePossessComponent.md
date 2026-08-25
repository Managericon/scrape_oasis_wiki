---
id: "api:class:UActivityFakePossessComponent"
title: "UActivityFakePossessComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UActivityFakePossessComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UActivityFakePossessComponent

能够将这个Actor的控制权传递给玩家的组件

## Inheritance

`UActorComponent` -> `IFakePossessInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OnPossess` | `FFakePossesserChangeDelegate` | 获取控制权事件事件委托<br>	 @param PC 获取到这个Actor控制权的PC |
| `OnUnPossess` | `FFakePossesserChangeDelegate` | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC |
| `OnUnPossessWithReason` | `FFakeUnPossessDelegate` | 解除控制权事件委托<br>	 @param PC 解除这个Actor控制权的PC<br>	 @param Reason 解除控制权的原因 |

## Functions

### `FakePossess`

```text
FakePossess(PC: AController *) -> bool
```

生效范围：S
	  让一个PlayerController控制这个Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `AController *` | 获得控制权的PlayerController |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FakeUnPossess`

```text
FakeUnPossess(Reason: EUnPossessReason) -> void
```

生效范围：S
	  解除这个Actor上的PC的控制权

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EUnPossessReason` | 解除控制权的原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `FakePossessWithAttach`

```text
FakePossessWithAttach(PC: AController *, AttachScene: USceneComponent *, SocketName: FName, bMulticastToClient: bool) -> bool
```

生效范围：S
	  让一个PlayerController控制这个Actor，并将当前控制的角色Attach到这个Actor上

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PC` | `AController *` | 获得控制权的PlayerController |
| `AttachScene` | `USceneComponent *` | Attach到的组件 |
| `SocketName` | `FName` | Attach到的Socket |
| `bMulticastToClient` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `FakeUnPossessWithDettach`

```text
FakeUnPossessWithDettach(Reason: EUnPossessReason) -> void
```

生效范围：S
	  解除这个Actor上的PC的控制权，并将角色从这个Actor上Detach

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Reason` | `EUnPossessReason` | 解除控制权的原因 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanBePossess`

```text
CanBePossess(Character: ASTExtraBaseCharacter *) -> bool
```

生效范围：S
	  获取是否可以由这个Character控制当前Actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraBaseCharacter *` | 要检查的Character |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
