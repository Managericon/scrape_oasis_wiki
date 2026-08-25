---
id: "api:class:UDamageType"
title: "UDamageType"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDamageType.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDamageType

A DamageType is intended to define and describe a particular form of damage and to provide an avenue 
  for customizing responses to damage from various sources.
 
  For example, a game could make a DamageType_Fire set it up to ignite the damaged actor.
 
  DamageTypes are never instanced and should be treated as immutable data holders with static code
  functionality.  They should never be stateful.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bCausedByWorld` | `uint32` | True if this damagetype is caused by the world (falling off level, into lava, etc). |
| `bScaleMomentumByMass` | `uint32` | True to scale imparted momentum by the receiving pawn's mass for pawns using character movement |
| `bRadialDamageVelChange` | `uint32` | When applying radial impulses, whether to treat as impulse or velocity change. |
| `DamageImpulse` | `float` | The magnitude of impulse to apply to the Actors damaged by this type. |
| `DestructibleImpulse` | `float` | How large the impulse should be applied to destructible meshes |
| `DestructibleDamageSpreadScale` | `float` | How much the damage spreads on a destructible mesh |
| `DamageFalloff` | `float` | Damage fall-off for radius damage (exponent).  Default 1.0=linear, 2.0=square of distance, etc. |

## Functions

### `HasDamageTypeTags_DamageType`

```text
HasDamageTypeTags_DamageType() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetDamageTypeTags_DamageType`

```text
GetDamageTypeTags_DamageType(OutTags: TArray < FName > &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutTags` | `TArray < FName > &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
