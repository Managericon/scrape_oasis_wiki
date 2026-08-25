---
id: "api:class:APickUpWrapperActor"
title: "APickUpWrapperActor"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E5%9C%B0%E9%9D%A2%E5%8F%AF%E6%8B%BE%E5%8F%96%E7%89%A9%E7%B1%BB/APickUpWrapperActor.json"
category: "API Wiki/class/和平类事件/地面可拾取物类"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# APickUpWrapperActor

地面可拾取物类

## Inheritance

`AUAENetActor` -> `IGeneratorActorInterface` -> `IPickupInterface` -> `IPickupCustomInterface` -> `IObjectPoolInterface` -> `IManagedActorInterface` -> `IDropActorCurveInterface` -> `IDropItemPerformanceInterface` -> `ILuaInterface` -> `IInteractorInterface` -> `IScopeInteractionInterface`

## Delegates

### `UGC_PickUpWrapperHideDelegate`

```text
UGC_PickUpWrapperHideDelegate(InRefreshTimeStamp: float) -> void
```

生效范围:SC
	 可拾取道具隐藏事件委托

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InRefreshTimeStamp` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PickUpWrapperShowDelegate`

```text
UGC_PickUpWrapperShowDelegate() -> void
```

生效范围:S
	 可拾取道具显示事件委托

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_PickUpWrapperDestroyDelegate`

```text
UGC_PickUpWrapperDestroyDelegate() -> void
```

生效范围:SC
	 可拾取道具销毁事件委托

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
