---
id: "api:class:ALevelBounds"
title: "ALevelBounds"
source: "https://developer.gp.qq.com/api/class/detail/Others/ALevelBounds.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ALevelBounds

Defines level bounds
  Updates bounding box automatically based on actors transformation changes or holds fixed user defined bounding box
  Uses only actors where AActor::IsLevelBoundsRelevant() == true

## Inheritance

`AActor` -> `FEditorTickableLevelBounds`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bAutoUpdateBounds` | `bool` | Whether to automatically update actor bounds based on all relevant actors bounds belonging to the same level |
| `bCalWithoutLandscapeSpline` | `bool` | - |

## Functions

### `SaveLevelBoudns`

```text
SaveLevelBoudns() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CaculateFoliageLevelBounds`

```text
CaculateFoliageLevelBounds() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `CaculateLandscapeLevelBounds`

```text
CaculateLandscapeLevelBounds() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
