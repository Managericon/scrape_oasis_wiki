---
id: "api:class:UGCVehicleSeatSystem"
title: "UGCVehicleSeatSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E8%BD%BD%E5%85%B7/UGCVehicleSeatSystem.json"
category: "API Wiki/class/和平全局接口/载具"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCVehicleSeatSystem

载具系统座位系统接口库

## Functions

### `ChangePassengerSeat`

```text
ChangePassengerSeat(Vehicle: ASTExtraVehicleBase, Passenger: ASTExtraBaseCharacter, SeatIndex: number)
```

在目标座位上没有乘客时更换乘客座位
生效范围：客户端&服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Passenger` | `ASTExtraBaseCharacter` | 乘客 |
| `SeatIndex` | `number` | 座位 ID |

### `ForceChangePassengerSeat`

```text
ForceChangePassengerSeat(Vehicle: ASTExtraVehicleBase, Passenger: ASTExtraBaseCharacter, SeatIndex: number)
```

在目标座位上有乘客时更换乘客座位
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Passenger` | `ASTExtraBaseCharacter` | 乘客 |
| `SeatIndex` | `number` | 座位 ID |

### `GetSeatNum`

```text
GetSeatNum(Vehicle: ASTExtraVehicleBase) -> number
```

获得载具座位个数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 载具座位个数 |

### `GetAvailableSeatNum`

```text
GetAvailableSeatNum(Vehicle: ASTExtraVehicleBase) -> number
```

获得空闲的载具座位个数
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `number` | 空闲的载具座位个数 |

### `GetPassenger`

```text
GetPassenger(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> ASTExtraBaseCharacter
```

获得对应座位的乘客
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter` | 对应座位的乘客 |

### `IsSeatIndexAvailable`

```text
IsSeatIndexAvailable(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> boolean
```

获得对应座位是否空着
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 对应座位是否空着 |

### `GetCharacterSeatIndex`

```text
GetCharacterSeatIndex(Vehicle: ASTExtraVehicleBase, Passenger: ASTExtraBaseCharacter, GetBySocket: boolean) -> number
```

获得指定乘客的座位 ID
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `Passenger` | `ASTExtraBaseCharacter` | 乘客 |
| `GetBySocket` | `boolean` | BySocket |

**Returns**

| Type | Description |
|---|---|
| `number` | 指定乘客的座位 ID |

### `GetDriver`

```text
GetDriver(Vehicle: ASTExtraVehicleBase) -> ASTExtraBaseCharacter
```

获得司机
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter` | 司机 |

### `GetPassengers`

```text
GetPassengers(Vehicle: ASTExtraVehicleBase) -> ASTExtraBaseCharacter[]
```

获得所有乘客
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `ASTExtraBaseCharacter[]` | 所有乘客 |

### `GetAvailableSeatIndexes`

```text
GetAvailableSeatIndexes(Vehicle: ASTExtraVehicleBase) -> int32[]
```

获得所有空闲座位的 Index
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |

**Returns**

| Type | Description |
|---|---|
| `int32[]` | 所有空闲座位的索引 |

### `CanLeanOut`

```text
CanLeanOut(Vehicle: ASTExtraVehicleBase, SeatIndex: number) -> boolean
```

座位上是否可以探头
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否可以探头 |

### `RemoveVehicleWeapon`

```text
RemoveVehicleWeapon(Vehicle: ASTExtraVehicleBase, SeatIndex: number, WeaponIndex: number)
```

移除指定座位上对应 ID 的车载武器
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |
| `WeaponIndex` | `number` | 车载武器 ID |

### `AddVehicleWeaponFromSupportKit`

```text
AddVehicleWeaponFromSupportKit(Vehicle: ASTExtraVehicleBase, SeatIndex: number, WeaponIndex: number, WeaponIndexSupport: number)
```

将座位武器库中的武器装备到座位武器孔上
需要这个座位原来也配置了载具武器，且这个载具武器不在使用中
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |
| `WeaponIndex` | `number` | 车载武器 ID |
| `WeaponIndexSupport` | `number` | 武器库武器 ID |

### `SetPassengerVehicleWeapon`

```text
SetPassengerVehicleWeapon(Vehicle: ASTExtraVehicleBase, SeatIndex: number, bControlVehicleWeapon: boolean)
```

设置当前座位上的车载武器是否能使用
需要这个座位原来也配置了载具武器，且乘客正在该座位上
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Vehicle` | `ASTExtraVehicleBase` | 载具 |
| `SeatIndex` | `number` | 座位 ID |
| `bControlVehicleWeapon` | `boolean` | 是否能控制车载武器 |

## Language

`lua`
