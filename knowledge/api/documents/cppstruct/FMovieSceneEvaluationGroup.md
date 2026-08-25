---
id: "api:cppstruct:FMovieSceneEvaluationGroup"
title: "FMovieSceneEvaluationGroup"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationGroup.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneEvaluationGroup

Holds segment pointers for all segments that are active for a given range of the sequence

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LUTIndices` | `TArray < FMovieSceneEvaluationGroupLUTIndex >` | Array of indices that define all the flush groups in the range. |
| `SegmentPtrLUT` | `TArray < FMovieSceneEvaluationFieldSegmentPtr >` | A grouping of evaluation pointers that occur in this range of the sequence |
