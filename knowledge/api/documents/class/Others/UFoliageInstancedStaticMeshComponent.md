---
id: "api:class:UFoliageInstancedStaticMeshComponent"
title: "UFoliageInstancedStaticMeshComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UFoliageInstancedStaticMeshComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UFoliageInstancedStaticMeshComponent

## Inheritance

`UHierarchicalInstancedStaticMeshComponent`

## Delegates

### `OnInstanceTakePointDamage`

```text
OnInstanceTakePointDamage(InstanceIndex: int32, Damage: float, InstigatedBy: AController*, HitLocation: FVector, ShotFromDirection: FVector, DamageType: const class UDamageType*, DamageCauser: AActor*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `Damage` | `float` | - |
| `InstigatedBy` | `AController*` | - |
| `HitLocation` | `FVector` | - |
| `ShotFromDirection` | `FVector` | - |
| `DamageType` | `const class UDamageType*` | - |
| `DamageCauser` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnInstanceTakeRadialDamage`

```text
OnInstanceTakeRadialDamage(Instances: const TArray<int32>&, Damages: const TArray<float>&, InstigatedBy: AController*, Origin: FVector, MaxRadius: float, DamageType: const class UDamageType*, DamageCauser: AActor*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Instances` | `const TArray&` | - |
| `Damages` | `const TArray&` | - |
| `InstigatedBy` | `AController*` | - |
| `Origin` | `FVector` | - |
| `MaxRadius` | `float` | - |
| `DamageType` | `const class UDamageType*` | - |
| `DamageCauser` | `AActor*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
