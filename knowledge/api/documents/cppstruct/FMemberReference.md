---
id: "api:cppstruct:FMemberReference"
title: "FMemberReference"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FMemberReference.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FMemberReference

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `MemberParent` | `UObject *` | Most often the Class that this member is defined in. Could be a UPackage <br>	  if it is a native delegate signature function (declared globally). Should <br>	  be NULL if bSelfContext is true. |
| `MemberScope` | `FString` | - |
| `MemberName` | `FName` | Name of variable |
| `MemberGuid` | `FGuid` | The Guid of the variable |
| `bSelfContext` | `bool` | Whether or not this should be a "self" context |
| `bWasDeprecated` | `bool` | Whether or not this property has been deprecated |
