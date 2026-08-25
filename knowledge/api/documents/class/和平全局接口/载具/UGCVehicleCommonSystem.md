---
id: "api:class:UGCVehicleCommonSystem"
title: "UGCVehicleCommonSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%BD%BD%E5%85%B7/UGCVehicleCommonSystem.json"
category: "API Wiki/class/和平全局接口/载具"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCVehicleCommonSystem

载具系统通用功能接口库

## Functions

### `SetVehicleHPMax`

```text
SetVehicleHPMax(Vehicle: ASTExtraVehicleBase, MaxHP: number)
```

设置载具最大血量
本接口不会自动改变载具血量，游戏逻辑中改变载具血量时（比如收到伤害、载具维修等）会考虑载具最大血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `MaxHP` | `number` | 最大血量 |

### `SetVehicleHP`

```text
SetVehicleHP(Vehicle: ASTExtraVehicleBase, HP: number)
```

设置载具血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `HP` | `number` | 血量 |

### `SetVehicleFuelPercent`

```text
SetVehicleFuelPercent(Vehicle: ASTExtraVehicleBase, FuelPercent: number)
```

设置载具油量（按照百分比设置）
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `FuelPercent` | `number` | 油量百分比 |

### `GetVehicleHPMax`

```text
GetVehicleHPMax(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具最大血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具最大血量 |

### `GetVehicleHP`

```text
GetVehicleHP(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具当前血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具当前血量 |

### `GetVehicleFuelMax`

```text
GetVehicleFuelMax(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具最大油量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具最大油量 |

### `GetVehicleFuelConsumeFactor`

```text
GetVehicleFuelConsumeFactor(Vehicle: ASTExtraVehicleBase) -> number
```

获得当前油耗系数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前油耗系数 |

### `GetVehicleFuel`

```text
GetVehicleFuel(Vehicle: ASTExtraVehicleBase) -> number
```

获得当前油量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 当前油量 |

### `IsDontConsumeFuel`

```text
IsDontConsumeFuel(Vehicle: ASTExtraVehicleBase) -> boolean
```

获得当前是否不耗油
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前是否不耗油 |

### `IsDontDamage`

```text
IsDontDamage(Vehicle: ASTExtraVehicleBase) -> boolean
```

获得当前是否不受到伤害
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 当前是否不受到伤害 |

### `GetWheelHP`

```text
GetWheelHP(Vehicle: ASTExtraVehicleBase, WheelIndex: number) -> number
```

获得轮胎血量
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `WheelIndex` | `number` | 轮胎 ID（从 1 开始） |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具轮子血量 |

### `SetWheelHP`

```text
SetWheelHP(Vehicle: ASTExtraVehicleBase, WheelIndex: number, HP: number) -> boolean
```

设置轮胎血量
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `WheelIndex` | `number` | 轮胎 ID（从 1 开始） |
| `HP` | `number` | 载具轮子血量 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 设置是否成功 |

## Language

`lua`
