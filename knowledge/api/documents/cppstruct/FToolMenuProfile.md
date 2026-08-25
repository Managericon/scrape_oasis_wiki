---
id: "api:cppstruct:FToolMenuProfile"
title: "FToolMenuProfile"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FToolMenuProfile.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FToolMenuProfile

A menu profile is a way for systems to modify instances of a menu by showinghiding specific items. You can have multiple profiles active on
  a single menu at the same time.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `Entries` | `TMap < FName , FCustomizedToolMenuEntry >` | - |
| `Sections` | `TMap < FName , FCustomizedToolMenuSection >` | - |
| `SuppressExtenders` | `TArray < FName >` | - |
