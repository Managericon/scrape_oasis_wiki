---
id: "api:class:UMediaPlayer"
title: "UMediaPlayer"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMediaPlayer.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMediaPlayer

Implements a media player asset that can play movies and other media sources.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CacheAhead` | `FTimespan` | Duration of samples to cache ahead of the play head.<br>	 <br>	  @see CacheBehind, CacheBehindGame |
| `CacheBehind` | `FTimespan` | Duration of samples to cache behind the play head (when not running as game).<br>	 <br>	  @see CacheAhead, CacheBehindGame |
| `CacheBehindGame` | `FTimespan` | Duration of samples to cache behind the play head (when running as game).<br>	 <br>	  @see CacheAhead, CacheBehind |
| `NativeAudioOut` | `bool` | Output any audio via the operating system's sound mixer instead of a Sound Wave asset.<br>	 <br>	  If enabled, the assigned Sound Wave asset will be ignored. The SetNativeVolume<br>	  function can then be used to change the audio output volume at runtime. Note that<br>	  not all media player plug-ins may support native audio output on all platforms.<br>	 <br>	  @see SetNativeVolume |
| `PlayOnOpen` | `bool` | Automatically start playback after media opened successfully.<br>	 <br>	  If disabled, listen to the OnMediaOpened Blueprint event to detect when<br>	  the media finished opening, and then start playback using the Play function.<br>	 <br>	  @see OpenFile, OpenPlaylist, OpenPlaylistIndex, OpenSource, OpenUrl, Play |
| `Shuffle` | `uint32` | Whether playback should shuffle media sources in the play list.<br>	 <br>	  @see OpenPlaylist, OpenPlaylistIndex |
| `Loop` | `uint32` | Whether the player should loop when media playback reaches the end.<br>	 <br>	  Use the SetLooping function to change this value at runtime.<br>	 <br>	  @see IsLooping, SetLooping |
| `Playlist` | `UMediaPlaylist *` | The play list to use, if any.<br>	 <br>	  Use the OpenPlaylist or OpenPlaylistIndex function to change this value at runtime.<br>	 <br>	  @see OpenPlaylist, OpenPlaylistIndex |
| `PlaylistIndex` | `int32` | The current index of the source in the play list being played.<br>	 <br>	  Use the Previous and Next methods to change this value at runtime.<br>	 <br>	  @see Next, Previous |
| `HorizontalFieldOfView` | `float` | The initial horizontal field of view (in Euler degrees; default = 90).<br>	 <br>	  This setting is used only for 360 videos. It determines the portion of the<br>	  video that is visible at a time. To modify the field of view at runtime in<br>	  Blueprints, use the SetHorizontalFieldOfView function.<br>	 <br>	  @see GetHorizontalFieldOfView, SetHorizontalFieldOfView, VerticalFieldOfView, ViewRotation |
| `VerticalFieldOfView` | `float` | The initial vertical field of view (in Euler degrees; default = 60).<br>	 <br>	  This setting is used only for 360 videos. It determines the portion of the<br>	  video that is visible at a time. To modify the field of view at runtime in<br>	  Blueprints, use the SetHorizontalFieldOfView function.<br>	 <br>	  Please note that some 360 video players may be able to change only the<br>	  horizontal field of view, and this setting may be ignored.<br>	 <br>	  @see GetVerticalFieldOfView, SetVerticalFieldOfView, HorizontalFieldOfView, ViewRotation |
| `ViewRotation` | `FRotator` | The initial view rotation.<br>	 <br>	  This setting is used only for 360 videos. It determines the rotation of<br>	  the video's view. To modify the view orientation at runtime in Blueprints,<br>	  use the GetViewRotation and SetViewRotation functions.<br>	 <br>	  Please note that not all players may support video view rotations.<br>	 <br>	  @see GetViewRotation, SetViewRotation, HorizontalFieldOfView, VerticalFieldOfView |
| `PlayerGuid` | `FGuid` | The player's globally unique identifier. |

## Functions

### `CanPause`

```text
CanPause() -> bool
```

Check whether media playback can be paused right now.
	 
	  Playback can be paused if the media supports pausing and if it is currently playing.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if pausing playback can be paused, false otherwise. |

### `CanPlaySource`

```text
CanPlaySource(MediaSource: UMediaSource *) -> bool
```

Check whether the specified media source can be played by this player.
	 
	  If a desired player name is set for this player, it will only check
	  whether that particular player type can play the specified source.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to check. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media source can be opened, false otherwise. |

### `CanPlayUrl`

```text
CanPlayUrl(Url: FString &) -> bool
```

Check whether the specified URL can be played by this player.
	 
	  If a desired player name is set for this player, it will only check
	  whether that particular player type can play the specified URL.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Url` | `FString &` | The URL to check. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `Close`

