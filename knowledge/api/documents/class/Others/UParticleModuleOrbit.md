---
id: "api:class:UParticleModuleOrbit"
title: "UParticleModuleOrbit"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleOrbit.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleOrbit

## Inheritance

`UParticleModuleOrbitBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChainMode` | `TEnumAsByte < enum EOrbitChainMode >` | Orbit modules will chain together in the order they appear in the module stack.<br>	 	The combination of a module with the one prior to it is defined by using one<br>	 	of the following enumerations:<br>	 		EOChainMode_Add		Add the values to the previous results<br>	 		EOChainMode_Scale	Multiply the values by the previous results<br>	 		EOChainMode_Link	'Break' the chain and apply the values from the	previous results |
| `OffsetAmount` | `FRawDistributionVector` | The amount to offset the sprite from the particle position. |
| `OffsetOptions` | `FOrbitOptions` | The options associated with the OffsetAmount look-up. |
| `RotationAmount` | `FRawDistributionVector` | The amount (in 'turns') to rotate the offset about the particle position.<br>	 		0.0 = no rotation<br>	 		0.5	= 180 degree rotation<br>	 		1.0 = 360 degree rotation |
| `RotationOptions` | `FOrbitOptions` | The options associated with the RotationAmount look-up. |
| `RotationRateAmount` | `FRawDistributionVector` | The rate (in 'turns') at which to rotate the offset about the particle positon.<br>	 		0.0 = no rotation<br>	 		0.5	= 180 degree rotation<br>	 		1.0 = 360 degree rotation |
| `RotationRateOptions` | `FOrbitOptions` | The options associated with the RotationRateAmount look-up. |

## Language

`cpp`
