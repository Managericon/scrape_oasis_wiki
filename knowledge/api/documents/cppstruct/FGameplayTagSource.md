---
id: "api:cppstruct:FGameplayTagSource"
title: "FGameplayTagSource"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FGameplayTagSource.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FGameplayTagSource

Struct defining where gameplay tags are loadedsaved from. Mostly for the editor

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `SourceName` | `FName` | Name of this source |
| `SourceType` | `EGameplayTagSourceType` | Type of this source |
| `SourceTagList` | `UGameplayTagsList *` | If this is bound to an ini object for saving, this is the one |
