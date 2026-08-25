---
id: "api:cppstruct:FMovieSceneSequenceHierarchyNode"
title: "FMovieSceneSequenceHierarchyNode"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMovieSceneSequenceHierarchyNode.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMovieSceneSequenceHierarchyNode

Simple structure specifying parent and child sequence IDs for any given sequences

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParentID` | `FMovieSceneSequenceID` | Movie scene sequence ID of this node's parent sequence |
| `Children` | `TArray < FMovieSceneSequenceID >` | Array of child sequences contained within this sequence |