```text
Close() -> void
```

Close the currently open media, if any.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAudioTrackChannels`

```text
GetAudioTrackChannels(TrackIndex: int32, FormatIndex: int32) -> int32
```

Get the number of channels in the specified audio track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | Index of the audio track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of channels. |

### `GetAudioTrackSampleRate`

```text
GetAudioTrackSampleRate(TrackIndex: int32, FormatIndex: int32) -> int32
```

Get the sample rate of the specified audio track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | Index of the audio track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Samples per second. |

### `GetAudioTrackType`

```text
GetAudioTrackType(TrackIndex: int32, FormatIndex: int32) -> FString
```

Get the type of the specified audio track format.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FString` | Audio format type string. |

### `GetDesiredPlayerName`

```text
GetDesiredPlayerName() -> FName
```

Get the name of the current desired native player.

**Returns**

| Type | Description |
|---|---|
| `FName` | The name of the desired player, or NAME_None if not set. |

### `GetDuration`

```text
GetDuration() -> FTimespan
```

Get the media's duration.

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | A time span representing the duration. |

### `GetHorizontalFieldOfView`

```text
GetHorizontalFieldOfView() -> float
```

Get the current horizontal field of view (only for 360 videos).

**Returns**

| Type | Description |
|---|---|
| `float` | Horizontal field of view (in Euler degrees). |

### `GetMediaName`

```text
GetMediaName() -> FText
```

Get the human readable name of the currently loaded media source.

**Returns**

| Type | Description |
|---|---|
| `FText` | Media source name, or empty text if no media is opened |

### `GetNumTracks`

```text
GetNumTracks(TrackType: EMediaPlayerTrack) -> int32
```

Get the number of tracks of the given type.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of media tracks. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of tracks. |

### `GetNumTrackFormats`

```text
GetNumTrackFormats(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> int32
```

Get the number of formats of the specified track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of media tracks. |
| `TrackIndex` | `int32` | The index of the track. |

**Returns**

| Type | Description |
|---|---|
| `int32` | Number of formats. |

### `GetPlayerName`

```text
GetPlayerName() -> FName
```

Get the name of the current native media player.

**Returns**

| Type | Description |
|---|---|
| `FName` | Player name, or NAME_None if not available. |

### `GetPlaylist`

```text
GetPlaylist() -> UMediaPlaylist *
```

Get the current play list.
	 
	  Media players always have a valid play list. In C++ code you can use
	  the GetPlaylistRef to get a reference instead of a pointer to it.

**Returns**

| Type | Description |
|---|---|
| `UMediaPlaylist *` | The play list. |

### `GetPlaylistIndex`

```text
GetPlaylistIndex() -> int32
```

Get the current play list index.

**Returns**

| Type | Description |
|---|---|
| `int32` | Play list index. |

### `GetRate`

```text
GetRate() -> float
```

Get the media's current playback rate.

**Returns**

| Type | Description |
|---|---|
| `float` | The playback rate. |

### `GetSelectedTrack`

```text
GetSelectedTrack(TrackType: EMediaPlayerTrack) -> int32
```

Get the index of the currently selected track of the given type.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track to get. |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the selected track, or INDEX_NONE if no track is active. |

### `GetSupportedRates`

```text
GetSupportedRates(OutRates: TArray < FFloatRange > &, Unthinned: bool) -> void
```

Get the supported playback rates.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OutRates` | `TArray < FFloatRange > &` | - |
| `Unthinned` | `bool` | Whether the rates are for unthinned playback. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTime`

