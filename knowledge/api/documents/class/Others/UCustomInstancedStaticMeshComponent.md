---
id: "api:class:UCustomInstancedStaticMeshComponent"
title: "UCustomInstancedStaticMeshComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCustomInstancedStaticMeshComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCustomInstancedStaticMeshComponent

A custom component that efficiently renders multiple instances of the same StaticMesh.

## Inheritance

`UStaticMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseCustomBounds` | `bool` | - |
| `PerInstanceSMData` | `TArray < FInstancedStaticMeshInstanceData >` | Array of instances, bulk serialized. |
| `PerInstanceSMCustomData` | `TArray < FVector4 >` | Array of custom data for instances. This will contains NumCustomDataFloatsInstanceCount entries. The entries are represented sequantially, in instance order. Can be read in a material and manipulated through Blueprints.<br>	 	Example: If NumCustomDataFloats is 1, then each entry will belong to an instance. Custom data 0 will belong to Instance 0. Custom data 1 will belong to Instance 1 etc.<br>	 	Example: If NumCustomDataFloats is 2, then each pair of sequential entries belong to an instance. Custom data 0 and 1 will belong to Instance 0. Custom data 2 and 3 will belong to Instance 2 etc. |
| `PerInstanceSMCustomDataAdd` | `TArray < FVector4 >` | - |
| `InstancingRandomSeed` | `int32` | Value used to seed the random number stream that generates random numbers for each of this mesh's instances.<br>		this is set to zero (default), it will be populated automatically by the editor. |
| `InstanceStartCullDistance` | `int32` | Distance from camera at which each instance begins to fade out. |
| `InstanceEndCullDistance` | `int32` | Distance from camera at which each instance completely fades out. |
| `InstanceNearCullDistance` | `int32` | Distance from camera at which each instance. |
| `InstanceReorderTable` | `TArray < int32 >` | Mapping from PerInstanceSMData order to instance render buffer order. If empty, the PerInstanceSMData order is used. |
| `RemovedInstances` | `TArray < int32 >` | - |
| `InstanceVisibilityMapping` | `TMap < int32 , FInstanceVisibilityData >` | - |
| `UseDynamicInstanceBuffer` | `bool` | Set to true to permit updating the vertex buffer used in the instance buffer without recreating it completely. This should be used if you plan on dynamically changing the instances at run-time. |
| `KeepInstanceBufferCPUAccess` | `bool` | Set to true to keep instance buffer accessible by the CPU, otherwise it's discarded and considered never changing, only GPU has a copy of the data. |
| `PhysicsSerializer` | `UPhysicsSerializer *` | Serialization of all the InstanceBodies. Helps speed up physics creation time. |
| `StashInstanceTransform` | `TMap < int32 , FMatrix >` | - |
| `NumPendingLightmaps` | `int32` | Number of pending lightmaps still to be calculated (Apply()'d). |

## Functions

### `AddInstance`

```text
AddInstance(InstanceTransform: FTransform &) -> int32
```

Add an instance to this component. Transform is given in local space of this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `AddInstanceWorldSpace`

```text
AddInstanceWorldSpace(WorldTransform: FTransform &) -> int32
```

Add an instance to this component. Transform is given in world space.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldTransform` | `FTransform &` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetCustomDataValue`

```text
SetCustomDataValue(InstanceIndex: int32, CustomDataValue: FVector4, CustomDataAddValue: FVector4, bMarkRenderStateDirty: bool) -> bool
```

Update custom data for specific instance

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `CustomDataValue` | `FVector4` | - |
| `CustomDataAddValue` | `FVector4` | - |
| `bMarkRenderStateDirty` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetInstanceTransform`

```text
GetInstanceTransform(InstanceIndex: int32, OutInstanceTransform: FTransform &, bWorldSpace: bool) -> bool
```

Get the transform for the instance specified. Instance is returned in local space of this component unless bWorldSpace is set.  Returns True on success.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |
| `OutInstanceTransform` | `FTransform &` | - |
| `bWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `UpdateInstanceTransform`

```text
UpdateInstanceTransform(InstanceIndex: int32, NewInstanceTransform: FTransform &, bWorldSpace: bool, bMarkRenderStateDirty: bool, bTeleport: bool) -> bool
```

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | The index of the instance to update |
| `NewInstanceTransform` | `FTransform &` | The new transform |
| `bWorldSpace` | `bool` | If true, the new transform interpreted as a World Space transform, otherwise it is interpreted as Local Space |
| `bMarkRenderStateDirty` | `bool` | If true, the change should be visible immediately. If you are updating many instances you should only set this to true for the last instance. |
| `bTeleport` | `bool` | Whether or not the instance's physics should be moved normally, or teleported (moved instantly, ignoring velocity). |

**Returns**

| Type | Description |
|---|---|
| `bool` | True on success. |

### `BatchUpdateInstancesData`

```text
BatchUpdateInstancesData(StartInstanceIndex: int32, NumInstances: int32, StartCustomData: TArray < FVector4 > &, StartCustomDataAdd: TArray < FVector4 > &, bMarkRenderStateDirty: bool, bTeleport: bool) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartInstanceIndex` | `int32` | - |
| `NumInstances` | `int32` | - |
| `StartCustomData` | `TArray < FVector4 > &` | - |
| `StartCustomDataAdd` | `TArray < FVector4 > &` | - |
| `bMarkRenderStateDirty` | `bool` | - |
| `bTeleport` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `RemoveInstance`

```text
RemoveInstance(InstanceIndex: int32) -> bool
```

Remove the instance specified. Returns True on success. Note that this will leave the array in order, but may shrink it.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ClearInstances`

```text
ClearInstances() -> void
```

Clear all instances being rendered by this component.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstanceCount`

```text
GetInstanceCount() -> int32
```

Get the number of instances in this component.

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetCullDistances`

```text
SetCullDistances(StartCullDistance: int32, EndCullDistance: int32) -> void
```

Sets the fading start and culling end distances for this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `StartCullDistance` | `int32` | - |
| `EndCullDistance` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetNearCullDistance`

```text
SetNearCullDistance(CullDistance: int32) -> void
```

Sets the cull near distance for this component.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CullDistance` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetInstancesOverlappingSphere`

```text
GetInstancesOverlappingSphere(Center: FVector &, Radius: float, bSphereInWorldSpace: bool) -> TArray < int32 >
```

Returns the instances with instance bounds overlapping the specified sphere. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Center` | `FVector &` | - |
| `Radius` | `float` | - |
| `bSphereInWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < int32 >` | - |

### `GetInstancesOverlappingBox`

```text
GetInstancesOverlappingBox(Box: FBox &, bBoxInWorldSpace: bool) -> TArray < int32 >
```

Returns the instances with instance bounds overlapping the specified box. The return value is an array of instance indices.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Box` | `FBox &` | - |
| `bBoxInWorldSpace` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `TArray < int32 >` | - |

### `HideInstance`

```text
HideInstance(InstanceIndices: TArray < int32 > &, bForceLocalLocation: bool) -> bool
```

Update the transform for the instance specified.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndices` | `TArray < int32 > &` | - |
| `bForceLocalLocation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | True on success. |

### `ShowInstance`

```text
ShowInstance(InstanceIndices: TArray < int32 > &) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceIndices` | `TArray < int32 > &` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
