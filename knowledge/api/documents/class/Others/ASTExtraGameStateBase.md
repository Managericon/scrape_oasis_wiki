---
id: "api:class:ASTExtraGameStateBase"
title: "ASTExtraGameStateBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/ASTExtraGameStateBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASTExtraGameStateBase

游戏状态基类

## Inheritance

`AUAEGameState` -> `IUAELevelEventCenterInterface` -> `IImmediateUIInterface`

## Delegates

### `UGCPickupUsefulDelegate`

```text
UGCPickupUsefulDelegate(defineID: FItemDefineID) -> FUGCItemUsefulType
```

推荐拾取处理委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `defineID` | `FItemDefineID` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCItemUsefulType` | - |

### `UGCAutoPickupItemDelegate`

```text
UGCAutoPickupItemDelegate(defineID: FItemDefineID) -> FUGCAutoPickType
```

自动拾取处理委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `defineID` | `FItemDefineID` | - |

**Returns**

| Type | Description |
|---|---|
| `FUGCAutoPickType` | - |

## Language

`cpp`