```text
GetTime() -> FTimespan
```

Get the media's current playback time.

**Returns**

| Type | Description |
|---|---|
| `FTimespan` | Playback time. |

### `GetTrackDisplayName`

```text
GetTrackDisplayName(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> FText
```

Get the human readable name of the specified track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track. |
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FText` | Display name. |

### `GetTrackFormat`

```text
GetTrackFormat(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> int32
```

Get the index of the active format of the specified track type.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track. |
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `int32` | The index of the selected format. |

### `GetTrackLanguage`

```text
GetTrackLanguage(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> FString
```

Get the language tag of the specified track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track. |
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FString` | Language tag, i.e. "en-US" for English, or "und" for undefined. |

### `GetUrl`

```text
GetUrl() -> const FString &
```

Get the URL of the currently loaded media, if any.

**Returns**

| Type | Description |
|---|---|
| `const FString &` | Media URL, or empty string if no media was loaded. |

### `GetVerticalFieldOfView`

```text
GetVerticalFieldOfView() -> float
```

Get the current vertical field of view (only for 360 videos).

**Returns**

| Type | Description |
|---|---|
| `float` | Vertical field of view (in Euler degrees), or 0.0 if not available. |

### `GetVideoTrackAspectRatio`

```text
GetVideoTrackAspectRatio(TrackIndex: int32, FormatIndex: int32) -> float
```

Get the aspect ratio of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | Index of the video track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `float` | Aspect ratio. |

### `GetVideoTrackDimensions`

```text
GetVideoTrackDimensions(TrackIndex: int32, FormatIndex: int32) -> FIntPoint
```

Get the current dimensions of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | Video dimensions (in pixels). |

### `GetVideoTrackFrameRate`

```text
GetVideoTrackFrameRate(TrackIndex: int32, FormatIndex: int32) -> float
```

Get the frame rate of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `float` | Frame rate (in frames per second). |

### `GetVideoTrackFrameRates`

```text
GetVideoTrackFrameRates(TrackIndex: int32, FormatIndex: int32) -> FFloatRange
```

Get the supported range of frame rates of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FFloatRange` | Frame rate range (in frames per second). |

### `GetVideoTrackType`

```text
GetVideoTrackType(TrackIndex: int32, FormatIndex: int32) -> FString
```

Get the type of the specified video track format.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |

**Returns**

| Type | Description |
|---|---|
| `FString` | Video format type string. |

### `GetViewRotation`

```text
GetViewRotation() -> FRotator
```

Get the current view rotation (only for 360 videos).

**Returns**

| Type | Description |
|---|---|
| `FRotator` | View rotation, or zero rotator if not available. |

### `HasError`

```text
HasError() -> bool
```

Check whether the player is in an error state.
	 
	  When the player is in an error state, no further operations are possible.
	  The current media must be closed, and a new media source must be opened
	  before the player can be used again. Errors are usually caused by faulty
	  media files or interrupted network connections.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsBuffering`

```text
IsBuffering() -> bool
```

Check whether playback is buffering data.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if looping, false otherwise. |

### `IsConnecting`

```text
IsConnecting() -> bool
```

Check whether the player is currently connecting to a media source.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if connecting, false otherwise. |

### `IsLooping`

```text
IsLooping() -> bool
```

Check whether playback is looping.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if looping, false otherwise. |

### `IsPaused`

```text
IsPaused() -> bool
```

Check whether playback is currently paused.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is paused, false otherwise. |

### `IsPlaying`

```text
IsPlaying() -> bool
```

Check whether playback has started.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback has started, false otherwise. |

### `IsPreparing`

```text
IsPreparing() -> bool
```

Check whether the media is currently opening or buffering.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is being prepared, false otherwise. |

### `IsReady`

```text
IsReady() -> bool
```

Check whether media is ready for playback.
	 
	  A player is ready for playback if it has a media source opened that
	  finished preparing and is not in an error state.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if media is ready, false otherwise. |

### `Next`

```text
Next() -> bool
```

Open the next item in the current play list.
	 
	  The player will start playing the new media source if it was playing
	  something previously, otherwise it will only open the media source.

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `OpenFile`

```text
OpenFile(FilePath: FString &) -> bool
```

Opens the specified media file path.
	 
	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FilePath` | `FString &` | The file path to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the file path will be opened, false otherwise. |

### `OpenPlaylist`

```text
OpenPlaylist(InPlaylist: UMediaPlaylist *) -> bool
```

Open the first media source in the specified play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlaylist` | `UMediaPlaylist *` | The play list to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the source will be opened, false otherwise. |

### `OpenPlaylistIndex`

```text
OpenPlaylistIndex(InPlaylist: UMediaPlaylist *, Index: int32) -> bool
```

Open a particular media source in the specified play list.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlaylist` | `UMediaPlaylist *` | The play list to open. |
| `Index` | `int32` | The index of the source to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the source will be opened, false otherwise. |

### `OpenSource`

```text
OpenSource(MediaSource: UMediaSource *) -> bool
```

Open the specified media source.
	 
	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `MediaSource` | `UMediaSource *` | The media source to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the source will be opened, false otherwise. |

### `OpenUrl`

```text
OpenUrl(Url: FString &) -> bool
```

Opens the specified media URL.
	 
	  A return value of true indicates that the player will attempt to open
	  the media, but it may fail to do so later for other reasons, i.e. if
	  a connection to the media server timed out. Use the OnMediaOpened and
	  OnMediaOpenFailed delegates to detect if and when the media is ready!

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Url` | `FString &` | The URL to open. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the URL will be opened, false otherwise. |

### `Pause`

```text
Pause() -> bool
```

Pauses media playback.
	 
	  This is the same as setting the playback rate to 0.0.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is being paused, false otherwise. |

### `Play`

```text
Play() -> bool
```

Starts media playback.
	 
	  This is the same as setting the playback rate to 1.0.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if playback is starting, false otherwise. |

### `Previous`

```text
Previous() -> bool
```

Open the previous item in the current play list.
	 
	  The player will start playing the new media source if it was playing
	  something previously, otherwise it will only open the media source.

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `Reopen`

```text
Reopen() -> bool
```

Reopens the currently opened media or play list.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the media will be opened, false otherwise. |

### `Rewind`

```text
Rewind() -> bool
```

Rewinds the media to the beginning.
	 
	  This is the same as seeking to zero time.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if rewinding, false otherwise. |

### `Seek`

```text
Seek(Time: FTimespan &) -> bool
```

Seeks to the specified playback time.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Time` | `FTimespan &` | The playback time to set. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SelectTrack`

```text
SelectTrack(TrackType: EMediaPlayerTrack, TrackIndex: int32) -> bool
```

Select the active track of the given type.
	 
	  The selected track will use its currently active format. Active formats will
	  be remembered on a per track basis. The first available format is active by
	  default. To switch the track format, use SetTrackFormat instead.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track to select. |
| `TrackIndex` | `int32` | The index of the track to select, or INDEX_NONE to deselect. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the track was selected, false otherwise. |

### `SetDesiredPlayerName`

```text
SetDesiredPlayerName(PlayerName: FName) -> void
```

Set the name of the desired native player.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PlayerName` | `FName` | The name of the player to set. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetLooping`

```text
SetLooping(Looping: bool) -> bool
```

Enables or disables playback looping.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Looping` | `bool` | Whether playback should be looped. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetRate`

```text
SetRate(Rate: float) -> bool
```

Changes the media's playback rate.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | The playback rate to set. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetNativeVolume`

```text
SetNativeVolume(Volume: float) -> bool
```

Set the volume on the native player if not mixing with Sound Wave asset.
	 
	  The SetNativeVolume can be used to change the audio output volume at runtime. Note that
	  not all media player plug-ins may support native audio output on all platforms.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Volume` | `float` | The volume to set. |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetTrackFormat`

```text
SetTrackFormat(TrackType: EMediaPlayerTrack, TrackIndex: int32, FormatIndex: int32) -> bool
```

Set the format on the specified track.
	 
	  Selecting the format will not switch to the specified track. To switch
	  tracks, use SelectTrack instead. If the track is already selected, the
	  format change will be applied immediately.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackType` | `EMediaPlayerTrack` | The type of track to update. |
| `TrackIndex` | `int32` | The index of the track to update. |
| `FormatIndex` | `int32` | The index of the format to select (must be valid). |

**Returns**

| Type | Description |
|---|---|
| `bool` | true if the track was selected, false otherwise. |

### `SetVideoTrackFrameRate`

```text
SetVideoTrackFrameRate(TrackIndex: int32, FormatIndex: int32, FrameRate: float) -> bool
```

Set the frame rate of the specified video track.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `TrackIndex` | `int32` | The index of the track, or INDEX_NONE for the selected one. |
| `FormatIndex` | `int32` | Index of the track format, or INDEX_NONE for the selected one. |
| `FrameRate` | `float` | The frame rate to set (must be in range of format's supported frame rates). |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetViewField`

```text
SetViewField(Horizontal: float, Vertical: float, Absolute: bool) -> bool
```

Set the field of view (only for 360 videos).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Horizontal` | `float` | Horizontal field of view (in Euler degrees). |
| `Vertical` | `float` | Vertical field of view (in Euler degrees). |
| `Absolute` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SetViewRotation`

```text
SetViewRotation(Rotation: FRotator &, Absolute: bool) -> bool
```

Set the view's rotation (only for 360 videos).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rotation` | `FRotator &` | The desired view rotation. |
| `Absolute` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | true on success, false otherwise. |

### `SupportsRate`

```text
SupportsRate(Rate: float, Unthinned: bool) -> bool
```

Check whether the specified playback rate is supported.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Rate` | `float` | The playback rate to check. |
| `Unthinned` | `bool` | Whether no frames should be dropped at the given rate. |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SupportsScrubbing`

```text
SupportsScrubbing() -> bool
```

Check whether the currently loaded media supports scrubbing.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if scrubbing is supported, false otherwise. |

### `SupportsSeeking`

```text
SupportsSeeking() -> bool
```

Check whether the currently loaded media can jump to a certain position.

**Returns**

| Type | Description |
|---|---|
| `bool` | true if seeking is supported, false otherwise. |

### `SetAudioDeviceGUID`

```text
SetAudioDeviceGUID(DeviceGUID: FString &) -> void
```

Sets the audio device for the media player; currently only effective on PC platforms.
	  add by watsonxie

**Parameters**

| Name | Type | Description |
|---|---|---|
| `DeviceGUID` | `FString &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnEndReached`

```text
OnEndReached() -> void
```

A delegate that is invoked when playback has reached the end of the media.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaClosed`

```text
OnMediaClosed() -> void
```

A delegate that is invoked when a media source has been closed.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaOpened`

```text
OnMediaOpened(OpenedUrl: FString) -> void
```

A delegate that is invoked when a media source has been opened.
	 
	  Depending on whether the underlying player implementation opens the media
	  synchronously or asynchronously, this event may be executed before or
	  after the call to OpenSource  OpenUrl returns.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `OpenedUrl` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaOpenFailed`

```text
OnMediaOpenFailed(FailedUrl: FString) -> void
```

A delegate that is invoked when a media source has failed to open.
	 
	  This delegate is only executed if OpenSource  OpenUrl returned true and
	  the media failed to open asynchronously later. It is not executed if
	  OpenSource  OpenUrl returned false, indicating an immediate failure.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FailedUrl` | `FString` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlaybackResumed`

```text
OnPlaybackResumed() -> void
```

A delegate that is invoked when media playback has been resumed.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnPlaybackSuspended`

```text
OnPlaybackSuspended() -> void
```

A delegate that is invoked when media playback has been suspended.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnSeekCompleted`

```text
OnSeekCompleted() -> void
```

A delegate that is invoked when a seek operation completed successfully.
	 
	  Depending on whether the underlying player implementation performs seeks
	  synchronously or asynchronously, this event may be executed before or
	  after the call to Seek returns.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnTracksChanged`

```text
OnTracksChanged() -> void
```

A delegate that is invoked when the media track collection changed.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnMediaPlayFirstFrame`

```text
OnMediaPlayFirstFrame() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
