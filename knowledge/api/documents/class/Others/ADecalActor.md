---
id: "api:class:ADecalActor"
title: "ADecalActor"
source: "https://developer.gp.qq.com/api/class/detail/Others/ADecalActor.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ADecalActor

DecalActor contains a DecalComponent which can be used to render material modifications on top of existing geometry.

 @see UDecalComponent

## Inheritance

`AActor`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Decal` | `UDecalComponent *` | The decal component for this decal actor |
| `ArrowComponent` | `UArrowComponent *` | Reference to the editor only arrow visualization component |
| `SpriteComponent` | `UBillboardComponent *` | Reference to the billboard component |
| `BoxComponent_DEPRECATED` | `UBoxComponent *` | - |

## Functions

### `SetDecalMaterial`

```text
SetDecalMaterial(NewDecalMaterial: UMaterialInterface *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewDecalMaterial` | `UMaterialInterface *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDecalMaterial`

```text
GetDecalMaterial() -> UMaterialInterface *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInterface *` | - |

### `CreateDynamicMaterialInstance`

```text
CreateDynamicMaterialInstance() -> UMaterialInstanceDynamic *
```

**Returns**

| Type | Description |
|---|---|
| `UMaterialInstanceDynamic *` | - |

## Language

`cpp`
