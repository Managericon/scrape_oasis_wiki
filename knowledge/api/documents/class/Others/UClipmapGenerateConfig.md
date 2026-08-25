---
id: "api:class:UClipmapGenerateConfig"
title: "UClipmapGenerateConfig"
source: "https://developer.gp.qq.com/api/class/detail/Others/UClipmapGenerateConfig.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UClipmapGenerateConfig

## Inheritance

`UDataAsset`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `TargetTexture` | `UTexture2D *` | - |
| `TargetClipmapTexture` | `UClipmapTexture *` | - |
| `ClipmapWetnessConfig` | `FClipmapWetness` | - |
| `FoliageHealthAndAbsorptionConfig` | `FClipmapFoliageHealthAndAbsorption` | - |
| `LandscapeTintConfig` | `FClipmapLandscapeTint` | - |
| `BurshTintNum` | `int32` | - |
| `WeightBitsNum` | `int32` | - |
| `WeightMax` | `int32` | - |

## Functions

### `GenerateGChannel`

```text
GenerateGChannel() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GenerateBAChannel`

```text
GenerateBAChannel() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GenerateCustomMips`

```text
GenerateCustomMips() -> void
```

统一的Mip后处理入口：先让引擎生成标准Mip，再后处理R通道(Max降采样)，可选BA通道(众数)

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
