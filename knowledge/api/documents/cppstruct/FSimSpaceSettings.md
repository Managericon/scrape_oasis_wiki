---
id: "api:cppstruct:FSimSpaceSettings"
title: "FSimSpaceSettings"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FSimSpaceSettings.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FSimSpaceSettings

Settings for the system which passes motion of the simulation's space into the simulation. This allows the simulation to pass a 
  fraction of the world space motion onto the bodies which allows Bone-Space and Component-Space simulations to react to world-space 
  movement in a controllable way.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MasterAlpha` | `float` | - |
| `VelocityScaleZ` | `float` | - |
| `MaxLinearVelocity` | `float` | - |
| `MaxAngularVelocity` | `float` | - |
| `MaxLinearAcceleration` | `float` | - |
| `MaxAngularAcceleration` | `float` | - |
| `ExternalLinearDrag_DEPRECATED` | `float` | - |
| `ExternalLinearDragV` | `FVector` | - |
| `ExternalLinearVelocity` | `FVector` | - |
| `ExternalAngularVelocity` | `FVector` | - |
