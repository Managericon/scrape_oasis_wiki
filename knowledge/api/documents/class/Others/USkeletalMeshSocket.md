---
id: "api:class:USkeletalMeshSocket"
title: "USkeletalMeshSocket"
source: "https://developer.gp.qq.com/api/class/detail/Others/USkeletalMeshSocket.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USkeletalMeshSocket

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SocketName` | `FName` | Defines a named attachment location on the USkeletalMesh. <br>	 	These are set up in editor and used as a shortcut instead of specifying <br>	 	everything explicitly to AttachComponent in the SkeletalMeshComponent.<br>	 	The Outer of a SkeletalMeshSocket should always be the USkeletalMesh. |
| `BoneName` | `FName` | - |
| `RelativeLocation` | `FVector` | - |
| `RelativeRotation` | `FRotator` | - |
| `RelativeScale` | `FVector` | - |
| `BaseLocation` | `FVector` | - |
| `BaseRotation` | `FRotator` | - |
| `BaseScale` | `FVector` | - |
| `bDynamicCreate` | `bool` | - |
| `RelativeBoneName` | `FName` | - |
| `bForceAlwaysAnimated` | `bool` | If true then the hierarchy of bones this socket is attached to will always be <br>	    evaluated, even if it had previously been removed due to the current lod setting |

## Functions

### `GetSocketLocation`

```text
GetSocketLocation(SkelComp: USkeletalMeshComponent *) -> ENGINE_API FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkelComp` | `USkeletalMeshComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | - |

### `InitializeSocketFromLocation`

```text
InitializeSocketFromLocation(SkelComp: USkeletalMeshComponent *, WorldLocation: FVector, WorldNormal: FVector) -> ENGINE_API void
```

Sets BoneName, RelativeLocation and RelativeRotation based on closest bone to WorldLocation and WorldNormal

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkelComp` | `USkeletalMeshComponent *` | - |
| `WorldLocation` | `FVector` | - |
| `WorldNormal` | `FVector` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`
