---
id: "api:class:UWindDirectionalSourceComponent"
title: "UWindDirectionalSourceComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWindDirectionalSourceComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWindDirectionalSourceComponent

Component that provides a directional wind source. Only affects SpeedTree assets.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Strength` | `float` | - |
| `Speed` | `float` | - |
| `MinGustAmount` | `float` | - |
| `MaxGustAmount` | `float` | - |
| `Radius` | `float` | - |
| `bPointWind` | `uint32` | - |

## Functions

### `SetStrength`

```text
SetStrength(InNewStrength: float) -> void
```

Because the actual data used to query wind is stored on the render thread in
	  an instance of FWindSourceSceneProxy all of our properties are read only.
	  The data can be manipulated with the following functions which will queue 
	  a render thread update for this component
	 
	 Sets the strength of the generated wind

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewStrength` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetSpeed`

```text
SetSpeed(InNewSpeed: float) -> void
```

Sets the windspeed of the generated wind

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewSpeed` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMinimumGustAmount`

```text
SetMinimumGustAmount(InNewMinGust: float) -> void
```

Set minimum deviation for wind gusts

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewMinGust` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaximumGustAmount`

```text
SetMaximumGustAmount(InNewMaxGust: float) -> void
```

Set maximum deviation for wind gusts

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewMaxGust` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetRadius`

```text
SetRadius(InNewRadius: float) -> void
```

Set the effect radius for point wind

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewRadius` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetWindType`

```text
SetWindType(InNewType: EWindSourceType) -> void
```

Set the type of wind generator to use

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InNewType` | `EWindSourceType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
