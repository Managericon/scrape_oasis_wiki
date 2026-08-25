---
id: "api:class:UMoviePlayerSettings"
title: "UMoviePlayerSettings"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMoviePlayerSettings.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMoviePlayerSettings

Implements the settings for the Windows target platform.

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bWaitForMoviesToComplete` | `bool` | If enabled, The game waits for startup movies to complete even if loading has finished. |
| `bMoviesAreSkippable` | `TArray < FString >` | If enabled, Startup movies can be skipped by the user when a mouse button is pressed. |
| `StartupMovies` | `TArray < FString >` | Movies to play on startup. Note that these must be in your game's GameContentMovies directory. |

## Language

`cpp`
