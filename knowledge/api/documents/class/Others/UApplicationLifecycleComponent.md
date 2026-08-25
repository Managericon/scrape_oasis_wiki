---
id: "api:class:UApplicationLifecycleComponent"
title: "UApplicationLifecycleComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UApplicationLifecycleComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UApplicationLifecycleComponent

Component to handle receiving notifications from the OS about application state (activated, suspended, termination, etc).

## Inheritance

`UActorComponent`

## Delegates

### `ApplicationWillDeactivateDelegate`

```text
ApplicationWillDeactivateDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationHasReactivatedDelegate`

```text
ApplicationHasReactivatedDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationWillEnterBackgroundDelegate`

```text
ApplicationWillEnterBackgroundDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationHasEnteredForegroundDelegate`

```text
ApplicationHasEnteredForegroundDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationWillTerminateDelegate`

```text
ApplicationWillTerminateDelegate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTemperatureChangeDelegate`

```text
OnTemperatureChangeDelegate(Severity: ETemperatureSeverityType) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Severity` | `ETemperatureSeverityType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
