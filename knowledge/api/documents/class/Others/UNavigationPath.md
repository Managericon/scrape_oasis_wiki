---
id: "api:class:UNavigationPath"
title: "UNavigationPath"
source: "https://developer.gp.qq.com/api/class/detail/Others/UNavigationPath.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UNavigationPath

UObject wrapper for FNavigationPath

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PathPoints` | `TArray < FVector >` | - |
| `RecalculateOnInvalidation` | `TEnumAsByte < ENavigationOptionFlag :: Type >` | - |

## Functions

### `GetDebugString`

```text
GetDebugString() -> FString
```

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

### `EnableDebugDrawing`

```text
EnableDebugDrawing(bShouldDrawDebugData: bool, PathColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bShouldDrawDebugData` | `bool` | - |
| `PathColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableRecalculationOnInvalidation`

```text
EnableRecalculationOnInvalidation(DoRecalculation: TEnumAsByte < ENavigationOptionFlag :: Type >) -> void
```

if enabled path will request recalculation if it gets invalidated due to a change to underlying navigation

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DoRecalculation` | `TEnumAsByte < ENavigationOptionFlag :: Type >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPathLength`

```text
GetPathLength() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetPathCost`

```text
GetPathCost() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `IsPartial`

```text
IsPartial() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsValid`

```text
IsValid() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsStringPulled`

```text
IsStringPulled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `PathUpdatedNotifier`

```text
PathUpdatedNotifier(AffectedPath: UNavigationPath*, PathEvent: TEnumAsByte<ENavPathEvent::Type>) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AffectedPath` | `UNavigationPath*` | - |
| `PathEvent` | `TEnumAsByte` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
