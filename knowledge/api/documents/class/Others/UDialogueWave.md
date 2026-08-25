---
id: "api:class:UDialogueWave"
title: "UDialogueWave"
source: "https://developer.gp.qq.com/api/class/detail/Others/UDialogueWave.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UDialogueWave

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bMature` | `uint32` | true if this dialogue is considered to contain matureadult content. |
| `bOverride_SubtitleOverride` | `uint32` | - |
| `SpokenText` | `FString` | A localized version of the text that is actually spoken phonetically in the audio. |
| `SubtitleOverride` | `FString` | A localized version of the subtitle text that should be displayed for this audio. By default this will be the same as the Spoken Text. |
| `ContextMappings` | `TArray < FDialogueContextMapping >` | Mappings between dialogue contexts and associated soundwaves. |
| `LocalizationGUID` | `FGuid` | - |
| `VoiceActorDirection` | `FString` | Provides general notes to the voice actor intended to direct their performance, as well as contextual information to the translator. |

## Language

`cpp`
