---
id: "api:class:USpotLightComponent"
title: "USpotLightComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/USpotLightComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USpotLightComponent

A spot light component emits a directional cone shaped light (Eg a Torch).

## Inheritance

`UPointLightComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `InnerConeAngle` | `float` | Degrees. |
| `OuterConeAngle` | `float` | Degrees. |
| `bCastPhotonShadow` | `uint32` | #if WITH_PHOTON_SHADOW<br>	 Whether the light should cast photon shadow for character<br>	 #endif |
| `NearPlaneOffset` | `float` | - |
| `FarPlaneOffset` | `float` | - |
| `LightShaftConeAngle` | `float` | Degrees. <br>	UPROPERTY(EditAnywhere, BlueprintReadOnly, Category=LightShaft, meta=(UIMin = "1.0", UIMax = "180.0")) |

## Functions

### `SetInnerConeAngle`

```text
SetInnerConeAngle(NewInnerConeAngle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewInnerConeAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetOuterConeAngle`

```text
SetOuterConeAngle(NewOuterConeAngle: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewOuterConeAngle` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
