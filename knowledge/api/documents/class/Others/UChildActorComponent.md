---
id: "api:class:UChildActorComponent"
title: "UChildActorComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UChildActorComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UChildActorComponent

A component that spawns an Actor when registered, and destroys it when unregistered.

## Inheritance

`USceneComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ChildActorClass` | `TSubclassOf < AActor >` | The class of Actor to spawn |
| `ChildActor` | `AActor *` | The actor that we spawned and own |
| `bAllowTemplateModification` | `bool` | - |
| `ChildActorTemplate` | `AActor *` | Property to point to the template child actor for details panel purposes |
| `IsDestoryChildActor` | `bool` | - |
| `bKeepChildActorComponet` | `bool` | - |
| `bEnableReplication` | `bool` | - |
| `bDumpChildActorLocation` | `bool` | - |
| `bRedirectComps` | `uint8` | - |
| `bPCOnlyComps` | `uint8` | - |

## Functions

### `SetChildActorClass`

```text
SetChildActorClass(InClass: TSubclassOf < AActor >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InClass` | `TSubclassOf < AActor >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnRep_ChildActor`

```text
OnRep_ChildActor() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CreateChildActor`

```text
CreateChildActor() -> void
```

Create the child actor

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DestroyChildActor`

```text
DestroyChildActor(bNeedInstanceData: bool) -> void
```

Kill any currently present child actor

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bNeedInstanceData` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnChildActorRep`

```text
OnChildActorRep() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
