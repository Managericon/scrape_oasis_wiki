---
id: "api:class:UBTComposite_SimpleParallel"
title: "UBTComposite_SimpleParallel"
source: "https://developer.gp.qq.com/api/class/detail/Others/UBTComposite_SimpleParallel.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UBTComposite_SimpleParallel

Simple Parallel composite node.
  Allows for running two children: one which must be a single task node (with optional decorators), and the other of which can be a complete subtree.

## Inheritance

`UBTCompositeNode`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FinishMode` | `TEnumAsByte < EBTParallelMode :: Type >` | how background tree should be handled when main task finishes execution |

## Language

`cpp`
