---
id: "api:class:UWidgetSkinProxy"
title: "UWidgetSkinProxy"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWidgetSkinProxy.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWidgetSkinProxy

The user widget proxy, using this proxy to activate widget skin for an user widget.

## Inheritance

`UObject` -> `IWidgetSkinProxyInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `bHideBeforeLoadSkin` | `bool` | - |
| `ActiveSkins` | `TArray < UUserWidgetSkin * >` | - |

## Functions

### `ApplySkin`

```text
ApplySkin(SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >, bAsyncLoad: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |
| `bAsyncLoad` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertSkin`

```text
RevertSkin(SkinPathPtr: TSoftClassPtr < UUserWidgetSkin >) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `SkinPathPtr` | `TSoftClassPtr < UUserWidgetSkin >` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `RevertRevertableSkin`

```text
RevertRevertableSkin() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetActiveSkins`

```text
GetActiveSkins() -> TArray < UUserWidgetSkin * >
```

**Returns**

| Type | Description |
|---|---|
| `TArray < UUserWidgetSkin * >` | - |

### `GetRevertableSkin`

```text
GetRevertableSkin() -> UUserWidgetSkin *
```

**Returns**

| Type | Description |
|---|---|
| `UUserWidgetSkin *` | - |

### `ContainsSkin`

```text
ContainsSkin(InSkin: UUserWidgetSkin *) -> bool
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSkin` | `UUserWidgetSkin *` | - |

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `GetOwnerUserWidget`

```text
GetOwnerUserWidget() -> UUserWidget *
```

**Returns**

| Type | Description |
|---|---|
| `UUserWidget *` | - |

## Language

`cpp`
