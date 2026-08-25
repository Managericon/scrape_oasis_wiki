---
id: "api:class:UMovieSceneAudioSection"
title: "UMovieSceneAudioSection"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneAudioSection.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneAudioSection

Audio section, for use in the master audio, or by attached audio objects

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Sound` | `USoundBase *` | The sound cue or wave that this section plays |
| `StartOffset` | `float` | The offset into the beginning of the audio clip |
| `AudioStartTime_DEPRECATED` | `float` | The absolute time that the sound starts playing at |
| `AudioDilationFactor_DEPRECATED` | `float` | The amount which this audio is time dilated by |
| `AudioVolume_DEPRECATED` | `float` | The volume the sound will be played with. |
| `SoundVolume` | `FRichCurve` | The volume the sound will be played with. |
| `PitchMultiplier` | `FRichCurve` | The pitch multiplier the sound will be played with. |
| `bSuppressSubtitles` | `bool` | - |
| `bOverrideAttenuation` | `bool` | Should the attenuation settings on this section be used. |
| `AttenuationSettings` | `USoundAttenuation *` | The attenuation settings to use. |
| `OnQueueSubtitles` | `FOnQueueSubtitles` | Called when subtitles are sent to the SubtitleManager.  Set this delegate if you want to hijack the subtitles for other purposes |
| `OnAudioFinished` | `FOnAudioFinished` | called when we finish playing audio, either because it played to completion or because a Stop() call turned it off early |
| `OnAudioPlaybackPercent` | `FOnAudioPlaybackPercent` | - |

## Language

`cpp`
