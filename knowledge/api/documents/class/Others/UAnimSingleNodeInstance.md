---
id: "api:class:UAnimSingleNodeInstance"
title: "UAnimSingleNodeInstance"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAnimSingleNodeInstance.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAnimSingleNodeInstance

## Inheritance

`UAnimInstance`

## Functions

### `SetLooping`

```text
SetLooping(bIsLooping: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsLooping` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlayRate`

```text
SetPlayRate(InPlayRate: float) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetReverse`

```text
SetReverse(bInReverse: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bInReverse` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPosition`

```text
SetPosition(InPosition: float, bFireNotifies: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosition` | `float` | - |
| `bFireNotifies` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPositionWithPreviousTime`

```text
SetPositionWithPreviousTime(InPosition: float, InPreviousTime: float, bFireNotifies: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosition` | `float` | - |
| `InPreviousTime` | `float` | - |
| `bFireNotifies` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBlendSpaceInput`

```text
SetBlendSpaceInput(InBlendInput: FVector &) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBlendInput` | `FVector &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPlaying`

```text
SetPlaying(bIsPlaying: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsPlaying` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLength`

```text
GetLength() -> float
```

**Returns**

| Type | Description |
|---|---|
| `float` | - |

### `PlayAnim`

```text
PlayAnim(bIsLooping: bool, InPlayRate: float, InStartPosition: float) -> void
```

For AnimSequence specific

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bIsLooping` | `bool` | - |
| `InPlayRate` | `float` | - |
| `InStartPosition` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `StopAnim`

```text
StopAnim() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetAnimationAsset`

```text
SetAnimationAsset(NewAsset: UAnimationAsset *, bIsLooping: bool, InPlayRate: float) -> void
```

Set New Asset - calls InitializeAnimation, for now we need MeshComponent

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewAsset` | `UAnimationAsset *` | - |
| `bIsLooping` | `bool` | - |
| `InPlayRate` | `float` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAnimationAsset`

```text
GetAnimationAsset() -> UAnimationAsset *
```

Get the currently used asset

**Returns**

| Type | Description |
|---|---|
| `UAnimationAsset *` | - |

### `SetPreviewCurveOverride`

```text
SetPreviewCurveOverride(PoseName: FName &, Value: float, bRemoveIfZero: bool) -> void
```

Set pose value

**Parameters**

| Name | Type | Description |
|---|---|---|
| `PoseName` | `FName &` | - |
| `Value` | `float` | - |
| `bRemoveIfZero` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `PostEvaluateAnimEvent`

```text
PostEvaluateAnimEvent() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAnimSinglePlayAnim`

```text
OnAnimSinglePlayAnim(AnimAsset: UAnimationAsset*, bPlay: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `AnimAsset` | `UAnimationAsset*` | - |
| `bPlay` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
