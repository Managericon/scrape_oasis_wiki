---
id: "api:cppstruct:FCustomProfile"
title: "FCustomProfile"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCustomProfile.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCustomProfile

Structure for custom profiles.
 
  if you'd like to just add custom channels, not changing anything else engine defined
  if you'd like to override all about profile, please use 
  +Profiles=(Name=NameOfProfileYouLikeToOverwrite,....)

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Name` | `FName` | - |
| `CustomResponses` | `TArray < FResponseChannel >` | Types of objects that this physics objects will collide with. |
