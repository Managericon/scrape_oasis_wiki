---
id: "api:class:USTBaseBuffSystemComponent"
title: "USTBaseBuffSystemComponent"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/Buff/USTBaseBuffSystemComponent.json"
category: "API Wiki/class/和平类事件/Buff"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USTBaseBuffSystemComponent

Buff管理组件

## Inheritance

`UActorComponent` -> `IUTSkillInstanceNodeContainerInterface` -> `IObjectPoolInterface`

## Delegates

### `UGC_BuffAttachedDelegate`

```text
UGC_BuffAttachedDelegate(BuffName: const FName&) -> void
```

Buff添加委托
	  生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuffName` | `const FName&` | Buff名字 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_BuffDetachedDelegate`

```text
UGC_BuffDetachedDelegate(BuffName: const FName&) -> void
```

Buff移除委托
	  生效范围：SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BuffName` | `const FName&` | Buff名字 |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
