---
id: "api:cppstruct:FInputAxisKeyMapping"
title: "FInputAxisKeyMapping"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FInputAxisKeyMapping.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FInputAxisKeyMapping

Defines a mapping between an axis and key

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `AxisName` | `FName` | Friendly name of axis, e.g "MoveForward" |
| `Key` | `FKey` | Key to bind it to. |
| `Scale` | `float` | Multiplier to use for the mapping when accumulating the axis value |
| `KeySeq` | `uint8` | key sequence number: 0 for Primary key, 1 for Backup key |
