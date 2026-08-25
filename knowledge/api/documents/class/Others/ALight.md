---
id: "api:class:ALight"
title: "ALight"
source: "https://developer.gp.qq.com/api/class/detail/Others/ALight.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ALight

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LightComponent` | `ULightComponent *` | @todo document |
| `bEnabled` | `uint32` | replicated copy of LightComponent's bEnabled property |

## Functions

### `OnRep_bEnabled`

```text
OnRep_bEnabled() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetEnabled`

```text
SetEnabled(bSetEnabled: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bSetEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsEnabled`

```text
IsEnabled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ToggleEnabled`

```text
ToggleEnabled() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBrightness`

```text
SetBrightness(NewBrightness: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewBrightness` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBrightness`

```text
GetBrightness() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetLightColor`

```text
SetLightColor(NewLightColor: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLightColor`

```text
GetLightColor() -> FLinearColor
```

**Returns**

| Type | Description |
|---|---|
| `FLinearColor` | - |

### `SetLightFunctionMaterial`

```text
SetLightFunctionMaterial(NewLightFunctionMaterial: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionScale`

```text
SetLightFunctionScale(NewLightFunctionScale: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionScale` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLightFunctionFadeDistance`

```text
SetLightFunctionFadeDistance(NewLightFunctionFadeDistance: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLightFunctionFadeDistance` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCastShadows`

```text
SetCastShadows(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAffectTranslucentLighting`

```text
SetAffectTranslucentLighting(bNewValue: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNewValue` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
