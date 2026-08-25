---
id: "api:class:UAudioMixerBlueprintLibrary"
title: "UAudioMixerBlueprintLibrary"
source: "https://developer.gp.qq.com/api/class/detail/Others/UAudioMixerBlueprintLibrary.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UAudioMixerBlueprintLibrary

## Inheritance

`UBlueprintFunctionLibrary`

## Functions

### `AddMasterSubmixEffect`

```text
AddMasterSubmixEffect(WorldContextObject: UObject *, SubmixEffectPreset: USoundEffectSubmixPreset *) -> void
```

Adds a submix effect preset to the master submix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SubmixEffectPreset` | `USoundEffectSubmixPreset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveMasterSubmixEffect`

```text
RemoveMasterSubmixEffect(WorldContextObject: UObject *, SubmixEffectPreset: USoundEffectSubmixPreset *) -> void
```

Removes a submix effect preset from the master submix.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `SubmixEffectPreset` | `USoundEffectSubmixPreset *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearMasterSubmixEffects`

```text
ClearMasterSubmixEffects(WorldContextObject: UObject *) -> void
```

Clears all master submix effects.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `AddSourceEffectToPresetChain`

```text
AddSourceEffectToPresetChain(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *, Entry: FSourceEffectChainEntry) -> void
```

Adds source effect entry to preset chain. Only effects the instance of the preset chain

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |
| `Entry` | `FSourceEffectChainEntry` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RemoveSourceEffectFromPresetChain`

```text
RemoveSourceEffectFromPresetChain(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *, EntryIndex: int32) -> void
```

Adds source effect entry to preset chain. Only affects the instance of preset chain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |
| `EntryIndex` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetBypassSourceEffectChainEntry`

```text
SetBypassSourceEffectChainEntry(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *, EntryIndex: int32, bBypassed: bool) -> void
```

Set whether or not to bypass the effect at the source effect chain index.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |
| `EntryIndex` | `int32` | - |
| `bBypassed` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetNumberOfEntriesInSourceEffectChain`

```text
GetNumberOfEntriesInSourceEffectChain(WorldContextObject: UObject *, PresetChain: USoundEffectSourcePresetChain *) -> int32
```

Returns the number of effect chain entries in the given source effect chain.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `WorldContextObject` | `UObject *` | - |
| `PresetChain` | `USoundEffectSourcePresetChain *` | - |

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

## Language

`cpp`
