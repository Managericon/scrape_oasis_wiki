---
id: "api:class:UUGCMBackpackComponentV2"
title: "UUGCMBackpackComponentV2"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUGCMBackpackComponentV2.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUGCMBackpackComponentV2

手机 V2背包组件

## Inheritance

`UBackpackComponentV2`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Compatible_ItemOperationDelegate` | `FItemOperationDelegate` | Delegate<br>	  平替经典 ItemOperationDelegate：物品操作广播<br>	  由经典背包的同名委托原样转发（见 OnClassicItemOperation），参数与经典完全一致<br>	  广播范围：服务端、客户端 |
| `Compatible_ItemUpdatedDelegate` | `FItemUpdatedDelegate` | Delegate<br>	  平替经典 ItemUpdatedDelegate：物品更新广播<br>	  由经典背包的同名委托原样转发（见 OnClassicItemUpdated），参数与经典完全一致<br>	  广播范围：服务端、客户端 |
| `Compatible_ItemRemovedDelegate` | `FItemRemovedDelegate` | Delegate<br>	  平替经典 ItemRemovedDelegate：物品移除广播<br>	  由经典背包的同名委托原样转发（见 OnClassicItemRemoved），参数与经典完全一致<br>	  广播范围：服务端、客户端 |

## Language

`cpp`
