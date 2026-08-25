---
id: "api:class:UUGCItemWarehouseBase"
title: "UUGCItemWarehouseBase"
source: "https://developer.gp.qq.com/api/class/detail/Others/UUGCItemWarehouseBase.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UUGCItemWarehouseBase

仓库对象

## Inheritance

`UObject` -> `IUGCItemContainerInterface`

## Delegates

### `ItemChangeDelegate`

```text
ItemChangeDelegate(ChangeType: const EUGCItemChangeType&, DefineID: const FItemDefineID&) -> void
```

当仓库物品实例数据发生改变时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ChangeType` | `const EUGCItemChangeType&` | - |
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemAddDelegate`

```text
ItemAddDelegate(DefineID: const FItemDefineID&) -> void
```

当仓库新增物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemUpdateDelegate`

```text
ItemUpdateDelegate(DefineID: const FItemDefineID&) -> void
```

当物品实例数据更新时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ItemRemoveDelegate`

```text
ItemRemoveDelegate(DefineID: const FItemDefineID&) -> void
```

当移除物品实例时广播
	  广播范围：服务端 & 客户端

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DefineID` | `const FItemDefineID&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
