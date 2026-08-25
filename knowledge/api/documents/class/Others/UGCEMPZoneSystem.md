---
id: "api:class:UGCEMPZoneSystem"
title: "UGCEMPZoneSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCEMPZoneSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCEMPZoneSystem

电磁干扰区接口库

## Functions

### `GenerateElectromagneticArea`

```text
GenerateElectromagneticArea(ConfigID: number, Location: FVector) -> number
```

生成电磁干扰区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 电磁干扰区配置 ID |
| `Location` | `FVector` | 电磁干扰区中心坐标 |

**Returns**

| Type | Description |
|---|---|
| `number` | 是否成功生成电磁干扰区, 实例ID |

### `DestroyElectromagneticArea`

```text
DestroyElectromagneticArea(InstanceID: number) -> bool
```

取消电磁干扰区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 电磁干扰区实例 ID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功取消电磁干扰区 |

### `ModifyConfigElectromagneticArea`

```text
ModifyConfigElectromagneticArea(ConfigID: number, ParameterType: string, NewValue: number) -> bool
```

修改电磁干扰区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 电磁干扰区配置 ID |
| `ParameterType` | `string` | 参数类型 |
| `NewValue` | `number` | 新的参数值 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功修改电磁干扰区配置 |

### `GetAllConfigElectromagneticArea`

```text
GetAllConfigElectromagneticArea() -> UGCEMPZoneConfig>
```

查看当前全部电磁干扰区
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneConfig>` | 所有电磁干扰区实例ID和对应的电磁干扰区参数 |

### `GetSpecifyElectromagneticAreaList`

```text
GetSpecifyElectromagneticAreaList(InstanceID: number) -> UGCEMPZoneConfig
```

查看指定电磁干扰区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 电磁干扰区实例 ID |

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneConfig` | 指定实例的电磁干扰区参数 |

### `GetEMPZoneManager`

```text
GetEMPZoneManager() -> UGCEMPZoneManager
```

获取电磁干扰区管理器
获取电磁干扰区全局管理器实例，用于绑定电磁干扰区相关事件
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneManager` | 电磁干扰区管理器实例，失败时返回nil |

## Language

`lua`
