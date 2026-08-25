---
id: "api:class:URichTextBlock"
title: "URichTextBlock"
source: "https://developer.gp.qq.com/api/class/detail/Others/URichTextBlock.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# URichTextBlock

The rich text block
 
   Fancy Text
   No Children

## Inheritance

`UTextLayoutWidget`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `Text` | `FText` | The text to display |
| `TextDelegate` | `FGetText` | A bindable delegate to allow logic to drive the text of the widget |
| `Font` | `FSlateFontInfo` | The default font for the text. |
| `Color` | `FLinearColor` | The default color for the text. |
| `Decorators` | `TArray < URichTextBlockDecorator * >` | - |

## Functions

### `GetLocalText`

```text
GetLocalText() -> FText
```

**Returns**

| Type | Description |
|---|---|
| `FText` | - |

## Language

`cpp`
