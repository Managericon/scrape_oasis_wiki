---
id: "api:class:UVehicleSeatComponent"
title: "UVehicleSeatComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UVehicleSeatComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UVehicleSeatComponent

载具座位组件类

## Inheritance

`UVehicleComponent`

## Delegates

### `UGC_OnSeatAttachedDelegate`

```text
UGC_OnSeatAttachedDelegate(Character: ASTExtraPlayerCharacter*, SeatType: ESTExtraVehicleSeatType, SeatIdx: int32) -> void
```

使用座位
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter*` | 乘客 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |
| `SeatIdx` | `int32` | 座位Index |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnSeatDetachedDelegate`

```text
UGC_OnSeatDetachedDelegate(Character: ASTExtraPlayerCharacter*, SeatType: ESTExtraVehicleSeatType, SeatIdx: int32) -> void
```

离开座位
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter*` | 乘客 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |
| `SeatIdx` | `int32` | 座位Index |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnSeatChangedDelegate`

```text
UGC_OnSeatChangedDelegate(Character: ASTExtraPlayerCharacter*, LastSeatType: ESTExtraVehicleSeatType, LastSeatIdx: int32, NewSeatType: ESTExtraVehicleSeatType, NewSeatIdx: int32) -> void
```

离开座位
	 生效范围S

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter*` | 乘客 |
| `LastSeatType` | `ESTExtraVehicleSeatType` | 旧座位类型 |
| `LastSeatIdx` | `int32` | 旧座位Index |
| `NewSeatType` | `ESTExtraVehicleSeatType` | 新座位类型 |
| `NewSeatIdx` | `int32` | 新座位Index |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnDriverChange`

```text
OnDriverChange(OldChara: ASTExtraPlayerCharacter*, NewChara: ASTExtraPlayerCharacter*) -> void
```

驾驶员变更事件Delegate

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OldChara` | `ASTExtraPlayerCharacter*` | - |
| `NewChara` | `ASTExtraPlayerCharacter*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
