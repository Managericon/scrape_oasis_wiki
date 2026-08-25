---
id: "api:class:UGCMiscFunctionSystem"
title: "UGCMiscFunctionSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCMiscFunctionSystem.json"
category: "API Wiki/class/和平全局接口/工具库"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCMiscFunctionSystem

游戏杂项函数接口库

## Functions

### `StartAirRoute`

```text
StartAirRoute(WorldObjectContext: UObject)
```

开始航线飞行
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldObjectContext` | `UObject` | 世界上下文对象 |

### `StartAirDrop`

```text
StartAirDrop(WorldObjectContext: UObject, Index: number, AirDropType: EAirDropType)
```

【废弃】请使用 UGCAirDropManagerSystem
开始空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldObjectContext` | `UObject` | 世界上下文对象 |
| `Index` | `number` | 定时普通空投设置中的配置序号（AirDropConfigsUGC） |
| `AirDropType` | `EAirDropType` | 空投箱空投类型一般为 EAirDropType.AirDrop_NormalAirDrop |

### `StartNormalAirDrop`

```text
StartNormalAirDrop(WorldObjectContext: UObject, StartPos: Vector2D, DropPos: Vector2D, Distance: number, AirDropType: EAirDropType)
```

【废弃】请使用 UGCAirDropManagerSystem
自定义空投
生效范围：服务器

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldObjectContext` | `UObject` | 世界上下文对象 |
| `StartPos` | `Vector2D` | 飞机起始点,结构：{X=x,Y=y} |
| `DropPos` | `Vector2D` | 飞机结束点，结构：{X=x,Y=y} |
| `Distance` | `number` | 空投点距离起始点的比例 （0-1）的一个范围，0=StartPos，1=DropPos |
| `AirDropType` | `EAirDropType` | 空投箱空投类型一般为EAirDropType.AirDrop_NormalAirDrop |

## Language

`lua`
