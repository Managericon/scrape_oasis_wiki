---
id: "api:cppstruct:FShapedTextOptions"
title: "FShapedTextOptions"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FShapedTextOptions.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FShapedTextOptions

Common data for all widgets that use shaped text.
  Contains the common options that should be exposed for the underlying Slate widget.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bOverride_TextShapingMethod` | `uint32` | - |
| `bOverride_TextFlowDirection` | `uint32` | - |
| `TextShapingMethod` | `ETextShapingMethod` | Which text shaping method should the text within this widget use? (unset to use the default returned by GetDefaultTextShapingMethod) |
| `TextFlowDirection` | `ETextFlowDirection` | Which text flow direction should the text within this widget use? (unset to use the default returned by GetDefaultTextFlowDirection) |
