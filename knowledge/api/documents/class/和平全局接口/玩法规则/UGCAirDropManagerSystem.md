---
id: "api:class:UGCAirDropManagerSystem"
title: "UGCAirDropManagerSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E7%8E%A9%E6%B3%95%E8%A7%84%E5%88%99/UGCAirDropManagerSystem.json"
category: "API Wiki/class/和平全局接口/玩法规则"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCAirDropManagerSystem

空投系统接口库

## Functions

### `GenerateAirDrop`

```text
GenerateAirDrop(ID: number, DroppingLocation: FVector, DroppingSpeed: number) -> int32
```

生成指定ID空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `number` | 空投配置ID |
| `DroppingLocation` | `FVector` | 掉落位置 结构Vector={X=0,Y=0,Z=0} |
| `DroppingSpeed` | `number` | 掉落速度 |

**Returns**

| Type | Description |
|---|---|
| `int32` | 是否生成成功, 实例ID |

### `GetAllAirDropConfigs`

```text
GetAllAirDropConfigs(ID: number) -> OneAirDrop[]
```

获得所有空投配置
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ID` | `number` | 空投配置ID |

**Returns**

| Type | Description |
|---|---|
| `OneAirDrop[]` | 空投配置 |

### `DestroyAirDrop`

```text
DestroyAirDrop(InsID: number) -> boolean
```

销毁指定实例ID空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InsID` | `number` | 指定实例ID的空投 0.1s 后销毁 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | 是否销毁成功 |

### `GetAirDropItemList`

```text
GetAirDropItemList(InsID: number) -> FPickUpItemData[]
```

获取指定实例ID空投的物品列表
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InsID` | `number` | 空投实例InsID |

**Returns**

| Type | Description |
|---|---|
| `FPickUpItemData[]` | 空投的物品列表 |

### `GetAllAirDropInstanceIDs`

```text
GetAllAirDropInstanceIDs() -> int32[]
```

获取当前场景内所有的实例ID
生效范围：服务器

**Returns**

| Type | Description |
|---|---|
| `int32[]` | 空投实例ID列表 |

## Language

`lua`
