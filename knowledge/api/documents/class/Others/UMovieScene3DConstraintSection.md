---
id: "api:class:UMovieScene3DConstraintSection"
title: "UMovieScene3DConstraintSection"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieScene3DConstraintSection.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieScene3DConstraintSection

Base class for 3D constraint section

## Inheritance

`UMovieSceneSection`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConstraintId` | `FGuid` | The possessable guid that this constraint uses |
| `ConstraintBindingID` | `FMovieSceneObjectBindingID` | The binding ID of the target this constraint attaches to. May resolve into a parent sequence for cross-sub-sequence spawnables. |

## Functions

### `GetConstraintBindingID`

```text
GetConstraintBindingID() -> const MOVIESCENETRACKS_API FMovieSceneObjectBindingID &
```

Get the full binding ID (supports cross-sub-sequence bindings).

**Returns**

| Type | Description |
|---|---|
| `const MOVIESCENETRACKS_API FMovieSceneObjectBindingID &` | - |

### `SetConstraintBindingID`

```text
SetConstraintBindingID(InBindingID: FMovieSceneObjectBindingID &) -> MOVIESCENETRACKS_API void
```

Set the full binding ID (supports cross-sub-sequence bindings).

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBindingID` | `FMovieSceneObjectBindingID &` | - |

**Returns**

| Type | Description |
|---|---|
| `MOVIESCENETRACKS_API void` | - |

## Language

`cpp`
