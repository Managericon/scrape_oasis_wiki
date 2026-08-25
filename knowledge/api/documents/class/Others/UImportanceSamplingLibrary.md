---
id: "api:class:UImportanceSamplingLibrary"
title: "UImportanceSamplingLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UImportanceSamplingLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UImportanceSamplingLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `RandomSobolFloat`

```text
RandomSobolFloat(Index: int32, Dimension: int32, Seed: float) -> ENGINE_API float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `Dimension` | `int32` | - Which Sobol dimension (0 to 15) |
| `Seed` | `float` | - Random seed (in the range 0-1) to randomize across multiple sequences |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | Sobol-distributed random number between 0 and 1 |

### `NextSobolFloat`

```text
NextSobolFloat(Index: int32, Dimension: int32, PreviousValue: float) -> ENGINE_API float
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `Dimension` | `int32` | - Which Sobol dimension (0 to 15) |
| `PreviousValue` | `float` | - The Sobol value for Index-1 |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API float` | Sobol-distributed random number between 0 and 1 |

### `RandomSobolCell2D`

```text
RandomSobolCell2D(Index: int32, NumCells: int32, Cell: FVector2D, Seed: FVector2D) -> ENGINE_API FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point in the cell (starting at 0) |
| `NumCells` | `int32` | - Size of cell grid, 1 to 32768. Rounded up to the next power of two |
| `Cell` | `FVector2D` | - Give a point from this integer grid cell |
| `Seed` | `FVector2D` | - Random 2D seed (components in the range 0-1) to randomize across multiple sequences |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector2D` | Sobol-distributed random 2D position in the given grid cell |

### `NextSobolCell2D`

```text
NextSobolCell2D(Index: int32, NumCells: int32, PreviousValue: FVector2D) -> ENGINE_API FVector2D
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `NumCells` | `int32` | - Size of cell grid, 1 to 32768. Rounded up to the next power of two |
| `PreviousValue` | `FVector2D` | - The Sobol value for Index-1 |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector2D` | Sobol-distributed random 2D position in the same grid cell |

### `RandomSobolCell3D`

```text
RandomSobolCell3D(Index: int32, NumCells: int32, Cell: FVector, Seed: FVector) -> ENGINE_API FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point in the cell (starting at 0) |
| `NumCells` | `int32` | - Size of cell grid, 1 to 1024. Rounded up to the next power of two |
| `Cell` | `FVector` | - Give a point from this integer grid cell |
| `Seed` | `FVector` | - Random 3D seed (components in the range 0-1) to randomize across multiple sequences |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | Sobol-distributed random 3D vector in the given grid cell |

### `NextSobolCell3D`

```text
NextSobolCell3D(Index: int32, NumCells: int32, PreviousValue: FVector) -> ENGINE_API FVector
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `int32` | - Which sequential point |
| `NumCells` | `int32` | - Size of cell grid, 1 to 1024. Rounded up to the next power of two |
| `PreviousValue` | `FVector` | - The Sobol value for Index-1 |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FVector` | Sobol-distributed random 3D position in the same grid cell |

### `MakeImportanceTexture`

```text
MakeImportanceTexture(Texture: UTexture2D *, WeightingFunc: TEnumAsByte < EImportanceWeight :: Type >) -> ENGINE_API FImportanceTexture
```

Create an FImportanceTexture object for texture-driven importance sampling from a 2D RGBA8 texture

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture2D *` | - Texture object to use. Must be RGBA8 format. |
| `WeightingFunc` | `TEnumAsByte < EImportanceWeight :: Type >` | - How to turn the texture data into probability weights |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API FImportanceTexture` | new ImportanceTexture object for use with ImportanceSample |

### `BreakImportanceTexture`

```text
BreakImportanceTexture(ImportanceTexture: FImportanceTexture &, Texture: UTexture2D * &, WeightingFunc: TEnumAsByte < EImportanceWeight :: Type > &) -> ENGINE_API void
```

Get texture used to create an ImportanceTexture object

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ImportanceTexture` | `FImportanceTexture &` | - The source ImportanceTexture object |
| `Texture` | `UTexture2D * &` | - |
| `WeightingFunc` | `TEnumAsByte < EImportanceWeight :: Type > &` | - How to turn the texture data into probability weights |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | new ImportanceTexture object for use with ImportanceSample |

### `ImportanceSample`

```text
ImportanceSample(Texture: FImportanceTexture &, Rand: FVector2D &, Samples: int, Intensity: float, SamplePosition: FVector2D &, SampleColor: FLinearColor &, SampleIntensity: float &, SampleSize: float &) -> ENGINE_API void
```

Distribute sample points proportional to Texture2D luminance.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `FImportanceTexture &` | - |
| `Rand` | `FVector2D &` | - Random 2D point with components evenly distributed between 0 and 1 |
| `Samples` | `int` | - Total number of samples that will be used |
| `Intensity` | `float` | - Total intensity for light |
| `SamplePosition` | `FVector2D &` | - |
| `SampleColor` | `FLinearColor &` | - |
| `SampleIntensity` | `float &` | - |
| `SampleSize` | `float &` | - |

**Returns**

| Type | Description |
|---|---|
| `ENGINE_API void` | - |

## Language

`cpp`
