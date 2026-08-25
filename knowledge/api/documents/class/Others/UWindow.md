---
id: "api:class:UWindow"
title: "UWindow"
source: "https://developer.gp.qq.com/api/class/detail/Others/UWindow.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UWindow

## Inheritance

`UUserWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Title` | `FText` | - |
| `InitSize` | `FVector2D` | - |
| `ContentSlot` | `UWindowSlot *` | - |

## Functions

### `SetTitle`

```text
SetTitle(InTitle: FText) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InTitle` | `FText` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetContent`

```text
SetContent(Content: UWidget *) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `Resize`

```text
Resize(NewSize: FVector2D) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `NewSize` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
