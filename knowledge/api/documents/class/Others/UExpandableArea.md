---
id: "api:class:UExpandableArea"
title: "UExpandableArea"
source: "https://developer.gp.qq.com/api/class/detail/Others/UExpandableArea.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UExpandableArea

## Inheritance

`UWidget` -> `INamedSlotInterface`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Style` | `FExpandableAreaStyle` | - |
| `BorderBrush` | `FSlateBrush` | - |
| `BorderColor` | `FSlateColor` | - |
| `bIsExpanded` | `bool` | - |
| `MaxHeight` | `float` | The maximum height of the area |
| `HeaderPadding` | `FMargin` | - |
| `AreaPadding` | `FMargin` | - |
| `HeaderContent` | `UWidget *` | - |
| `BodyContent` | `UWidget *` | - |

## Functions

### `GetIsExpanded`

```text
GetIsExpanded() -> bool
```

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetIsExpanded`

```text
SetIsExpanded(IsExpanded: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsExpanded` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetIsExpanded_Animated`

```text
SetIsExpanded_Animated(IsExpanded: bool) -> void
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `IsExpanded` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Delegates

### `OnExpansionChanged`

```text
OnExpansionChanged(Area: UExpandableArea*, bIsExpanded: bool) -> void
```

A bindable delegate for the IsChecked.

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Area` | `UExpandableArea*` | - |
| `bIsExpanded` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
