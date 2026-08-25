---
id: "api:class:UMovieSceneSubSection"
title: "UMovieSceneSubSection"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneSubSection.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneSubSection

Implements a section in sub-sequence tracks.

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Parameters` | `FMovieSceneSectionParameters` | - |
| `StartOffset_DEPRECATED` | `float` | - |
| `TimeScale_DEPRECATED` | `float` | - |
| `PrerollTime_DEPRECATED` | `float` | - |
| `SubSequence` | `UMovieSceneSequence *` | Movie scene being played by this section.<br>	 <br>	  @todo Sequencer: Should this be lazy loaded? |
| `ActorToRecord` | `TLazyObjectPtr < AActor >` | Target actor to record |
| `TargetSequenceName` | `FString` | Target name of sequence to try to record to (will record automatically to another if this already exists) |
| `TargetPathToRecordTo` | `FDirectoryPath` | Target path of sequence to record to |

## Language

`cpp`
