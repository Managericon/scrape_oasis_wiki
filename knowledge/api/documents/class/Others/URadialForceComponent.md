---
id: "api:class:URadialForceComponent"
title: "URadialForceComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/URadialForceComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# URadialForceComponent

Used to emit a radial force or impulse that can affect physics objects and or destructible objects.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Radius` | `float` | The radius to apply the force or impulse in |
| `Falloff` | `TEnumAsByte < enum ERadialImpulseFalloff >` | How the force or impulse should fall off as object are further away from the center |
| `ImpulseStrength` | `float` | How strong the impulse should be |
| `bImpulseVelChange` | `uint32` | If true, the impulse will ignore mass of objects and will always result in a fixed velocity change |
| `bIgnoreOwningActor` | `uint32` | If true, do not apply forceimpulse to any physics objects that are part of the Actor that owns this component. |
| `ForceStrength` | `float` | How strong the force should be |
| `DestructibleDamage` | `float` | If > 0.f, will cause damage to destructible meshes as well |
| `ObjectTypesToAffect` | `TArray < TEnumAsByte < enum EObjectTypeQuery > >` | The object types that are affected by this radial force |

## Functions

### `FireImpulse`

```text
FireImpulse() -> void
```

Fire a single impulse

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddObjectTypeToAffect`

```text
AddObjectTypeToAffect(ObjectType: TEnumAsByte < enum EObjectTypeQuery >) -> void
```

Add an object type for this radial force to affect

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectType` | `TEnumAsByte < enum EObjectTypeQuery >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveObjectTypeToAffect`

```text
RemoveObjectTypeToAffect(ObjectType: TEnumAsByte < enum EObjectTypeQuery >) -> void
```

Remove an object type that is affected by this radial force

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ObjectType` | `TEnumAsByte < enum EObjectTypeQuery >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
