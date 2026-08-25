---
id: "api:cppstruct:FMovieSceneEvaluationKey"
title: "FMovieSceneEvaluationKey"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationKey.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneEvaluationKey

Keyable struct that represents a particular entity within an evaluation template (either a sectiontemplate or a track)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SequenceID` | `FMovieSceneSequenceID` | ID of the sequence that the entity is contained within |
| `TrackIdentifier` | `FMovieSceneTrackIdentifier` | ID of the track this key relates to |
| `SectionIdentifier` | `uint32` | ID of the section this key relates to (or -1 where this key relates to a track) |
