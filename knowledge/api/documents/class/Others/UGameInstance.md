---
id: "api:class:UGameInstance"
title: "UGameInstance"
source: "https://developer.gp.qq.com/api/class/detail/Others/UGameInstance.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UGameInstance

GameInstance: high-level manager object for an instance of the running game.
  Spawned at game creation and not destroyed until game instance is shut down.
  Running as a standalone game, there will be one of these.
  Running in PIE (play-in-editor) will generate one of these per PIE instance.

## Inheritance

`UObject` -> `FExec`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `EncryptedLocalPlayers` | `TArray < int64 >` | - |
| `LocalPlayers` | `TArray < ULocalPlayer * >` | - |
| `OnlineSession` | `UOnlineSession *` | Class to manage online services |
| `bUseEncryptLocalPlayerPtr` | `bool` | - |
| `DSHUD` | `UObject *` | - |
| `CachedConsoleVariableBunch_Groups` | `TArray < TArray < uint8 > >` | - |
| `CachedConsoleVariableBunch_BigWorld` | `TArray < uint8 >` | - |
| `CachedConsoleVariableBunch_Permanent` | `TArray < uint8 >` | - |
| `SpecialPakResStates` | `TMap < ESpecialPakID , EPakResState >` | - |

## Functions

### `ReceiveInit`

```text
ReceiveInit() -> void
```

Opportunity for blueprints to handle the game instance being initialized.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveShutdown`

```text
ReceiveShutdown() -> void
```

Opportunity for blueprints to handle the game instance being shutdown.

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleNetworkError`

```text
HandleNetworkError(FailureType: ENetworkFailure :: Type, bIsServer: bool) -> void
```

Opportunity for blueprints to handle network errors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FailureType` | `ENetworkFailure :: Type` | - |
| `bIsServer` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `HandleTravelError`

```text
HandleTravelError(FailureType: ETravelFailure :: Type) -> void
```

Opportunity for blueprints to handle travel errors.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `FailureType` | `ETravelFailure :: Type` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugCreatePlayer`

```text
DebugCreatePlayer(ControllerId: int32) -> void
```

Local player access 
	
	  Debug console command to create a player.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControllerId` | `int32` | - The controller ID the player should accept input from. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `DebugRemovePlayer`

```text
DebugRemovePlayer(ControllerId: int32) -> void
```

Debug console command to remove the player with a given controller ID.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `ControllerId` | `int32` | - The controller ID to search for. |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetDynaConfigAndDynaCVar`

```text
ResetDynaConfigAndDynaCVar() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetDynaConfig`

```text
ResetDynaConfig() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SendConsoleVariableBunch`

```text
SendConsoleVariableBunch(CVarType: ECVarType, Connection: UNetConnection *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |
| `Connection` | `UNetConnection *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveConsoleVariableBunch_BigWorld`

```text
ReceiveConsoleVariableBunch_BigWorld(InConsoleVariablesBunch: TArray < uint8 >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InConsoleVariablesBunch` | `TArray < uint8 >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ReceiveConsoleVariableBunch_Permanent`

```text
ReceiveConsoleVariableBunch_Permanent(InConsoleVariablesBunch: TArray < uint8 >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InConsoleVariablesBunch` | `TArray < uint8 >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `EnableConsoleVariableBunch`

```text
EnableConsoleVariableBunch(CVarType: ECVarType, bMapIsBigWorld: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |
| `bMapIsBigWorld` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ClearConsoleVariableBunch`

```text
ClearConsoleVariableBunch(CVarType: ECVarType) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `ResetConsoleVariable`

```text
ResetConsoleVariable(CVarType: ECVarType) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `CVarType` | `ECVarType` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetPakResState`

```text
SetPakResState(InPakID: ESpecialPakID, InPakState: EPakResState) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |
| `InPakState` | `EPakResState` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPakResState`

```text
GetPakResState(InPakID: ESpecialPakID) -> EPakResState
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |

**Returns**

| Type | Description |
|---|---|
| `EPakResState` | - |

### `IsPlatformSplitPakRes`

```text
IsPlatformSplitPakRes(InPakID: ESpecialPakID) -> EPakSplitState
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |

**Returns**

| Type | Description |
|---|---|
| `EPakSplitState` | - |

### `InitPakResState`

```text
InitPakResState() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnPakResStateChanged`

```text
OnPakResStateChanged(InPakID: ESpecialPakID, InPakOldState: EPakResState, InPakNewState: EPakResState) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPakID` | `ESpecialPakID` | - |
| `InPakOldState` | `EPakResState` | - |
| `InPakNewState` | `EPakResState` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
