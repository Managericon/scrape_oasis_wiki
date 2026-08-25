---
id: "api:class:USceneCaptureComponent"
title: "USceneCaptureComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/USceneCaptureComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# USceneCaptureComponent

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `PrimitiveRenderMode` | `ESceneCapturePrimitiveRenderMode` | Controls what primitives get rendered into the scene capture. |
| `HiddenComponents` | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | The components won't rendered by current component. |
| `HiddenActors` | `TArray < AActor * >` | The actors to hide in the scene capture. |
| `ShowOnlyComponents` | `TArray < TWeakObjectPtr < UPrimitiveComponent > >` | The only components to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList. |
| `bShowAttachedActor` | `bool` | - |
| `ShowOnlyActors` | `TArray < AActor * >` | The only actors to be rendered by this scene capture, if PrimitiveRenderMode is set to UseShowOnlyList. |
| `bCaptureEveryFrame` | `bool` | Whether to update the capture's contents every frame.  If disabled, the component will render once on load and then only when moved. |
| `bCaptureOnMovement` | `bool` | Whether to update the capture's contents on movement.  Disable if you are going to capture manually from blueprint. |
| `bAlwaysPersistRenderingState` | `bool` | Whether to persist the rendering state even if bCaptureEveryFrame==false.  This allows velocities for Motion Blur and Temporal AA to be computed. |
| `LODDistanceFactor` | `float` | Scales the distance used by LOD. Set to values greater than 1 to cause the scene capture to use lower LODs than the main view to speed up the scene capture pass. |
| `MaxViewDistanceOverride` | `float` | if > 0, sets a maximum render distance override.  Can be used to cull distant objects from a reflection if the reflecting plane is in an enclosed area like a hallway or room |
| `CaptureSortPriority` | `int32` | Capture priority within the frame to sort scene capture on GPU to resolve interdependencies between multiple capture components. Highest come first. |
| `ShowFlagSettings` | `TArray < struct FEngineShowFlagsSetting >` | ShowFlags for the SceneCapture's ViewFamily, to control rendering settings for this view. Hidden but accessible through details customization |
| `LightingChannels` | `FLightingChannels` | - |
| `bUseLightingChannels` | `bool` | - |

## Functions

### `HideComponent`

```text
HideComponent(InComponent: UPrimitiveComponent *) -> void
```

Adds the component to our list of hidden components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UPrimitiveComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HideActorComponents`

```text
HideActorComponents(InActor: AActor *) -> void
```

Adds all primitive components in the actor to our list of hidden components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowOnlyComponent`

```text
ShowOnlyComponent(InComponent: UPrimitiveComponent *) -> void
```

Adds the component to our list of show-only components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UPrimitiveComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowOnlyActorComponents`

```text
ShowOnlyActorComponents(InActor: AActor *) -> void
```

Adds all primitive components in the actor to our list of show-only components.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveShowOnlyComponent`

```text
RemoveShowOnlyComponent(InComponent: UPrimitiveComponent *) -> void
```

Removes a component from the Show Only list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InComponent` | `UPrimitiveComponent *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveShowOnlyActorComponents`

```text
RemoveShowOnlyActorComponents(InActor: AActor *) -> void
```

Removes a actor's components from the Show Only list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InActor` | `AActor *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearShowOnlyComponents`

```text
ClearShowOnlyComponents() -> void
```

Clears the Show Only list.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearHiddenComponents`

```text
ClearHiddenComponents() -> void
```

Clears the hidden list.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetCaptureSortPriority`

```text
SetCaptureSortPriority(NewCaptureSortPriority: int32) -> void
```

Changes the value of TranslucentSortPriority.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewCaptureSortPriority` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
