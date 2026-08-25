---
id: "api:class:ASkeletalMeshActor"
title: "ASkeletalMeshActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/ASkeletalMeshActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ASkeletalMeshActor

SkeletalMeshActor is an instance of a USkeletalMesh in the world.
  Skeletal meshes are deformable meshes that can be animated and change their geometry at run-time.
  Skeletal meshes dragged into the level from the Content Browser are automatically converted to StaticMeshActors.
  
  @see USkeletalMesh

## Inheritance

`AActor` -> `IMatineeAnimInterface` -> `IObjectPoolInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShouldDoAnimNotifies` | `uint32` | Whether or not this actor should respond to anim notifies - CURRENTLY ONLY AFFECTS PlayParticleEffect NOTIFIES |
| `bWakeOnLevelStart_DEPRECATED` | `uint32` | - |
| `bSupportObjectPool` | `uint32` | - |
| `SkeletalMeshComponent` | `USkeletalMeshComponent *` | - |
| `ReplicatedMesh` | `USkeletalMesh *` | Used to replicate mesh to clients |
| `ReplicatedPhysAsset` | `UPhysicsAsset *` | Used to replicate physics asset to clients |
| `ReplicatedMaterial0` | `UMaterialInterface *` | used to replicate the material in index 0 |
| `ReplicatedMaterial1` | `UMaterialInterface *` | - |

## Functions

### `OnRep_ReplicatedMesh`

```text
OnRep_ReplicatedMesh() -> void
```

Replication Notification Callbacks

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedPhysAsset`

```text
OnRep_ReplicatedPhysAsset() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedMaterial0`

```text
OnRep_ReplicatedMaterial0() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ReplicatedMaterial1`

```text
OnRep_ReplicatedMaterial1() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
