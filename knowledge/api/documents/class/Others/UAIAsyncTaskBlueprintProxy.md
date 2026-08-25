---
id: "api:class:UAIAsyncTaskBlueprintProxy"
title: "UAIAsyncTaskBlueprintProxy"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAIAsyncTaskBlueprintProxy.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAIAsyncTaskBlueprintProxy

## Inheritance

`UObject`

## Functions

### `OnMoveCompleted`

```text
OnMoveCompleted(RequestID: FAIRequestID, MovementResult: EPathFollowingResult :: Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `RequestID` | `FAIRequestID` | - |
| `MovementResult` | `EPathFollowingResult :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnSuccess`

```text
OnSuccess(MovementResult: EPathFollowingResult::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MovementResult` | `EPathFollowingResult::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnFail`

```text
OnFail(MovementResult: EPathFollowingResult::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MovementResult` | `EPathFollowingResult::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
