---
id: "api:class:UListView"
title: "UListView"
source: "https://developer.gp.qq.com/api/class/detail/Others/UListView.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# UListView

Allows thousands of items to be displayed in a list.  Generates widgets dynamically for each item.

## Inheritance

`UTableViewBase`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `ItemHeight` | `float` | The height of each widget |
| `Items` | `TArray < UObject * >` | The list of items to generate widgets for |
| `SelectionMode` | `TEnumAsByte < ESelectionMode :: Type >` | The selection method for the list |
| `OnGenerateRowEvent` | `FOnGenerateRowUObject` | Called when a widget needs to be generated |

## Language

`cpp`
