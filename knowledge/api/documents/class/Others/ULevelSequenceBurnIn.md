---
id: "api:class:ULevelSequenceBurnIn"
title: "ULevelSequenceBurnIn"
source: "https://developer.gp.qq.com/api/class/detail/Others/ULevelSequenceBurnIn.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# ULevelSequenceBurnIn

Base class for level sequence burn ins

## Inheritance

`UUserWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `FrameInformation` | `FLevelSequencePlayerSnapshot` | Snapshot of frame information. |
| `LevelSequenceActor` | `ALevelSequenceActor *` | The actor to get our burn in frames from |

## Functions

### `SetSettings`

```text
SetSettings(InSettings: UObject *) -> void
```

Called when this burn in is receiving its settings

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSettings` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSettingsClass`

```text
GetSettingsClass() -> TSubclassOf < ULevelSequenceBurnInInitSettings >
```

Get the settings class to use for this burn in

**Returns**

| Type | Description |
|---|---|
| `TSubclassOf < ULevelSequenceBurnInInitSettings >` | - |

## Language

`cpp`
