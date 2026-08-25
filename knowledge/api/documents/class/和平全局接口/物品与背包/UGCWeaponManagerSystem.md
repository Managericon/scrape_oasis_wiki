---
id: "api:class:UGCWeaponManagerSystem"
title: "UGCWeaponManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%89%A9%E5%93%81%E4%B8%8E%E8%83%8C%E5%8C%85/UGCWeaponManagerSystem.json"
category: "API Wiki/class/和平全局接口/物品与背包"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCWeaponManagerSystem

武器管理系统接口库

## Functions

### `GetWeaponManagerComponent`

```text
GetWeaponManagerComponent(PlayerPawn: PlayerPawn) -> UWeaponManagerComponent
```

获取武器管理组件
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `UWeaponManagerComponent` | 武器管理组件 |

### `GetWeaponBySlot`

```text
GetWeaponBySlot(PlayerPawn: PlayerPawn, Slot: ESurviveWeaponPropSlot) -> ASTExtraWeapon
```

获取对应插槽的武器实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `Slot` | `ESurviveWeaponPropSlot` | 武器槽位 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraWeapon` | 武器 |

### `GetCurrentWeapon`

```text
GetCurrentWeapon(PlayerPawn: PlayerPawn) -> ASTExtraWeapon
```

获取当前使用的武器实例
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraWeapon` | 武器 |

### `GetLastUsedWeapon`

```text
GetLastUsedWeapon(PlayerPawn: PlayerPawn) -> ASTExtraWeapon
```

获取上一把武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraWeapon` | 武器 |

### `GetCurrentWeaponSlot`

```text
GetCurrentWeaponSlot(PlayerPawn: PlayerPawn) -> ESurviveWeaponPropSlot
```

获取当前使用武器插槽
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `ESurviveWeaponPropSlot` | 武器槽位 |

### `SwitchWeaponBySlot`

```text
SwitchWeaponBySlot(PlayerPawn: PlayerPawn, Slot: ESurviveWeaponPropSlot, IsUseAnimation: boolean)
```

切换对应槽位的武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `Slot` | `ESurviveWeaponPropSlot` | 武器槽位 |
| `IsUseAnimation` | `boolean` | 是否播放使用动画 |

### `CurrentWeaponAttachToBack`

```text
CurrentWeaponAttachToBack(PlayerPawn: PlayerPawn)
```

收起武器
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

### `GetWeaponItemID`

```text
GetWeaponItemID(Weapon: ASTExtraWeapon) -> number
```

获取武器ItemID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weapon` | `ASTExtraWeapon` | 武器 |

**Returns**

| Type | Description |
|---|---|
| `number` | 物品ID,对应物品表中ID |

### `GetWeaponName`

```text
GetWeaponName(Weapon: ASTExtraWeapon) -> string
```

获取武器名
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Weapon` | `ASTExtraWeapon` | 武器 |

**Returns**

| Type | Description |
|---|---|
| `string` | 武器名称 |

### `GetCurrentUsingAmmoID`

```text
GetCurrentUsingAmmoID(PlayerPawn: PlayerPawn) -> number
```

获取当前消耗弹药
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |

**Returns**

| Type | Description |
|---|---|
| `number` | 弹药ID |

### `SetWeaponSlotVisible`

```text
SetWeaponSlotVisible(PlayerPawn: PlayerPawn, WeaponSlot: ESurviveWeaponPropSlot, bVisible: boolean)
```

设置武器的可见性
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerPawn` | `PlayerPawn` | 玩家角色 |
| `WeaponSlot` | `ESurviveWeaponPropSlot` | 武器槽位 |
| `bVisible` | `boolean` | 是否可见 |

## Language

`lua`
