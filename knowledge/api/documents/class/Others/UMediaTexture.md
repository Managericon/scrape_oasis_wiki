---
id: "api:class:UMediaTexture"
title: "UMediaTexture"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMediaTexture.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMediaTexture

Implements a texture asset for rendering video tracks from UMediaPlayer assets.

## Inheritance

`UTexture`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AddressX` | `TEnumAsByte < TextureAddress >` | The addressing mode to use for the X axis. |
| `AddressY` | `TEnumAsByte < TextureAddress >` | The addressing mode to use for the Y axis. |
| `AutoClear` | `bool` | Whether to clear the texture when no media is being played (default = enabled). |
| `ClearColor` | `FLinearColor` | The color used to clear the texture if AutoClear is enabled (default = black). |
| `MediaPlayer` | `UMediaPlayer *` | The media player asset associated with this texture. |

## Functions

### `GetAspectRatio`

```text
GetAspectRatio() -> float
```

Gets the current aspect ratio of the texture.

**Returns**

| Type | Description |
|---|---|
| `float` | Texture aspect ratio. |

### `GetHeight`

```text
GetHeight() -> int32
```

Gets the current height of the texture.

**Returns**

| Type | Description |
|---|---|
| `int32` | Texture height (in pixels). |

### `GetWidth`

```text
GetWidth() -> int32
```

Gets the current width of the texture.

**Returns**

| Type | Description |
|---|---|
| `int32` | Texture width (in pixels). |

### `ResetFirstFrame`

```text
ResetFirstFrame() -> void
```

Reset The IsFirstFrameRender&IsFirstFrameNotify to false for iOS

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
