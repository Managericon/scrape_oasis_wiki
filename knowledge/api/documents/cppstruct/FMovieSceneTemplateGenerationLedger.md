---
id: "api:cppstruct:FMovieSceneTemplateGenerationLedger"
title: "FMovieSceneTemplateGenerationLedger"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneTemplateGenerationLedger.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneTemplateGenerationLedger

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LastTrackIdentifier` | `FMovieSceneTrackIdentifier` | - |
| `TrackReferenceCounts` | `TMap < FMovieSceneTrackIdentifier , int32 >` | Map of track identifiers to number of references within th template (generally 1, maybe >1 for shared tracks) |
| `TrackSignatureToTrackIdentifier` | `TMap < FGuid , FMovieSceneTrackIdentifiers >` | Map of track signature to array of track identifiers that it created |
