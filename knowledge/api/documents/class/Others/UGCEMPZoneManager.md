---
id: "api:class:UGCEMPZoneManager"
title: "UGCEMPZoneManager"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGCEMPZoneManager.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGCEMPZoneManager

电磁干扰区管理器

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `UGCEMPZoneManager.SuccessfullyGeneratedElectromagnetic` | `-` | param InstanceID number<br>@param CenterLocation FVector |
| `UGCEMPZoneManager.SuccessfullyStopElectromagnetic` | `-` | param InstanceID number |
| `UGCEMPZoneManager.NormalEndElectromagnetic` | `-` | param InstanceID number |
| `UGCEMPZoneManager.SuccessfullyStartElectromagnetic` | `-` | param InstanceID number |
| `UGCEMPZoneManager.AffectedElectromagneticPlayers` | `-` | param AffectedPlayerKeys number |
| `UGCEMPZoneManager.__EMPZoneMarkTypeID` | `-` | - |
| `UGCEMPZoneManager.__EMPZoneMarkInstIDs` | `-` | - |

## Functions

### `_ValidateAndClampConfig`

```text
_ValidateAndClampConfig(Config: UGCEMPZoneConfig) -> UGCEMPZoneConfig
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Config` | `UGCEMPZoneConfig` | - |

**Returns**

| Type | Description |
|---|---|
| `UGCEMPZoneConfig` | - |

### `_GetInstanceDetailData`

```text
_GetInstanceDetailData(InstanceID: number) -> table|nil
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | - |

### `_GetConfigByIndex`

```text
_GetConfigByIndex(Index: number) -> table|nil
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | - |

### `_ModifyConfigByIndex`

```text
_ModifyConfigByIndex(Index: number, NewConfig: table) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Index` | `number` | - |
| `NewConfig` | `table` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `_GetElectromagneticAreaConfigs`

```text
_GetElectromagneticAreaConfigs(InstanceID: number|nil) -> table|nil
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number\|nil` | - |

**Returns**

| Type | Description |
|---|---|
| `table\|nil` | - |

### `_ConvertToLuaConfigs`

```text
_ConvertToLuaConfigs(ElectromagneticInstances: table) -> table
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ElectromagneticInstances` | `table` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `_GenerateNextInstanceID`

```text
_GenerateNextInstanceID() -> number
```

**Returns**

| Type | Description |
|---|---|
| `number` | - |

### `_MapLuaConfigToComponent`

```text
_MapLuaConfigToComponent(LuaConfig: UGCEMPZoneConfig) -> FEMPZoneCfg
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `LuaConfig` | `UGCEMPZoneConfig` | - |

**Returns**

| Type | Description |
|---|---|
| `FEMPZoneCfg` | - |

### `_SyncCapsuleRadius`

```text
_SyncCapsuleRadius(EMPZoneActor: AEMPZoneActor, InstanceData: table) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `EMPZoneActor` | `AEMPZoneActor` | - |
| `InstanceData` | `table` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `_WriteConfigToComponent`

```text
_WriteConfigToComponent(Comp: UEMPZoneControlComponent, ComponentConfig: FEMPZoneCfg) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Comp` | `UEMPZoneControlComponent` | - |
| `ComponentConfig` | `FEMPZoneCfg` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `CreateEMPZone`

```text
CreateEMPZone(ConfigID: string, CenterLocation: FVector)
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigID` | `string` | - |
| `CenterLocation` | `FVector` | - |

### `_CreateEMPZoneActor`

```text
_CreateEMPZoneActor(InstanceID: number) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `DestroyElectromagneticArea`

```text
DestroyElectromagneticArea(InstanceID: number) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `_DestroyAllElectromagneticAreas`

```text
_DestroyAllElectromagneticAreas() -> boolean
```

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `ModifyConfigElectromagneticArea`

```text
ModifyConfigElectromagneticArea(ConfigIndex: number, ParameterName: string, NewValue: any) -> boolean
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ConfigIndex` | `number` | - |
| `ParameterName` | `string` | - |
| `NewValue` | `any` | - |

**Returns**

| Type | Description |
|---|---|
| `boolean` | - |

### `GetAllConfigElectromagneticArea`

```text
GetAllConfigElectromagneticArea() -> table
```

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `GetSpecifyElectromagneticAreaList`

```text
GetSpecifyElectromagneticAreaList(InstanceID: number) -> table
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

**Returns**

| Type | Description |
|---|---|
| `table` | - |

### `_NotifyClientHideMapMark`

```text
_NotifyClientHideMapMark(InstanceID: number)
```

当 EMPZone 销毁时隐藏小地图标记

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | - |

### `Client_OnEMPZoneMapMarkShow`

```text
Client_OnEMPZoneMapMarkShow(InstanceID: number, LocX: number, LocY: number, LocZ: number, EffectRadius: number, ZoneState: number)
```

[Client RPC] 显示 EMPZone 小地图标记

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 实例ID |
| `LocX` | `number` | 位置X坐标 |
| `LocY` | `number` | 位置Y坐标 |
| `LocZ` | `number` | 位置Z坐标 |
| `EffectRadius` | `number` | 影响半径 |
| `ZoneState` | `number` | 区域状态 |

### `Client_OnEMPZoneMapMarkHide`

```text
Client_OnEMPZoneMapMarkHide(InstanceID: number)
```

[Client RPC] 隐藏 EMPZone 小地图标记

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InstanceID` | `number` | 实例ID |

## Language

`lua`
