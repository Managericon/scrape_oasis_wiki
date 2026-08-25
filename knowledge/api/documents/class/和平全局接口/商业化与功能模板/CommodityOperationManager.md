---
id: "api:class:CommodityOperationManager"
title: "CommodityOperationManager"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%95%86%E4%B8%9A%E5%8C%96%E4%B8%8E%E5%8A%9F%E8%83%BD%E6%A8%A1%E6%9D%BF/CommodityOperationManager.json"
category: "API Wiki/class/和平全局接口/商业化与功能模板"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# CommodityOperationManager

UGC商业化购买流程全局管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CommodityOperationManager.BuyProductResultDelegate` | `-` | 生效范围：客户端&&服务端<br>发起购买商品后触发<br>@param Result BuyProductResult @购买结果 |
| `CommodityOperationManager.LimitProductUpdateDelegate` | `-` | 生效范围：客户端&&服务端<br>限购商品购买次数发生变化时触发 |
| `CommodityOperationManager.PurchasedProductListUpdateDelegate` | `-` | 生效范围：客户端&&服务端<br>商品购买次数发生变化时触发 |

## Functions

### `BuyProduct`

```text
BuyProduct(ProductID: number, Num: number, CurrentPrice: number, bCheckPrivilege: boolean) -> PromiseFuture
```

发起商品购买
生效范围：客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `Num` | `number` | 购买商品数量 |
| `CurrentPrice` | `number` | 发起购买时的价格，用于校验 |
| `bCheckPrivilege` | `boolean` | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |

**Returns**

| Type | Description |
|---|---|
| `PromiseFuture` | 绿洲币购买UI界面的PromiseFuture实例，非绿洲币商品则返回nil |

### `ServerBuyProduct`

```text
ServerBuyProduct(PlayerKey: number, ProductID: number, Num: number, CurrentPrice: number, bCheckPrivilege: boolean)
```

发起自定义货币商品购买
生效范围：服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerKey` | `number` | 发起购买者的 PlayerKey |
| `ProductID` | `number` | 商品的ID |
| `Num` | `number` | 购买商品数量 |
| `CurrentPrice` | `number` | 发起购买时的价格，用于校验 |
| `bCheckPrivilege` | `boolean` | 是否检查玩家特权（即当前商品为仅特权可购买），默认false |

### `CanAfford`

```text
CanAfford(ProductID: number, Num: number, PlayerController: UUGCPlayerController) -> boolean
```

检查是否买得起指定数量的商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `Num` | `number` | 购买的商品数量 |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetLimitPurchasedTimes`

```text
GetLimitPurchasedTimes(ProductID: number, PlayerController: UUGCPlayerController) -> number
```

获得限购商品的购买次数
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetAllLimitPurchasedProducts`

```text
GetAllLimitPurchasedProducts(PlayerController: UUGCPlayerController) -> table
```

获取所有已购买的限购商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetPurchasedTimes`

```text
GetPurchasedTimes(ProductID: number, PlayerController: UUGCPlayerController) -> number
```

获得商品的累计购买次数
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `GetAllPurchasedProducts`

```text
GetAllPurchasedProducts(PlayerController: UUGCPlayerController) -> table
```

获取所有已购买的商品
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerController` | `UUGCPlayerController` | 玩家控制器，客户端可以不传 |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetAllProductData`

```text
GetAllProductData() -> table
```

获取所有商品信息
生效范围：客户端&&服务器

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetProductData`

```text
GetProductData(ProductID: number) -> table
```

获取指定商品信息
生效范围：客户端&&服务端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ProductID` | `number` | 商品的ID |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

## Language

`lua`
