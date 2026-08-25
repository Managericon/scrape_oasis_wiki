---
id: "api:class:UPaperFlipbook"
title: "UPaperFlipbook"
source: "https://developer.gp.qq.com/api/class/detail/Others/UPaperFlipbook.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UPaperFlipbook

Contains an animation sequence of sprite frames

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FramesPerSecond` | `float` | - |
| `KeyFrames` | `TArray < FPaperFlipbookKeyFrame >` | - |
| `DefaultMaterial` | `UMaterialInterface *` | - |
| `CollisionSource` | `TEnumAsByte < EFlipbookCollisionMode :: Type >` | - |

## Functions

### `GetNumFrames`

```text
GetNumFrames() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetTotalDuration`

```text
GetTotalDuration() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetKeyFrameIndexAtTime`

```text
GetKeyFrameIndexAtTime(Time: float, bClampToEnds: bool) -> int32
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bClampToEnds` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetSpriteAtTime`

```text
GetSpriteAtTime(Time: float, bClampToEnds: bool) -> UPaperSprite *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `float` | - |
| `bClampToEnds` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `UPaperSprite *` | - |

### `GetSpriteAtFrame`

```text
GetSpriteAtFrame(FrameIndex: int32) -> UPaperSprite *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FrameIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `UPaperSprite *` | - |

### `GetNumKeyFrames`

```text
GetNumKeyFrames() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsValidKeyFrameIndex`

```text
IsValidKeyFrameIndex(Index: int32) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Language

`cpp`
