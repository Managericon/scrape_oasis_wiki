---
id: "api:class:ASTExtraWeapon"
title: "ASTExtraWeapon"
source: "https://developer.gp.qq.com/api/class/detail/%E5%92%8C%E5%B9%B3%E7%B1%BB%E4%BA%8B%E4%BB%B6/%E6%AD%A6%E5%99%A8/ASTExtraWeapon.json"
category: "API Wiki/class/和平类事件/武器"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASTExtraWeapon

武器基类

## Inheritance

`AActor` -> `IOwnerRelevancyDependencyInterface` -> `IRegionObjectInterface` -> `IActorHiddenInterface` -> `IAttrModifyInterface` -> `IActorFeedbackInterface` -> `IGenericAbilityCarrierInterface` -> `IGameAttributeCarrierInterface` -> `ILogicEffectInterface` -> `IUAESharedModuleInterface` -> `IOwnershipChainInterface`

## Events

### `OnWeaponMeshLoadFinished`

```text
OnWeaponMeshLoadFinished(SlotID: int32, IsEquipped: bool) -> void
```

武器加载模型完毕的接口，之后可以获取武器的MeshComponent
	 生效范围：C

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SlotID` | `int32` | - |
| `IsEquipped` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnWeaponDrawHUDDelegate`

```text
OnWeaponDrawHUDDelegate(WeaponHudWidget: UHUDWidgetBase*, Canvas: UCanvas*) -> void
```

Delegate
	  生效范围C
	  武器绘制HUD事件，传入武器的HUDWidiget， Canvas

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WeaponHudWidget` | `UHUDWidgetBase*` | - |
| `Canvas` | `UCanvas*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPressingWeaponFuncBtnDelegate`

```text
OnPressingWeaponFuncBtnDelegate(DeltaTime: float) -> void
```

Delegate
	  生效范围C
	  持续按键事件，有DeltaTime传入

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeltaTime` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `UGC_AttachmentChangeDelegate`

```text
UGC_AttachmentChangeDelegate(AttachHandleID: int32, IsEquip: bool) -> void
```

武器配件装卸委托
	 
	  生效范围SC

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AttachHandleID` | `int32` | 配件ID |
| `IsEquip` | `bool` | 是否是装备配件 |

**Returns**

| Type | Description |
|---|---|
| `void` | void |

### `OnWeaponTriggerEventDelegate`

```text
OnWeaponTriggerEventDelegate(Event: EWeaponTriggerEvent, EventData: const FString&) -> void
```

Delegate
	  生效范围C
	  武器按键事件

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Event` | `EWeaponTriggerEvent` | - |
| `EventData` | `const FString&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnWeaponAttachToBackpackDelegate`

```text
OnWeaponAttachToBackpackDelegate() -> void
```

Delegate
	  生效范围SC
	  武器挂背事件

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
