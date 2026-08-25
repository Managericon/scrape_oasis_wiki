---
id: "api:class:UMovieSceneNewEventTrack"
title: "UMovieSceneNewEventTrack"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneNewEventTrack.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneNewEventTrack

Implements a movie scene track that triggers discrete events during playback.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `EventPosition` | `EFireEventsAtPosition` | Defines where in the evaluation to trigger events |
| `Sections` | `TArray < UMovieSceneSection * >` | The track's sections. |

## Language

`cpp`
