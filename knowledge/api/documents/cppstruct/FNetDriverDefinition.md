---
id: "api:cppstruct:FNetDriverDefinition"
title: "FNetDriverDefinition"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FNetDriverDefinition.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FNetDriverDefinition

Container for describing various types of netdrivers available to the engine
  The engine will try to construct a netdriver of a given type and, failing that,
  the fallback version.

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `DefName` | `FName` | Unique name of this net driver definition |
| `DriverClassName` | `FName` | Class name of primary net driver |
| `DriverClassNameFallback` | `FName` | Class name of the fallback net driver if the main net driver class fails to initialize |
