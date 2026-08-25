---
id: "api:cppstruct:FMovieSceneEvaluationGroupLUTIndex"
title: "FMovieSceneEvaluationGroupLUTIndex"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneEvaluationGroupLUTIndex.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneEvaluationGroupLUTIndex

Lookup table index for a group of evaluation templates

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LUTOffset` | `int32` | The offset within FMovieSceneEvaluationGroup::SegmentPtrLUT that this index starts |
| `NumInitPtrs` | `int32` | The number of initialization pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset. |
| `NumEvalPtrs` | `int32` | The number of evaluation pointers are stored after &FMovieSceneEvaluationGroup::SegmentPtrLUT[0] + LUTOffset + NumInitPtrs. |
