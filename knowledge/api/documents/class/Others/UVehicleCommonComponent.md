---
id: "api:class:UVehicleCommonComponent"
title: "UVehicleCommonComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UVehicleCommonComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UVehicleCommonComponent

载具通用逻辑组件类

## Inheritance

`UVehicleComponent`

## Delegates

### `UGC_OnVehicleHPChangedDelegate`

```text
UGC_OnVehicleHPChangedDelegate(HP: float, HPMax: float) -> void
```

载具血量变化
	 生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `HP` | `float` | 当前血量 |
| `HPMax` | `float` | 最大血量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleFuelChangedDelegate`

```text
UGC_OnVehicleFuelChangedDelegate(Fuel: float, FuelMax: float) -> void
```

载具油量变化
	 生效范围C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Fuel` | `float` | 当前血量 |
| `FuelMax` | `float` | 最大血量 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleWheelsHPChangedDelegate`

```text
UGC_OnVehicleWheelsHPChangedDelegate() -> void
```

生效范围C
	 载具轮子血量发生变化

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_OnVehicleFuelUsedUpDelegate`

```text
UGC_OnVehicleFuelUsedUpDelegate() -> void
```

生效范围CS
	 油量消耗完

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
