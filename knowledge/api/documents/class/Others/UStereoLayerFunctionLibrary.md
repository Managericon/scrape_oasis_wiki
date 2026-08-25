---
id: "api:class:UStereoLayerFunctionLibrary"
title: "UStereoLayerFunctionLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UStereoLayerFunctionLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UStereoLayerFunctionLibrary

StereoLayer Extensions Function Library

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `SetSplashScreen`

```text
SetSplashScreen(Texture: UTexture *, Scale: FVector2D, Offset: FVector2D, bShowLoadingMovie: bool, bShowOnSet: bool) -> void
```

Set splash screen attributes

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Texture` | `UTexture *` | (in) A texture to be used for the splash. B8R8G8A8 format. |
| `Scale` | `FVector2D` | (in) Scale of the texture. |
| `Offset` | `FVector2D` | (in) Position from which to start rendering the texture. |
| `bShowLoadingMovie` | `bool` | - |
| `bShowOnSet` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ShowSplashScreen`

```text
ShowSplashScreen() -> void
```

Show the splash screen and override the VR display

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HideSplashScreen`

```text
HideSplashScreen() -> void
```

Hide the splash screen and return to normal display.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableAutoLoadingSplashScreen`

```text
EnableAutoLoadingSplashScreen(InAutoShowEnabled: bool) -> void
```

Enablesdisables splash screen to be automatically shown when LoadMap is called.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAutoShowEnabled` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
