---
id: "api:cppstruct:FAnimNode_RandomPlayer"
title: "FAnimNode_RandomPlayer"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAnimNode_RandomPlayer.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAnimNode_RandomPlayer

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bShuffleMode` | `bool` | When shuffle mode is active we will never loop a sequence beyond MaxLoopCount<br>	   without visiting each sequence in turn (no repeats). Enabling this will ignore<br>	   ChanceToPlay for each entry |
| `Entries` | `TArray < FRandomPlayerSequenceEntry >` | List of sequences to randomly step through |
