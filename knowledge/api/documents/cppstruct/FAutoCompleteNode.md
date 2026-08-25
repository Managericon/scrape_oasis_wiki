---
id: "api:cppstruct:FAutoCompleteNode"
title: "FAutoCompleteNode"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAutoCompleteNode.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAutoCompleteNode

Node for storing an auto-complete tree based on each char in the command.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `IndexChar` | `int32` | Char for node in the tree |
| `AutoCompleteListIndices` | `TArray < int32 >` | Indices into AutoCompleteList for commands that match to this level |
