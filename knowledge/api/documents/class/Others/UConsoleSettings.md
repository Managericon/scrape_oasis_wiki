---
id: "api:class:UConsoleSettings"
title: "UConsoleSettings"
source: "https://developer.gp.qq.com/api/class/detail/Others/UConsoleSettings.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UConsoleSettings

Implements the settings for the UConsole class.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MaxScrollbackSize` | `int32` | Visible Console stuff |
| `ManualAutoCompleteList` | `TArray < struct FAutoCompleteCommand >` | Manual list of auto-complete commands and info specified in BaseInput.ini |
| `AutoCompleteMapPaths` | `TArray < FString >` | List of relative paths (e.g. ContentMaps) to search for map names for auto-complete usage. Specified in BaseInput.ini. |
| `BackgroundOpacityPercentage` | `float` | Amount of transparency of the console background. |
| `bOrderTopToBottom` | `bool` | Whether we legacy bottom-to-top ordering or regular top-to-bottom ordering |
| `InputColor` | `FColor` | The color used for text input. |
| `HistoryColor` | `FColor` | The color used for the previously typed commands history. |
| `AutoCompleteCommandColor` | `FColor` | The autocomplete color used for executable commands. |
| `AutoCompleteCVarColor` | `FColor` | The autocomplete color used for mutable CVars. |
| `AutoCompleteFadedColor` | `FColor` | The autocomplete color used for command descriptions and read-only CVars. |

## Language

`cpp`
