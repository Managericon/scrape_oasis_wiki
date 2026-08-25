---
id: "api:cppstruct:FRedirector"
title: "FRedirector"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FRedirector.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FRedirector

This is used for redirecting old name to new name
 We use manually parsing array, but that makes harder to modify from property setting
 So adding this USTRUCT to support it properly

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `OldName` | `FName` | - |
| `NewName` | `FName` | Types of objects that this physics objects will collide with. |
