---
id: "api:class:UMediaPlaylist"
title: "UMediaPlaylist"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMediaPlaylist.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMediaPlaylist

Implements a media play list.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Loop` | `uint32` | Whether the play list should loop (default = true). |
| `Items` | `TArray < UMediaSource * >` | List of media sources to play. |

## Functions

### `Add`

```text
Add(MediaSource: UMediaSource *) -> bool
```

Add a media source to the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to append. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was added, false otherwise. |

### `AddFile`

```text
AddFile(FilePath: FString &) -> bool
```

Add a media file path to the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FilePath` | `FString &` | The file path to add. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the file was added, false otherwise. |

### `AddUrl`

```text
AddUrl(Url: FString &) -> bool
```

Add a media URL to the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Url` | `FString &` | The URL to add. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the URL was added, false otherwise. |

### `Get`

```text
Get(Index: int32) -> UMediaSource *
```

Get the media source at the specified index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the media source to get. |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The media source, or nullptr if the index doesn't exist. |

### `GetNext`

```text
GetNext(InOutIndex: int32 &) -> UMediaSource *
```

Get the next media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOutIndex` | `int32 &` | Index of the current media source (will contain the new index). |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The media source after the current one, or nullptr if the list is empty. |

### `GetPrevious`

```text
GetPrevious(InOutIndex: int32 &) -> UMediaSource *
```

Get the previous media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOutIndex` | `int32 &` | Index of the current media source (will contain the new index). |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The media source before the current one, or nullptr if the list is empty. |

### `GetRandom`

```text
GetRandom(OutIndex: int32 &) -> UMediaSource *
```

Get a random media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutIndex` | `int32 &` | Will contain the index of the returned media source. |

**Returns**

| Type | Description |
|---|---|
| `UMediaSource *` | The random media source, or nullptr if the list is empty. |

### `Insert`

```text
Insert(MediaSource: UMediaSource *, Index: int32) -> void
```

Insert a media source into the play list at the given position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to insert. |
| `Index` | `int32` | The index to insert into. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Num`

```text
Num() -> int32
```

Get the number of media sources in the play list.

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of media sources. |

### `Remove`

```text
Remove(MediaSource: UMediaSource *) -> bool
```

Remove all occurrences of the given media source in the play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to remove. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was removed, false otherwise. |

### `RemoveAt`

```text
RemoveAt(Index: int32) -> bool
```

Remove the media source at the specified position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the media source to remove. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was removed, false otherwise. |

### `Replace`

```text
Replace(Index: int32, Replacement: UMediaSource *) -> bool
```

Replace the media source at the specified position.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | The index of the media source to replace. |
| `Replacement` | `UMediaSource *` | The replacement media source. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source was replaced, false otherwise. |

## Language

`cpp`
