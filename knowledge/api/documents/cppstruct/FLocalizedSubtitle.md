---
id: "api:cppstruct:FLocalizedSubtitle"
title: "FLocalizedSubtitle"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FLocalizedSubtitle.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FLocalizedSubtitle

A subtitle localized to a specific language.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bMature` | `uint32` | true if this sound is considered to contain mature content. |
| `LanguageExt` | `FString` | The 3-letter language for this subtitle |
| `Subtitles` | `TArray < FSubtitleCue >` | Subtitle cues.  If empty, use SoundNodeWave's SpokenText as the subtitle.  Will often be empty,<br>	  as the contents of the subtitle is commonly identical to what is spoken. |
| `bManualWordWrap` | `uint32` | true if the subtitles have been split manually. |
| `bSingleLine` | `uint32` | true if the subtitles should be displayed one line at a time. |
