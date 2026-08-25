---
id: "api:cppstruct:FNetViewer"
title: "FNetViewer"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FNetViewer.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FNetViewer

stores information on a viewer that actors need to be checked against for relevancy

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Connection` | `UNetConnection *` | - |
| `InViewer` | `AActor *` | The "controlling net object" associated with this view (typically player controller) |
| `ViewTarget` | `AActor *` | The actor that is being directly viewed, usually a pawn.  Could also be the net actor of consequence |
| `ViewLocation` | `FVector` | Where the viewer is looking from |
| `ViewDir` | `FVector` | Direction the viewer is looking |
