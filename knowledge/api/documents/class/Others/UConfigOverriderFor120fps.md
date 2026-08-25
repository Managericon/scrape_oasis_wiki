---
id: "api:class:UConfigOverriderFor120fps"
title: "UConfigOverriderFor120fps"
source: "https://developer.gp.qq.com/api/class/detail/Others/UConfigOverriderFor120fps.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UConfigOverriderFor120fps

## Inheritance

`UObject`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ConfigFor120fps` | `TArray < FConfigOverriderSetting >` | - |
| `ConfigForEnergySaving` | `TArray < FConfigOverriderSetting >` | - |
| `TextureLODGroupFilterOverride` | `TArray < FTextureLODGroupFilterOverride >` | - |
| `bHadApplyConfigFor120fps` | `bool` | - |
| `bHadApplyForEnergySaving` | `bool` | - |

## Functions

### `Enable120fpsConfigs`

```text
Enable120fpsConfigs(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableEnergySavingModeConfigs`

```text
EnableEnergySavingModeConfigs(bEnergySaving: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnergySaving` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecoverConfigs`

```text
RecoverConfigs() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Recover120fpsConfigs`

```text
Recover120fpsConfigs() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RecoverEnergySavingModeConfigs`

```text
RecoverEnergySavingModeConfigs() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableTextureFilterOverrider`

```text
EnableTextureFilterOverrider(bEnable: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `bEnable` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
