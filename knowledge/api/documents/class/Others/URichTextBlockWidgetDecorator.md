---
id: "api:class:URichTextBlockWidgetDecorator"
title: "URichTextBlockWidgetDecorator"
source: "https://developer.gp.qq.com/api/class/detail/Others/URichTextBlockWidgetDecorator.json"
category: "API Wiki/class/Others"
kind: "class"
api_root: "https://developer.gp.qq.com/api/"
---

# URichTextBlockWidgetDecorator

Allows you to embed a UserWidget inline within a RichTextBlock. Configure a DataTable (row struct = FRichWidgetRow) to map tag ids to widget classes. Markup usage:  \- id : (required) Row name in the WidgetSet DataTable \- param : (optional) Arbitrary string parameter forwarded to the widget via SetWidgetParam \- width : (optional) Override width in pixels (takes precedence over DataTable value) \- height : (optional) Override height in pixels (ignored when autoHeight is true) \- autoHeight: (optional) "true""1" to let the widget's height follow its DesiredSize, width stays fixed. Overrides the DataTable's bAutoHeight flag. The created UserWidget should implement a function "SetWidgetParam(const FString&)" to receive the param string. This is called via the IWidgetParamReceiver interface or can be done in a subclass override of OnWidgetCreated.

## Inheritance

`URichTextBlockDecorator`

## Variables

| Name | Type/Value | Description |
|---|---|---|
| `WidgetSet` | `UDataTable *` | - |

## Language

`cpp`
