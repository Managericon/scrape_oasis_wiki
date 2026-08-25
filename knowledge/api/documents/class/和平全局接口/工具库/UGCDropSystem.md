---
id: "api:class:UGCDropSystem"
title: "UGCDropSystem"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E5%85%A8%E5%B1%80%E6%8E%A5%E5%8F%A3/%E5%B7%A5%E5%85%B7%E5%BA%93/UGCDropSystem.json"
category: "API Wiki/class/和平全局接口/工具库"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCDropSystem

掉落系统接口库

## Functions

### `DropItems`

```text
DropItems(DropID: number) -> table
```

根据掉落信息进行物品掉落
根据权重掉落：每次掉落一个物品
根据概率掉落：每次根据物品表的物品数量掉落物品
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DropID` | `number` | 掉落ID |

**Returns**

| Type | Description |
|---|---|
| `table` | 掉落结果 {key-物品ID : value-物品数量} |

### `DropItemsByGroup`

```text
DropItemsByGroup(DropGroupID: number) -> table
```

根据掉落组信息进行物品掉落
掉落组配置参考掉落表格配置（DropGroup Table）
生效范围：服务器&客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DropGroupID` | `number` | 掉落组ID |

**Returns**

| Type | Description |
|---|---|
| `table` | 掉落结果 {key-物品ID : value-物品数量} |

## Language

`lua`
