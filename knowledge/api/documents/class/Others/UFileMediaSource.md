---
id: "api:class:UFileMediaSource"
title: "UFileMediaSource"
source: "https://developer.gp.qq.com/api/class/detail/Others/UFileMediaSource.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UFileMediaSource

## Inheritance

`UBaseMediaSource`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FilePath` | `FString` | The path to the media file to be played.<br>	 <br>	  @see SetFilePath |
| `PrecacheFile` | `bool` | Load entire media file into memory and play from there (if possible). |

## Functions

### `SetFilePath`

```text
SetFilePath(Path: FString &) -> void
```

Set the path to the media file that this source represents.
	 
	  Automatically converts full paths to media sources that reside in the
	  Engine's or project's ContentMovies directory into relative paths.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Path` | `FString &` | The path to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
