---
id: "api:class:UPaperSpriteComponent"
title: "UPaperSpriteComponent"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPaperSpriteComponent.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPaperSpriteComponent

A component that handles rendering and collision for a single instance of a UPaperSprite asset.
 
  This component is created when you drag a sprite asset from the content browser into a Blueprint, or
  contained inside of the actor created when you drag one into the level.
 
  @see UPrimitiveComponent, UPaperSprite

## Inheritance

`UMeshComponent`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceSprite` | `UPaperSprite *` | - |
| `MaterialOverride_DEPRECATED` | `UMaterialInterface *` | - |
| `SpriteColor` | `FLinearColor` | - |

## Functions

### `SetSprite`

```text
SetSprite(NewSprite: UPaperSprite *) -> bool
```

Change the PaperSprite used by this instance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSprite` | `UPaperSprite *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetSprite`

```text
GetSprite() -> UPaperSprite *
```

Gets the PaperSprite used by this instance.

**Returns**

| Type | Description |
|---|---|
| `UPaperSprite *` | - |

### `SetSpriteColor`

```text
SetSpriteColor(NewColor: FLinearColor) -> void
```

Set color of the sprite

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewColor` | `FLinearColor` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
