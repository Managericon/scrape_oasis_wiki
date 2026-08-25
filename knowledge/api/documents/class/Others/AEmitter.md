---
id: "api:class:AEmitter"
title: "AEmitter"
source: "https://developer.gp.qq.com/api/class/detail/Others/AEmitter.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# AEmitter

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParticleSystemComponent` | `UParticleSystemComponent *` | - |
| `bDestroyOnSystemFinish` | `uint32` | - |
| `bPostUpdateTickGroup` | `uint32` | - |
| `bCurrentlyActive` | `uint32` | used to update status of toggleable level placed emitters on clients |

## Functions

### `OnParticleSystemFinished`

```text
OnParticleSystemFinished(FinishedComponent: UParticleSystemComponent *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FinishedComponent` | `UParticleSystemComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_bCurrentlyActive`

```text
OnRep_bCurrentlyActive() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Activate`

```text
Activate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Deactivate`

```text
Deactivate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ToggleActive`

```text
ToggleActive() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsActive`

```text
IsActive() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetTemplate`

```text
SetTemplate(NewTemplate: UParticleSystem *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewTemplate` | `UParticleSystem *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetFloatParameter`

```text
SetFloatParameter(ParameterName: FName, Param: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetVectorParameter`

```text
SetVectorParameter(ParameterName: FName, Param: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetColorParameter`

```text
SetColorParameter(ParameterName: FName, Param: FLinearColor) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetActorParameter`

```text
SetActorParameter(ParameterName: FName, Param: AActor *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaterialParameter`

```text
SetMaterialParameter(ParameterName: FName, Param: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Param` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnParticleSpawn`

```text
OnParticleSpawn(EventName: FName, EmitterTime: float, Location: FVector, Velocity: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `Location` | `FVector` | - |
| `Velocity` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnParticleBurst`

```text
OnParticleBurst(EventName: FName, EmitterTime: float, ParticleCount: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `ParticleCount` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnParticleDeath`

```text
OnParticleDeath(EventName: FName, EmitterTime: float, ParticleTime: int32, Location: FVector, Velocity: FVector, Direction: FVector) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `ParticleTime` | `int32` | - |
| `Location` | `FVector` | - |
| `Velocity` | `FVector` | - |
| `Direction` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnParticleCollide`

```text
OnParticleCollide(EventName: FName, EmitterTime: float, ParticleTime: int32, Location: FVector, Velocity: FVector, Direction: FVector, Normal: FVector, BoneName: FName, PhysMat: UPhysicalMaterial*) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EventName` | `FName` | - |
| `EmitterTime` | `float` | - |
| `ParticleTime` | `int32` | - |
| `Location` | `FVector` | - |
| `Velocity` | `FVector` | - |
| `Direction` | `FVector` | - |
| `Normal` | `FVector` | - |
| `BoneName` | `FName` | - |
| `PhysMat` | `UPhysicalMaterial*` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
