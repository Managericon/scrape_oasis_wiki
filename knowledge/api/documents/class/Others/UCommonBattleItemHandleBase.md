---
id: "api:class:UCommonBattleItemHandleBase"
title: "UCommonBattleItemHandleBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCommonBattleItemHandleBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCommonBattleItemHandleBase

通用扩展 ItemHandle 基类

## Inheritance

`UBattleItemHandleBase` -> `ICommonBattleItemUseInterface`

## Events

### `CanCreateItemHandleV2`

```text
CanCreateItemHandleV2() -> bool
```

能否创建物品 Handle
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许创建物品 Handle |

### `OnCreateItemHandleV2`

```text
OnCreateItemHandleV2() -> void
```

当创建物品 Handle 后回调
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanDestoryItemHandleV2`

```text
CanDestoryItemHandleV2() -> bool
```

能否销毁物品 Handle
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许销毁物品 Handle |

### `OnDestoryItemHandleV2`

```text
OnDestoryItemHandleV2() -> void
```

销毁物品 Handle 前回调
	  可重载并自定义
	  DS 被调用

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CanUpdateItemCountV2`

```text
CanUpdateItemCountV2(NewItemCount: int32, OldItemCount: int32) -> bool
```

能否更新此物品实例的数量
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewItemCount` | `int32` | - |
| `OldItemCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | 是否允许物品数量更新 |

### `OnUpdateItemCountV2`

```text
OnUpdateItemCountV2(NewItemCount: int32, OldItemCount: int32) -> void
```

物品数量更新后回调
	  可重载并自定义
	  DS 被调用

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewItemCount` | `int32` | - |
| `OldItemCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
