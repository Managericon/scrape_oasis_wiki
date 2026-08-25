---
id: "api:class:UUGCBackpackAvatarHandle"
title: "UUGCBackpackAvatarHandle"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUGCBackpackAvatarHandle.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUGCBackpackAvatarHandle

外显装备基类

## Inheritance

`UBackpackAvatarHandle` -> `IUGCItemDataInterface` -> `IUGCObjectItemTableInterface` -> `IUGCItemEquipmentInterface` -> `IUGCItemEquipTargetInterface` -> `IUGCCommonDeadDropItemInterface` -> `IUGCBattleEquipHandleAttachInterface`

## Events

### `OnDurabilityChanged`

```text
OnDurabilityChanged(OriginDurability: float, ChangedDurability: float) -> void
```

当物品耐久度变化时执行
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OriginDurability` | `float` | 原始耐久度 |
| `ChangedDurability` | `float` | 改变后的耐久度 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
