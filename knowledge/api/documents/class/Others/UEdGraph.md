---
id: "api:class:UEdGraph"
title: "UEdGraph"
source: "https://developer.gp.qq.com/api/class/detail/Others/UEdGraph.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UEdGraph

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Schema` | `TSubclassOf < UEdGraphSchema >` | The schema that this graph obeys |
| `Nodes` | `TArray < UEdGraphNode * >` | Set of all nodes in this graph |
| `bEditable` | `uint32` | If true, graph can be edited by the user |
| `bAllowDeletion` | `uint32` | - |
| `bAllowRenaming` | `uint32` | If true, graph can be renamed; Note: Graph can also be renamed if bAllowDeletion is true currently |

## Language

`cpp`
