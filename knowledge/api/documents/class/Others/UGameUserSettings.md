---
id: "api:class:UGameUserSettings"
title: "UGameUserSettings"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameUserSettings.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameUserSettings

Stores user settings for a game (for example graphics and sound settings), with the ability to save and load to and from a file.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bUseVSync` | `bool` | Whether to use VSync or not. (public to allow UI to connect to it) |
| `ResolutionSizeX` | `uint32` | Game screen resolution width, in pixels. |
| `ResolutionSizeY` | `uint32` | Game screen resolution height, in pixels. |
| `LastUserConfirmedResolutionSizeX` | `uint32` | Game screen resolution width, in pixels. |
| `LastUserConfirmedResolutionSizeY` | `uint32` | Game screen resolution height, in pixels. |
| `IsBorderless` | `bool` | Is game window borderless added by windzjliu |
| `BorderlessMode` | `int32` | - |
| `WindowPosX` | `int32` | Window PosX |
| `WindowPosY` | `int32` | Window PosY |
| `FullscreenMode` | `int32` | Game window fullscreen mode<br>	 	0 = Fullscreen<br>	 	1 = Windowed fullscreen<br>	 	2 = Windowed |
| `LastConfirmedFullscreenMode` | `int32` | Last user confirmed fullscreen mode setting. |
| `PreferredFullscreenMode` | `int32` | Fullscreen mode to use when toggling between windowed and fullscreen. Same values as r.FullScreenMode. |
| `Version` | `uint32` | All settings will be wiped and set to default if the serialized version differs from UE_GAMEUSERSETTINGS_VERSION. |
| `AudioQualityLevel` | `int32` | - |
| `FrameRateLimit` | `float` | Frame rate cap |
| `DesiredScreenWidth` | `int32` | Desired screen width used to calculate the resolution scale when user changes display mode |
| `bUseDesiredScreenHeight` | `bool` | If true, the desired screen height will be used to scale the render resolution automatically. |
| `DesiredScreenHeight` | `int32` | Desired screen height used to calculate the resolution scale when user changes display mode |
| `LastRecommendedScreenWidth` | `float` | Result of the last benchmark; calculated resolution to use. |
| `LastRecommendedScreenHeight` | `float` | Result of the last benchmark; calculated resolution to use. |
| `LastCPUBenchmarkResult` | `float` | Result of the last benchmark (CPU); -1 if there has not been a benchmark run |
| `LastGPUBenchmarkResult` | `float` | Result of the last benchmark (GPU); -1 if there has not been a benchmark run |
| `LastCPUBenchmarkSteps` | `TArray < float >` | Result of each individual sub-section of the last CPU benchmark; empty if there has not been a benchmark run |
| `LastGPUBenchmarkSteps` | `TArray < float >` | Result of each individual sub-section of the last GPU benchmark; empty if there has not been a benchmark run |
| `LastGPUBenchmarkMultiplier` | `float` | Multiplier used against the last GPU benchmark |
| `bUseHDRDisplayOutput` | `bool` | HDR |
| `HDRDisplayOutputNits` | `int32` | HDR |

## Functions

### `ApplySettings`

```text
ApplySettings(bCheckForCommandLineOverrides: bool) -> void
```

Applies all current user settings to the game and saves to permanent storage (e.g. file), optionally checking for command line overrides.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bCheckForCommandLineOverrides` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyNonResolutionSettings`

```text
ApplyNonResolutionSettings() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyResolutionSettings`

```text
ApplyResolutionSettings(bCheckForCommandLineOverrides: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bCheckForCommandLineOverrides` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetScreenResolution`

```text
GetScreenResolution() -> FIntPoint
```

Returns the user setting for game screen resolution, in pixels.

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | - |

### `GetLastConfirmedScreenResolution`

```text
GetLastConfirmedScreenResolution() -> FIntPoint
```

Returns the last confirmed user setting for game screen resolution, in pixels.

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | - |

### `GetDesktopResolution`

```text
GetDesktopResolution() -> FIntPoint
```

Returns user's desktop resolution, in pixels.

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | - |

### `SetScreenResolution`

```text
SetScreenResolution(Resolution: FIntPoint) -> void
```

Sets the user setting for game screen resolution, in pixels.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Resolution` | `FIntPoint` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetIsBorderless`

```text
GetIsBorderless() -> bool
```

IsBorderless getter and setter added by windzjliu

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIsBorderless`

```text
SetIsBorderless(InIsBorderless: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InIsBorderless` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetBorderlessMode`

```text
GetBorderlessMode() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetBorderlessMode`

```text
SetBorderlessMode(InBorderlessMode: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBorderlessMode` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFullscreenMode`

```text
GetFullscreenMode() -> EWindowMode :: Type
```

Returns the user setting for game window fullscreen mode.

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | - |

### `GetLastConfirmedFullscreenMode`

```text
GetLastConfirmedFullscreenMode() -> EWindowMode :: Type
```

Returns the last confirmed user setting for game window fullscreen mode.

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | - |

### `SetFullscreenMode`

```text
SetFullscreenMode(InFullscreenMode: EWindowMode :: Type) -> void
```

Sets the user setting for the game window fullscreen mode. See UGameUserSettings::FullscreenMode.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InFullscreenMode` | `EWindowMode :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPreferredFullscreenMode`

```text
GetPreferredFullscreenMode() -> EWindowMode :: Type
```

Returns the user setting for game window fullscreen mode.

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | - |

### `SetVSyncEnabled`

```text
SetVSyncEnabled(bEnable: bool) -> void
```

Sets the user setting for vsync. See UGameUserSettings::bUseVSync.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `IsVSyncEnabled`

```text
IsVSyncEnabled() -> bool
```

Returns the user setting for vsync.

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsScreenResolutionDirty`

```text
IsScreenResolutionDirty() -> bool
```

Checks if the Screen Resolution user setting is different from current

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsFullscreenModeDirty`

```text
IsFullscreenModeDirty() -> bool
```

Checks if the FullscreenMode user setting is different from current

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `IsVSyncDirty`

```text
IsVSyncDirty() -> bool
```

Checks if the vsync user setting is different from current system setting

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ConfirmVideoMode`

```text
ConfirmVideoMode() -> void
```

Mark current video mode settings (fullscreenmoderesolution) as being confirmed by the user

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertVideoMode`

```text
RevertVideoMode() -> void
```

Revert video mode (fullscreenmoderesolution) back to the last user confirmed values

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBenchmarkFallbackValues`

```text
SetBenchmarkFallbackValues() -> void
```

Set scalability settings to sensible fallback values, for use when the benchmark fails or potentially causes a crash

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAudioQualityLevel`

```text
SetAudioQualityLevel(QualityLevel: int32) -> void
```

Sets the user's audio quality level setting

**Parameters**

| Name | Type | Description |
|---|---|---|
| `QualityLevel` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAudioQualityLevel`

```text
GetAudioQualityLevel() -> int32
```

Returns the user's audio quality level setting

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetFrameRateLimit`

```text
SetFrameRateLimit(NewLimit: float) -> void
```

Sets the user's frame rate limit (0 will disable frame rate limiting)

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewLimit` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFrameRateLimit`

```text
GetFrameRateLimit() -> float
```

Gets the user's frame rate limit (0 indiciates the frame rate limit is disabled)

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `SetOverallScalabilityLevel`

```text
SetOverallScalabilityLevel(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOverallScalabilityLevel`

```text
GetOverallScalabilityLevel() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `GetResolutionScaleInformation`

```text
GetResolutionScaleInformation(CurrentScaleNormalized: float &, CurrentScaleValue: int32 &, MinScaleValue: int32 &, MaxScaleValue: int32 &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentScaleNormalized` | `float &` | - |
| `CurrentScaleValue` | `int32 &` | - |
| `MinScaleValue` | `int32 &` | - |
| `MaxScaleValue` | `int32 &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetResolutionScaleInformationEx`

```text
GetResolutionScaleInformationEx(CurrentScaleNormalized: float &, CurrentScaleValue: float &, MinScaleValue: float &, MaxScaleValue: float &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CurrentScaleNormalized` | `float &` | - |
| `CurrentScaleValue` | `float &` | - |
| `MinScaleValue` | `float &` | - |
| `MaxScaleValue` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResolutionScaleValue`

```text
SetResolutionScaleValue(NewScaleValue: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScaleValue` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResolutionScaleValueEx`

```text
SetResolutionScaleValueEx(NewScaleValue: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScaleValue` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetResolutionScaleNormalized`

```text
SetResolutionScaleNormalized(NewScaleNormalized: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewScaleNormalized` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetViewDistanceQuality`

```text
SetViewDistanceQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetViewDistanceQuality`

```text
GetViewDistanceQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetShadowQuality`

```text
SetShadowQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetShadowQuality`

```text
GetShadowQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetAntiAliasingQuality`

```text
SetAntiAliasingQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAntiAliasingQuality`

```text
GetAntiAliasingQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetTextureQuality`

```text
SetTextureQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetTextureQuality`

```text
GetTextureQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetVisualEffectQuality`

```text
SetVisualEffectQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetVisualEffectQuality`

```text
GetVisualEffectQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetPostProcessingQuality`

```text
SetPostProcessingQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPostProcessingQuality`

```text
GetPostProcessingQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetFoliageQuality`

```text
SetFoliageQuality(Value: int32) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Value` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetFoliageQuality`

```text
GetFoliageQuality() -> int32
```

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsDirty`

```text
IsDirty() -> bool
```

Checks if any user settings is different from current

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `ValidateSettings`

```text
ValidateSettings() -> void
```

Validates and resets bad user settings to default. Deletes stale user settings file if necessary.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `LoadSettings`

```text
LoadSettings(bForceReload: bool) -> void
```

Loads the user settings from persistent storage

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bForceReload` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SaveSettings`

```text
SaveSettings() -> void
```

Save the user settings to persistent storage (automatically happens as part of ApplySettings)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetToCurrentSettings`

```text
ResetToCurrentSettings() -> void
```

This function resets all settings to the current system settings

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetToDefaults`

```text
SetToDefaults() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetDefaultResolutionScale`

```text
GetDefaultResolutionScale() -> float
```

Gets the desired resolution quality based on DesiredScreenWidthHeight and the current screen resolution

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetRecommendedResolutionScale`

```text
GetRecommendedResolutionScale() -> float
```

Gets the recommended resolution quality based on LastRecommendedScreenWidthHeight and the current screen resolution

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `GetDefaultResolution`

```text
GetDefaultResolution() -> FIntPoint
```

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | The default resolution when no resolution is set |

### `GetDefaultWindowPosition`

```text
GetDefaultWindowPosition() -> FIntPoint
```

**Returns**

| Type | Description |
|---|---|
| `FIntPoint` | The default window position when no position is set |

### `GetDefaultWindowMode`

```text
GetDefaultWindowMode() -> EWindowMode :: Type
```

**Returns**

| Type | Description |
|---|---|
| `EWindowMode :: Type` | The default window mode when no mode is set |

### `GetGameUserSettings`

```text
GetGameUserSettings() -> UGameUserSettings *
```

Returns the game local machine settings (resolution, windowing mode, scalability settings, etc...)

**Returns**

| Type | Description |
|---|---|
| `UGameUserSettings *` | - |

### `RunHardwareBenchmark`

```text
RunHardwareBenchmark(WorkScale: int32, CPUMultiplier: float, GPUMultiplier: float) -> void
```

Runs the hardware benchmark and populates ScalabilityQuality as well as the last benchmark results config members, but does not apply the settings it determines. Designed to be called in conjunction with ApplyHardwareBenchmarkResults

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorkScale` | `int32` | - |
| `CPUMultiplier` | `float` | - |
| `GPUMultiplier` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ApplyHardwareBenchmarkResults`

```text
ApplyHardwareBenchmarkResults() -> void
```

Applies the settings stored in ScalabilityQuality and saves settings

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SupportsHDRDisplayOutput`

```text
SupportsHDRDisplayOutput() -> bool
```

Whether the curently running system supports HDR display output

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `EnableHDRDisplayOutput`

```text
EnableHDRDisplayOutput(bEnable: bool, DisplayNits: int32) -> void
```

Enables or disables HDR display output. Can be called again to change the desired nit level

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |
| `DisplayNits` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetCurrentHDRDisplayNits`

```text
GetCurrentHDRDisplayNits() -> int32
```

Returns 0 if HDR isn't supported or is turned off

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `IsHDREnabled`

```text
IsHDREnabled() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

## Delegates

### `OnGameUserSettingsUINeedsUpdate`

```text
OnGameUserSettingsUINeedsUpdate() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
