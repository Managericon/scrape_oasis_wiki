---
id: "api:class:UBehaviorTreeComponent"
title: "UBehaviorTreeComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBehaviorTreeComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBehaviorTreeComponent

## Inheritance

`UBrainComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `NodeInstances` | `TArray < UBTNode * >` | instanced nodes |

## Functions

### `GetTagCooldownEndTime`

```text
GetTagCooldownEndTime(CooldownTag: FGameplayTag) -> float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | - |

**Returns**

| Type | Description |
|---|---|
| `float` | the cooldown tag end time, 0.0f if CooldownTag is not found |

### `AddCooldownTagDuration`

```text
AddCooldownTagDuration(CooldownTag: FGameplayTag, CooldownDuration: float, bAddToExistingDuration: bool) -> void
```

add to the cooldown tag's duration

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CooldownTag` | `FGameplayTag` | - |
| `CooldownDuration` | `float` | - |
| `bAddToExistingDuration` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetDynamicSubtree`

```text
SetDynamicSubtree(InjectTag: FGameplayTag, BehaviorAsset: UBehaviorTree *) -> void
```

assign subtree to RunBehaviorDynamic task specified by tag

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InjectTag` | `FGameplayTag` | - |
| `BehaviorAsset` | `UBehaviorTree *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetUGCMobBTDebugInfo`

```text
GetUGCMobBTDebugInfo(OutTreeInfo: FUGCMobBTDebugInfo &, OutBlackBoardInfo: TArray < FUGCMobBTBlackBoardInfo > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutTreeInfo` | `FUGCMobBTDebugInfo &` | - |
| `OutBlackBoardInfo` | `TArray < FUGCMobBTBlackBoardInfo > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
