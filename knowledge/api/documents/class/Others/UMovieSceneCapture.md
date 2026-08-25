---
id: "api:class:UMovieSceneCapture"
title: "UMovieSceneCapture"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneCapture.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneCapture

Class responsible for capturing scene data

## Inheritance

`UObject` -> `IMovieSceneCaptureInterface` -> `ICaptureProtocolHost`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CaptureType` | `FCaptureProtocolID` | The type of capture protocol to use |
| `ProtocolSettings` | `UMovieSceneCaptureProtocolSettings *` | Settings specific to the capture protocol |
| `Settings` | `FMovieSceneCaptureSettings` | Settings that define how to capture |
| `bUseSeparateProcess` | `bool` | Whether to capture the movie in a separate process or not |
| `bCloseEditorWhenCaptureStarts` | `bool` | When enabled, the editor will shutdown when the capture starts |
| `AdditionalCommandLineArguments` | `FString` | Additional command line arguments to pass to the external process when capturing |
| `InheritedCommandLineArguments` | `FString` | Command line arguments inherited from this process |

## Language

`cpp`
