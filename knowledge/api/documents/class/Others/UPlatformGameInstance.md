---
id: "api:class:UPlatformGameInstance"
title: "UPlatformGameInstance"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPlatformGameInstance.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPlatformGameInstance

UObject based class for handling mobile events. Having this object as an option gives the app lifetime access to these global delegates. The component UApplicationLifecycleComponent is destroyed at level loads

## Inheritance

`UGameInstance`

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

### `ApplicationRegisteredForRemoteNotificationsDelegate`

```text
ApplicationRegisteredForRemoteNotificationsDelegate(inArray: const TArray<uint8>&) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inArray` | `const TArray&` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationRegisteredForUserNotificationsDelegate`

```text
ApplicationRegisteredForUserNotificationsDelegate(inInt: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inInt` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationFailedToRegisterForRemoteNotificationsDelegate`

```text
ApplicationFailedToRegisterForRemoteNotificationsDelegate(inString: FString) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inString` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationReceivedRemoteNotificationDelegate`

```text
ApplicationReceivedRemoteNotificationDelegate(inString: FString, inAppState: EApplicationState::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inString` | `FString` | - |
| `inAppState` | `EApplicationState::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationReceivedLocalNotificationDelegate`

```text
ApplicationReceivedLocalNotificationDelegate(inString: FString, inInt: int32, inAppState: EApplicationState::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inString` | `FString` | - |
| `inInt` | `int32` | - |
| `inAppState` | `EApplicationState::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplicationReceivedScreenOrientationChangedNotificationDelegate`

```text
ApplicationReceivedScreenOrientationChangedNotificationDelegate(inScreenOrientation: EScreenOrientation::Type) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `inScreenOrientation` | `EScreenOrientation::Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
