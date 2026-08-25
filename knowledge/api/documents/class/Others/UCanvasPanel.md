---
id: "api:class:UCanvasPanel"
title: "UCanvasPanel"
source: "https://developer.gp.qq.com/api/class/detail/Others/UCanvasPanel.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UCanvasPanel

The canvas panel is a designer friendly panel that allows widgets to be laid out at arbitrary 
  locations, anchored and z-ordered with other children of the canvas.  The canvas is a great widget
  for manual layout, but bad when you want to procedurally just generate widgets and place them in a 
  container (unless you want absolute layout).
 
   Many Children
   Absolute Layout
   Anchors

## Inheritance

`UPanelWidget`

## Functions

### `AddChildToCanvas`

```text
AddChildToCanvas(Content: UWidget *) -> UCanvasPanelSlot *
```

**Parameters**

| Name | Type | Description |
|---|---|---|
| `Content` | `UWidget *` | - |

**Returns**

| Type | Description |
|---|---|
| `UCanvasPanelSlot *` | - |

## Language

`cpp`
