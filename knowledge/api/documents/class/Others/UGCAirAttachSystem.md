---
id: "api:class:UGCAirAttachSystem"
title: "UGCAirAttachSystem"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCAirAttachSystem.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCAirAttachSystem

轰炸区接口库

## Functions

### `GenerateBombingArea`

```text
GenerateBombingArea(ConfigID: number, Location: FVector) -> number
```

生成轰炸区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 轰炸配置 ID |
| `Location` | `FVector` | 轰炸中心坐标（系统会自动通过射线检测将炸弹位置修正到地面高度） |

**Returns**

| Type | Description |
|---|---|
| `number` | 是否成功生成轰炸区, 实例ID |

### `StopBombingArea`

```text
StopBombingArea(InstanceID: number) -> bool
```

停止轰炸区
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 轰炸实例 ID |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功停止轰炸区 |

### `ModifyBombingAreaConfig`

```text
ModifyBombingAreaConfig(ConfigID: number, ParameterType: string, NewValue: number) -> bool
```

修改轰炸区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `number` | 轰炸配置 ID |
| `ParameterType` | `string` | 参数类型（如："AttackAreaRadius", "EscapeTime", "AttackLastingTime"等） |
| `NewValue` | `number` | 新的参数值 |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否成功修改轰炸配置 |

### `GetAllConfigBombingArea`

```text
GetAllConfigBombingArea() -> UGCAirAttackConfig>
```

查看当前全部轰炸区
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `UGCAirAttackConfig>` | 所有轰炸实例ID和对应的轰炸参数 |

### `GetSpecifyBombingAreaList`

```text
GetSpecifyBombingAreaList(InstanceID: number) -> UGCAirAttackConfig
```

查看指定轰炸区参数
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 轰炸实例 ID |

**Returns**

| Type | Description |
|---|---|
| `UGCAirAttackConfig` | 指定实例的轰炸参数 |

### `GetAirAttackManager`

```text
GetAirAttackManager() -> UGCAirAttackManager
```

获取轰炸区管理器
生效范围：服务器&客户端

**Returns**

| Type | Description |
|---|---|
| `UGCAirAttackManager` | 轰炸区管理器实例，失败时返回nil |

## Language

`lua`
