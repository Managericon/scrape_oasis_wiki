---
id: "api:class:UViewport"
title: "UViewport"
source: "https://developer.gp.qq.com/api/class/detail/Others/UViewport.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UViewport

## Inheritance

`UContentWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BackgroundColor` | `FLinearColor` | - |

## Functions

### `GetViewportWorld`

```text
GetViewportWorld() -> UWorld *
```

**Returns**

| Type | Description |
|---|---|
| `UWorld *` | - |

### `GetViewLocation`

```text
GetViewLocation() -> FVector
```

**Returns**

| Type | Description |
|---|---|
| `FVector` | - |

### `SetViewLocation`

```text
SetViewLocation(Location: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Location` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewRotation`

```text
GetViewRotation() -> FRotator
```

**Returns**

| Type | Description |
|---|---|
| `FRotator` | - |

### `SetViewRotation`

```text
SetViewRotation(Rotation: FRotator) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotation` | `FRotator` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Spawn`

```text
Spawn(ActorClass: TSubclassOf < AActor >) -> AActor *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ActorClass` | `TSubclassOf < AActor >` | - |

**Returns**

| Type | Description |
|---|---|
| `AActor *` | - |

## Language

`cpp`
