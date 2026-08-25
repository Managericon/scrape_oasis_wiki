---
id: "api:cppstruct:FMovieSceneSequenceHierarchy"
title: "FMovieSceneSequenceHierarchy"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceHierarchy.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneSequenceHierarchy

Structure that stores hierarchical information pertaining to all sequences contained within a master sequence

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SubSequences` | `TMap < uint32 , FMovieSceneSubSequenceData >` | Map of all (recursive) sub sequences found in this template, keyed on sequence ID |
| `Hierarchy` | `TMap < uint32 , FMovieSceneSequenceHierarchyNode >` | Structural information describing the structure of the sequence |
