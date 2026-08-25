---
id: "api:class:ASTExtraVehicleBase"
title: "ASTExtraVehicleBase"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E8%BD%BD%E5%85%B7%E5%9F%BA%E7%B1%BB/ASTExtraVehicleBase.json"
category: "API Wiki/class/和平类事件/载具基类"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASTExtraVehicleBase

载具基类

## Inheritance

`APawn` -> `IGeneratorVehicleInterface` -> `IRegionObjectInterface` -> `IDamageableInterface` -> `ISeekAndLockOwnerInterface` -> `IActorHiddenInterface` -> `IFastRemoteReplicationTargetInterface` -> `IRelativeMoveMgrInterface` -> `IInteractorInterface` -> `IAttrModifyInterface` -> `ITargetFilterInfoProviderInterface`

## Events

### `UGC_OnVehicleEnterEvent`

```text
UGC_OnVehicleEnterEvent(IsSucc: bool, Character: ASTExtraPlayerCharacter *, SeatType: ESTExtraVehicleSeatType) -> void
```

玩家进入载具事件
	 生效范围CS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsSucc` | `bool` | 上车是否成功 |
| `Character` | `ASTExtraPlayerCharacter *` | 乘客 |
| `SeatType` | `ESTExtraVehicleSeatType` | 座位类型 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleExitEvent`

```text
UGC_OnVehicleExitEvent(Character: ASTExtraPlayerCharacter *) -> void
```

玩家离开载具事件
	 生效范围CS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Character` | `ASTExtraPlayerCharacter *` | 乘客 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `UGC_OnVehicleHealthStateChangedDelegate`

```text
UGC_OnVehicleHealthStateChangedDelegate(InVehicleHealthState: ESTExtraVehicleHealthState) -> void
```

载具健康状态变化	 
	  生效范围 CS

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InVehicleHealthState` | `ESTExtraVehicleHealthState` | 变化后的健康状态 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleExplosionDelegate`

```text
UGC_OnVehicleExplosionDelegate() -> void
```

生效范围S
	 载具爆炸事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
