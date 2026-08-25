---
id: "api:class:UMediaSource"
title: "UMediaSource"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMediaSource.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMediaSource

Abstract base class for media sources.
 
  Media sources describe the location andor settings of media objects that can
  be played in a media player, such as a video file on disk, a video stream on
  the internet, or a web cam attached to or built into the target device. The
  location is encoded as a media URL string, whose URI scheme and optional file
  extension will be used to locate a suitable media player.

## Inheritance

`UObject` -> `IMediaOptions`

## Functions

### `GetUrl`

```text
GetUrl() -> FString
```

Get the media source's URL string (must be implemented in child classes).

**Returns**

| Type | Description |
|---|---|
| `FString` | The media URL. |

### `Validate`

```text
Validate() -> bool
```

Validate the media source settings (must be implemented in child classes).

**Returns**

| Type | Description |
|---|---|
| `bool` | true if validation passed, false otherwise. |

## Language

`cpp`
