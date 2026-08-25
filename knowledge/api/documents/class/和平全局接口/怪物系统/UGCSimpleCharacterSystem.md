---
id: "api:class:UGCSimpleCharacterSystem"
title: "UGCSimpleCharacterSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E6%80%AA%E7%89%A9%E7%B3%BB%E7%BB%9F/UGCSimpleCharacterSystem.json"
category: "API Wiki/class/和平全局接口/怪物系统"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCSimpleCharacterSystem

怪物小动物系统接口库

## Functions

### `GetHealth`

```text
GetHealth(SimpleCharacter: ASTExtraSimpleCharacterBase) -> number
```

获取当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量 |

### `SetHealth`

```text
SetHealth(SimpleCharacter: ASTExtraSimpleCharacterBase, Health: number)
```

设置当前血量（不会超过血量最大值）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `Health` | `number` | 血量 |

### `GetHealthMax`

```text
GetHealthMax(SimpleCharacter: ASTExtraSimpleCharacterBase) -> number
```

获取当前最大血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 血量 |

### `SetHealthMax`

```text
SetHealthMax(SimpleCharacter: ASTExtraSimpleCharacterBase, HealthMax: number)
```

设置当前最大血量（当前血量不会随之变大，但如果超过最大血量，则会变小）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `HealthMax` | `number` | 最大血量 |

### `GetSpeedScale`

```text
GetSpeedScale(SimpleCharacter: ASTExtraSimpleCharacterBase) -> number
```

获取移动速度系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `number` | 移动系数 |

### `SetSpeedScale`

```text
SetSpeedScale(SimpleCharacter: ASTExtraSimpleCharacterBase, SpeedScale: number)
```

设置移动速度系数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `SpeedScale` | `number` | 移动系数 |

### `IsInvincible`

```text
IsInvincible(SimpleCharacter: ASTExtraSimpleCharacterBase) -> boolean
```

获取是否无敌
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否无敌 |

### `SetInvincible`

```text
SetInvincible(SimpleCharacter: ASTExtraSimpleCharacterBase, IsInvincible: boolean)
```

设置是否无敌
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |
| `IsInvincible` | `boolean` | 是否无敌 |

### `IsAlive`

```text
IsAlive(SimpleCharacter: ASTExtraSimpleCharacterBase) -> boolean
```

获取是否存活
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SimpleCharacter` | `ASTExtraSimpleCharacterBase` | 小动物/ ASTExtraSimpleCharacter @怪物 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否存活 |

## Language

`lua`
