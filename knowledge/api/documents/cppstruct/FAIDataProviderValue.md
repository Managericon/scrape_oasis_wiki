---
id: "api:cppstruct:FAIDataProviderValue"
title: "FAIDataProviderValue"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FAIDataProviderValue.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FAIDataProviderValue

AIDataProvider is an object that can provide collection of properties
  associated with bound pawn owner or request Id.
 
  Editable properties are used to set up provider instance,
  creating additional filters or ways of accessing data (e.g. gameplay tag of ability)
 
  Non editable properties are holding data

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `CachedProperty` | `UProperty *` | cached uproperty of provider |
| `DataBinding` | `UAIDataProvider *` | (optional) provider for dynamic data binding |
| `DataField` | `FName` | name of provider's value property |
