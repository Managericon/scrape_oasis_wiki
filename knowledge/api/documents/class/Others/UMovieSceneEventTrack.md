---
id: "api:class:UMovieSceneEventTrack"
title: "UMovieSceneEventTrack"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneEventTrack.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneEventTrack

Implements a movie scene track that triggers discrete events during playback.

## Inheritance

`UMovieSceneNameableTrack`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bFireEventsWhenForwards` | `uint32` | If events should be fired when passed playing the sequence forwards. |
| `bFireEventsWhenBackwards` | `uint32` | If events should be fired when passed playing the sequence backwards. |
| `EventPosition` | `EFireEventsAtPosition` | Defines where in the evaluation to trigger events |
| `EventReceivers` | `TArray < FMovieSceneObjectBindingID >` | Defines a list of object bindings on which to trigger the events in this track. When empty, events will trigger in the default event contexts for the playback environment (such as the level blueprint, or widget). |
| `Sections` | `TArray < UMovieSceneSection * >` | The track's sections. |

## Language

`cpp`
