---
id: "api:class:UCanvasPanelSlot"
title: "UCanvasPanelSlot"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCanvasPanelSlot.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCanvasPanelSlot

## Inheritance

`UPanelSlot`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `LayoutData` | `FAnchorData` | The anchoring information for the slot |
| `bAutoSize` | `bool` | When AutoSize is true we use the widget's desired size |
| `ZOrder` | `int32` | The order priority this widget is rendered in.  Higher values are rendered last (and so they will appear to be on top). |
| `bAntiAdaptation` | `bool` | - |

## Functions

### `SetLayout`

```text
SetLayout(InLayoutData: FAnchorData &) -> void
```

Sets the layout data of the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InLayoutData` | `FAnchorData &` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetLayout`

```text
GetLayout() -> FAnchorData
```

Gets the layout data of the slot

**Returns**

| Type | Description |
|---|---|
| `FAnchorData` | - |

### `SetPosition`

```text
SetPosition(InPosition: FVector2D) -> void
```

Sets the position of the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InPosition` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetPosition`

```text
GetPosition() -> FVector2D
```

Gets the position of the slot

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetSize`

```text
SetSize(InSize: FVector2D) -> void
```

Sets the size of the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InSize` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetSize`

```text
GetSize() -> FVector2D
```

Gets the size of the slot

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetOffsets`

```text
SetOffsets(InOffset: FMargin) -> void
```

Sets the offset data of the slot, which could be position and size, or margins depending on the anchor points

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InOffset` | `FMargin` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetOffsets`

```text
GetOffsets() -> FMargin
```

Gets the offset data of the slot, which could be position and size, or margins depending on the anchor points

**Returns**

| Type | Description |
|---|---|
| `FMargin` | - |

### `SetAnchors`

```text
SetAnchors(InAnchors: FAnchors) -> void
```

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAnchors` | `FAnchors` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAnchors`

```text
GetAnchors() -> FAnchors
```

Gets the anchors on the slot

**Returns**

| Type | Description |
|---|---|
| `FAnchors` | - |

### `SetAlignment`

```text
SetAlignment(InAlignment: FVector2D) -> void
```

Sets the alignment on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InAlignment` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAlignment`

```text
GetAlignment() -> FVector2D
```

Gets the alignment on the slot

**Returns**

| Type | Description |
|---|---|
| `FVector2D` | - |

### `SetAutoSize`

```text
SetAutoSize(InbAutoSize: bool) -> void
```

Sets if the slot to be auto-sized

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbAutoSize` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAutoSize`

```text
GetAutoSize() -> bool
```

Gets if the slot to be auto-sized

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetZOrder`

```text
SetZOrder(InZOrder: int32) -> void
```

Sets the z-order on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InZOrder` | `int32` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetZOrder`

```text
GetZOrder() -> int32
```

Gets the z-order on the slot

**Returns**

| Type | Description |
|---|---|
| `int32` | - |

### `SetAntiAdaptation`

```text
SetAntiAdaptation(InbAntiAdaptation: bool) -> void
```

Sets the bAntiAdaptation on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InbAntiAdaptation` | `bool` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `GetAntiAdaptation`

```text
GetAntiAdaptation() -> bool
```

Gets the bAntiAdaptation on the slot

**Returns**

| Type | Description |
|---|---|
| `bool` | - |

### `SetMinimum`

```text
SetMinimum(InMinimumAnchors: FVector2D) -> void
```

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMinimumAnchors` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `SetMaximum`

```text
SetMaximum(InMaximumAnchors: FVector2D) -> void
```

Sets the anchors on the slot

**Parameters**

| Name | Type | Description |
|---|---|---|
| `InMaximumAnchors` | `FVector2D` | - |

**Returns**

| Type | Description |
|---|---|
| `void` | - |

### `OnAntiAdaptationOffsetsChange`

```text
OnAntiAdaptationOffsetsChange() -> void
```

**Returns**

| Type | Description |
|---|---|
| `void` | - |

## Language

`cpp`
