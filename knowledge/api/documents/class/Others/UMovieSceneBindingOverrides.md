---
id: "api:class:UMovieSceneBindingOverrides"
title: "UMovieSceneBindingOverrides"
source: "https://developer.gp.qq.com/api/class/detail/Others/UMovieSceneBindingOverrides.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UMovieSceneBindingOverrides

A one-to-many definition of movie scene object binding IDs to overridden objects that should be bound to that binding.

## Inheritance

`UObject` -> `IMovieSceneBindingOverridesInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `BindingData` | `TArray < FMovieSceneBindingOverrideData >` | The actual binding data |

## Functions

### `GetBindingData`

```text
GetBindingData() -> const TArray < FMovieSceneBindingOverrideData > &
```

**Returns**

| Type | Description |
|---|---|
| `const TArray < FMovieSceneBindingOverrideData > &` | - |

### `MakeBindingID`

```text
MakeBindingID(InBindingID: FGuid &, InSequenceID: FMovieSceneSequenceID, InSpace: EMovieSceneObjectBindingSpace) -> FMovieSceneObjectBindingID
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InBindingID` | `FGuid &` | - |
| `InSequenceID` | `FMovieSceneSequenceID` | - |
| `InSpace` | `EMovieSceneObjectBindingSpace` | - |

**Returns**

| Type | Description |
|---|---|
| `FMovieSceneObjectBindingID` | - |

### `GetGuidStr`

```text
GetGuidStr(BindingID: FMovieSceneObjectBindingID &) -> FString
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `BindingID` | `FMovieSceneObjectBindingID &` | - |

**Returns**

| Type | Description |
|---|---|
| `FString` | - |

## Language

`cpp`
