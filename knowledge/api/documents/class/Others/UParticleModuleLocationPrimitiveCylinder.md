---
id: "api:class:UParticleModuleLocationPrimitiveCylinder"
title: "UParticleModuleLocationPrimitiveCylinder"
source: "https://developer.gp.qq.com/api/class/detail/Others/UParticleModuleLocationPrimitiveCylinder.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UParticleModuleLocationPrimitiveCylinder

## Inheritance

`UParticleModuleLocationPrimitiveBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `RadialVelocity` | `uint32` | If true, get the particle velocity form the radial distance inside the primitive. |
| `StartRadius` | `FRawDistributionFloat` | The radius of the cylinder. |
| `StartHeight` | `FRawDistributionFloat` | The height of the cylinder, centered about the location. |
| `HeightAxis` | `TEnumAsByte < enum CylinderHeightAxis >` | Determine particle particle system axis that should represent the height of the cylinder.<br>	  Can be one of the following:<br>	    PMLPC_HEIGHTAXIS_X - Orient the height along the particle system X-axis.<br>	    PMLPC_HEIGHTAXIS_Y - Orient the height along the particle system Y-axis.<br>	    PMLPC_HEIGHTAXIS_Z - Orient the height along the particle system Z-axis. |

## Language

`cpp`
