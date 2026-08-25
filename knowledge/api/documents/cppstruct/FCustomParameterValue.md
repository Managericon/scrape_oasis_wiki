---
id: "api:cppstruct:FCustomParameterValue"
title: "FCustomParameterValue"
source: "https://developer.gp.qq.com/api/cppstruct/detail/FCustomParameterValue.json"
category: "API Wiki/cppstruct"
kind: "cppstruct"
api_root: "https://developer.gp.qq.com/api/"
---

# FCustomParameterValue

项目自定义参数统一容器。
  一个值多街区须通过 Kind 分支。字段参考 FCustomParameterValue-重构方案.md 第 2.1 节。
 
  注意：
  - 该结构不进入 FMaterialInstanceResource，渲染线程完全无感
  - Atlas 的数值是 Index，写回 FScalarParameterValue::ParameterValue
  - Clipmap 的 Texture 值写回 FTextureParameterValue::ParameterValue（UClipmapTexture 继承 UTexture）

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ParameterName` | `FName` | - |
| `Kind` | `ECustomParameterKind` | - |
| `ExpressionGUID` | `FGuid` | - |
| `bIsUsedAsAtlasPosition` | `bool` | - |
| `AtlasCurve` | `TSoftObjectPtr < UCurveLinearColor >` | - |
| `Atlas` | `TSoftObjectPtr < UCurveLinearColorAtlas >` | - |
| `bIsUsedAsClipmapTexture` | `bool` | - |
| `ClipmapTexture` | `UClipmapTexture *` | - |
