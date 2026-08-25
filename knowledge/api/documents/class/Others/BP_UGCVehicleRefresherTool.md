---
id: "api:class:BP_UGCVehicleRefresherTool"
title: "BP_UGCVehicleRefresherTool"
source: "https://developer.gp.qq.com/api/class/detail/Others/BP_UGCVehicleRefresherTool.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# BP_UGCVehicleRefresherTool

载具刷新器工具，用于管理载具的自动刷新和生成

## Functions

### `AddVehicleEventListener`

```text
AddVehicleEventListener(callback: function, context: any)
```

添加载具生成事件监听器，外部代码调用此方法注册载具生成事件监听
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数，参数为(Vehicle) |
| `context` | `any` | 上下文对象（可选） |

### `AddVehicleDriveAwayEventListener`

```text
AddVehicleDriveAwayEventListener(callback: function, context: any)
```

添加载具开走事件监听器，外部代码调用此方法注册载具开走事件监听
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数，参数为(Vehicle) |
| `context` | `any` | 上下文对象（可选） |

### `RemoveVehicleEventListener`

```text
RemoveVehicleEventListener(callback: function, context: any)
```

移除载具生成事件监听器
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数 |
| `context` | `any` | 上下文对象 |

### `RemoveVehicleDriveAwayEventListener`

```text
RemoveVehicleDriveAwayEventListener(callback: function, context: any)
```

移除载具开走事件监听器
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `callback` | `function` | 回调函数 |
| `context` | `any` | 上下文对象 |

### `GenerateVehicle`

```text
GenerateVehicle() -> boolean
```

根据权重配置随机生成载具
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-生成成功, false-生成失败 |

### `GenerateCustomizeVehicle`

```text
GenerateCustomizeVehicle(VehiclePath: string) -> boolean
```

生成指定的载具蓝图
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `VehiclePath` | `string` | 载具蓝图路径，如"/Game/Arts_PlayerBluePrints/Vehicle/VH_Buggy/BP_VH_Buggy.BP_VH_Buggy_C" |

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-生成成功, false-生成失败 |

### `DestroyCurrentVehicle`

```text
DestroyCurrentVehicle() -> boolean
```

销毁当前刷新点管理的载具
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-销毁成功, false-销毁失败 |

### `ResetVehicleRespawnPoint`

```text
ResetVehicleRespawnPoint() -> boolean
```

重置载具刷新点，如果载具还在原地，先销毁再重新刷新
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `boolean` | true-重置成功, false-重置失败 |

### `GetVehicleRespawnPointConfig`

```text
GetVehicleRespawnPointConfig() -> table
```

获取配置的载具列表信息
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `table` | 载具配置列表，包含index、path、weight字段 |

### `GetVehicleStatusConfig`

```text
GetVehicleStatusConfig() -> table
```

获取当前车辆的实时状态信息
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `table` | 当前车辆信息（包含isValid、location、healthState、hasDriver等字段），如无车辆返回false |

## Language

`lua`
